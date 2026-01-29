from __future__ import annotations
import os
import pandas as pd

from src.extract.export import to_csv, to_json, to_parquet
from pathlib import Path
from databricks import sql
from dotenv import load_dotenv

load_dotenv()

def connect_dbx():
    return sql.connect(
        server_hostname=os.environ["DATABRICKS_SERVER_HOSTNAME"],
        http_path=os.environ["DATABRICKS_HTTP_PATH"],
        access_token=os.environ["DATABRICKS_ACCESS_TOKEN"],
    )

def execute_sql(sql_text: str, params: tuple | None = None) -> None:
    # with our database connection object, closes when finished
    with connect_dbx() as conn:
        # and with our cursor object from connection, closes when finished
        with conn.cursor() as cur:
            # check params or pass empty tuple
            cur.execute(sql_text, params or ())

def execute_many(statements: list[tuple[str, tuple | None]]) -> None:
    with connect_dbx() as conn:
        with conn.cursor() as cur:
            for sql_text, params in statements:
                cur.execute(sql_text, params or ())

def execute_many_named(statements: list[tuple[str, str, tuple | None]]) -> None:
    """
    statements: [(step_name, sql_text, params), ...]
    raises an error to tell exactly which step of table creation failed
    """
    with connect_dbx() as conn:
        with conn.cursor() as cur:
            for name, sql_text, params in statements:
                try:
                    cur.execute(sql_text, params or ())
                except Exception as e:
                    raise RuntimeError(f"Databricks SQL failed at step: {name}") from e

def extract_df(sql_text: str, params: tuple | None = None) -> pd.DataFrame:
    with connect_dbx() as conn:
        with conn.cursor() as cur:
            cur.execute(sql_text, params or ())
            rows = cur.fetchall()
            cols = [c[0] for c in cur.description]
    return pd.DataFrame(rows, columns=cols)

def extract_df_with_cursor(cur, sql_text: str, params: tuple | None = None) -> pd.DataFrame:
    cur.execute(sql_text, params or ())
    rows = cur.fetchall()
    cols = [c[0] for c in cur.description]
    return pd.DataFrame(rows, columns=cols)

def export_tables_one_conn(tables: dict[str, str], out_dir: Path) -> dict[str, pd.DataFrame]:
    out_dir.mkdir(parents=True, exist_ok=True)
    dfs: dict[str, pd.DataFrame] = {}

    with connect_dbx() as conn:
        with conn.cursor() as cur:
            for name, fqn in tables.items():
                sql_text = f"SELECT * FROM {fqn}"
                df = extract_df_with_cursor(cur, sql_text)
                dfs[name] = df

                base = out_dir / name
                to_csv(df, base.with_suffix(".csv"))
                to_json(df, base.with_suffix(".json"))
                to_parquet(df, base.with_suffix(".parquet"))

    return dfs
