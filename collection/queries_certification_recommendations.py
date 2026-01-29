
TOTAL_CERTS="""
SELECT 
  cl.certification_name
FROM 
  certs_licenses cl
WHERE 
  job_role = 'Data Scientist'
"""
#rows: 45,526

# Frequency Table Build
CERTS_FREQUENCY_DS="""
WITH git_cert_count AS(
SELECT 
  SUM(CASE WHEN cl.certification_name LIKE '%Git%' THEN 1 ELSE 0 END) AS git_certs_ds,
  1 AS join_key
FROM 
  certs_licenses cl
WHERE
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%Git%'),

aws_cert_count AS(
  SELECT 
    SUM(CASE WHEN cl.certification_name LIKE '%AWS%' THEN 1 ELSE 0 END) AS aws_certs_ds,
    1 AS join_key
FROM 
  certs_licenses cl
WHERE
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%AWS%'
),
python_cert_count AS (
  SELECT 
    SUM(CASE WHEN cl.certification_name LIKE '%Python%' THEN 1 ELSE 0 END) AS python_certs_ds,
    1 AS join_key
FROM 
  certs_licenses cl
WHERE
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%Python%'
),
microsoft_cert_count AS (
  SELECT 
    SUM(CASE WHEN cl.certification_name LIKE '%Microsoft%' THEN 1 ELSE 0 END) AS microsoft_certs_ds,
    1 AS join_key
FROM 
  certs_licenses cl
WHERE
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%Microsoft%'
),
sql_cert_count AS (
  SELECT 
    SUM(CASE WHEN cl.certification_name LIKE '%SQL%' THEN 1 ELSE 0 END) AS sql_certs_ds,
    1 AS join_key
FROM 
  certs_licenses cl
WHERE
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%SQL%'
),
machine_learning_cert_count AS (
  SELECT 
    SUM(CASE WHEN cl.certification_name LIKE '%Machine Learning%' THEN 1 ELSE 0 END) AS machine_learning_certs_ds,
    1 AS join_key
FROM 
  certs_licenses cl
WHERE
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%Machine Learning%'
),
pwrbi_cert_count AS (
  SELECT 
    SUM(CASE WHEN cl.certification_name LIKE '%Power BI%' THEN 1 ELSE 0 END) AS pwrbi_certs_ds,
    1 AS join_key
FROM 
  certs_licenses cl
WHERE
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%Power BI%'
),
cloud_cert_count AS (
  SELECT 
    SUM(CASE WHEN cl.certification_name LIKE '%Cloud%' THEN 1 ELSE 0 END) AS cloud_certs_ds,
    1 AS join_key
FROM 
  certs_licenses cl
WHERE
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%Cloud%'
),
ai_cert_count AS (
  SELECT 
    SUM(CASE WHEN cl.certification_name LIKE '%AI%' THEN 1 ELSE 0 END) AS ai_certs_ds,
    1 AS join_key
FROM 
  certs_licenses cl
WHERE
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%AI%'
),
analytics_cert_count AS (
  SELECT 
    SUM(CASE WHEN cl.certification_name LIKE '%Analy%' THEN 1 ELSE 0 END) AS analy_certs_ds,
    1 AS join_key
FROM 
  certs_licenses cl
WHERE
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%Analy%'
),
ibm_cert_count AS (
  SELECT 
    SUM(CASE WHEN cl.certification_name LIKE '%IBM%' THEN 1 ELSE 0 END) AS ibm_certs_ds,
    1 AS join_key
FROM 
  certs_licenses cl
WHERE
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%IBM%'
),
freq_table_wide AS (
SELECT 
  gcc.git_certs_ds,
  awscc.aws_certs_ds,
  python_certs_ds,
  microsoft_certs_ds,
  sql_certs_ds,
  machine_learning_certs_ds,
  pwrbi_certs_ds,
  cloud_certs_ds,
  ai_certs_ds,
  analy_certs_ds,
  ibm_certs_ds
FROM 
  git_cert_count gcc

  JOIN aws_cert_count awscc
  ON gcc.join_key = awscc.join_key

  JOIN python_cert_count pcc
  ON awscc.join_key = pcc.join_key

  JOIN microsoft_cert_count mcc
  ON pcc.join_key = mcc.join_key

  JOIN sql_cert_count sqlcc
  ON mcc.join_key = sqlcc.join_key

  JOIN machine_learning_cert_count mlcc
  ON mcc.join_key = mlcc.join_key

  JOIN pwrbi_cert_count pbicc
  ON mlcc.join_key = pbicc.join_key

  JOIN cloud_cert_count clcc
  ON pbicc.join_key = clcc.join_key

  JOIN ai_cert_count aicc
  ON clcc.join_key = aicc.join_key

  JOIN analytics_cert_count ancc
  ON aicc.join_key = ancc.join_key

  JOIN ibm_cert_count ibmcc
  ON ancc.join_key = ibmcc.join_key),

freq_table_long AS (
  SELECT 
  gcc.git_certs_ds,
  awscc.aws_certs_ds,
  python_certs_ds,
  microsoft_certs_ds,
  sql_certs_ds,
  machine_learning_certs_ds,
  pwrbi_certs_ds,
  cloud_certs_ds,
  ai_certs_ds,
  analy_certs_ds,
  ibm_certs_ds
FROM 
  git_cert_count gcc
  JOIN aws_cert_count awscc ON gcc.join_key = awscc.join_key
  JOIN python_cert_count pcc ON awscc.join_key = pcc.join_key
  JOIN microsoft_cert_count mcc ON pcc.join_key = mcc.join_key
  JOIN sql_cert_count sqlcc ON mcc.join_key = sqlcc.join_key
  JOIN machine_learning_cert_count mlcc ON mcc.join_key = mlcc.join_key
  JOIN pwrbi_cert_count pbicc ON mlcc.join_key = pbicc.join_key
  JOIN cloud_cert_count clcc ON pbicc.join_key = clcc.join_key
  JOIN ai_cert_count aicc ON clcc.join_key = aicc.join_key
  JOIN analytics_cert_count ancc ON aicc.join_key = ancc.join_key
  JOIN ibm_cert_count ibmcc ON ancc.join_key = ibmcc.join_key
)
SELECT 
  'git_certs_ds' AS cert_type, 
   git_certs_ds AS num_certs 
FROM 
  freq_table_wide 
UNION ALL
SELECT 
  'aws_certs_ds' AS cert_type, 
   aws_certs_ds AS num_certs
FROM 
  freq_table_wide
UNION ALL
SELECT 
  'python_certs_ds' AS cert_type,
   python_certs_ds AS num_certs
FROM freq_table_wide
UNION ALL 
SELECT 
  'microsoft_certs_ds' AS cert_type,
   microsoft_certs_ds AS num_certs
FROM 
  freq_table_wide
UNION ALL 
SELECT 
  'sql_certs_ds' AS cert_type,
   sql_certs_ds AS num_certs
FROM 
  freq_table_wide
UNION ALL  
SELECT 
  'machine_learning_certs_ds' AS cert_type,
   machine_learning_certs_ds AS num_certs
FROM 
  freq_table_wide
UNION ALL
SELECT 
  'pwrbi_certs_ds' AS cert_type,
   pwrbi_certs_ds AS num_certs
FROM 
  freq_table_wide
UNION ALL 
SELECT 
  'cloud_certs_ds' AS cert_type,
   cloud_certs_ds AS num_certs
FROM freq_table_wide
UNION ALL 
SELECT 
  'ai_certs_ds' AS cert_type,
   ai_certs_ds AS num_certs
FROM 
  freq_table_wide
UNION ALL 
SELECT 
  'analy_certs_ds' AS cert_type,
   analy_certs_ds AS num_certs
FROM 
  freq_table_wide
UNION ALL 
SELECT 
  'ibm_certs_ds' AS cert_type,
   ibm_certs_ds AS num_certs
FROM 
  freq_table_wide
ORDER BY 
  num_certs DESC;
"""

# Validation Query
SHOW_ALL_CERTS_DS="""
SELECT 
  cl.certification_name
FROM 
  certs_licenses cl
WHERE 
  job_role = 'Data Scientist'
  AND cl.certification_name LIKE '%Microsoft%'
"""
# the LIKE string was rotated for all noteworthy keywords for row count validation


HIRING_COMPANIES_DS="""
SELECT
  job_role,
  company_name,
  job_postings_count
FROM 
  company_num_postings
WHERE 
  job_role = 'Data Scientist'
ORDER BY
  job_postings_count DESC
LIMIT 20;
"""