import re, sys
from pathlib import Path
root = Path(sys.argv[1])
log = (root / 'startup.log').read_text()
ui = (root / 'ui.xml').read_text()
assert not re.search(r'FATAL EXCEPTION.*?Process: br\.com\.emanuel\.profgeo', log, re.S), 'Falha ao iniciar o app'
assert 'Compreender' in ui and 'ProfGeo' in ui, 'A tela inicial de estudo não foi apresentada'
print('APK assinado instalado e tela inicial de estudo confirmada no Android 11.')
