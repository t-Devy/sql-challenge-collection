## **Business Question 2 (Medium · Difficulty 5/9)**
### **“Are we training people for the experience levels the market actually needs?”**

**Scenario**  
A **bootcamp provider** wants to audit whether their programs skew too junior or too senior compared to real market demand. They’re considering adjusting curriculum length and prerequisites.

**Business Ask**  
For a selected role and country:
- What does the **experience distribution** of the workforce look like?
- Which experience bands align with the **largest number of job postings**?
- Is demand concentrated at entry, mid, or senior levels?

**Datasets Used**
- `experience_dist_perc.csv`
- `company_num_postings.csv`

**Core SQL Tasks Exercised**
- Percentage interpretation
- Aggregations + filtering
- CTEs for staging logic
- Business-aligned grouping (experience bands)

**Expected Deliverable**
- `experience_alignment_analysis.md`
    - Table: experience band vs % of workforce
    - Narrative: “Where the mismatch is”
    - Optional bar chart (Power BI / Tableau optional)