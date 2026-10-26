"""Esquemas conceituais exatos da unidade 1.3, todos em 1280 × 720."""
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
    d.text((62,37),'UNIDADE 1.3',font=font(21,True),fill='white')
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
                        source='tools/illustrate_unit_1_3.py',changes='Esquema original em 1280 × 720; proporção 16:9.'))


im,d=base('Do assunto à ferramenta de pensamento','Um exemplo; os termos não formam uma hierarquia universal.')
for box,title,body in [
    ((60,236,620,415),'CONTEÚDO','Usos e regras de uma praça.\nO que será estudado?'),
    ((660,236,1220,415),'CONCEITO','Território.\nComo ler relações de poder?'),
    ((60,438,620,624),'PERGUNTA','Quem decide os usos\ne quem pode participar?'),
    ((660,438,1220,624),'APRENDIZAGEM','Explicar uma regra, seus agentes\ne seus efeitos sobre o acesso.')]:
    panel(d,box);x0,y0,x1,y1=box;label(d,title,(x0+10,y0+12,x1-10,y0+63),29,True)
    label(d,body,(x0+16,y0+67,x1-16,y1-12),30)
save(im,'u13-conceitos-conteudos.png')

im,d=base('Espaço: formas, ações e história','Os elementos ganham sentido em suas relações.')
panel(d,(65,245,585,540));panel(d,(695,245,1215,540),PALE)
label(d,'OBJETOS',(85,265,565,330),35,True)
label(d,'Cais\nRua\nArmazém',(90,345,560,520),34)
label(d,'AÇÕES',(715,265,1195,330),35,True)
label(d,'Transportar\nNegociar\nRegular os usos',(720,345,1190,520),34)
d.line((600,380,680,380),fill=GREEN,width=6);d.polygon([(685,380),(666,367),(666,393)],fill=GREEN)
d.line((680,430,600,430),fill=GREEN,width=6);d.polygon([(595,430),(614,417),(614,443)],fill=GREEN)
label(d,'Uma mesma forma pode mudar de função ao longo do tempo.',(65,565,1215,637),30,True)
save(im,'u13-objetos-acoes.png')

im,d=base('Regionalizar depende do problema e do critério','Localidades fictícias; esquema sem escala cartográfica.')
for side,title,groups,legends in [
    (60,'Características do relevo',[0,0,0,1,1,1],['Planície','Colinas']),
    (670,'Conexão principal com mercados',[0,1,1,0,0,1],['Mercado X','Mercado Y'])]:
    panel(d,(side,232,side+550,630));label(d,title,(side+8,240,side+542,305),28,True)
    for i,name in enumerate('ABCDEF'):
        x=side+100+(i%3)*175;y=355+(i//3)*136
        color=GREEN if groups[i]==0 else GOLD
        d.ellipse((x-43,y-43,x+43,y+43),fill=color)
        label(d,name,(x-34,y-34,x+34,y+34),31,True,'white' if groups[i]==0 else INK)
    for i,legend in enumerate(legends):
        x=side+36+i*257;d.ellipse((x,575,x+21,596),fill=GREEN if i==0 else GOLD)
        d.text((x+29,570),legend,font=font(23),fill=INK)
save(im,'u13-regionalizacoes.png')

im,d=base('Uma chuva, condições e efeitos diferentes','Relação didática; não é mapa nem cálculo de risco real.')
parts=[('PROCESSO','Chuva e\ncondições físicas.'),('EXPOSIÇÃO','Pessoas, atividades\ne bens no local.'),('VULNERABILIDADE','Condições desiguais\nde proteção e acesso.')]
for i,(title,body) in enumerate(parts):
    x=55+i*410;panel(d,(x,260,x+385,510),PALE if i==1 else 'white')
    label(d,title,(x+9,280,x+376,345),27,True);label(d,body,(x+12,365,x+373,484),29)
panel(d,(85,548,1195,631),INK)
label(d,'Explicar exige investigar como essas condições se combinam.',(96,555,1184,622),29,True,'white')
save(im,'u13-natureza-sociedade.png')

im,d=base('O conceito participa da tarefa e da avaliação','Exemplo autoral com território; adapte a turma e as fontes.')
for i,(title,body) in enumerate([
    ('OBJETIVO','Explicar como uma regra\norganiza o uso da praça.'),
    ('TAREFA','Comparar usos, agentes\ne normas em duas situações.'),
    ('EVIDÊNCIA','Justificar quem decide\ne como isso afeta o acesso.')]):
    x=55+i*410;panel(d,(x,265,x+385,548),PALE if i==1 else 'white')
    label(d,title,(x+10,284,x+375,350),31,True);label(d,body,(x+14,368,x+371,525),29)
label(d,'Copiar a definição não demonstra sozinho o uso do conceito.',(70,568,1210,636),30,True)
save(im,'u13-objetivo-evidencia.png')

im,d=base('Progressão: ampliar relações e autonomia','As operações não pertencem exclusivamente a uma etapa.')
for i,(title,body) in enumerate([
    ('ANOS INICIAIS','Observar, representar\ne comparar com apoio.\nRelacionar vivido e mundo.'),
    ('ANOS FINAIS','Cruzar fontes e explicar\nprocessos e conexões.\nRever generalizações.'),
    ('ENSINO MÉDIO','Confrontar argumentos,\nagentes e escalas.\nSustentar uma posição.')]):
    x=55+i*410;panel(d,(x,255,x+385,574),PALE if i==1 else 'white')
    label(d,title,(x+8,272,x+377,337),29,True);label(d,body,(x+12,350,x+373,550),27)
label(d,'A complexidade depende do problema, da mediação e da turma.',(55,589,1225,645),29,True)
save(im,'u13-progressao.png')

path=ROOT/'content/media-sources.json';sources=json.loads(path.read_text())
sources=[s for s in sources if s['filename'] not in {c['filename'] for c in credits}]+credits
path.write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
print(f'{len(credits)} esquemas da unidade 1.3 verificados em 16:9.')
