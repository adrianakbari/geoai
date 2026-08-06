# Gemeente Amstelveen

## Contact person
Peter Paul Koonings

# Data
their open data portal: 
https://aa.kaartviewer.nl/dataportaal/index.html?website=DataportaalAA

Thema's
    Bestuur
         Officiele bekendmakingen
         Stembureaus Aalsmeer
         Stembureaus Amstelveen
         Verkiezingsuitslagen Europees Parlement, Amstelveen 2024
         Verkiezingsuitslagen gemeenteraad Aalsmeer 2022
         Verkiezingsuitslagen Provinciale Staten Noord-Holland, Aalsmeer 2023
         Verkiezingsuitslagen Provinciale Staten Noord-Holland, Amstelveen 2023
         Verkiezingsuitslagen Tweede Kamer Aalsmeer 2023
         Verkiezingsuitslagen Tweede Kamer Amstelveen 2023
    Bevolking
        ...
    Cultuur en recreatie
    Economie
    Financien
    Landbouw
    Migratie en integratie
    Natuur en milieu
    Onderwijs en wetenschap
    Openbare orde en veiligheid
    Recht
    Ruimte en infrastructuur
    Sociale zekerheid
    Verkeer
    Werk en inkomen
    Wonen
        Definitieve energielabels Aalsmeer en Amstelveen: https://aa.kaartviewer.nl/dataportaal/index.html?website=DataportaalAA&page=dataset&tab=databronnen&dataset=energielabelsdefportaalaa
    Zorg en gezondheid

# Use Case
"geef me alle panden in wijk: “Amsterdamse bos”, die de laatste 10 jaar zijn gebouwd"
to successfully answer this question the LLM needs to:
- understand this data exists in the Definitieve energielabels Aalsmeer en Amstelveen table
- create the query wijknaam = 'Amsterdamse Bos' and bouwjaar > 2000 (with variations for example 'Amsterdamse bos', 'amsterdamse bos', 'AmsterdamseBos', 'Amsterdamse_Bos')
- and return the results 

- waar men kan parkeren in Amstelveen
- https://www.nieuwlandgeo.nl/aanbeveling/van-probleem-naar-webgisapp/ 
    - grass cutting planner: grass cutting companies in a municipalities need to know which area they need to go today to plan their cut. 
    - contact person in gemeente Hugo Weijgertse. Medewerker basis-informatie (IB-BI)
    - contractor: Nieuwlandgeo
- https://www.nieuwlandgeo.nl/aanbeveling/geoportaal-gemeente-amstelveen-en-aalsmeer/
    - publish data automatically via C-Sam. Employee asks online web map "Show me all the parking data. the software can find the dataset and show it online." citizens want to know where they can park their car (static and dynamic info)
    - contact person in gemeente Hugo Weijgertse. Medewerker basis-informatie (IB-BI)
    - contractor: Nieuwlandgeo
- https://www.nieuwlandgeo.nl/aanbeveling/appsmaps-veldregistratie/
    - pest control map: a field worker goes to the location sets a trap, inputs the location of the trap on the map. next time he can easily find it. tracking. they want to see the period in which they were used, and the number of catches. they can report also damage poses problems for water flow or for the safety of the flood defence. 
    - Wilfred Meijer, Senior Pest Control Officer at Water Authority Groot Salland and Pieter Reitsma, Team Leader Water Authority Noorderzijlvest
    - contractor: Nieuwlandgeo
- https://www.nieuwlandgeo.nl/aanbeveling/appsmaps-app-metenmelden/
- https://www.nieuwlandgeo.nl/aanbeveling/joep-korting-app-meten-melden/
    - all kinds of reports, such as holes in the work path, embankment subsidence, and violations, but also the landscaping procedure and recording locations where invasive species occur. If you come across something somewhere, you record the location, take a photo if necessary, and forward the report directly to the right person. inspection
    - contact person: Joep Korting, District Boven Aa
    - contractor: Nieuwlandgeo
- https://www.nieuwlandgeo.nl/aanbeveling/c-slierendrecht-webgis-publisher/
    - task management and planning for external contractors: External agencies regularly carry out work commissioned by the municipality. These agencies are often based elsewhere in the country. Subject to conditions and with their own authorization. 
    - Charles Slierendrecht, Municipality of Maastricht
    - contractor: Nieuwlandgeo
- https://www.nieuwlandgeo.nl/aanbeveling/willem-berndsen-gemeente-den-haag-4/

