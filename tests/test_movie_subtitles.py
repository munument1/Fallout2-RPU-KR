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
          'boil1', 'boil2', 'boil3', 'credits', 'elder', 'intro', 'ovrintro', 'tanker')


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


    def test_intro_frame_cues_and_gender_parity(self):
        # RPU 2.4.34 data/text/english/cuts/intro.sve: keep exact movie timings.
        expected = (460, 505, 590, 665, 710, 805, 840, 960, 1065,
                    1190, 1255, 1330, 1430, 1520, 1550, 1580, 1645)
        subtitles = []
        for folder in ('cuts', 'cuts_female'):
            source = ROOT / 'mods/rpu/text/korean' / folder / 'intro.sve'
            data, _ = runtime_bytes(source)
            lines = data.decode('cp949').splitlines()
            frames = [int(line.partition(':')[0]) for line in lines]
            self.assertEqual(tuple(frames), expected)
            self.assertEqual([int(line.partition(':')[0]) for line in lines
                              if not line.partition(':')[2].strip()], [1550, 1645])
            subtitles.append(data)
        self.assertEqual(subtitles[0], subtitles[1])

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
