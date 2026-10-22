"""Audit Fallout 2 RPU ending subtitles without modifying sources.

The translation ZIP stores CP949 text, while repository files may be UTF-8.
English-only files are reported for follow-up, not silently rewritten.
Only known, user-reported nar_2/nar_3 regressions fail --verify-critical.
"""

import argparse
import json
import re
from pathlib import Path

CUT_ROOT = Path("mods/rpu/text/korean")
FOLDERS = ("cuts", "cuts_female")
CRITICAL = ("nar_2.txt", "nar_3.txt")
REVIEWED = ("nar_9.txt", "nar_10.txt", "nar_11.txt", "nar_12.txt", "nar_13.txt", "nar_15.txt", "nar_16.txt", "nar_18.txt", "nar_19.txt", "nar_20.txt", "nar_21.txt", "nar_22.txt", "nar_23.txt", "nar_24.txt", "nar_25.txt", "nar_27.txt", "nar_28.txt", "nar_29.txt", "nar_31.txt", "nar_32.txt", "nar_34.txt", "nar_35.txt", "nar_36.txt", "nar_37.txt", "nar_38.txt", "nar_39.txt", "nar_40.txt", "nar_41.txt", "nar_42.txt", "nar_44.txt", "nar_45.txt", "nar_46.txt")
NUMBERED = re.compile(r"^([0-9]+):(.+)$")
HANGUL = re.compile(r"[가-힣]")


def decode_source(data):
    if data.isascii():
        return data.decode("ascii")
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return data.decode("cp949", errors="strict")


def audit(root):
    root = Path(root)
    english_only = {}
    unreadable = []
    critical_errors = []
    critical_texts = {}
    file_counts = {}
    for folder in FOLDERS:
        directory = root / CUT_ROOT / folder
        if not directory.is_dir():
            critical_errors.append(f"Missing subtitle directory: {directory}")
            english_only[folder] = []
            file_counts[folder] = 0
            continue
        paths = sorted(directory.glob("*.txt"))
        file_counts[folder] = len(paths)
        untranslated = []
        for path in paths:
            relative = f"{folder}/{path.name}"
            try:
                text = decode_source(path.read_bytes())
                text.encode("cp949", errors="strict")
            except UnicodeError as error:
                unreadable.append(f"{relative}: {error}")
                if path.name in CRITICAL:
                    critical_errors.append(f"{relative}: invalid CP949-compatible text")
                continue
            if not HANGUL.search(text):
                untranslated.append(path.name)
            if path.name not in CRITICAL:
                continue
            critical_texts[relative] = text
            lines = text.splitlines()
            parsed = [NUMBERED.fullmatch(line) for line in lines]
            if len(lines) != 2 or any(item is None for item in parsed):
                critical_errors.append(f"{relative}: expected two numbered subtitle lines")
                continue
            if [int(item.group(1)) for item in parsed] != [1, 2]:
                critical_errors.append(f"{relative}: expected subtitle numbers 1 and 2")
            if any(not HANGUL.search(item.group(2)) for item in parsed):
                critical_errors.append(f"{relative}: untranslated subtitle line")
        english_only[folder] = untranslated
        for name in REVIEWED:
            relative = f"{folder}/{name}"
            source = directory / name
            if not source.is_file():
                critical_errors.append(f"{relative}: missing reviewed source")
                continue
            try:
                value = decode_source(source.read_bytes())
                value.encode("cp949", errors="strict")
            except UnicodeError:
                critical_errors.append(f"{relative}: invalid CP949-compatible reviewed text")
                continue
            for line in value.splitlines():
                match = NUMBERED.fullmatch(line)
                if match and not HANGUL.search(match.group(2)):
                    critical_errors.append(f"{relative}: untranslated subtitle line {match.group(1)}")
        for name in CRITICAL:
            if f"{folder}/{name}" not in critical_texts:
                critical_errors.append(f"{folder}/{name}: missing critical source subtitle")
    for name in CRITICAL:
        male, female = (critical_texts.get(f"{folder}/{name}") for folder in FOLDERS)
        if male is not None and female is not None and male != female:
            critical_errors.append(f"{name}: male/female text differs unexpectedly")
    return {
        "scanned": file_counts,
        "english_only": english_only,
        "unreadable": unreadable,
        "critical_errors": critical_errors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--verify-critical", action="store_true",
                        help="fail only if the reported nar_2/nar_3 subtitles regress")
    args = parser.parse_args()
    result = audit(args.root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if args.verify_critical and result["critical_errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
