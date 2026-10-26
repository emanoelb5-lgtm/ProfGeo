"""Revisão didática 2 da unidade 1.2, compatível com o APK 1.1.1.

O pacote r1 é o registro imutável dos problemas já respondidos. Questões
anteriores conservam o sentido e os IDs; o novo simulado tem IDs próprios.
"""
import copy
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with zipfile.ZipFile(ROOT/'content/packages/1.2-r1.zip') as archive:
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


def picture(filename, title, caption):
    old = next(b for l in ORIGINAL['lessons'] for b in l['blocks']
               if b.get('src') == 'media/'+filename)
    return dict(type='photo', src=old['src'], title=title, caption=caption, credit=old['credit'])


def match(title, pairs):
    return dict(type='match', title=title, pairs=pairs)


def order(title, items):
    return dict(type='order', title=title, items=items)


lessons = []


def lesson(n, title, kicker, minutes, blocks, summary, practice):
    lessons.append(dict(id=f'l{n:02d}', title=title, kicker=kicker, minutes=minutes,
                        blocks=blocks, summary=summary, practice=practice))


lesson(1, 'Ensinar exige mais de um saber', 'Acompanhe uma professora tomando decisões', 17, [
    text('Da unidade 1.1 para esta unidade', 'Na 1.1, você estudou como diferentes concepções ajudam a explicar o espaço e orientar seu ensino. Agora vamos mudar a pergunta: que conhecimentos a professora mobiliza para transformar uma explicação geográfica em aprendizagem? O objetivo é analisar decisões docentes, em vez de decorar quatro nomes separados.\nVamos acompanhar Lia, uma professora fictícia de Geografia. Ela prepara uma aula sobre acesso à escola no período chuvoso. A turma sabe localizar a escola, mas afirma que o caminho mais curto é necessariamente o mais rápido. Esse é o problema de aprendizagem que vai ligar as lições. As falas, os dados e os episódios de Lia são inventados para estudo; não descrevem uma pesquisa realizada em uma escola.'),
    text('O que Lia precisa resolver?', 'Primeiro, Lia verifica se distância, tempo de deslocamento e acesso significam a mesma coisa. Depois, pergunta o que pretende que a turma aprenda: localizar trajetos ou explicar diferenças entre eles? Lembra que, em outra aula, os estudantes olharam o desenho do mapa sem consultar a tabela. Precisa escolher uma intervenção e descobrir se ela ajudou.\nCada decisão exige conhecimento. Chamar esse conjunto de saberes docentes permite reconhecer que ensinar envolve compreender, interpretar, julgar e agir em condições concretas. Ter domínio da Geografia é necessário, mas não responde sozinho como organizar a aprendizagem de uma turma.'),
    table('Dê nome depois de compreender a decisão', ['Decisão de Lia', 'Saber em destaque e por quê'], [
        ['Distinguir distância, tempo e condições de circulação.', 'Disciplinar: compreender conceitos e relações da Geografia.'],
        ['Situar a comparação de trajetos no percurso de aprendizagem.', 'Curricular: interpretar objetivos, conteúdos e sua organização escolar.'],
        ['Rever a intervenção com base em uma dificuldade observada no trabalho.', 'Da experiência: aprendizagem profissional construída na docência.'],
        ['Examinar resultados de práticas explicitadas e testadas por pesquisas sobre o ensino.', 'Da ação pedagógica, na acepção de Gauthier: conhecimento da experiência submetido a exame público.']]),
    text('Por que não são quatro gavetas?', 'Ao escolher a comparação de dois trajetos, Lia mobiliza conteúdo, objetivo e experiência ao mesmo tempo. A classificação destaca uma dimensão da decisão; não divide a professora em quatro partes. Em uma questão, procure o aspecto que o enunciado pede para analisar e justifique essa predominância.\nObserve também a última linha da tabela: qualquer aula tem ações pedagógicas no sentido comum da expressão. O saber da ação pedagógica, em Gauthier, tem um sentido específico, que será explicado na lição 5. Não basta dar uma aula para demonstrar que esse conhecimento foi produzido.'),
    picture('u12-quatro-saberes.png', 'Retome as quatro perguntas', 'Use o esquema depois do caso: o que compreender, o que selecionar, o que aprender no trabalho e o que submeter ao exame público? Os focos se articulam; a figura não esgota as classificações dos autores.'),
    picture('u12-sala-aula.jpg', 'O que uma fotografia permite concluir?', 'Esta é uma sala da Escola Técnica de Paulínia, em fotografia de 2015, com conteúdo de História na lousa. Ela situa uma cena escolar, mas não mostra o planejamento nem prova o que os estudantes aprenderam. Não é a turma fictícia de Lia.'),
    compare('Primeiro caso resolvido', 'Enunciado', '“Lia consulta a sequência de aprendizagens antes de decidir o que retomar.” O destaque é a relação entre sua decisão e o percurso escolar.', 'Raciocínio da resposta', 'O foco é curricular: a professora interpreta a organização da aprendizagem. Ela pode usar experiência e conhecimento geográfico nessa decisão; o destaque curricular não apaga os demais saberes.'),
    call('Pare e explique', 'Sem olhar a tabela, explique por que “saber Geografia” e “saber ensinar Geografia” se relacionam, mas não se resumem à mesma exigência. Uma resposta possível: o conteúdo precisa ser compreendido, selecionado, representado e avaliado para uma turma concreta.'),
    text('Como seguir', 'Nas lições 2 a 5, vamos acompanhar cada decisão de Lia com mais calma. A lição 6 compara autores. Da 7 à 11, construiremos explicação, planejamento, mediação, avaliação e investigação. A última lição mostrará como transformar essa análise em resposta de prova e argumento escrito.')
], 'Os saberes docentes ajudam a explicar decisões profissionais. Uma aula articula conhecimentos de fontes diferentes; identificar o foco de uma decisão exige mostrar sua função no caso.', match('Associe a decisão ao foco principal', [
    ['Compreender a diferença entre distância e tempo de viagem.', 'Saber disciplinar'],
    ['Situar a aprendizagem na sequência prevista para a turma.', 'Saber curricular'],
    ['Rever uma escolha a partir de dificuldades observadas no trabalho.', 'Saber da experiência'],
    ['Examinar a experiência explicitada e testada por pesquisas sobre o ensino.', 'Saber da ação pedagógica em Gauthier']]))

lesson(2, 'Saber disciplinar: compreender para explicar', 'O que a Geografia permite afirmar?', 19, [
    text('Antes de ensinar, Lia verifica a própria explicação', 'Retome a frase da turma: “o mais perto é sempre o mais rápido”. Para enfrentá-la, Lia precisa compreender o conteúdo. Distância mede a extensão de um percurso; tempo indica sua duração. Acessibilidade diz respeito às condições de alcançar lugares, serviços e oportunidades. As três ideias podem se relacionar, mas não são intercambiáveis.\nEsse é um exemplo de saber disciplinar: conhecimentos produzidos nos campos científicos e incorporados à formação e ao trabalho docente. Em Geografia, não se limita a nomes de rios ou capitais. Inclui conceitos, explicações e critérios para investigar relações espaciais.'),
    text('Uma explicação que conserva as relações', 'Uma escola a cinco quilômetros pode ser de acesso difícil se a via estiver interrompida ou faltar transporte. Outra, mais distante, pode ser alcançada em menos tempo por uma conexão regular. Os dados necessários dependem da pergunta: localizar exige informações diferentes de explicar condições de acesso.\nLia não pode concluir que uma estrada será sempre mais rápida que um rio. Modalidade, condições do percurso, espera, custo e momento da observação precisam ser considerados. O conhecimento disciplinar permite formular perguntas e reconhecer os limites de uma generalização.'),
    picture('u12-rio-guama.jpg', 'Do rio observado ao problema de circulação', 'Rio Guamá visto do campus da UFPA, em setembro de 2019. A fotografia registra aspectos visíveis desse momento. Para analisar a circulação, Lia precisaria consultar trajetos, condições e outras fontes. A imagem não comprova tempos de viagem.'),
    table('Resolva a pergunta antes de escolher a fonte', ['Pergunta', 'O que procurar', 'Limite a reconhecer'], [
        ['Onde estão a escola e as comunidades?', 'Mapa com localização, orientação, legenda e fonte.', 'Localizar os pontos não explica o tempo de viagem.'],
        ['Qual percurso é mais demorado?', 'Registros de duração e condições das viagens.', 'Um registro não garante o mesmo resultado em todo período.'],
        ['Por que os acessos são diferentes?', 'Relações entre trajetos, transportes, infraestrutura e organização social.', 'A causa não pode ser deduzida apenas da aparência de uma foto.']]),
    compare('Exemplo resolvido: mapa de pontos', 'Resposta precipitada', '“Há duas escolas no mapa, portanto o acesso é igual.” A quantidade de pontos é uma informação de localização, insuficiente para essa conclusão.', 'Resposta fundamentada', '“O mapa localiza escolas; precisamos comparar condições de deslocamento, distribuição dos serviços e informações sobre os usuários para discutir o acesso.” A fonte é usada dentro do seu alcance.'),
    text('E quando a dificuldade é cartográfica?', 'Lia também precisa conservar a precisão quando ensina escala: 1:10.000 é uma escala maior que 1:100.000, porque reduz menos a realidade. Um centímetro corresponde, respectivamente, a 100 metros e a um quilômetro. Compare as frações antes de associar o maior denominador à maior escala.\nEntender essa relação é uma exigência de conteúdo. Escolher como explicá-la à turma envolve outro trabalho, que aprofundaremos com Shulman na lição 7. A clareza da linguagem não autoriza inverter o significado do conceito.'),
    call('Do caso ao saber', 'Por que o foco aqui é disciplinar? Porque examinamos a validade da explicação geográfica e das fontes. Se a pergunta fosse por que Lia escolheu essa aprendizagem para aquele momento escolar, o foco passaria à organização curricular.'),
    text('Transfira antes da prática', 'Pense em uma feira: localizar o ponto de venda explica sozinho quem consegue abastecê-la? Não. É necessário examinar conexões, trajetos e condições de circulação. Você aplicou a mesma distinção entre localizar e explicar em outro contexto. Na próxima lição, Lia vai selecionar quais dessas relações ensinar primeiro.')
], 'Saber disciplinar permite compreender conceitos, formular perguntas e examinar o alcance das fontes. Uma explicação acessível precisa preservar a validade das relações geográficas.', match('Relacione pergunta e informação necessária', [
    ['Localizar a escola.', 'Posição representada e orientação no mapa.'],
    ['Comparar a duração de dois trajetos.', 'Registros de tempo e condições de deslocamento.'],
    ['Explicar diferenças de acesso.', 'Relações entre circulação, infraestrutura e organização espacial.'],
    ['Comparar escalas cartográficas.', 'Relação de redução entre representação e realidade.']]))

