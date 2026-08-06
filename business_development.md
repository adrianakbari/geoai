# Business Model
so we have 4 options: 
## 1. OEM / Technology License to GIS Software Vendors
"Embed GeoAI in your platform, serve your clients".
I give you the software. you sell it to your network. For each client you sell to, I get a cut. support and training is by you. 

Revenue structure:
  - Annual license per vendor × number of end-client deployments
  - Example: Geosquare pays €800/month per municipality they serve → 100 municipalities = €80K MRR from one contract
  - Optional: setup/integration fee (€10K–25K)

## 2. Project-Based Implementation + Annual License
"We deploy GeoAI for your client, you maintain the relationship"
you find clients for GeoAI, I implement and support. contractor gets a cut.

Revenue structure:
  - Implementation: €25K–50K per project
  - Annual license: €15K–30K/year per municipality
  - Contractor takes a margin cut (10–20%)

## 3. Reseller/Partner Program
"Certified GIS contractors sell GeoAI to their clients"
I sell GeoAI to a business. they embed and sell it to all of their clients. I charge them for 1 bulk license. 

Revenue structure:
  - Partner training fee (€2K–5K)
  - Wholesale license per deployment (contractors mark up 30–50%)
  - Annual partner fee for ongoing support

## 4. EU/Grant-Funded Research + Commercializatio
"Get funded to prove the product, then license it"

  How it works: Use GeoCommons (Jeroen Ticheler, €6M EU call), ESA BIC, or Dutch innovation grants to fund prototype development. Use the funded pilot as a reference case to license commercially.

  Revenue structure: Grant income (non-dilutive) → commercial license revenue post-grant

Suggested Pricing Architecture

  ┌────────────────┬──────────────────────────┬──────────────────────────────────────────────────┬───────────────────────────┐
  │      Tier      │           Who            │                       What                       │           Price           │
  ├────────────────┼──────────────────────────┼──────────────────────────────────────────────────┼───────────────────────────┤
  │ Pilot          │ First vendor/contractor  │ 3-month trial, 1 municipality, limited layers    │ €0 or €5K (cost-recovery) │
  ├────────────────┼──────────────────────────┼──────────────────────────────────────────────────┼───────────────────────────┤
  │ OEM Starter    │ GIS software vendor      │ API license, up to 10 municipality deployments   │ €2,500/month              │
  ├────────────────┼──────────────────────────┼──────────────────────────────────────────────────┼───────────────────────────┤
  │ OEM Growth     │ GIS software vendor      │ API license, up to 50 deployments                │ €8,000/month              │
  ├────────────────┼──────────────────────────┼──────────────────────────────────────────────────┼───────────────────────────┤
  │ OEM Enterprise │ Large vendor (Geosquare) │ Unlimited deployments + custom model fine-tuning │ €15K–25K/month            │
  ├────────────────┼──────────────────────────┼──────────────────────────────────────────────────┼───────────────────────────┤
  │ Direct Project │ Contractor per project   │ On-premise deployment + 1-year support           │ €30K + €20K/year          │
  └────────────────┴──────────────────────────┴──────────────────────────────────────────────────┴───────────────────

# Monitization of GeoAI
How much should I sell my product? 

## How much does it cost me? 
### Development Cost
- my hours: 2x8hrsx4weeks = 64 hrs/m
- Full time engineer1 (soheil): 1650 e/m
- Full time backup engineer: 4000 e/m
- Licenses: 2000 e/m
- Hardware: 3000 e one-off
- Lawyer: 3000 e one-off
- Buffer: 50%
======== 21000 e/m x 3 + 3000 + 3000 = 67500 for 3 months total

### Implementation Cost
- Implementation
- Support
- Training
- Business Developer (Octavian Fee) = to be defined in percentage.
for a new client, downloading their data, indexing and bug fixing and support i consider 1 - 2 weeks time. 


## How much time/cost does it save from the client? 
to be defined

## How much are the competitors selling?
to be defined

## Income Split
50% of the revenue from licenses
25% from Implementation
15% from support
10% from training

# Tiers
** Look at the architecture diagram. each circle should be sold as a seperated module with seperated license
## Free tier Open-Source
This is our contribution to the open-source community. 
This is also our marketing strategy. Instead of spending money on marketing. we spend money on OS version and get credability and users. 

## Tier 1:
[temporary raw estimation. number sto be changed later] Up to 10 users. ~ 10k per year

## Tier 2:
[temporary raw estimation. number sto be changed later]. up to 20 users. ~ 20k per year

## Tier 3: 
[temporary raw estimation. number sto be changed later]. up to 50 users. ~ 50k per year

# GeoAI Business Development Framework
This framework fits in nicely with CRM, Sales Intel, OSINT. 

## Flowchart

Find organization --> research whats this organization is responsible for? i.e. management of utility assets -> whats their vision? i.e Green Vision 2028 or Energie Transitie --> What regulations, rules and policies affect them? i.e. zero emission until 2026, EUDR --> check their (previous) tenders: if found, what is it for? --> check their competitors or similar companies: what projects, visions, regulations, etc do they have? what about their tenders? --> find their pain points (money, time, hr, technology, etc...) --> research how they are solving their issues now --> find their contractors (blogs, tender portals, etc) --> Make a cost estimation (time, money, hr, technology and licensing of their current solution) --> find a better solution --> find key decission makers in their org . --> create a personalized message.--> approach them  