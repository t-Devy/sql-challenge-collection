from collection.ctas_queries import WF_DIST_BY_EXP_TABLES
from src.extract.constants import DATA_OUT
from src.extract.databricks_extract import export_tables_one_conn


def main():
    dfs = export_tables_one_conn(WF_DIST_BY_EXP_TABLES, DATA_OUT)

    for df_name, df in dfs.items():
        print(df_name)
        print(df)

if __name__ == "__main__":
    main()