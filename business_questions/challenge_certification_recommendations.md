## **Business Question 1**

### **“Which certifications should we recommend first for entry-level data scientist candidates?”**

**Scenario**  

A **workforce development nonprofit** is building a guided pathway for people transitioning into data roles. They want to recommend **high-signal certifications** that align with **real employer demand**, not just popularity.

**Business Ask**  
For a selected role (e.g., _Data Analyst_ or _Data Engineer_) in the U.S.:
- Which certifications appear most frequently?
- Which of those align with companies that are actively hiring?

**Datasets Used**
- `certs_licenses.csv`
- `company_num_postings.csv`

**Core SQL Tasks Exercised**
- Filtering by role and country
- Aggregations (`COUNT`)
- `GROUP BY`, `ORDER BY`
- Simple joins
- De-duplication logic

**Expected Deliverable**
- `certification_recommendations.md`
    - Ranked list of certifications
    - Short interpretation (“why these matter”)

