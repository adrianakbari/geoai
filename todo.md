# TODO
- Soheil
    - create Demo for gebruikers dag Geosquare: 
        - [X] an iframe with chatbox, map and table. when a question is answered , map and table are updated
        - [X] remove 3D rendering
    - [X] create website for after conference connections
    - create sample datasets for each target client and integrate framework. this is more useful for this stage rather than having questions answered 100% accurately. we need to approach clients from differnet organizations. 
    - make it work with all databases: oracle, postgres --> together with making demo for industries
    - [X] visualize the result of queries on the map. for better testing of the results.
    - Aricles: 
        - knowledge graph
        - 1 article for each step of the framework
        - article about how much cost a user saves when they use GeoAI vs proprietary software (embedding, AI tokens , etc,,,)
    - [research] Jev: https://typesafe.ai/ is it gonna make our lives better?
    - [research] OS version of grokbot or openAI astra that can do computer tasks for you
    - [test] we need to find a way to make the LLM spatially aware. for example user asks "Show all playgrounds in Amstelveen with their surface type". to answer this question the LLM goes find the playgrounds dataset in our database. then it needs to verify this data is in gemeente Amstelveen. therefore it goes and search for a column named "Gemeente" with contains a value "Amstelveen". it cant find it. So it goes to make a join of this layer with gemeente layer to see which record falls in Amstelveen. it cannot find a common key to join the tables. therefore it fails. however it could be much easier to make the LLM spatially aware in a way. so that the LLM knows this geometry falls within the boundary of geometry of Amstelveen and neighborhood X. we can mayeb add this information for each dataset in the catalogue. but is that the most efficient way of doing it? or are there other more efficient ways?  
        - How about we define the geographic boundary of the question first, and then query all the layers within that boundary? so if I ask show me all the NGE risicigebeiden in Alsmeer --> LLM needs to define the spatial boundary of the question (= bounding box of Almstelveen) and then run a spacial query on all relevant layers within that boundary and return the sum of the results. 
    - [refine] optimize query columns --> needs research
        - go through questions and define which columns needs to be returend for a handful of questions
    - [test] spatial operations improvement: now the join agent doesnt automatically recognize if an spatial join is required. it does looking for columns to join, if it cant it needs to check if operation is  possible via spatial join. also definition of spatial keywords must be defined: close by, on the side of, touching, by, ... these keywords that indicate a buffer or intersect needs to happen. the LLM doesnt associate these keywords with spatial operations. see Q 51
        - [X] apply DE-9IM model: https://en.wikipedia.org/wiki/DE-9IM
    - [X] not found results language always in English. needs to be in the same language as the chat.
    - [posted] general question: in case the first query doesnt bring any result, should we build another agent that double checks it? double chekcs selected layers, query, ...? a verifier agent
        - when a query result is ambigous, LLM asks the user for guidance. "I selected this layer did this query but I couldnt find it. help me chose the right layer and right query if you know" --> this also helps with the chat memory.
    - VM an virual nework: make he server conneciviy robust
    - [posted] admin panel
    - [Done] catalogue finds out abbreviations used in data: sends them to the admin to understand them. for example asv in our tables is abbrv. for amstelveen.
    - [X] we are entering the next phase of major features. we need to make smart plans and architecture designs. we want to keep the sql module seperated. if we need to run more geospatial analysis.
    - [X] discuss Q26 from sample questions and Q11 from feedback files. we are entering the next phase: data operaition sconversions, running qgis tools and scripts
    - [Posted] Query reliability: Queruies are c
    onsistent. no hallucinations. very reliable queries.
    
    - [Posted] data output formats: list, csv, json
    [data engineering needed] - data ambiguity: ask the user anytime it reaches a point when something is ambigious --> its done needs improvement. for Q26 from the list worked very well with the ambiguity. --> conclusion: a dedicated module/product that is expert in data engineering, ETL, cleaning is needed. 
    - [Posted] prioritize following user instructions: if the user instruct the AI to use table A and column B and run Analysis C. try its best to follow user instruction.
    - [Posted] join table specialist agent: an agent dedicated to research if two tables are joinable, if so on which key fields
    - [Posted] is it a good idea to categorize questions to 5w categories? 
        - when
        - [discuss] where --> could need geocoding, reverse geocoding, (spatial) join with another layer. where means geometry? address? see Q27 from feedback doc. Q30 from sample questions also need geocoding
        - who
        - what
        - how
    - [Posted] is it a good idea to categorize questions into:
        - simple questions
        - cross-layer questions
        - statistical question
        - gis analysis question (that run buffer, intersect or a python script that does an analysis)?
        - external question: a question where we dont have the data in our database but it can be retrieved from external databases such as national external databases. for example from PDOK and Kadaster
    - llm chat: better error handling. give more details about the errors
    - [Posted] llm chat: let us download the data
    [Stop] Think about business development. do you need to make any agents?  see Business Intel Tool X CRM in D:\web-development\knowledge-base-claude\ToDo.md
            where we going from here:
                1. chat memory 
                2. create a catalogue that index file directories and understands GIS tools
                    -> geocoding
                    -> gis python analysis scripts
                    -> organizational gis python scripts
                3. Fetch external Data when needed --> see header below External Data Sources Feature
                    -> pdok
                    -> kadaster
                4. Create private network on azure and make pc run well
                5. business development together.
    - LLM as the brain guide the (new) employee to help him find data: "where is the table that contains data bout trees to be fallen ?" or help the manager to find tables for energie labels and create a dashboard/presentation
        --> organizational crawler
    - give memory to the chat
        - cache?!
    - think about how to run python scripts for gis analysis -> org crawler
    - create a library of geospatial tools (qgis, ahck esri). LLM needs to run them when needed. 
        --> workflow chaining
    - geoai searches and finds external libraries
    - connect to ado board to get tickets and find solutions based on that. 
        - first finds out the solution itself. -> if couldnt find it,--> asks the right person for that question (admin, developer, etc), --> documents the question so that next time it doesnt need to ask the admin again. 
    - integrate provincie zuid holland
    - MCPs? do we need to design them when connecting to external services?
        - see https://github.com/sparkgeo/geo-mcp-servers vfor mcp connectors to geocoders and so
    - integrate with geolibre and collab wiht Quisheng Wu? http://web.geolibre.app/ --> geolibre is basically opensource qgis and arcgis pro. we can automate it with AI.
    

