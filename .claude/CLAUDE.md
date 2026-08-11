# GeoAI — Project Overview

## What This Is

GeoAI is an on-premise AI system that lets users query geospatial data using natural language. A user types "Show me all trees within 5m of roads" and the system figures out which PostGIS layers to use, plans and executes the GIS analysis, and returns the result as a map with a natural language summary.

Everything runs on a single on-premise server. No data is sent to external services.

## Architecture (5-Step Pipeline)

```
User NL Query
     ↓
Step 1 — On-Premise LLM         Ollama + Qwen3 14B (reasoning), nomic-embed-text (embeddings)
     ↓
Step 2 — Data Catalog           pgvector semantic search over all PostGIS layer metadata
     ↓
Step 3 — Query Planner          LLM → structured JSON execution plan
     ↓
Step 4 — Execution Engine       PostGIS SQL / GeoPandas / custom scripts
     ↓
Step 5 — Output Layer           MapLibre map + LLM summary + stats + export
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Application framework | Spring Boot 4 (Java 21) |
| Spatial database | PostgreSQL 17 + PostGIS (287 layers) |
| Vector search | pgvector (inside PostGIS) |
| LLM runtime | Ollama (local) |
| Reasoning model | Qwen3 14B |
| Embedding model | nomic-embed-text |
| Python backend | FastAPI |
| Frontend map | MapLibre GL JS |
| Caching | Redis |
| Tile server | Martin / pg_tileserv |

## Key Concepts

**Data Catalog** — YAML/DB entries describing every PostGIS layer (id, description, geometry type, CRS, attributes, tags, example queries). The LLM cannot know what data exists without it. Embeddings stored in pgvector enable semantic search: `user query → embed → top N relevant layers → LLM context`.

**Tools Library** — Same structure as the Data Catalog but for GIS operations (buffer, spatial_join, clip, intersect, heatmap, routing, etc.). Each tool has a pgvector embedding so the planner can semantically retrieve which tools to use.

**Execution Plan** — Structured JSON output from the LLM planner:
```json
{
  "layers": ["trees", "roads"],
  "operations": [
    { "type": "buffer", "layer": "roads", "distance_m": 5 },
    { "type": "spatial_join", "layer_a": "trees", "layer_b": "roads_buffer", "predicate": "within" }
  ],
  "output": "map + count"
}
```

**Execution Engine** — Reads the plan, routes each operation to PostGIS SQL (preferred) or GeoPandas (complex logic). Handles CRS normalization, intermediate results, row limits, and timeouts.

## Supported GIS Operations (v1 target)

Proximity: buffer, nearest_neighbor  
Overlay: intersect, clip, difference, spatial_join  
Aggregate: count, density, dissolve  
Network: routing, accessibility  
Raster: heatmap, slope, viewshed  
Filter: filter_attribute  

## Infrastructure

Single on-premise server or Hetzner GPU cloud:
- AI NPU: 50 TOPS
- GPU: Radeon 8060S graphic. 40-core RDNA 3.5 architecture
- RAM: 128GB
- CPU: AMD Ryzen™ AI Max+ 395. 16 cores / 32 threads
- Storage: 200GB NVMe SSD

## First / Target Client

**Gemeente Amstelveen** — data files are in `Gemeente_Amstelveen/`. Contains energy labels shapefile for Aalsmeer and Amstelveen, and a list of available GIS layers.

**Go-to-market**: Cannot sell directly to Dutch government. Must sell through GIS contractors who build apps for municipalities, waterschappen (water boards), and RWS:
- Sweco, CGI, Net4s, Tensing, NieuwlandGeo, Allinq

**Target sectors**: Gemeenten, Waterschappen, Rijkswaterstaat (RWS), RIVM, Stedin (utilities)

## Current Status & Roadmap

- Phase 1 (1 month, 1 VA): Business development, use case definition
- Phase 2 (2 months): Prototype — 1 fullstack AI dev + 1 VA
- Phase 3 (20 months): Production — fullstack + AI + GIS + frontend team

**Prototype scope** (~60 days, 1 mid-level Python/GIS developer):
- Week 1: Ollama + catalog YAML (5–10 layers) + tools YAML (5 tools) + pgvector setup
- Week 2: LLM planner + prompt engineering + JSON validation
- Week 3: Execution engine (5 operations via PostGIS SQL)
- Week 4: FastAPI endpoint + LLM summary + end-to-end testing

## Open TODOs

- Define 100–200 detailed sample questions a GIS analyst at a municipality would ask
- LLM chat: expose reasoning (which GIS analysis it decided to run)
- LLM chat: show the SQL query being executed
- LLM chat: better error messages
- LLM chat: let users download result data

## Files in This Repo

| File | Contents |
|------|----------|
| `geoai.md` | Full architecture, step-by-step breakdown, cost estimates |
| `geospatial_use_cases.md` | GIS use cases per sector |
| `target_clients.md` | Contacts and intermediary companies |
| `competitors.md` | Competitor research |
| `business_development.md` | BD strategy |
| `dsp.md` | DSP-related notes |
| `g_migratie.md` | Migration notes |
| `todo.md` | Current task list |
| `architecture.jpg` | Visual architecture diagram |
| `GeoAI_LLM_Setup_Guide.pdf` | LLM setup guide |
| `Gemeente_Amstelveen/` | Data and notes for Amstelveen pilot |