lesson(3, 'Saber curricular: construir um percurso', 'O que aprender, em que sequência e para quê?', 20, [
    text('Lia domina o assunto; ainda precisa escolher', 'A Geografia oferece muitas possibilidades para estudar os trajetos: rede, circulação, paisagem, lugar, desigualdade de acesso. Não cabe trabalhar tudo com a mesma profundidade em uma aula. Lia consulta as orientações e a proposta curricular da escola, considera o percurso da turma e seleciona uma aprendizagem.\nSaber curricular é o conhecimento mobilizado para interpretar e trabalhar a seleção e a organização escolar de objetivos, conteúdos e métodos. Não é apenas lembrar o nome de um documento. Envolve compreender o que a escola escolhe ensinar, com que finalidades e como as aprendizagens se encadeiam.'),
    compare('Separe três decisões', 'Tema e recurso', '“Trajetos até a escola” é o assunto. “Usar um mapa” é uma escolha de suporte. Nenhum dos dois informa, sozinho, o que o aluno deverá aprender.', 'Objetivo de aprendizagem', '“Comparar dois trajetos e explicar por que a menor distância não garante o menor tempo.” Indica uma operação e uma relação que podem aparecer na produção do aluno.'),
    text('Construa a progressão com a turma', 'Para explicar diferenças, os alunos precisam identificar os percursos e ler suas informações. Lia começa verificando a leitura de legenda e a distinção entre quilômetros e minutos. Depois propõe a comparação e, por fim, a justificativa. Essa sequência é uma decisão do caso, não uma ordem universal para toda aula.\nProgressão é ampliar e reorganizar relações ao longo do percurso. Repetir o mesmo mapa com outro título não garante avanço. Também não basta passar a um assunto mais difícil se a turma ainda não dispõe dos conhecimentos necessários para enfrentá-lo.'),
    picture('u12-caminho-curricular.png', 'Acompanhe a escolha até sua verificação', 'A orientação curricular ajuda a definir um objetivo, que orienta a situação de ensino e a busca de evidências. O esquema resume o raciocínio; as decisões também precisam considerar a turma e as condições de trabalho.'),
    table('Planejamento resolvido, em três partes', ['Decisão', 'Exemplo de Lia', 'Por que se relacionam?'], [
        ['Objetivo', 'Explicar a diferença entre distância e tempo nos trajetos.', 'Define o que a turma deverá compreender.'],
        ['Atividade', 'Comparar mapa e tabela, discutir hipóteses e justificar a escolha.', 'Dá oportunidade para construir a relação pretendida.'],
        ['Avaliação', 'Justificar a resposta em outro par de trajetos.', 'Examina se a relação foi usada além do exemplo inicial.']]),
    text('O que mudaria se a avaliação cobrasse só nomes?', 'Imagine que Lia ensine a comparar trajetos, mas avalie apenas o nome das vias. O resultado pode informar memória de nomes; não responde se a turma aprendeu a explicar a diferença. Alinhamento significa que objetivo, atividade e avaliação trabalham a mesma aprendizagem, mesmo com tarefas diferentes.\nUm objetivo pode exigir localização, e reconhecer um nome pode ser pertinente. O problema do exemplo é a distância entre a exigência de explicar e o que foi efetivamente verificado. Julgue a tarefa em relação à finalidade, não como boa ou ruim em qualquer situação.'),
    text('Uma referência não é um plano pronto', 'A BNCC de 2018, aqui usada no recorte da introdução e da Geografia do Ensino Fundamental, é uma referência para aprendizagens; sua leitura não entrega automaticamente a aula de Lia. A proposta curricular, o contexto escolar e o planejamento dão forma concreta às escolhas. Documentos e normas serão aprofundados na unidade 1.4.\nSelecionar conteúdos também envolve finalidades e escolhas sociais. Trazer uma situação local pode ampliar a compreensão, desde que não reduza a aula a curiosidades do bairro nem elimine relações com outras escalas.'),
    call('Agora é sua vez, com resolução', '“Vou apresentar dez mapas sobre transportes.” Como transformar isso em objetivo? Uma possibilidade: “comparar a distribuição das conexões e explicar uma diferença de acesso usando os mapas”. A mudança explicita a aprendizagem; a quantidade de mapas deixa de ser seu único critério.')
], 'Saber curricular envolve interpretar a seleção e a organização escolar do conhecimento. Objetivo, sequência, atividade e avaliação precisam permitir construir e examinar a aprendizagem escolhida.', order('Organize o planejamento do caso', [
    'Interpretar o percurso curricular e verificar o que a turma já consegue fazer.',
    'Definir a relação geográfica que se espera que os alunos expliquem.',
    'Planejar uma comparação orientada com informações adequadas.',
    'Examinar a aprendizagem em uma justificativa sobre outro caso.' ]))

lesson(4, 'Saber da experiência: aprender no trabalho', 'Como uma dificuldade vira conhecimento profissional?', 19, [
    text('A aula não segue exatamente como Lia esperava', 'Lia mostra mapa e tabela. Vários alunos respondem olhando apenas o traçado: “esse é mais rápido porque parece menor”. Ela se lembra de uma dificuldade semelhante em outra turma e decide pedir que apontem primeiro a unidade de cada coluna. Depois acompanha se as justificativas mudam.\nO saber da experiência docente se constrói no trabalho, nas relações com os alunos, com colegas e com as condições escolares. A professora aprende a perceber dificuldades, interpretar situações e ajustar decisões. Não é uma coleção de lembranças sem relação com o que precisa fazer.'),
    compare('A lembrança e sua interpretação', 'Registro que pouco explica', '“A tabela não deu certo.” Não informa o objetivo, o obstáculo observado ou o que Lia fez para enfrentá-lo.', 'Registro que ajuda a aprender', '“A turma escolheu pelo desenho sem distinguir km e min. Pedi a comparação das unidades e depois recolhi justificativas individuais.” Explicita dificuldade, intervenção e modo de acompanhar.'),
    text('Por que tempo de serviço não é uma garantia?', 'Os anos de trabalho oferecem experiências, mas seu valor depende também de como são interpretadas. Repetir uma decisão pode conservar um erro; discutir respostas e rever critérios pode ampliar o conhecimento profissional. Uma professora iniciante também constrói saberes no encontro entre formação, prática e colaboração.\nNa análise de Tardif, os saberes são constituídos ao longo de trajetórias e em situações de trabalho. Isso permite perguntar como Lia chegou a reconhecer aquele obstáculo, em vez de imaginar que o domínio profissional surgiu inteiro no diploma ou apenas da intuição.'),
    picture('u12-experiencia-reflexao.png', 'Siga a passagem da observação à revisão', 'O esquema ajuda a retomar o episódio: observar uma dificuldade, interpretar, ajustar e acompanhar. Esse caminho explicita uma aprendizagem profissional; não garante por si só a validade de qualquer conclusão.'),
    table('Um pequeno diário de Lia', ['Registro', 'Função no raciocínio'], [
        ['Objetivo: explicar a diferença entre distância e tempo.', 'Permite avaliar se o obstáculo é relevante para a aprendizagem escolhida.'],
        ['Resposta observada: escolher pelo desenho sem ler a duração.', 'Localiza a dificuldade; não rotula a capacidade do estudante.'],
        ['Intervenção: comparar unidades e confrontar os dois dados.', 'Torna a decisão docente compreensível.'],
        ['Depois: pedir explicação em um novo exemplo.', 'Ajuda a verificar o alcance da mudança.']]),
    text('A experiência pode ser compartilhada', 'Ao conversar com uma colega, Lia descobre outra maneira de organizar os dados. A aprendizagem experiencial pode se desenvolver individual e coletivamente. Ela não exige que o professor trabalhe isolado nem dispensa estudo e diálogo com outros conhecimentos.\nÉ importante distinguir duas coisas: o estudante que relata sua viagem traz conhecimentos do cotidiano; a professora que aprende a interpretar dificuldades constrói aprendizagem profissional. Elas podem se encontrar na aula, mas a experiência de vida do aluno não é automaticamente o saber experiencial docente.'),
    call('Caso resolvido', '“Aprendi que preciso trabalhar a legenda antes dessa comparação.” O que permite reconhecer saber da experiência? A relação entre uma situação vivida no trabalho e uma decisão profissional aprendida. A frase ainda precisa de evidências e condições para sustentar uma recomendação a outras turmas.'),
    text('A pergunta que leva à lição 5', 'Lia afirma: “Na minha turma, essa intervenção ajudou”. Outro professor pergunta: como foi aplicada, que mudança ocorreu e em que condições? Agora o problema é como submeter a experiência a um exame que outros possam discutir. Essa passagem ajuda a entender Gauthier.')
], 'Saber da experiência é aprendizagem profissional construída no trabalho e em suas relações. Interpretar dificuldades e acompanhar decisões permite revisar a prática; repetir uma rotina não comprova sua adequação.', match('Relacione o episódio à sua função', [
    ['Um aluno descreve o caminho que percorre.', 'Conhecimento cotidiano do estudante.'],
    ['Lia aprende a reconhecer a confusão entre quilômetros e minutos.', 'Aprendizagem profissional da professora.'],
    ['Duas docentes analisam juntas as respostas da turma.', 'Reflexão profissional compartilhada.'],
    ['A mesma atividade é repetida sem examinar seus resultados.', 'Rotina que ainda precisa ser interrogada.']]))

lesson(5, 'Ação pedagógica: tornar a experiência examinável', 'Por que divulgar não basta, em Gauthier?', 20, [
    text('Retome a pergunta do colega de Lia', 'Lia percebeu uma melhora e contou à equipe. Seu relato pode ser valioso para a troca profissional. Mas um colega que queira examinar a afirmação precisa conhecer o problema, a intervenção e as respostas analisadas. Uma conclusão que fica apenas no julgamento de quem viveu a aula é difícil de discutir.\nNa acepção de Gauthier e colaboradores, o saber da ação pedagógica é o saber experiencial tornado público e testado por pesquisas sobre o ensino. A expressão designa uma forma de constituir conhecimento profissional examinável, não simplesmente o fato de o professor agir em sala.'),
    compare('O que muda entre os dois registros?', 'Divulgação de uma atividade', '“Fiz uma comparação de trajetos e todos gostaram.” Informa uma percepção e pode iniciar o diálogo. Não mostra o que os alunos aprenderam nem como a conclusão foi construída.', 'Experiência submetida à investigação', 'Explicitar a pergunta, as condições, a sequência, as produções analisadas e os critérios permite que outras pessoas examinem o argumento. Os resultados e seus limites também são comunicados.'),
    text('A diferença está na possibilidade de examinar', 'No caso fictício, Lia e a equipe decidem estudar como a comparação de mapa e tabela participa das explicações sobre acesso. Recolhem produções antes e depois, definem critérios e procuram também respostas que contrariem a expectativa. Depois, discutem o procedimento e a interpretação com outros docentes e pesquisadores.\nPublicar uma foto, receber elogios ou ter muitas visualizações não substitui esse exame. Uma publicação acadêmica também não dispensa olhar seus procedimentos e evidências: o nome do veículo não demonstra, sozinho, a força de uma conclusão.'),
    picture('u12-acao-pedagogica.png', 'A experiência passa a poder ser interrogada', 'A figura resume a distinção estudada: experiência, explicitação, investigação e exame público. Ela não transforma a investigação em uma receita única nem estabelece que qualquer relato já foi validado.'),
    table('O que outro professor precisa conseguir perguntar?', ['Dimensão', 'Pergunta aplicada ao caso'], [
        ['Problema', 'Que dificuldade de explicar os trajetos foi investigada?'],
        ['Procedimento', 'O que foi proposto e em que condições de turma, tempo e recursos?'],
        ['Evidências e critérios', 'Quais respostas sustentam a interpretação e como foram analisadas?'],
        ['Discussão e limites', 'O que não mudou e que outras condições podem ter participado?']]),
    text('Por que isso importa para a profissão?', 'Se cada professor conservar suas melhores decisões apenas como certezas pessoais, parte desse conhecimento ficará pouco acessível aos colegas e à formação de novos docentes. Gauthier destaca a construção de um repertório de conhecimentos sobre ensinar que possa ser explicitado e discutido.\nIsso não torna a experiência cotidiana inútil. Ela oferece problemas e aprendizados importantes. A distinção indica que a justificativa pública exige mais do que “comigo funciona”. Também não exige transformar toda aula em pesquisa formal: aqui estamos compreendendo o estatuto de um saber, não impondo uma obrigação a cada atividade.'),
    call('Resolva a afirmação', '“Como a atividade foi aplicada em três turmas, tornou-se uma técnica que funciona em qualquer escola.” O salto é indevido. A ampliação do estudo pode fortalecer a discussão, mas condições, critérios e limites continuam necessários. Testar uma prática não produz uma garantia universal.'),
    text('Ponte para os autores', 'A mesma aula permite investigar de onde Lia aprendeu suas decisões, como tornou um conceito compreensível e como a prática foi examinada. Essas perguntas se relacionam, mas destacam problemas diferentes. Na próxima lição, vamos situá-las em Tardif, Shulman e Gauthier.')
], 'Em Gauthier, o saber da ação pedagógica envolve experiência explicitada, tornada pública e testada por pesquisas sobre o ensino. Troca de relatos pode contribuir, mas divulgação e aprovação não substituem investigação.', order('Reconstrua a investigação do caso', [
    'Delimitar uma dificuldade concreta de aprendizagem.',
    'Explicitar condições, intervenção e critérios de análise.',
    'Examinar produções e confrontar a interpretação com os resultados.',
    'Comunicar procedimentos, evidências e limites para discussão pública.' ]))

