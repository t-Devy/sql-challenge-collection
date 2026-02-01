
WORKFORCE_DIST_BY_EXPERIENCE_DS = """
WITH role_band_totals AS (
SELECT
  job_role,
  CASE 
    WHEN experience BETWEEN 0 AND 5 THEN '0-5'
    WHEN experience BETWEEN 6 AND 10 THEN '6-10'
    WHEN experience BETWEEN 11 AND 15 THEN '11-15'
    WHEN experience BETWEEN 16 AND 20 THEN '16-20'
  END AS yrs_exp,
  SUM(workforce_distribution_percentage) AS total_band_per_per_role
FROM 
  experience_dist_perc
GROUP BY 1, 2
),
band_percentages_combined AS (
SELECT 
  job_role,
  yrs_exp,
  AVG(total_band_per_per_role) AS avg_market_dist_perc
FROM 
  role_band_totals
GROUP BY 
  yrs_exp, 
  job_role
ORDER BY
  yrs_exp)

SELECT *
FROM 
  band_percentages_combined
WHERE 
  job_role = 'Data Scientist'
ORDER BY 
  avg_market_dist_perc DESC;
"""

WORKFORCE_DIST_BY_EXPERIECE_DE = """
WITH role_band_totals AS (
SELECT
  job_role,
  CASE 
    WHEN experience BETWEEN 0 AND 5 THEN '0-5'
    WHEN experience BETWEEN 6 AND 10 THEN '6-10'
    WHEN experience BETWEEN 11 AND 15 THEN '11-15'
    WHEN experience BETWEEN 16 AND 20 THEN '16-20'
  END AS yrs_exp,
  SUM(workforce_distribution_percentage) AS total_band_per_per_role
FROM 
  experience_dist_perc
GROUP BY 1, 2
),
band_percentages_combined AS (
SELECT 
  job_role,
  yrs_exp,
  AVG(total_band_per_per_role) AS avg_market_dist_perc
FROM 
  role_band_totals
GROUP BY 
  yrs_exp, 
  job_role
ORDER BY
  yrs_exp)
  
SELECT *
FROM 
  band_percentages_combined
WHERE 
  job_role = 'Data Engineer'
ORDER BY 
  avg_market_dist_perc DESC;
"""


EXPERIENCE_BANDS_COUNT_DS = """
WITH exp_bands AS (
SELECT
  job_role,
  CASE 
    WHEN experience BETWEEN 0 AND 5 THEN '0-5'
    WHEN experience BETWEEN 6 AND 10 THEN '6-10'
    WHEN experience BETWEEN 11 AND 15 THEN '11-15'
    WHEN experience BETWEEN 16 AND 20 THEN '16-20'
  END AS yrs_exp
FROM 
  experience_dist_perc)

SELECT 
  job_role, 
  yrs_exp,
  COUNT(*) AS num_in_band
FROM 
  exp_bands
WHERE 
  job_role = 'Data Scientist'
GROUP BY 
  yrs_exp, 
  job_role
ORDER BY
  num_in_band;
"""

EXPERIENCE_BANDS_COUNT_DE = """
WITH exp_bands AS (
SELECT
  job_role,
  CASE 
    WHEN experience BETWEEN 0 AND 5 THEN '0-5'
    WHEN experience BETWEEN 6 AND 10 THEN '6-10'
    WHEN experience BETWEEN 11 AND 15 THEN '11-15'
    WHEN experience BETWEEN 16 AND 20 THEN '16-20'
  END AS yrs_exp
FROM 
  experience_dist_perc)

SELECT 
  job_role, 
  yrs_exp,
  COUNT(*) AS num_in_band
FROM 
  exp_bands
WHERE 
  job_role = 'Data Engineer'
GROUP BY 
  yrs_exp, 
  job_role
ORDER BY
  num_in_band;
"""

EXPERIENCE_BANDS_COMBINED = """
WITH exp_bands AS (
SELECT
  job_role,
  CASE 
    WHEN experience BETWEEN 0 AND 5 THEN '0_5'
    WHEN experience BETWEEN 6 AND 10 THEN '6_10'
    WHEN experience BETWEEN 11 AND 15 THEN '11_15'
    WHEN experience BETWEEN 16 AND 20 THEN '16_20'
  END AS yrs_exp
FROM 
  experience_dist_perc)

SELECT 
  job_role, 
  yrs_exp,
  COUNT(*) AS num_in_band
FROM 
  exp_bands
GROUP BY 
  yrs_exp, 
  job_role
ORDER BY
  num_in_band;
"""


EXPERIENCE_QUARTILE_DETAILS = """
WITH exp_quartiles AS (
SELECT
  job_role,
  experience,
  NTILE(4) OVER (ORDER BY experience ASC) AS exp_quartile
FROM 
  experience_dist_perc)

SELECT
  job_role,
  experience,
  exp_quartile,
  COUNT(*) OVER(PARTITION BY exp_quartile) AS quartile_counts
FROM 
  exp_quartiles
ORDER BY 
  exp_quartile,
  experience DESC;
"""

