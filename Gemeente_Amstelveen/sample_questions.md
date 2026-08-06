# GeoAI Sample Questions — Gemeente Amstelveen / Aalsmeer

100 example queries a GIS analyst at Gemeente Amstelveen might ask.  
Organized by theme. Each question is in Dutch first, English below.  
Data sources referenced are from the layers in `gementee_amstelveen_layers.txt`.

---

## 1. Energie & Energielabels
*Layers: ENERGIE_Energielabels_def, energielabels_amstelveen, energielabels_aalsmeer, energie_zonnepanelen, energie_zonnedakje, Thermische_panden_mediaan, Warmtenet_Eneco, Alliander_Kabel, energie_indicatoren, ENG_gas, Beschikbare_ruimte_panelen*

| # | Nederlands | English |
|---|-----------|---------|
| 1 | Toon alle panden met energielabel A++ of beter | Show all buildings with energy label A++ or better |
| 2 | Welke panden in wijk Bankras hebben nog energielabel F of G? | Which buildings in Bankras district still have energy label F or G? |
| 3 | Geef het gemiddeld energielabel per wijk in Amstelveen | Give the average energy label per district in Amstelveen |
| 4 | Hoeveel panden hebben al zonnepanelen geïnstalleerd? | How many buildings already have solar panels installed? |
| 5 | Welke daken hebben de hoogste zonnepanelen-potentie in Aalsmeer? | Which rooftops have the highest solar panel potential in Aalsmeer? |
| 6 | Toon panden die zijn aangesloten op het warmtenet van Eneco | Show buildings connected to the Eneco district heating network |
| 7 | Welke panden zijn nog niet opgenomen in het energielabelregister? | Which buildings are not yet included in the energy label register? |
| 8 | Welke panden verliezen het meeste warmte volgens de thermische opnames? | Which buildings lose the most heat according to thermal surveys? |
| 9 | Welke panden in Amstelveen zijn geschikt voor zonnepanelen maar hebben ze nog niet? | Which buildings in Amstelveen are suitable for solar panels but don't have them yet? |
| 10 | Vergelijk het aandeel energielabel A-woningen per wijk voor 2024 | Compare the share of energy label A homes per district for 2024 |

from linkedin:
Energietransitie
 Waar liggen de warmtenetten? 
 Waar staan de laadpalen?, de transformatorhuisjes?, de zonnepanelen op daken? 
 Welke kabels en leidingen liggen er in de ondergrond? 
 Waar is ruimte voor nieuwe energie-infrastructuur en waar botst dat met andere belangen?
 
---

## 2. Bomen
*Layers: BOR_GV_Bomen, BOR_GV_Bomen_amstelveen, BOR_GV_Bomen_aalsmeer, BOR_BOMEN_2024_VELLEN_AVEEN, BOR_BOMEN_HERPLANT_2023, BOR_Waardevolle_bomen_ASV_25, BOR_GV_Waardevolle_bomen_Aalsmeer, bgt_vgo_bomen*

| # | Nederlands | English |
|---|-----------|---------|
| 11 | Toon alle bomen die in 2024 gekapt zijn in Amstelveen | Show all trees felled in Amstelveen in 2024 |
| 12 | Welke bomen zijn aangewezen als waardevol in Aalsmeer? | Which trees are designated as valuable in Aalsmeer? |
| 13 | Hoeveel bomen zijn er herplant na kap in 2023? | How many trees were replanted after felling in 2023? |
| 14 | Geef alle bomen die binnen 5 meter van een rioolleiding staan | Show all trees within 5 meters of a sewer pipe |
| 15 | Hoeveel bomen zijn er per wijk in Amstelveen? | How many trees are there per district in Amstelveen? |
| 16 | Welke bomen staan binnen 50 meter van een speelterrein? | Which trees are within 50 meters of a playground? |
| 17 | Zijn er bomen die minder dan 3 meter van een gebouw staan? | Are there trees less than 3 meters from a building? |
| 18 | Toon waardevolle bomen die binnen een geluidszône vallen | Show valuable trees that fall within a noise zone |

---

## 3. Panden & Gebouwen (BAG / BGT / WOZ)
*Layers: BAG_PDOK_PANDEN_Amstelveen, BAG_PDOK_PANDEN_Aalsmeer, WOZ_bouwlagen_pand, hoogbouw_vanaf18meter, BGT_PND, brk_gemeentelijk_eigendom, vgs_bouwdossiers*

