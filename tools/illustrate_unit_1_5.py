"""Esquemas conceituais exatos da unidade 1.5, todos em 1280 × 720."""
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
    d.text((62,37),'UNIDADE 1.5',font=font(21,True),fill='white')
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
                        source='tools/illustrate_unit_1_5.py',changes='Esquema original em 1280 × 720; proporção 16:9.'))

def four(name,title,subtitle,cards,foot):
    im,d=base(title,subtitle)
    boxes=[(52,232,624,405),(656,232,1228,405),(52,425,624,598),(656,425,1228,598)]
    for i,(box,(heading,body)) in enumerate(zip(boxes,cards)):
        panel(d,box,fill=PALE if i%2==0 else BLUE)
        x0,y0,x1,y1=box
        label(d,heading,(x0+12,y0+8,x1-12,y0+54),30,True)
        label(d,body,(x0+12,y0+56,x1-12,y1-8),28)
    label(d,foot,(50,608,1230,651),24,True)
    save(im,name)

four('u15-problema.png','Quando uma dúvida se torna pesquisa?','Caso fictício: explicações dos estudantes sobre trajetos',[
 ('PERGUNTA','Como relacionam circulação\ne diferenças de acesso?'),
 ('CONCEITOS','Redes, circulação e acesso\norientam o que examinar.'),
 ('FONTES E ANÁLISE','Produções e registros\ncom critérios explícitos.'),
 ('CONCLUSÃO E REVISÃO','Sustentar uma interpretação,\nindicar limites e replanejar.')
],'As escolhas dialogam e podem ser revistas ao longo da investigação.')

four('u15-desenho.png','Uma escolha precisa fazer sentido com outra','Coerência metodológica no caso didático',[
 ('PROBLEMA','Construção de explicações\nem uma turma e um período.'),
 ('REFERÊNCIAS','Conceitos e literatura ajudam\na formular e interpretar.'),
 ('DESENHO E FONTES','Por que este caso, estes\nmateriais e estes momentos?'),
 ('CRITÉRIOS E ALCANCE','Como analisar as relações?\nO que se pode concluir?')
],'Citar uma técnica não demonstra, sozinho, toda essa articulação.')

four('u15-fontes.png','O que cada fonte ajuda a conhecer?','O confronto exige autoria, contexto, finalidade e recorte',[
 ('MAPA','Posições, conexões e escolhas\nde representação.'),
 ('RELATO','Perspectivas e interpretações\nproduzidas em uma situação.'),
 ('REGISTRO DE AULA','Mediações, intervenções\ne condições observadas.'),
 ('PRODUÇÃO DO ESTUDANTE','Relações construídas em\numa tarefa identificada.')
],'As fontes são parciais; divergências também precisam ser analisadas.')

im,d=base('Da categoria à distribuição','DADOS FICTÍCIOS · mesmos 20 pares · grade autoral')
for box,title,values in [
 ((52,235,624,570),'MOMENTO INICIAL',[8,6,6]),
 ((656,235,1228,570),'MOMENTO FINAL',[2,4,14])
]:
    panel(d,box,PALE if values[0]==8 else BLUE)
    x0,y0,x1,y1=box
    label(d,title,(x0+10,y0+7,x1-10,y0+60),32,True)
    for j,(name,count) in enumerate(zip(['R0 · enumera','R1 · descreve','R2 · relaciona com fonte'],values)):
        y=y0+76+j*65
        label(d,name,(x0+12,y,x1-100,y+56),26,False)
        label(d,str(count),(x1-95,y,x1-14,y+56),36,True)
    label(d,'TOTAL: 20',(x0+20,y1-58,x1-20,y1-7),30,True)
label(d,'Distribuições não mostram, sozinhas, trajetórias individuais ou causas.',(45,585,1235,645),24,True)
save(im,'u15-analise.png')

four('u15-ciclo.png','Investigar a ação para rever a prática','Ciclo didático: acompanhar, refletir e voltar ao planejamento',[
 ('PLANEJAR','Delimitar problema, critérios,\nparticipação e intervenção.'),
 ('AGIR E REGISTRAR','Realizar a ação e documentar\ncondições e acontecimentos.'),
 ('ANALISAR E REFLETIR','Confrontar evidências,\ndificuldades e alternativas.'),
 ('REPLANEJAR','Justificar mudanças e\nacompanhar novo ciclo.')
],'Uma atividade diferente não comprova, por si, pesquisa-ação.')

four('u15-evidencia.png','O que sustenta a afirmação?','Um argumento construído com o exemplo fictício',[
 ('AFIRMAÇÃO DELIMITADA','Mais produções atenderam\nao critério R2 no final.'),
 ('EVIDÊNCIA','6 de 20 no início;\n14 de 20 no final.'),
 ('RACIOCÍNIO','Critérios e registros ajudam\na interpretar as relações.'),
 ('ALCANCE','Esse conjunto e essas condições;\nsem causa exclusiva demonstrada.')
],'Pergunta, evidência e raciocínio precisam permanecer relacionados.')

path=ROOT/'content/media-sources.json';sources=json.loads(path.read_text())
names={c['filename'] for c in credits}
sources=[s for s in sources if s['filename'] not in names]+credits
path.write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
print(f'{len(credits)} esquemas da unidade 1.5 verificados em 16:9.')


