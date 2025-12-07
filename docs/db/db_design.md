# Database Design

## 1. DB general architecture 
### 1.1 Two-Tier Storage Architecture
**Separation Rationale:**

1. ***BRG (Base Roadmap Group):***
    - Acts as a knowledge repository - contains validated, ``Topic`` and ``skill``
2. ***MRG (Main Roadmap Group):*** 
    - Acts as user interaction layer - contains personalized  roadmap  derivative  from ``Topic`` and ``skill``

## 2.BRG

- **general concept**:
1. each topic can become subtopic 
2. each skill has perquisites

- **key point**:
1. acyclic graph Skill A requires Skill B and B requires 