lesson(6, 'Tardif, Gauthier e Shulman: perguntas diferentes', 'Compare os autores a partir da aula', 23, [
    text('Primeiro a pergunta, depois o nome', 'Você já conhece três problemas. Como Lia construiu seus conhecimentos ao longo da trajetória? Como escolheu uma representação para enfrentar uma dificuldade específica? Como a experiência pode fundamentar conhecimento público sobre o ensino? Agora é possível aproximar os autores desses problemas sem decorar uma tabela vazia.\nO item 1.2 do edital não atribui sua lista a um único pesquisador. As referências desta unidade são leituras complementares selecionadas para explicar os saberes docentes. As classificações dialogam, mas seus termos não devem ser tratados como traduções automáticas.'),
    text('Tardif: fontes, trajetória e situação de trabalho', 'Na leitura de Tardif, o saber docente é plural: a formação profissional, as disciplinas, os currículos e a experiência contribuem para sua constituição. Saber da formação profissional inclui contribuições das ciências da educação e das ideias pedagógicas estudadas na formação. Esse conjunto não se reduz ao conhecimento específico da Geografia.\nNo caso, Lia articula estudos da licenciatura, conceitos geográficos, orientações curriculares e aprendizagens no trabalho. A pergunta é como ela mobiliza essas fontes na situação concreta, e não qual delas elimina todas as outras.'),
    table('Termos de Tardif com um exemplo', ['Característica', 'Sentido no caso de Lia'], [
        ['Temporais', 'Os saberes se constituem ao longo da história escolar, da formação e da carreira; não vêm prontos em um único momento.'],
        ['Plurais e heterogêneos', 'Formação, conteúdo, currículo e experiência têm fontes e funções diferentes na decisão.'],
        ['Personalizados e situados', 'O conhecimento se mobiliza por uma professora concreta, com uma turma e condições de trabalho. Isso não torna qualquer opinião verdadeira.'],
        ['Trabalho com seres humanos', 'As decisões envolvem estudantes com trajetórias e respostas diversas, não objetos idênticos a controlar.']]),
    text('Gauthier: um ofício sustentado por saberes', 'Gauthier e colaboradores discutem um reservatório de saberes: disciplinares, curriculares, das ciências da educação, da tradição pedagógica, experienciais e da ação pedagógica. Portanto, os quatro focos do título desta unidade não esgotam sua proposta. Tradição pedagógica envolve maneiras de imaginar e organizar o ensino, inclusive concepções herdadas da própria vida escolar, que precisam ser interrogadas.\nA contribuição estudada aqui destaca a passagem de julgamentos experienciais para conhecimento público e testado sobre ensinar. Saber da ação pedagógica não equivale a todos os saberes pedagógicos, nem a toda estratégia usada pelo professor.'),
    text('Shulman: compreender o conteúdo para fazê-lo compreensível', 'Na contribuição de Shulman, o conhecimento pedagógico do conteúdo inclui modos de representar e explicar assuntos e de lidar com dificuldades e concepções dos alunos. Ao escolher mapa e tabela para enfrentar a confusão entre distância e tempo, Lia precisa saber por que essa combinação pode ajudar.\nEsse foco não é idêntico ao de Gauthier. Uma professora pode elaborar uma explicação pertinente sem demonstrar, por esse fato, que a intervenção foi submetida a pesquisa pública. Conhecer para ensinar um conteúdo e investigar publicamente uma prática são questões relacionadas, com exigências diferentes.'),
    table('Uma aula, três entradas de análise', ['Pergunta do enunciado', 'Contribuição que ajuda a responder'], [
        ['De onde vêm os saberes de Lia e como se transformam no trabalho?', 'Tardif: pluralidade de fontes, trajetória e caráter situado.'],
        ['Como explicitar e testar a experiência para constituir conhecimento sobre ensinar?', 'Gauthier: repertório profissional e saber da ação pedagógica.'],
        ['Como representar distância e tempo diante da dificuldade da turma?', 'Shulman: conhecimento pedagógico do conteúdo.']]),
    compare('Caso de prova resolvido', 'Destaque 1', '“Lia usa uma tabela porque conhece a dificuldade de confundir quilômetros e minutos.” O problema é como ensinar aquele conteúdo: o foco se aproxima de Shulman.', 'Destaque 2', '“O grupo publica procedimentos e evidências de uma investigação dessa intervenção.” O problema é o exame público da experiência: o foco se aproxima de Gauthier.'),
    call('Explique a aproximação sem apagar a diferença', 'Os três autores contribuem para reconhecer a complexidade do conhecimento docente. Esse ponto de encontro não permite afirmar que usaram a mesma classificação. Em uma resposta, diga qual pergunta está sendo enfrentada e qual contribuição ajuda a analisá-la.'),
    text('Retome o percurso', 'Agora vamos voltar à aula de Lia. Nas próximas lições, você verá o conhecimento profissional em funcionamento: explicar, planejar, dialogar e avaliar. Use as referências para interpretar essas decisões, em vez de procurar o nome de um autor em cada objeto da sala.')
], 'Tardif ajuda a analisar fontes e constituição situada dos saberes; Gauthier, o repertório profissional e o exame público da experiência; Shulman, as formas de tornar um conteúdo compreensível. Há diálogo, sem equivalência automática.', match('Associe a pergunta à entrada de análise', [
    ['Como formação, currículo e experiência se combinam na trajetória?', 'Pluralidade e constituição dos saberes em Tardif.'],
    ['Como a experiência é explicitada e testada publicamente?', 'Saber da ação pedagógica em Gauthier.'],
    ['Como enfrentar uma dificuldade própria de um conteúdo?', 'Conhecimento pedagógico do conteúdo em Shulman.'],
    ['Os três autores propõem a mesma lista de saberes?', 'As contribuições dialogam, mas não têm classificação idêntica.']]))

lesson(7, 'Do conceito à explicação que ensina', 'Mostre como o aluno pode reconstruir a relação', 21, [
    text('O problema da turma fica visível', 'Lia dispõe de dois trajetos hipotéticos: A tem oito quilômetros e duração de 45 minutos; B tem 15 quilômetros e duração de 25 minutos. Um estudante escolhe A como o mais rápido, porque oito é menor que 15. Ele comparou corretamente as distâncias, mas usou essa comparação para responder sobre o tempo.\nEsse diagnóstico é mais útil que dizer “ele não entendeu nada”. Mostra o que já consegue fazer e a relação que ainda precisa construir. Para ensinar o conteúdo, Lia precisa interpretar a resposta e escolher uma representação que exponha a diferença entre as grandezas.'),
    call('Preveja antes da animação', 'Qual trajeto você escolheria se a pergunta fosse menor distância? E se fosse menor duração? Formule as duas respostas antes de usar os controles. Não tente explicar a diferença de tempo apenas com os números: eles mostram o resultado, mas não identificam sozinhos sua causa.'),
    anim('quantitative', 'Distância e tempo precisam de critérios diferentes', 'Compare as rotas A e B pelos controles. A tem 8 km e 45 min; B tem 15 km e 25 min. São dados didáticos hipotéticos. Observe o resultado e depois explique por que responder “mais rápido” exige consultar a duração.'),
    text('Resolução passo a passo', 'Primeiro, leia o que foi perguntado. Para menor distância, compare quilômetros: A é menor. Para menor duração, compare minutos: B é mais rápida nas condições informadas. Depois, relacione os resultados: neste caso, a menor distância não corresponde ao menor tempo.\nPor fim, delimite a conclusão. Os dados permitem comparar os percursos apresentados. Para explicar por que um é mais rápido, precisaríamos de informações sobre transporte, espera, condições e velocidade ao longo da viagem. Inventar essas causas como se estivessem na tabela enfraqueceria o argumento.'),
    table('A intervenção de Lia tem um motivo', ['Dificuldade observada', 'Escolha para ensinar', 'O que procurar depois'], [
        ['Comparar números sem observar as unidades.', 'Destacar km e min e pedir uma resposta para cada pergunta.', 'O aluno distingue distância e duração.'],
        ['Supor que o menor percurso é necessariamente o mais rápido.', 'Confrontar os resultados e pedir que explique a diferença.', 'O aluno revê a relação automática entre as grandezas.'],
        ['Repetir a resposta B sem justificar.', 'Apresentar outro par de trajetos e pedir um argumento.', 'O aluno usa a relação em uma situação nova.']]),
    text('Agora reconheça o conhecimento pedagógico do conteúdo', 'Lia não escolheu a animação apenas porque se move. Relacionou uma dificuldade específica, uma forma de representar o assunto e uma pergunta que obriga a comparar critérios. Essa articulação ajuda a compreender o conhecimento pedagógico do conteúdo em Shulman.\nUma técnica geral, como organizar grupos, pode contribuir para a aula. Mas o foco aqui é por que determinada explicação ou representação ajuda a aprender este conteúdo. Outro professor poderia usar papel e lápis e mobilizar o mesmo cuidado, se mantivesse a comparação e a orientação.'),
    compare('Transferência resolvida', 'Novo par hipotético', 'C tem 10 km e 20 min; D tem 6 km e 35 min. Um aluno diz: “D é mais curta, mas C tem menor duração”.', 'O que essa resposta mostra?', 'Ele distingue as duas grandezas em outro exemplo. Para avançar, Lia pode pedir que explique por que distância não basta para analisar acesso e que informações adicionais seriam necessárias.'),
    text('Simplificar sem distorcer', 'Volte à escala cartográfica da lição 2. Lia pode usar a mesma área representada em duas escalas para tornar visível a redução. Precisa verificar se os alunos compreendem a relação, em vez de ensinar que “número maior significa escala maior”. Uma simplificação adequada preserva o conceito e oferece uma entrada compreensível.\nNa próxima lição, esse cuidado será integrado ao planejamento. A representação é escolhida em função de uma aprendizagem e de uma dificuldade, e não como etapa decorativa.' )
], 'Ensinar um conteúdo envolve reconhecer dificuldades, escolher representações e orientar relações. O conhecimento pedagógico do conteúdo ajuda a justificar essas escolhas; a resposta em um novo caso permite examinar a aprendizagem.', order('Reconstrua a resolução do caso', [
    'Ler se a pergunta pede menor distância ou menor duração.',
    'Comparar a grandeza e a unidade correspondentes.',
    'Relacionar os resultados sem inventar causas ausentes dos dados.',
    'Aplicar a distinção em outro par de trajetos e justificar.' ]))

