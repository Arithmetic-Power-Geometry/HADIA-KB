import pandas as pd

def filter_df(df: pd.DataFrame, query: str="", **filters) -> pd.DataFrame:
    out=df.copy()
    for col,val in filters.items():
        if val and val != "All" and col in out.columns:
            out=out[out[col].astype(str)==str(val)]
    q=(query or "").strip().lower()
    if q and not out.empty:
        mask=out.astype(str).apply(lambda col: col.str.lower().str.contains(q, regex=False)).any(axis=1)
        out=out[mask]
    return out.reset_index(drop=True)
