"""Revisão 2 da unidade 1.1: explicação encadeada e situações resolvidas.

O pacote r1 preserva enunciados e IDs anteriores, usados sem reinterpretação
dos resultados já salvos. O simulado novo possui identificadores próprios.
"""
import copy
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with zipfile.ZipFile(ROOT/'content/packages/1.1-r1.zip') as archive:
    ORIGINAL = json.loads(archive.read('unit.json'))


def text(title, body):
    return dict(type='text', title=title, body=body)


def call(title, body, warning=False):
    return dict(type='callout', title=title, body=body, tone='warning' if warning else 'tip')


def table(title, headers, rows):
    return dict(type='table', title=title, headers=headers, rows=rows)


def compare(title, a, at, b, bt):
    return dict(type='compare', title=title, left=dict(title=a, body=at), right=dict(title=b, body=bt))


def anim(kind, title, caption):
    return dict(type='animation', kind=kind, title=title, caption=caption)


def photo(src, title, caption, credit):
    return dict(type='photo', src='media/'+src, title=title, caption=caption, credit=credit)


def match(title, pairs):
    return dict(type='match', title=title, pairs=pairs)


def order(title, items):
    return dict(type='order', title=title, items=items)


lessons = []


def lesson(n, title, kicker, minutes, blocks, summary, practice):
    lessons.append(dict(id=f'l{n:02d}', title=title, kicker=kicker, minutes=minutes,
                        blocks=blocks, summary=summary, practice=practice))


lesson(1, 'Da informação à explicação geográfica', 'Qual problema vamos aprender a explicar?', 13, [
    text('O fio que vai ligar a unidade', 'Você vai estudar maneiras de compreender o espaço e as consequências dessas escolhas para o ensino. A pergunta central é: por que olhar o mesmo lugar pode produzir explicações e aulas diferentes? Ao final, você deverá conseguir analisar uma proposta de ensino e justificar a concepção que a orienta.\nVamos acompanhar uma situação inventada: duas comunidades vivem próximas de um rio e seus alunos precisam chegar à escola no período chuvoso. Em uma área, há acesso estruturado; na outra, o trajeto apresenta mais obstáculos. A chuva é parte do problema, mas a diferença entre os acessos pede uma explicação. Este caso didático não é um diagnóstico de uma comunidade real.'),
    text('Informar e explicar são trabalhos diferentes', 'Uma informação responde, por exemplo, qual é o rio ou onde fica a escola. Uma explicação procura mostrar relações: como o trajeto, a chuva, o transporte e as condições da via participam da dificuldade de chegar à escola. A informação pode ser correta e necessária sem, ainda, responder ao problema.\nPense em uma fotografia de uma estrada com água. Ela permite observar uma condição naquele registro. Para explicar os acessos diferentes, precisamos investigar também usos da via, obras e decisões. A diferença entre observar e explicar será importante em todas as concepções estudadas.'),
    call('Antes de mexer na cena', 'Preveja: se a chuva continuar igual e uma condição de acesso melhorar, o efeito sobre o trajeto precisa permanecer o mesmo? Formule sua hipótese antes de escolher “Infraestrutura melhorada”.'),
    anim('inequality', 'Uma chuva, duas condições de acesso', 'Compare “Acesso vulnerável” e “Infraestrutura melhorada”. Observe o que muda na via e na circulação. A cena é hipotética: ilustra uma relação, sem calcular riscos nem garantir que uma obra resolva todo problema.'),
    text('Leia o resultado com raciocínio', 'A melhoria representada altera uma condição do acesso, enquanto o evento natural continua fazendo parte da situação. Portanto, a dificuldade não pode ser atribuída apenas à presença da chuva. É necessário relacionar condições naturais e formas de organização do espaço.\nO raciocínio foi: identificar o problema, comparar condições, observar uma diferença e formular uma explicação que considere a relação entre elas. Isso é mais consistente que concluir “a chuva explica tudo” ou “a natureza não importa”.'),
    compare('Uma primeira questão resolvida', 'Resposta incompleta', '“As aulas são prejudicadas porque chove.” Identifica um fator, mas não explica por que trajetos próximos podem apresentar dificuldades diferentes.', 'Resposta ampliada', '“A chuva interage com as condições das vias e dos transportes. Para entender os acessos, precisamos comparar essas condições e investigar como foram constituídas.”'),
    text('Por que isso muda o ensino?', 'Se o objetivo for nomear o rio, o professor pode verificar o reconhecimento do nome. Se for explicar diferenças de acesso, precisará propor comparações, oferecer fontes e pedir justificativas. A maneira de compreender o espaço participa, assim, da escolha do que o estudante deverá aprender a fazer.\nNomes e localizações ajudam a situar a investigação. O limite aparece quando a aula termina na lista e não ensina a estabelecer relações.'),
    call('Transfira a ideia', 'Troque a escola por uma feira: saber o nome da estrada explica sozinho a chegada dos produtos? Não. Precisamos relacionar trajetos, condições de circulação e abastecimento. Você usou o mesmo raciocínio em outra situação.'),
    text('Seu percurso', 'Na lição 2, você vai dar nome às escolhas que acabamos de fazer: teoria, método, metodologia de ensino e recurso. Nas lições 3 a 8, vai comparar concepções. Depois, vai transformar essa compreensão em uma aula, investigar outro lugar e resolver situações de prova. Ao terminar cada leitura, explique a ideia com suas palavras antes da prática.')
], 'Uma informação localiza ou descreve; uma explicação relaciona condições e processos. Uma concepção geográfica orienta o que buscamos explicar e quais relações o aluno será ajudado a construir.', order('Reconstrua o raciocínio do caso', [
    'Identificar que o problema é a diferença de acesso à escola.',
    'Comparar chuva, trajetos e condições das vias.',
    'Relacionar o evento natural à organização do acesso.',
    'Justificar a explicação e indicar o que ainda precisa ser investigado.' ]))

lesson(2, 'Teoria, método e ensino: o que muda?', 'Dê sentido aos termos do edital', 16, [
    text('Agora podemos nomear nossas escolhas', 'Na lição anterior, você percebeu que “chove” não explica sozinho os acessos diferentes. Ao procurar infraestrutura, transporte e decisões, passou a escolher relações importantes para compreender o espaço. Essa escolha tem uma dimensão teórica. Teoria não é um palpite pessoal: envolve conceitos e argumentos para construir e discutir explicações.\nUma concepção teórico-metodológica reúne uma maneira de compreender o objeto e um modo de investigá-lo. A parte teórica ajuda a perguntar o que conta na explicação; a metodológica ajuda a justificar como se chega a ela. O título do edital pede, assim, mais que reconhecer nomes de correntes.'),
    text('Método: como sustentar a explicação?', 'Suponha que investigamos se diferenças nas vias participam da dificuldade de chegar à escola. Precisamos definir o que comparar, quais fontes consultar e como confrontar a hipótese com as informações. Um relato indica uma dificuldade; mapas, registros e outras observações ajudam a examinar seu alcance.\nEsse caminho faz parte do método. Ele não é apenas a lista “entrevista, fotografia e mapa”: essa lista reúne procedimentos ou fontes. O método envolve a lógica que dá sentido à escolha e à interpretação deles.'),
    table('Siga uma decisão de ponta a ponta', ['Plano da decisão', 'Aplicação ao caso'], [
        ['Teoria: como compreender o espaço?', 'Investigar como decisões sociais e condições materiais participam dos acessos desiguais.'],
        ['Método: como investigar?', 'Comparar trajetos, examinar sua história e confrontar fontes sobre circulação e infraestrutura.'],
        ['Metodologia de ensino: como ajudar a aprender?', 'Pedir uma hipótese, orientar a comparação e discutir as explicações construídas pela turma.'],
        ['Recurso: com que apoio?', 'Mapa dos trajetos, fotografias, tabela e relatos.']]),
    compare('A mesma ferramenta, duas aulas', 'Uso 1 do mapa', 'A turma copia nomes das vias e a posição da escola. O mapa apoia uma tarefa de identificação.', 'Uso 2 do mapa', 'A turma compara acessos, relaciona condições das vias e justifica diferenças. O mapa participa de uma investigação explicativa.'),
    text('Resolva a confusão mais frequente', 'Ser digital não diz qual concepção orienta o mapa. Uma tabela pode apoiar um modelo de distribuição ou uma análise crítica da desigualdade. Uma entrevista pode investigar vivências do lugar ou fornecer dados sobre relações de trabalho. A diferença está no problema e na função das informações na explicação.\nUma exposição do professor também não impede, por si só, a aprendizagem ativa. Ele pode explicar um conceito para que os alunos o usem em uma comparação. Analise o conjunto da proposta, não apenas um recurso ou um momento isolado.'),
    text('Dois termos que agora fazem sentido', 'Epistemologia é a reflexão sobre como produzimos e justificamos conhecimento. Perguntar “por que uma fotografia permite observar o trajeto, mas não provar a causa da desigualdade?” é enfrentar um problema epistemológico. O termo nomeia uma reflexão sobre evidência e explicação que você já começou a fazer.\nParadigma se refere a um quadro de referências compartilhadas que orienta problemas e formas de explicação em uma comunidade científica. Ajuda a compreender por que certos modos de pesquisar se fortalecem e passam a ser questionados. Não significa que todos os pesquisadores de uma época pensem igual.'),
    call('Verificação com resposta explicada', '“Vou organizar um debate com a turma.” Isso define uma concepção geográfica? Ainda não. Define parte de uma estratégia de ensino. Para analisar a concepção, precisamos saber qual problema será debatido e com quais conceitos, fontes e relações.'),
    text('Ponte para as próximas lições', 'Para cada concepção, procure três respostas: qual problema ela destaca, como constrói sua explicação e que aprendizagem pode orientar na escola. Esse encadeamento permitirá comparar natureza, regiões, modelos, produção do espaço e experiência do lugar.')
], 'Teoria orienta a compreensão; método organiza a investigação; metodologia de ensino organiza a aprendizagem; recurso oferece apoio. Eles se articulam, mas um mapa ou um debate não define sozinho a concepção.', match('Associe a decisão ao seu papel', [
    ['Interpretar relações de poder no território', 'Concepção teórica'],
    ['Relacionar processos e confrontar explicações', 'Método de investigação'],
    ['Organizar perguntas e intervenções do professor', 'Metodologia de ensino'],
    ['Utilizar um mapa digital', 'Recurso didático']]))

