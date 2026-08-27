from hadia.data import load_all, metadata
from hadia.validate import validate_all

t=load_all(); m=metadata()
print("HADIA-KB",m["version"])
for k,v in t.items(): print(f"{k}: {len(v)}")
errors=validate_all(t)
if errors:
    raise SystemExit("Validation failed:\n"+"\n".join(errors))
print("Validation: PASS")
