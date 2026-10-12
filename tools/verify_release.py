import json,sys,re,hashlib,zipfile
from pathlib import Path
root=Path(__file__).resolve().parents[1];release=json.loads((root/'downloads/release.json').read_text());report=Path(sys.argv[1]).read_text()
cert=re.search(r'certificate SHA-256 digest: ([a-fA-F0-9]+)',report);assert cert and cert.group(1).lower()==release['certificateSha256'].lower(),'Certificado diferente da identidade persistente'
assert hashlib.sha256((root/'downloads/ProfGeo.apk').read_bytes()).hexdigest()==release['apkSha256']
with zipfile.ZipFile(root/'downloads/ProfGeo.apk') as z:
 assert 'classes.dex' in z.namelist() and 'assets/content/units/1.1.json' in z.namelist()
 assert 'assets/content/media/ver-o-peso.jpg' in z.namelist() and 'assets/content/media/belem-feira.jpg' in z.namelist()
print('APK íntegro, assinatura persistente verificada e unidade offline incluída.')
