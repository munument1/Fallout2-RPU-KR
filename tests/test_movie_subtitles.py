"""Movie SVE files must ship alongside the unrelated ending TXT files."""
import hashlib
import json
import re
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from build_translation import build, runtime_bytes

MOVIES = ('afailed', 'artimer1', 'artimer2', 'artimer3', 'artimer4',
          'boil1', 'boil2', 'boil3', 'credits', 'elder', 'ovrintro', 'tanker')


class MovieSubtitles(unittest.TestCase):
    def test_movie_timing_and_korean(self):
        for folder in ('cuts', 'cuts_female'):
            for movie in MOVIES:
                path = ROOT / 'mods/rpu/text/korean' / folder / (movie + '.sve')
                with self.subTest(folder=folder, movie=movie):
                    data, _ = runtime_bytes(path)
                    cues = [line for line in data.decode('cp949').splitlines() if line.strip()]
                    self.assertTrue(cues)
                    previous = -1
                    for cue in cues:
                        match = re.fullmatch(r'(\d+):(.*)', cue)
                        self.assertIsNotNone(match, cue)
                        frame, text = match.groups()
                        self.assertGreater(int(frame), previous, cue)
                        previous = int(frame)
                        if text.strip():
                            self.assertRegex(text, '[가-힣]')

    def test_all_movie_subtitles_in_zip_with_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'translation.zip'
            build(ROOT, output)
            with zipfile.ZipFile(output) as archive:
                manifest = json.loads(archive.read('translation-manifest.json'))
                for folder in ('cuts', 'cuts_female'):
                    for movie in MOVIES:
                        name = f'data/text/korean/{folder}/{movie}.sve'
                        source = ROOT / 'mods/rpu/text/korean' / folder / (movie + '.sve')
                        data = archive.read(name)
                        self.assertEqual(data, runtime_bytes(source)[0])
                        self.assertEqual(hashlib.sha256(data).hexdigest(), manifest['files'][name])


if __name__ == '__main__':
    unittest.main()
