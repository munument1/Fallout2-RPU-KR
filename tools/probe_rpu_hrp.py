"""Read-only RPU HRP PE entry point comparison with Resurrection KR1.2.
Does not patch or ship any DLL. Use official upstream RPU v2.4.34 asset.
"""
import argparse
import hashlib
import json
import struct
from pathlib import Path

RESURRECTION_ORIGINAL_SHA256 = "2d3c52cf624b22958db7fa44e3db71c2d0478503da5ceb40f0636dea1202fb5a"
RESURRECTION_HOOK_RVAS = (0xF250, 0xF2E0)


def read_u16(data, at):
    return struct.unpack_from("<H", data, at)[0]


def read_u32(data, at):
    return struct.unpack_from("<I", data, at)[0]


def inspect(data):
    if len(data) < 256 or data[:2] != b"MZ":
        raise ValueError("Not an MZ executable")
    pe = read_u32(data, 0x3C)
    if data[pe:pe + 4] != b"PE\0\0":
        raise ValueError("Not a PE executable")
    sections_count = read_u16(data, pe + 6)
    size_optional = read_u16(data, pe + 20)
    optional = pe + 24
    if read_u16(data, optional) != 0x10B:
        raise ValueError("Not PE32")
    table = optional + size_optional
    sections = []
    for i in range(sections_count):
        off = table + i * 40
        name = data[off:off + 8].split(b"\0")[0].decode("ascii", "replace")
        vs, va, rs, ro = struct.unpack_from("<IIII", data, off + 8)
        sections.append({"name":name, "va":va, "virtual_size":vs, "raw_size":rs, "raw_offset":ro})
    hooks = {}
    for rva in RESURRECTION_HOOK_RVAS:
        match = next((s for s in sections if s["va"] <= rva < s["va"] + s["raw_size"]), None)
        if match is None:
            raise ValueError(f"RVA {rva:x} unmapped")
        at = match["raw_offset"] + rva - match["va"]
        block = data[at:at+48]
        hooks[f"{rva:#x}"] = {
            "file_offset":at,
            "first_48_bytes":block.hex(),
            "starts_with_push_ebp_mov_ebp_esp": block[:3] == b"\x55\x8b\xec",
        }
    digest = hashlib.sha256(data).hexdigest()
    return {
        "size":len(data),
        "sha256":digest,
        "same_binary_as_resurrection_base":digest == RESURRECTION_ORIGINAL_SHA256,
        "sections":sections,
        "candidate_rvas":hooks,
        "safe_to_apply_resurrection_patch_without_reverse_engineering":digest == RESURRECTION_ORIGINAL_SHA256,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dll",type=Path)
    a=parser.parse_args()
    result=inspect(a.dll.read_bytes())
    print(json.dumps(result,indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
