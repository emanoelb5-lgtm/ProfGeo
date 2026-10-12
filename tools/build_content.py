"""Valida e empacota conteúdo declarativo; imagens baixadas no GitHub Actions."""
import argparse,hashlib,io,json,re,shutil,urllib.request,urllib.parse,zipfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--download-media',action='store_true');p.add_argument('--check',action='store_true');a=p.parse_args()
CAT=ROOT/'content/catalog.json';catalog=json.loads(CAT.read_text());assert catalog['schemaVersion']==1
sources=json.loads((ROOT/'content/media-sources.json').read_text())
media=ROOT/'content/media';media.mkdir(exist_ok=True)
if a.download_media:
 from PIL import Image,ImageOps
 for src in sources:
  out=media/src['filename']
  if out.is_file():continue
  name=src['commonsFile'].replace(' ','_');md5=hashlib.md5(name.encode()).hexdigest()
  url='https://upload.wikimedia.org/wikipedia/commons/'+md5[0]+'/'+md5[:2]+'/'+urllib.parse.quote(name)
  for attempt in range(3):
   try:
    request=urllib.request.Request(url,headers={'User-Agent':'ProfGeoStudy/1.0 (educational Android app; github.com/emanoelb5-lgtm/ProfGeo)'})
    with urllib.request.urlopen(request,timeout=40) as response:raw=response.read(24*1024*1024)
    im=Image.open(io.BytesIO(raw)).convert('RGB');im=ImageOps.fit(im,(1280,720),method=Image.Resampling.LANCZOS);im.save(out,'JPEG',quality=87,optimize=True);print('Foto obtida:',out.name);break
   except Exception as e:
    if attempt==2:raise RuntimeError('Falha ao baixar imagem '+src['filename']) from e
    time.sleep(2+attempt)
entries=catalog['modules'];seen=set();lessons=questions=0
for mod in entries:
 for entry in mod['units']:
  id=entry['id'];assert re.fullmatch(r'[1-9][0-9]?\.[1-9][0-9]?',id) and id not in seen;seen.add(id)
  if entry['status']!='published':continue
  file=ROOT/'content/units'/f'{id}.json';u=json.loads(file.read_text());assert u['id']==id and u['schemaVersion']==1 and u['revision']==entry['revision']
  lids=set();qids=set()
  assert len(u['lessons'])>0 and len(u['questions'])>0
  for l in u['lessons']:
   assert l['id'] not in lids;lids.add(l['id']);lessons+=1
   assert l['minutes']>0 and l['blocks'] and l['summary']
   for b in l['blocks']:
    assert b['type'] in ['text','callout','list','photo','animation','compare','table']
    if b['type']=='photo':assert re.fullmatch(r'media/[a-zA-Z0-9._/-]+',b['src']) and '..' not in b['src']
  for q in u['questions']:
   assert q['id'] not in qids;qids.add(q['id']);questions+=1
   assert q['lesson'] in lids and len(q['options'])>=2 and len(q['feedback'])==len(q['options']) and 0<=q['answer']<len(q['options'])
   assert all(len(f)>25 for f in q['feedback'])
  for l in u['lessons']:assert any(q['lesson']==l['id'] and q['pool']=='lesson' for q in u['questions'])
  archive=ROOT/'content/packages'/f'{id}-r{u["revision"]}.zip';archive.parent.mkdir(exist_ok=True)
  with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
   def put(name,data):
    zi=zipfile.ZipInfo(name,date_time=(2026,1,1,0,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;z.writestr(zi,data)
   put('unit.json',file.read_bytes())
   used={b['src'] for l in u['lessons'] for b in l['blocks'] if b['type']=='photo'}
   for src in sorted(used):
    f=ROOT/'content'/src
    if a.download_media:assert f.is_file(),f
    if f.is_file():put(src,f.read_bytes())
   put('media/CREDITS.txt',json.dumps(sources,ensure_ascii=False,indent=2).encode())
  entry['package']='packages/'+archive.name;entry['sha256']=hashlib.sha256(archive.read_bytes()).hexdigest();entry['bytes']=archive.stat().st_size
if not a.check:CAT.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
assert len(seen)==15, 'Preserve os 15 itens do edital no plano de expansão.'
assets=ROOT/'app/src/main/assets/content'
if assets.exists():shutil.rmtree(assets)
shutil.copytree(ROOT/'content',assets,ignore=shutil.ignore_patterns('packages','media-sources.json','app-release.json'))
print(f'Conteúdo validado: {len(seen)} unidades no plano; {lessons} lições e {questions} questões publicadas.')