lesson(3, 'Natureza e sociedade: determinismo e possibilismo', 'Uma condição natural é um destino social?', 20, [
    text('Retome nossa primeira explicação', 'Agora analise a resposta: “As comunidades próximas ao rio terão sempre a mesma dificuldade porque o ambiente decide sua vida”. Ela reconhece o rio, mas transforma uma condição em resultado inevitável. Como explicaria grupos que usam técnicas e organizam acessos diferentes?\nEssa dificuldade ajuda a compreender o debate entre determinismo ambiental e possibilismo, tradicionalmente apresentado no estudo da Geografia moderna. Primeiro entenda a lógica; depois situe os nomes históricos.'),
    text('Por que esse debate surgiu?', 'No século XIX, a Geografia se institucionalizou em universidades, sociedades científicas e sistemas de ensino, em contextos de formação dos Estados nacionais e expansão colonial. Conhecer territórios, comparar áreas e explicar relações entre sociedade e natureza eram problemas importantes. Esse contexto ajuda a compreender as perguntas, sem tornar todas as obras daquela época iguais.\nAs histórias da ciência e da disciplina escolar se relacionam, mas a escola não é apenas uma cópia posterior de uma teoria universitária. Finalidades educativas e mediação também participam da construção do conteúdo escolar, como veremos na lição 9.'),
    compare('Duas lógicas de explicação', 'Determinismo ambiental', 'Uma condição natural é tomada como causa decisiva de características sociais. O limite é tratá-la como destino e reduzir a análise das mediações históricas e sociais.', 'Possibilismo', 'O meio oferece condições e possibilidades, mobilizadas de modos distintos por grupos humanos, por técnicas e práticas historicamente constituídas.'),
    text('Autores e contexto, sem caricaturas', 'Friedrich Ratzel é tradicionalmente associado ao debate determinista; Paul Vidal de la Blache, à escola francesa e ao possibilismo. Essas associações são referências de estudo, não resumos suficientes de toda a obra de cada autor. Nem toda consideração da natureza é determinismo; possibilismo não quer dizer que a sociedade pode fazer qualquer coisa.\nA noção de gêneros de vida, associada à tradição vidaliana, ajuda a estudar formas de relação entre grupos e meio por práticas e técnicas constituídas ao longo do tempo. Não significa um modo de vida imutável, nem elimina limitações materiais.'),
    call('Use a cena para testar uma explicação', 'Em “Rio como destino”, identifique a relação que foi apagada. Depois mude para “Rio + práticas sociais” e explique por que a presença do mesmo rio não obriga todos os grupos a organizar a vida da mesma maneira.'),
    anim('river', 'O rio participa da vida, mas não a decide sozinho', 'Compare as técnicas e práticas representadas. Os cenários hipotéticos ajudam a distinguir condição natural, mediação técnica e explicação de destino inevitável.'),
    text('Caso resolvido: “o clima explica o atraso”', 'Primeiro, identifique o resultado que a frase tenta explicar: uma condição social definida como “atraso”. Segundo, identifique a causa apresentada: o clima. Terceiro, examine “inevitável”: essa palavra dispensa investigar história, acesso à terra, técnicas, trabalho e decisões políticas. O defeito está na redução, não no simples fato de mencionar o clima.\nUma resposta mais consistente reconhece as condições naturais e investiga como se combinam a processos sociais. Não precisa afirmar que chuva e relevo não importam. Condicionar uma atividade e determinar sozinho sua organização são afirmações diferentes.'),
    text('Transforme a compreensão em uma aula', 'O professor pode apresentar dois usos distintos das margens de um rio e pedir hipóteses. Orienta a comparação de técnicas, trajetos e organização, usando fontes além da imagem. A aprendizagem aparece quando o aluno deixa de repetir “é assim porque tem rio” e consegue explicar as mediações.\nEm uma questão, associe a concepção com base nesse motivo. O nome decorado, sem a lógica da explicação, deixa o conhecimento frágil diante de um caso novo.'),
    call('Ligação com a lição 4', 'Para comparar usos das margens, precisamos observar, descrever e definir critérios. Como esses procedimentos podem contribuir para explicar as áreas, sem terminar em uma lista?')
], 'Determinismo ambiental transforma condições naturais em resultados sociais necessários. O possibilismo destaca condições, técnicas e práticas históricas, sem supor liberdade ilimitada. O nome do autor não substitui a análise da explicação.', match('Qual ideia está sendo enfatizada?', [
    ['O clima tornaria inevitável uma característica social.', 'Lógica determinista'],
    ['Condições semelhantes são mobilizadas de maneiras distintas.', 'Lógica possibilista'],
    ['Modos de relação com o meio se constituem em práticas históricas.', 'Gêneros de vida'],
    ['A obra de um autor não cabe em uma frase de manual.', 'Cuidado com a simplificação histórica']]))

lesson(4, 'Descrever e comparar regiões', 'Quando observar ajuda a explicar?', 16, [
    text('A descrição é um começo necessário', 'Na lição 3, você comparou relações com o meio. Antes de explicar uma diferença, alguém precisa observar o que se parece e o que varia. Descrever é produzir uma apresentação organizada do objeto estudado.\nO limite surge quando a descrição vira explicação completa. Dizer que uma área possui rio, estrada e feira identifica elementos. Falta perguntar como se articulam: de que modo as condições dos acessos participam do abastecimento da feira, por exemplo.'),
    text('O que se chama Geografia tradicional?', 'A expressão reúne tradições diferentes. Observação, descrição, classificação e diferenciação de áreas são aspectos recorrentes. A Geografia regional procurou compreender combinações de características de áreas, não apenas escrever inventários sem relação. Uma prática escolar de memorização pode ser criticada sem reduzir toda essa produção científica a uma lista.\nEmpirismo destaca a importância da experiência e da observação na produção do conhecimento. O positivismo, influente em parte desse debate, valoriza o estudo de fatos e relações observáveis. Não são dois nomes intercambiáveis para toda a Geografia tradicional. O problema de uma descrição limitada aparece quando os dados parecem falar sozinhos: reunir características não explica automaticamente sua organização.'),
    compare('Passe do inventário ao problema', 'Inventário inicial', '“Há três comunidades, duas escolas, uma estrada e um rio.” São elementos que podem integrar a análise.', 'Pergunta explicativa', '“Como os acessos conectam as comunidades às escolas, e quais diferenças aparecem no período chuvoso?” Agora os elementos entram em relações.'),
    text('Região: um recorte precisa de critério', 'Organize comunidades segundo o principal acesso à escola: fluvial ou terrestre. Esse é um critério. Se o critério mudar para participação em um circuito de comercialização, os agrupamentos podem mudar: comunidades com acessos distintos podem vender na mesma feira.\nO limite da região depende também do problema que orienta o recorte. Isso não torna qualquer divisão igualmente adequada. É necessário explicitar o critério, mostrar as informações utilizadas e verificar se o recorte ajuda a compreender o fenômeno.'),
    table('Exercício resolvido de regionalização', ['Decisão', 'Por que ela importa'], [
        ['Pergunta: como se organiza o acesso à escola?', 'Define o fenômeno a analisar.'],
        ['Critério: principal rede de acesso utilizada.', 'Permite justificar o agrupamento.'],
        ['Fontes: trajetos, mapas e relatos confrontados.', 'Sustentam e permitem discutir o recorte.'],
        ['Novo critério: circuito de abastecimento.', 'Pode produzir outra regionalização, adequada a outra pergunta.']]),
    text('Como isso aparece no ensino?', 'A tarefa pode começar por localizar comunidades e classificar trajetos. O professor pede, então, a justificativa do agrupamento e sua comparação com outro critério. O aluno aprende a organizar informações e a compreender que representar uma região envolve escolhas fundamentadas.\nSe a tarefa termina em decorar uma divisão como a única possível, a aprendizagem fica restrita. A diferença entre as propostas é o trabalho intelectual solicitado, não a presença de um mapa regional.'),
    call('Explique sem olhar a tabela', 'Por que regiões climáticas e áreas de influência de uma cidade podem ter limites diferentes? Porque seus critérios e relações de análise diferem. Uma mudança de limite não prova que um dos mapas esteja errado.'),
    text('A pergunta que abre a lição 5', 'Alguns geógrafos buscaram ir além da descrição de cada área para explicar regularidades entre muitas áreas. Para isso, enfatizaram modelos, hipóteses e medidas. Agora vamos entender como esses elementos constroem uma investigação.')
], 'Observar e descrever ajudam a construir o problema. Regionalizar exige critérios e fontes. A aprendizagem avança quando o aluno justifica o recorte e relaciona processos, em vez de apenas decorar um inventário.', match('Relacione cada decisão à sua função', [
    ['Identificar rios, escolas e vias.', 'Descrição inicial'],
    ['Agrupar áreas pelo principal acesso utilizado.', 'Critério de regionalização'],
    ['Explicar a relação entre acesso e circulação.', 'Análise de relações'],
    ['Considerar o recorte o único possível para qualquer pergunta.', 'Limite a ser revisto']]))

