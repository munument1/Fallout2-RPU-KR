"""Focused regression tests for issue #4 (RPU ending subtitles)."""

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import audit_cut_subtitles
import build_translation


class CutSubtitleTests(unittest.TestCase):
    def test_reported_narrations_are_translated_and_structured(self):
        report = audit_cut_subtitles.audit(ROOT)
        self.assertEqual(report["critical_errors"], [])
        for folder in audit_cut_subtitles.FOLDERS:
            for name in audit_cut_subtitles.CRITICAL:
                self.assertNotIn(name, report["english_only"][folder])

    def test_translated_files_are_identical_across_gender_folders(self):
        for name in audit_cut_subtitles.CRITICAL:
            male = (ROOT / audit_cut_subtitles.CUT_ROOT / "cuts" / name).read_bytes()
            female = (ROOT / audit_cut_subtitles.CUT_ROOT / "cuts_female" / name).read_bytes()
            self.assertEqual(male, female)

    def test_packaged_subtitles_match_cp949_source(self):
        with tempfile.TemporaryDirectory() as directory:
            archive_path = Path(directory) / "translation.zip"
            build_translation.build(ROOT, archive_path)
            with zipfile.ZipFile(archive_path) as archive:
                for folder in audit_cut_subtitles.FOLDERS:
                    for name in audit_cut_subtitles.CRITICAL:
                        path = ROOT / audit_cut_subtitles.CUT_ROOT / folder / name
                        text = audit_cut_subtitles.decode_source(path.read_bytes())
                        expected = text.replace("\r\n", "\n").replace("\r", "\n")
                        expected = expected.replace("\n", "\r\n").encode("cp949")
                        self.assertEqual(archive.read(f"data/text/korean/{folder}/{name}"), expected)

    def test_reviewed_english_subtitles_are_all_translated(self):
        report = audit_cut_subtitles.audit(ROOT)
        self.assertEqual(report["critical_errors"], [])
        for folder in audit_cut_subtitles.FOLDERS:
            for name in audit_cut_subtitles.REVIEWED:
                self.assertNotIn(name, report["english_only"][folder])

    def test_audit_detects_english_regression(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for folder in audit_cut_subtitles.FOLDERS:
                cut_dir = root / audit_cut_subtitles.CUT_ROOT / folder
                cut_dir.mkdir(parents=True)
                for name in audit_cut_subtitles.CRITICAL:
                    (cut_dir / name).write_text("1:English only.\n2:Still English.\n", encoding="ascii")
            report = audit_cut_subtitles.audit(root)
            self.assertTrue(report["critical_errors"])
            for folder in audit_cut_subtitles.FOLDERS:
                for name in audit_cut_subtitles.CRITICAL:
                    self.assertIn(name, report["english_only"][folder])


if __name__ == "__main__":
    unittest.main()
