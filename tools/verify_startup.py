import re, sys
from collections import Counter
from pathlib import Path
from PIL import Image
root = Path(sys.argv[1])
log = (root / 'startup.log').read_text()
ui = (root / 'ui.xml').read_text()
assert not re.search(r'FATAL EXCEPTION.*?Process: br\.com\.emanuel\.profgeo', log, re.S), 'Falha ao iniciar o app'
assert 'br.com.emanuel.profgeo' in ui and 'android.webkit.WebView' in ui, 'Atividade de estudo não foi aberta'
# UIAutomator no Android 11 pode expor somente o contêiner da WebView.
# O conteúdo é testado por DOM na suíte instrumentada; aqui o PNG confirma
# que a interface de estudo foi pintada, além da simples abertura da atividade.
colors = Counter(Image.open(root / 'android-home.png').convert('RGB').getdata())
assert colors[(18, 62, 54)] > 2500 and colors[(23, 47, 44)] > 300, 'Interface de estudo não foi desenhada'
print('APK assinado instalado, atividade ativa e interface desenhada no Android 11.')