lesson(8, 'Planejar articulando os saberes', 'Da intenção à sequência de ensino', 20, [
    text('Agora Lia precisa organizar a aula inteira', 'Já sabemos o conteúdo, a aprendizagem escolhida e uma dificuldade da turma. Lia planeja uma sequência sobre acesso à escola na chuva. Seu objetivo é que os estudantes expliquem diferenças de acesso relacionando trajetos, tempo e condições de circulação. Ela não pretende apenas trocar a ideia “sempre mais curto” pela memorização de “a resposta é B”.\nOs dados e o caso são fictícios. Em uma aula real, informações locais precisariam ser obtidas e verificadas, respeitando as condições de deslocamento e participação dos estudantes. A sequência abaixo é uma proposta analisada, não uma receita obrigatória.'),
    table('Observe o que cada momento faz pela aprendizagem', ['Momento', 'Decisão de Lia', 'Função'], [
        ['Ponto de partida', 'Pedir uma hipótese e uma justificativa sobre os trajetos.', 'Conhecer o raciocínio inicial, sem adivinhar a dificuldade.'],
        ['Comparação orientada', 'Oferecer mapa e tabela, distinguir unidades e confrontar respostas.', 'Dar condições para construir a relação pretendida.'],
        ['Sistematização', 'Explicar circulação e acesso com base nas comparações.', 'Organizar o que foi aprendido em conceitos.'],
        ['Nova situação', 'Propor outro caso e recolher explicações individuais.', 'Examinar o uso das relações além do exemplo inicial.']]),
    call('Antes de avançar na cena', 'Em cada etapa, procure o que muda no trabalho intelectual do aluno: ele apresenta uma ideia, confronta informações, usa um conceito e constrói uma explicação? Use os controles de etapas para acompanhar essa passagem.'),
    anim('mediation', 'A atividade precisa produzir uma relação', 'Avance pelos quatro controles da cena. Ela é um apoio já existente no aplicativo para discutir mediação. Relacione a progressão representada à sequência de Lia: partir do vivido, comparar, mobilizar conceitos e explicar relações.'),
    text('O planejamento articula fontes de conhecimento', 'A distinção entre distância, duração e acesso depende do saber disciplinar. A seleção do objetivo e sua posição no percurso mobilizam saber curricular. A lembrança de dificuldades anteriores contribui como saber da experiência. A escolha de uma representação ligada ao obstáculo pode ser analisada com Shulman.\nCaso Lia consulte pesquisas que explicitaram e testaram práticas de ensino, estará dialogando com conhecimento público sobre a ação pedagógica. Isso é diferente de afirmar que seu plano, antes de ser realizado, já produziu evidências de aprendizagem.'),
    compare('Uma adaptação justificada', 'Condição do trabalho', 'A sala não tem internet e alguns estudantes precisam de material com letras maiores. Lia prepara mapa e tabela impressos, legíveis para a turma.', 'Critério da decisão', 'A adaptação preserva a possibilidade de comparar informações e explicar relações. Sua adequação depende do objetivo e do acesso ao material, não do prestígio de usar tecnologia.'),
    text('Planejar não é prever cada resposta', 'A professora organiza uma intenção e condições de aprendizagem, mas acompanha o que acontece. Se a turma ainda confunde as unidades, retoma essa relação antes de exigir uma explicação mais ampla. Se a dificuldade for localizar os percursos, precisa orientar a leitura da representação.\nEsse ajuste não significa abandonar o currículo a cada resposta. Significa interpretar a distância entre o que se espera e o que a turma demonstra, escolhendo intervenções pertinentes. Para isso, é necessário tempo, recursos e trabalho coletivo; o planejamento não depende apenas de disposição individual.'),
    call('Verifique a justificativa', '“Farei um debate porque é uma metodologia ativa.” A frase explica a aprendizagem esperada? Ainda não. É preciso dizer o que será discutido, com quais informações e como o debate ajudará a construir a relação geográfica escolhida. O nome da atividade não resolve essas decisões.'),
    text('Ponte para a lição 9', 'No início da sequência, Lia ouviu os estudantes. Agora precisamos entender como essas falas entram na aprendizagem: não são apenas uma abertura simpática, nem substituem a elaboração conceitual. Elas podem orientar perguntas, comparações e revisão das explicações.')
], 'Planejar articula conteúdo, percurso curricular, experiência e escolhas para ensinar. A sequência deve oferecer condições de construir uma relação e permitir acompanhá-la, com adaptações pertinentes à turma.', order('Organize os momentos da sequência de Lia', [
    'Recolher hipóteses e justificativas iniciais sobre os trajetos.',
    'Orientar a comparação das informações e confrontar explicações.',
    'Sistematizar as relações com conceitos de circulação e acesso.',
    'Examinar explicações individuais em uma nova situação.' ]))

lesson(9, 'Saberes dos estudantes e mediação conceitual', 'O vivido vira ponto de partida para explicar', 19, [
    text('O relato traz uma questão, mas ainda precisa ser analisado', 'Na turma fictícia, um estudante diz: “Minha casa é perto da escola, mas espero muito pelo transporte”. Outro conta que percorre uma distância maior, com menos espera. Essas falas mostram experiências diferentes de deslocamento. Podem desestabilizar a hipótese de que distância resolve tudo.\nLia pergunta como os percursos se conectam e quais condições participam dos tempos. Ao colocar relatos em relação com mapas, registros e conceitos, faz mediação pedagógica. Na contribuição discutida de Cavalcanti, o diálogo entre conhecimentos cotidianos e científicos ajuda a ampliar a compreensão geográfica do vivido.'),
    text('O que torna a passagem didática?', 'Se Lia apenas recolher histórias e agradecer, terá ouvido experiências, mas ainda precisará construir a relação que pretende ensinar. Se ignorar as falas e pedir que repitam uma definição, pode perder uma possibilidade de reconhecer as explicações da turma.\nNo caso, ela organiza três perguntas: que diferença aparece nos relatos? Que informações podem ajudar a examiná-la? Como circulação e acesso ajudam a explicá-la? As perguntas ligam vivido, confronto de informações e elaboração conceitual. O conceito passa a servir para compreender uma situação.'),
    call('Antecipe uma interpretação', 'Uma praça tem o mesmo sentido para uma pessoa que trabalha ali, outra que atravessa o local e outra que o usa para encontrar amigos? Antes dos controles, pense em uma diferença possível e no que ela exigiria investigar.'),
    anim('lived', 'Três vivências, um lugar', 'Use “Pessoa 1”, “Pessoa 2” e “Pessoa 3” para comparar as leituras da praça. São personagens hipotéticos. Observe como a mudança de experiência oferece perguntas sobre o lugar; ela não prova que toda pessoa de um grupo terá a mesma vivência.'),
    text('Leia o resultado sem transformar diferença em rótulo', 'As personagens chamam atenção para usos e significados distintos. Lia pode pedir que comparem as interpretações e investiguem suas condições. Não deve concluir que moradores de uma área, estudantes do campo ou de comunidades ribeirinhas pensam todos do mesmo modo.\nConhecimentos cotidianos são relevantes e também podem ser discutidos. A afirmação “toda estrada é mais rápida que qualquer rio” precisa ser confrontada com condições e fontes. Valorizar quem fala não exige aceitar uma generalização sem exame.'),
    compare('Transferência: comercialização no campo', 'Fala de uma estudante', '“A produção passa por dois lugares antes de chegar à feira.” O relato informa uma experiência de circulação e pode revelar conexões que o mapa inicial não mostrava.', 'Mediação possível', 'Lia pede representar as etapas, comparar percursos e investigar transportes e intermediários. O conceito de rede ajuda a organizar relações; a aula não termina em uma lista de lugares.'),
    text('O que Lia aprende ao ouvir?', 'As falas também podem mudar o conhecimento profissional de Lia. Ela percebe, por exemplo, que sua tabela não incluía a espera e revê o que precisa representar. O estudante traz um conhecimento do cotidiano; a professora aprende sobre o ensino e sobre a situação ao examiná-lo.\nEssa distinção evita confundir experiência do aluno e saber da experiência docente. Mostra também que mediação não é uma transmissão em sentido único: a professora conserva a responsabilidade de orientar o estudo e pode rever suas próprias interpretações.'),
    call('Resposta que indica aprendizagem', '“Meu trajeto é perto, mas depende de uma conexão com longa espera; por isso a distância não basta para explicar o acesso.” A fala relaciona o vivido a condições de circulação. Para verificar o alcance da compreensão, Lia pode propor outra situação, sem exigir exposição de experiências pessoais de todos.')
], 'A mediação relaciona conhecimentos cotidianos, fontes e conceitos para ampliar explicações. Ouvir não encerra o ensino; orientar comparações e justificativas permite elaborar o vivido sem apagar sua diversidade.', match('Relacione a intervenção ao seu efeito', [
    ['Ouvir diferentes relatos e explicações iniciais.', 'Reconhecer conhecimentos e perguntas da turma.'],
    ['Confrontar uma afirmação geral com trajetos e condições.', 'Examinar o alcance de uma generalização.'],
    ['Usar circulação e rede para interpretar os relatos.', 'Organizar relações com conceitos geográficos.'],
    ['Lia revê a tabela porque percebe a importância da espera.', 'Construir aprendizagem profissional no diálogo.']]))