- Adrian:
    - Prepare demo for Geosquare gebruikers dag: 
        - prepare a very short summerized demo but setup links to organizations with big details specifically made for them 
            --> [after_inteviews] create QR code for Gemeente with specific use cases how GeoAI can help gemeente
            --> [after_inteviews] create QR code for utilities with specific use cases how GeoAI can help Gas, electricity, Water
    - Prepare GeoBuzz 16 & 17 Nov
        - [X] fill in website in the profile
        - tshirt
        - [X] banner 
        - talk (presentation) --> https://geobuzz.nl/mijn-sessie image + presentation
    - [X] Pitch Deck
        -> [X] send to nadine and caroline
    - Pricing: how am I going to price it?
    - [STOP] Plan taxes and Hunting trip, fashion designer, ...
    - Planning for Funding:
        - Grants --> VA
        - VCs --> VA
        - Clients
    - [after_inteviews] Create datasets for each industry we demo'ing: 1 for real estate, 1 for construction, 1 for waterschap, 1 for utility, etc...
        - identify 1 most important use case for each sector. --> comes in meeting with (GIS) consultants
            - Omgevingswet (ruimtelijke plannen) --> everybody talks about it. good use case for Germany, NL, Swiss
    - set meetings with all gqis conference leads
    - [meeting] with Florent to analyze their ocean use case
    - [meeting] with Thijs in provincie to analyze their omgevingswet use case
    - [reminder] Octavian
    - [Meeting] with Tekin: he has good connections in Stedin, Enexis, Provincie Noord Brabant, Gasunie, etc...
    - [Meeting] with all POs + Tom White in Stedin: show them the product in 15 minutes
    - [Meeting] with Thomas and demo the product to association of makelaars
    - [after_pitch_deck] [Meeting] with Caroline: show her architecture, roadmap, live demo.
    - [Meeting] with the guys from RVO from horizon matchmaking
    - [deadline_30_nov] submit abstract for https://geospatialworld.net/gwf/2027/index.php
        - Submit your abstract or write to us at papers@geospatialworldforum.org for a speaking slot. 
    - answer atlas geospatial india
    - narrow down target audience: see # Target Audience More Niche in target_clients
        - Gemeentes: VNG en Geonovum make the policies. you need to convince them. the omgevingswet is their big project. try to find a solution for that. --> deadline 2031 everything needs to be migrated to omgevings wet. problems are that its too complicated for the users and too many rules --> AI can simplify that
    - Build prototype for each use case: storingen, omgevingswet,... rather than talking about data.
        --> interview each and every gis expert, consultant, professional --> collect the flowchart of all the use cases
    - Go through CRM and message people
    - try grok bot can login to different applications and create agents and deliver sales intel and score and....
    - apply for geocommons grant: https://nlnet.nl/geocommons/
    - [X] [reminder] [sent_to_soheil_and_octavian_for_feedback] Prepare pitch for Nadine in YC Combinator format and plan the next meeting. 
    - [X] [Business_Development] EU horizon match maker: https://www.b2match.com/e/cl4-digital2026-matchmaking/components/61258
        - [X] and business developer partners: https://mail.proton.me/u/1/inbox/nY_OCGZ0tXawjYrq55J5sBMOx31eAMa5f_Ojxz2d-qfyMY_w1MgrAA0KKo45BG1INa1cYv2IXFbsQZTb8qg5lg==#category=primary
    - GeoAI Knowledge Sessions for organizations: 
        - Stedin --> Mesg Tom
        - PZH
        - Alliander
        - Net4s
        - D2Win
        --> this is our best way. get real feedback and see what their needs are. --> introduce yourself and your capabilities --> get trust and data --> Dont sell. help them find their answers and trust you.
        - Topics:
            - How can we create AI that connects to ADO board and suggests fixes? How can We automate it further to know the scritps and people ? 
            - [sovereign AI] How can we install and run open-weights model without sharing data to Copilot?   
    - [Business_Development] [agentic] [automation]: How do you know which project is an organization doing? their blogs, social media, tender portals and their job openings. normally they hire specialists for a specific project. and they explain what project they are busy right now and they have urgency.
        - [reminder] [Business_Development] Research and make a relevant demo for Geonius --> contact Jeffrey
        - complete business analyst agent: .claude\agents\business_analyst.md
        - test it on Geonius and 10 other companies. 
        - [X] send to Soheil
    - [sent_to_soheil] enrich sample questions with geographical extent and gis operations step by step breakdown
    - [engineering] research all gis tools that you have deve
    loped (Stedin, Alliander, Net4s, Sweco workflows and Python scripts). what GIS questions are they answering? what steps are they taking? if we put that logic into our GeoAI flowchart, will it be able to solve that issue? 
        - every GIS question is coming from a project
            - train an AI agent to go through list of projects of an organization and extract GIS questions, use cases, like we did for Gem Amstelveen. 
            - see if you can find any directory of GIS python scripts, fme scripts, model builders, etc from open source/ Esri /FME community
    - [Research] DGGS, Knowledge Graphs,...
        - [GeoAI_Hackathon]: give a sample data from Gemeente Amstelveen (Translated to english) how can we apply DGGS to improve Geo RAG queries and answer to our questions? 
        - Knowledge Graphs
        - Swarm Intelligence
        - Ants, Bees, Mycelium see claude chat about tribes
    - [X] Send Octavian how you can find contractors of the Municipality of Amstelveen
        - we need to make it smart and use claude agents. we can create claude agents that:
            - search all the Gemeentes in Netherlands
                - for each gemeente: search the web to find contractors for them. this includes search + ranking. see .claude\agents\find_contractors.md
                    - for each result: find their contact person
            - search all companies who have done geo projects in Netherlands similar to companies listed in https://docs.google.com/spreadsheets/d/1eYKDn65LAKHqkD9Uceqe3WZiRsc_N5AL-G25z5jbudI/edit?gid=1154661267#gid=1154661267
            - Search Linkedin posts that include trigger keywords
            - fill them all the in CRM table 
    - [BusinessDevelopment] find out comission fee for Octavian and communicate it with him
        - contact value: 15 - 20% 
        - gross margin (revenue - direct delivery costs): 25 - 35% --> less risk for me
    - [BusinessDevelopment] design the business model
        [done] - self with calude
        - with sameer
        [done] - with george
        - other successful founders in hacker building
    - after 100 questions is tested and accepted, stop: make a business development plan and agents. and then go to the next features. 
    - [Engineering] optimize query columns
        - go through questions and define which columns needs to be returend for a handful of questi
        ons
    - [BusinessDevelopment]: load existing users into sales crm database and collect intel and create personalized message for them. create agents and triggers to prepare an eamil for them after [todo] tag is changed to [tested]
    - [BusinessDevelopment]: integrate an online todo list (that soheil can have an overview of his items as well) --> every item that is marked with [done] it automatically create a post for [1. Linkedin 2. Each of the customers with a personalized approach based on our previous conversations and their unique needs] --> send it to me for review and post.
    - [BusinessDevelopment]: Business Analyst Agent: just like what i did for Gem Amstelveen, RIVM, RWS--> create an agent that goes through the website of an organization, read their projects, vision, blogs and finds out business needs and challenges for them. so that we can send a tailor made approach. 
    - go trhough the modular centcom architecture: what open source existing projects we can use to help us giving a good starting foundation?
    - [post] each item that is done post it. 
        - [X] explain the steps that the LLM takes to solve that task
        - [X] admin panel
        - [X] performance of agentic rag geo ai compared to other systems based on the charts in paper: "D:\web-development\graph-geonetwork\papers_geoAgenticRag_multi_agent_framework.pdf"
        - generate articles from "D:\web-development\graph-geonetwork\geoAgenticRag_multi_agent_framework.pdf"
    - design a researcher agent to research Github, X, technical conferences, academic papers, Linkedin and blogs to see what other developments have been used on local native LLMs. take advantage of their work
    - analyze graph geonetwork: https://github.com/oosterhuisthijs-source/graph-geonetwork/tree/main --> send to Soheil. our goal is to slowly collaborate with Thijs. maybe generate a graph geonetwork of all NGR data
    - research knowledge graph applications in geospatial/utility/gas/ electericity network --> linked data
    - workflow chaining
    - [X] Can we run a prototype on https://www.geocat.com/blog/news-1/the-inspire-geoportal-is-gone-here-s-what-we-built-instead-25 ? And put this to Stefanie?
    

