read complete website of https://opensourcewerken.nl/. Where do you think they can help us with our GeoAI project? if there are any projects they can help us with, keep the link for me so that I can check it myself. think    deep                                                                                                                                                                                                                         
  
● web-searcher(Read opensourcewerken.nl thoroughly)
  ⎿  Done (99 tool uses · 69.2k tokens · 11m 3s)
  (ctrl+o to expand)

● This is a goldmine. Here's what matters most for GeoAI, in priority order:

  ---
  Where OpenSourceWerken Can Help GeoAI

  1. TITAAN — Most Critical Find
  The Dutch government just funded a GeoAI Foundation Model built by Het Waterschapshuis (the IT org for all Dutch waterschappen). It does automated change detection on aerial photos + AHN data.

  Why it matters for you:
  - Your target clients (waterschappen) are co-funding it — so they're already spending money on GeoAI
  - TITAAN is about image analysis; GeoAI is about NL→query execution on vector data — these are complementary, not competing
  - Explicitly designed so "small municipalities can use GeoAI without building their own" — you could position GeoAI as the NL querying layer on top of TITAAN's detections

  Action: Contact them directly
  - TITAAN project page (https://www.digitaleoverheid.nl/innovatieproject/titaan/)
  - Waterschapshuis article (https://www.hetwaterschapshuis.nl/titaan-een-gedeeld-ai-model-voor-nederlands-beeldmateriaal)
  - Email: datascience@hetwaterschapshuis.nl

  ---
  2. NL-GOV-MCP — Technical Integration Opportunity

  An open-source MCP server that connects 44 Dutch government data sources (CBS, KNMI, RDW, spatial data, etc.) to any AI assistant. Apache 2.0 license.

  Why it matters: GeoAI could consume this as a data source layer — your NL query engine routing to both PostGIS layers and national open data through MCP. Huge value-add for municipalities.

  - nlgovmcp.nl (https://www.nlgovmcp.nl/en)

  ---
  3. Funding — Three Paths, One Accessible Now

  ┌──────────────────────┬────────────┬────────────────────────────────┬───────────────────────────────────────────────────────────────────────────────┐
  │       Program        │   Amount   │             Status             │                                     Notes                                     │
  ├──────────────────────┼────────────┼────────────────────────────────┼───────────────────────────────────────────────────────────────────────────────┤
  │ SIDN Fonds Pioneers  │ up to €10K │ Open year-round                │ No consortium needed. Easiest entry point.                                    │
  ├──────────────────────┼────────────┼────────────────────────────────┼───────────────────────────────────────────────────────────────────────────────┤
  │ Innovatiebudget 2027 │ Varies     │ Next call late 2026/early 2027 │ Needs a gemeente or kennisinstelling as lead — Amstelveen could be your lever │
  ├──────────────────────┼────────────┼────────────────────────────────┼───────────────────────────────────────────────────────────────────────────────┤
  │ NLnet (new calls)    │ €5K–€50K   │ Opens Sept 3, 2026             │ Deadline Nov 3, 2026 — this is imminent                                       │
  └──────────────────────┴────────────┴────────────────────────────────┴───────────────────────────────────────────────────────────────────────────────┘

  - SIDN Fonds apply (https://www.sidnfonds.nl/aanvragen)
  - NLnet propose (https://nlnet.nl/propose/)
  - innovatiebudget@ictu.nl

  ---
  4. Atlas — Open Source GIS Viewer Used by Dutch Municipalities

  An open source GIS viewer (Gemeente Purmerend + Delta10, adopted by Utrecht and others) that follows Common Ground standards.

  Why it matters: GeoAI's MapLibre output layer could integrate with or replace Atlas's viewer component. This gives you an existing municipality install base to target.

  - VNG Atlas practical example (https://vng.nl/praktijkvoorbeelden/atlas-een-open-source-gis-viewer)

  ---
  5. Generieke Geo Componenten (Kadaster)

  Kadaster released their map components (OpenLayers + Angular) as open source in May 2026 — powering the PDOK Viewer, BAG Viewer, WOZ-waardeloket.

  Why it matters: If GeoAI needs a production-grade Dutch government map frontend, these components are battle-tested and interoperable. Could replace building MapLibre from scratch.

  - Developer blog (https://developer.overheid.nl/blog/2026/05/18/generieke-geo-componenten)
  - generiekegeocomponenten.nl (https://generiekegeocomponenten.nl/)

  ---
  6. Go-to-Market — GIBIT 2025 as a Tailwind

  The updated municipal IT procurement framework now has a mandatory open source chapter. Municipalities must "comply or explain" on open source. This means your GIS contractor targets (Sweco, CGI, Tensing) are getting RFPs
  that require them to offer open source options.

  - iBestuur GIBIT article (https://ibestuur.nl/markt-en-overheid/sectoren-en-organisaties/opensource-nieuw-hoofdstuk-in-gibit-2025)

  ---
  7. Events — Get Visible

  T-DOSE 2026 — Open source conference, June 6-7, Geldrop. Free. Call for talks is open. A GeoAI demo talk would be very well-positioned here.

  - t-dose.org/2026 (https://t-dose.org/2026/)
  - Event listing on opensourcewerken (https://opensourcewerken.nl/events/view/dbe84ad6-a54e-4774-9f35-9d07dbaf0bc2/t-dose-open-source-conferentie)

  ---
  Biggest Strategic Insight

  The Dutch government is actively funding GeoAI — but all funded projects are remote-sensing / image analysis (TITAAN, Kadaster change detection). Nobody is funding NL→PostGIS vector query (what you're building). That's the   gap. Positioning GeoAI as the missing conversational query layer on top of existing open government GeoAI infrastructure is the strongest angle for both funding applications and partnership conversations with TITAAN,
  Kadaster, and Geonovum.

  community forum: https://opensourcewerken.nl/groups/view/75fc54b2-f4bf-4e67-a931-1d5b5b4c038a/open-source-community/search?q=geo