# GeoAI Sample Questions — Gemeente Amstelveen / Aalsmeer

100 example queries a GIS analyst at Gemeente Amstelveen might ask.  
Organized by theme. Each question is in Dutch first, English below.  
Data sources referenced are from the layers in `gementee_amstelveen_layers.txt.

---

## 1. Energie & Energielabels
*Layers: ENERGIE_Energielabels_def, energielabels_amstelveen, energielabels_aalsmeer, energie_zonnepanelen, energie_zonnedakje, Thermische_panden_mediaan, Warmtenet_Eneco, Alliander_Kabel, energie_indicatoren, ENG_gas, Beschikbare_ruimte_panelen*

| # | Nederlands                                                                                 | English |
|---|--------------------------------------------------------------------------------------------|---------|
| 1 | [demo] Toon alle panden met energielabel A++ of beter                                      | Show all buildings with energy label A++ or better |
| 2 | Welke panden in wijk Bankras hebben nog energielabel F of G?                               | Which buildings in Bankras district still have energy label F or G? |
| 3 | Geef het gemiddeld energielabel per wijk in Amstelveen                                     | Give the average energy label per district in Amstelveen |
| 4 | Hoeveel panden hebben al zonnepanelen geïnstalleerd?                                       | How many buildings already have solar panels installed? |
| 5 | [demo] Welke daken hebben de hoogste zonnepanelen-potentie in Aalsmeer?                    | Which rooftops have the highest solar panel potential in Aalsmeer? |
| 6 | Toon panden die zijn aangesloten op het warmtenet van Eneco                                | Show buildings connected to the Eneco district heating network |
| 7 | [demo] Welke panden zijn nog niet opgenomen in het energielabelregister?                   | Which buildings are not yet included in the energy label register? |
| 8 | [demo] Welke panden verliezen het meeste warmte volgens de thermische opnames?             | Which buildings lose the most heat according to thermal surveys? |
| 9 | [demo] Welke panden in Amstelveen zijn geschikt voor zonnepanelen maar hebben ze nog niet? | Which buildings in Amstelveen are suitable for solar panels but don't have them yet? |
| 10 | Vergelijk het aandeel energielabel A-woningen per wijk voor 2024                          | Compare the share of energy label A homes per district for 2024 |

from linkedin:
Energietransitie
 Waar liggen de warmtenetten? 
 Waar staan de laadpalen?, de transformatorhuisjes?, de zonnepanelen op daken? 
 Welke kabels en leidingen liggen er in de ondergrond? 
 Waar is ruimte voor nieuwe energie-infrastructuur en waar botst dat met andere belangen?
 
---

## 2. Bomen
*Layers: BOR_GV_Bomen, BOR_GV_Bomen_amstelveen, BOR_GV_Bomen_aalsmeer, BOR_BOMEN_2024_VELLEN_AVEEN, BOR_BOMEN_HERPLANT_2023, BOR_Waardevolle_bomen_ASV_25, BOR_GV_Waardevolle_bomen_Aalsmeer, bgt_vgo_bomen*

| # | Nederlands                                                           | English |
|---|----------------------------------------------------------------------|---------|
| 11 | Toon alle bomen die in 2024 gekapt zijn in Amstelveen                | Show all trees felled in Amstelveen in 2024 |
| 12 | Welke bomen zijn aangewezen als waardevol in Aalsmeer?               | Which trees are designated as valuable in Aalsmeer? |
| 13 | Hoeveel bomen zijn er herplant na kap in 2023?                                                               | How many trees were replanted after felling in 2023? |
| 14 | [gebruikersdag] [demo] Geef alle bomen die binnen 5 meter van een rioolleiding staan in de wijk heldenbuurt | Show all trees within 5 meters of a sewer pipe in Heldenbuurt neighbourhood |
| 15 | Hoeveel bomen zijn er per wijk in Amstelveen?                        | How many trees are there per district in Amstelveen? |
| 16 | Welke bomen staan binnen 50 meter van een speelterrein?              | Which trees are within 50 meters of a playground? |
| 17 | Zijn er bomen die minder dan 3 meter van een gebouw staan?           | Are there trees less than 3 meters from a building? |
| 18 | [ambigous] Toon waardevolle bomen die binnen een geluidszône vallen  | Show valuable trees that fall within a noise zone |

---

## 3. Panden & Gebouwen (BAG / BGT / WOZ)
*Layers: BAG_PDOK_PANDEN_Amstelveen, BAG_PDOK_PANDEN_Aalsmeer, WOZ_bouwlagen_pand, hoogbouw_vanaf18meter, BGT_PND, brk_gemeentelijk_eigendom, vgs_bouwdossiers*

| # | Nederlands                                                                                               | English |
|---|----------------------------------------------------------------------------------------------------------|---------|
| 19 | Geef me alle panden in wijk Amsterdamse Bos die de laatste 10 jaar zijn gebouwd                          | Show me all buildings in the Amsterdamse Bos district built in the last 10 years |
| 20 | [demo] Hoeveel panden in Amstelveen hebben meer dan 5 bouwlagen?                                         | How many buildings in Amstelveen have more than 5 floors? |
| 21 | Wat is de gemiddelde bouwjaar van panden per wijk?                                                       | What is the average construction year of buildings per district? |
| 22 | Toon alle panden in gemeentelijk eigendom in Aalsmeer                                                    | Show all buildings in municipal ownership in Aalsmeer |
| 23 | [demo] Welke panden zijn gebouwd vóór 1945 en hebben nog geen renovatievergunning?                       | Which buildings were built before 1945 and have no renovation permit yet? |
| 24 | Toon alle hoogbouw (vanaf 18 meter) in Amstelveen                                                        | Show all high-rise buildings (18 meters and above) in Amstelveen |
| 25 | Hoeveel verblijfsobjecten (VBO's) zijn er per postcode in Amstelveen?                                    | How many dwelling objects (VBOs) are there per postcode in Amstelveen? |
| 26 | [ambigous][data enginnering needed] Welke panden hebben een bouwdossier geopend in de afgelopen 2 jaar? | Which buildings have had a construction file opened in the last 2 years? |

---

## 4. Parkeren
*Layers: Parkeerplaatsen_ASV, Parkeren_Aalsmeer, BOR_PARKEERMETING_2023/2024/2025_ASV, BOR_PARKEERMETING_BUURT_ASV, parkeerautomaat, parkeerlocaties, Parkeren_vergunningsgebieden*

| # | Nederlands                                                                      | English |
|---|---------------------------------------------------------------------------------|---------|
| 27 | [gis ops: geocoding] Waar zijn de parkeerplaatsen in Amstelveen?                | Where are the parking spots in Amstelveen? |
| 28 | [ambigous] In welke wijken is de parkeerdruk in 2024 het hoogst?                | In which districts is parking pressure highest in 2024? |
| 29 | [ambigous] Vergelijk de parkeerdruk per buurt in 2023, 2024 en 2025             | Compare parking pressure per neighbourhood in 2023, 2024 and 2025 |
| 30 | [gis ops: geocoding] Toon alle parkeerautomaten in Amstelveen                   | Show all parking meters in Amstelveen |
| 31 | [ambogious] Welke parkeervergunningsgebieden hebben de laagste bezettingsgraad? | Which parking permit zones have the lowest occupancy rate? |
| 32 | Hoeveel parkeerplaatsen zijn er per wijk in Amstelveen?                         | How many parking spots are there per district in Amstelveen? |
| 33 | Toon de parkeerlocaties in Aalsmeer                                             | Show the parking locations in Aalsmeer |

---

## 5. Groen & Maaibeheer
*Layers: BOR_GV_Groen, BOR_Groen_MaaienMN_ASV, Hoofdgroenstructuur_ASV, wijkgroenstructuur_ASV, wijkgroenstructuur_AMR, parken_amstelveen, GV_GROEN*

| # | Nederlands                                                                                   | English |
|---|----------------------------------------------------------------------------------------------|---------|
| 34 | [not in database] Toon alle groengebieden die dit seizoen gemaaid moeten worden              | Show all green areas scheduled to be mowed this season |
| 35 | [demo][instructions needed] Welke groengebieden liggen binnen 100 meter van een basisschool? | Which green areas are within 100 meters of a primary school? |
| 36 | Wat is de totale oppervlakte groen per wijk in Amstelveen?                                   | What is the total green area per district in Amstelveen? |
| 37 | Toon de hoofdgroenstructuur van Amstelveen                                                   | Show the main green structure of Amstelveen |
| 38 | [demo] Welke parken liggen binnen de bebouwde kom van Amstelveen?                            | Which parks are within the built-up area of Amstelveen? |
| 39 | [data does not exist: create or fetch]Toon groene zones die direct grenzen aan waterpartijen | Show green zones that directly border water bodies |
| 40 | [data engineering needed] Hoeveel vierkante meter groen is er per inwoner per wijk?          | How many square meters of green space are there per resident per district? |

---

## 6. Geluid & Milieu
*Layers: Geluidskaart_2022_AA, NEN_geluidkaart22_amstelveen, NEN_geluidkaart22_aalsmeer, Luchtvaart_Contouren_Lden/Lnight, Wegverkeerslawaai_Contouren, Railverkeerslawaai_Tram_Contouren, Industrie_Contouren, Geluidskaart_zonebesluiten*

| # | Nederlands                                                                                           | English |
|---|------------------------------------------------------------------------------------------------------|---------|
| 41 | [demo] Welke woningen liggen binnen de geluidszône Lden > 55 dB van Schiphol?                        | Which homes are within the Schiphol Lden > 55 dB noise zone? |
| 42 | Toon panden die te maken hebben met zowel wegverkeerslawaai als industriegeluid                      | Show buildings affected by both road traffic noise and industrial noise |
| 43 | [demo] Welke scholen in Aalsmeer liggen in een zone met meer dan 55 dBA wegverkeerslawaai?           | Which schools in Aalsmeer are in a zone with more than 55 dBA road traffic noise? |
| 44 | [demo] Hoeveel woningen liggen in de tramgeluidszône in Amstelveen?                                  | How many homes are in the tram noise zone in Amstelveen? |
| 45 | [data does not exists: create or fetch]In welke buurten is de geluidsnormoverschrijding het grootst? | In which neighbourhoods is the noise standard exceeded the most? |
| 46 | Toon de geluidszonebesluiten voor industriegebied Amstelveen                                         | Show the noise zone decisions for the Amstelveen industrial area |

---

## 7. Riolering & Water
*Layers: BOR_LEIDING_RIOLERING, BOR_GV_PUT_Kolken, BOR_GV_PUT_Putten, hoofdriool_leidingen_AA, BGT_KWD_Duiker, BOR_LEIDING_DRAIN, riool_gemalen_obsurv, BOR_GV_gemalen, bgt_kolken, bor_gv_water*

| # | Nederlands                                                                                       | English |
|---|--------------------------------------------------------------------------------------------------|---------|
| 47 | Toon alle rioolgemalen in Amstelveen                                                             | Show all sewage pumping stations in Amstelveen |
| 48 | [demo] Welke hoofdrioolleidingen in Aalsmeer hebben een diameter groter dan 500 mm?              | Which main sewer pipes in Aalsmeer have a diameter larger than 500 mm? |
| 49 | [instructions needed] Zijn er kolken die niet op het riool zijn aangesloten?                     | Are there drain pits that are not connected to the sewer? |
| 50 | Toon alle duikers op het grondgebied van Amstelveen                                              | Show all culverts on the territory of Amstelveen |
| 51 | [instructions needed] Welke gebieden hebben drainageleidingen naast het reguliere riool?         | Which areas have drainage pipes in addition to the regular sewer? |
| 52 | [data does not exists: create or fetch] Toon alle walbeschermingen langs het water in Amstelveen | Show all bank protections along the water in Amstelveen |

---

## 8. Brandveiligheid & OOV
*Layers: OOV_brandkranen_IFV, Brandkranen_unmatched, Brandputten, Openwater_brandkraan, 100/200/40meter_brandkraan, Explosieven, NGE-Risicogebied (all variants)*

| # | Nederlands                                                                                                                                               | English |
|---|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| 53 | Welke panden liggen meer dan 40 meter van de dichtstbijzijnde brandkraan?                                                                                | Which buildings are more than 40 meters from the nearest fire hydrant? |
| 54 | [doesnt work] [geocoding][data engineering needed: grouping nge_risico* layers] Toon alle NGE-risicogebieden (niet-gesprongen explosieven) in Amstelveen | Show all unexploded ordnance risk areas in Amstelveen |
| 55 | Zijn er bouwdossiers geopend in een NGE-risicogebied?                                                                                                    | Are there construction files opened within an unexploded ordnance risk area? |
| 56 | Welke scholen liggen binnen een explosievenrisicozone?                                                                                                   | Which schools are located within an explosive risk zone? |
| 57 | [missing data: brandweernormen] [geocoding] Hoeveel brandkranen zijn er per wijk en voldoet dat aan de brandweernorm?                                    | How many fire hydrants are there per district and does that meet fire safety standards? |

---

## 9. Speelplaatsen
*Layers: BOR_speelterreinen_ASV, BOR_speeltoestellen_ASV, BOR_speelondergrond_ASV, GV_SPEELTERREIN, GV_SPEELTOESTEL, BOR_spelen_AMR, Speelplek_AMR*

| # | Nederlands                                                                                                                           | English |
|---|--------------------------------------------------------------------------------------------------------------------------------------|---------|
| 58 | [instructions needed] Toon alle speelterreinen in Amstelveen met hun ondergrondtype                                                  | Show all playgrounds in Amstelveen with their surface type |
| 59 | [multi-hop reasoning] [chain gis ops] Welke wijken hebben geen speelterrein binnen 500 meter van woningen?                           | Which districts have no playground within 500 meters of homes? |
| 60 | Hoeveel speeltoestellen zijn er per buurt in Amstelveen?                                                                             | How many play devices are there per neighbourhood in Amstelveen? |
| 61 | [data does not exist: water - create or fetch] Welke speelplaatsen liggen direct naast een waterpartij (mogelijk veiligheidsrisico)? | Which playgrounds are directly next to a water body (possible safety risk)? |

---

## 10. Scholen & Onderwijs
*Layers: BEL_Scholen_ASV, OEW_Onderwijslocaties_adres, scholen_schoolbestuur, BIO_Leerlingen_BO_woonplaats_postcode, SZ_kinderopvanglocaties*

| # | Nederlands                                                                                | English |
|---|-------------------------------------------------------------------------------------------|---------|
| 62 | Toon alle basisscholen in Amstelveen met hun schoolbestuur                                | Show all primary schools in Amstelveen with their school board |
| 63 | [doesnt work] Welke scholen liggen meer dan 1 km van de dichtstbijzijnde school?          | Which schools are more than 1 km from the nearest school? |
| 64 | [doesnt work] Hoeveel leerlingen per postcode gaan naar het basisonderwijs in Amstelveen? | How many pupils per postcode attend primary school in Amstelveen? |
| 65 | Toon alle kinderopvanglocaties in Aalsmeer                                                | Show all childcare locations in Aalsmeer |

---

## 11. Laadpalen & Mobiliteit
*Layers: RI_Laadpalen, Fietsroutes_AMR, Fietsroutes_Hoofdroutes_AMR, OSM_Public_Transport_stop_position, BOR_Strooiroutes_AMS, verkeersborden*

| # | Nederlands                                                                | English |
|---|---------------------------------------------------------------------------|---------|
| 66 | Toon alle laadpalen voor elektrische auto's in Amstelveen                 | Show all electric vehicle charging points in Amstelveen |
| 67 | Welke wijken hebben minder dan 1 laadpaal per 500 meter?                  | Which districts have fewer than 1 charging point per 500 meters? |
| 68 | Welke OV-haltes liggen meer dan 500 meter van de dichtstbijzijnde school? | Which public transport stops are more than 500 meters from the nearest school? |
| 69 | Toon de fietsroutes in Aalsmeer inclusief de hoofdroutes                  | Show cycling routes in Aalsmeer including the main routes |
| 70 | Welke strooiroutes zijn er voor de gladheidbestrijding in Amstelveen?     | Which gritting routes are there for anti-icing in Amstelveen? |

---

## 12. Monumenten & Erfgoed
*Layers: Monumenten, Dorpsgezichten, CER_Archeologiebeleid, CER_Archeologierapporten, CER_Beeldkunst_Amstelveen, CER_Beeldkunst_Aalsmeer*

| # | Nederlands                                                                       | English |
|---|----------------------------------------------------------------------------------|---------|
| 71 | Toon alle rijks- en gemeentemonumenten in Amstelveen                             | Show all national and municipal monuments in Amstelveen |
| 72 | Welke monumenten liggen in de beschermde dorpsgezichten?                         | Which monuments are within protected village views? |
| 73 | Zijn er vergunningaanvragen ingediend voor panden in een beschermd dorpsgezicht? | Are there permit applications submitted for buildings in a protected village view? |
| 74 | Toon alle beeldkunst in de openbare ruimte van Aalsmeer                          | Show all public art in the public space of Aalsmeer |
| 75 | Welke archeologisch waardevolle gebieden overlappen met geplande bouwprojecten?  | Which archaeologically valuable areas overlap with planned construction projects? |

---

## 13. Woningen & WOZ
*Layers: WOZ_KoopHuur_Kaart, WOZ_bouwlagen_pand, BIO_Type_woningen, BIO_Woningen_eigendom, BEL_kamergewijzeverhuur_ASV, BAG_PDOK_VBO*

| # | Nederlands                                                                  | English |
|---|-----------------------------------------------------------------------------|---------|
| 76 | Welke woningen in Amstelveen zijn huurwoningen en welke koopwoningen?       | Which homes in Amstelveen are rental properties and which are owner-occupied? |
| 77 | Toon panden met de hoogste WOZ-waarde per m² per wijk                       | Show buildings with the highest WOZ value per m² per district |
| 78 | Welk type woning domineert per wijk (rijtjeshuis, appartement, vrijstaand)? | Which housing type dominates per district (terraced, apartment, detached)? |
| 79 | Hoeveel kamergewijze verhuurvergunningen zijn er in Amstelveen?             | How many room-by-room rental permits are there in Amstelveen? |
| 80 | Toon alle ligplaatsen en standplaatsen in Aalsmeer                          | Show all mooring places and pitch locations in Aalsmeer |

---

## 14. Bevolking & Demografie
*Layers: BIO_Inwoners_buurt_leeftijdsklasse, BIO_Huishoudens_samenstelling, BIO_Inkomen_Amstelveen, BIO_Werkzame_personen, BIO_Vestigingen_bedrijven*

| # | Nederlands                                                       | English |
|---|------------------------------------------------------------------|---------|
| 81 | Welke buurten hebben de meeste inwoners ouder dan 65 jaar?       | Which neighbourhoods have the most residents over 65 years old? |
| 82 | Toon de bevolkingsdichtheid per wijk in Amstelveen               | Show population density per district in Amstelveen |
| 83 | In welke wijken wonen de meeste gezinnen met kinderen?           | In which districts do the most families with children live? |
| 84 | Welke buurten hebben het hoogste gemiddeld besteedbaar inkomen?  | Which neighbourhoods have the highest average disposable income? |
| 85 | Hoe is de bevolkingsgroei per wijk verlopen tussen 2023 en 2025? | How has population growth developed per district between 2023 and 2025? |

---

## 15. Afval & Containers
*Layers: BOR_Afvalbakken_Amstelveen, BOR_Afvalbakken_aalsmeer, BOR_Containers_ASV, BOR_Afval_boven_onder_containers, bgt_afvalbakken, BOR_ophaallocatie_standplaats*

| # | Nederlands                                                        | English |
|---|-------------------------------------------------------------------|---------|
| 86 | Waar zijn de ondergrondse afvalcontainers in Amstelveen?          | Where are the underground waste containers in Amstelveen? |
| 87 | Welke adressen liggen meer dan 200 meter van een afvalcontainer?  | Which addresses are more than 200 meters from a waste container? |
| 88 | Toon de ophaallocaties voor grof vuil in Amstelveen               | Show the collection locations for bulky waste in Amstelveen |
| 89 | Welke buurt heeft de minste afvalcontainercapaciteit per inwoner? | Which neighbourhood has the least waste container capacity per resident? |

---

## 16. Honden & Losloopgebieden
*Layers: BOR_Hondenlosloopgebieden_ASV, BOR_Hondenlosloopgebieden_AMR, BOR_Hondenlosloopgebieden_AA, Losloopgebieden_amstelveen, Losloopgebieden_aalsmeer*

| # | Nederlands                                                                | English |
|---|---------------------------------------------------------------------------|---------|
| 90 | Waar mogen honden vrij loslopen in Amstelveen?                            | Where are dogs allowed to run off-leash in Amstelveen? |
| 91 | Welke hondenlosloopgebieden liggen binnen 500 meter van een speelterrein? | Which dog off-leash areas are within 500 meters of a playground? |

---

## 17. Cross-Dataset Vragen (Ruimtelijke Combinaties)
*Multiple layers combined*

| # | Nederlands                                                                                               | English |
|---|----------------------------------------------------------------------------------------------------------|---------|
| 92 | Welke panden met energielabel G liggen binnen 100 meter van het warmtenet (potentieel aansluiten)?       | Which buildings with energy label G are within 100 meters of the district heating network (potential connection)? |
| 93 | Toon bomen die in een geluidszône staan en kunnen bijdragen aan geluidsabsorptie                         | Show trees in a noise zone that can contribute to sound absorption |
| 94 | Welke speelterreinen liggen in een wijk waar meer dan 25% van de bevolking jonger dan 12 jaar is?        | Which playgrounds are in a district where more than 25% of the population is under 12 years old? |
| 95 | Combineer energielabels met WOZ-waarden: welke dure woningen hebben nog een slecht energielabel?         | Combine energy labels with WOZ values: which expensive homes still have a poor energy label? |
| 96 | Welke panden gebouwd vóór 1970, in gemeentelijk eigendom, hebben nog geen label A?                       | Which buildings built before 1970, in municipal ownership, do not yet have label A? |
| 97 | Welke adressen liggen zowel in een NGE-risicozone als in een actief bouwdossiergebied?                   | Which addresses are both in an unexploded ordnance risk zone and in an active construction file area? |
| 98 | Hoeveel zonnepaneel-geschikte daken zijn er in buurten met een gemiddeld inkomen onder €30.000?          | How many solar-panel-suitable roofs are there in neighbourhoods with an average income below €30,000? |
| 99 | Combineer parkeerdruk 2024 met bevolkingsdichtheid: welke wijken zijn het meest overbelast qua parkeren? | Combine 2024 parking pressure with population density: which districts are most overloaded in terms of parking? |
| 100 | Welke scholen liggen in een zone met zowel Schiphol-vliegtuiglawaai (Lden > 50 dB) als industriegeluid?  | Which schools are in a zone with both Schiphol aircraft noise (Lden > 50 dB) and industrial noise? |

## 18. Tijdsfilters

| # | Nederlands | English |
|---|-----------|---------|
| 101 | Toon alle bomen die in de afgelopen 2 jaar zijn geplant | Show all trees planted in the last 2 years |
| 102 | Welke bouwdossiers zijn de laatste 6 maanden geopend? | Which construction files were opened in the last 6 months? |
| 103 | Toon alle panden gebouwd tussen 1950 en 1970 | Show all buildings constructed between 1950 and 1970 |
| 104 | Welke kamergewijze verhuurvergunningen zijn dit jaar verleend? | Which room-by-room rental permits were granted this year? |
| 105 | Toon kapvergunningen die ouder zijn dan 5 jaar | Show felling permits older than 5 years |

---

## 19. Anti-Join (rijen in A zonder match in B)

| # | Nederlands | English |
|---|-----------|---------|
| 106 | Welke gekapte bomen uit 2024 hebben geen herplant-registratie? | Which trees felled in 2024 have no replanting record? |
| 107 | Welke parkeerautomaten staan niet in een vergunningsgebied? | Which parking meters are not located in a permit zone? |
| 108 | Welke monumenten hebben geen enkel bouwdossier? | Which monuments have no construction file at all? |
| 109 | Welke verblijfsobjecten hebben geen geregistreerd energielabel? | Which dwelling objects have no registered energy label? |
| 110 | Welke speelterreinen hebben geen geregistreerde speeltoestellen? | Which playgrounds have no registered play equipment? |

---

## 20. Anti-Join per Gebied (gebieden waar NIETS matcht)

| # | Nederlands | English |
|---|-----------|---------|
| 111 | Welke buurten hebben geen laadpaal binnen 300 meter van woningen? | Which neighbourhoods have no charging point within 300 meters of homes? |
| 112 | In welke wijken staat geen enkele afvalcontainer? | In which districts is there not a single waste container? |
| 113 | In welke buurten staat geen enkele waardevolle boom? | In which neighbourhoods is there not a single valuable tree? |
| 114 | Welke wijken hebben geen kinderopvanglocatie binnen 500 meter van woningen? | Which districts have no childcare location within 500 meters of homes? |

---

## 21. Sibling Union & Jaargang-vergelijking

| # | Nederlands | English |
|---|-----------|---------|
| 115 | Vergelijk het aantal gekapte bomen in 2023 en 2024 | Compare the number of trees felled in 2023 and 2024 |
| 116 | Hoeveel parkeermetingen zijn er in totaal over alle meetjaren samen? | How many parking measurements are there in total across all measurement years? |
| 117 | Toon alle bomen in Amstelveen en Aalsmeer samen | Show all trees in Amstelveen and Aalsmeer combined |
| 118 | Is de parkeerdruk in Elsrijk gestegen tussen 2023 en 2025? | Has parking pressure in Elsrijk increased between 2023 and 2025? |
| 119 | Welke buurten komen in alle drie de parkeermeting-jaren voor? | Which neighbourhoods appear in all three parking measurement years? |

---

## 22. Verandering-detectie (delta tussen jaargangen)

| # | Nederlands | English |
|---|-----------|---------|
| 120 | Welke parkeerplaatsen uit de meting van 2023 komen niet meer voor in 2025? | Which parking spots from the 2023 measurement no longer appear in 2025? |
| 121 | Welke panden zijn nieuw in het energielabelregister ten opzichte van het vorige register? | Which buildings are new in the energy label register compared to the previous register? |
| 122 | Hoeveel buurten zijn toegevoegd of verdwenen tussen de parkeermetingen van 2023 en 2025? | How many neighbourhoods were added or removed between the 2023 and 2025 parking measurements? |
| 123 | Welke bomen staan in het bestand van 2024 maar niet in de herplant van 2023? | Which trees appear in the 2024 inventory but not in the 2023 replanting file? |

---

## 23. Adres-verankering

| # | Nederlands | English |
|---|-----------|---------|
| 124 | Welke bomen staan binnen 100 meter van Dorpsstraat 5 in Aalsmeer? | Which trees are within 100 meters of Dorpsstraat 5 in Aalsmeer? |
| 125 | Toon alle afvalcontainers binnen 200 meter van Stadsplein 1 | Show all waste containers within 200 meters of Stadsplein 1 |
| 126 | Wat is de dichtstbijzijnde laadpaal bij Kerkweg 10? | What is the nearest charging point to Kerkweg 10? |
| 127 | Welke geluidszones gelden op het adres Amsterdamseweg 100? | Which noise zones apply at the address Amsterdamseweg 100? |
| 128 | Hoeveel speelterreinen liggen binnen 500 meter van Ouderkerkerlaan 20? | How many playgrounds are within 500 meters of Ouderkerkerlaan 20? |
| 129 | Welke brandkraan ligt het dichtst bij Zijdstraat 30 in Aalsmeer? | Which fire hydrant is closest to Zijdstraat 30 in Aalsmeer? |

---

## 24. Mediaan & Percentiel

| # | Nederlands | English |
|---|-----------|---------|
| 130 | Wat is de mediane WOZ-waarde per wijk? | What is the median WOZ value per district? |
| 131 | Wat is het mediane bouwjaar van panden in Aalsmeer? | What is the median construction year of buildings in Aalsmeer? |
| 132 | Wat is de mediane woonoppervlakte per buurt? | What is the median living area per neighbourhood? |
| 133 | In welke wijk is de mediane parkeerdruk het hoogst? | In which district is the median parking pressure highest? |

---

## 25. Afgeleide Klassen & Verdelingen

| # | Nederlands | English |
|---|-----------|---------|
| 134 | Toon de verdeling van panden per bouwdecennium | Show the distribution of buildings per construction decade |
| 135 | Hoeveel bomen zijn er per stamdiameter-klasse? | How many trees are there per trunk diameter class? |
| 136 | Groepeer woningen in oppervlakteklassen van 25 m² | Group homes into floor area classes of 25 m² |
| 137 | Hoeveel panden liggen per afstandsband (0–50, 50–100, 100–200 m) van het warmtenet? | How many buildings lie per distance band (0–50, 50–100, 100–200 m) from the district heating network? |
| 138 | Toon de verdeling van energielabels over alle panden | Show the distribution of energy labels across all buildings |

---

## 26. Ruimtelijke OF (disjunctieve constraints)

| # | Nederlands | English |
|---|-----------|---------|
| 139 | Welke woningen liggen in de geluidszone van Schiphol óf van de tram? | Which homes are in the noise zone of Schiphol or of the tram? |
| 140 | Toon panden die in een NGE-risicogebied of een archeologisch waardevol gebied liggen | Show buildings located in an unexploded ordnance risk area or an archaeologically valuable area |
| 141 | Welke bomen staan in een park of in de hoofdgroenstructuur? | Which trees are in a park or in the main green structure? |

---

## 27. Samengestelde Cross-Layer Berekeningen

| # | Nederlands | English |
|---|-----------|---------|
| 142 | Welke buurten hebben de meeste 65-plussers per afvalcontainer? | Which neighbourhoods have the most residents over 65 per waste container? |
| 143 | Wat is het verschil in gemiddeld energielabel tussen koop- en huurwoningen per wijk? | What is the difference in average energy label between owner-occupied and rental homes per district? |
| 144 | Welke wijken combineren hoge geluidsbelasting met weinig groenoppervlakte? | Which districts combine high noise load with little green area? |
| 145 | Hoeveel laadpalen zijn er per 1000 inwoners per wijk? | How many charging points are there per 1000 residents per district? |

---

## 28. Drie-laags Ketens

| # | Nederlands | English |
|---|-----------|---------|
| 146 | Welke panden van vóór 1960 in gemeentelijk eigendom liggen binnen een geluidszone? | Which buildings from before 1960 in municipal ownership are within a noise zone? |
| 147 | Welke huurwoningen met energielabel F of G liggen binnen 100 meter van het warmtenet? | Which rental homes with energy label F or G are within 100 meters of the district heating network? |
| 148 | Welke scholen in een NGE-risicozone hebben een actief bouwdossier? | Which schools in an unexploded ordnance risk zone have an active construction file? |
| 149 | Welke koopwoningen in een beschermd dorpsgezicht hebben geen energielabel? | Which owner-occupied homes in a protected village view have no energy label? |
| 150 | Welke waardevolle bomen staan binnen 50 meter van een rioolleiding in een wijk met hoge bevolkingsdichtheid? | Which valuable trees are within 50 meters of a sewer pipe in a district with high population density? |

---

## 29. Aggregatie per Gebied

| # | Nederlands | English |
|---|-----------|---------|
| 151 | Hoeveel bomen zijn er per wijk in Aalsmeer? | How many trees are there per district in Aalsmeer? |
| 152 | Wat is de gemiddelde oppervlakte per wijk voor gebouwen zonder energielabel? | What is the average surface per district for buildings without an energy label? |

---

## 30. Ruimtelijke Uitsluiting (niet-overlappend)

| # | Nederlands | English |
|---|-----------|---------|
| 153 | Welke parken overlappen niet met de hoofdgroenstructuur? | Which parks do not overlap the main green structure? |
| 154 | Welke groengebieden in Amstelveen liggen buiten elke geluidszone? | Which green areas in Amstelveen lie outside every noise zone? |
| 155 | Welke beschermde dorpsgezichten overlappen geen enkel NGE-risicogebied? | Which protected village views do not overlap any unexploded ordnance risk area? |
| 156 | Welke wijken in Amstelveen overlappen niet met de Schiphol-geluidscontour? | Which districts in Amstelveen do not overlap the Schiphol noise contour? |
| 157 | Welke groengebieden worden niet doorkruist door een rioolleiding? | Which green areas are not crossed by a sewer pipe? |
| 158 | Welke bebouwde-komgebieden in Aalsmeer overlappen niet met een industriegeluidszone? | Which built-up areas in Aalsmeer do not overlap an industrial noise zone? |

---

## 31. Aangrenzendheid

| # | Nederlands | English |
|---|-----------|---------|
| 159 | Welke buurten in Amstelveen grenzen direct aan de gemeente Aalsmeer? | Which neighbourhoods in Amstelveen directly border the municipality of Aalsmeer? |
| 160 | Welke parken grenzen aan de hoofdgroenstructuur? | Which parks border the main green structure? |
| 161 | Welke beschermde dorpsgezichten grenzen aan de bebouwde kom van Aalsmeer? | Which protected village views border the built-up area of Aalsmeer? |
| 162 | Welke groengebieden grenzen direct aan een park? | Which green areas directly border a park? |

---

## 32. Ruimtelijke Voorwaarde op een Identiteits-Join

| # | Nederlands | English |
|---|-----------|---------|
| 163 | Welke panden zonder energielabel liggen binnen 100 meter van het warmtenet? | Which buildings without an energy label are within 100 meters of the district heating network? |
| 164 | Welke monumenten met een bouwdossier liggen binnen een beschermd dorpsgezicht? | Which monuments with a construction file are located within a protected village view? |
| 165 | Welke verblijfsobjecten zonder energielabel liggen binnen de bebouwde kom van Amstelveen? | Which dwelling objects without an energy label are within the built-up area of Amstelveen? |
| 166 | Wat is de gemiddelde oppervlakte per wijk van panden zonder energielabel binnen de bebouwde kom? | What is the average surface area per district of buildings without an energy label within the built-up area? |
| 167 | Hoeveel panden zonder energielabel staan er per buurt binnen 200 meter van het warmtenet? | How many buildings without an energy label are there per neighbourhood within 200 meters of the district heating network? |

---

## 33. Groepsdrempels (aantal per gebied)

| # | Nederlands | English |
|---|-----------|---------|
| 168 | Welke wijken in Amstelveen bevatten meer dan 100 bomen? | Which districts in Amstelveen contain more than 100 trees? |
| 169 | Welke buurten in Amstelveen bevatten minder dan 3 speeltoestellen? | Which neighbourhoods in Amstelveen contain fewer than 3 play devices? |
| 170 | In welke wijken van Amstelveen staat geen enkele afvalcontainer? | In which districts of Amstelveen is there not a single waste container? |
---

## Notes for GeoAI System

- Questions 1–91 are **single-dataset** queries (one primary layer + possibly a wijk/buurt boundary layer).
- Questions 92–100 are **cross-dataset** queries requiring spatial joins between 2 or more layers.
- Each question can be phrased in many ways by different users. The system must understand variations such as:
  - "Amsterdamse Bos" / "amsterdamse bos" / "AmsterdamseBos" / "Amsterdamse_Bos"
  - "de laatste 10 jaar" / "gebouwd na 2015" / "jonger dan 10 jaar"
  - "toon" / "geef me" / "waar zijn" / "laat zien" / "welke"
- The system should always **show its reasoning**: which dataset it used, which query it ran, and how many results it found.