lesson(5, 'Modelos e padrões: a Geografia quantitativa', 'Como formular e testar uma hipótese?', 19, [
    text('Da área particular à busca de regularidades', 'A lição 4 mostrou como descrever e diferenciar áreas. Agora pergunte: existem relações que ajudam a explicar a distribuição de serviços entre vários lugares? A Geografia teórico-quantitativa, fortalecida em meados do século XX, enfatizou modelos, hipóteses e padrões espaciais.\nO ponto não é apenas usar números. Um modelo seleciona relações e simplifica uma situação para investigá-las. Uma hipótese é uma resposta provisória, que precisa ser confrontada com dados. A passagem dos dados à explicação deve ser discutida, não presumida.'),
    text('Entenda o termo neopositivismo', 'A referência ao neopositivismo, importante nesse debate, ajuda a compreender a valorização da formulação lógica, das hipóteses verificáveis e da busca de regularidades. Em vez de conhecer cada área somente por suas particularidades, examinam-se relações que possam ser formuladas e testadas explicitamente.\nAlguém define as variáveis, escolhe os dados e interpreta os resultados; o computador não toma essas decisões sozinho. Explanation in Geography, livro de David Harvey publicado em 1969, integra esse momento de discussão metodológica. Autores também podem mudar de orientação ao longo de sua trajetória.'),
    call('Faça uma previsão', 'Hipótese didática: “Entre as rotas da cena, a de menor distância terá menor tempo de viagem”. Escolha A, depois B. Compare os dois tipos de medida antes de decidir se a hipótese se sustenta neste caso.'),
    anim('quantitative', 'O dado testa uma hipótese', 'Dados inventados: rota A, 8 km e 45 minutos; rota B, 15 km e 25 minutos. Não são medições de comunidades reais. Comparar distância não é o mesmo que comparar tempo.'),
    text('Resolução passo a passo', 'A é menor em distância: 8 é menor que 15. Porém, leva mais tempo: 45 minutos contra 25. Os dados desse caso não sustentam a previsão de que menor distância corresponde a menor tempo. A comparação pede considerar meio de transporte, condições do trajeto e outras relações pertinentes.\nFormular uma hipótese, deduzir uma consequência e confrontá-la com dados ilustra um raciocínio hipotético-dedutivo. Não se resume a realizar uma operação de cálculo.\nVocê não provou que a estrada é sempre mais rápida que o rio. Examinou uma hipótese em duas rotas fictícias. Generalizar uma relação exige outros dados e critérios. Distinguir resultado situado de afirmação universal ajuda a resolver questões.'),
    table('Outro exemplo: duas médias iguais', ['Conjunto fictício de tempos', 'Leitura'], [
        ['Grupo X: 20, 30 e 40 minutos.', 'Média: 30 minutos. Os três valores estão próximos desse resumo.'],
        ['Grupo Y: 5, 5 e 80 minutos.', 'Média: 30 minutos. Um trajeto muito longo fica escondido pelo resumo.'],
        ['Os dois têm média de 30 minutos.', 'Isso não significa condições iguais. É necessário examinar a distribuição.']]),
    text('Como ensinar esse raciocínio?', 'O professor pede uma previsão, oferece dados e orienta a comparação entre o previsto e o observado. A aprendizagem aparece quando o aluno explica por que manteve ou reviu a hipótese, quais medidas usou e até onde a conclusão vale. Somar corretamente é parte da tarefa, mas não substitui a interpretação.\nUma tabela também pode alimentar uma análise crítica da desigualdade. O papel do modelo na explicação, e não apenas a presença de números, é o que estamos analisando.'),
    call('O problema que permanece', 'Uma comparação mostra quais trajetos são longos. Mas por que determinadas áreas receberam certos investimentos, quem se beneficia dos fluxos e como se constituíram as diferenças? A lição 6 aprofunda essas perguntas.')
], 'Modelos e hipóteses ajudam a explicar padrões espaciais. Os dados precisam de interpretação: a média pode ocultar diferenças e uma comparação não autoriza qualquer generalização.', match('Reconheça as partes da investigação', [
    ['Menor distância corresponderia a menor tempo.', 'Hipótese a examinar'],
    ['Selecionar distância e tempo para representar a relação.', 'Construção do modelo'],
    ['Comparar 8 km / 45 min e 15 km / 25 min.', 'Confronto com os dados'],
    ['Não estender duas rotas a todas as estradas e rios.', 'Limite da conclusão']]))

lesson(6, 'Produção do espaço: as Geografias críticas', 'Como as diferenças se constituem?', 20, [
    text('Faça uma pergunta nova ao resultado', 'Você identificou acessos diferentes e viu como medidas mostram padrões. Agora pergunte como esses acessos foram produzidos: quem decidiu abrir a via, a que atividades atende e como os investimentos foram distribuídos? A desigualdade deixa de ser apenas uma diferença registrada e passa a ser um problema histórico e social.\nGeografias críticas designa vertentes que questionam interpretações que tratam a organização espacial como neutra ou natural. Não formam uma escola homogênea. Muitas dialogam com o materialismo histórico e dialético; compreender essa referência ajuda a analisar suas explicações.'),
    text('Histórico e dialético em uma situação concreta', 'Histórico indica que a situação presente foi construída ao longo do tempo: a estrada resulta de projetos, técnicas, trabalho e decisões. Dialético chama atenção para relações e contradições: a mesma via pode facilitar a circulação de mercadorias e não assegurar transporte adequado a todos os moradores.\nNão basta reunir causas independentes. É preciso examinar como produção, trabalho, Estado e outras relações se articulam na organização espacial. No caso da escola, pode-se investigar como a distribuição de infraestrutura se relaciona às atividades econômicas e às escolhas públicas. A resposta depende de evidências, não de uma conclusão antecipada.'),
    photo('ver-o-peso.jpg', 'Da forma visível às relações que a organizam', 'No Ver-o-Peso, em Belém, observamos uma paisagem de circulação e comércio. Investigar trabalho, abastecimento e decisões exige outras fontes. A foto não demonstra renda nem condições individuais dos sujeitos.', 'Fabio Gomes · Wikimedia Commons · CC BY-SA 4.0'),
    text('Objetos e ações: uma contribuição de Milton Santos', 'Milton Santos propõe compreender o espaço pela relação indissociável entre sistemas de objetos e sistemas de ações. É preciso estudar a materialidade com os usos e as relações que lhe dão funcionamento. Estrada, ponte e escola não são formas separadas da circulação, do trabalho e das decisões que as conectam.\n“Sistemas” também importa: não estamos somando objetos sem relação. Uma escola integra trajetos, serviços e práticas; uma feira participa de redes de abastecimento. Para compreender uma forma, investigamos como opera nessas relações e como sua função pode mudar.'),
    compare('Caso resolvido: criticar e explicar', 'Denúncia sem desenvolvimento', '“O acesso é injusto.” A frase expressa uma avaliação, mas ainda não explica como a diferença foi constituída.', 'Investigação crítica', '“Vamos comparar onde foram implantadas as vias, quais fluxos atendem e que decisões participaram dessa distribuição.” A proposta indica relações e fontes a investigar.'),
    text('Uma aula crítica precisa ensinar a argumentar', 'O professor reúne mapas de acessos, registros de obras e relatos. A turma compara fontes, analisa quem é atendido e justifica uma interpretação. Conceitos são oferecidos, e explicações concorrentes também devem ser examinadas.\nRepetir a opinião do professor não demonstra, por si só, aprendizagem crítica. Um avanço seria explicar uma relação entre investimento, circulação e acesso, apoiando-a nas fontes e reconhecendo o que ainda não se sabe. Exposição conceitual e dados quantitativos podem ajudar esse trabalho.'),
    call('Verifique sua compreensão', 'Por que números não eliminam o caráter crítico de uma investigação? Porque medidas podem apoiar o estudo da desigualdade. O foco crítico aparece no problema da produção social, das relações e contradições que os dados ajudam a investigar.'),
    text('O que ainda queremos compreender?', 'Investigar produção e poder não elimina a experiência das pessoas. A mesma praça pode integrar uma rede de trabalho e ter sentidos diferentes para seus usuários. A lição 7 muda o foco para compreender como o lugar é vivido, sem afirmar que sua materialidade desapareceu.')
], 'Uma análise crítica investiga como o espaço foi produzido, suas relações de poder e contradições. Em Milton Santos, objetos e ações são indissociáveis. Denunciar ou repetir uma opinião não substitui explicar relações com evidências.', order('Construa uma investigação crítica possível', [
    'Identificar uma diferença de acesso que precisa ser explicada.',
    'Examinar fontes sobre vias, usos, investimentos e decisões.',
    'Relacionar essas informações à produção social do espaço.',
    'Justificar a interpretação e discutir seus limites com a turma.' ]))

lesson(7, 'Experiência e lugar: a Geografia humanística', 'Como o espaço é vivido pelas pessoas?', 18, [
    text('Mude o foco sem abandonar o que aprendeu', 'Na lição 6, você investigou a organização material e social do espaço. Agora imagine que duas pessoas percorrem o mesmo caminho: uma reconhece encontros, lembranças e segurança; outra relata medo ou afastamento. A distância medida não explica sozinha essa diferença de experiência.\nA perspectiva humanística enfatiza como as pessoas percebem, vivenciam e atribuem sentidos aos lugares. Yi-Fu Tuan é uma referência desse debate. A pergunta não é apenas onde a pessoa está, mas como sua relação com aquele espaço se constitui na experiência.'),
    text('O que a fenomenologia ajuda a perguntar?', 'A fenomenologia, referência importante para vertentes humanísticas, orienta a atenção ao modo como o mundo é vivido e ganha sentido para o sujeito. Em vez de tomar o lugar como um ponto neutro que seria igual para todos, investigamos como se apresenta na experiência.\nIsso não significa que qualquer impressão substitua uma explicação ou que o espaço material deixe de existir. Uma entrevista precisa ser situada: quem fala, de qual experiência, em que momento e com quais relações? Um relato não representa automaticamente todos os moradores.'),
    call('Antes de ouvir os personagens', 'Na praça da cena, preveja: trabalhar, encontrar amigos e recordar a infância precisam produzir o mesmo sentido de lugar? Escolha os três relatos e procure o vínculo que cada um enfatiza.'),
    anim('lived', 'A mesma praça, três experiências', 'Use os botões “Pessoa 1”, “Pessoa 2” e “Pessoa 3”. As falas são fictícias. Compare os sentidos de trabalho, pertencimento, memória e dificuldade; não os transforme em retratos de grupos inteiros.'),
    text('Resolva o exemplo', 'A primeira pessoa destaca relações de trabalho; outra, encontro e pertencimento; a terceira reúne memória e dificuldade de circulação. A praça não mudou de localização entre as falas. Mudou a experiência narrada e a relação que está sendo analisada.\nÉ por isso que o lugar não se esgota em coordenadas. Também não precisa ser sempre acolhedor: familiaridade, afeto, conflito e desconforto podem coexistir. Conhecer um sentimento não dispensa perguntar em quais condições ele se constitui.'),
    compare('Humanística e crítica: qual é a pergunta principal?', 'Experiência do lugar', '“Como a estudante vive o caminho e que sentidos atribui a ele?” O foco recai sobre experiência, percepção e significado.', 'Produção e relações de poder', '“Como investimentos e usos organizaram acessos diferentes?” O foco recai sobre constituição social, decisões e contradições.'),
    text('Da investigação à aprendizagem', 'O professor pode pedir mapas mentais dos trajetos, solicitar que os alunos expliquem suas escolhas e comparar o que cada representação destaca. O objetivo não é escolher o desenho mais bonito, mas compreender o lugar vivido e usar conceitos para interpretá-lo.\nUm avanço ocorre quando o aluno percebe que sua experiência não é a única, compara sentidos e justifica sua interpretação. Se a atividade termina apenas na coleção de histórias, a formação conceitual ainda precisa ser trabalhada.'),
    call('Ponte para a lição 8', 'Viver um lugar e produzir uma imagem pública dele são problemas próximos, mas distintos. A seguir, vamos investigar por que uma propaganda pode apresentar um lugar de maneira muito diferente daquela vivida por parte de seus moradores.')
], 'A perspectiva humanística investiga experiência, percepção e significados do lugar. As vivências precisam ser contextualizadas; lugar não é apenas coordenada nem necessariamente um espaço de harmonia.', match('Identifique o foco de cada investigação', [
    ['Como se sente e que memórias tem quem percorre a praça?', 'Experiência e sentidos do lugar'],
    ['Que decisões e relações produziram acessos desiguais?', 'Produção social do espaço'],
    ['Que trajetos têm tempos semelhantes?', 'Padrão de distribuição'],
    ['O que um mapa mental enfatiza para quem o produziu?', 'Representação do vivido']]))

