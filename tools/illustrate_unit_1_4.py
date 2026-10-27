"""Esquemas conceituais exatos da unidade 1.4, todos em 1280 × 720."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
MEDIA=ROOT/'content/media'
INK='#173f36';GREEN='#2f7464';BG='#f4f1e8';PALE='#e8eedd';GOLD='#d2a452';BLUE='#dce9ef'
credits=[]


def font(size,bold=False):
    return ImageFont.truetype('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf',size)


def label(d,content,box,size=32,bold=False,fill=INK):
    x0,y0,x1,y1=box
    for step in range(size,21,-1):
        f=font(step,bold);rows=content.split('\n');height=len(rows)*(step+9)
        if max(d.textlength(row,font=f) for row in rows)<=x1-x0-16 and height<=y1-y0:break
    assert height<=y1-y0 and max(d.textlength(row,font=f) for row in rows)<=x1-x0-16,content
    y=y0+(y1-y0-height)/2
    for row in rows:
        d.text((x0+(x1-x0-d.textlength(row,font=f))/2,y),row,font=f,fill=fill);y+=step+9


def panel(d,box,fill='white'):
    d.rounded_rectangle(box,radius=22,fill=fill,outline='#cad8cd',width=2)


def base(title,subtitle):
    im=Image.new('RGB',(1280,720),BG);d=ImageDraw.Draw(im)
    d.rounded_rectangle((48,28,224,72),radius=12,fill=GREEN)
    d.text((62,37),'UNIDADE 1.4',font=font(21,True),fill='white')
    label(d,title,(40,88,1240,155),44,True)
    label(d,subtitle,(45,160,1235,211),26)
    d.line((52,660,1228,660),fill='#cad8cd',width=2)
    d.text((56,679),'PROFGEO  /  ESQUEMA DIDÁTICO AUTORAL',font=font(17,True),fill=GREEN)
    return im,d


def save(im,name):
    MEDIA.mkdir(exist_ok=True);temporary=MEDIA/(name+'.tmp')
    im.save(temporary,format='PNG',optimize=True)
    with Image.open(temporary) as check:assert check.size==(1280,720);check.verify()
    temporary.replace(MEDIA/name)
    credits.append(dict(filename=name,author='ProfGeo',license='Ilustração didática autoral',
                        source='tools/illustrate_unit_1_4.py',changes='Esquema original em 1280 × 720; proporção 16:9.'))


im,d=base('Documentos respondem a perguntas diferentes','Relações entre funções; não é uma fila única de autoridade.')
for box,title,body in [
    ((60,235,620,420),'CONSTITUIÇÃO E LDB','Direitos, princípios\ne organização da educação.'),
    ((660,235,1220,420),'DCN E BNCC','Diretrizes de organização\ne aprendizagens essenciais.'),
    ((60,440,620,625),'CURRÍCULO E PPP','Decisões da rede e da escola\nem seus contextos.'),
    ((660,440,1220,625),'PLANO DE ENSINO','Problema, objetivos, tarefas\ne evidências da aprendizagem.')]:
    panel(d,box);x0,y0,x1,y1=box;label(d,title,(x0+10,y0+12,x1-10,y0+66),29,True);label(d,body,(x0+14,y0+70,x1-14,y1-12),30)
save(im,'u14-instrumentos.png')

im,d=base('Da habilidade à aprendizagem observável','Exemplo autoral relacionado à EF06GE01; a aula exige planejamento.')
for i,(title,body) in enumerate([
    ('REFERÊNCIA','Comparar mudanças\ndas paisagens e dos usos\nem tempos diferentes.'),
    ('TAREFA','Confrontar registros\ndatados e fontes\nsobre as transformações.'),
    ('EVIDÊNCIA','Justificar uma mudança\ne uma permanência\ncom as informações.')]):
    x=55+i*410;panel(d,(x,255,x+385,565),PALE if i==1 else 'white');label(d,title,(x+8,273,x+377,337),29,True);label(d,body,(x+12,351,x+373,545),28)
label(d,'Registrar o código não substitui ensinar a relação.',(60,585,1220,645),31,True)
save(im,'u14-habilidade-aula.png')

im,d=base('Ensino Médio: distinguir regra e situação','Referência: LDB, arts. 35-C e 36, após a Lei 14.945/2024.')
panel(d,(60,246,620,505),PALE);panel(d,(660,246,1220,505))
label(d,'FORMAÇÃO GERAL BÁSICA',(74,262,606,320),29,True);label(d,'Mínimo de 2.400 horas',(75,331,605,408),39,True);label(d,'BNCC e parte diversificada.',(75,422,605,483),29)
label(d,'ITINERÁRIOS FORMATIVOS',(674,262,1206,320),29,True);label(d,'Mínimo de 600 horas',(675,331,1205,408),39,True);label(d,'Articulação e aprofundamento.',(675,422,1205,483),29)
label(d,'Oferta técnica e profissional tem especificidades legais.\nOs totais não definem sozinhos horas semanais de Geografia.',(60,535,1220,644),29,True)
save(im,'u14-ensino-medio.png')

im,d=base('Planejar é articular referências e contexto','Os instrumentos não são cópias uns dos outros.')
for i,(title,body) in enumerate([
    ('CURRÍCULO','Seleção e organização\nda aprendizagem na rede.'),
    ('PPP','Compromissos e contexto\nda proposta da escola.'),
    ('PLANO','Objetivos, sequência\ne avaliação do trabalho.')]):
    x=55+i*410;panel(d,(x,258,x+385,555),PALE if i==1 else 'white');label(d,title,(x+9,279,x+376,343),33,True);label(d,body,(x+12,362,x+373,530),29)
label(d,'Autonomia exige decisões justificadas e respeito às normas.',(60,578,1220,640),29,True)
save(im,'u14-curriculo-ppp-plano.png')

im,d=base('PNE: planejar políticas e acompanhar resultados','Lei 15.388/2026; duração de dez anos a contar da publicação.')
for i,(title,body) in enumerate([
    ('OBJETIVOS','Que mudanças\nas políticas devem buscar?'),
    ('METAS','Como verificar o alcance\nem um intervalo de tempo?'),
    ('ESTRATÉGIAS','Que ações dos governos\npodem conduzir às metas?')]):
    x=55+i*410;panel(d,(x,260,x+385,555),PALE if i==1 else 'white');label(d,title,(x+8,280,x+377,345),32,True);label(d,body,(x+12,366,x+373,530),29)
label(d,'Essas funções não equivalem à sequência de uma aula.',(60,579,1220,640),30,True)
save(im,'u14-pne.png')

im,d=base('Como ler um ato antes de aplicá-lo','Perguntas de conferência; consulte o texto oficial e seu contexto.')
for box,title,body in [
    ((60,236,620,420),'IDENTIFICAÇÃO','Órgão, espécie, número,\nano e assunto.'),
    ((660,236,1220,420),'ABRANGÊNCIA','Etapa, modalidade, rede\ne competência do órgão.'),
    ((60,440,620,624),'TEMPO','Redação, alterações, vigência\ne regras de transição.'),
    ((660,440,1220,624),'APLICAÇÃO','O que a norma permite, exige\ne deixa para outras decisões?')]:
    panel(d,box);x0,y0,x1,y1=box;label(d,title,(x0+10,y0+12,x1-10,y0+65),30,True);label(d,body,(x0+14,y0+70,x1-14,y1-12),29)
save(im,'u14-ler-norma.png')

path=ROOT/'content/media-sources.json';sources=json.loads(path.read_text())
sources=[s for s in sources if s['filename'] not in {c['filename'] for c in credits}]+credits
path.write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
print(f'{len(credits)} esquemas da unidade 1.4 verificados em 16:9.')


