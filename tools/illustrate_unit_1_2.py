"""Seis esquemas exatos em 16:9; as legendas completas ficam no conteúdo."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT/'content/media'
W, H = 1280, 720
P = dict(bg='#f4f1e8', ink='#173f36', green='#2f7464', gold='#d2a452', pale='#e8eedd', line='#cdd9cc', blue='#e5edef')


def font(size, bold=False):
    name = 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
    return ImageFont.truetype(name, size)


def lines(d, words, xy, size=38, bold=False, fill=None, spacing=10):
    f = font(size, bold)
    x, y = xy
    for row in words.split('\n'):
        d.text((x, y), row, font=f, fill=fill or P['ink'])
        y += size + spacing


def centered(d, words, box, size=38, bold=False, fill=None):
    rows = words.split('\n')
    x0, y0, x1, y1 = box
    f = font(size, bold)
    while size > 24 and max(d.textlength(row, font=f) for row in rows) >= x1-x0-14:
        size -= 1
        f = font(size, bold)
    spacing = size+10
    top = y0+(y1-y0-len(rows)*spacing)/2
    for row in rows:
        width = d.textlength(row, font=f)
        assert width < x1-x0-14, (row, width, x1-x0)
        d.text((x0+(x1-x0-width)/2, top), row, font=f, fill=fill or P['ink'])
        top += spacing


def base(title, subtitle):
    im = Image.new('RGB', (W, H), P['bg'])
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((48, 38, 214, 80), radius=12, fill=P['green'])
    d.text((62, 43), 'UNIDADE 1.2', font=font(18, True), fill='#ffffff')
    lines(d, title, (58, 105), 48, True)
    lines(d, subtitle, (60, 168), 26)
    d.line((60, 665, 1220, 665), fill=P['line'], width=2)
    d.text((60, 681), 'PROFGEO  /  ESQUEMA DIDÁTICO AUTORAL', font=font(17, True), fill=P['green'])
    return im, d


def panel(d, box, fill='#ffffff'):
    x0, y0, x1, y1 = box
    d.rounded_rectangle((x0+3, y0+5, x1+3, y1+5), radius=24, fill='#e5e5d9')
    d.rounded_rectangle(box, radius=24, fill=fill, outline=P['line'], width=2)


def arrow(d, x0, x1, y):
    d.line((x0, y, x1-10, y), fill=P['green'], width=6)
    d.polygon([(x1, y), (x1-15, y-12), (x1-15, y+12)], fill=P['green'])


def save(im, filename):
    MEDIA.mkdir(exist_ok=True)
    assert im.size == (1280, 720)
    temp = MEDIA/(filename+'.tmp')
    im.save(temp, format='PNG', optimize=True)
    with Image.open(temp) as check:
        check.verify()
    temp.replace(MEDIA/filename)
    return dict(filename=filename, author='ProfGeo', license='Ilustração didática autoral',
                source='tools/illustrate_unit_1_2.py', changes='Esquema original em 1280 × 720; proporção 16:9.')


credits = []
im, d = base('Quatro saberes, uma prática', 'Procure o destaque da decisão de ensino.')
for x, y, title, body, letter in [
    (60, 232, 'Disciplinar', 'Compreender e investigar\na matéria.', 'D'),
    (660, 232, 'Curricular', 'Selecionar objetivos\ne progressão.', 'C'),
    (60, 420, 'Da experiência', 'Aprender e rever\nno trabalho.', 'E'),
    (660, 420, 'Da ação pedagógica', 'Tornar público e investigar\no saber da experiência.', 'A')]:
    panel(d, (x, y, x+560, y+166))
    d.ellipse((x+22, y+26, x+74, y+78), fill=P['green'])
    centered(d, letter, (x+22, y+22, x+74, y+80), 28, True, '#ffffff')
    lines(d, title, (x+93, y+20), 34, True)
    lines(d, body, (x+30, y+80), 30, spacing=6)
centered(d, 'Os saberes se articulam na aula.', (60, 600, 1220, 650), 31, True)
credits.append(save(im, 'u12-quatro-saberes.png'))


im, d = base('Da orientação à aprendizagem', 'Uma organização possível para analisar o planejamento.')
labels = ['Orientação\ncurricular', 'Objetivo\nda aula', 'Situação\nde ensino', 'Evidência\nde\naprendizagem']
for i, label in enumerate(labels):
    x = 60+i*298
    panel(d, (x, 265, x+265, 493), '#ffffff' if i%2==0 else P['pale'])
    centered(d, label, (x+10, 284, x+255, 470), 31, True)
    if i<3:
        arrow(d, x+271, x+291, 380)
panel(d, (90, 536, 1190, 621), P['ink'])
centered(d, 'Seleção + progressão + avaliação', (106, 549, 1174, 610), 36, True, '#ffffff')
credits.append(save(im, 'u12-caminho-curricular.png'))


im, d = base('Aprender ao observar a prática', 'Exemplo fictício: a turma ignora a legenda do mapa.')
for i, (label, body) in enumerate([
    ('Observar', 'Identificar\na dificuldade.'),
    ('Intervir', 'Comparar\njustificativas.'),
    ('Rever', 'Retomar e\nverificar de novo.')]):
    x = 64+i*399
    panel(d, (x, 258, x+354, 493), '#ffffff' if i!=1 else P['pale'])
    centered(d, label, (x+16, 273, x+338, 335), 40, True)
    centered(d, body, (x+14, 348, x+340, 471), 32)
    if i<2:
        arrow(d, x+363, x+386, 370)
d.line((1040, 520, 1040, 577, 239, 577, 239, 520), fill=P['green'], width=5)
d.polygon([(239, 508), (226, 526), (252, 526)], fill=P['green'])
centered(d, 'A experiência pode ser revista.', (295, 585, 1124, 644), 31, True)
credits.append(save(im, 'u12-experiencia-reflexao.png'))


im, d = base('Ação pedagógica em Gauthier', 'A publicização e a investigação fazem parte do sentido do termo.')
for i, label in enumerate(['Experiência\nprivada', 'Prática\nexplicitada', 'Exame público\npor pesquisas']):
    x = 64+i*399
    panel(d, (x, 272, x+354, 495), P['pale'] if i==2 else '#ffffff')
    centered(d, label, (x+10, 299, x+344, 468), 37, True)
    if i<2:
        arrow(d, x+363, x+386, 382)
panel(d, (96, 540, 1184, 626), P['ink'])
centered(d, 'Divulgar, por si só, não é validar.', (115, 552, 1165, 615), 37, True, '#ffffff')
credits.append(save(im, 'u12-acao-pedagogica.png'))


im, d = base('O que as respostas mostram?', 'Caso fictício: A tem 8 km / 45 min; B tem 15 km / 25 min.')
for i, (title, body, step) in enumerate([
    ('Resposta 1', '“A é mais rápida:\né mais curta.”', 'Retomar medidas'),
    ('Resposta 2', '“B leva 25 min;\nA, 45 min.”', 'Ampliar a relação'),
    ('Resposta 3', '“B: menor tempo,\nmaior distância.”', 'Discutir o limite')]):
    x = 64+i*399
    panel(d, (x, 252, x+354, 555), P['pale'] if i==2 else '#ffffff')
    centered(d, title, (x+12, 267, x+342, 328), 34, True)
    centered(d, body, (x+12, 337, x+342, 466), 31)
    d.line((x+27, 480, x+327, 480), fill=P['line'], width=2)
    centered(d, step, (x+12, 491, x+342, 545), 26, True)
centered(d, 'Reconheça o avanço e indique o próximo passo.', (60, 584, 1220, 647), 32, True)
credits.append(save(im, 'u12-evidencias.png'))


im, d = base('Investigar a prática de ensino', 'Registre decisões e evidências para que possam ser examinadas.')
for i, label in enumerate(['Problema\ndelimitado', 'Intervenção\ndescrita', 'Evidências\nanalisadas', 'Resultados\ne limites']):
    x = 60+i*298
    panel(d, (x, 273, x+265, 498), '#ffffff' if i%2==0 else P['pale'])
    centered(d, label, (x+8, 302, x+257, 470), 32, True)
    if i<3:
        arrow(d, x+271, x+291, 387)
panel(d, (100, 544, 1180, 626), P['ink'])
centered(d, 'Examinar antes de generalizar.', (120, 554, 1160, 615), 38, True, '#ffffff')
credits.append(save(im, 'u12-investigar-pratica.png'))


photo_credits = [
    dict(filename='u12-sala-aula.jpg', commonsFile='Escola Técnica de Paulínia (ETEP) - sala de aula.jpg',
         author='Alebasi24', license='CC BY-SA 4.0', licenseUrl='https://creativecommons.org/licenses/by-sa/4.0/',
         source='https://commons.wikimedia.org/wiki/File:Escola_T%C3%A9cnica_de_Paul%C3%ADnia_(ETEP)_-_sala_de_aula.jpg',
         changes='Imagem redimensionada para 1280 × 720; fotografia original em 16:9.'),
    dict(filename='u12-rio-guama.jpg', commonsFile='Vista do Rio Guamá a partir do campus da Universidade Federal do Pará, Belém, setembro de 2019 (2).jpg',
         author='Fronteira', license='CC BY-SA 4.0', licenseUrl='https://creativecommons.org/licenses/by-sa/4.0/',
         source='https://commons.wikimedia.org/wiki/File:Vista_do_Rio_Guam%C3%A1_a_partir_do_campus_da_Universidade_Federal_do_Par%C3%A1,_Bel%C3%A9m,_setembro_de_2019_(2).jpg',
         changes='Imagem redimensionada para 1280 × 720; fotografia original em 16:9.')]

path = ROOT/'content/media-sources.json'
sources = json.loads(path.read_text())
new = photo_credits+credits
names = {c['filename'] for c in new}
sources = [c for c in sources if c['filename'] not in names]+new
path.write_text(json.dumps(sources, ensure_ascii=False, indent=2)+'\n')
print('Seis esquemas autorais em 16:9; fontes de duas fotografias cadastradas.')