lesson(8, 'Cultura e representações do espaço', 'Quem mostra o lugar e o que fica de fora?', 18, [
    text('Uma nova pergunta sobre o mesmo espaço', 'Você compreendeu que uma praça pode ser vivida de maneiras diferentes. Agora imagine uma campanha fictícia que mostra a Amazônia apenas como floresta sem habitantes. O problema já não é somente como uma pessoa vive o lugar. Precisamos perguntar como se produz e circula uma representação que seleciona certos elementos e omite outros.\nAs abordagens culturais investigam práticas, símbolos, identidades e representações em suas relações com o espaço. Existem tradições diferentes nessa área; não se trata de um conjunto único de respostas nem de estudar apenas festas e costumes.'),
    text('Representar é fazer escolhas', 'Uma imagem não contém o lugar inteiro. Alguém seleciona enquadramento, palavras, personagens e temas. Essas escolhas podem favorecer uma ideia de natureza vazia, cidade moderna, lugar perigoso ou destino turístico. Por isso, interessa saber quem representa, para quem e com quais possíveis efeitos.\nExaminar a omissão de cidades e comunidades em uma propaganda não permite adivinhar a intenção individual de seu autor. Permite analisar o que o material mostra, o que deixa de mostrar e como isso participa da compreensão pública do espaço.'),
    compare('Não confunda duas perguntas', 'Humanística', '“O que a feira significa na experiência de quem trabalha nela?” Investiga o vínculo vivido pelo sujeito.', 'Cultural', '“Como a feira é representada em uma campanha, e quais sujeitos aparecem?” Investiga a produção e circulação de sentidos e representações.'),
    table('Leia uma campanha fictícia em quatro passos', ['Passo', 'Aplicação'], [
        ['1. Identificar o material.', 'Campanha turística com imagens de floresta.'],
        ['2. Examinar a seleção.', 'Que elementos aparecem? Cidades e atividades de moradores estão ausentes?'],
        ['3. Comparar outras representações.', 'Consultar imagens, narrativas e fontes produzidas em outros contextos.'],
        ['4. Justificar a interpretação.', 'Explicar que ideia de Amazônia o conjunto favorece, com base na análise dos materiais.']]),
    text('Por que cultura não é uma caixa fixa?', 'As práticas mudam, são discutidas e variam dentro dos grupos. Afirmar que todo ribeirinho, indígena ou agricultor vive do mesmo modo transforma uma categoria social em personagem único. Uma investigação precisa perguntar pelas diferenças e pelas relações, não confirmar um retrato pronto.\nDa mesma forma, analisar um símbolo ou uma imagem não dispensa sua dimensão material e histórica. Sentidos, práticas e relações de poder podem se cruzar; a distinção de foco serve para orientar a pergunta, não para impedir qualquer diálogo entre abordagens.'),
    text('Como ensinar essa leitura?', 'O professor pode colocar a campanha fictícia ao lado de fontes que apresentem cidades, trabalho e vivências. Os alunos identificam escolhas, comparam materiais e justificam uma interpretação. O objetivo é aprender a ler representações espacialmente situadas, e não apenas dizer se a imagem é bonita ou feia.\nA avaliação pode pedir que analisem outra campanha: conseguem reconhecer a seleção e apoiar a conclusão em elementos do material? Essa transferência mostra mais compreensão do que decorar “cultura = costumes”.'),
    call('Retome antes de avançar', 'Até aqui, você mudou a pergunta para examinar condições naturais, regiões, padrões, produção do espaço, experiências e representações. Agora precisamos compreender como o professor transforma essas formas de pensar em aprendizagem geográfica.')
], 'As abordagens culturais investigam práticas e representações espaciais, perguntando por seleção, diferenças e produção de sentidos. Humanística e cultural podem dialogar, mas não são nomes intercambiáveis.', match('Qual pergunta está sendo feita?', [
    ['Que vínculo uma moradora relata com sua praça?', 'Experiência do lugar'],
    ['Quem aparece e quem é omitido em uma campanha?', 'Seleção da representação'],
    ['Por que não presumir uma vida igual para todo um grupo?', 'Diversidade interna'],
    ['Que elementos do material sustentam minha interpretação?', 'Justificação da análise']]))

lesson(9, 'Como transformar essas ideias em aprendizagem', 'Cotidiano, conceito e mediação', 21, [
    text('Conhecer a concepção não basta para ensinar', 'Você já dispõe de perguntas e modos de explicar o espaço. Mas entregar uma definição de “produção do espaço” ou “lugar vivido” não garante que o aluno aprenda a usá-la. É necessário organizar uma situação em que a definição faça trabalho na interpretação de um problema.\nA Geografia escolar dialoga com conhecimentos científicos, experiências, currículos e condições de ensino. Não é somente uma versão menor de um livro universitário. O professor seleciona e organiza conhecimentos para finalidades educativas e acompanha como os estudantes os compreendem.'),
    text('Diferencie dois planos da discussão', 'Uma concepção geográfica orienta como compreender o espaço. Uma concepção pedagógica orienta como compreender a aprendizagem e organizar o ensino. Elas se articulam, mas não formam uma única lista. “Geografia crítica” e “perspectiva histórico-cultural” não são dois nomes para a mesma classificação.\nNa discussão histórico-cultural mobilizada por Lana Cavalcanti, a mediação ajuda a articular conhecimentos cotidianos e científicos na formação de conceitos. O estudante participa da construção do conhecimento; o professor intervém intencionalmente. Participação ativa não exige que o aluno descubra tudo sozinho.'),
    call('Acompanhe uma explicação em construção', 'O ponto de partida será “na chuva, fica difícil chegar à escola”. Antes de escolher as etapas da cena, pense: o que o professor precisa acrescentar para o relato se tornar uma explicação geográfica?'),
    anim('mediation', 'Do relato à explicação: acompanhe a mudança', 'Percorra “1. Relato”, “2. Pergunta”, “3. Conceito” e “4. Explicação”. Observe o que cada intervenção acrescenta ao pensamento do aluno. A cena apresenta uma possibilidade, não um roteiro obrigatório para qualquer aula.'),
    text('O que mudou em cada etapa?', 'O relato identifica uma experiência importante, mas ainda pouco diferenciada. A pergunta orienta a comparação: que trajetos e grupos são mais afetados? Os conceitos de redes, acesso e circulação ajudam a interpretar relações entre caminhos, serviços e condições. A explicação final articula esses elementos.\nNote que o professor não apenas pediu que os alunos falassem. Ele forneceu instrumentos para pensar. Também não descartou o relato: ajudou a retomá-lo com maior poder explicativo. Essa mudança é a conexão entre cotidiano e conceito.'),
    compare('Caso resolvido: dois resultados de aula', 'Reprodução verbal', 'O aluno recita: “rede é um conjunto de pontos interligados”. Ainda não sabemos se consegue usar essa ideia para analisar um acesso.', 'Uso conceitual', 'O aluno explica como escola, comunidade e trajetos se conectam, indica um ponto de interrupção e justifica como isso altera a circulação.'),
    text('Faça a aprendizagem ir além do exemplo', 'Depois da análise do acesso escolar, o professor apresenta o abastecimento de uma feira. Pergunta quais pontos e caminhos se conectam e como uma interrupção pode alterar a circulação. Se os alunos mobilizam as relações em outra situação, há uma evidência de generalização do conceito.\nA avaliação deve procurar essa ampliação da compreensão. Participar, desenhar e gostar da atividade são informações relevantes, mas não demonstram sozinhas que o estudante aprendeu a explicar. A exposição conceitual e a orientação de uma tarefa podem ser necessárias para esse avanço.'),
    call('Ponte para a lição 10', 'A mediação precisa de operações concretas: localizar, comparar, reconhecer distribuições e estabelecer conexões. Vamos agora organizar essas operações em uma investigação, entendendo para que serve cada uma.')
], 'A mediação relaciona experiência e conceitos, com ação intencional do professor e atividade intelectual do estudante. A compreensão aparece quando o aluno usa o conceito para explicar uma situação, inclusive além do primeiro exemplo.', order('Organize uma sequência de mediação', [
    'Levantar como os estudantes percebem os trajetos.',
    'Formular uma pergunta sobre acesso e circulação.',
    'Comparar fontes e mobilizar conceitos geográficos.',
    'Construir uma explicação e avaliar o que se aprendeu.' ]))

lesson(10, 'Como construir uma explicação geográfica', 'Localizar, comparar, conectar e mudar a escala', 18, [
    text('Dê função às operações de pensamento', 'Na lição 9, o conceito ajudou a ampliar uma explicação. Para construí-la, o aluno precisa fazer algo com as informações. Localizar, reconhecer distribuições, comparar e relacionar escalas são operações que organizam a investigação. Não são palavras para recitar sem um problema.\nVamos usá-las no caso do acesso: onde ficam as escolas e os trajetos? As dificuldades estão concentradas ou dispersas? Que condições diferenciam os acessos? Com quais decisões e fluxos esses lugares se conectam? Cada pergunta acrescenta uma relação à análise.'),
    table('Uma operação, uma contribuição', ['Operação', 'O que acrescenta ao caso'], [
        ['Localizar', 'Situar escola, comunidades e caminhos; reconhecer posição e acessos relativos.'],
        ['Examinar a distribuição', 'Verificar onde se concentram trajetos mais longos ou dificuldades.'],
        ['Comparar', 'Usar critérios comuns para analisar semelhanças e diferenças.'],
        ['Estabelecer conexões', 'Relacionar caminhos, transportes, serviços e decisões.'],
        ['Articular escalas de análise', 'Investigar relações que ultrapassam um trajeto ou uma comunidade.']]),
    call('Antecipe a mudança de escala', 'Um caminho está em uma comunidade, mas a decisão sobre uma via ou um serviço pode ultrapassar esse recorte. Na cena, observe o que se torna visível ao passar de comunidade para município e rede regional.'),
    anim('scale', 'O lugar participa de relações mais amplas', 'Escolha “Comunidade”, “Município” e “Rede regional”. As conexões são hipotéticas. Explique que problema cada recorte ajuda a investigar; não se limite a dizer que a imagem ficou maior.'),
    text('Caso resolvido: não confunda recorte e isolamento', 'No recorte da comunidade, observamos trajetos e experiências próximas. Ao analisar o município, podemos comparar a distribuição de serviços. Na rede regional, surgem relações de abastecimento e circulação que ajudam a explicar o funcionamento de lugares próximos. Uma análise local não obriga a ignorar essas conexões.\nMudar a escala de análise não é apenas afastar a imagem. O avanço ocorre quando reconhecemos processos e relações que aquele recorte permite investigar. Um mapa mais abrangente pode continuar sendo usado só para listar nomes, sem produzir essa articulação.'),
    compare('Duas escalas, dois sentidos', 'Escala cartográfica', 'É a relação de proporção entre distâncias no mapa e no terreno. Ajuda a compreender a representação e seu grau de redução.', 'Escala geográfica de análise', 'Diz respeito ao recorte e às relações dos processos investigados: comunidade, município ou rede regional, por exemplo.'),
    text('Como avaliar uma explicação?', 'Uma resposta forte indica a diferença observada, utiliza conceitos pertinentes e justifica relações com as fontes. Se o aluno afirma “a estrada é importante”, falta dizer para qual circulação e sob quais condições. Se explica como uma interrupção afeta o acesso e conecta a situação à rede de serviços, a ideia ficou mais determinada.\nO professor pode apresentar outro recorte e perguntar o que muda na explicação. Isso permite avaliar o uso das operações de pensamento, sem supor que aumentar o número de lugares citados seja o mesmo que compreender mais.'),
    call('O próximo desafio', 'Você já tem instrumentos para investigar. Na lição 11, vai aplicá-los a outro lugar e comparar concepções diante da mesma fotografia. O objetivo é transferir o raciocínio, sem depender da cena da escola.')
], 'Operações de pensamento ganham sentido quando ajudam a responder a um problema. Articular escalas é investigar relações entre recortes; não é apenas mudar o zoom nem confundir análise com proporção cartográfica.', order('Organize esta investigação possível', [
    'Definir uma pergunta sobre diferenças no acesso.',
    'Localizar e comparar os trajetos com critérios e fontes.',
    'Relacionar a distribuição às conexões e escalas pertinentes.',
    'Construir uma explicação e examinar seus limites.' ]))