## Summary
- Field maps. a municipality need to {do a task}. it needs to plan it for the {external contractor}. external contractor logs in on the field app. it sees a list of tasks it needs to do on the map. it goes and do them --> the municipality is informed. --> municipality employee logs in on the office app and checks if the work is done (checks can be automated with AI agents)
example: mowing, pest control, repair (asphalt, lights, ...), asbest, ....
- Licensing maps: criteria for a regulation needs to be controled before a license can be generated. 
example: construction, renovation, waste management, ....


## Test Queries
see Gemeente_Amstelveen\sample_questions.md
**Use Claude to write mix and match tests based on data and fields**
- Give me a list of all tables in the database, and their fields and a brief explanation about each table. 
### Queries of 1 dataset
geef me alle panden in wijk: “Amsterdamse bos”, die de laatste 10 jaar zijn gebouwd
- create a series of queries that asks information of a table
### Cross dataset queries
- create a series of queries that crosses the information among tables
    - spatial
        - intersect (later add within, touches, neighbourhood, ...)
        - buffer 
        - clip
        - statistics
    - non-spatial
--> pay attention each question can be asked in N ways by different people. Chat needs to understand all those questions in various forms and find the right answer to that
--> show the thinking process: we want the employee to see that AI is calling this query now and is querying this database now. so that it can fact check and control

