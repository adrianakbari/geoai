# Newsletter email list:
[peterpaul.koonings@geosquare.nl,maarten.van.der.hoek@geosquare.nl,douwe.blanksma@geosquare.nl,harco.de.jager@d2win.nl,robert@erbeegeo.nl,marlex@marlex.nl,jeroen.ticheler@geocat.com,j.deleeuw@net4s.nl,jtromp@datacollectors.net,emmanuel@digitalpathlines.ch,djoerd@giscovery.com,nalameh@lunateai.com,caroline_robinson@posteo.net,stany.luyet@ig-group.ch]
to be added: [Jsorensen@bgcengineering.ca,Wenzel@iaccess.de,W.balster@amsterdam.nl,Twm.vander.horst@zeeland.nl,Ej.leemreijze@zeeland.nl,m.kassing@swbm.de,a.weber@geogrid.ch,Francois.voisard@ne.ch]


# Target Audience More Niche
At this stage its too soon to target general "Municipality" as our target client. we need to find clients that have a problem/need/urgency.
--> who is already moving from esri
--> who cant afford esri: SMEs, real estate, contractors, construction
--> who is obliged to be sovereign and OS: see opensourcewerken.nl those organizations (PZH, MBZ, Alliander,..) are already started moving towards this
--> engineering companies who are servicing municipalities: all around europe. 
    --> those who dont have a very good developers team.


# Geosquare 
- Peter Paul Koonings
- Douwe
- Gesprek 09.09.2026
    - Goal: Ze willen aan klanten laten zien dat ze iets doen met AI. dat ze bezig zijn. 
    - Wie zijn de audience / users? Voornamelijk van Gemeenten en Utiliteit sector. 
    - Competitors van geosquare: Mapgear
    - Gebruikers dag: 
        - 180 mensen zijn aangemeld. 
        - ik kan 70 - 80 mensen verwachten voor mijn sessie
    - [Limitations] [Expertise] [people] Geonovation: 6 people 2 developers. problem with developers: old 50 years old guys who doesnt like to work with AI beacuase AI consumes a lot of energy. he doesnt like to go to the clients and talk to them. they are not pro innovation
    - [Limitations] [Expertise] [people] Onemap (Geoexperts) has 20 people where 5 dev. their issue is same as above. 
    - Other projects they are working with: FME lite bouwen: building an ETL engine. this is also where GeoAI can help.

- Gesprek met PP 24.06.2026
    - belangrijkste punt: integrate our GeoAI into their software. to have a chat widget in their front end. the chat takes the question, sends it via the api to backend and backend does the processing and manipulates the front end web viewer components in a way that visualizes the results on the web in map and on dashboard widgets and ....
    they have a conference on 27 okt that they want to show their clients that they have some kind of AI in their suite. en dan een concrete plan maken dat tot Jan of zo kan echt gerealizeerd worden en in productie gebeuren.
    - authnz moet gebeuren via hun API. welke data mag getoond worden aan welke client
    - Ideally to retrieve missing data from open source. for example our organization doesnt have PDOK or Kadaster data. when needed in a question, the AI model needs to be able to retrieve this information from external parties: PDOK, Kadaster, RIVM, ...
    - now we are building SQL queries. to work with their API, we need to be able to build API calls as well? or not we can just send the query to backend and process it there?!
    - Clients: 
        - 100 gemeentes 
        - omgevingsdienst --> meldingen (incident) worklfow
    - Use cases:
        - Geosquare and its suit helps clients transition from Esri to OS. that is an interesting use case for them. 
        - AI for helpdesk (what I though for stedin with automated reading and analyzing tickets from azure board or sap) 
        
## Peter Paul 
Founder of Geonovation. grew to 10 man. sold it to geosquare. he is the CTO of the geosquare nu. 

# Nadine Lunate AI
website: https://www.lunateai.com/
## Latest Conversation with Nadine on 31.08.2026:
- Create a Powerpoint Pitch in YC Combinator Format. and send it to her. --> then plan the next meeting. 
- Lunate can help me finding investors, initial clients and introduce me in her network. she asks for equity. 
    - [X] there is also another option that she joins the meetings and do the feedback together with me. for that she asks for equity + money. 
