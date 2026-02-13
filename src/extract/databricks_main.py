from src.extract.databricks_extract import extract_df
from collection.ctas_queries import MANY_JOB_POSTS_TABLE
from src.extract.constants import DATA_RAW

import pandas as pd

def main():
    # execute_many_named(ddl_ctas_batch_named)

    # dfs = export_tables_one_conn(TABLES, DATA_RAW)

    # had to update a table with an additional column
    # execute_sql(COMPANY_NUM_POSTINGS)

    df = extract_df(MANY_JOB_POSTS_TABLE)
    print(df.head())
    df.to_csv(DATA_RAW/'many_job_posts_trunc.csv', index=False)






if __name__ == "__main__":
    main()











