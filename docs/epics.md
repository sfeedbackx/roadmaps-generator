**this file is constantly changing**
**NOTE**
We are going to define general stuff like and we start updating the epics with tool we will need
to fulfill our goal.
# Ref 
Road map : RM (we will use the full name only in goal)

# Goal
We need to generate a road map based on the skill that the user already learned and we use that
to create the road map customized  map with detailed : *learning time-sub topics* (we still did
not those detailed .It can change anytime)


# Flow 
1. A logged user is prompted to specify the filed of the industry the RM is about for example: (Tech 
Math Poetry).Then the topic that he is interested in and want to learned it and the user will add
his skills he knows (we hope that the skills are related to the topic choosing) we will assume
that the user will give general topics we will discus how we are going to handle this efficiently 
2. We are going using Ai with some tools(like scraping tools ...) to fetch some popular (RM-articles...) and use them a long 
side the context (skills of the user) and we start making our RM.
- We are trying to  create  RM containing Free Resources, Paid Resources Time...
3. We present the result in tree structured way with the option to presented as markdown 
- we are giving the option to download the RM as markdown or image  format.


# Basic Requirement
1. we Gui for the User 
2. we need Ai with capable to use other tools and with context (Ai agents)
3. we need data persistence : Db
4. Backend so we can run our agent and manage Db 

## Tools
those are basic .We can change them while we make our research 

```bash
Frontend: React + TypeScript + Tailwind + React Flow
Backend: FastAPI (Python)
AI: LangChain + Gemini 
Scraping: Playwright + BeautifulSoup
Database: PostgreSQL + Prisma 
Auth: Auth0
```


