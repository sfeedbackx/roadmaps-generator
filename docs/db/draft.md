```

-- CATEGORIZATION (for browsing/organization)
topics:
├── topic_id
├── title
├── parent_topic_id (FK → topics) [category hierarchy]
├── category_depth (0-3) [limit category tree depth]
└── is_category (boolean) [true = organizational, false = learnable]

-- LEARNING UNITS (actual skills)
skills:
├── skill_id
├── title
├── topic_id (FK → topics) [which category it belongs to]
├── duration
├── difficulty
└── learning_sequence_priority [0-100, determines default order]

-- LEARNING DEPENDENCIES (sequencing logic)
skill_prerequisites:
├── skill_id
├── prerequisite_skill_id
└── importance ('required', 'recommended', 'optional')
```

---

## How This Solves Your Problem

### Scenario: Generating "Web Development" Roadmap

**Step 1: Generate Category Tree** (limited depth)
```
AI generates:
Web Development (depth 0)
├── Frontend (depth 1)
├── Backend (depth 1)
└── DevOps (depth 1)

STOP at depth 1 (only 3 main categories)
```

**Step 2: Generate Skills for ALL Categories** (breadth-first)

For "Frontend": HTML, CSS, JavaScript, React (4 skills)
For "Backend": Python, Flask, SQLAlchemy, APIs (4 skills)
For "DevOps": Git, CI/CD, Deployment (3 skills)

Total: 11 skills across 3 categories

**Step 3: AI Defines Prerequisites**
Git: [] (no prerequisites)
HTML: []
CSS: [HTML]
Python: []
JavaScript: [HTML]
Flask: [Python]
React: [JavaScript]
Deployment: [Flask, React]

**Step 4: Topological Sort for Roadmap Order**

Algorithm output:
1. Git (no prereqs, high priority)
2. HTML (no prereqs)
3. CSS (requires HTML)
4. Python (no prereqs)
5. JavaScript (requires HTML)
6. Flask (requires Python)
7. React (requires JavaScript)
8. SQLAlchemy (requires Python)
9. APIs (requires Flask)
10. Deployment (requires Flask + React)

**Result**: Git appears first, even though it's in "DevOps" category!

---

## The Key Design Principle

### **Separation of Concerns**

**Categories** answer: *"How should I browse/explore topics?"*
- Tree structure
- Depth-limited (3 levels max)
- For UI navigation

**Prerequisites** answer: *"What order should I learn things?"*
- DAG (Directed Acyclic Graph)
- No depth limit (but validated for cycles)
- For roadmap sequencing

**Priority Scores** answer: *"What's foundational vs. advanced?"*
- Numerical ranking
- Git = high priority (0-10)
- Deployment = low priority (90-100)
- Breaks ties when prerequisites are equal

---

## Theoretical Algorithm: Breadth-First Category Generation

### Problem with Depth-First (Your Concern):
```
Depth-first exploration:
Web Dev → Frontend → HTML → CSS → ... → (never reaches DevOps)
```

### Solution: Breadth-First Generation

```
Level 0: Generate "Web Development"
↓
Level 1: Generate ALL immediate subtopics
  - Frontend
  - Backend
  - DevOps
  - Database
↓
Level 2: Generate skills for EACH Level 1 topic
  - Frontend: [HTML, CSS, JS, React]
  - Backend: [Python, Flask, APIs]
  - DevOps: [Git, Docker, Deploy]
  - Database: [SQL, NoSQL]
↓
STOP (categories complete, skills generated for all)
```

Link:
https://excalidraw.com/#json=TuedDRJqpqtdXaoip-VKe,aZMKtfhAaaLFAqL0w1ox1A
