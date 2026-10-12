"""Conteúdo autoral da unidade 1.2; usa somente recursos do APK 1.1.1."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = 'Saberes disciplinares, curriculares, saberes da experiência e da ação pedagógica dos docentes'
REFERENCE_PAGE = 'https://github.com/emanoelb5-lgtm/ProfGeo/blob/main/docs/UNIDADE_1_2.md'


def text(title, body):
    return dict(type='text', title=title, body=body)


def callout(title, body, warning=False):
    return dict(type='callout', title=title, body=body, tone='warning' if warning else 'info')


def listing(title, *items):
    return dict(type='list', title=title, items=list(items))


def table(title, headers, rows):
    return dict(type='table', title=title, headers=headers, rows=rows)


def compare(title, left, lb, right, rb):
    return dict(type='compare', title=title, left=dict(title=left, body=lb), right=dict(title=right, body=rb))


def picture(name, title, caption, credit='ProfGeo · ilustração didática autoral em 16:9'):
    return dict(type='photo', src='media/'+name, title=title, caption=caption, credit=credit)


def animation(kind, title, caption):
    return dict(type='animation', kind=kind, title=title, caption=caption)


def match(title, pairs):
    return dict(type='match', title=title, pairs=pairs)


def order(title, items):
    return dict(type='order', title=title, items=items)


lessons = []


def lesson(n, title, kicker, minutes, blocks, summary, practice=None):
    l = dict(id=f'l{n:02d}', title=title, kicker=kicker, minutes=minutes, blocks=blocks, summary=summary)
    if practice:
        l['practice'] = practice
    lessons.append(l)


lesson(1, 'Ensinar exige mais de um saber', 'Reconhecer as decisões do professor', 10, [
    text('Uma aula começa antes de entrar na sala', 'Imagine uma professora preparando uma aula sobre o caminho até a escola. Ela precisa compreender circulação e acesso, consultar o que a turma deve aprender, considerar dificuldades que observou e escolher como acompanhar a aprendizagem. Conhecer o assunto participa desse trabalho, mas não resolve todas essas decisões.\nNesta unidade, saber significa conhecimento mobilizado para compreender uma situação e agir profissionalmente. Os quatro focos do item 1.2 ajudam a analisar a docência. Em uma aula real, eles se articulam; separá-los aqui é uma ferramenta de estudo.'),
    picture('u12-quatro-saberes.png', 'Quatro perguntas para ler uma prática docente', 'O esquema organiza os quatro focos do edital. Uma mesma decisão pode envolver mais de um deles; procure o aspecto destacado em cada situação.'),
    table('Reconheça o foco da decisão', ['Saber', 'Pergunta que ajuda a reconhecer'], [
        ['Disciplinar', 'Que conceitos, explicações e formas de investigar sustentam o assunto?'],
        ['Curricular', 'Por que, para quem e em que progressão ensinar esse conteúdo?'],
        ['Da experiência', 'Que aprendizagens o professor construiu no exercício da profissão?'],
        ['Da ação pedagógica', 'Como uma prática se torna pública e é investigada, na acepção de Gauthier?']]),
    picture('u12-sala-aula.jpg', 'Uma sala reúne escolhas de ensino', 'Sala da Escola Técnica de Paulínia, em São Paulo, fotografada em 2015. A lousa apresenta uma aula de História. A foto ajuda a observar recursos e organização do espaço; não comprova o método usado nem a aprendizagem da turma.', 'Alebasi24 · Wikimedia Commons · CC BY-SA 4.0 · imagem redimensionada'),
    callout('Como usar as categorias', 'Quando uma questão pede o saber predominante, observe a ação enfatizada. Consultar a progressão do currículo destaca um foco diferente de interpretar a escala de um mapa. Isso não significa que os outros saberes estejam ausentes.'),
    text('Desafio mental', 'A professora troca um mapa porque percebeu uma dificuldade recorrente da turma. Pense: o destaque está na aprendizagem profissional construída ao observar os alunos. Ao analisar o mapa e definir o objetivo da nova atividade, ela também mobiliza saberes disciplinares e curriculares.')
], 'Os saberes docentes se articulam. Para classificá-los, identifique a decisão e o aspecto enfatizado, sem reduzir uma aula a uma única fonte de conhecimento.', match('Associe o destaque ao saber', [
    ['Explicar relações entre circulação e acesso', 'Disciplinar'],
    ['Situar o conteúdo nos objetivos e na progressão da turma', 'Curricular'],
    ['Rever uma rotina após observar dificuldades recorrentes', 'Da experiência'],
    ['Investigar uma prática explicitada para exame de outros professores', 'Da ação pedagógica']]))

lesson(2, 'Saber disciplinar: compreender a Geografia', 'Conceitos, relações e fontes', 12, [
    text('Dominar a matéria tem conteúdo', 'O saber disciplinar envolve conhecimentos produzidos no campo da Geografia: conceitos, explicações, modos de formular perguntas e de examinar fontes. Saber onde um rio fica é útil, mas uma aula pode exigir também compreender como ele se relaciona com circulação, ocupação e atividades econômicas.\nO professor precisa reconhecer o que uma evidência permite afirmar. Um mapa de localização mostra onde estão certos elementos; não demonstra sozinho as causas de uma desigualdade. Uma fotografia registra um recorte visível, não tudo o que acontece naquele lugar.'),
    picture('u12-rio-guama.jpg', 'Do olhar sobre o rio à pergunta geográfica', 'Rio Guamá visto do campus da UFPA, em Belém, em setembro de 2019. A foto pode iniciar perguntas sobre paisagem, circulação e uso das margens. Explicações sobre trabalho, renda ou transporte exigem outras fontes.', 'Fronteira · Wikimedia Commons · CC BY-SA 4.0 · imagem redimensionada'),
    compare('Duas respostas ao mesmo tema', 'Nomear', '“O rio está em Belém.” A localização é um ponto de apoio.', 'Relacionar', '“Como as travessias e os acessos às margens participam da circulação?” A pergunta orienta a investigação de relações espaciais.'),
    table('Cuidado com a fonte', ['Fonte', 'Pergunta de verificação'], [
        ['Fotografia', 'Qual lugar, data, enquadramento e limite do registro?'],
        ['Mapa', 'Qual tema, legenda, escala e informação representada?'],
        ['Relato', 'De quem é a experiência e com quais outras fontes posso dialogar?'],
        ['Tabela', 'Quais unidades, recorte e critérios de produção dos dados?']]),
    callout('Exemplo de revisão conceitual', 'No mapa, uma escala 1:10.000 é maior que 1:100.000, pois representa o terreno com menor redução. Se o professor domina essa relação, pode explicar o conceito e reconhecer uma interpretação equivocada. Como ensiná-lo à turma envolve ainda decisões pedagógicas.'),
    text('Escolha profissional', 'Antes de usar uma imagem para explicar uma enchente, a professora confere o que sabe sobre chuva, ocupação e infraestrutura. Se a fotografia não traz informações sobre os fatores envolvidos, ela formula hipóteses e busca evidências adicionais. Esse cuidado mostra domínio da matéria e de seus critérios de análise.')
], 'Saber disciplinar é compreender e investigar o conteúdo, relacionando conceitos e fontes. Acumular nomes ou confiar em uma única imagem não basta.')

lesson(3, 'Saber curricular: escolher o que ensinar', 'Objetivos, seleção e progressão', 13, [
    text('Entre o campo científico e a aprendizagem escolar', 'A Geografia produz muitos conhecimentos. Uma turma não estuda tudo ao mesmo tempo. O saber curricular participa da leitura de objetivos, conteúdos e formas de organização do ensino: o que selecionar, em que momento e com que relações.\nNesta unidade, a BNCC aparece como referência para discutir aprendizagens essenciais e sua relação com os currículos. Ela não é um roteiro completo de aula. Redes e escolas organizam propostas curriculares, e o professor precisa interpretá-las em seu contexto. O estudo detalhado dos documentos fica para a unidade 1.4.'),
    picture('u12-caminho-curricular.png', 'Da orientação curricular à evidência de aprendizagem', 'Sequência didática autoral: compreender a orientação, explicitar um objetivo, organizar uma situação e examinar o que o aluno consegue fazer. Ela ilustra decisões profissionais; não é uma ordem obrigatória de um documento.'),
    compare('Tema e objetivo não são a mesma coisa', 'Tema', '“Transporte e circulação.” Diz sobre o que a aula trata.', 'Objetivo', '“Comparar dois trajetos e explicar por que menor distância não garante menor tempo.” Diz o que o estudante deverá aprender a fazer.'),
    text('Progressão com sentido', 'Em um percurso hipotético, a turma pode primeiro identificar trajetos e ler suas legendas; depois comparar distância e tempo; por fim explicar diferenças de acesso relacionando meios de transporte e condições da via. A progressão deve considerar conhecimentos prévios e objetivos da turma. Não basta trocar o nome do conteúdo no plano.'),
    table('Alinhe três decisões', ['Decisão', 'Exemplo autoral'], [
        ['Objetivo', 'Explicar diferenças de tempo entre dois trajetos.'],
        ['Atividade', 'Ler uma tabela e comparar os trajetos com apoio de um mapa.'],
        ['Avaliação', 'Justificar a escolha de uma rota com dados e condições do percurso.']]),
    callout('Leitura do currículo', 'Consultar uma orientação e justificadamente selecionar um conteúdo é diferente de copiar um código de habilidade no plano. Também é diferente de escolher uma atividade só porque ocupa o tempo da turma.', True)
], 'O saber curricular orienta seleção, objetivos e progressão. O professor interpreta as orientações e articula atividade e avaliação à aprendizagem pretendida.', match('Qual é a função de cada decisão?', [
    ['Transporte e circulação', 'Tema de estudo'],
    ['Explicar diferenças de tempo entre trajetos', 'Objetivo de aprendizagem'],
    ['Comparar mapa e tabela em duplas', 'Situação de aprendizagem'],
    ['Justificar a conclusão com dados do percurso', 'Evidência de aprendizagem']]))

lesson(4, 'Saber da experiência: aprender no trabalho', 'Observação, trajetória e revisão', 11, [
    text('Experiência é aprendizagem profissional', 'Ao acompanhar turmas, o professor aprende a reconhecer dúvidas, administrar situações e rever escolhas. O saber da experiência se constrói no exercício da profissão e nas relações de trabalho. Ter muitos anos de serviço não garante, por si só, que uma interpretação seja adequada.\nUma professora nota que a turma lê as cores de um mapa, mas ignora a legenda. Ela passa a pedir uma justificativa para cada interpretação e acompanha as respostas. O destaque é o aprendizado que ela constrói ao observar a prática e ajustar sua intervenção.'),
    picture('u12-experiencia-reflexao.png', 'Da dificuldade observada à decisão revista', 'Caso fictício sobre leitura de mapas. Os passos representam uma possibilidade de reflexão profissional, com observação das respostas antes de manter ou modificar a estratégia.'),
    compare('Duas formas de lembrar uma aula', 'Impressão isolada', '“Gostaram muito; então todos aprenderam.” A reação é relevante, mas não demonstra o domínio do conceito.', 'Observação orientada', '“Gostaram da atividade; ao justificar, parte da turma ainda confundiu cor e valor. Vou trabalhar a legenda e verificar de novo.”'),
    listing('O que registrar em um diário de aula', 'Qual dificuldade apareceu, com um exemplo de resposta.', 'Que intervenção foi feita e em quais condições.', 'O que mudou nas explicações dos estudantes.', 'Qual dúvida permanece e o que será revisto.'),
    callout('Duas experiências diferentes', 'Os estudantes também possuem conhecimentos construídos no cotidiano. O saber experiencial docente discutido aqui é a aprendizagem profissional do professor. As duas experiências podem dialogar, mas não devem ser tratadas como termos equivalentes.'),
    text('Experiência em conversa com outras fontes', 'Se uma rotina deixa de ajudar uma nova turma, o professor pode rever sua hipótese, conversar com colegas e buscar referências. Aprender no trabalho não dispensa formação e conhecimento disciplinar. Permite interrogar como esses conhecimentos participam de situações concretas.')
], 'O saber da experiência se desenvolve na prática profissional e pode ser revisto. Tempo de serviço e entusiasmo da turma não substituem análise da aprendizagem.')

lesson(5, 'Saber da ação pedagógica em Gauthier', 'Tornar público e investigar', 14, [
    text('Um sentido que merece atenção', 'Na discussão de Gauthier e colaboradores, o saber da ação pedagógica se refere ao saber experiencial tornado público e testado por pesquisas sobre o ensino. Ele não é simplesmente qualquer ação do professor. A experiência deixa de ficar restrita a uma certeza individual e passa a poder ser examinada por outros.\nContar que uma dinâmica “funcionou” pode iniciar uma troca profissional. Para sustentar conhecimento sobre a prática, é preciso explicitar o que foi feito, com quem, em quais condições, que aprendizagem se procurou e quais evidências foram analisadas.'),
    picture('u12-acao-pedagogica.png', 'Da experiência privada ao exame público da prática', 'Esquema de estudo inspirado na distinção de Gauthier. Divulgar é um passo; a investigação das evidências e das condições faz parte do sentido específico de saber da ação pedagógica.'),
    compare('A postagem e a investigação', 'Relato de sucesso', '“Usei um jogo de mapas e a turma participou.” O relato informa a experiência, mas ainda não esclarece a aprendizagem conceitual.', 'Prática examinável', '“Definimos o objetivo, registramos as intervenções e comparamos justificativas de leitura da legenda. Outros professores analisaram o procedimento, os resultados e seus limites.”'),
    table('Perguntas para tornar uma prática examinável', ['Aspecto', 'Pergunta'], [
        ['Objetivo', 'O que os alunos deveriam aprender?'],
        ['Procedimento', 'O que professor e estudantes fizeram?'],
        ['Evidências', 'Quais respostas permitem acompanhar a aprendizagem?'],
        ['Condições e limites', 'O que pode ter influenciado os resultados?']]),
    callout('Não transforme resultado em receita', 'Uma investigação pode ajudar outros docentes, mas seus resultados precisam ser interpretados. Turmas, conteúdos, recursos e condições variam. Uma melhora observada não prova automaticamente que uma única estratégia foi sua causa.', True),
    text('Aplicação autoral', 'Um grupo compara formas de ensinar orientação cartográfica. Ele registra tarefas, critérios e produções, discute os erros e comunica o estudo. A intenção é produzir conhecimento profissional sobre a prática, e não apenas escolher a atividade que teve mais aplausos.')
], 'Em Gauthier, ação pedagógica tem sentido específico: experiência tornada pública e investigada. A divulgação sozinha e uma receita universal não satisfazem esse sentido.', order('Organize um percurso de investigação da prática', [
    'Delimitar uma dificuldade e o objetivo de aprendizagem.',
    'Explicitar a intervenção e as condições de realização.',
    'Reunir e analisar evidências com critérios claros.',
    'Comunicar procedimentos, resultados e limites para exame público.' ]))

lesson(6, 'Autores: aproximações sem confusão', 'Tardif, Gauthier e Shulman', 11, [
    text('O título do edital não é uma lista atribuída a um autor', 'O item 1.2 reúne focos para estudar os saberes docentes. Não informa que todos pertencem a uma única classificação teórica. Quando o enunciado nomeia um autor, é preciso respeitar o sentido dos seus termos.\nTardif destaca a pluralidade, a temporalidade e o caráter situado dos saberes profissionais. Gauthier e colaboradores discutem um repertório de saberes e o problema de sua validação. Shulman contribui com a discussão do conhecimento pedagógico do conteúdo: compreender modos de tornar uma matéria ensinável, considerando representações e dificuldades de aprendizagem.'),
    table('Três entradas para analisar a docência', ['Referência', 'Foco de estudo nesta unidade'], [
        ['Tardif', 'Diversas fontes e aprendizagens mobilizadas ao longo da trajetória profissional.'],
        ['Gauthier e colaboradores', 'Experiência tornada pública e testada; conhecimento profissional examinável.'],
        ['Shulman', 'Representações, explicações e dificuldades próprias do ensino de um conteúdo.']]),
    text('Uma prática, perguntas diferentes', 'Uma professora muda a forma de ensinar escala. Pela entrada da trajetória, podemos perguntar de onde veio o aprendizado que orienta a decisão. Pela entrada da investigação, perguntamos como a prática e seus resultados foram explicitados e examinados. Pela entrada do conteúdo ensinável, analisamos a representação escolhida para enfrentar uma dificuldade conceitual. Essas perguntas se aproximam, mas não são definições intercambiáveis.'),
    callout('Cuidado de prova', 'Conhecimento pedagógico do conteúdo, em Shulman, não é sinônimo automático de saber da ação pedagógica, em Gauthier. Os termos pertencem a discussões diferentes. Leia a definição e o foco do enunciado antes de decidir.'),
    listing('Como estudar as referências', 'Associe cada autor a uma questão de estudo, sem reduzir sua obra a uma palavra.', 'Construa um exemplo e explique a relação com o conceito.', 'Nas referências, diferencie o edital das leituras complementares selecionadas pelo app.')
], 'Compare os autores pelo problema que discutem. Pluralidade dos saberes, validação da prática e ensino de um conteúdo são focos relacionados, mas não idênticos.', match('Associe o foco à referência', [
    ['Saberes temporais, plurais e situados', 'Tardif'],
    ['Experiência pública e testada por pesquisas sobre o ensino', 'Gauthier e colaboradores'],
    ['Representações e dificuldades no ensino de uma matéria', 'Shulman']]))

lesson(7, 'Do conceito à explicação que ensina', 'Conhecimento pedagógico do conteúdo', 13, [
    text('Adaptar com precisão', 'Uma explicação pode ser correta para o professor e continuar difícil para o aluno. Ensinar requer reconhecer como a turma pensa, escolher representações e verificar o que ela compreendeu. O conhecimento pedagógico do conteúdo ajuda a discutir essa relação entre a matéria e as maneiras de ensiná-la.\nUm professor sabe que distância e tempo de viagem são medidas diferentes. Para enfrentar a ideia de que “o caminho menor é sempre mais rápido”, ele prepara um exemplo com rotas, solicita uma previsão e pede justificativas depois da comparação. A representação foi escolhida para uma dificuldade conceitual específica.'),
    animation('quantitative', 'Antes de escolher a rota, explique seu critério', 'Compare as duas rotas hipotéticas. A: 8 km e 45 minutos; B: 15 km e 25 minutos. Observe como o professor pode usar a diferença entre distância e tempo para construir uma pergunta, e não só mostrar uma cena.'),
    table('Uma intervenção com intenção', ['Momento', 'Decisão do professor'], [
        ['Ideia inicial', 'Perguntar qual rota parece mais rápida e por quê.'],
        ['Representação', 'Oferecer distância e tempo das duas rotas.'],
        ['Mediação', 'Pedir que o aluno revise ou sustente sua previsão com os dados.'],
        ['Nova situação', 'Apresentar outro trajeto para verificar se a distinção foi compreendida.']]),
    compare('Recurso e conhecimento profissional', 'Recurso', 'Um mapa, uma animação ou uma tabela pode apoiar a atividade.', 'Conhecimento para ensinar', 'Saber por que usar a representação, qual dificuldade ela enfrenta e como verificar a compreensão.'),
    callout('Clareza sem distorção', 'Exemplos e analogias precisam conservar o sentido do conceito. Dizer que “escala maior é o maior denominador” facilita uma frase, mas ensina uma relação errada. Ao simplificar a linguagem, confira a precisão.'),
    text('Sua verificação', 'No exemplo, a rota B tem menor tempo, embora tenha maior distância. Isso vale para os dados da cena, não para todas as estradas e rios. Uma resposta bem construída indica o critério, compara os valores e reconhece o limite do caso.')
], 'Ensinar um conteúdo exige selecionar representações e intervenções adequadas às dificuldades da turma, conservando a precisão conceitual.')

lesson(8, 'Planejar articulando os saberes', 'Da pergunta à avaliação', 12, [
    text('Caso fictício: chegar à escola na chuva', 'Uma professora propõe investigar por que certos trajetos até a escola ficam mais demorados no período de chuva. Seu objetivo é que os alunos expliquem diferenças de acesso relacionando circulação, infraestrutura e condições do percurso. Não se trata de diagnosticar uma comunidade real.\nO planejamento articula conhecimentos geográficos, objetivos curriculares, aprendizagens da experiência e referências de práticas investigadas. As decisões precisam se ajustar às condições da turma, sem perder a aprendizagem pretendida.'),
    animation('mediation', 'Acompanhe as decisões da mediação', 'Explore relato, pergunta, conceito e explicação. Depois identifique: que conceito a professora mobilizou? Que objetivo orientou a sequência? Que dificuldade ela poderia observar? Que evidência permitiria avaliar a aprendizagem?'),
    table('Leia os saberes na proposta', ['Decisão em destaque', 'Saber mobilizado'], [
        ['Relacionar circulação, acesso e infraestrutura', 'Disciplinar.'],
        ['Definir a explicação esperada e a progressão', 'Curricular.'],
        ['Antecipar dificuldades observadas em turmas anteriores', 'Da experiência.'],
        ['Analisar uma estratégia investigada, com seus limites', 'Da ação pedagógica, no sentido discutido.']]),
    text('Planejamento e condições reais', 'Se não há internet, o professor pode preparar um mapa impresso ou um croqui discutido com a turma. A ausência de um recurso não torna o conteúdo irrelevante. Ao mudar o suporte, ele confere se os estudantes ainda poderão comparar trajetos e justificar as conclusões. Na turma, as respostas orientam ajustes que o plano não podia prever em detalhe.'),
    callout('Uma atividade não vale pelo nome', '“Debate”, “mapa” e “jogo” não informam, sozinhos, a aprendizagem. Explique o que os estudantes farão com os conceitos e como o professor vai acompanhar esse trabalho.')
], 'Um planejamento articula conceito, objetivo, situação de aprendizagem e avaliação. Os saberes docentes ajudam a justificar as decisões e os ajustes.', order('Organize este planejamento possível', [
    'Ler o objetivo curricular e levantar conhecimentos e dificuldades da turma.',
    'Formular um problema e selecionar conceitos e fontes.',
    'Organizar a atividade e as intervenções para comparar explicações.',
    'Examinar as produções com critérios e decidir o replanejamento.' ]))

lesson(9, 'Dialogar com os saberes dos estudantes', 'Cotidiano e conhecimento geográfico', 12, [
    text('O cotidiano oferece perguntas', 'Em uma turma do campo, os estudantes podem conhecer tempos de viagem, usos de estradas, épocas de comercialização e trajetos por rios. Esses conhecimentos são referências para o diálogo, não um retrato único de todas as pessoas que vivem no campo.\nA professora reúne relatos e pede que a turma compare trajetos em um croqui. Em seguida, mobiliza circulação, rede e escala para investigar relações que ultrapassam uma experiência individual. Na discussão de Cavalcanti, o diálogo entre conhecimentos cotidianos e científicos participa da formação de conceitos geográficos.'),
    animation('lived', 'Um lugar pode ser vivido de maneiras diferentes', 'Ouça os três relatos fictícios da praça. Eles ilustram conhecimentos e sentidos dos personagens. O saber da experiência docente é outro foco: o que o professor aprende ao observar, mediar e avaliar situações de ensino.'),
    compare('Duas escolhas de mediação', 'Ficar só no relato', 'A turma conta trajetos, mas não os compara nem constrói explicações. A escuta ocorreu; a ampliação conceitual ainda precisa ser trabalhada.', 'Ampliar a leitura do vivido', 'A turma compara trajetos, questiona diferenças e relaciona suas experiências a redes, infraestrutura e outras escalas.'),
    text('Valorizar sem generalizar', 'Uma aluna que trabalha na agricultura não conhece necessariamente todos os cultivos, nem todos os alunos fazem a mesma atividade. O professor pergunta e acompanha as respostas. Os relatos também precisam ser confrontados com outras fontes quando a questão exigir uma explicação mais ampla.'),
    callout('Uma aprendizagem em duas direções', 'Os alunos podem ampliar suas interpretações com conceitos geográficos. O professor pode aprender, pela observação da turma, quais perguntas e representações precisam ser revistas. Isso não transforma o relato do aluno em saber experiencial docente por simples mudança de nome.'),
    listing('Perguntas para a turma', 'Quais trajetos aparecem e quais ainda não foram considerados?', 'O que varia entre as experiências?', 'Que conceito ajuda a explicar a diferença?', 'Que outra fonte precisamos consultar?')
], 'Saberes dos estudantes e saberes docentes podem dialogar. A mediação valoriza as experiências e oferece conceitos para ampliar a compreensão.')

lesson(10, 'Avaliar para aprender a ensinar melhor', 'Critérios, evidências e feedback', 12, [
    text('Avaliação também orienta decisões', 'A avaliação pode oferecer informação sobre a aprendizagem e sobre a intervenção do professor. Para isso, precisa estar relacionada ao objetivo. Se o objetivo é explicar diferenças de acesso, pedir apenas nomes de lugares verifica uma parte diferente do conhecimento.\nEm uma tarefa fictícia, os alunos comparam duas rotas e justificam qual tem menor tempo. O professor lê as respostas considerando três critérios: distinguir tempo e distância, usar os dados do caso e justificar sem transformar o exemplo em regra universal.'),
    picture('u12-evidencias.png', 'Leia o que as respostas permitem observar', 'Respostas fictícias para uma tarefa sobre rotas. Os comentários indicam aspectos a trabalhar; não são notas oficiais nem uma classificação definitiva de alunos.'),
    table('Resposta e próxima intervenção', ['Resposta fictícia', 'Feedback que orienta a aprendizagem'], [
        ['“A menor distância é mais rápida.”', 'Compare os tempos e reveja a relação entre as duas medidas.'],
        ['“B, porque 25 minutos é menos que 45.”', 'Você comparou o tempo; explique também o que ocorre com a distância.'],
        ['“B tem menor tempo, apesar de maior distância.”', 'A distinção apareceu; agora justifique os limites da conclusão.']]),
    text('Replanejar com evidências', 'Se muitas justificativas ainda confundem tempo e distância, a professora pode usar outro exemplo, retomar as unidades ou pedir uma comparação orientada. Essas decisões alimentam sua aprendizagem profissional. Uma mudança de desempenho oferece uma pista; para explicar suas causas, é necessário examinar também condições e outras intervenções.'),
    callout('Evidência não é o mesmo que impressão', 'Participação, satisfação e conclusão da atividade são informações úteis, mas não substituem a demonstração da aprendizagem conceitual. Uma turma pode estar animada e ainda precisar de mediação.', True)
], 'A avaliação oferece evidências quando tarefa e critérios correspondem ao objetivo. O feedback explica a dificuldade e indica um próximo passo.')

lesson(11, 'Construir conhecimento com outros docentes', 'Registro e investigação coletiva', 13, [
    text('Um problema de ensino pode ser investigado', 'Uma equipe percebe que estudantes decoram tipos de mapas, mas têm dificuldade para usá-los em uma explicação. O grupo delimita a pergunta: “Que mudanças aparecem nas justificativas quando pedimos comparar legenda, fonte e informação representada?” O caso é autoral e hipotético.\nOs professores explicam a sequência aplicada, registram produções em momentos diferentes e constroem critérios de análise. Também observam dificuldades e resultados que não confirmam suas expectativas. Tornar a prática examinável exige esse esforço de descrição e interpretação.'),
    picture('u12-investigar-pratica.png', 'Uma pergunta de ensino vira objeto de estudo', 'O esquema mostra decisões de uma investigação formativa: problema, intervenção, evidências e comunicação dos limites. Ele não representa uma prova automática de eficácia.'),
    table('Um registro que permite discussão', ['Parte do registro', 'Exemplo de informação'], [
        ['Problema', 'Dificuldade para justificar a leitura de um mapa.'],
        ['Condições', 'Turma, conhecimentos prévios, recursos e tempo da sequência.'],
        ['Intervenção', 'Comparação orientada de legenda, fonte e informação.'],
        ['Evidências', 'Justificativas dos alunos e critérios usados na análise.'],
        ['Limites', 'Outras intervenções, diferenças entre turmas e dúvidas restantes.']]),
    text('Compartilhar com responsabilidade', 'Um relatório pode apresentar exemplos de respostas sem expor os estudantes. O foco é a análise pedagógica, não a identificação pública de quem errou. Ao usar relatos e produções para pesquisa, a equipe deve observar os procedimentos éticos aplicáveis ao seu estudo e à instituição. Aqui treinamos a leitura da prática, sem solicitar dados reais de alunos.'),
    callout('Depois da comunicação', 'Outros docentes podem discutir os critérios, propor novas interpretações e examinar a estratégia em outros contextos. Essa interlocução ajuda a superar a certeza privada de que uma atividade funciona para todos.')
], 'A investigação coletiva explicita perguntas, procedimentos, evidências e limites. Compartilhar a prática permite discussão profissional, sem transformar um resultado em garantia universal.', match('Associe a informação à parte do estudo', [
    ['Por que os alunos confundem a informação de dois mapas?', 'Problema de investigação'],
    ['Comparar legendas e fontes com perguntas orientadoras', 'Intervenção de ensino'],
    ['Justificativas produzidas em dois momentos', 'Evidências para análise'],
    ['Diferenças entre turmas e outras intervenções', 'Condições e limites']]))

lesson(12, 'Casos integrados e preparação para a prova', 'Justificar, comparar e argumentar', 12, [
    text('Analise a decisão, não só uma palavra', 'Em questões sobre os saberes docentes, pergunte primeiro o que o professor fez. Depois observe o destaque: conteúdo e investigação; objetivos e progressão; aprendizagem profissional na prática; ou experiência pública e investigada. O contexto pode mobilizar vários saberes, embora a questão peça um foco.\nSe o enunciado nomeia um autor, retome sua definição. Evite associar toda ação em sala a “ação pedagógica” no sentido específico de Gauthier. Nas questões integradas, justifique como as diferentes fontes de conhecimento participam da decisão.'),
    animation('inequality', 'Use a cena para analisar a decisão de ensino', 'A chuva e as condições de acesso são hipotéticas. Imagine que o objetivo seja explicar relações entre infraestrutura e acesso. O saber disciplinar sustenta a análise; o curricular orienta o objetivo; observar dúvidas alimenta a experiência docente; investigar a intervenção permite seu exame público.'),
    compare('Duas respostas a um caso', 'Resposta genérica', '“A professora usa todos os saberes.” A frase nomeia a articulação, mas não demonstra onde ela aparece.', 'Resposta justificada', '“Ao explicar circulação, mobiliza conhecimento disciplinar; ao situar o objetivo na progressão, usa o curricular; ao rever uma dificuldade recorrente, aprende com a experiência.”'),
    listing('Roteiro para uma resposta curta', 'Apresente a ideia que responde ao tema.', 'Explique o sentido de um ou mais saberes.', 'Analise uma decisão concreta de ensino de Geografia.', 'Relacione a intervenção à aprendizagem e indique um limite.'),
    callout('Treino autoral', 'O simulado reúne 20 questões desta unidade. Os enunciados foram produzidos para estudo; não são questões oficiais nem previsão do que cairá na seleção. A oficina de redação oferece autoavaliação formativa.'),
    text('Retome os pontos difíceis', 'Antes de concluir, confira se consegue distinguir: assunto e objetivo; experiência do aluno e aprendizagem profissional do professor; divulgação da prática e sua investigação; recurso didático e conhecimento para ensinar um conteúdo. Faça os cartões e retorne às questões em que errou.')
], 'Uma boa resposta explica conceitos e decisões concretas. As categorias ajudam a analisar a prática; autores, contextos e limites precisam aparecer no argumento.', order('Construa uma resposta argumentativa', [
    'Responder ao tema com uma ideia central.',
    'Explicar os saberes ou conceitos necessários.',
    'Analisar uma decisão de ensino com esses conceitos.',
    'Concluir relacionando a prática à aprendizagem e aos seus limites.' ]))

questions = []


def q(lesson_n, stem, options, answer, feedback, tag, pool='lesson'):
    assert len(options) == len(feedback)
    questions.append(dict(id=f'q{len(questions)+1:02d}', lesson=f'l{lesson_n:02d}', stem=stem,
                          options=options, answer=answer, feedback=feedback, tag=tag, pool=pool,
                          type='truefalse' if options == ['Verdadeiro', 'Falso'] else 'single'))


# 40 questões de prática: a correção explica cada alternativa.
q(1, 'Ao preparar uma aula sobre acesso à escola, a professora consulta objetivos, revisa conceitos e considera dificuldades da turma. Qual interpretação é mais adequada?',
  ['O planejamento combina diferentes saberes profissionais.', 'O currículo substitui a necessidade de compreender o conteúdo.', 'A experiência define a aula sem relação com outras fontes.', 'A escolha do recurso resume os conhecimentos mobilizados.'], 0,
  ['As decisões articulam conteúdo, currículo e aprendizagem profissional. As categorias ajudam a ler os destaques dessa articulação.', 'Consultar objetivos não substitui conceitos e critérios de análise da matéria ensinada.', 'A experiência participa da decisão, mas dialoga com objetivos, conteúdo e condições da turma.', 'O recurso é uma parte da situação de ensino; não resume as decisões que a sustentam.'], 'articulação dos saberes')
q(1, 'Uma questão destaca que a professora relaciona circulação, redes e acesso ao explicar trajetos. Qual saber predomina nesse destaque?',
  ['Curricular.', 'Disciplinar.', 'Da experiência.', 'Da ação pedagógica no sentido de Gauthier.'], 1,
  ['O saber curricular aparece quando se enfatizam objetivos, seleção ou progressão do ensino.', 'O destaque é a compreensão de conceitos e relações próprias do conteúdo geográfico.', 'Seria o foco se o enunciado destacasse a aprendizagem profissional construída na prática.', 'O caso não destaca a publicização e a investigação de uma prática de ensino.'], 'saber disciplinar')
q(1, 'As categorias de saberes docentes são úteis para estudar a prática, embora uma mesma decisão possa mobilizar mais de uma delas.',
  ['Verdadeiro', 'Falso'], 0,
  ['A separação é analítica. No trabalho docente, conhecimentos de diferentes fontes participam de decisões concretas.', 'O enunciado reconhece a articulação e não afirma que as categorias sejam caixas isoladas.'], 'articulação dos saberes')
q(1, 'A professora seleciona uma aprendizagem prevista para o percurso da turma e define como o conteúdo será retomado. Qual aspecto está em destaque?',
  ['A formação histórica do conceito geográfico.', 'A descrição dos materiais disponíveis na sala.', 'A seleção e a progressão curriculares.', 'A validação pública de uma investigação da docência.'], 2,
  ['A história do conceito pertence a outra pergunta; o foco aqui está no percurso de aprendizagem.', 'Ter materiais disponíveis não explica a seleção do objetivo e sua progressão.', 'Situar a aprendizagem e organizar sua retomada são decisões relacionadas ao saber curricular.', 'Não há no caso investigação pública da prática; há organização do ensino para a turma.'], 'saber curricular')

q(2, 'Uma foto do rio Guamá é usada para iniciar uma aula. Que pergunta demonstra cuidado com o saber disciplinar?',
  ['Quais relações espaciais podemos investigar e que outras fontes serão necessárias?', 'Qual legenda decorativa combina melhor com a imagem?', 'Como mostrar a mesma foto em todas as séries sem mudar o objetivo?', 'Como reconhecer pela foto a renda de quem usa o rio?'], 0,
  ['A pergunta mobiliza relações geográficas e os limites da evidência, sem tirar conclusões que a fotografia não sustenta.', 'A apresentação pode ajudar, mas a escolha decorativa não demonstra análise do conteúdo.', 'As decisões de ensino precisam considerar objetivos e conhecimentos da turma, não apenas repetir o material.', 'Uma foto não permite determinar a renda das pessoas; essa conclusão exige informações adicionais.'], 'fontes e conceitos')
q(2, 'O professor explica por que 1:10.000 é uma escala maior que 1:100.000. O que essa decisão evidencia principalmente?',
  ['Conhecimento das relações do conceito de escala.', 'A definição da carga horária curricular.', 'A divulgação de uma experiência docente.', 'O registro das preferências dos estudantes.'], 0,
  ['Compreender a redução representada pelas escalas expressa domínio do conteúdo cartográfico.', 'A carga horária não é o aspecto destacado na explicação das escalas.', 'Não há publicização de uma experiência; há explicação de um conceito.', 'As preferências podem orientar um planejamento, mas não são o foco dessa decisão.'], 'saber disciplinar')
q(2, 'Um mapa de localização de escolas informa onde elas estão. Para explicar diferenças no acesso, o professor deveria:',
  ['Relacionar o mapa a fontes sobre trajetos e condições de circulação.', 'Tratar os pontos do mapa como prova suficiente das causas de acesso.', 'Trocar a legenda por uma lista de nomes para dispensar a análise.', 'Deduzir o tempo de viagem apenas pela proximidade visual dos pontos.'], 0,
  ['A localização contribui, mas a explicação de acesso exige relações com trajetos, meios e condições.', 'Localizar escolas não explica, por si só, os fatores que dificultam ou facilitam a chegada.', 'Listar nomes pode apoiar uma identificação, mas não responde à pergunta sobre diferenças de acesso.', 'Proximidade visual depende da representação e não informa sozinha tempo ou condições de viagem.'], 'limites das fontes')
q(2, 'O saber disciplinar da Geografia inclui critérios para formular perguntas e examinar fontes, além de nomes e localizações.',
  ['Verdadeiro', 'Falso'], 0,
  ['Os modos de compreender e investigar o conteúdo fazem parte do conhecimento do campo disciplinar.', 'Restringir o saber disciplinar a nomes deixaria de fora conceitos, relações e critérios de investigação.'], 'saber disciplinar')

q(3, 'Qual enunciado expressa um objetivo de aprendizagem, em vez de apenas nomear um tema ou recurso?',
  ['Comparar tempos de viagem e justificar diferenças entre dois trajetos.', 'Transportes do município.', 'Mapa digital de circulação.', 'Vídeo sobre estradas e rios.'], 0,
  ['O enunciado indica uma ação intelectual e o que o estudante deverá conseguir explicar.', 'A frase nomeia o assunto, mas não esclarece o que se espera que o aluno aprenda a fazer.', 'O mapa é um recurso; ainda falta explicitar a aprendizagem a que servirá.', 'O vídeo é um suporte possível, não uma definição do objetivo de aprendizagem.'], 'objetivos de aprendizagem')
q(3, 'Uma leitura adequada da relação entre BNCC e planejamento de aula reconhece que:',
  ['A referência às aprendizagens essenciais exige interpretação curricular e decisões de ensino.', 'A BNCC descreve todas as intervenções que devem ocorrer em cada aula.', 'Um código de habilidade copiado garante o alinhamento da avaliação.', 'A escolha de uma atividade interessante dispensa a leitura do currículo.'], 0,
  ['A referência curricular precisa ser relacionada ao contexto, ao objetivo, à atividade e à avaliação.', 'A BNCC não é um roteiro completo de cada aula e não antecipa todas as condições concretas.', 'O código registrado não garante que a atividade e a avaliação trabalhem a aprendizagem pretendida.', 'O interesse dos estudantes conta, mas não elimina a seleção e a justificativa curricular.'], 'saber curricular')
q(3, 'O objetivo é explicar por que o menor trajeto não tem necessariamente menor tempo. Qual tarefa de avaliação se alinha melhor a ele?',
  ['Listar nomes de meios de transporte.', 'Justificar a comparação usando distância, tempo e condições das rotas.', 'Colorir cada trajeto com uma cor diferente.', 'Copiar a definição de transporte do livro.'], 1,
  ['A lista mostra reconhecimento de termos, mas não exige a explicação pretendida.', 'A tarefa solicita a relação entre medidas e condições que constitui o objetivo da aula.', 'Colorir pode apoiar a leitura, mas não demonstra a explicação das diferenças de tempo.', 'Copiar uma definição não mostra se o aluno consegue analisar o caso e justificar sua conclusão.'], 'alinhamento curricular')
q(3, 'Organizar uma progressão curricular significa usar a mesma tarefa em todas as etapas, mudando apenas seu título.',
  ['Verdadeiro', 'Falso'], 1,
  ['A progressão envolve relações e desafios de aprendizagem, considerando o percurso da turma.', 'Trocar o título não assegura avanço. É necessário planejar o que será identificado, comparado e explicado.'], 'progressão curricular')

q(4, 'Após observar dificuldades recorrentes com a legenda, a professora modifica sua intervenção e acompanha as novas respostas. Qual aspecto evidencia saber da experiência?',
  ['A aprendizagem profissional construída ao observar e rever a prática.', 'A existência de cores na legenda do mapa.', 'A numeração da habilidade citada no plano.', 'A garantia de que a mudança funcionará em qualquer turma.'], 0,
  ['O foco é o que a professora aprende no exercício da profissão e como isso orienta uma nova decisão.', 'As cores fazem parte do recurso; o saber experiencial está no aprendizado da professora sobre o ensino.', 'A leitura de uma habilidade destaca o saber curricular, não a aprendizagem profissional enfatizada.', 'Uma revisão pode ajudar, mas a experiência não oferece garantia universal para outras turmas.'], 'saber da experiência')
q(4, 'Qual registro ajuda melhor a transformar uma impressão sobre a aula em reflexão profissional?',
  ['“A sala ficou silenciosa durante a tarefa.”', '“Concluíram o exercício antes do intervalo.”', '“Parte da turma confundiu cor e valor; vou retomar a legenda e comparar novas justificativas.”', '“Usarei a mesma atividade porque já está preparada.”'], 2,
  ['O silêncio informa uma condição, mas não esclarece a compreensão do conteúdo.', 'O tempo de conclusão não demonstra sozinho se os estudantes compreenderam o conceito.', 'O registro identifica uma dificuldade, uma intervenção e uma maneira de acompanhar a aprendizagem.', 'A conveniência do material não justifica manter a atividade diante das necessidades da turma.'], 'reflexão sobre a prática')
q(4, 'O relato de um aluno sobre sua viagem até a escola e a aprendizagem profissional do professor são exatamente o mesmo saber experiencial docente.',
  ['Verdadeiro', 'Falso'], 1,
  ['O aluno oferece conhecimento do cotidiano. O saber experiencial docente diz respeito à aprendizagem profissional do professor.', 'As duas experiências podem dialogar, mas pertencem a sujeitos e focos diferentes de análise.'], 'saberes docentes e discentes')

q(5, 'No sentido discutido por Gauthier, o saber da ação pedagógica está relacionado a:',
  ['Experiência docente tornada pública e testada por pesquisas sobre o ensino.', 'Qualquer movimento do professor dentro da sala.', 'Preferências pessoais mantidas como certeza privada.', 'Todo conteúdo previsto no programa da disciplina.'], 0,
  ['A publicização e a investigação distinguem esse saber da experiência restrita ao julgamento privado.', 'O termo tem uma acepção específica no autor; não nomeia simplesmente toda ação em sala.', 'A certeza privada é justamente um limite que a investigação pública procura superar.', 'O programa é ligado ao saber curricular, enquanto aqui se discute conhecimento sobre a prática de ensino.'], 'Gauthier')
q(5, 'Um professor posta a foto de uma dinâmica e escreve “a turma adorou”. A partir desse registro, é mais adequado concluir que:',
  ['Há um relato público da experiência, mas faltam elementos para examinar a aprendizagem.', 'A aprovação dos alunos comprova o domínio do conceito ensinado.', 'A divulgação equivale à validação por pesquisa.', 'O registro demonstra que a atividade serve a qualquer conteúdo.'], 0,
  ['A postagem comunica a atividade, mas não esclarece objetivo, procedimento, evidências e limites.', 'Gostar da atividade não comprova, por si só, a compreensão dos conceitos.', 'Publicar um relato e investigar a prática são ações relacionadas, porém distintas.', 'O registro não autoriza generalizar a atividade para todo conteúdo e toda turma.'], 'publicização e investigação')
q(5, 'Qual informação torna mais examinável um relato de ensino sobre leitura de mapas?',
  ['A quantidade de elogios recebidos pelo professor.', 'A descrição de objetivos, intervenção, critérios, respostas e condições da turma.', 'O nome comercial do aplicativo usado.', 'A afirmação de que a aula foi inovadora.'], 1,
  ['Os elogios não permitem examinar a aprendizagem nem reconstruir a intervenção.', 'Essas informações permitem compreender e discutir o procedimento, as evidências e seus limites.', 'O nome do recurso não explica como ele foi usado nem o que os estudantes aprenderam.', 'Chamar a aula de inovadora não oferece elementos para analisar seus efeitos e condições.'], 'evidências da prática')
q(5, 'Uma equipe observa melhora após uma sequência. Por que deve discutir limites antes de atribuir a melhora exclusivamente à estratégia?',
  ['Porque outras condições e intervenções também podem ter participado do resultado.', 'Porque dados de aprendizagem nunca contribuem para conhecer a prática.', 'Porque os resultados dispensam a descrição do contexto.', 'Porque todo saber da experiência precisa ser descartado.'], 0,
  ['Uma mudança observada não estabelece sozinha uma causa exclusiva. É preciso analisar condições e explicações alternativas.', 'Dados podem contribuir, desde que sejam interpretados com critérios e atenção ao contexto.', 'O contexto ajuda a interpretar os resultados e a discutir os limites da conclusão.', 'A experiência é uma fonte importante; o ponto é submetê-la a exame, não eliminá-la.'], 'limites da investigação')

q(6, 'A discussão de Tardif sobre saberes temporais, plurais e situados orienta qual pergunta?',
  ['Como diferentes fontes e momentos da trajetória participam do conhecimento profissional?', 'Qual recurso digital garante uma aula bem-sucedida?', 'Como atribuir toda decisão docente a um saber isolado?', 'Qual sequência pode ser repetida sem considerar o contexto?'], 0,
  ['A pergunta analisa origem, desenvolvimento e mobilização dos saberes ao longo do trabalho e da formação.', 'A discussão não procura uma tecnologia que garanta aprendizagem em qualquer situação.', 'A pluralidade sugere diferentes fontes e articulações, não isolamento de cada decisão.', 'O caráter situado exige considerar as condições; não autoriza repetição indiferente ao contexto.'], 'Tardif')
q(6, 'Uma professora escolhe uma representação para enfrentar a confusão entre distância e tempo. Qual foco aproxima a análise da contribuição de Shulman?',
  ['A numeração do item no currículo.', 'As formas de tornar um conteúdo ensinável diante de dificuldades específicas.', 'A antiguidade da professora na escola.', 'A divulgação de uma investigação para validação pública.'], 1,
  ['A numeração curricular não é o foco da representação usada para ensinar o conceito.', 'Representações e dificuldades próprias do ensino da matéria integram a discussão do conhecimento pedagógico do conteúdo.', 'O tempo de trabalho não explica sozinho a adequação da representação ao conteúdo.', 'Esse seria outro foco; a questão destaca a relação entre matéria, representação e dificuldade de aprendizagem.'], 'Shulman')
q(6, 'Conhecimento pedagógico do conteúdo em Shulman e saber da ação pedagógica em Gauthier devem ser usados como termos automaticamente equivalentes.',
  ['Verdadeiro', 'Falso'], 1,
  ['Os autores tratam problemas e classificações diferentes; proximidade não é equivalência de definição.', 'É preciso conservar o sentido de cada discussão e analisar o foco do enunciado.'], 'comparação entre autores')

q(7, 'Na cena, a rota A tem 8 km e 45 minutos; B tem 15 km e 25 minutos. Qual resposta demonstra a distinção que o professor pretende ensinar?',
  ['B tem menor tempo, embora sua distância seja maior.', 'A tem menor tempo porque é mais curta.', 'As duas rotas têm a mesma duração porque chegam ao mesmo destino.', 'A estrada sempre será mais rápida que o rio.'], 0,
  ['Você comparou as duas medidas e usou os dados do caso sem tratar distância e tempo como equivalentes.', 'Os dados indicam 45 minutos para A e 25 para B; distância menor não implica menor tempo nesse exemplo.', 'Ter o mesmo destino não significa levar o mesmo tempo para alcançá-lo.', 'O caso hipotético não sustenta uma regra geral sobre estradas e rios.'], 'conteúdo e representação')
q(7, 'Qual pergunta do professor favorece a revisão da ideia “menor distância sempre significa menor tempo”?',
  ['Que nome podemos dar ao barco desenhado?', 'Quantas cores aparecem na cena?', 'Como os tempos das duas rotas mudam sua previsão inicial?', 'Qual opção foi escolhida por mais colegas?'], 2,
  ['O nome do barco não enfrenta a relação conceitual em estudo.', 'As cores podem organizar a representação, mas a contagem não analisa distância e tempo.', 'A pergunta confronta a previsão com os dados e solicita uma revisão justificada.', 'A popularidade da escolha não demonstra a correção da relação entre as medidas.'], 'mediação do conteúdo')
q(7, 'Escolher uma animação e saber como ela pode enfrentar uma dificuldade conceitual são decisões idênticas.',
  ['Verdadeiro', 'Falso'], 1,
  ['A animação é um recurso. Saber por que usá-la e como verificar a compreensão é uma decisão profissional mais ampla.', 'Recurso e conhecimento para ensinar se relacionam, mas não são o mesmo elemento da prática.'], 'recurso e saber docente')
q(7, 'Ao simplificar uma explicação de escala para a turma, o professor deveria:',
  ['Conservar a precisão do conceito e verificar se a representação ajuda a entendê-lo.', 'Preferir uma frase curta mesmo que inverta a relação entre as escalas.', 'Dispensar perguntas dos alunos para concluir a exposição.', 'Usar qualquer analogia desde que desperte interesse.'], 0,
  ['Clareza envolve linguagem acessível e correção conceitual, acompanhadas da verificação da aprendizagem.', 'Uma frase simples que ensina uma relação errada prejudica a aprendizagem do conceito.', 'As perguntas ajudam a identificar o que a explicação esclareceu ou deixou confuso.', 'Interesse é útil, mas a analogia precisa corresponder ao conceito e ter seus limites considerados.'], 'precisão didática')


q(8, 'No planejamento sobre trajetos na chuva, a professora pergunta que explicação espera dos alunos. Essa pergunta ajuda a:',
  ['Articular objetivo, atividade e avaliação.', 'Escolher o recurso mais caro disponível.', 'Substituir a leitura do conteúdo pela opinião da turma.', 'Manter a mesma avaliação para qualquer objetivo.'], 0,
  ['Definir a aprendizagem esperada ajuda a selecionar uma situação e critérios coerentes para acompanhá-la.', 'O preço do recurso não determina se ele atende ao objetivo de aprendizagem.', 'Conhecimentos da turma dialogam com a matéria, mas não substituem a compreensão disciplinar.', 'Objetivos diferentes podem exigir evidências diferentes; repetir a avaliação sem análise pode perder alinhamento.'], 'planejamento integrado')
q(8, 'Sem internet na sala, o professor usa um croqui impresso para comparar trajetos. Qual é o critério mais relevante para justificar a adaptação?',
  ['A possibilidade de conservar a tarefa de comparação e o objetivo de aprendizagem.', 'A semelhança da impressão com a aparência de um aplicativo.', 'A exigência de usar tecnologia em toda aula.', 'A redução do trabalho a preencher o tempo disponível.'], 0,
  ['A mudança de suporte é justificada quando permite realizar as operações necessárias ao objetivo.', 'A aparência pode ajudar, mas não substitui a adequação da atividade ao conteúdo.', 'A aprendizagem não depende de usar tecnologia digital em todas as situações.', 'A proposta deve sustentar aprendizagem, não apenas ocupar o tempo da turma.'], 'adaptação de recursos')
q(8, 'Qual decisão destaca principalmente a experiência docente no planejamento de uma nova aula?',
  ['Rever uma dificuldade de leitura de mapas observada em turmas anteriores.', 'Localizar a habilidade no documento curricular.', 'Explicar cientificamente o conceito de rede.', 'Analisar uma pesquisa publicada sobre uma intervenção.'], 0,
  ['O destaque é o conhecimento construído na prática profissional e usado para antecipar uma necessidade.', 'Localizar uma habilidade enfatiza a orientação curricular do planejamento.', 'Explicar rede enfatiza o domínio disciplinar, embora possa dialogar com outras fontes.', 'Examinar uma prática investigada enfatiza outro aspecto do conhecimento profissional.'], 'saberes no planejamento')

q(9, 'Estudantes do campo contam trajetos de comercialização. Qual intervenção amplia o diálogo com esses saberes?',
  ['Comparar os relatos e relacioná-los a circulação e redes, buscando outras fontes.', 'Registrar as falas e encerrar a aula antes da comparação.', 'Presumir que todos os alunos vivem a mesma experiência.', 'Tratar cada relato como explicação suficiente de toda a região.'], 0,
  ['A intervenção valoriza o vivido e oferece conceitos e fontes para ampliar sua interpretação.', 'A escuta é relevante, mas a situação ainda precisa trabalhar as relações e explicações pretendidas.', 'Viver no campo não produz experiências iguais; o professor precisa ouvir a diversidade da turma.', 'Um relato tem alcance situado e não representa automaticamente todas as relações regionais.'], 'saberes dos estudantes')
q(9, 'Na cena da praça, três personagens atribuem sentidos diferentes ao lugar. Para o professor, a cena ajuda a:',
  ['Discutir diversidade de experiências e construir perguntas sobre o lugar.', 'Demonstrar que um personagem representa todos os moradores.', 'Concluir que o pertencimento elimina qualquer dificuldade de acesso.', 'Classificar as falas dos personagens como experiência profissional docente.'], 0,
  ['As diferenças oferecem um ponto de partida para comparar sentidos e discutir relações espaciais.', 'Um personagem fictício não representa a totalidade das pessoas ou suas experiências.', 'Pertencimento e dificuldade podem coexistir; uma experiência não elimina outras dimensões.', 'Os relatos são experiências dos personagens, não o saber profissional do professor.'], 'cotidiano e mediação')
q(9, 'O diálogo entre conhecimento cotidiano e científico, na contribuição discutida de Cavalcanti, procura:',
  ['Ampliar a compreensão do vivido mediante a formação de conceitos geográficos.', 'Reduzir o ensino à memorização de definições sem situações de uso.', 'Substituir a análise geográfica por uma soma de opiniões.', 'Excluir os conhecimentos dos alunos antes de apresentar o conteúdo.'], 0,
  ['A mediação considera o cotidiano e trabalha conceitos como instrumentos para interpretar relações geográficas.', 'Definições isoladas não garantem que o conceito seja usado para compreender uma situação.', 'Os relatos precisam de comparação e mediação conceitual; não basta somar opiniões.', 'O cotidiano pode participar da construção do conhecimento, não precisa ser excluído.'], 'Cavalcanti')

q(10, 'Uma turma se diverte em um jogo sobre mapas. Para verificar a aprendizagem conceitual, o professor deveria também:',
  ['Examinar como os alunos justificam interpretações usando legenda e informações do mapa.', 'Contar quantas vezes a turma riu.', 'Comparar a duração da atividade com o intervalo.', 'Registrar se os alunos preferem jogos a textos.'], 0,
  ['As justificativas oferecem evidências relacionadas à leitura cartográfica e ao objetivo.', 'O riso é uma reação à atividade, mas não demonstra sozinho a compreensão cartográfica.', 'A duração informa uma condição de realização, não o domínio do conceito.', 'A preferência importa para o planejamento, mas não substitui a evidência da aprendizagem.'], 'avaliação da aprendizagem')
q(10, 'O aluno responde “B, porque 25 minutos é menos que 45”. Qual feedback acompanha melhor esse avanço?',
  ['Você comparou o tempo; explique também como ele se relaciona com as distâncias do caso.', 'Como a resposta está curta, não existe nenhum conhecimento demonstrado.', 'Essa frase comprova que qualquer estrada é mais rápida.', 'Você só aprenderá se copiar a conclusão do professor.'], 0,
  ['O comentário reconhece o que apareceu e indica um próximo passo ligado ao objetivo.', 'A comparação de tempos é um conhecimento demonstrado, embora ainda possa ser ampliado.', 'O caso permite comparar essas rotas, mas não sustenta uma regra universal sobre estradas.', 'O aluno precisa compreender e justificar a relação, não apenas copiar uma conclusão.'], 'feedback formativo')
q(10, 'Replanejar a partir das justificativas dos alunos significa:',
  ['Usar evidências para decidir que explicações e intervenções precisam ser retomadas.', 'Atribuir a dificuldade exclusivamente à falta de interesse.', 'Abandonar o objetivo sempre que aparece um erro.', 'Repetir a mesma tarefa sem analisar as respostas.'], 0,
  ['A leitura das produções orienta decisões sobre as necessidades da turma e a intervenção docente.', 'Antes de atribuir causas, é necessário examinar respostas, condições e a situação de ensino.', 'O erro pode orientar uma nova intervenção para o mesmo objetivo de aprendizagem.', 'A repetição sem análise não aproveita a informação oferecida pelas respostas.'], 'replanejamento')

q(11, 'Uma equipe quer investigar dificuldade de leitura de mapas. Qual problema é mais delimitado para orientar seu estudo?',
  ['Que mudanças aparecem nas justificativas após uma comparação orientada de legendas?', 'Como resolver todos os problemas da educação?', 'Qual professor é mais popular entre os estudantes?', 'Como provar antecipadamente que a estratégia escolhida é perfeita?'], 0,
  ['A pergunta delimita aprendizagem, intervenção e evidências que podem ser analisadas.', 'A pergunta é ampla demais para orientar procedimentos e critérios claros nesse estudo.', 'Popularidade não corresponde ao problema de aprendizagem cartográfica em investigação.', 'Uma pesquisa deve examinar resultados e limites, não partir de uma conclusão imune à análise.'], 'investigação da prática')
q(11, 'Qual conjunto favorece o exame público de uma prática de ensino?',
  ['Procedimentos claros, produções analisadas, critérios e limites do estudo.', 'Apenas um título atraente e uma foto da turma.', 'Uma lista de ferramentas digitais usadas.', 'A afirmação de que todos aprenderam, sem exemplos de respostas.'], 0,
  ['O conjunto permite reconstruir a intervenção e discutir as evidências e o alcance das conclusões.', 'O título e a foto não mostram o que foi aprendido nem os critérios de análise.', 'Ferramentas são recursos; é necessário explicitar seu uso, a aprendizagem e as evidências.', 'Uma afirmação sem evidências não permite examinar como a aprendizagem foi identificada.'], 'comunicação profissional')
q(11, 'Um relatório usa exemplos de erros dos alunos para discutir uma intervenção. Qual decisão mantém o foco profissional?',
  ['Apresentar as respostas sem identificar os estudantes e explicitar os critérios da análise.', 'Publicar o nome de quem errou para facilitar a classificação.', 'Omitir as dificuldades para aumentar a aparência de sucesso.', 'Retirar informações sobre as condições da sequência.'], 0,
  ['O foco fica na análise pedagógica, com cuidado com os estudantes e transparência dos critérios.', 'Identificar publicamente quem errou não é necessário para discutir o problema de ensino.', 'Dificuldades também são evidências; ocultá-las compromete a interpretação da prática.', 'As condições ajudam a compreender o procedimento e os limites dos resultados.'], 'investigação coletiva')

q(12, 'O enunciado informa que a professora examinou uma prática tornada pública e testada em pesquisas. Qual associação é mais direta?',
  ['Saber da ação pedagógica, na discussão de Gauthier.', 'Reconhecimento de um recurso decorativo.', 'Saber disciplinar definido apenas como lista de lugares.', 'Experiência privada tratada como certeza não examinável.'], 0,
  ['O destaque reúne a publicização e a investigação que caracterizam o sentido estudado do termo.', 'O caso destaca conhecimento examinável sobre a prática, não a decoração de um material.', 'Listar lugares não é a definição completa do saber disciplinar e não é o foco do enunciado.', 'A investigação pública ultrapassa justamente o limite da certeza mantida em âmbito privado.'], 'leitura de enunciados')
q(12, 'Qual resposta analisa melhor a articulação dos saberes em uma aula?',
  ['Relacionar decisões de conteúdo, objetivo e revisão da prática aos saberes que as sustentam.', 'Afirmar “o professor usa todos os saberes” sem explicar nenhuma decisão.', 'Nomear os quatro focos do edital sem relacioná-los à situação.', 'Escolher uma categoria e negar qualquer participação das demais.'], 0,
  ['A resposta explica onde a articulação aparece e demonstra compreensão das categorias.', 'A frase pode reconhecer a articulação, mas não a demonstra na prática analisada.', 'A lista de termos não substitui o uso dos conceitos para interpretar o caso.', 'Uma decisão pode ter um foco predominante e ainda articular outras fontes de conhecimento.'], 'argumentação')


def final(n, stem, options, answer, feedback, tag):
    q(n, stem, options, answer, feedback, tag, pool='final')


# 20 questões próprias para o simulado, sem repetir os enunciados da prática.
final(2, 'Em uma aula, o professor verifica se o mapa permite explicar fluxos ou apenas localizar pontos. O aspecto predominante dessa verificação é:',
      ['O critério disciplinar de análise das fontes.', 'A organização curricular do bimestre.', 'O aprendizado da gestão do tempo de aula.', 'A investigação pública de uma intervenção didática.'], 0,
      ['A decisão analisa a relação entre pergunta geográfica e informação oferecida por uma fonte.', 'O caso não enfatiza seleção ou progressão curricular do bimestre.', 'A verificação não trata da duração da atividade, mas do alcance informativo do mapa.', 'Não há exame público de uma intervenção; o foco é a análise da fonte geográfica.'], 'fontes geográficas')
final(3, 'Uma professora escolhe o que retomar antes de comparar fluxos, consultando o percurso previsto para a turma. O destaque principal é:',
      ['O saber curricular.', 'A interpretação disciplinar de uma fotografia.', 'A acepção de ação pedagógica como validação pública.', 'A reação afetiva da turma ao recurso.'], 0,
      ['A consulta ao percurso e a decisão de retomada enfatizam seleção e progressão de aprendizagem.', 'O enunciado não destaca a interpretação de uma imagem, mas a organização do ensino.', 'Não foi descrita uma prática tornada pública e investigada.', 'As reações da turma podem importar, mas não são o aspecto enfatizado.'], 'seleção curricular')
final(4, 'O professor afirma: “Aprendi a pedir comparação de legendas ao perceber um erro recorrente; agora verifico se essa decisão ajuda esta turma”. O destaque é:',
      ['Aprendizagem profissional construída na experiência e aberta à revisão.', 'Aplicação de um procedimento independente do contexto.', 'Substituição do conteúdo pelo tempo de serviço.', 'Validação da prática garantida pela repetição.'], 0,
      ['O professor explica a origem prática da decisão e acompanha sua adequação em uma nova situação.', 'A fala considera a turma atual, portanto não apresenta um procedimento indiferente ao contexto.', 'A observação da dificuldade serve para melhorar o ensino do conteúdo, não para substituí-lo.', 'Repetir uma prática não valida automaticamente sua explicação nem seus resultados.'], 'experiência docente')
final(5, 'Uma intervenção foi descrita, submetida a pesquisa sobre o ensino e discutida publicamente com suas evidências. Na acepção estudada de Gauthier, ela se aproxima de:',
      ['Saber da ação pedagógica.', 'Saber curricular como seleção dos conteúdos.', 'Saber disciplinar como domínio da matéria.', 'Julgamento experiencial mantido em âmbito privado.'], 0,
      ['Publicização e investigação da prática correspondem ao foco específico desse saber no autor.', 'A seleção curricular pode integrar a intervenção, mas não é o aspecto enfatizado.', 'O conhecimento da matéria participa do ensino, porém não define o destaque de investigação pública.', 'A descrição ultrapassa o caráter privado e apresenta evidências para exame público.'], 'ação pedagógica')
final(1, 'Duas afirmações: I — Uma decisão pode articular vários saberes. II — Identificar um saber predominante implica negar a presença dos demais. A leitura correta é:',
      ['I é verdadeira e II é falsa.', 'I e II são verdadeiras.', 'I é falsa e II é verdadeira.', 'I e II são falsas.'], 0,
      ['A análise pode destacar uma fonte de conhecimento sem transformar a prática em compartimentos isolados.', 'A primeira é adequada; a segunda erra ao converter predominância em exclusividade.', 'A articulação é possível, e a predominância não nega outras fontes de conhecimento.', 'A primeira reconhece corretamente a articulação dos saberes; só a segunda precisa ser recusada.'], 'articulação')
final(3, 'Tema: redes de transporte. Objetivo: explicar uma diferença de acesso. Qual avaliação preserva melhor essa intenção?',
      ['Interpretar trajetos e justificar a diferença com dados e condições da rede.', 'Identificar o nome de uma rodovia sem discutir relações.', 'Contar os símbolos do mapa sem ler a legenda.', 'Reproduzir a imagem apresentada pelo professor sem explicação.'], 0,
      ['A tarefa exige uma explicação apoiada nas relações estudadas e oferece evidências do objetivo.', 'Identificar um nome pode apoiar a análise, mas não verifica a explicação pretendida.', 'Contar símbolos não demonstra a compreensão da diferença de acesso.', 'Reproduzir a imagem não mostra necessariamente a compreensão das relações representadas.'], 'objetivo e avaliação')
final(7, 'Ao notar que “denominador maior” é confundido com “escala maior”, a professora compara duas representações do mesmo lugar e pede justificativas. O foco de Shulman ajuda a analisar:',
      ['A escolha de representações diante de uma dificuldade de aprendizagem do conteúdo.', 'A posição do conteúdo no calendário escolar.', 'A publicação dos resultados para exame por pesquisa.', 'A distância física entre a escola e a residência da professora.'], 0,
      ['A relação entre matéria, representação e dificuldade específica é central ao conhecimento pedagógico do conteúdo.', 'O calendário enfatizaria organização curricular, mas não é o foco da comparação descrita.', 'A investigação pública seria outro aspecto; o caso destaca como tornar o conceito ensinável.', 'A distância da residência não é relevante para a dificuldade conceitual descrita.'], 'conhecimento pedagógico do conteúdo')
final(6, 'Qual alternativa conserva os sentidos dos autores estudados?',
      ['Tardif: pluralidade e trajetória; Gauthier: prática pública e investigada; Shulman: conhecimento para ensinar uma matéria.', 'Tardif: recurso digital; Gauthier: todo gesto em sala; Shulman: programa curricular como única fonte.', 'Tardif: saber isolado; Gauthier: certeza privada; Shulman: analogia sem relação com o conceito.', 'Tardif: experiência do aluno como sinônimo de docência; Gauthier: popularidade; Shulman: tempo de serviço.'], 0,
      ['A alternativa sintetiza os focos trabalhados sem afirmar que as classificações sejam equivalentes.', 'Os autores não são definidos por esses elementos, e ação pedagógica possui sentido específico em Gauthier.', 'A alternativa contraria pluralidade, exame público da prática e precisão das representações de ensino.', 'São aspectos que podem aparecer em situações escolares, mas não definem os conceitos desses autores.'], 'autores e conceitos')
final(9, 'Em uma turma do campo, uma aluna descreve a rota de sua produção. Para formar uma explicação geográfica mais ampla, a mediação deveria:',
      ['Relacionar o relato a outros trajetos, conceitos e fontes, considerando seu alcance.', 'Tratar o relato como retrato completo de toda a produção regional.', 'Trocar o relato por uma definição, sem estabelecer relações entre eles.', 'Presumir a experiência dos colegas sem lhes fazer perguntas.'], 0,
      ['A decisão dialoga com o cotidiano e amplia a interpretação com conceitos e evidências.', 'Um relato é situado e não representa automaticamente todas as relações regionais.', 'A definição precisa ser relacionada à situação para apoiar sua interpretação.', 'Os estudantes têm experiências diferentes; é preciso investigar, não presumir uma vivência comum.'], 'cotidiano e Geografia')
final(4, 'Ao ouvir dúvidas sobre o croqui, a professora aprende que precisa trabalhar melhor a orientação. O croqui do aluno e esse aprendizado docente são:',
      ['Conhecimentos relacionados na aula, com sujeitos e focos distintos.', 'Um único saber experiencial docente, sem distinção.', 'Informações sem relação com o ensino da Geografia.', 'Provas de validação pública de uma estratégia.'], 0,
      ['A produção do aluno informa sua compreensão; a professora constrói uma aprendizagem profissional ao analisá-la.', 'A experiência do estudante e o saber profissional do professor não são termos idênticos.', 'As produções e sua análise podem orientar a mediação e a aprendizagem geográfica.', 'O caso não apresenta investigação pública; mostra diálogo e aprendizado na prática.'], 'docentes e estudantes')
final(10, 'Após um jogo de localização, a turma identifica nomes, mas não justifica diferenças de acesso. O objetivo da aula era explicar essas diferenças. A professora deve reconhecer que:',
      ['Há uma aprendizagem observada, mas ela não cobre ainda toda a explicação pretendida.', 'O reconhecimento dos nomes comprova o objetivo completo.', 'O interesse da turma torna a justificativa desnecessária.', 'O erro de explicação elimina o conhecimento já demonstrado.'], 0,
      ['Reconhecer nomes é um avanço possível; o objetivo exige também relacionar e explicar as diferenças.', 'Identificar nomes e explicar acesso são operações distintas, embora possam participar da mesma aula.', 'O interesse contribui, mas não dispensa evidências da explicação solicitada.', 'É preciso reconhecer o que foi aprendido e o que ainda precisa de mediação.'], 'evidências e objetivo')
final(11, 'Uma equipe compara justificativas antes e depois de uma sequência e comunica procedimentos e limites. Que cuidado melhora a interpretação?',
      ['Considerar outras intervenções e diferenças de contexto antes de atribuir uma causa exclusiva.', 'Usar somente respostas que confirmem a expectativa inicial.', 'Omitir critérios para que cada leitor suponha seu próprio resultado.', 'Tratar qualquer mudança como garantia de aplicação em todas as turmas.'], 0,
      ['O cuidado reconhece que mudanças observadas precisam ser interpretadas com atenção às condições.', 'Selecionar apenas confirmações esconde evidências relevantes e compromete a análise.', 'Os critérios permitem compreender como as produções foram interpretadas.', 'As condições variam; uma mudança observada não autoriza garantia universal.'], 'investigação e limites')
final(5, 'A divulgação de uma atividade em uma rede social basta, por si só, para constituir saber da ação pedagógica no sentido de Gauthier.',
      ['Verdadeiro', 'Falso'], 1,
      ['A divulgação não substitui o exame da prática por pesquisas e a discussão de suas evidências.', 'Tornar público é relevante, mas o sentido estudado inclui investigação e teste da experiência.'], 'publicização')
final(6, 'Para Tardif, reconhecer que os saberes profissionais têm diferentes fontes permite analisar formação, trajetória e condições concretas de trabalho.',
      ['Verdadeiro', 'Falso'], 0,
      ['A pluralidade e o desenvolvimento temporal ajudam a examinar como o professor constrói e mobiliza seus saberes.', 'A afirmação relaciona fontes e trajetória; não reduz o saber a um material ou momento isolado.'], 'pluralidade dos saberes')
final(8, 'A professora mantém o objetivo de comparar trajetos, mas troca o mapa online por um material impresso. Qual justificativa analisa melhor essa decisão?',
      ['O suporte mudou, e a docente verifica se a tarefa continua permitindo a comparação pretendida.', 'Trocar o suporte significa abandonar o saber disciplinar.', 'A impressão garante aprendizagem sem necessidade de intervenção.', 'A adaptação é curricular apenas porque envolve papel.'], 0,
      ['A justificativa conserva a relação entre recurso, atividade e objetivo, acompanhando sua adequação.', 'O conteúdo e as relações geográficas podem continuar presentes em outro suporte.', 'O recurso precisa de uma situação de uso e da mediação; não garante aprendizagem sozinho.', 'O tipo de material não define, por si só, a natureza curricular da decisão.'], 'planejamento e condições')
final(7, 'A rota A tem 8 km e 45 minutos; B tem 15 km e 25 minutos. O aluno escolhe A como a de menor distância. O professor deveria:',
      ['Reconhecer que a escolha atende ao critério distância e perguntar como muda a decisão se o critério for tempo.', 'Marcar a escolha como errada porque B tem menor tempo.', 'Concluir que A também tem menor tempo.', 'Dispensar a explicação porque distância e tempo são equivalentes.'], 0,
      ['A é menor em distância. A pergunta seguinte permite distinguir os critérios sem invalidar uma comparação correta.', 'B tem menor tempo, mas o aluno respondeu pelo critério distância, para o qual A é correta.', 'O tempo de A é maior nos dados apresentados; as duas medidas precisam ser diferenciadas.', 'As medidas não são equivalentes e podem conduzir a escolhas diferentes no mesmo caso.'], 'critérios de comparação')
final(10, 'Ao ler “todas as estradas são mais rápidas que os rios”, qual intervenção enfrenta o limite dessa resposta?',
      ['Pedir que o aluno indique o que os dados das duas rotas permitem afirmar e o que exigiria novas fontes.', 'Aceitar a regra porque uma estrada foi mais rápida na cena.', 'Substituir os valores por uma preferência pessoal do professor.', 'Pedir apenas que o aluno copie o nome dos transportes.'], 0,
      ['A intervenção trabalha o alcance da evidência e a diferença entre conclusão situada e generalização.', 'Um exemplo não comprova uma regra sobre todas as estradas e rios.', 'A preferência do professor não substitui os dados e os critérios de análise.', 'Copiar nomes não enfrenta a generalização indevida feita na resposta.'], 'feedback e inferência')
final(11, 'Para apresentar exemplos de respostas no estudo de uma prática, a equipe deveria:',
      ['Preservar a identidade dos estudantes e explicar os critérios usados na análise.', 'Identificar quem errou para reforçar a credibilidade.', 'Eliminar respostas diferentes do padrão esperado.', 'Dispensar a descrição do procedimento realizado.'], 0,
      ['A decisão mantém o foco na investigação pedagógica e no cuidado com os participantes.', 'A identificação pública de quem errou não é necessária para analisar a intervenção.', 'Respostas diferentes podem revelar dificuldades e limites importantes para o estudo.', 'A descrição é necessária para compreender e discutir a prática e os resultados.'], 'registro responsável')
final(12, 'Qual trecho oferece argumento mais consistente sobre saberes docentes?',
      ['Ao ensinar circulação, o professor relaciona conceitos, objetivos e dificuldades observadas, justificando suas escolhas de mediação.', 'Uma aula boa é aquela que utiliza o maior número de materiais.', 'O domínio de nomes de lugares encerra todas as exigências da docência.', 'A experiência longa torna a revisão das decisões dispensável.'], 0,
      ['O trecho explica a articulação em decisões de ensino e a conecta ao processo de aprendizagem.', 'Quantidade de materiais não demonstra sua adequação ao conteúdo e ao objetivo.', 'Nomes podem apoiar o ensino, mas não substituem as outras decisões profissionais.', 'A experiência é revisável; tempo de trabalho não elimina a necessidade de reflexão e formação.'], 'argumentação integrada')
final(12, 'Uma escola quer compreender como uma sequência modifica as explicações geográficas dos estudantes. Qual conjunto é mais adequado ao objetivo?',
      ['Problema delimitado, intervenção descrita, produções analisadas e discussão de limites.', 'Recurso atraente, conclusão antecipada e ausência de registros.', 'Número de participantes, satisfação e promessa de eficácia universal.', 'Lista de conteúdos, foto final e omissão das dificuldades.'], 0,
      ['O conjunto permite examinar aprendizagem, procedimentos e alcance da interpretação.', 'Sem registros e com conclusão antecipada, não se consegue examinar adequadamente a questão.', 'Participação e satisfação informam aspectos da atividade, mas não sustentam garantia universal.', 'Os elementos podem compor um relato, mas a omissão de dificuldades prejudica sua análise.'], 'síntese profissional')


flashcards = [dict(id=f'c{i:02d}', front=front, back=back) for i, (front, back) in enumerate([
    ('Saber disciplinar', 'Conceitos, explicações e formas de investigar o conteúdo de uma área. Em Geografia, envolve ler relações espaciais e examinar fontes.'),
    ('Saber curricular', 'Conhecimentos mobilizados para interpretar objetivos, selecionar e organizar conteúdos e sua progressão no ensino.'),
    ('Saber da experiência docente', 'Aprendizagem profissional construída no exercício da docência e em suas relações de trabalho. Pode ser revista e discutida.'),
    ('Saber da ação pedagógica em Gauthier', 'Saber experiencial tornado público e testado por pesquisas sobre o ensino. Não equivale a qualquer ação em sala.'),
    ('Divulgar uma prática é validá-la?', 'Não automaticamente. A divulgação pode iniciar a troca; a análise de procedimentos, evidências e condições é necessária para seu exame.'),
    ('Tema e objetivo', 'Tema nomeia o assunto. Objetivo explicita uma aprendizagem esperada, como comparar trajetos e explicar uma diferença.'),
    ('Progressão curricular', 'Organização de aprendizagens e relações ao longo do percurso. Não se resume a repetir a tarefa com outro título.'),
    ('Alinhamento no planejamento', 'Objetivo, atividade e avaliação precisam trabalhar a mesma aprendizagem pretendida.'),
    ('Uma foto mostra causas?', 'Pode iniciar perguntas e registrar aspectos visíveis. Explicar processos exige examinar seu alcance e dialogar com outras fontes.'),
    ('Escala 1:10.000 e 1:100.000', '1:10.000 é maior: tem menor redução. Uma explicação acessível deve conservar essa relação.'),
    ('Recurso e saber para ensinar', 'O recurso é o suporte. Saber para ensinar envolve por que escolhê-lo, como mediar e como verificar a aprendizagem.'),
    ('Conhecimento pedagógico do conteúdo', 'Em Shulman, ajuda a discutir representações, explicações e dificuldades próprias do ensino de uma matéria.'),
    ('Tardif: uma entrada de estudo', 'Pluralidade de fontes e desenvolvimento dos saberes ao longo da trajetória, em situações concretas de trabalho.'),
    ('Gauthier: uma entrada de estudo', 'Constituição de conhecimento profissional examinável sobre o ensino, para além da experiência privada.'),
    ('Shulman: uma entrada de estudo', 'Relação entre o conhecimento da matéria e as formas de torná-la ensinável diante das dificuldades da turma.'),
    ('Cavalcanti: cotidiano e conceito', 'A mediação dialoga com conhecimentos cotidianos e científicos para ampliar a compreensão geográfica do vivido.'),
    ('Experiência do aluno e do professor', 'O aluno traz conhecimentos do cotidiano. O professor constrói aprendizagem profissional ao observar, mediar e avaliar. Podem dialogar, sem serem sinônimos.'),
    ('Participação é evidência de domínio conceitual?', 'Informa uma dimensão da atividade. A compreensão conceitual precisa aparecer em tarefas e explicações relacionadas ao objetivo.'),
    ('Feedback formativo', 'Reconhece o que o aluno demonstrou, explica a dificuldade e indica um próximo passo para aprender.'),
    ('Replanejamento', 'Revisão de escolhas de ensino a partir da análise de respostas, dificuldades e condições da turma.'),
    ('O que registrar sobre uma prática?', 'Objetivo, condições, intervenção, produções dos estudantes, critérios de análise e limites da interpretação.'),
    ('Resultado observado e causa', 'Uma melhora não prova sozinha uma causa exclusiva. Outras intervenções e condições podem participar do resultado.'),
    ('Um saber predominante elimina os demais?', 'Não. Predominância destaca o foco do enunciado; uma decisão pode articular vários saberes.'),
    ('Resposta argumentativa sobre docência', 'Explique os conceitos, analise uma decisão concreta e relacione a prática à aprendizagem, reconhecendo limites.')
], 1)]

references = [
    dict(title='Edital PROFGEO-UFPA n. 03/2026 — Anexo III, item 1.2', author='UFPA / PROFGEO', year=2026,
         url='https://www.profgeo.propesp.ufpa.br/', note='Fonte do título e do programa de estudo. PDF enviado pelo estudante; ingresso 2027. O edital não atribui o item a um único autor nem apresenta estas leituras como bibliografia obrigatória.'),
    dict(title='Saberes profissionais dos professores e conhecimentos universitários', author='Maurice Tardif', year=2000,
         url=REFERENCE_PAGE+'#tardif-2000', note='Revista Brasileira de Educação, n. 13. Fonte primária complementar para temporalidade, pluralidade e caráter situado dos saberes profissionais. Síntese em linguagem própria. O link abre a ficha com acesso à fonte.'),
    dict(title='Saberes docentes e formação profissional', author='Maurice Tardif', year=2012,
         url=REFERENCE_PAGE+'#tardif-2012', note='Editora Vozes; edição digital consultada. A primeira edição brasileira é de 2002. Leitura complementar sobre fontes e mobilização dos saberes docentes. O link abre a ficha com acesso à fonte.'),
    dict(title='Por uma teoria da pedagogia: pesquisas contemporâneas sobre o saber docente',
         author='Clermont Gauthier, Stéphane Martineau, Jean-François Desbiens, Annie Malo e Denis Simard', year=2013,
         note='Editora Unijuí, 3ª edição; tradução de Francisco Pereira de Lima. Referência primária complementar, especialmente a discussão do saber da experiência e do saber da ação pedagógica. Não são sinônimos de qualquer atividade em sala. A primeira edição brasileira é de 1998.'),
    dict(title='Those Who Understand: Knowledge Growth in Teaching', author='Lee S. Shulman', year=1986,
         url=REFERENCE_PAGE+'#shulman-1986', note='Educational Researcher, 15(2), p. 4–14. Fonte primária complementar para conhecimento pedagógico do conteúdo. Esse conceito não é apresentado como equivalente à classificação de Gauthier. O link abre a ficha com acesso à fonte.'),
    dict(title='Cotidiano, mediação pedagógica e formação de conceitos: uma contribuição de Vygotsky ao ensino de geografia',
         author='Lana de Souza Cavalcanti', year=2005,
         url='https://www.scielo.br/j/ccedes/a/WnXnVgTRQHZttxBQR44gt9x/?lang=pt', note='Cadernos Cedes. Fonte primária complementar para diálogo entre cotidiano, mediação e formação de conceitos geográficos.'),
    dict(title='Base Nacional Comum Curricular — introdução e Geografia no Ensino Fundamental', author='Ministério da Educação', year=2018,
         url=REFERENCE_PAGE+'#bncc',
         note='Documento oficial usado como exemplo de referência curricular, especialmente a introdução, a relação entre base e currículos e a seção de Geografia no Ensino Fundamental. Documentos e normas serão estudados no item 1.4. O link abre a ficha com acesso à fonte.'),
    dict(title='Fontes, autoria e licença dos recursos visuais da unidade 1.2', author='ProfGeo / Wikimedia Commons', year=2026,
         url='https://github.com/emanoelb5-lgtm/ProfGeo/blob/main/docs/UNIDADE_1_2.md',
         note='Duas fotografias de fontes identificadas; seis esquemas autorais em 16:9. Créditos individuais nos blocos e no pacote. Cenas, dados, falas e situações didáticas fictícias são identificados como autorais. As questões são de treino, não oficiais.')
]

essay = dict(
    title='Oficina de redação · os saberes docentes em uma aula de Geografia',
    prompt='Analise como saberes disciplinares, curriculares, da experiência e da ação pedagógica podem participar de uma prática de ensino de Geografia. Explique pelo menos duas categorias, analise uma decisão de planejamento, mediação ou avaliação e discuta a importância de examinar as evidências e os limites da prática.',
    maxLines=20,
    note='Tema autoral de treino, em até 20 linhas digitadas. Autoavaliação formativa; não é questão oficial, previsão da prova nem correção automática do conteúdo.',
    rubric=[
        'Apresentei uma ideia central que responde ao tema.',
        'Expliquei pelo menos dois saberes, em vez de apenas listar os nomes.',
        'Analisei uma decisão concreta de ensino de Geografia.',
        'Relacionei a intervenção à aprendizagem e às suas evidências.',
        'Se citei ação pedagógica em Gauthier, conservei o sentido de experiência pública e investigada.',
        'Reconheci um limite da prática e escrevi com clareza em até 20 linhas.'
    ],
    model='Ensinar Geografia exige articular conhecimentos de diferentes fontes. O domínio de conceitos é necessário, mas precisa dialogar com objetivos de aprendizagem, experiência profissional e exame das práticas de ensino.\nEm uma aula sobre trajetos até a escola, o saber disciplinar permite relacionar circulação e acesso. Uma perspectiva crítica examina como infraestrutura e decisões sociais participam dessas condições. O saber curricular orienta o objetivo: explicar diferenças entre percursos, em vez de apenas localizar lugares.\nAo observar que a turma confunde distância e tempo, a professora usa sua experiência para rever a intervenção. Ela propõe comparar mapas e dados e pede justificativas, procurando tornar os conceitos instrumentos de análise.\nAs respostas oferecem evidências para avaliar e replanejar. Quando a experiência é explicitada e investigada publicamente, aproxima-se do saber da ação pedagógica discutido por Gauthier. Isso não autoriza uma receita universal, pois outras condições participam dos resultados.\nAssim, a articulação dos saberes sustenta decisões justificadas, abertas à reflexão e voltadas à aprendizagem geográfica.'
)


def balance_options():
    """Distribui posições corretas sem separar alternativas dos comentários."""
    i = 0
    for question in questions:
        if len(question['options']) != 4:
            continue
        target = [2, 0, 3, 1][i % 4]
        shift = (target - question['answer']) % 4
        items = list(zip(question['options'], question['feedback']))
        items = items[-shift:] + items[:-shift] if shift else items
        question['options'] = [x[0] for x in items]
        question['feedback'] = [x[1] for x in items]
        question['answer'] = target
        i += 1


def save():
    assert len(lessons) == 12
    assert len(questions) == 60
    assert sum(q['pool'] == 'final' for q in questions) == 20
    u = dict(schemaVersion=1, id='1.2', moduleId='1', revision=1, title=TITLE,
             shortTitle='Os saberes que sustentam o ensinar',
             subtitle='Reconheça os conhecimentos do professor nas decisões de uma aula de Geografia.',
             editalItem='1.2', estimatedMinutes=sum(l['minutes'] for l in lessons),
             objectives=[
                 'Distinguir os saberes disciplinares, curriculares, da experiência e da ação pedagógica.',
                 'Comparar os focos de Tardif, Gauthier e Shulman sem igualar suas classificações.',
                 'Analisar decisões de planejamento, mediação e avaliação em aulas de Geografia.',
                 'Relacionar saberes docentes e saberes dos estudantes em situações de ensino.',
                 'Argumentar com exemplos e evidências sobre a construção do conhecimento profissional.'
             ], lessons=lessons, questions=questions, flashcards=flashcards, references=references, essay=essay)
    (ROOT/'content/units/1.2.json').write_text(json.dumps(u, ensure_ascii=False, indent=2)+'\n')
    catalog_path = ROOT/'content/catalog.json'
    catalog = json.loads(catalog_path.read_text())
    entry = next(e for m in catalog['modules'] for e in m['units'] if e['id']=='1.2')
    entry.update(status='published', revision=1)
    catalog['revision'] = max(2, catalog['revision'])
    catalog['updatedAt'] = '2026-10-12'
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2)+'\n')
    print(f'Unidade 1.2: {len(lessons)} lições, {len(questions)} questões, {len(flashcards)} cartões.')


if __name__ == '__main__':
    balance_options()
    save()