- [sales_intel] Sparkgeo and element 84 are losing clients becuase big organizations can do the AI development by themselves and small organizations dont have the money to pay the, 
- [Resources]
    - Carto : https://carto.com/blog/all-of-carto-in-every-agent/
    - Mapchat
    - AEC from Dubai --> Real Estate department
    - Map Africa from microsoft


# Provincie Zuid Holland
# Sep 2026
their goal: 
    - the director of water and environment siiting in a meeting. they neeed a chat bot that gives them correct actual data for decision making when they need it. for example when military sites overlap with nature and stuff
    - to shift from openAI llms to host their own models
- they officially started a project for 2 years. 7 developers are working on it. 
- Stack:
    - data bricks
    - embeddings done via AI search Index of data bricks
    - LLM: open AI
- architecture: 
    - DGGS
    - Agents --> they havent started it yet. 
    - Knowledge graphs

# June 2026
Paticipated in FOSS4G with 17 people
AI architect: Thijs oosterhuis 
AI data: Sebastiaan Schmidt
Get their challenges in their slides
"Find the right place to live " question demo
They are using openai tokens. 
They also presented in kennis kring geoai 

# Jeroen Ticheler GeoCat
## Sept 2026
Geocommons has won the funding now they have the grant available: 
https://nlnet.nl/geocommons/

## june 2026
applied for geocommons 
GeoCommons (jeroen thieler presentation)
A European incubator for geospatial open source
FOSSG EUROPE SOARA202
HorizonEuropecall HORIOO-CL6-2026-03-GOVERNANCE-06
€6M
12
90k+
EU fundingforone project
partner organisations
hours funded for the community
Coordinated by NLnet, GeoCommons sets out to cut Europe's dependence on foreign proprietary geospatial software. OSGeo is a full partner, which the European entity made possible.
Submitted and under evaluation! We hope for a positive result in summer 2026.

# EU Programs
see .\Geoai\EU
Contact Person: Stefanie
Stefanie.lumnitz@ec.europa.eu
- https://eu-mayors.ec.europa.eu/en/home
- https://business.esa.int/OpenCfPlist

# Intermediare Companies
We cant sell directly to the government. we must sell to the contractors who work for gemeente
- Tom Spoor GeoAI Agents --> Douwe
- Harco D2Win
- Jeffrey Tromp
    - omgevingbeheerders
- Sweco
- CGI
- Net4s
- Tensing
- contractors: for each use case see which contractor company is doing the work for gemeente example for fiber optic: KPN, https://www.allinq.com/, https://www.bbr-rijswijk.nl/lid-has-infra-bv, omgevingsbeheerders
- advising other companies to go soverenity: https://www.linkedin.com/in/degraafpeter/
- Ithax
- cihan

# Interim Innovators Robert Buis Markex de Jong Erik de Jonge
https://interiminnovators.nl/
Robert Buis
Marlex de Jong
Erik de Jonge
and 4 more experts

## Robert
Geo Architect met ervaring in business en business development
PWN
RWS
ATOS

## Marlex
Geo Architect met ervaring in business en business development
startups towards scale ups
founded gisspecialisten and sold it
RWS

## Services
Consultancy and coaching for geo organizations such as RWS, PWN, ...


# Vital Schreurs
industries: Government, Utilities, Retail, Banking and Insurance
years of experience: 30 years
- he has made and sold severala companies. such as GIM
- he can offer 1 thing to me: mentorship. he doesnt invest in companies pout of belgium. 
- next session: send him investor pitch. and a follow up message if he likes to coach me. 

# Octavian Borca
latest conv: we make a deal to work for success fee. each successful project he brings he will take a fee. we still need to agree on a fee. 
worked with:    swiss pot

# Net4s
Jan de Leuuw

# Aveco De Bondt
https://www.avecodebondt.nl/
find similar comanies like this: every contractor that is contracting for Gemeente
    another similar : https://www.omgevingmanager.nl/

# Jeffrey
send updates

# Gemeente Amsterdam
open data portal: 
https://kaartviewer.amsterdam.nl/dashboards/?menuId=b8320cf2-57e7-44be-90eb-a9cde3574321