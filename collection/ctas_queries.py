# =================================
# DataBricks Batching
# =================================

CREATE_CHALLENGE_COLLECTION = """CREATE SCHEMA IF NOT EXISTS challenges.collection;"""

COUNTRY = 'United States of America'
ROLE_LIKE = '%Data%'

# all_data_us = 44351
CNP_TABLE = "challenges.collection.company_num_postings"
COMPANY_NUM_POSTINGS = f"""
CREATE OR REPLACE TABLE {CNP_TABLE} AS
SELECT 
    job_role,
    country,
    company_name,
    job_postings_count
FROM 
    draup_inc_global_labor_market_data_talent_intelligence_sample.role_country.competitors_country_job_role
WHERE 
    country = "{COUNTRY}"
    AND job_role LIKE "{ROLE_LIKE}";
"""

# all_data_us = 106901
CL_TABLE = "challenges.collection.certs_licenses"
CERTS_LICENSES = f"""
CREATE OR REPLACE TABLE {CL_TABLE} AS
SELECT 
    job_role,
    country,
    certification_name
FROM
   draup_inc_global_labor_market_data_talent_intelligence_sample.role_country.licenses_certifications_country_job_role
WHERE 
    country = "{COUNTRY}"
    AND job_role LIKE "{ROLE_LIKE}";
"""

# all_data_us = 42
EDP_TABLE = "challenges.collection.experience_dist_perc"
EXPERIENCE_DIST_PERC = f"""
CREATE OR REPLACE TABLE {EDP_TABLE} AS
SELECT
    job_role,
    country,
    experience,
    workforce_distribution_percentage
FROM
    draup_inc_global_labor_market_data_talent_intelligence_sample.role_country.seniority_country_job_role
WHERE 
    country = "{COUNTRY}"
    AND job_role LIKE "{ROLE_LIKE}";
"""

# all_data_us = 2
TDP_TABLE = "challenges.collection.talent_demand_pay"
TALENT_DEMAND_PAY = f"""
CREATE OR REPLACE TABLE {TDP_TABLE} AS
SELECT
    job_role,
    country,
    talent_size,
    talent_demand,
    median_base_pay,
    hiring_difficulty_index
FROM 
    draup_inc_global_labor_market_data_talent_intelligence_sample.role_country.talent_metrics_country_job_role
WHERE
    country = "{COUNTRY}"
    AND job_role LIKE "{ROLE_LIKE}";
"""

# all_data_us = 38333
TE_TABLE = "challenges.collection.top_employers"
TOP_EMPLOYERS = f"""
CREATE OR REPLACE TABLE {TE_TABLE} AS
SELECT 
    job_role,
    country,
    company_name
FROM
   draup_inc_global_labor_market_data_talent_intelligence_sample.role_country.top_employers_country_job_role
WHERE
  country = "{COUNTRY}"
  AND job_role LIKE "{ROLE_LIKE}";
"""

# all_data_us = 66
IDP_TABLE = "challenges.collection.industry_dist_perc"
INDUSTRY_DIST_PERC = f"""
CREATE OR REPLACE TABLE {IDP_TABLE} AS
SELECT 
    job_role,
    country,
    industry,
    workforce_distribution_percentage
FROM
   draup_inc_global_labor_market_data_talent_intelligence_sample.role_country.vertical_split_country_job_role
WHERE
  country = "{COUNTRY}"
  AND job_role LIKE "{ROLE_LIKE}";
"""

COUNTRY = "United States of America"
ROLE_LIKE = "%Data%"

ddl_ctas_batch = [
    (CREATE_CHALLENGE_COLLECTION, None),
    (COMPANY_NUM_POSTINGS, (COUNTRY, ROLE_LIKE)),
    (CERTS_LICENSES, (COUNTRY, ROLE_LIKE)),
    (EXPERIENCE_DIST_PERC, (COUNTRY, ROLE_LIKE)),
    (TALENT_DEMAND_PAY, (COUNTRY, ROLE_LIKE)),
    (TOP_EMPLOYERS, (COUNTRY, ROLE_LIKE)),
    (INDUSTRY_DIST_PERC, (COUNTRY, ROLE_LIKE)),
]

ddl_ctas_batch_named = [
    ("create schema", CREATE_CHALLENGE_COLLECTION, None),
    ("company_num_postings", COMPANY_NUM_POSTINGS, (COUNTRY, ROLE_LIKE)),
    ("certs_licenses", CERTS_LICENSES, (COUNTRY, ROLE_LIKE)),
    ("experience_dist_perc", EXPERIENCE_DIST_PERC, (COUNTRY, ROLE_LIKE)),
    ("talent_demand_pay", TALENT_DEMAND_PAY, (COUNTRY, ROLE_LIKE)),
    ("top_employers", TOP_EMPLOYERS, (COUNTRY, ROLE_LIKE)),
    ("industry_dist_perc", INDUSTRY_DIST_PERC, (COUNTRY, ROLE_LIKE)),
]

TABLES = {
    "company_num_postings": CNP_TABLE,
    "certs_licenses": CL_TABLE,
    "experience_dist_perc": EDP_TABLE,
    "talent_demand_pay": TDP_TABLE,
    "top_employers": TE_TABLE,
    "industry_dist_perc": IDP_TABLE,
}









# =========================================