lesson(11, 'Uma situação, diferentes concepções', 'Laboratório explicado do Ver-o-Peso', 23, [
    text('Agora o caso é outro', 'Chegou o momento de verificar se você compreendeu além do exemplo inicial. Vamos estudar uma paisagem de feira. Antes de nomear uma concepção, separe o que a fotografia permite observar daquilo que exigiria outras informações. Depois compare que perguntas orientariam cada investigação.\nA mudança para o Ver-o-Peso testa sua capacidade de transferir o raciocínio: a relação entre problema, fonte e explicação continua válida, embora o lugar e as atividades sejam outros.'),
    photo('belem-feira.jpg', 'Observe o registro e reconheça seus limites', 'A fotografia do Ver-o-Peso, em Belém, mostra um recorte da paisagem. Formas e práticas visíveis ajudam a iniciar perguntas; renda, condições de trabalho e trajetórias pessoais não podem ser deduzidas pela aparência dos sujeitos.', 'Cayambe · Wikimedia Commons · CC BY-SA 3.0'),
    table('Acompanhe cinco percursos', ['Foco', 'Pergunta, fonte e explicação procurada'], [
        ['Descrição e diferenciação de áreas', 'Que elementos e usos caracterizam a feira? Observações e representações ajudam a descrever e comparar sua organização.'],
        ['Teórico-quantitativo', 'Que padrão de fluxos pode ser explicado por um modelo? Dados de origem, distância e tempo permitem testar relações.'],
        ['Crítico', 'Como trabalho, decisões e relações de poder organizam o abastecimento? Documentos, dados e relatos ajudam a investigar sua produção social.'],
        ['Humanístico', 'Como diferentes sujeitos vivem e significam a feira? Narrativas contextualizadas ajudam a compreender experiências do lugar.'],
        ['Cultural', 'Como a feira é representada e quem aparece nas imagens públicas? A comparação de materiais permite analisar seleções e sentidos.']]),
    call('Use a animação como exercício de comparação', 'A cena oferece quatro escolhas sintéticas. Em cada uma, explique o foco da pergunta e indique uma informação que a imagem não fornece. A representação cultural, estudada na lição 8, deve ser comparada também pela tabela, sem supor que tenha um botão próprio.'),
    anim('lenses', 'Mudar a pergunta muda a investigação', 'Compare “Descrever”, “Medir padrões”, “Investigar poder” e “Ouvir experiências”. São sínteses para orientar o estudo; não classificam automaticamente toda aula em uma etiqueta.'),
    text('Caso resolvido: uma pesquisa com números e entrevistas', 'Considere uma investigação fictícia que usa dados de transporte e entrevistas para compreender como decisões sobre circulação beneficiam grupos de maneiras distintas. A presença dos números não determina uma concepção quantitativa, e a entrevista não determina uma concepção humanística. O foco explicativo é a constituição das diferenças e das relações de poder, aproximando o caso de uma análise crítica.\nSe a pergunta principal fosse como os trabalhadores vivem a feira e constroem vínculos com ela, o foco mudaria para a experiência do lugar. O tipo de fonte poderia ser parecido; sua função na explicação seria outra.'),
    text('É possível dialogar entre abordagens?', 'Perguntas podem se aproximar, e fontes diferentes podem contribuir para um problema comum. Isso exige explicitar o que cada uma permite investigar e como as interpretações se articulam. Somar uma tabela, uma fala e uma foto não produz coerência por si só.\nAs concepções também possuem pressupostos e limites. Não é necessário afirmar que todas dizem a mesma coisa, nem escolher uma única técnica para cada corrente. O exercício é justificar a relação entre pergunta, conceito, procedimento e conclusão.'),
    compare('Como uma aula pode usar esse laboratório', 'Tarefa restrita', 'Pedir que a turma copie os elementos da fotografia e memorize uma lista de correntes.', 'Tarefa de compreensão', 'Pedir que formule um problema, selecione fontes, explique uma relação e justifique qual foco orienta sua análise.'),
    call('Retomada sem consulta', 'Explique a diferença entre ouvir o significado da feira para uma pessoa e analisar como a feira aparece em uma campanha. Se conseguiu distinguir experiência vivida e seleção da representação, já está relacionando as lições 7 e 8 em um caso novo.')
], 'Reconheça a concepção pela função dos conceitos e das fontes na explicação. A mesma paisagem permite perguntas distintas; combinar fontes exige coerência e reconhecer os limites de cada uma.', match('Qual pergunta combina com cada foco?', [
    ['Que formas e usos caracterizam a feira?', 'Descrição da paisagem'],
    ['Como se distribuem os fluxos de abastecimento?', 'Padrões e modelos'],
    ['Que relações organizam trabalho e acesso?', 'Produção social e poder'],
    ['Que sentidos as pessoas atribuem à feira?', 'Experiência do lugar']]))

lesson(12, 'Resolver questões e construir um argumento', 'Do raciocínio estudado à prova', 24, [
    text('Como estudar esta síntese', 'Você percorreu uma explicação: partiu de um problema, distinguiu teoria e método, comparou concepções e investigou como ensinar esse raciocínio. Agora vai aplicar a sequência à leitura de questões e à escrita. Tente formular uma resposta antes de ler cada resolução.\nO treino desta unidade cobre o item 1.1. O Anexo III também contém outros temas. Os exemplos e o simulado são autorais: não reproduzem questões oficiais nem permitem prever a cobrança da seleção.'),
    table('Compare pela lógica, não pela palavra isolada', ['Foco estudado', 'O que procurar na explicação'], [
        ['Determinismo ambiental', 'Uma condição natural transformada em destino social necessário.'],
        ['Possibilismo', 'Condições e possibilidades mobilizadas por práticas e técnicas históricas.'],
        ['Tradições regionais', 'Observação, critérios, combinações e diferenciação de áreas.'],
        ['Teórico-quantitativo', 'Modelo e hipótese para explicar padrões e regularidades.'],
        ['Crítico', 'Produção social do espaço, relações de poder e contradições.'],
        ['Humanístico', 'Experiência, percepção e sentidos do lugar.'],
        ['Cultural', 'Práticas, representações, identidades e produção de sentidos espaciais.']]),
    call('Questão resolvida 1 — pense antes de ler', 'Uma aula compara gráficos de tempo de transporte e documentos sobre investimentos para discutir a produção de acessos desiguais. O uso dos gráficos permite classificá-la automaticamente como teórico-quantitativa?'),
    text('Resolução 1: encontre o papel da fonte', 'Primeiro, identifique o problema: como os acessos desiguais foram produzidos. Segundo, veja a função dos dados: apoiar a investigação de investimentos e de seus efeitos sobre grupos. Terceiro, reconheça que os gráficos não decidem a concepção. O foco está próximo de uma leitura crítica, embora utilize técnicas quantitativas.\nUma alternativa que diga “todo gráfico é quantitativo, portanto a aula não pode ser crítica” confunde técnica e concepção. Uma alternativa adequada deve justificar a relação entre o problema e a explicação.'),
    call('Questão resolvida 2 — compare dois objetivos', 'Uma turma entrevista moradores sobre lembranças e pertencimento à praça. Outra compara campanhas que mostram a praça sem seus trabalhadores. Que diferença de foco ajuda a analisar as duas propostas?'),
    text('Resolução 2: não classifique pela entrevista ou pela imagem', 'No primeiro objetivo, procure a experiência e os sentidos do lugar para sujeitos concretos: é um foco humanístico. No segundo, procure a seleção e a circulação de uma representação: é um foco cultural. Os temas podem dialogar, mas a distinção está na pergunta principal.\nSe o enunciado informar apenas que foram feitas entrevistas ou usadas fotografias, faltam elementos para decidir com segurança. Não acrescente ao caso uma intenção que ele não apresentou.'),
    text('Questão discursiva: construa um argumento', 'Considere o tema de treino da oficina: como concepções teórico-metodológicas podem orientar práticas que ultrapassem a memorização. Comece com uma tese que responda ao tema. Em seguida, explique uma concepção ou conceito, analise uma situação de ensino e indique uma evidência de aprendizagem.\nUm planejamento possível é: defender a importância de explicar relações; esclarecer uma perspectiva crítica do acesso; descrever como a turma compararia fontes e mobilizaria conceitos; concluir pelo avanço na capacidade de justificar uma interpretação. É necessário mostrar por que a atividade ensina, e não apenas citar o nome de um jogo ou aplicativo.'),
    compare('Uma escrita mais determinada', 'Afirmação genérica', '“A Geografia crítica é importante e os alunos precisam participar.” A frase não explica conceito, intervenção nem aprendizagem.', 'Argumento desenvolvido', '“Ao relacionar condições de circulação e decisões públicas, os alunos podem explicar acessos desiguais. O professor orienta a comparação de fontes e avalia se conseguem justificar essas relações.”'),
    call('Como usar o treino da unidade', 'Há 56 questões de prática e um simulado novo de 20 situações, com comentários para todas as alternativas. Faça o simulado sem consultar a síntese; depois, explique o motivo de cada erro e releia a lição correspondente. As perguntas da versão anterior continuam na prática, com seus identificadores preservados.'),
    text('Organize a revisão pela dificuldade', 'Se confunde recurso e concepção, volte à lição 2. Se reconhece os nomes mas não explica as diferenças, compare os casos das lições 3 a 8. Se sabe a teoria mas não sabe como ensiná-la, retome as intervenções e evidências das lições 9 a 11. Use os cartões para recuperar as relações e a oficina para construir uma resposta própria.\nNo edital enviado, o treino envolve questões objetivas e redação de até 20 linhas. O modelo da oficina é um exemplo comentável, não um texto para repetir em qualquer tema. Seu objetivo é conseguir explicar, comparar e aplicar com autonomia.')
], 'Na prova, identifique problema, explicação e função das fontes antes de nomear a concepção. Na redação, articule tese, conceito, intervenção e evidência de aprendizagem. Uma palavra-chave ou um recurso não substitui esse raciocínio.', order('Organize um argumento didático', [
    'Apresentar uma tese que responda ao tema.',
    'Explicar um conceito relevante.',
    'Analisar uma situação de ensino com esse conceito.',
    'Concluir relacionando ensino e aprendizagem.' ]))