When a citizen asks a questions different data sources and file formats need to be checked: 
Omgevingswet (files)
Leidraad inrichting openbare ruimte (LIOR) (files)
Duurzame bouwen (https://www.amstelveen.nl/duurzaam-bouwen)
Geo data 
And process all this data and give an answer to the user. 

# Intel
- X https://www.amstelveen.nl/projecten-en-plannen
- X https://www.amstelveen.nl/publicaties-en-regelgeving
- X https://www.amstelveen.nl/nieuws
- X https://www.amstelveen.nl/vergunningen-en-toestemming
- X https://www.amstelveen.nl/bouwen-en-wonen
- X https://www.amstelveen.nl/jeugd-en-onderwijs
- X https://www.amstelveen.nl/zorg-en-ondersteuning
- X https://www.amstelveen.nl/contact-melden-klacht-compliment
- X https://www.amstelveen.nl/afval
- X https://www.amstelveen.nl/parkeren-en-verkeer

## Projecten
### Summary
1. Maintenance
2. Vergunningen
3. Yearly inspection work
3. Citizen's Participation

### Maintenance and Repair
By far the most recurring process in Gemeente:
Construction and maintenance work: 
Highway A1 is closed from A to B. Who will be affected (services, citizens)? How to inform them? How the traffic will be diverted? How will the services continue work? I e garbage collection
Map of closures and detours: 
https://bereikbaarheid.andes.nl/amstelveen
--> the exact same thing happen with utility maintenance: Gas, water, Electra and any other maintenance. --> related to incident reporting as well. 

### Incident Management
this is directly related to maintenance flow. after each incident a maintenance flow must be started with supervision of a human admin
https://www.amstelveen.nl/contact-melden-klacht-compliment
- Citizens report an incident: make it easy via voice or text and let the chat ask relevant questions
- Report crimes. Crime analysis based on historical data, 
- Report rats and annoying animals > the flow of nuance animal management starts

### Yearly Inspection Work
GNI
yearly cleaning of rain water ways

yearly mowing the grass
    Mow less: 
    Citizens know which are they should mow and which areas are not -> they have an app for this now made by NieuwlandGeo
yearly inspection of water ways (Waterschap, Schouw)

Trees trimming: 
[Based on satellite image] which trees should be cut in this municipality? Plan it, inform the contractors, monitor the work of the contractors, archive, adjust statuses.

Pest Control:
- https://www.nieuwlandgeo.nl/aanbeveling/appsmaps-veldregistratie/
    - pest control map: a field worker goes to the location sets a trap, inputs the location of the trap on the map. next time he can easily find it. tracking. they want to see the period in which they were used, and the number of catches. they can report also damage poses problems for water flow or for the safety of the flood defence. 
    - Wilfred Meijer, Senior Pest Control Officer at Water Authority Groot Salland and Pieter Reitsma, Team Leader Water Authority Noorderzijlvest
    - contractor: Nieuwlandgeo
--> yearly cleaning of rain water ways/GNI/mowing/... : --> citizen need to be informed about moving their car, being home, leaving the garden open --> send push notifis to citizens in area A

### Vergunningen Licences Permissions
First check if I need a vergunning > then start the automated vergunning process . {Research the vergunning flow. How can we automate it?} (it depends on the type of vergunning they are asking vergunning to build is different than vergunning to organize an evcent)
> Then give a license. > Register the license for the user in a database. > Monitor and police the activity of it matches the license > people can search for given vergunningen (https://www.amstelveen.nl/bekendmaking-van-vergunningen-0)
https://www.amstelveen.nl/vergunningen-en-toestemming
https://www.amstelveen.nl/bouwen-en-wonen

Omgevingswet falls under vergunningen mostly
### Omgevingswet,  Omgevings Plannen
Het omgevingsplan bevat alle regels voor de fysieke leefomgeving op lokaal niveau. Bijvoorbeeld regels over gebouwen, grond, woningen, milieu, wegen, klimaatadaptatie, natuur en water
https://documenten.amstelveen.nl/omgevingsplan
https://iplo.nl/regelgeving/instrumenten/omgevingsplan/procedure-wijzigen-omgevingsplan/
https://omgevingswet.overheid.nl/home
Any activity a citizen or a company want to do need to be checked against the Omgevingswet. So that they know if they can do it or not. For example if you want to build a house, cut a tree, trim a tree, do something with the water, green space etc. There are many different categories of Omgevingswet (green, water, construction...) 
So the user picks a location on the map and ask the gpt can I do {my activity} here? He gets a full overview of omgevingsplan en that are relevant for that activity on that location
https://iplo.nl/digitaal-stelsel/omgevingsloket/animatie-zo-werkt-regels-op-kaart/
https://omgevingswet.overheid.nl/home

### Citizens Participation 
this is a good chance to work on digital nomads app - geo messaging - events - matchmaking
Citizens need to know where they can swim
https://www.amstelveen.nl/blauwalg-en-zwemwater
So a chatbot like app that I can ask all my questions as a citizen and get answers. 
"What are the road maintenance in my area?"
"Can I swim here?"
"When is the electricity back?"
"When is the trash being collected?" 
"Where can I dump my large trash?"
"When is the next meeting for town {event}?"
"Where can/can't I walk my dog?"
"Where can I install electric charger for my car?" What's the process? Start the flow for me. 
"How can I protect my garden from drought? Give suggestions"
"How can we protect ourselves against heat waves?
"How can I prevent water overlast? What do I do if there is water overlast?"
"Where can I go for bbq/picnic?"
"Where can I go in a hot day ? > Swim, climate park,..."
"Whats going on in the neighbourhood today? Events, heat map of population density"
"Can I build my house?" regels  voor de bouwhoogte, het uiterlijk en het gebruik van de bouwwerken.
"Can I register a company on this location?"
"Welke geluidsnormen er gelden voor mij als ondernemer?" Omgevingswet, omgevingsplan
- help each other, recycle (give articles to each other, geo chat, event (festival, concert in the neighbourhood), we are adding children swimming pools for children in the summer> add it automatically on the map and chat ("where can I find children swim places?"), map of noise, map of flood risks, 
- give me advise and subsidies voor isolation/recycling/settingup a garden... {task}
- Garbage afval: https://www.amstelveen.nl/afval
- Parking: "Where can I park my car/van?"

--> this is a good chance to work on digital nomads app - geo messaging - events - matchmaking

### Carbon Neutrality, Energietransitie
Carbon neutrality 0 emission energie transitie 
1. Solar panel feasibility map
2. Thermo fotos for analysing where the energy is wasted most. 
Thermo Fotos and energie saving
https://www.amstelveen.nl/thermische-fotos-amstelveen
By comparing thermo Fotos of 5 years intervals citizens can see how is their energy wasting compared to before. Therefore evaluate the effectiveness of their measurements and apply new measurements when possible
3. Analyse for green area: where can we have more green spaces ? 
Groen Raad - green advice 
To give advice how to make our city greener. Requires geospatial analysis to where to collect more rain water? Where we can build places for bees, insects and birds? Where can we plant more trees? 
4. Installation of electrical charges for cars > find suitable places
5. Alternatieve energy sources analyses.
6. Citizens carpooling: I am going driving to the same neighborhood for work every day, who is coming with me?

### Asielzoekers
Asielzoekers in gemeente: what are the rules? Where are the social houdings? What are their current capacity? 

### Fiber Optic Cable
Fiber optic cable for internet 
Contractors KPN, https://www.allinq.com/, https://www.bbr-rijswijk.nl/lid-has-infra-bv