lesson(10, 'Avaliar para compreender e replanejar', 'O que a resposta realmente demonstra?', 20, [
    text('Lia chega ao momento de verificar a aprendizagem', 'Depois da comparação, a turma participa e responde rapidamente. Isso informa envolvimento, mas Lia quer saber se os estudantes aprenderam a explicar relações. Ela precisa olhar para o que o aluno faz com os dados e conceitos, em função do objetivo da aula.\nAvaliar aqui é interpretar evidências para orientar novas decisões. Uma resposta correta pode resultar de compreensão, memorização ou acaso. Pedir justificativa e propor uma situação diferente ajuda a examinar essas possibilidades, sem presumir o pensamento do aluno apenas pela alternativa marcada.'),
    table('Três respostas fictícias, três leituras', ['Resposta', 'O que já mostra', 'Próxima intervenção'], [
        ['“A é mais rápida porque tem 8 km.”', 'Compara distâncias, mas responde sobre tempo com outra grandeza.', 'Distinguir km e min e comparar as duas perguntas.'],
        ['“B é mais rápida: 25 minutos é menos que 45.”', 'Compara corretamente as durações.', 'Pedir relação com a distância e informações para explicar a diferença.'],
        ['“B leva menos tempo; o menor percurso não foi o mais rápido neste caso.”', 'Relaciona os dois resultados e delimita a conclusão.', 'Propor outro caso e discutir condições de acesso.']]),
    text('Um feedback que faz o raciocínio avançar', 'Para a segunda resposta, Lia pode escrever: “Você comparou corretamente os minutos. Agora confronte esse resultado com as distâncias: o que ele permite concluir sobre a ideia de que o mais curto é sempre o mais rápido?” O comentário reconhece o avanço e indica o trabalho seguinte.\n“Está certo, parabéns” pode incentivar, mas não orienta essa passagem. “Está incompleto” também não informa o que fazer. Feedback formativo relaciona o que foi demonstrado, a dificuldade ou ampliação necessária e um próximo passo possível.'),
    picture('u12-evidencias.png', 'Leia produções para decidir o próximo passo', 'O esquema retoma a relação entre resposta, interpretação e intervenção. Use os exemplos da tabela para dar conteúdo às etapas; uma impressão de sucesso não substitui a análise do que o aluno demonstrou.'),
    text('Transferência: acerto que merece outra pergunta', 'No novo exemplo, C tem 10 km e 20 minutos; D tem seis quilômetros e 35 minutos. A resposta esperada é que D tem menor distância e C menor duração. Lia pede que justifiquem as duas afirmações. Isso reduz a possibilidade de apenas repetir “B”, a resposta do primeiro exemplo.\nMesmo assim, uma tarefa não resume toda aprendizagem. A professora pode retomar a relação em outro momento e com outras condições. Não se trata de desconfiar de qualquer acerto, mas de adequar a evidência à amplitude da conclusão.'),
    compare('Do resultado à decisão docente', 'Leitura genérica', '“A turma foi mal; vou repetir tudo.” Não identifica o obstáculo e pode repetir uma intervenção que não o enfrentou.', 'Replanejamento orientado', '“A turma localiza os trajetos, mas troca distância por duração. Vou retomar unidades e comparar as justificativas antes de ampliar a análise do acesso.” A dificuldade orienta o ajuste.'),
    text('Dois usos que não são idênticos', 'Lia pode usar essas produções para replanejar a aula, construindo saber da experiência. Se decidir investigar e comunicar a prática, precisará explicitar problema, condições, critérios e limites. O simples ato de corrigir exercícios não demonstra que houve pesquisa pública no sentido de Gauthier.\nNa próxima lição, vamos acompanhar essa segunda possibilidade. O mesmo material pode contribuir para fins diferentes, mas a força da conclusão depende de como foi produzido e analisado.'),
    call('Verifique sua leitura', '“Os estudantes acertaram dez nomes de vias; logo aprenderam a explicar o acesso.” Qual é o limite? A evidência informa reconhecimento de nomes. Para concluir sobre explicação, é preciso examinar relações em uma tarefa adequada a esse objetivo.')
], 'A avaliação interpreta o que as produções demonstram em relação ao objetivo. Feedback orienta um próximo passo; replanejar exige localizar a dificuldade e ajustar a intervenção com base em evidências.', match('Escolha a leitura coerente da evidência', [
    ['Acertar nomes de lugares.', 'Demonstra reconhecimento; não prova sozinho uma explicação.'],
    ['Distinguir km e min em um novo par de trajetos.', 'Oferece evidência de uso da relação além do primeiro exemplo.'],
    ['Elogiar sem indicar como avançar.', 'Pode incentivar, mas não explicita o próximo trabalho conceitual.'],
    ['Retomar unidades após analisar um erro recorrente.', 'Replanejamento orientado pela dificuldade observada.']]))

lesson(11, 'Investigar a prática com outros docentes', 'Como sustentar e limitar uma conclusão?', 21, [
    text('Lia transforma a dificuldade em uma pergunta', 'Lia e a equipe querem investigar o ensino da relação entre distância e tempo. “Os alunos têm dificuldade em Geografia” é amplo demais para orientar o estudo. Delimitam: “Que mudanças aparecem nas justificativas sobre trajetos após uma comparação orientada de mapa e tabela?”\nA pergunta identifica um objeto examinável: as justificativas. A equipe registra as condições, descreve a intervenção e define como ler as produções. O exemplo é fictício e formativo; não apresenta resultados de uma pesquisa realmente realizada.'),
    table('Torne o procedimento compreensível', ['Decisão', 'Exemplo do estudo fictício'], [
        ['Registrar condições', 'Turma, tempo, materiais disponíveis e conhecimentos já trabalhados.'],
        ['Explicitar intervenção', 'Hipótese inicial, confronto de dados, discussão e nova situação.'],
        ['Definir critérios', 'Distingue grandezas? Relaciona os resultados? Justifica sem inventar causas?'],
        ['Conservar o que desafia a hipótese', 'Incluir respostas que não avançaram e explicações alternativas.'],
        ['Comunicar limites', 'Indicar diferenças entre tarefas, outras intervenções e alcance do caso.']]),
    picture('u12-investigar-pratica.png', 'Problema, intervenção, evidências e discussão', 'O esquema organiza decisões da investigação. As setas ajudam a acompanhar o trabalho, mas não dispensam justificar os critérios, examinar contradições e voltar ao problema quando necessário.'),
    text('Por que melhorar depois não prova uma causa exclusiva?', 'Suponha que as justificativas finais fiquem mais completas. A comparação é um resultado relevante, mas a turma também pode ter recebido outra explicação, aprendido com colegas ou enfrentado uma tarefa diferente. A sequência estudada pode ter contribuído sem ser demonstrada como causa única.\nA equipe deve discutir essas possibilidades em vez de escondê-las. Não é necessário que todo estudo use um mesmo desenho de pesquisa; é necessário que os procedimentos e a interpretação sustentem o tipo de afirmação que se pretende fazer.'),
    compare('Duas conclusões, alcances diferentes', 'Conclusão que excede o estudo', '“Nossa técnica elimina a dificuldade de todos os estudantes.” A afirmação estende um resultado situado a qualquer contexto e apaga respostas divergentes.', 'Conclusão compatível com o caso', '“Nas produções analisadas, apareceram mais distinções entre distância e tempo após a sequência; precisamos discutir outras intervenções e verificar como a proposta funciona em condições diferentes.”'),
    text('O coletivo amplia o exame da interpretação', 'Uma colega pode perceber que a resposta considerada “errada” distinguiu as grandezas, mas não conseguiu escrever a conclusão. Outra pode apontar que a segunda tarefa era mais simples. A discussão não serve apenas para confirmar Lia: ajuda a tornar critérios e interpretações mais consistentes.\nEsse exame público se relaciona à construção do saber da ação pedagógica em Gauthier. O valor profissional está em tornar o conhecimento discutível e utilizável com julgamento, sem impor a reprodução automática da atividade.'),
    text('Comunicar sem expor os estudantes', 'O relatório pode trabalhar com exemplos de respostas sem divulgar identidades ou constranger quem errou. Uma investigação com dados reais deve observar os procedimentos éticos aplicáveis ao estudo e à instituição. A unidade não solicita dados pessoais de alunos.\nA análise deve permanecer no problema de ensino: o que as produções permitem interpretar, que intervenção foi realizada e quais limites continuam. Esse cuidado evita transformar a dificuldade do estudante em rótulo ou a prática docente em propaganda.'),
    call('Transfira o modo de investigar', 'Agora troque trajetos por leitura de legendas. “A turma não sabe mapas” ainda é amplo. Uma pergunta possível é: “Como os alunos justificam diferenças entre dois mapas após comparar suas legendas e fontes?” Você conserva a lógica de delimitar, intervir e examinar, com outro conteúdo.')
], 'Investigar a prática exige delimitar perguntas, explicitar procedimentos, analisar produções e discutir limites. O exame coletivo pode fortalecer o conhecimento profissional sem transformar resultados situados em garantia universal.', order('Construa uma conclusão sustentada', [
    'Delimitar o que será investigado nas justificativas dos alunos.',
    'Registrar condições, intervenção e critérios antes de interpretar os resultados.',
    'Confrontar produções, respostas divergentes e explicações alternativas.',
    'Comunicar o que as evidências sustentam e onde a conclusão encontra limites.' ]))

lesson(12, 'Casos de prova e construção do argumento', 'Explique decisões, em vez de listar categorias', 23, [
    text('Agora reúna o que foi aprendido', 'Lia precisa compreender a Geografia, interpretar o percurso curricular, aprender no trabalho, representar o conteúdo e examinar respostas. A unidade não acrescentou nomes a uma aula pronta: mostrou como cada decisão pede conhecimento e justificativa. Esse é o raciocínio a levar para questões e redação.\nNos treinos autorais a seguir, primeiro identifique o problema do enunciado. Depois destaque o que a professora faz e a função dessa ação. Se o enunciado nomeia um autor, use sua acepção. Por fim, verifique se a alternativa descreve aquela função sem ampliar indevidamente a conclusão.'),
    compare('Questão resolvida 1: o foco da decisão', 'Situação', '“Uma professora escolhe o que retomar antes de comparar fluxos, considerando a sequência prevista para a turma.” Disciplinar ou curricular é o destaque?', 'Resolução', 'A decisão se refere à posição da aprendizagem no percurso: curricular. O conteúdo geográfico participa, mas o enunciado não destaca a validade de uma explicação ou a escolha de uma fonte.'),
    compare('Questão resolvida 2: duas exigências distintas', 'Situação', '“O professor conhece uma confusão de escala e elabora uma comparação para enfrentá-la.” Isso demonstra conhecimento pedagógico do conteúdo ou já comprova saber da ação pedagógica em Gauthier?', 'Resolução', 'O destaque se aproxima de Shulman: dificuldade específica e representação para ensinar. Para afirmar o exame público da experiência no sentido de Gauthier, faltam explicitação e teste por pesquisas sobre o ensino.'),
    call('Observe para argumentar', 'Na cena, compare “Acesso vulnerável” e “Infraestrutura melhorada”. Depois imagine a decisão de ensino: qual relação a turma precisa explicar e que tarefa permitiria verificar essa aprendizagem? A cena é hipotética; não oferece dados de uma escola real.'),
    anim('inequality', 'Uma situação geográfica, várias decisões docentes', 'Use os dois controles e distinga os planos da análise. Explicar chuva e condições de circulação mobiliza conteúdo; escolher o objetivo envolve currículo; rever uma intervenção com base nas respostas produz aprendizagem profissional.'),
    text('Do conceito à frase argumentativa', 'Uma resposta fraca diz: “Lia usa todos os saberes, que são importantes”. Ela não mostra a função de nenhum. Uma resposta desenvolvida afirma: “Ao distinguir distância e duração, Lia mobiliza conhecimento disciplinar; ao organizar a comparação no percurso da turma, usa saber curricular. Essas escolhas precisam ser verificadas em explicações dos alunos”.\nA segunda formulação apresenta conceitos, decisões e uma consequência para a aprendizagem. O exemplo deixa de ser uma ilustração solta: passa a sustentar o argumento.'),
    table('Construa um parágrafo em quatro movimentos', ['Movimento', 'Aplicação ao tema'], [
        ['Ideia central', 'Ensinar Geografia exige articular saberes para transformar conteúdo em aprendizagem.'],
        ['Explicação conceitual', 'Distinguir saber disciplinar, curricular e aprendizagem na experiência.'],
        ['Decisão analisada', 'Mostrar por que comparar trajetos e orientar a leitura de km e min.'],
        ['Consequência e limite', 'Examinar justificativas em outro caso; não deduzir compreensão da participação.']]),
    text('Modelo comentado de raciocínio', '“O domínio dos conceitos é necessário, mas o professor precisa organizá-los em situações de aprendizagem. Em uma aula sobre trajetos, distinguir distância e duração mobiliza saber disciplinar; selecionar a comparação e sua progressão envolve saber curricular. Ao analisar justificativas, o docente pode rever a intervenção e aprender com a experiência. A compreensão deve aparecer no uso dessas relações em outra situação.”\nObserve a sequência: a primeira frase responde ao problema; as duas seguintes explicam os saberes em uma decisão; a última indica uma evidência de aprendizagem. A oficina de redação amplia esse argumento e acrescenta o exame público da prática.'),
    call('Use a revisão de forma ativa', 'Antes do simulado, explique sem consultar: por que divulgar não basta em Gauthier? Como Shulman ajuda a analisar uma representação? O que significa saber situado em Tardif? Se só consegue repetir a palavra, volte ao caso da lição correspondente. O simulado tem 20 casos novos comentados; são questões autorais, sem previsão de cobrança oficial.'),
    text('Feche o percurso com uma transferência', 'Troque trajetos por um problema de leitura de mapas, abastecimento ou uso de uma praça. Você consegue definir conteúdo, objetivo, dificuldade, intervenção e evidência? Se consegue justificar essas relações, já dispõe de um modo de analisar a docência além dos exemplos memorizados. Continue pelas questões, pelos cartões e pela escrita.')
], 'Na prova, identifique a função da decisão, use os conceitos na acepção correta e sustente o argumento com um caso analisado. Relacione intervenção e evidência de aprendizagem, reconhecendo o alcance da conclusão.', order('Organize um argumento sobre os saberes docentes', [
    'Responder ao problema com uma ideia central.',
    'Explicar os saberes necessários sem confundir os autores.',
    'Analisar uma decisão concreta de ensino de Geografia.',
    'Relacionar a intervenção à aprendizagem e delimitar a conclusão.' ]))