# O histórico das questões anteriores mantém seu sentido e seu gabarito.
questions = copy.deepcopy(ORIGINAL['questions'])
previous_final_lessons = {
    'f01':'l01', 'f02':'l01', 'f03':'l05', 'f04':'l06', 'f05':'l07',
    'f06':'l08', 'f07':'l09', 'f08':'l02', 'f09':'l03', 'f10':'l03',
    'f11':'l05', 'f12':'l10', 'f13':'l09', 'f14':'l08', 'f15':'l09',
    'f16':'l04', 'f17':'l11', 'f18':'l11', 'f19':'l12', 'f20':'l11'
}
for question in questions:
    if question['id'] in previous_final_lessons:
        question['lesson'] = previous_final_lessons[question['id']]
        question['pool'] = 'lesson'


def final(n, lesson_n, stem, options, answer, feedback, tag):
    assert len(options) == len(feedback) == 4
    questions.append(dict(id=f'r2f{n:02d}', lesson=f'l{lesson_n:02d}', stem=stem,
                          options=options, answer=answer, feedback=feedback,
                          tag=tag, pool='final', type='single'))

# Simulado novo: casos com resolução individual de todas as alternativas.
final(1, 2, 'Uma professora usa um mapa digital, uma tabela e entrevistas para investigar como decisões sobre transporte produziram acessos desiguais à escola. Que elemento permite reconhecer melhor a concepção geográfica da proposta?',
      ['A quantidade de ferramentas utilizadas na comparação.', 'A centralidade das decisões e relações sociais na explicação do acesso.', 'O suporte digital como definidor de uma orientação quantitativa.', 'A presença de relatos como definidora de uma orientação humanística.'], 1,
      ['Combinar ferramentas informa os recursos, mas ainda é necessário analisar a função deles no problema.', 'O foco explicativo é a produção social das diferenças. Dados e relatos podem contribuir para essa investigação crítica.', 'O mapa digital pode apoiar orientações diferentes; sua tecnologia não determina a explicação construída.', 'Relatos também podem ser fontes de uma investigação crítica. É preciso examinar para que são utilizados.'], 'teoria e recursos')
final(2, 3, 'Ao estudar dificuldades de circulação, um texto afirma que o relevo torna inevitável a mesma organização social em todas as comunidades da área. Qual revisão enfrenta o limite dessa explicação?',
      ['Substituir a análise do relevo pela descrição dos nomes das comunidades.', 'Tratar as diferenças observadas como exceções sem interesse para a análise.', 'Reconhecer o relevo e investigar como técnicas, história e relações sociais medeiam seus efeitos.', 'Adotar a ideia de que condições naturais não participam de nenhuma atividade social.'], 2,
      ['Mudar para uma lista de nomes não explica as mediações que a afirmação deixou de analisar.', 'As diferenças ajudam a questionar a necessidade do resultado e precisam ser investigadas.', 'A revisão conserva a importância da condição natural e recusa transformá-la em causa social suficiente.', 'A resposta troca uma redução por outra. Recusar o destino ambiental não implica negar a natureza.'], 'determinismo e mediações')
final(3, 3, 'Duas comunidades próximas do mesmo rio organizam trajetos diferentes por técnicas e práticas construídas historicamente. Uma análise possibilista do caso deveria:',
      ['Examinar as condições e possibilidades mobilizadas, sem presumir liberdade ilimitada.', 'Tomar as técnicas como prova de independência completa em relação ao meio.', 'Atribuir as duas organizações ao mesmo resultado necessário do ambiente.', 'Transformar cada modo de vida em uma característica permanente de seus habitantes.'], 0,
      ['A análise destaca a relação entre condições do meio e práticas e técnicas históricas, conservando seus limites.', 'Possibilismo não equivale a autonomia completa diante de condições materiais e naturais.', 'A resposta apresenta uma lógica de determinação necessária, e não a análise das possibilidades mobilizadas.', 'Os modos de relação com o meio são históricos; não devem ser tratados como identidades imóveis.'], 'possibilismo')
final(4, 4, 'Um estudo agrupa comunidades pela rede de acesso à escola. Outro as agrupa pelo circuito de comercialização. Os mapas têm limites diferentes. Que conclusão é mais consistente?',
      ['O primeiro recorte elimina a pertinência de qualquer regionalização comercial.', 'Os limites diferentes indicam que os dois estudos usaram informações incorretas.', 'A regionalização comercial independe de problema e de critérios explicitados.', 'A adequação de cada recorte depende do problema, dos critérios e das fontes.'], 3,
      ['Duas perguntas podem justificar recortes distintos, sem que uma torne a outra desnecessária.', 'Diferenças de limites podem resultar de critérios diferentes, não necessariamente de erro nos dados.', 'O critério e as fontes também precisam ser explicitados e discutidos nesse estudo.', 'A comparação pede examinar a finalidade de cada regionalização, e não exigir limites iguais para problemas distintos.'], 'região e critérios')
final(5, 4, 'A turma começa localizando escolas e classificando trajetos, depois justifica os critérios e investiga relações com a circulação. Como analisar a contribuição da descrição?',
      ['A descrição fornece uma base que é mobilizada e ampliada na explicação.', 'A classificação impede o desenvolvimento posterior de relações conceituais.', 'A descrição da primeira etapa demonstra que a sequência inteira é memorização.', 'A investigação final dispensa conferir as informações produzidas na observação.'], 0,
      ['A proposta usa observação e classificação como etapas relacionadas a uma pergunta explicativa.', 'Classificar pode apoiar a análise quando os critérios e as relações são discutidos.', 'É necessário analisar o percurso: a sequência não termina no reconhecimento de elementos.', 'A explicação precisa voltar às evidências, não abandonar sua verificação.'], 'descrição e explicação')
final(6, 5, 'A hipótese era que a menor distância corresponderia ao menor tempo. Nos dados fictícios, a rota C tem 4 km e 35 minutos; D tem 9 km e 20 minutos. Qual conclusão respeita o teste?',
      ['A hipótese foi confirmada porque C tem menor distância.', 'Os dados do caso não sustentam a hipótese e sugerem examinar outras condições do trajeto.', 'A comparação demonstra que a relação entre distância e tempo nunca pode ser investigada.', 'O resultado permite concluir que o transporte de D será mais rápido em qualquer situação.'], 1,
      ['A hipótese se refere à relação com o tempo; comparar apenas as distâncias não basta.', 'D tem maior distância e menor tempo. Isso contraria a previsão do caso, sem autorizar uma regra universal.', 'Uma previsão não sustentada ajuda a rever o modelo; não torna a relação impossível de estudar.', 'O resultado vale para os dados e condições apresentados. Generalizações exigem outros critérios e evidências.'], 'hipóteses e modelos')
final(7, 5, 'Dois grupos fictícios têm tempos de viagem P = 10, 20 e 60 minutos; Q = 25, 30 e 35 minutos. As médias são de 30 minutos. O que essa igualdade permite afirmar?',
      ['As distribuições e as dificuldades individuais são equivalentes.', 'O grupo P não apresenta tempo muito diferente dos demais.', 'O grupo Q não pode ser comparado a P porque possui outra distribuição.', 'O resumo é igual, mas a distribuição precisa ser examinada antes de concluir sobre o acesso.'], 3,
      ['A média igual não elimina a diferença entre os valores e as condições de cada grupo.', 'P contém um trajeto de 60 minutos, muito acima dos outros dois do conjunto.', 'A diferença de distribuição é precisamente uma informação relevante para a comparação.', 'Os resumos são iguais e os valores se distribuem de maneira diferente. A interpretação exige considerar ambos.'], 'média e distribuição')
final(8, 6, 'Uma via facilita o transporte de mercadorias, mas parte dos moradores continua com acesso escolar precário. Qual pergunta desenvolve uma análise crítica dessa situação?',
      ['Que nome da estrada a turma deve memorizar antes da avaliação?', 'Qual relato individual permite dispensar todas as outras fontes?', 'Como a via foi produzida, quais usos privilegia e que relações explicam os efeitos diferentes?', 'Que característica natural torna necessários os mesmos efeitos para todos os usuários?'], 2,
      ['O nome ajuda a identificar a via, mas não desenvolve a explicação dos efeitos socialmente diferentes.', 'Um relato é uma fonte situada e não substitui sozinho a investigação das relações.', 'A pergunta investiga produção, usos, interesses e contradições, em vez de presumir neutralidade da infraestrutura.', 'A formulação pressupõe uma determinação que não enfrenta a diferença descrita no caso.'], 'produção do espaço')
final(9, 6, 'Um antigo armazém passa a funcionar como escola e integra novos fluxos de estudantes e serviços. À luz da relação entre objetos e ações, a análise deveria:',
      ['Tratar o prédio como espaço de função inalterável por conservar parte de sua forma.', 'Relacionar sua materialidade às práticas e às redes que passam a lhe dar funcionamento.', 'Reduzir o novo funcionamento à mudança de nome na fachada.', 'Substituir o estudo da materialidade pela enumeração das opiniões sobre o prédio.'], 1,
      ['Uma forma material pode integrar ações e funções que se transformam historicamente.', 'A contribuição estudada pede compreender objetos e ações de modo indissociável e relacional.', 'O novo funcionamento envolve práticas, usos e conexões que não se esgotam no nome.', 'Reconhecer as ações não implica eliminar os objetos e suas condições materiais da análise.'], 'objetos e ações')
