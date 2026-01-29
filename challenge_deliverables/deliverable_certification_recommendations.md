# Certification Recommendations (deliverable)

## Business Scenario

A **workforce development nonprofit** is building a guided pathway for 
people transitioning into data roles. They want to recommend 
**high-signal certifications** that align with **real employer demand**, 
not just popularity.


### Source Dataset

**Databricks:** `draup_inc_global_labor_market_data_talent_intelligence_sample.role_country`\
**Accessed:** Jan 27, 2026\
**Source Last Updated** Sep 05, 2025

**Certification Rows:** 45,526\
Query: `TOTAL_CERTS` - `queries_certification_recommendations.py`

================================================================

### Task 1 - Which certifications appear most frequently for data scientists?

Frequency Table Query: `CERTS_FREQUENCY_DS` - `queries_certification_recommendations.py`\
Frequency Validation Query: `SHOW_ALL_CERTS_DS` - `queries_certification_recommendations.py`

| cert_type                     | num_certs |
|-------------------------------|-----------|
| analy_certs_ds                | 3535      |
| python_certs_ds               | 3224      |
| machine_learning_certs_ds     | 2109      |
| ai_certs_ds                   | 1967      |
| sql_certs_ds                  | 1425      |
| microsoft_certs_ds            | 1170      |
| cloud_certs_ds                | 1122      |
| aws_certs_ds                  | 768       |
| ibm_certs_ds                  | 753       |
| pwrbi_certs_ds                | 287       |
| git_certs_ds                  | 172       |


### Task 2 - Which of those align with companies that are actually hiring data scientists?

Query: `HIRING_COMPANIES_DS` - `queries_certification_recommendations.py`

| Job Role       | Company Name                                 | Job Postings Count |
|----------------|----------------------------------------------|--------------------|
| Data Scientist | Tietalent                                     | 2416 |
| Data Scientist | SynergisticIT                                 | 2103 |
| Data Scientist | Capital One Financial Corporation             | 1882 |
| Data Scientist | Jobs via Dice                                 | 1627 |
| Data Scientist | Amazon.com                                    | 1621 |
| Data Scientist | Lensa                                          | 1282 |
| Data Scientist | Google Inc.                                   | 1225 |
| Data Scientist | Deloitte                                       | 1158 |
| Data Scientist | Varsity Tutors                                | 1127 |
| Data Scientist | CVS Health Corporation                        | 1122 |
| Data Scientist | Meta Platforms, Inc.                          | 1020 |
| Data Scientist | Outlier                                       | 983  |
| Data Scientist | United States Department of the Treasury      | 822  |
| Data Scientist | Oracle Corporation                            | 769  |
| Data Scientist | Humana Inc.                                   | 745  |
| Data Scientist | Intuit                                        | 742  |
| Data Scientist | Launch Potato                                 | 711  |
| Data Scientist | PricewaterhouseCoopers                        | 694  |
| Data Scientist | TikTok                                        | 661  |
| Data Scientist | Apple Inc.                                    | 648  |

# Methodology

The business question posed the challenge of finding a way to aggregate 
certification names/types across a column where values all completely
distinct. Thus, grouping was not effective to get value counts. The next
approach involved testing various string parsing algorithms to collect 
common phrases along with their appearance counts to gauge the significance
of a certain type of certificate. This method satisfies **"which 
certifications appear most frequently?"** The word-frequency-count output
(**APPENDIX A**), was used to do string-likeness filtering in SQL to build 
a frequency table of the most common types
of certifications. There is overlap, appropriately,
because some certifications include multiple high-frequency words
such as `Microsoft` and `Machine Learning`. This step of which 
certification types to include relied heavily upon
the analyst's personal subject-matter-expertise, identifying high-frequency
words that represent valid certification types. Thus, some key strings
might have been overlooked, e.g. "Google" -- addressed below in `Discussion`.

The frequency table query `CERTS_FREQUENCY_DS` utilizes CTEs to build and
join the frequencies with string matching filters, and 
then converts the table  into a long format for better readability and 
presentation. 

NOTE: `analy_certs_ds` is named such because the string filter used was
`analy` to capture certificates including `Analytics`, `Analysis`, and 
any other variations of the word.

# Discussion

### Task 1 - Common Certs

