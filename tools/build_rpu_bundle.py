"""Bundle RPU v2.4.34 Korean data with the known-fixed high-resolution DLL."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

def sha(data):
    return hashlib.sha256(data).hexdigest()

def build(source, patched, output):
    source, patched, output = Path(source), Path(patched), Path(output)
    dll = patched.read_bytes()
    if dll[:2] != b"MZ" or b".krfit" not in dll[:8192]:
        raise ValueError("Missing independently verified .krfit patch")
    with zipfile.ZipFile(source) as archive:
        files = {entry.filename: archive.read(entry) for entry in archive.infolist() if not entry.is_dir()}
    if "f2_res.dll" in files:
        raise ValueError("Unexpected DLL in translation-only source ZIP")
    files["f2_res.dll"] = dll
    files["RPU-KR-BUNDLE-MANIFEST.json"] = json.dumps({
        "target":"RPU v2.4.34, exact official f2_res.dll only",
        "base_sha256":"2d3c52cf624b22958db7fa44e3db71c2d0478503da5ceb40f0636dea1202fb5a",
        "patched_sha256":sha(dll)
    }, indent=2).encode()
    output.parent.mkdir(exist_ok=True,parents=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for filename, data in sorted(files.items()):
            info=zipfile.ZipInfo(filename,date_time=(1980,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o644<<16
            archive.writestr(info,data)
    with zipfile.ZipFile(output) as archive:
        if archive.read("f2_res.dll") != dll:
            raise ValueError("Bundle mismatch")
    return {"files":len(files),"patched_sha256":sha(dll),"artifact":str(output)}

if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("--translation",required=True)
    a.add_argument("--hrp",required=True)
    a.add_argument("--output",required=True)
    p=a.parse_args()
    print(json.dumps(build(p.translation,p.hrp,p.output),indent=2))
