from pathlib import Path
import pandas as pd
import numpy as np
import json


def to_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)

def to_json(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_json(path, orient='records', indent=2)

def _jsonify_cell(x):
    if isinstance(x, np.ndarray):
        return [_jsonify_cell(i) for i in x.tolist()]
    if isinstance(x, (np.generic,)):
        return x.item()
    if isinstance(x, dict):
        return {k: _jsonify_cell(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_jsonify_cell(v) for v in x]
    return x

def _safe_dumps(v):
    try:
        return json.dumps(_jsonify_cell(v), ensure_ascii=False)     # first try to convert with _jsonify_cell()
    except TypeError:
        return json.dumps(str(v), ensure_ascii=False)       # fall back to string, preserve emoji/non-English text

def to_parquet(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df2 = df.copy()
    # detect any complex types in the column, usually named 'object' dtype return True if any()
    for col in df2.select_dtypes(include=['object']).columns:
        if df2[col].map(lambda v: isinstance(v, (np.ndarray, list, tuple, dict))).any():
            # if detected, convert to JSON string with _safe_dumps(), or if not complex, keep orig value
            df2[col] = df2[col].map(lambda v: _safe_dumps(v) if isinstance(v, (np.ndarray, list, tuple, dict)) else v)
    df2.to_parquet(path, index=False)