final(10, 7, 'Duas pessoas percorrem a mesma praça: uma a descreve como lugar de encontro; outra, como lugar de desconforto e lembranças difíceis. Para um estudo humanístico, é pertinente:',
      ['Examinar como as experiências situadas constituem sentidos diferentes do lugar.', 'Escolher um relato e tratá-lo como sentido comum a todos os moradores.', 'Usar a localização idêntica para desconsiderar as diferenças de experiência.', 'Tomar o desconforto como prova de que a praça não pode ser considerada lugar.'], 0,
      ['O estudo considera os vínculos vividos e seus contextos, sem reduzir o lugar às coordenadas.', 'Um relato não representa automaticamente todos os sujeitos; as diferenças também precisam ser compreendidas.', 'A mesma posição não torna idênticas as relações vividas com aquele espaço.', 'Lugar não precisa significar harmonia: memória, conflito e desconforto podem participar da experiência.'], 'experiência do lugar')
final(11, 8, 'Uma campanha apresenta uma região como paisagem natural sem habitantes. Qual procedimento desenvolve uma análise cultural da representação?',
      ['Adotar o material como reprodução completa da região.', 'Deduzir pela ausência que a região de fato não possui habitantes.', 'Examinar seleção, contexto e público, comparando outras fontes e os sentidos produzidos.', 'Avaliar a campanha pelo número de elementos naturais, dispensando os critérios de enquadramento.'], 2,
      ['Uma representação seleciona elementos; precisa ser analisada em seu contexto e alcance.', 'A omissão no registro não demonstra ausência no espaço representado.', 'O procedimento analisa o que a representação favorece ou apaga e sustenta a interpretação na comparação.', 'Contar elementos pode descrever o material, mas não examina por si só a produção de sentidos.'], 'representações culturais')
final(12, 8, 'Uma atividade investiga o significado da feira para trabalhadores; outra analisa como a feira aparece em propagandas. Como distinguir seus focos principais?',
      ['A primeira é quantitativa porque envolve trabalho; a segunda é regional porque usa imagens.', 'As duas têm a mesma pergunta porque tratam da mesma localização.', 'A presença de pessoas nas duas elimina qualquer diferença entre seus objetivos.', 'A primeira enfatiza experiência do lugar; a segunda, seleção e circulação de representações.'], 3,
      ['Trabalho e imagem não definem, isoladamente, os focos explicativos propostos.', 'O lugar pode ser o mesmo, enquanto problema, fonte e explicação procurada mudam.', 'É necessário analisar para que se investigam os sujeitos e os materiais, não apenas reconhecer sua presença.', 'A distinção permite compreender perguntas humanísticas e culturais sem negar que possam dialogar.'], 'comparação de abordagens')
final(13, 9, 'Alunos dizem que a estrada “fica ruim” na chuva. O professor pede comparações, oferece os conceitos de rede e circulação e acompanha a revisão das explicações. O que caracteriza essa mediação?',
      ['A articulação intencional entre experiência cotidiana e instrumentos conceituais.', 'A substituição do conhecimento do aluno por uma definição sem aplicação.', 'A retirada do professor para que cada estudante descubra todos os conceitos sozinho.', 'A identificação automática da teoria da aprendizagem com uma única corrente geográfica.'], 0,
      ['A intervenção retoma a experiência e oferece meios para elaborar uma explicação mais determinada.', 'O caso apresenta aplicação e revisão, não apenas transmissão verbal de uma definição.', 'A atividade do aluno ocorre com mediação e orientação; não exige ausência docente.', 'Concepção geográfica e concepção pedagógica são planos relacionados, mas não classificações equivalentes.'], 'mediação conceitual')
final(14, 9, 'Após aprender o conceito de rede em trajetos escolares, a estudante o usa para explicar como a interrupção de um caminho altera o abastecimento de uma feira. Qual evidência apareceu?',
      ['Memorização do nome da escola como explicação de toda circulação.', 'Uso do conceito em outra situação, estabelecendo relações pertinentes.', 'Repetição da mesma experiência pessoal, sem mudança de interpretação.', 'Abandono do conteúdo científico porque o exemplo passou a ser cotidiano.'], 1,
      ['O caso mostra uma relação conceitual, e não apenas o reconhecimento de um nome.', 'A transferência indica que o conceito participa da interpretação além do exemplo inicial.', 'A estudante utiliza uma relação aprendida para compreender uma nova situação.', 'O cotidiano é interpretado com o conceito; a mudança de caso não implica abandono do conhecimento científico.'], 'formação de conceitos')
final(15, 10, 'A turma amplia um mapa e passa a copiar mais nomes. Em outra tarefa, relaciona o trajeto local à distribuição municipal de serviços. Qual análise da escala é adequada?',
      ['As duas tarefas comprovam articulação de escalas por mostrar mais lugares.', 'O tamanho da imagem determina sozinho o nível explicativo da investigação.', 'As tarefas usam o mesmo tipo de escala porque ambas possuem mapas.', 'A segunda explicita relações entre recortes; alterar a imagem não demonstra isso por si só.'], 3,
      ['Aumentar nomes ou área visível não mostra, sozinho, relações entre processos em diferentes recortes.', 'É necessário analisar o problema e as relações investigadas, além da representação gráfica.', 'Mapa e escala de análise não são termos idênticos; o suporte não define o raciocínio.', 'A segunda conecta trajeto e organização de serviços. A primeira ainda pode permanecer no inventário.'], 'escalas de análise')
final(16, 6, 'Em uma aula anunciada como crítica, a turma apenas repete a avaliação do professor sobre uma desigualdade. Qual mudança oferece melhor evidência de aprendizagem?',
      ['Trocar a fala repetida por um nome mais recente para a mesma atividade.', 'Usar uma tecnologia diferente sem mudar a exigência intelectual.', 'Solicitar uma explicação fundamentada que relacione processos e confronte as fontes.', 'Avaliar o acordo com o professor como critério suficiente de domínio conceitual.'], 2,
      ['Mudar o nome não altera necessariamente o que os alunos precisam compreender e justificar.', 'O novo suporte pode manter a mesma reprodução verbal, sem ampliar a análise.', 'A tarefa exige mobilizar conceitos e evidências para construir e discutir a interpretação.', 'Concordância não substitui demonstração das relações que sustentam uma explicação.'], 'ensino e pensamento crítico')
final(17, 11, 'Uma fotografia da feira mostra bancas e circulação. Um estudante conclui que conhece, pela imagem, a renda e as condições de trabalho de cada pessoa. Qual intervenção é mais adequada?',
      ['Explicitar o alcance do registro e selecionar outras fontes para investigar essas relações.', 'Aceitar a conclusão porque a fotografia registra uma situação real.', 'Descartar a fotografia como fonte para qualquer pergunta geográfica.', 'Transformar a aparência visível em medida suficiente de renda.'], 0,
      ['A fotografia ajuda a observar certos aspectos, enquanto a conclusão sobre renda e trabalho pede outras evidências.', 'Ser um registro real não elimina enquadramento, seleção e limites da informação.', 'O limite para uma conclusão não torna a fonte inútil para toda investigação.', 'A aparência não fornece esse tipo de medida, e utilizá-la assim produz uma inferência sem fundamento.'], 'fontes e inferências')
final(18, 11, 'Uma investigação reúne dados de fluxos, narrativas e imagens do mesmo lugar. Que condição dá coerência metodológica à combinação?',
      ['A expectativa de que todas as fontes ofereçam exatamente a mesma informação.', 'O uso de recursos variados como prova automática de profundidade.', 'A análise de cada material sem relação com a pergunta inicial.', 'A explicitação do problema, da função de cada fonte e dos critérios de interpretação.'], 3,
      ['Fontes podem contribuir de modos distintos. É necessário justificar sua relação com o problema.', 'Variedade não substitui coerência entre procedimentos, conceitos e conclusão.', 'Materiais desconectados podem formar uma coleção de informações sem explicar o objeto.', 'A combinação é justificável quando permite discutir como as contribuições se articulam e quais limites conservam.'], 'coerência metodológica')
final(19, 12, 'Um texto afirma que concepções geográficas devem orientar o ensino para além da memorização. Que desenvolvimento torna a tese mais consistente?',
      ['Uma lista de autores sem explicar as ideias mobilizadas.', 'A explicação de um conceito, uma intervenção didática analisada e uma evidência do avanço do aluno.', 'A repetição da importância da disciplina em diferentes frases.', 'A enumeração de ferramentas que poderiam ser usadas, sem relacioná-las ao objetivo.'], 1,
      ['A lista pode identificar referências, mas não demonstra como sustentam a tese.', 'O desenvolvimento conecta fundamento, ação de ensino e aprendizagem, construindo um argumento.', 'Reafirmar a tese sem explicação e aplicação não aumenta sua fundamentação.', 'Recursos precisam ser relacionados ao que se quer ensinar e ao que a turma deverá compreender.'], 'argumentação para a redação')
final(20, 2, 'Ao comparar correntes, uma candidata associa uma lista de técnicas a cada uma, sem analisar problema e explicação. O que falta em sua preparação teórico-metodológica?',
      ['Memorizar os nomes das técnicas em ordem alfabética.', 'Tratar cada autor como representante imutável de uma única frase.', 'Compreender como conceitos e procedimentos se articulam para justificar o conhecimento.', 'Substituir os casos de ensino pela classificação dos aparelhos usados em aula.'], 2,
      ['A ordenação não resolve a ausência de relação entre problema, método e explicação.', 'A simplificação histórica pode reforçar o limite da classificação sem compreensão.', 'O foco teórico-metodológico está na relação entre compreensão do objeto, investigação e justificativa da explicação.', 'Classificar aparelhos mantém a confusão entre recurso e concepção que a preparação deve superar.'], 'síntese teórico-metodológica')


def balance_new_options():
    # Só as questões novas são reorganizadas. As alternativas antigas não mudam.
    for i, question in enumerate(q for q in questions if q['id'].startswith('r2f')):
        target = [1, 3, 0, 2][i % 4]
        shift = (target-question['answer']) % 4
        pairs = list(zip(question['options'], question['feedback']))
        if shift:
            pairs = pairs[-shift:]+pairs[:-shift]
        question['options'], question['feedback'] = map(list, zip(*pairs))
        question['answer'] = target


