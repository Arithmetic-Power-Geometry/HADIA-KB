from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import Response
from hadia.data import load_table, metadata
from hadia.search import filter_df

app=FastAPI(title="HADIA-KB API",version="1.0.0",description="Evidence-linked API for Handia/Hadia/Haria public research data.")

@app.get("/api/v1")
def root():
    return {"name":"HADIA-KB API","version":"1.0.0","copyright":"Copyright (C) 2026 Mohammad Amir Khusru Akhtar"}

@app.get("/api/v1/metadata")
def get_metadata(): return metadata()

@app.get("/api/v1/{table}")
def get_table(table: str, q: str = Query(default=""), limit: int = Query(default=500, ge=1, le=5000)):
    try: df=load_table(table)
    except ValueError as e: raise HTTPException(status_code=404,detail=str(e))
    df=filter_df(df,q)
    return {"table":table,"count":len(df),"records":df.head(limit).to_dict(orient="records")}

@app.get("/api/v1/{table}.csv")
def get_table_csv(table: str, q: str = Query(default="")):
    try: df=load_table(table)
    except ValueError as e: raise HTTPException(status_code=404,detail=str(e))
    df=filter_df(df,q)
    return Response(df.to_csv(index=False),media_type="text/csv",headers={"Content-Disposition":f"attachment; filename=hadia_{table}.csv"})