# Na de gesprek met PP 24.06.2026
- belangrijkste punt: integrate our GeoAI into their software. to have a chat widget in their front end. the chat takes the question, sends it via the api to backend and backend does the processing and manipulates the front end web viewer components in a way that visualizes the results on the web in map and on dashboard widgets and ....
    they have a conference on 27 okt that they want to show their clients that they have some kind of AI in their suite. en dan een concrete plan maken dat tot Jan of zo kan echt gerealizeerd worden en in productie gebeuren.
    - authnz moet gebeuren via hun API. welke data mag getoond worden aan welke client
    - Ideally to retrieve missing data from open source. for example our organization doesnt have PDOK or Kadaster data. when needed in a question, the AI model needs to be able to retrieve this information from external parties: PDOK, Kadaster, RIVM, ...
    - now we are building SQL queries. to work with their API, we need to be able to build API calls as well? or not we can just send the query to backend and process it there?!

# Features
** [look at the new architecture]
## Data that does not exists
at some point we are going to face questions for which we dont have the data. so we need to either create data by mixing from what we have or get from external sources.
we need to find a solution for this.
probably the flow will be this:
    - can we find the exact data from any of our registered external sources? if yes find and use it
    - if no : create data by mix and match
### External Data Sources:
- Nationale Geo Register (NGR)
    - https://nationaalgeoregister.nl/geonetwork/srv/dut/catalog.search#/home