# Todos os problemas anteriores passam à prática, com o significado intacto.
questions = copy.deepcopy(ORIGINAL['questions'])
for question in questions:
    question['pool'] = 'lesson'


def final(n, lesson_n, stem, options, answer, feedback, tag):
    assert len(options) == len(feedback) == 4
    questions.append(dict(id=f'r2f{n:02d}', lesson=f'l{lesson_n:02d}', stem=stem,
                          options=options, answer=answer, feedback=feedback,
                          tag=tag, pool='final', type='single'))


final(1, 2, 'Lia tem um mapa com a posição das escolas e uma tabela de tempos de viagem. Um colega conclui que o mapa, sozinho, comprova que todos têm acesso semelhante. Qual análise mobiliza melhor o saber disciplinar?',
      ['O mapa situa as escolas; explicar acesso exige examinar conexões e condições que sua localização não informa sozinha.',
       'O mapa é suficiente se tiver uma legenda completa, pois a legenda transforma localização em explicação do acesso.',
       'A tabela deve substituir o mapa em toda a aula, porque durações dispensam a análise da distribuição espacial.',
       'A conclusão será adequada se o número de escolas for igual nas áreas, pois essa igualdade é o critério decisivo de acesso.'], 0,
      ['A resposta delimita o alcance da fonte e explicita o que falta investigar. Saber disciplinar inclui julgar a validade da explicação geográfica.',
       'Legenda é importante para interpretar o mapa, mas não acrescenta automaticamente informações sobre transportes, trajetos e condições de acesso.',
       'Tempos ajudam a analisar deslocamentos, mas não tornam a distribuição e as conexões espaciais irrelevantes. As fontes podem ser articuladas.',
       'Quantidades iguais podem coexistir com distribuições, capacidades e condições de circulação diferentes. O critério não sustenta sozinho a conclusão.'], 'alcance das fontes')

final(2, 3, 'O objetivo de uma aula é explicar diferenças entre trajetos. A turma compara mapa e tabela, mas a avaliação pede apenas os nomes das vias. Qual revisão enfrenta diretamente o problema?',
      ['Pedir uma justificativa sobre outro par de trajetos, usando dados e relações trabalhados na aula.',
       'Aumentar a quantidade de nomes na avaliação, para que a amostra do conteúdo fique mais extensa.',
       'Atribuir o mesmo peso à participação e aos nomes, presumindo que os dois resultados representam a explicação.',
       'Repetir os dados do exemplo e pedir a letra da rota escolhida, sem solicitar o raciocínio.'], 0,
      ['A tarefa se alinha ao objetivo de explicar e permite examinar o uso das relações em outra situação.',
       'Mais nomes ampliam a tarefa de reconhecimento, mas não passam a exigir uma explicação sobre as diferenças de acesso.',
       'Participar e reconhecer nomes informam dimensões da atividade. A combinação não comprova a relação conceitual que o objetivo pede.',
       'A repetição pode resultar em memorização da resposta. Outra situação e uma justificativa oferecem evidências mais adequadas ao objetivo.'], 'alinhamento curricular')

final(3, 4, 'Após perceber que vários alunos escolhem rotas pelo desenho, Lia passa a pedir a leitura das unidades antes da comparação. Ela acompanha se a mudança ajuda a turma. O que caracteriza saber da experiência nesse episódio?',
      ['A aprendizagem de uma decisão profissional a partir da interpretação de uma dificuldade vivida no trabalho.',
       'O número de anos de serviço, que por si só confirma a adequação de qualquer ajuste feito na aula.',
       'A proximidade pessoal com os estudantes, que transforma a impressão da professora em validação pública da estratégia.',
       'A origem local do mapa, que converte automaticamente seu conteúdo em saber experiencial docente.'], 0,
      ['O destaque é a aprendizagem profissional na relação entre situação, interpretação e ajuste acompanhado. A experiência não é só passagem do tempo.',
       'Tempo de serviço oferece experiências, mas não garante a validade de todas as decisões. O episódio destaca o exame de uma dificuldade.',
       'A relação com os alunos é relevante para o trabalho, mas a impressão pessoal não equivale ao exame público de uma prática.',
       'A origem do material não define esse saber. É o aprendizado profissional da professora que está em análise.'], 'experiência e reflexão')

final(4, 5, 'Uma equipe publica a sequência de uma aula e recebe elogios de colegas. Quer afirmar que produziu saber da ação pedagógica na acepção de Gauthier. Qual informação ainda é decisiva para sustentar essa afirmação?',
      ['Como a experiência foi testada por pesquisa sobre o ensino, com procedimentos, evidências e limites acessíveis ao exame.',
       'Quantos professores aprovaram a sequência, pois o consenso substitui a análise das produções dos alunos.',
       'Se a atividade empregou uma tecnologia recente, pois a inovação do recurso define a natureza pública do saber.',
       'Se o relato contém o plano completo, pois explicitar a intenção do professor já demonstra os resultados da intervenção.'], 0,
      ['Tornar público e submeter a experiência ao teste por pesquisas é central nessa acepção. A divulgação e a investigação têm exigências distintas.',
       'A aprovação pode favorecer a circulação da proposta, mas não substitui os critérios e as evidências que sustentam o conhecimento.',
       'A idade da tecnologia não define o estatuto do saber. Uma intervenção impressa também pode ser investigada publicamente.',
       'Um plano torna as intenções compreensíveis. Resultados precisam ser examinados; não podem ser deduzidos do que se pretendia fazer.'], 'ação pedagógica em Gauthier')

final(5, 6, 'Ao estudar a trajetória de Lia, um pesquisador considera sua vida escolar, a licenciatura, o início da carreira e as relações com colegas. Na contribuição de Tardif, esse recorte ajuda principalmente a compreender:',
      ['A constituição temporal e plural dos saberes mobilizados em situações de trabalho.',
       'A substituição gradual da formação pelo tempo de serviço, como se aprender uma fonte anulasse as anteriores.',
       'A existência de um saber pessoal que dispensa confrontar explicações com outros conhecimentos.',
       'A transferência direta de conhecimentos universitários para a aula, independentemente da turma.'], 0,
      ['A trajetória permite examinar diferentes fontes e momentos de constituição dos saberes, considerando sua mobilização no trabalho concreto.',
       'O caráter temporal não significa que a experiência apaga a formação. O problema é compreender a combinação e a transformação das fontes.',
       'Personalização e situação de trabalho não tornam toda opinião válida. As decisões continuam abertas a exame e diálogo.',
       'A análise da trajetória e do trabalho questiona a ideia de aplicação direta e indiferente às situações de ensino.'], 'temporalidade e pluralidade')

final(6, 7, 'Lia percebe que a turma associa o maior denominador à maior escala. Compara representações da mesma área e pede que os alunos expliquem a redução. Pela entrada de Shulman, o aspecto central é:',
      ['A relação entre uma dificuldade específica do conteúdo e a escolha de uma representação para torná-lo compreensível.',
       'A seleção da etapa curricular, já que qualquer comparação entre imagens define a progressão escolar completa.',
       'A existência de pesquisa pública, que fica comprovada quando a professora muda a representação de um conteúdo.',
       'A adoção de uma técnica de participação que pode ser justificada sem referência ao significado de escala.'], 0,
      ['O conhecimento pedagógico do conteúdo envolve representações, explicações e dificuldades próprias do assunto ensinado.',
       'A seleção curricular pode participar da aula, mas o destaque do enunciado é como enfrentar uma confusão conceitual específica.',
       'Alterar uma representação não comprova que a experiência foi testada por pesquisas e submetida a exame público.',
       'A pertinência da intervenção depende da relação de redução que precisa ser aprendida, não apenas de promover participação.'], 'conhecimento pedagógico do conteúdo')

final(7, 9, 'Uma aluna relata a espera pelo barco. Ao ouvi-la, Lia percebe que sua tabela não registra a espera e aprende a incluí-la em comparações futuras. Como distinguir os conhecimentos em jogo?',
      ['A aluna traz um conhecimento do cotidiano; Lia constrói aprendizagem profissional ao interpretar o relato para o ensino.',
       'O relato da aluna e a revisão de Lia são o mesmo saber experiencial docente, porque ambos se originam de algo vivido.',
       'Apenas Lia produz conhecimento, pois um relato do cotidiano não pode contribuir para um problema geográfico.',
       'A experiência da aluna elimina a necessidade de outros dados, tornando sua viagem um modelo suficiente para todos os percursos.'], 0,
      ['As experiências dialogam, mas têm funções distintas no episódio. O aprendizado profissional de Lia não apaga o conhecimento trazido pela estudante.',
       'Ter origem no vivido não torna os dois conhecimentos idênticos. Saber experiencial docente se refere à aprendizagem no exercício profissional.',
       'O relato pode levantar relações e informações importantes. A mediação o confronta e articula com outras fontes e conceitos.',
       'Uma viagem pode iniciar uma investigação, mas não autoriza generalizar as condições de todos os trajetos.'], 'experiência do estudante e do docente')

final(8, 10, 'Depois de um jogo com mapas, todos participaram e localizaram as escolas. Lia pretende concluir que aprenderam a explicar o acesso. Qual evidência seria mais adequada para ampliar essa conclusão?',
      ['Justificativas que relacionem trajetos e condições de circulação a uma diferença de acesso.',
       'Uma votação indicando que a turma prefere o jogo à exposição oral, como medida suficiente da relação conceitual.',
       'Um registro de participação ainda mais detalhado, mantendo a explicação das relações fora da tarefa.',
       'Uma fotografia dos mapas preenchidos, sem examinar o que os alunos conseguem explicar com eles.'], 0,
      ['Essa produção se aproxima da aprendizagem pretendida. Participação e localização são relevantes, mas não demonstram sozinhas uma explicação.',
       'A preferência informa a percepção da atividade, não o uso das relações geográficas para explicar acesso.',
       'Detalhar o envolvimento melhora esse registro, mas não muda a dimensão conceitual que ainda precisa ser examinada.',
       'A foto registra um produto. É necessário analisar seu conteúdo e o que sustenta a conclusão sobre a aprendizagem.'], 'evidências e objetivo')

