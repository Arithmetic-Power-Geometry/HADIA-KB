from pathlib import Path
import io, json, zipfile
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
TABLES = ["sources","claims","plants","microorganisms","measurements","names","locations","communities","policy_law","relations","contradictions","gaps"]

def load_table(name: str) -> pd.DataFrame:
    if name not in TABLES:
        raise ValueError(f"Unknown HADIA table: {name}")
    path = DATA / f"{name}.csv"
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str, keep_default_na=False)

def load_all() -> dict[str, pd.DataFrame]:
    return {name: load_table(name) for name in TABLES}

def metadata() -> dict:
    return json.loads((DATA / "metadata.json").read_text(encoding="utf-8"))

def to_csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8-sig")

def to_json_bytes(df: pd.DataFrame) -> bytes:
    return df.to_json(orient="records", force_ascii=False, indent=2).encode("utf-8")

def tables_zip_bytes(tables: dict[str,pd.DataFrame]) -> bytes:
    bio=io.BytesIO()
    with zipfile.ZipFile(bio,"w",zipfile.ZIP_DEFLATED) as z:
        for name,df in tables.items():
            z.writestr(f"{name}.csv", df.to_csv(index=False))
        z.write(DATA / "metadata.json", "metadata.json")
    return bio.getvalue()
