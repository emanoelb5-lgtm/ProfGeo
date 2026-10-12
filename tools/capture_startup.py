"""Capture release evidence even when UIAutomator temporarily has no root."""
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path


def capture(root, attempts=5, delay=1):
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)

    def adb(*args):
        result = subprocess.run(
            ['adb', *args], capture_output=True, text=True, timeout=30
        )
        with (root / 'capture.log').open('a') as log:
            log.write(f"adb {' '.join(args)}\n{result.stdout}{result.stderr}\n")
        return result

    def screenshot():
        shot = adb('shell', 'screencap', '-p', '/sdcard/profgeo-final.png')
        if shot.returncode:
            raise RuntimeError('Não foi possível capturar a tela do APK.')
        pulled = adb('pull', '/sdcard/profgeo-final.png', str(root / 'android-home.png'))
        if pulled.returncode:
            raise RuntimeError('Não foi possível baixar a captura do APK.')

    try:
        adb('shell', 'input', 'keyevent', 'KEYCODE_WAKEUP')
        adb('shell', 'wm', 'dismiss-keyguard')
        # Keep the painted screen even if every hierarchy attempt fails.
        screenshot()
        for attempt in range(1, attempts + 1):
            adb('shell', 'rm', '-f', '/sdcard/profgeo-ui.xml')
            dumped = adb('shell', 'uiautomator', 'dump', '/sdcard/profgeo-ui.xml')
            candidate = root / f'ui-attempt-{attempt}.xml'
            pulled = adb('pull', '/sdcard/profgeo-ui.xml', str(candidate))
            if dumped.returncode == 0 and pulled.returncode == 0 and candidate.is_file():
                try:
                    nodes = ET.parse(candidate).getroot().iter('node')
                    opened = any(
                        n.get('package') == 'br.com.emanuel.profgeo'
                        and n.get('class') == 'android.webkit.WebView' for n in nodes
                    )
                except ET.ParseError:
                    opened = False
                if opened:
                    (root / 'ui.xml').write_bytes(candidate.read_bytes())
                    screenshot()
                    print(f'Interface do APK capturada na tentativa {attempt}.')
                    return
            if attempt < attempts:
                time.sleep(delay)
        raise RuntimeError('A interface do ProfGeo não apareceu na hierarquia do Android.')
    finally:
        # Preserve diagnostics before the runner terminates the emulator.
        for name, args in (
            ('startup.log', ('logcat', '-d')),
            ('activity.txt', ('shell', 'dumpsys', 'activity', 'activities')),
            ('window.txt', ('shell', 'dumpsys', 'window', 'windows')),
        ):
            result = adb(*args)
            (root / name).write_text(result.stdout + result.stderr)


if __name__ == '__main__':
    capture(sys.argv[1])