final(9, 10, 'Um aluno escreve: “B leva menos tempo porque 25 minutos é menos que 45”. Qual feedback o ajuda a avançar além dessa comparação correta?',
      ['“Você comparou as durações. Agora relacione o resultado às distâncias e explique o que isso mostra sobre a hipótese inicial.”',
       '“Resposta correta; memorize que B é a melhor rota para qualquer pergunta que envolva o exemplo.”',
       '“Faltou escrever mais; acrescente os nomes das vias sem alterar o raciocínio.”',
       '“A justificativa está incompleta; copie a definição de circulação e encerre a atividade.”'], 0,
      ['O comentário reconhece o avanço e orienta uma relação adicional pertinente ao objetivo da aula. Esse é um próximo passo formativo.',
       'B tem menor duração no exemplo, mas não menor distância. A memorização da letra apaga a distinção entre critérios.',
       'A extensão do texto e os nomes não resolvem, por si só, a relação que ainda pode ser construída.',
       'Copiar um conceito não garante que o aluno consiga usá-lo. O feedback precisa orientar o raciocínio exigido no caso.'], 'feedback formativo')

final(10, 8, 'Sem internet e com necessidade de ampliar letras, Lia troca o mapa digital por um croqui e uma tabela impressos. Qual justificativa analisa melhor a adaptação?',
      ['A escolha deve preservar a comparação e a explicação pretendidas, com material legível e acessível à turma.',
       'A adaptação se justifica por ser impressa, característica que garante compreensão mais profunda que qualquer suporte digital.',
       'A troca mantém o objetivo automaticamente, pois recursos diferentes sempre produzem a mesma atividade intelectual.',
       'A perda da internet exige reduzir a aula à cópia de nomes, pois explicar relações depende da plataforma original.'], 0,
      ['O critério conecta condições de trabalho e possibilidade de aprendizagem. O recurso é julgado pelo que permite realizar com orientação.',
       'O suporte impresso não garante compreensão por si só. É preciso examinar o conteúdo, a legibilidade e seu uso na sequência.',
       'A função da tarefa pode mudar com a adaptação. Preservar o objetivo exige verificar o que o novo material permite comparar e explicar.',
       'Comparar fontes e explicar relações pode ser feito com materiais impressos; a plataforma não determina sozinha a aprendizagem.'], 'planejamento e condições')

final(11, 4, 'Duas professoras analisam respostas e trocam maneiras de trabalhar a legenda. Não há informação de que realizaram uma pesquisa pública. Qual interpretação é sustentada pelo episódio?',
      ['A troca pode participar da construção coletiva de saberes da experiência, sem comprovar por si só o saber da ação pedagógica em Gauthier.',
       'A experiência deixa de ser experiencial quando compartilhada, passando necessariamente a conhecimento testado por pesquisa.',
       'O saber da experiência é estritamente solitário; a conversa entre professoras não pode participar de sua construção.',
       'O acordo entre as colegas permite recomendar a mesma intervenção para qualquer turma, sem precisar examinar as condições.'], 0,
      ['Aprender no trabalho pode incluir relações com colegas. Para afirmar pesquisa e exame público, são necessárias informações que o caso não fornece.',
       'Compartilhar é relevante, mas não demonstra automaticamente investigação com procedimentos e evidências examináveis.',
       'Saberes experienciais podem se construir individual e coletivamente nas relações profissionais.',
       'A troca não produz uma garantia universal. A pertinência da decisão continua dependendo do problema e das condições de ensino.'], 'experiência coletiva')

final(12, 3, 'Uma turma já localiza pontos e lê a legenda. O próximo objetivo é explicar diferenças entre conexões. Qual proposta evidencia uma progressão coerente com esse ponto de partida?',
      ['Comparar trajetos e dados, orientando a passagem da localização para uma justificativa sobre as conexões.',
       'Repetir a cópia dos mesmos pontos com outro título, tomando a mudança de tema como prova de avanço.',
       'Introduzir termos mais numerosos sem exigir relações, considerando a quantidade de palavras o critério de progressão.',
       'Abandonar a localização e a legenda em todas as tarefas, porque conhecimentos anteriores impedem avançar.'], 0,
      ['A proposta amplia operações e relações a partir do que a turma já demonstra, coerente com a aprendizagem escolhida.',
       'Trocar o título sem alterar o trabalho intelectual não demonstra ampliação da aprendizagem.',
       'Vocabulário pode ser necessário, mas a progressão pretendida envolve usar relações para explicar, não apenas aumentar a lista.',
       'Conhecimentos anteriores podem sustentar novas relações. Avançar não exige apagar o que já foi aprendido.'], 'progressão curricular')

final(13, 6, 'Considere duas informações: I — Lia escolheu uma representação para enfrentar uma dificuldade de escala. II — Uma equipe explicitou e testou essa intervenção por pesquisa, comunicando evidências e limites. Qual associação conserva as diferenças estudadas?',
      ['I destaca o conhecimento pedagógico do conteúdo em Shulman; II permite discutir o saber da ação pedagógica em Gauthier.',
       'I e II designam a mesma categoria em ambos os autores, pois toda representação didática já é pesquisa pública.',
       'I demonstra exclusivamente saber curricular; II se refere apenas ao domínio dos conceitos da Geografia.',
       'I dispensa compreender escala; II permite transformar o resultado em regra universal para o ensino.'], 0,
      ['As duas análises podem se articular, mas focalizam exigências distintas: ensinar um conteúdo e submeter a experiência ao exame público.',
       'Uma representação pode ser pertinente sem ter sido testada por pesquisa. As classificações não são automaticamente equivalentes.',
       'O primeiro destaque é a relação entre dificuldade e representação; o segundo é a investigação do ensino, não apenas o conteúdo geográfico.',
       'A representação precisa conservar o conceito, e resultados de pesquisa continuam exigindo interpretação de condições e limites.'], 'comparação entre autores')

final(14, 6, 'Lia argumenta: “Minha decisão foi adequada naquela turma, com aqueles conhecimentos e recursos; preciso examiná-la em outras condições”. Como essa afirmação pode dialogar com a ideia de saber situado em Tardif?',
      ['Reconhece que os saberes se mobilizam em situações concretas, sem tornar a experiência incomunicável ou imune à crítica.',
       'Demonstra que cada professora possui uma verdade própria, dispensando critérios para discutir as decisões.',
       'Prova que apenas o conhecimento sobre o bairro pode ser ensinado, excluindo relações com outras escalas.',
       'Indica que estudos da formação não podem contribuir para o trabalho, porque não nasceram naquela turma.'], 0,
      ['Situação de trabalho, pessoas e condições participam das decisões. Reconhecê-las não impede compartilhar e confrontar conhecimentos.',
       'O caráter situado não equivale a considerar toda opinião válida. É preciso examinar justificativas e resultados.',
       'Situado se refere à constituição e mobilização dos saberes no trabalho. Não restringe o conteúdo geográfico à escala local.',
       'Conhecimentos de diferentes fontes podem ser mobilizados e reinterpretados na situação. A formação não é excluída.'], 'saberes situados')

final(15, 6, 'Antes de começar a ensinar, Lia imaginava que uma boa aula deveria reproduzir o formato que viveu como estudante. Ao confrontar essa ideia com a aprendizagem da turma, passa a revê-la. No repertório discutido por Gauthier, o primeiro aspecto se aproxima de:',
      ['Saberes da tradição pedagógica: representações herdadas sobre ensinar, que precisam ser interrogadas.',
       'Saberes da ação pedagógica: concepções já validadas por pesquisa pelo fato de serem conhecidas por gerações.',
       'Saberes disciplinares: a estrutura conceitual da Geografia, independentemente das imagens que Lia tem da aula.',
       'Saberes curriculares: a definição completa das aprendizagens oficiais, deduzida da lembrança da vida escolar.'], 0,
      ['O episódio destaca concepções anteriores sobre o ensino, formadas também na vida escolar. Sua presença não dispensa exame crítico.',
       'A permanência de uma prática não comprova teste por pesquisas. Tradição e saber da ação pedagógica não são sinônimos.',
       'O conteúdo geográfico pode participar da aula, mas o caso destaca uma representação de como ensinar.',
       'Lembranças da escola podem influenciar decisões, mas não definem por si só os objetivos e a organização curricular atuais.'], 'tradição pedagógica')

final(16, 11, 'Após uma sequência de comparação de mapas, as justificativas ficam mais completas. No mesmo período, a turma recebeu outra explicação e a tarefa final tinha dados diferentes. Qual conclusão é mais consistente?',
      ['Há um resultado a analisar, mas a contribuição da sequência deve ser discutida considerando outras intervenções e diferenças entre tarefas.',
       'A melhora prova que a sequência é causa exclusiva, pois a ordem antes/depois dispensa outras informações.',
       'A presença de outras condições torna todas as produções inúteis para qualquer análise da prática.',
       'Para reforçar a conclusão, devem ser retiradas as respostas que não melhoraram, mantendo apenas os exemplos favoráveis.'], 0,
      ['A conclusão reconhece a evidência sem afirmar uma causalidade exclusiva não demonstrada. Procedimentos e limites orientam seu alcance.',
       'Uma mudança posterior pode envolver vários fatores. A ordem temporal não basta para provar a causa exclusiva.',
       'As produções continuam informativas. O necessário é interpretar o que sustentam e os limites da comparação.',
       'Excluir resultados divergentes enfraquece o exame da interpretação. Eles precisam participar da análise.'], 'evidência e causalidade')

final(17, 12, 'Uma professora quer discutir como decisões sociais e infraestrutura participam das diferenças de acesso à escola. Qual análise distingue a concepção geográfica do saber docente mobilizado?',
      ['A perspectiva crítica orienta relações da explicação; compreender essas relações integra o saber disciplinar, que se articula a escolhas curriculares e de ensino.',
       'A perspectiva crítica substitui os saberes docentes, tornando desnecessário organizar objetivo, intervenção e avaliação.',
       'Saber disciplinar é o nome exclusivo da Geografia crítica, enquanto outras concepções correspondem apenas a métodos de aula.',
       'A escolha de um debate identifica por si só a concepção crítica, independentemente do problema e dos argumentos discutidos.'], 0,
      ['A análise conserva planos distintos e articulados: como compreender o espaço e que conhecimentos sustentam as decisões de ensinar.',
       'Uma concepção não resolve sozinha como a turma vai aprender e como essa aprendizagem será acompanhada.',
       'O saber disciplinar inclui conhecimentos e formas de investigar o campo, não sendo um sinônimo de uma única corrente.',
       'Debate é uma estratégia. A concepção precisa ser analisada nas relações e explicações que orientam o trabalho.'], 'articulação com a unidade 1.1')

