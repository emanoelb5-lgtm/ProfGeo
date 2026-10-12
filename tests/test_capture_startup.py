import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    'capture_startup', Path(__file__).parents[1] / 'tools/capture_startup.py'
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CaptureStartupTest(unittest.TestCase):
    def fake_adb(self, fail_count):
        self.dumps = 0

        def run(command, **kwargs):
            args = command[1:]
            if 'uiautomator' in args:
                self.dumps += 1
                # Android can return success while exposing no root or file.
                output = 'ERROR: null root node returned' if self.dumps <= fail_count else 'UI hierarchy dumped'
                return subprocess.CompletedProcess(command, 0, output, '')
            if args[0] == 'pull':
                if args[1].endswith('.xml'):
                    if self.dumps <= fail_count:
                        return subprocess.CompletedProcess(command, 1, '', 'No such file')
                    Path(args[2]).write_text('<hierarchy><node package="br.com.emanuel.profgeo" class="android.webkit.WebView"/></hierarchy>')
                else:
                    Path(args[2]).write_bytes(b'screenshot')
            return subprocess.CompletedProcess(command, 0, 'diagnostic', '')
        return run

    def test_missing_root_is_retried_without_accepting_false_success(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(module.subprocess, 'run', side_effect=self.fake_adb(1)):
                module.capture(folder, delay=0)
            root = Path(folder)
            self.assertEqual(2, self.dumps)
            self.assertIn('android.webkit.WebView', (root / 'ui.xml').read_text())
            self.assertTrue((root / 'android-home.png').is_file())

    def test_persistent_failure_keeps_evidence_and_blocks_publication(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(module.subprocess, 'run', side_effect=self.fake_adb(5)):
                with self.assertRaises(RuntimeError):
                    module.capture(folder, attempts=2, delay=0)
            root = Path(folder)
            self.assertEqual(2, self.dumps)
            self.assertFalse((root / 'ui.xml').exists())
            for name in ('android-home.png', 'startup.log', 'capture.log', 'activity.txt', 'window.txt'):
                self.assertTrue((root / name).is_file(), name)


if __name__ == '__main__':
    unittest.main()