| # | Nederlands | English |
|---|-----------|---------|
| 19 | Geef me alle panden in wijk Amsterdamse Bos die de laatste 10 jaar zijn gebouwd | Show me all buildings in the Amsterdamse Bos district built in the last 10 years |
| 20 | Hoeveel panden in Amstelveen hebben meer dan 5 bouwlagen? | How many buildings in Amstelveen have more than 5 floors? |
| 21 | Wat is de gemiddelde bouwjaar van panden per wijk? | What is the average construction year of buildings per district? |
| 22 | Toon alle panden in gemeentelijk eigendom in Aalsmeer | Show all buildings in municipal ownership in Aalsmeer |
| 23 | Welke panden zijn gebouwd vóór 1945 en hebben nog geen renovatievergunning? | Which buildings were built before 1945 and have no renovation permit yet? |
| 24 | Toon alle hoogbouw (vanaf 18 meter) in Amstelveen | Show all high-rise buildings (18 meters and above) in Amstelveen |
| 25 | Hoeveel verblijfsobjecten (VBO's) zijn er per postcode in Amstelveen? | How many dwelling objects (VBOs) are there per postcode in Amstelveen? |
| 26 | Welke panden hebben een bouwdossier geopend in de afgelopen 2 jaar? | Which buildings have had a construction file opened in the last 2 years? |

---

## 4. Parkeren
*Layers: Parkeerplaatsen_ASV, Parkeren_Aalsmeer, BOR_PARKEERMETING_2023/2024/2025_ASV, BOR_PARKEERMETING_BUURT_ASV, parkeerautomaat, parkeerlocaties, Parkeren_vergunningsgebieden*

| # | Nederlands | English |
|---|-----------|---------|
| 27 | Waar zijn de parkeerplaatsen in Amstelveen? | Where are the parking spots in Amstelveen? |
| 28 | In welke wijken is de parkeerdruk in 2024 het hoogst? | In which districts is parking pressure highest in 2024? |
| 29 | Vergelijk de parkeerdruk per buurt in 2023, 2024 en 2025 | Compare parking pressure per neighbourhood in 2023, 2024 and 2025 |
| 30 | Toon alle parkeerautomaten in Amstelveen op de kaart | Show all parking meters in Amstelveen on the map |
| 31 | Welke parkeervergunningsgebieden hebben de laagste bezettingsgraad? | Which parking permit zones have the lowest occupancy rate? |
| 32 | Hoeveel parkeerplaatsen zijn er per wijk in Amstelveen? | How many parking spots are there per district in Amstelveen? |
| 33 | Toon de parkeerlocaties in Aalsmeer | Show the parking locations in Aalsmeer |

---

## 5. Groen & Maaibeheer
*Layers: BOR_GV_Groen, BOR_Groen_MaaienMN_ASV, Hoofdgroenstructuur_ASV, wijkgroenstructuur_ASV, wijkgroenstructuur_AMR, parken_amstelveen, GV_GROEN*

| # | Nederlands | English |
|---|-----------|---------|
| 34 | Toon alle groengebieden die dit seizoen gemaaid moeten worden | Show all green areas scheduled to be mowed this season |
| 35 | Welke groengebieden liggen binnen 100 meter van een basisschool? | Which green areas are within 100 meters of a primary school? |
| 36 | Wat is de totale oppervlakte groen per wijk in Amstelveen? | What is the total green area per district in Amstelveen? |
| 37 | Toon de hoofdgroenstructuur van Amstelveen | Show the main green structure of Amstelveen |
| 38 | Welke parken liggen binnen de bebouwde kom van Amstelveen? | Which parks are within the built-up area of Amstelveen? |
| 39 | Toon groene zones die direct grenzen aan waterpartijen | Show green zones that directly border water bodies |
| 40 | Hoeveel vierkante meter groen is er per inwoner per wijk? | How many square meters of green space are there per resident per district? |

---

## 6. Geluid & Milieu
*Layers: Geluidskaart_2022_AA, NEN_geluidkaart22_amstelveen, NEN_geluidkaart22_aalsmeer, Luchtvaart_Contouren_Lden/Lnight, Wegverkeerslawaai_Contouren, Railverkeerslawaai_Tram_Contouren, Industrie_Contouren, Geluidskaart_zonebesluiten*

| # | Nederlands | English |
|---|-----------|---------|
| 41 | Welke woningen liggen binnen de geluidszône Lden > 55 dB van Schiphol? | Which homes are within the Schiphol Lden > 55 dB noise zone? |
| 42 | Toon panden die te maken hebben met zowel wegverkeerslawaai als industriegeluid | Show buildings affected by both road traffic noise and industrial noise |
| 43 | Welke scholen in Aalsmeer liggen in een zone met meer dan 55 dBA wegverkeerslawaai? | Which schools in Aalsmeer are in a zone with more than 55 dBA road traffic noise? |
| 44 | Hoeveel woningen liggen in de tramgeluidszône in Amstelveen? | How many homes are in the tram noise zone in Amstelveen? |
| 45 | In welke buurten is de geluidsnormoverschrijding het grootst? | In which neighbourhoods is the noise standard exceeded the most? |
| 46 | Toon de geluidszonebesluiten voor industriegebied Amstelveen | Show the noise zone decisions for the Amstelveen industrial area |

---

## 7. Riolering & Water
*Layers: BOR_LEIDING_RIOLERING, BOR_GV_PUT_Kolken, BOR_GV_PUT_Putten, hoofdriool_leidingen_AA, BGT_KWD_Duiker, BOR_LEIDING_DRAIN, riool_gemalen_obsurv, BOR_GV_gemalen, bgt_kolken, bor_gv_water*

| # | Nederlands | English |
|---|-----------|---------|
| 47 | Toon alle rioolgemalen in Amstelveen | Show all sewage pumping stations in Amstelveen |
| 48 | Welke hoofdrioolleidingen in Aalsmeer hebben een diameter groter dan 500 mm? | Which main sewer pipes in Aalsmeer have a diameter larger than 500 mm? |
| 49 | Zijn er kolken die niet op het riool zijn aangesloten? | Are there drain pits that are not connected to the sewer? |
| 50 | Toon alle duikers op het grondgebied van Amstelveen | Show all culverts on the territory of Amstelveen |
| 51 | Welke gebieden hebben drainageleidingen naast het reguliere riool? | Which areas have drainage pipes in addition to the regular sewer? |
| 52 | Toon alle walbeschermingen langs het water in Amstelveen | Show all bank protections along the water in Amstelveen |

---

## 8. Brandveiligheid & OOV
*Layers: OOV_brandkranen_IFV, Brandkranen_unmatched, Brandputten, Openwater_brandkraan, 100/200/40meter_brandkraan, Explosieven, NGE-Risicogebied (all variants)*

| # | Nederlands | English |
|---|-----------|---------|
| 53 | Welke panden liggen meer dan 40 meter van de dichtstbijzijnde brandkraan? | Which buildings are more than 40 meters from the nearest fire hydrant? |
| 54 | Toon alle NGE-risicogebieden (niet-gesprongen explosieven) in Amstelveen | Show all unexploded ordnance risk areas in Amstelveen |
| 55 | Zijn er bouwdossiers geopend in een NGE-risicogebied? | Are there construction files opened within an unexploded ordnance risk area? |
| 56 | Welke scholen liggen binnen een explosievenrisicozone? | Which schools are located within an explosive risk zone? |
| 57 | Hoeveel brandkranen zijn er per wijk en voldoet dat aan de brandweernorm? | How many fire hydrants are there per district and does that meet fire safety standards? |

---

## 9. Speelplaatsen
*Layers: BOR_speelterreinen_ASV, BOR_speeltoestellen_ASV, BOR_speelondergrond_ASV, GV_SPEELTERREIN, GV_SPEELTOESTEL, BOR_spelen_AMR, Speelplek_AMR*

| # | Nederlands | English |
|---|-----------|---------|
| 58 | Toon alle speelterreinen in Amstelveen met hun ondergrondtype | Show all playgrounds in Amstelveen with their surface type |
| 59 | Welke wijken hebben geen speelterrein binnen 500 meter van woningen? | Which districts have no playground within 500 meters of homes? |
| 60 | Hoeveel speeltoestellen zijn er per buurt in Amstelveen? | How many play devices are there per neighbourhood in Amstelveen? |
| 61 | Welke speelplaatsen liggen direct naast een waterpartij (mogelijk veiligheidsrisico)? | Which playgrounds are directly next to a water body (possible safety risk)? |

---

## 10. Scholen & Onderwijs
*Layers: BEL_Scholen_ASV, OEW_Onderwijslocaties_adres, scholen_schoolbestuur, BIO_Leerlingen_BO_woonplaats_postcode, SZ_kinderopvanglocaties*

| # | Nederlands | English |
|---|-----------|---------|
| 62 | Toon alle basisscholen in Amstelveen met hun schoolbestuur | Show all primary schools in Amstelveen with their school board |
| 63 | Welke scholen liggen meer dan 1 km van de dichtstbijzijnde school? | Which schools are more than 1 km from the nearest school? |
| 64 | Hoeveel leerlingen per postcode gaan naar het basisonderwijs in Amstelveen? | How many pupils per postcode attend primary school in Amstelveen? |
| 65 | Toon alle kinderopvanglocaties in Aalsmeer | Show all childcare locations in Aalsmeer |

---

## 11. Laadpalen & Mobiliteit
*Layers: RI_Laadpalen, Fietsroutes_AMR, Fietsroutes_Hoofdroutes_AMR, OSM_Public_Transport_stop_position, BOR_Strooiroutes_AMS, verkeersborden*

| # | Nederlands | English |
|---|-----------|---------|
| 66 | Toon alle laadpalen voor elektrische auto's in Amstelveen | Show all electric vehicle charging points in Amstelveen |
| 67 | Welke wijken hebben minder dan 1 laadpaal per 500 meter? | Which districts have fewer than 1 charging point per 500 meters? |
| 68 | Welke OV-haltes liggen meer dan 500 meter van de dichtstbijzijnde school? | Which public transport stops are more than 500 meters from the nearest school? |
| 69 | Toon de fietsroutes in Aalsmeer inclusief de hoofdroutes | Show cycling routes in Aalsmeer including the main routes |
| 70 | Welke strooiroutes zijn er voor de gladheidbestrijding in Amstelveen? | Which gritting routes are there for anti-icing in Amstelveen? |

---

## 12. Monumenten & Erfgoed
*Layers: Monumenten, Dorpsgezichten, CER_Archeologiebeleid, CER_Archeologierapporten, CER_Beeldkunst_Amstelveen, CER_Beeldkunst_Aalsmeer*

| # | Nederlands | English |
|---|-----------|---------|
| 71 | Toon alle rijks- en gemeentemonumenten in Amstelveen | Show all national and municipal monuments in Amstelveen |
| 72 | Welke monumenten liggen in de beschermde dorpsgezichten? | Which monuments are within protected village views? |
| 73 | Zijn er vergunningaanvragen ingediend voor panden in een beschermd dorpsgezicht? | Are there permit applications submitted for buildings in a protected village view? |
| 74 | Toon alle beeldkunst in de openbare ruimte van Aalsmeer | Show all public art in the public space of Aalsmeer |
| 75 | Welke archeologisch waardevolle gebieden overlappen met geplande bouwprojecten? | Which archaeologically valuable areas overlap with planned construction projects? |

---

## 13. Woningen & WOZ
*Layers: WOZ_KoopHuur_Kaart, WOZ_bouwlagen_pand, BIO_Type_woningen, BIO_Woningen_eigendom, BEL_kamergewijzeverhuur_ASV, BAG_PDOK_VBO*

| # | Nederlands | English |
|---|-----------|---------|
| 76 | Welke woningen in Amstelveen zijn huurwoningen en welke koopwoningen? | Which homes in Amstelveen are rental properties and which are owner-occupied? |
| 77 | Toon panden met de hoogste WOZ-waarde per m² per wijk | Show buildings with the highest WOZ value per m² per district |
| 78 | Welk type woning domineert per wijk (rijtjeshuis, appartement, vrijstaand)? | Which housing type dominates per district (terraced, apartment, detached)? |
| 79 | Hoeveel kamergewijze verhuurvergunningen zijn er in Amstelveen? | How many room-by-room rental permits are there in Amstelveen? |
| 80 | Toon alle ligplaatsen en standplaatsen in Aalsmeer | Show all mooring places and pitch locations in Aalsmeer |

---

## 14. Bevolking & Demografie
*Layers: BIO_Inwoners_buurt_leeftijdsklasse, BIO_Huishoudens_samenstelling, BIO_Inkomen_Amstelveen, BIO_Werkzame_personen, BIO_Vestigingen_bedrijven*

| # | Nederlands | English |
|---|-----------|---------|
| 81 | Welke buurten hebben de meeste inwoners ouder dan 65 jaar? | Which neighbourhoods have the most residents over 65 years old? |
| 82 | Toon de bevolkingsdichtheid per wijk in Amstelveen | Show population density per district in Amstelveen |
| 83 | In welke wijken wonen de meeste gezinnen met kinderen? | In which districts do the most families with children live? |
| 84 | Welke buurten hebben het hoogste gemiddeld besteedbaar inkomen? | Which neighbourhoods have the highest average disposable income? |
| 85 | Hoe is de bevolkingsgroei per wijk verlopen tussen 2023 en 2025? | How has population growth developed per district between 2023 and 2025? |

---

## 15. Afval & Containers
*Layers: BOR_Afvalbakken_Amstelveen, BOR_Afvalbakken_aalsmeer, BOR_Containers_ASV, BOR_Afval_boven_onder_containers, bgt_afvalbakken, BOR_ophaallocatie_standplaats*

| # | Nederlands | English |
|---|-----------|---------|
| 86 | Waar zijn de ondergrondse afvalcontainers in Amstelveen? | Where are the underground waste containers in Amstelveen? |
| 87 | Welke adressen liggen meer dan 200 meter van een afvalcontainer? | Which addresses are more than 200 meters from a waste container? |
| 88 | Toon de ophaallocaties voor grof vuil in Amstelveen | Show the collection locations for bulky waste in Amstelveen |
| 89 | Welke buurt heeft de minste afvalcontainercapaciteit per inwoner? | Which neighbourhood has the least waste container capacity per resident? |

---

## 16. Honden & Losloopgebieden
*Layers: BOR_Hondenlosloopgebieden_ASV, BOR_Hondenlosloopgebieden_AMR, BOR_Hondenlosloopgebieden_AA, Losloopgebieden_amstelveen, Losloopgebieden_aalsmeer*

| # | Nederlands | English |
|---|-----------|---------|
| 90 | Waar mogen honden vrij loslopen in Amstelveen? | Where are dogs allowed to run off-leash in Amstelveen? |
| 91 | Welke hondenlosloopgebieden liggen binnen 500 meter van een speelterrein? | Which dog off-leash areas are within 500 meters of a playground? |

---

## 17. Cross-Dataset Vragen (Ruimtelijke Combinaties)
*Multiple layers combined*

| # | Nederlands | English |
|---|-----------|---------|
| 92 | Welke panden met energielabel G liggen binnen 100 meter van het warmtenet (potentieel aansluiten)? | Which buildings with energy label G are within 100 meters of the district heating network (potential connection)? |
| 93 | Toon bomen die in een geluidszône staan en kunnen bijdragen aan geluidsabsorptie | Show trees in a noise zone that can contribute to sound absorption |
| 94 | Welke speelterreinen liggen in een wijk waar meer dan 25% van de bevolking jonger dan 12 jaar is? | Which playgrounds are in a district where more than 25% of the population is under 12 years old? |
| 95 | Combineer energielabels met WOZ-waarden: welke dure woningen hebben nog een slecht energielabel? | Combine energy labels with WOZ values: which expensive homes still have a poor energy label? |
| 96 | Welke panden gebouwd vóór 1970, in gemeentelijk eigendom, hebben nog geen label A? | Which buildings built before 1970, in municipal ownership, do not yet have label A? |
| 97 | Welke adressen liggen zowel in een NGE-risicozone als in een actief bouwdossiergebied? | Which addresses are both in an unexploded ordnance risk zone and in an active construction file area? |
| 98 | Hoeveel zonnepaneel-geschikte daken zijn er in buurten met een gemiddeld inkomen onder €30.000? | How many solar-panel-suitable roofs are there in neighbourhoods with an average income below €30,000? |
| 99 | Combineer parkeerdruk 2024 met bevolkingsdichtheid: welke wijken zijn het meest overbelast qua parkeren? | Combine 2024 parking pressure with population density: which districts are most overloaded in terms of parking? |
| 100 | Welke scholen liggen in een zone met zowel Schiphol-vliegtuiglawaai (Lden > 50 dB) als industriegeluid? | Which schools are in a zone with both Schiphol aircraft noise (Lden > 50 dB) and industrial noise? |

---

## Notes for GeoAI System

- Questions 1–91 are **single-dataset** queries (one primary layer + possibly a wijk/buurt boundary layer).
- Questions 92–100 are **cross-dataset** queries requiring spatial joins between 2 or more layers.
- Each question can be phrased in many ways by different users. The system must understand variations such as:
  - "Amsterdamse Bos" / "amsterdamse bos" / "AmsterdamseBos" / "Amsterdamse_Bos"
  - "de laatste 10 jaar" / "gebouwd na 2015" / "jonger dan 10 jaar"
  - "toon" / "geef me" / "waar zijn" / "laat zien" / "welke"
- The system should always **show its reasoning**: which dataset it used, which query it ran, and how many results it found.