final(18, 7, 'No novo caso, C tem 10 km e 20 minutos; D tem 6 km e 35 minutos. O aluno responde: “D tem menor distância, C tem menor duração; os dados não explicam sozinhos a causa”. O que Lia pode concluir com mais fundamento?',
      ['O aluno distingue as grandezas e delimita o alcance dos dados em outra situação, oferecendo evidência de compreensão da relação trabalhada.',
       'O aluno demonstrou que a distância não participa de nenhum problema de acesso e deve ser excluída do estudo.',
       'A resposta estabelece que C é a melhor opção em qualquer condição, inclusive de custo e disponibilidade de transporte.',
       'A ausência de uma causa inventada mostra que o aluno ainda não consegue interpretar informações quantitativas.'], 0,
      ['A resposta aplica o raciocínio em outro exemplo e reconhece o que ainda exige investigação. Isso sustenta uma conclusão delimitada sobre aprendizagem.',
       'Distinguir distância e tempo não torna a distância irrelevante. Ela participa da análise com outras condições.',
       'Menor duração não resolve todos os critérios de acesso. Custo, disponibilidade e condições não estão informados.',
       'Reconhecer limites da fonte é um cuidado de interpretação, não uma incapacidade. Inventar uma causa ausente não seria avanço.'], 'transferência da aprendizagem')

final(19, 12, 'Qual trecho constrói melhor um argumento sobre os saberes docentes, usando o exemplo para explicar sua função?',
      ['“O domínio de distância e duração sustenta a explicação geográfica; organizar sua comparação no percurso da turma mobiliza saber curricular. Justificativas em outro caso ajudam a examinar a aprendizagem.”',
       '“Os saberes docentes são importantes e devem ser usados em conjunto. Isso mostra que todas as boas aulas são completas e fazem aprender.”',
       '“Lia usou mapa, tabela e animação. A quantidade de recursos comprova a articulação entre os saberes e o domínio dos alunos.”',
       '“Tardif, Gauthier e Shulman estudam professores. Assim, os conceitos de qualquer um deles podem substituir os dos demais no argumento.”'], 0,
      ['O trecho relaciona conceitos a decisões concretas e indica uma evidência pertinente. O exemplo sustenta o argumento em vez de apenas ornamentá-lo.',
       'A importância é afirmada sem explicar a função dos saberes. A conclusão sobre aprendizagem não apresenta evidência.',
       'Listar recursos não mostra como foram usados nem o que os alunos aprenderam. É preciso analisar decisões e produções.',
       'Um campo de interesse compartilhado não torna as contribuições equivalentes. A precisão conceitual continua necessária.'], 'argumentação')

final(20, 11, 'Uma equipe investiga dificuldades de leitura de mapas. Qual recorte oferece melhores condições para examinar uma prática de ensino?',
      ['Analisar como as justificativas sobre dois mapas mudam após comparar legendas e fontes, explicitando critérios, condições e limites.',
       'Perguntar se a turma é boa em Geografia, sem delimitar quais aprendizagens ou produções serão observadas.',
       'Comparar a popularidade de dois professores, tomando preferência pessoal como medida suficiente de compreensão cartográfica.',
       'Reunir apenas os relatos de sucesso e recomendar a intervenção antes de definir o que conta como aprendizagem.'], 0,
      ['O recorte identifica problema, intervenção e produções examináveis. A análise ainda precisa ser realizada, mas suas decisões estão mais claras.',
       'A formulação é ampla e pode rotular estudantes. Não delimita o problema de ensino nem a evidência a analisar.',
       'Preferência não equivale à aprendizagem cartográfica. O recorte precisa examinar produções relacionadas ao conteúdo.',
       'Selecionar só sucessos e concluir antes de definir critérios impede um exame consistente da prática e de seus limites.'], 'investigação da prática')


def balance_new_options():
    for i, question in enumerate(q for q in questions if q['pool'] == 'final'):
        target = [2, 0, 3, 1][i % 4]
        shift = (target-question['answer']) % 4
        items = list(zip(question['options'], question['feedback']))
        if shift:
            items = items[-shift:] + items[:-shift]
        question['options'] = [a for a, _ in items]
        question['feedback'] = [f for _, f in items]
        question['answer'] = target


flashcards = copy.deepcopy(ORIGINAL['flashcards'])
examples = [
    'No caso de Lia: distinguir distância, duração e condições de acesso.',
    'No caso de Lia: escolher a aprendizagem e a sequência que permite construí-la.',
    'Exemplo: perceber uma dificuldade recorrente e aprender a orientar a leitura das unidades.',
    'Pergunte como a prática foi explicitada, investigada e examinada por outras pessoas.',
    'Uma postagem com elogios não demonstra o que os alunos aprenderam.',
    '“Trajetos” é tema; “explicar a diferença entre distância e duração” explicita aprendizagem.',
    'Localizar pode sustentar comparar e explicar, conforme o problema e a turma.',
    'Se o objetivo é explicar, a avaliação precisa examinar relações e justificativas.',
    'A foto do rio Guamá não revela por si só os tempos de viagem.',
    'Um centímetro corresponde a 100 m na primeira e a 1 km na segunda.',
    'Mapa e tabela precisam ter uma função na dificuldade que se pretende enfrentar.',
    'Exemplo: representar km e min de modo que a turma confronte sua confusão entre as grandezas.',
    'Na aula, Lia mobiliza formação, Geografia, currículo e experiência de trabalho.',
    'O exame público não transforma o resultado de uma prática em receita universal.',
    'Conhecer a matéria inclui pensar em explicações que ajudem outros a compreendê-la.',
    'O relato de um trajeto pode ser confrontado com fontes e interpretado com circulação e rede.',
    'A estudante relata a espera; Lia aprende a incluir essa condição em sua intervenção.',
    'Para concluir sobre explicação, examine relações em uma produção adequada ao objetivo.',
    '“Você comparou os minutos; agora relacione o resultado às distâncias” indica um próximo passo.',
    'Repetir toda a aula sem localizar o obstáculo pode manter a mesma dificuldade.',
    'Registrar também respostas divergentes permite confrontar a interpretação inicial.',
    'Diferenças entre tarefas, outras explicações e condições da turma precisam ser discutidas.',
    'O foco curricular de uma pergunta não exclui que a professora conheça a Geografia.',
    'O exemplo deve mostrar como o saber participa da decisão e do resultado esperado.'
]
for card, example in zip(flashcards, examples):
    card['back'] += ' '+example
flashcards += [
    dict(id='c25', front='Saberes temporais em Tardif', back='Constituem-se ao longo da história escolar, da formação e da carreira. Tempo de serviço não garante, sozinho, a adequação de toda decisão.'),
    dict(id='c26', front='Saberes situados significam opinião sem critérios?', back='Não. Pessoas e condições concretas participam da mobilização dos saberes, que continuam abertos à crítica, ao estudo e à discussão profissional.'),
    dict(id='c27', front='Tradição pedagógica em Gauthier', back='Representações e modos herdados de imaginar e organizar o ensino. A lembrança de como se estudou pode orientar a docência e precisa ser interrogada.'),
    dict(id='c28', front='Experiência docente pode ser coletiva?', back='Sim. A análise com colegas pode produzir aprendizagem profissional. Compartilhar não comprova, por si só, que houve pesquisa pública no sentido de Gauthier.'),
    dict(id='c29', front='Resposta correta ou compreensão?', back='Um acerto isolado pode ter origens diferentes. Justificativa e uso da relação em outro caso ajudam a examinar o que foi compreendido.'),
    dict(id='c30', front='Os quatro focos do edital esgotam um autor?', back='Não. Tardif, Gauthier e Shulman têm perguntas e classificações próprias. Compare suas contribuições sem transformar todos os termos em equivalentes.')
]

references = copy.deepcopy(ORIGINAL['references'])
for reference in references:
    if reference['author'] == 'Lee S. Shulman':
        reference['note'] += ' Texto primário de 1986 disponível pela Western Carolina University na ficha de leitura.'

essay = copy.deepcopy(ORIGINAL['essay'])
# Os seis critérios originais conservam ordem e sentido das marcações salvas.
essay['rubric'] += [
    'Meu exemplo mostra por que cada saber participa da decisão, sem limitar-se aos nomes.',
    'Indiquei uma tarefa que permite verificar o uso do conceito além do exemplo inicial.'
]
essay['model'] = (
    'Ensinar Geografia exige articular saberes para transformar o conteúdo em aprendizagem. O domínio conceitual é necessário, mas precisa dialogar com a organização curricular e com a interpretação das situações de ensino.\n'
    'Em uma aula sobre trajetos, distinguir distância e duração mobiliza saber disciplinar. Definir que a turma deverá explicar diferenças de acesso e organizar uma comparação orientada envolve saber curricular. O exemplo mostra funções diferentes que participam da mesma decisão.\n'
    'Ao observar que os alunos escolhem pelo desenho sem consultar as unidades, a professora pode rever sua intervenção e aprender com a experiência. Em vez de apenas corrigir a letra, orienta a comparação entre quilômetros e minutos e pede uma justificativa em outro caso.\n'
    'Essas produções oferecem evidências para avaliar e replanejar. Para constituir saber da ação pedagógica na acepção de Gauthier, a experiência precisa ser explicitada, tornada pública e testada por pesquisas sobre o ensino; a impressão de sucesso não basta.\n'
    'Assim, a articulação dos saberes sustenta escolhas justificadas e abertas ao exame. As condições da turma e os limites das evidências devem ser considerados antes de transformar um resultado situado em recomendação geral.'
)


def save():
    catalog_path = ROOT/'content/catalog.json'
    catalog = json.loads(catalog_path.read_text())
    entry = next(e for m in catalog['modules'] for e in m['units'] if e['id'] == '1.2')
    assert entry['revision'] <= 2, 'Não sobrescreva uma revisão posterior.'
    balance_new_options()
    assert len(lessons) == 12 and len(questions) == 80 and len(flashcards) == 30
    assert len([q for q in questions if q['pool'] == 'final']) == 20
    by_id = {q['id']: q for q in questions}
    for old in ORIGINAL['questions']:
        for field in ['lesson', 'stem', 'options', 'answer', 'feedback', 'tag', 'type']:
            assert by_id[old['id']][field] == old[field], (old['id'], field)
    unit = copy.deepcopy(ORIGINAL)
    unit.update(revision=2, shortTitle='Aprender a decidir e ensinar Geografia',
                subtitle='Uma aula acompanhada: conteúdo, currículo, experiência, mediação e evidências para a prova.',
                estimatedMinutes=sum(l['minutes'] for l in lessons),
                objectives=[
                    'Explicar os saberes docentes a partir das funções que desempenham em decisões de ensino.',
                    'Distinguir tema, objetivo, recurso, progressão e evidência de aprendizagem.',
                    'Comparar Tardif, Gauthier e Shulman sem confundir suas perguntas e classificações.',
                    'Analisar uma dificuldade e justificar representação, mediação, feedback e replanejamento.',
                    'Resolver casos e construir um argumento com conceito, decisão, evidência e limite.'
                ], lessons=lessons, questions=questions, flashcards=flashcards,
                references=references, essay=essay)
    (ROOT/'content/units/1.2.json').write_text(json.dumps(unit, ensure_ascii=False, indent=2)+'\n')
    entry.update(revision=2)
    catalog['revision'] = max(4, catalog['revision'])
    catalog['updatedAt'] = '2026-10-26'
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2)+'\n')
    print(f'Unidade 1.2 r2: {len(lessons)} lições, {len(questions)} questões, {len(flashcards)} cartões, {unit["estimatedMinutes"]} minutos sugeridos.')


if __name__ == '__main__':
    save()