- pdok
    - https://www.pdok.nl/
- kadaster
    - https://www.kadaster.nl/zakelijk/datasets/open-datasets
- rivm open data
    - https://data.rivm.nl/meta/srv/dut/catalog.search#/home
    - https://statline.rivm.nl/portal.html?_la=nl&_catalog=RIVM
- rws open data
    - https://rijkswaterstaatdata.nl/ 
- knmi open data
    - https://dataplatform.knmi.nl/
    - https://www.knmidata.nl/open-data
- each gemeente
    - Amstelveen en Aalsmeer: https://aa.kaartviewer.nl/dataportaal/index.html?website=DataportaalAA
- each waterschap
- each provincie
    - provincie zuid holland: https://opendata.zuid-holland.nl/geonetwork/srv/dut/catalog.search#/home
- CBS Open Data
    - https://www.cbs.nl/nl-nl/zoeken?q=keyword:CBS%20open%20data
### Create Data
[to_be_defined]

## GIS Tools and Workflows
The GeoAI must have: 
1. a library of GIS tools (got from QGIS and hacked from arcgis) and inex them. so that it knows when to run each tool. what is the tool input, what is the process and what is the output. a simple example of this is geocidng and reverse geocoding
2. organizational crawler: crawls a list of directories of an organization. it finds all the python, fme and batch scripts. indexes them. keeps them in the catalogue. so that it knows for which question it needs to run those tools.
- LLM as the brain guide the (new) employee to help him find data: "where is the table that contains data bout trees to be fallen ?" or help the manager to find tables for energie labels and create a dashboard/presentation
        --> organizational crawler
- connect to ado board to get tickets and find solutions based on that. 
        - first finds out the solution itself. -> if couldnt find it,--> asks the right person for that question (admin, developer, etc), --> documents the question so that next time it doesnt need to ask the admin again.

## Chat Memory: 
so that you can keep asking questions one after each other and it remembers the context. 
