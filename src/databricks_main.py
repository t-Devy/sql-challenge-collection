from src.constants import DATA_RAW
from src.databricks_extract import execute_many_named, export_tables_one_conn
from collection.sql_queries import ddl_ctas_batch_named, TABLES

import pandas as pd


def main():
    execute_many_named(ddl_ctas_batch_named)

    dfs = export_tables_one_conn(TABLES, DATA_RAW)

    for name, df in dfs.items():
        print(f"\n=== {name} ===")
        print(df.shape)
        print(df.head(3))




if __name__ == "__main__":
    main()