flashcards = copy.deepcopy(ORIGINAL['flashcards'])
improved_backs = {
    'c01':'Referências conceituais para compreender e explicar o objeto. Exemplo: perguntar como relações sociais participam dos acessos diferentes.',
    'c02':'Caminho de investigação e interpretação, com perguntas, fontes e critérios. Não se resume a enumerar entrevista, mapa e fotografia.',
    'c03':'Apoio ao ensino. O mesmo mapa pode servir à identificação de nomes ou à análise da produção dos acessos; o recurso não define sozinho a concepção.',
    'c04':'Reflexão sobre como o conhecimento é produzido, justificado e limitado. Exemplo: por que uma fotografia mostra formas, mas não prova sozinha a renda das pessoas?',
    'c05':'Lógica que transforma uma condição natural em resultado social necessário. Reconhecer a chuva como fator não é, por si só, determinismo.',
    'c06':'Condições e possibilidades do meio mobilizadas por técnicas e práticas históricas. Não equivale a liberdade sem limites materiais.',
    'c07':'Conjunto heterogêneo de tradições com observação, descrição, classificação e diferenciação de áreas. Não deve ser reduzido a uma única prática escolar de memorização.',
    'c08':'Busca explicar padrões espaciais com modelos, hipóteses e procedimentos quantitativos. O modelo é confrontado com dados e possui pressupostos.',
    'c09':'Investigam a produção social do espaço, relações de poder e contradições. Uma denúncia precisa ser desenvolvida em explicação com conceitos e evidências.',
    'c10':'Investiga como pessoas vivem, percebem e significam lugares. Narrativas precisam de contexto e não representam todos os sujeitos automaticamente.',
    'c11':'Estudam práticas, símbolos, identidades e representações espaciais. Perguntam, por exemplo, quem representa um lugar e o que é selecionado ou omitido.',
    'c12':'Em Milton Santos, sistemas de objetos e de ações são indissociáveis. Uma estrada deve ser compreendida por sua materialidade, usos, práticas e conexões.',
    'c13':'Intervenção intencional que relaciona experiência e conceitos. O professor orienta a construção de uma explicação, sem exigir que o aluno descubra tudo sozinho.',
    'c14':'Organiza conhecimentos para finalidades educativas, em diálogo com ciência, currículos, experiências e condições de ensino. Não é só conteúdo acadêmico encurtado.',
    'c15':'Localizar, comparar, examinar distribuições, conectar e articular escalas para responder a um problema. A operação precisa de uma finalidade explicativa.',
    'c16':'Recorte e nível de análise das relações de um processo. Relacionar trajeto local e rede municipal é mais que ampliar a imagem do mapa.',
    'c17':'Relação de proporção entre distâncias no mapa e no terreno. Não é sinônimo da escala geográfica dos processos investigados.',
    'c18':'O aluno usa conceitos e evidências para explicar relações e justificar uma interpretação, inclusive em uma situação diferente da estudada.'
}
for card in flashcards:
    card['back'] = improved_backs[card['id']]
flashcards += [dict(id=f'c{i}', front=front, back=back) for i, (front, back) in enumerate([
    ('Hipótese e modelo: como se relacionam?', 'A hipótese é uma resposta provisória. O modelo seleciona relações para investigá-la; os dados ajudam a sustentar, limitar ou rever a explicação.'),
    ('Duas médias iguais demonstram o mesmo acesso?', 'Não. Valores próximos da média e valores muito desiguais podem produzir o mesmo resumo. É necessário examinar a distribuição e as condições.'),
    ('O que o histórico e o dialético ajudam a perguntar?', 'Como uma situação foi produzida no tempo e quais relações e contradições a constituem. Uma via pode favorecer certos fluxos e manter restrições a outros usos.'),
    ('Qual pergunta se aproxima da fenomenologia do lugar?', 'Como aquele espaço é vivido e ganha sentido na experiência dos sujeitos. A localização comum não torna idênticos os vínculos.'),
    ('Humanística e cultural: como distinguir o foco?', 'Investigar o sentido vivido da feira enfatiza a experiência. Analisar como uma campanha mostra a feira enfatiza a seleção e a produção de representações.'),
    ('Como fortalecer uma resposta de prova?', 'Identifique o problema, explique o conceito, analise uma situação e justifique relações. Não classifique a concepção só por um recurso ou uma palavra.')
], 19)]

REF_PAGE = 'https://github.com/emanoelb5-lgtm/ProfGeo/blob/main/docs/UNIDADE_1_1_REFEITA.md'
references = [
    dict(title='Edital PROFGEO-UFPA n. 03/2026 — Anexo III, item 1.1', author='UFPA / PROFGEO', year=2026,
         url='https://www.profgeo.propesp.ufpa.br/', note='Fonte do programa. O item define o tema, não uma bibliografia obrigatória. Este percurso, os exemplos e as questões são autorais.'),
    dict(title='Geografia: pequena história crítica', author='Antonio Carlos Robert Moraes', year=1981,
         note='Leitura complementar de referência para a história do pensamento geográfico. As classificações de correntes não resumem integralmente os autores e suas obras.'),
    dict(title='Explanation in Geography', author='David Harvey', year=1969,
         url=REF_PAGE+'#modelos-e-explicacao', note='Edward Arnold. Referência primária de discussão metodológica associada ao período da Nova Geografia. A ficha reúne o endereço bibliográfico da obra; os casos de teste de hipótese da unidade são exercícios próprios.'),
    dict(title='A natureza do espaço: técnica e tempo, razão e emoção', author='Milton Santos', year=1996,
         url=REF_PAGE+'#objetos-e-acoes', note='Referência primária para a relação entre sistemas de objetos e de ações. A ficha liga ao catálogo da Edusp. Os exemplos de escola, estrada e feira são aplicações didáticas próprias.'),
    dict(title='Espaço, tempo, lugar: um arcabouço humanista', author='Yi-Fu Tuan', year=2011,
         url=REF_PAGE+'#experiencia-e-lugar', note='Artigo em tradução publicado na Geograficidade. Fonte primária para a perspectiva da experiência e do lugar; a ficha oferece acesso ao periódico.'),
    dict(title='Lugar: uma perspectiva experiencial', author='Yi-Fu Tuan', year=2018,
         url=REF_PAGE+'#experiencia-e-lugar', note='Tradução publicada na Geograficidade de texto original de 1973. Leitura primária complementar sobre a diversidade de experiências de lugar.'),
    dict(title='A geografia pós-estrutural e a abordagem cultural', author='Paul Claval',
         url=REF_PAGE+'#cultura-e-representacao', note='Texto autoral na GEOUSP. Referência primária complementar para o debate cultural e sua diversidade. A ficha contém o link do artigo.'),
    dict(title='Cotidiano, mediação pedagógica e formação de conceitos: uma contribuição de Vygotsky ao ensino de geografia', author='Lana de Souza Cavalcanti', year=2005,
         url='https://www.scielo.br/j/ccedes/a/WnXnVgTRQHZttxBQR44gt9x/?lang=pt', note='Cadernos Cedes. Fonte primária complementar para cotidiano, mediação e formação conceitual. As situações de ensino e as resoluções foram redigidas para esta unidade.'),
    dict(title='Geografia, pesquisa e ensino', author='Editus / Universidade Estadual de Santa Cruz',
         url='https://uesc.br/editora/livrosdigitais2017/geografia_pesquisa_ensino.pdf', note='Livro digital complementar com debate de história, pesquisa e ensino de Geografia.'),
    dict(title='Percurso didático, referências e atualização da unidade 1.1', author='ProfGeo', year=2026,
         url=REF_PAGE, note='Apresenta o encadeamento das lições e as fontes selecionadas. Fotografias e animações mantêm os créditos originais. Não constitui bibliografia oficial da seleção.')
]

essay = copy.deepcopy(ORIGINAL['essay'])
essay['note'] = 'Tema autoral de treino em até 20 linhas digitadas. Use as resoluções da lição 12 para planejar e revisar. A autoavaliação é formativa; não é a grade oficial nem uma correção automática do conteúdo.'
# Os cinco primeiros critérios preservam a ordem para manter autoavaliações salvas.
essay['rubric'] += [
    'Expliquei por que a intervenção proposta ajuda a aprender, em vez de apenas nomear um recurso.',
    'Indiquei uma evidência de que o aluno passou a usar conceitos para explicar relações.'
]
essay['model'] = (
    'O ensino de Geografia deve ajudar o aluno a explicar relações espaciais. Nomes e localizações contribuem para esse trabalho, mas sua memorização não demonstra, sozinha, compreensão da organização do espaço.\n'
    'Uma perspectiva crítica permite investigar como decisões e relações sociais participam da produção dos acessos. A dificuldade de chegar à escola, por exemplo, não se explica apenas pela chuva, mas também pelas condições de circulação e pela infraestrutura historicamente constituída.\n'
    'Em uma situação de ensino, a turma pode apresentar seus trajetos, comparar mapas e consultar informações sobre as vias. O professor orienta as perguntas e mobiliza os conceitos de rede, acesso e circulação, ajudando os estudantes a rever explicações iniciais.\n'
    'A avaliação deve verificar se o aluno consegue justificar diferenças com essas relações e com as fontes. Apresentar outra situação de circulação permite examinar se o conceito foi usado além do exemplo inicial.\n'
    'Assim, concepção, método e mediação articulam-se em decisões de ensino voltadas à aprendizagem. O avanço está na capacidade de interpretar e argumentar, e não apenas em repetir termos ou utilizar uma ferramenta atraente.'
)


def save():
    balance_new_options()
    assert len(lessons) == 12 and len(questions) == 76 and len(flashcards) == 24
    assert len([q for q in questions if q['pool']=='final']) == 20
    by_id = {q['id']:q for q in questions}
    for old in ORIGINAL['questions']:
        for field in ['stem','options','answer','feedback','tag','type']:
            assert by_id[old['id']][field] == old[field], (old['id'], field)
    unit = copy.deepcopy(ORIGINAL)
    unit.update(revision=2, shortTitle='Aprender a pensar e ensinar Geografia',
                subtitle='Um percurso explicado: problema, concepção, exemplo resolvido, ensino e treino para a prova.',
                estimatedMinutes=sum(l['minutes'] for l in lessons),
                objectives=[
                    'Distinguir informação, explicação, teoria, método, metodologia de ensino e recurso.',
                    'Compreender o raciocínio de concepções geográficas, com seus alcances e limites.',
                    'Comparar concepções por problemas, fontes e explicações, sem rótulos automáticos.',
                    'Analisar a mediação e as evidências de aprendizagem em uma aula de Geografia.',
                    'Resolver casos e construir um argumento com conceito, intervenção e exemplo analisado.'
                ], lessons=lessons, questions=questions, flashcards=flashcards,
                references=references, essay=essay)
    (ROOT/'content/units/1.1.json').write_text(json.dumps(unit,ensure_ascii=False,indent=2)+'\n')
    path = ROOT/'content/catalog.json'
    catalog = json.loads(path.read_text())
    entry = next(e for m in catalog['modules'] for e in m['units'] if e['id']=='1.1')
    assert entry['revision'] <= 2, 'Não sobrescreva uma revisão posterior.'
    entry.update(revision=2)
    catalog['revision'] = max(3,catalog['revision'])
    catalog['updatedAt'] = '2026-10-26'
    path.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
    print(f'Unidade 1.1 r2: {len(lessons)} lições, {len(questions)} questões, {len(flashcards)} cartões, {unit["estimatedMinutes"]} minutos sugeridos.')


if __name__ == '__main__':
    save()
