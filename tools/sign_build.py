"""Assina somente com a identidade privada persistente do ProfGeo."""
import argparse,hashlib,json,os,re,shutil,subprocess,zipfile
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--build',type=Path,required=True);p.add_argument('--signing',type=Path,required=True);a=p.parse_args();root=Path(__file__).resolve().parents[1]
meta=json.loads((a.signing/'signing.json').read_text());assert meta['applicationId']=='br.com.emanuel.profgeo' and meta['alias']=='profgeo'
previous=json.loads((root/'downloads/release.json').read_text()) if (root/'downloads/release.json').is_file() else {}
jar=a.build/'signing-tools/apksigner.jar';apk=a.build/'ProfGeo-unsigned.apk';out=root/'downloads';out.mkdir(exist_ok=True)
env=os.environ.copy();env['PROFGEO_STORE_PASSWORD']=meta['storePassword'];env['PROFGEO_KEY_PASSWORD']=meta['keyPassword']
subprocess.run(['java','-jar',str(jar),'sign','--ks',str(a.signing/meta['keystore']),'--ks-key-alias',meta['alias'],'--ks-pass','env:PROFGEO_STORE_PASSWORD','--key-pass','env:PROFGEO_KEY_PASSWORD','--v1-signing-enabled','true','--v2-signing-enabled','true','--v3-signing-enabled','true','--out',str(out/'ProfGeo.apk'),str(apk)],env=env,check=True)
r=subprocess.run(['java','-jar',str(jar),'verify','--verbose','--print-certs',str(out/'ProfGeo.apk')],check=True,capture_output=True,text=True)
digest=re.search(r'certificate SHA-256 digest: ([a-fA-F0-9]+)',r.stdout).group(1).lower();assert digest==meta['certificateSha256']
sha=hashlib.sha256((out/'ProfGeo.apk').read_bytes()).hexdigest();(out/'ProfGeo.apk.sha256').write_text(sha+'  ProfGeo.apk\n')
gradle=(root/'app/build.gradle.kts').read_text();version=int(re.search(r'versionCode = (\d+)',gradle).group(1));name=re.search(r'versionName = "([^"]+)"',gradle).group(1)
release={'applicationId':meta['applicationId'],'versionCode':version,'versionName':name,'certificateSha256':digest,'apkSha256':sha,'bytes':(out/'ProfGeo.apk').stat().st_size,'builtWith':'GitHub Actions','minimumAndroid':'8.0','unit':'1.1','privateKeyInPublicRepository':False}
build_meta=json.loads((a.build/'build-metadata.json').read_text()) if (a.build/'build-metadata.json').is_file() else {}
if previous.get('versionName') and previous.get('versionName')!=name:release['previousVersionName']=previous['versionName']
else:release['previousVersionName']=previous.get('previousVersionName')
release.update({'buildCommit':build_meta.get('commit','não informado'),'buildRun':build_meta.get('runUrl','não informado')})
(out/'release.json').write_text(json.dumps(release,ensure_ascii=False,indent=2)+'\n')
if (a.build/'content').is_dir():shutil.copytree(a.build/'content',root/'content',dirs_exist_ok=True)
update_info=json.loads((root/'content/app-release.json').read_text())
update_info.update({'versionCode':version,'versionName':name,'url':'https://github.com/emanoelb5-lgtm/ProfGeo/releases/latest'})
(root/'content/app-release.json').write_text(json.dumps(update_info,ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(out/'ProfGeo.apk') as z:
 assert 'assets/content/media/ver-o-peso.jpg' in z.namelist() and 'assets/content/media/belem-feira.jpg' in z.namelist()
report=out/'signature-public.txt';report.write_text(r.stdout)
print(f'ProfGeo {name} assinado e verificado. SHA-256 do certificado: {digest}. APK: {release["bytes"]} bytes.')
