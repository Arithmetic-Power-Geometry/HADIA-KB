from __future__ import annotations
from urllib.parse import urlparse
import pandas as pd
from .data import load_all

ID_COLS={"sources":"source_id","claims":"claim_id","plants":"plant_id","microorganisms":"microbe_id","measurements":"measurement_id","names":"name_id","locations":"location_id"}

def validate_all(tables: dict[str,pd.DataFrame] | None=None) -> list[str]:
    t=tables or load_all(); errors=[]
    for name,idcol in ID_COLS.items():
        df=t.get(name,pd.DataFrame())
        if df.empty: continue
        if idcol not in df.columns: errors.append(f"{name}: missing {idcol}"); continue
        vals=df[idcol].astype(str)
        if (vals.str.strip()=="").any(): errors.append(f"{name}: blank IDs")
        if vals.duplicated().any(): errors.append(f"{name}: duplicate IDs")
    sources=t.get("sources",pd.DataFrame()); claims=t.get("claims",pd.DataFrame())
    if not sources.empty and not claims.empty:
        known=set(sources["source_id"])
        orphans=sorted(set(claims["source_id"])-known)
        if orphans: errors.append(f"claims: orphan source IDs: {orphans}")
    for name in ["plants","microorganisms","measurements"]:
        df=t.get(name,pd.DataFrame())
        if not df.empty and "source_id" in df.columns and not sources.empty:
            orphans=sorted(set(df["source_id"])-set(sources["source_id"]))
            if orphans: errors.append(f"{name}: orphan source IDs: {orphans}")
    if not sources.empty:
        bad=[]
        for sid,u in zip(sources["source_id"],sources["source_url"]):
            p=urlparse(str(u));
            if p.scheme not in {"http","https"} or not p.netloc: bad.append(sid)
        if bad: errors.append(f"sources: malformed URLs: {bad}")
    if not claims.empty:
        required=["claim_text","geographic_scope","source_id"]
        for col in required:
            if col not in claims.columns or (claims[col].astype(str).str.strip()=="").any():
                errors.append(f"claims: missing/blank required field {col}")
    return errors