The results show that `analysis` and `analytics` certifications are the 
most common types of certifications for data scientists. These are 
associated with other high-frequency words such as `Microsoft` and `SQL`,
(e.g. "Microsoft Certified: Data Analyst Associate" and
"Advanced SQL for Data Analysis Course")
so further analysis can filter the analytics certification types for 
frequency counts in combinations. 

Example: `LIKE '%SQL%' AND '%Analy%'` returns 162 rows)

The next highest certification type frequencies are Python and Machine
Learning, followed by AI, SQL, and Microsoft. It can be noted that 
Google returned 931 certification types, and thus would fit into the top in 
retrospect. 

### Task 2 - Hiring Companies

The list of hiring companies slightly aligns with high frequency
certification types, such as Amazon (`aws_certs_ds`) and Google. 
The top hiring companies are staffing/application portals, and 
surprisingly Capital One has a high demand for data scientists, 
but does not offer certifications, based on those included in this dataset.

Notably, Amazon (1,621 postings), Google (1,225 postings), and 
Oracle (769 postings; 1,501 certification mentions) all actively 
hire data scientists AND 
offer certifications that appear in our frequency analysis.

## Recommendations

One recommendation for data scientist clientele that want to know
which certifications to pursue, would be to seek
certifications offered by Microsoft and Google, that increase skills related
to `analysis`, `analytics`, `Python`, `SQL`, `Machine Learning`, and `AI`.

Another recommendation is to utilize the word-frequency counts list and
identify those other significant keywords that appear in many certifications
and determine if Microsoft or Google has associated certifications
for these. 

Lastly, it is recommended that a more granular analysis is pursued that
utilizes this `most_common_phrases()` output and `SQL` string combinations
to derive row counts for those certifications with overlapping
high-frequency word-counts.

# APPENDIX A

### Output - `most_common_phrases()` - `detect_common_certs.py`

[('data', 19195), ('and', 13581), ('certified', 11852), ('for', 10067), 
('with', 8199), ('in', 8186), ('python', 6961), ('learning', 6625), 
('of', 6118), ('to', 5978), ('science', 5940), ('certificate', 5712), 
('data science', 5024), ('certification', 4922), ('microsoft', 4480), 
('professional', 4335), ('sql', 4098), ('machine', 4067), 
('machine learning', 4000), ('cloud', 3890), ('the', 3789), 
('ai', 3760), ('associate', 3711), ('analytics', 3573),
('fundamentals', 3527), ('introduction', 3486), ('introduction to', 3254), 
('developer', 3100), ('business', 2895), ('management', 2872), 
('training', 2837), ('course', 2811), ('a', 2717), ('aws', 2695), 
('programming', 2679), ('advanced', 2654), ('on', 2566), ('google', 2381), 
('for data', 2293), ('analysis', 2252), ('1', 2239), ('ibm', 2208), 
('azure', 2128), ('level', 2105), ('engineer', 2065), ('r', 2033), 
('engineering', 2008), ('using', 1999), 
('foundations', 1985), ('specialist', 1878), ('development', 1799), 
('security', 1635), ('2', 1621), ('program', 1611), ('design', 1572), 
('big', 1527), ('oracle', 1501), ('intelligence', 1471), ('essentials', 1467), 
('server', 1453), ('big data', 1450), ('web', 1448), 
('with python', 1403), ('sas', 1403), 
('for data science', 1364), ('in python', 1362), ('deep', 1362), 
('power', 1360), ('java', 1354), ('project', 1339), ('database', 1336), 
('specialization', 1304), ('data analytics', 1254), ('excel', 1254), 
('master', 1244), ('by', 1211), ('microsoft certified', 1182), ('bi', 1179), 
('analyst', 1177), ('data analysis', 1147), ('architect', 1138), 
('tableau', 1136), ('deep learning', 1129), ('university', 1127), 
('foundation', 1123), ('spark', 1110), ('certified professional', 1108), 
('exam', 1095), ('bootcamp', 1095), ('administrator', 1089), 
('essential', 1062), ('google cloud', 1053), ('research', 1011), 
('solutions', 1001), ('3', 996), ('c', 994), ('sql server', 986), 
('apache', 981), ('certificate of', 977), ('complete', 967)]