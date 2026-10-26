"""Unidade 1.3: conceitos como instrumentos de interpretação e ensino."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TITLE='Conceitos, categorias e conteúdos de geografia no Ensino Fundamental e Médio'
PAGE='https://github.com/emanoelb5-lgtm/ProfGeo/blob/main/docs/UNIDADE_1_3.md'


def text(title,body):return dict(type='text',title=title,body=body)
def call(title,body,warning=False):return dict(type='callout',title=title,body=body,tone='warning' if warning else 'tip')
def table(title,headers,rows):return dict(type='table',title=title,headers=headers,rows=rows)
def compare(title,a,at,b,bt):return dict(type='compare',title=title,left=dict(title=a,body=at),right=dict(title=b,body=bt))
def anim(kind,title,caption):return dict(type='animation',kind=kind,title=title,caption=caption)
def match(title,pairs):return dict(type='match',title=title,pairs=pairs)
def order(title,items):return dict(type='order',title=title,items=items)


def picture(filename,title,caption):
    sources=json.loads((ROOT/'content/media-sources.json').read_text())
    source=next(s for s in sources if s['filename']==filename)
    return dict(type='photo',src='media/'+filename,title=title,caption=caption,
                credit=f'{source["author"]} · {source["license"]} · origem e alterações nos créditos da unidade')


lessons=[]


def lesson(n,title,kicker,minutes,blocks,summary,practice):
    lessons.append(dict(id=f'l{n:02d}',title=title,kicker=kicker,minutes=minutes,
                        blocks=blocks,summary=summary,practice=practice))


lesson(1,'Conceito, categoria e conteúdo: para que servem?','Comece por um problema, depois dê nome às ferramentas',18,[
    text('A investigação que vai ligar a unidade','Na 1.1, você estudou concepções geográficas; na 1.2, os saberes que sustentam decisões de ensinar. Agora vamos perguntar como conceitos e conteúdos ajudam o estudante a construir uma explicação geográfica. O objetivo é usar as ideias em problemas, em vez de apenas repetir um vocabulário.\nA professora Lia, personagem fictícia, propõe investigar a Feira da Ponte. Produtores chegam por estradas e pelo rio; há um cais, uma praça e um armazém. Alguns trabalhadores querem mudar os usos da praça. Por que a feira funciona ali, quem participa de suas decisões e como suas conexões ultrapassam o município? A feira, os personagens, os mapas e os dados desse caso são inventados para estudo.'),
    text('Primeiro, distinga assunto e ferramenta','“Abastecimento de uma feira” pode ser um conteúdo: um recorte do que se vai estudar. Rede ajuda a interpretar conexões; território ajuda a perguntar quem controla usos e acessos; paisagem ajuda a investigar formas percebidas e suas transformações. São conceitos usados para organizar relações, não nomes adicionais para decorar.\nChamaremos de categorias os conceitos com papel amplo na organização da análise geográfica, como espaço, lugar, paisagem, território e região. Essa é uma convenção de estudo: autores e correntes podem atribuir sentidos e posições diferentes a esses termos. Não existe uma tabela única que separe definitivamente toda categoria de todo conceito.'),
    picture('u13-conceitos-conteudos.png','O conceito precisa participar do raciocínio','No exemplo da praça, o conteúdo é analisado com território. A aprendizagem aparece quando o aluno explica agentes, regras e efeitos sobre o acesso; copiar a definição não realiza sozinho esse trabalho.'),
    picture('belem-feira.jpg','Uma feira real para formular perguntas','Registro do Ver-o-Peso, em Belém, de Cayambe. A fotografia não representa a Feira da Ponte inventada. Observe formas, usos e circulação; não deduza renda, regras ou trajetórias individuais apenas pela imagem.'),
    compare('Um primeiro exemplo resolvido','Resposta que só identifica','“Isso é território porque existe uma praça.” A presença de uma forma espacial não explica qual relação o conceito destaca.','Resposta que usa o conceito','“Ao investigar quem define os horários e as permissões de uso da praça, analisamos relações de poder e acesso.” A pergunta explicita por que território contribui para o estudo.'),
    text('Os conceitos não disputam a posse do lugar','A feira pode ser investigada como paisagem, lugar, território e parte de uma região. Isso não significa que os termos sejam sinônimos. O espaço estudado é o mesmo; mudam o problema e as relações colocadas em primeiro plano. Uma fotografia também não pertence exclusivamente a um conceito: sua função depende da pergunta.\nAo longo da unidade, acompanhe quatro movimentos: entender a pergunta, explicar a ideia, examinar um caso resolvido e transferir o raciocínio. As lições finais mostram como trabalhar essas relações nos anos iniciais, nos anos finais e no Ensino Médio, sem transformar as etapas em listas isoladas.'),
    call('Verifique antes da prática','“Vou dar uma aula com mapas.” Isso define o conteúdo e a aprendizagem? Ainda precisamos saber o que será estudado e o que o estudante fará com a representação: localizar, comparar, explicar conexões ou analisar decisões. Recurso, conteúdo e objetivo têm funções diferentes.')
], 'Conteúdo é o recorte do que se estuda; conceitos ajudam a organizar e explicar relações. Categorias têm papel amplo na análise, com sentidos que dependem das abordagens. Aprender exige usar essas ferramentas em problemas.',match('Associe a escolha à sua função',[
    ['Estudar o abastecimento de uma feira.','Recorte de conteúdo.'],
    ['Usar território para examinar controle dos acessos.','Ferramenta conceitual de análise.'],
    ['Comparar um mapa e uma fotografia.','Uso de linguagens e fontes.'],
    ['Explicar como uma regra afeta os usos da praça.','Aprendizagem que pode ser examinada.']]))

lesson(2,'Espaço geográfico: relações que se fazem no tempo','As formas não explicam sozinhas o funcionamento',20,[
    text('O armazém permaneceu, mas a feira mudou','No caso fictício, o mesmo armazém passou a receber mercadorias que antes eram vendidas diretamente no cais. A construção continua, mas trabalho, circulação e decisões mudaram. Se Lia pedir apenas uma lista de objetos, a turma não explicará essa transformação.\nEspaço geográfico não é um recipiente vazio onde as coisas simplesmente acontecem. Nesta leitura, ele se constitui nas relações entre sociedade e natureza, com técnicas, trabalho, usos e ações historicamente produzidos. Outras concepções podem construir esse objeto de modos diferentes, como você viu na 1.1.'),
    text('Uma entrada em Milton Santos','A relação entre sistemas de objetos e sistemas de ações, discutida por Milton Santos, ajuda a ler o caso. Cais, estrada e armazém não funcionam isolados: transportar, negociar, regular e trabalhar dão sentido aos seus usos. As condições materiais também oferecem possibilidades e limites às ações.\nEssa relação não autoriza opor objetos “sem sociedade” a ações “sem materialidade”. A estrada resulta de trabalho e decisões; a circulação depende de formas técnicas, condições naturais e organização social. O foco é compreender sua articulação.'),
    picture('u13-objetos-acoes.png','Leia as duas direções da relação','O esquema usa elementos da feira fictícia. As setas não indicam uma causa única: mostram que formas e ações precisam ser analisadas em conjunto e em sua história.'),
    compare('Caso resolvido: a mudança de função','Informação inicial','“O armazém continua no mesmo ponto, logo o espaço não mudou.” A frase toma a permanência de uma forma como prova de permanência de todas as relações.','Explicação ampliada','“O armazém permanece, mas recebe novos fluxos e organiza outros usos. Para explicar a mudança, precisamos investigar técnicas, agentes e decisões.” Forma e funcionamento são relacionados.'),
    text('O tempo participa da explicação','Uma construção antiga pode continuar sendo usada em um circuito recente. Marcas de momentos diferentes coexistem, e a função de uma forma pode mudar. Isso ajuda a evitar a ideia de que todas as partes do espaço pertencem a um único tempo ou a uma mesma condição técnica.\nPara estudar a transformação, Lia pode comparar registros de épocas identificadas, relatos e documentos. Uma foto sem data e outra com enquadramento diferente não formam automaticamente uma sequência de antes e depois. As fontes precisam sustentar a relação temporal que se pretende afirmar.'),
    table('Do objeto à relação espacial',['Observação','Pergunta que amplia a análise'],[
        ['Existe um cais.','Que transportes o utilizam e como se conecta aos demais trajetos?'],
        ['Há um armazém.','Quem decide seu uso, o que circula e como o trabalho é organizado?'],
        ['Uma rua foi modificada.','Como a mudança se relaciona a circulação, atividades e condições ambientais?']]),
    call('Aplique em outro contexto','Uma escola instalada no mesmo prédio pode mudar horários, público atendido e conexões com a comunidade. A permanência da edificação informa uma continuidade; não demonstra que todas as relações espaciais permaneceram iguais.'),
    text('Consequência para ensinar','Estudar espaço geográfico envolve ensinar a relacionar formas, ações e processos. Identificar elementos pode iniciar a investigação, mas o avanço aparece quando o aluno os usa em uma explicação. Na próxima lição, vamos examinar o que pode ser percebido na paisagem e o que ainda precisa de outras fontes.')
], 'Espaço geográfico é analisado por relações historicamente produzidas. A articulação de objetos e ações ajuda a explicar por que a permanência de uma forma não significa permanência de todos os usos e processos.',order('Reconstrua a explicação sobre o armazém',[
    'Identificar a forma material que permanece.',
    'Comparar usos, ações e conexões em momentos identificados.',
    'Investigar agentes, técnicas e decisões relacionados à mudança.',
    'Explicar a articulação entre permanências e transformações.' ]))

lesson(3,'Paisagem: perceber formas, investigar processos','O que a aparência permite e o que não permite concluir?',19,[
    text('Comece pelo que pode ser observado','Lia pede que a turma observe o cais e a praça: construções, vegetação, água, materiais, circulação e sinais dos usos. Em uma experiência presencial, sons, odores e outros aspectos perceptíveis também podem participar da leitura. Uma fotografia oferece apenas um registro visual, produzido de um ponto de vista e em um momento.\nPaisagem permite investigar formas e marcas perceptíveis da relação entre sociedade e natureza. Não se restringe a uma vista bonita, a uma área sem pessoas ou ao campo. Uma fábrica, um bairro e uma feira também podem ser estudados por suas paisagens.'),
    picture('ver-o-peso.jpg','Observar sem inventar o que a fonte não mostra','Complexo do Ver-o-Peso, de Fabio Gomes. Procure elementos naturais e construídos e formule perguntas sobre seus usos. Esta imagem e a foto anterior não constituem, por si só, uma comparação temporal controlada.'),
    text('Da descrição à interpretação','Descrever é reconhecer elementos e relações visíveis; explicar exige investigar processos que os produziram e lhes dão sentido. Ver um galpão fechado não basta para saber por que fechou. Podem ser necessárias informações sobre atividade, momento do registro, decisões e condições de funcionamento.\nA aparência tem valor como evidência, mas seu alcance precisa ser delimitado. Também não é possível inferir a renda de uma família, a identidade de uma pessoa ou uma situação de risco individual apenas pela forma da moradia em uma foto.'),
    compare('Uma mudança de paisagem, resolvida','Enunciado','Duas fotografias datadas e comparáveis mostram que árvores foram substituídas por pavimento na praça fictícia. O que se pode afirmar de início?','Raciocínio','É possível reconhecer uma transformação nas formas registradas. Para explicar causas e efeitos, Lia precisa investigar o projeto, os usos e condições físicas, sem deduzir todos os resultados da aparência.'),
    table('Uma fonte, diferentes níveis de afirmação',['Afirmação','Avaliação do alcance'],[
        ['A fotografia mostra uma área pavimentada.','Observação compatível com o registro, se a forma estiver visível.'],
        ['A pavimentação foi realizada por tal motivo.','Exige fonte sobre decisão, contexto e agentes.'],
        ['Todas as pessoas melhoraram de vida após a obra.','A foto não sustenta essa generalização sobre experiências e condições sociais.']]),
    text('A paisagem guarda marcas de tempos diferentes','Um mercado antigo pode coexistir com estruturas recentes de transporte. A leitura da paisagem permite levantar perguntas sobre essas permanências e mudanças; a interpretação histórica precisa confrontar registros. O antigo não é automaticamente atrasado, e o novo não representa necessariamente melhoria para todos.\nNo ensino, comparar paisagens com critérios pode desenvolver descrição, comparação e explicação. Um exercício que só pede “natural ou humanizada” pode servir a uma distinção inicial, mas precisa ser ampliado para evitar uma separação rígida entre natureza e sociedade.'),
    call('Transfira a leitura','Em uma área agrícola, a forma de um plantio pode sugerir questões sobre uso da terra e trabalho. Para afirmar quem possui a terra ou como o trabalho é contratado, serão necessárias outras fontes. Você aplicou o mesmo cuidado de evidência em outra paisagem.'),
    text('Ponte para o lugar','Duas pessoas podem observar a mesma praça e atribuir sentidos diferentes a ela. A paisagem oferece uma entrada; compreender experiências, vínculos e significados pede outra ênfase. É o problema da próxima lição.')
], 'Paisagem não é sinônimo de beleza nem de natureza sem sociedade. Sua leitura reconhece formas e marcas perceptíveis; explicar processos, decisões e experiências exige confrontar outras fontes.',match('Associe a afirmação ao cuidado necessário',[
    ['Reconhecer construções e vegetação visíveis.','Descrever aspectos do registro.'],
    ['Explicar por que uma construção mudou de uso.','Investigar processos e decisões com outras fontes.'],
    ['Comparar fotografias como antes e depois.','Conferir datas, enquadramento e condições de comparação.'],
    ['Afirmar a renda dos moradores pela aparência da casa.','Reconhecer uma inferência que a imagem não sustenta.']]))

lesson(4,'Lugar: experiência, vínculos e conexões','Um lugar não precisa ser vivido do mesmo modo por todos',18,[
    text('A praça tem sentidos diferentes','Na Feira da Ponte, uma trabalhadora associa a praça à sua renda; um estudante, aos encontros; uma pessoa com mobilidade reduzida relata barreiras à circulação. São falas fictícias. Elas mostram que partilhar uma localização não torna as experiências idênticas.\nNesta entrada, lugar ajuda a compreender a experiência e os significados construídos nas relações com o espaço. A perspectiva experiencial de Yi-Fu Tuan é uma referência complementar. Vínculo não significa apenas afeição: memória, desconforto, conflito e sensação de exclusão podem coexistir.'),
    call('Antecipe a comparação','Antes da cena, pense: que perguntas você faria a alguém que trabalha na praça e a alguém que apenas a atravessa? Evite decidir a resposta antes de ouvir a experiência.'),
    anim('lived','Um espaço vivido por três pessoas','Use “Pessoa 1”, “Pessoa 2” e “Pessoa 3”. Os relatos da cena são fictícios. Observe como trabalho, encontro e memória mudam o sentido atribuído ao lugar; não generalize cada fala para um grupo inteiro.'),
    text('Leia a diferença como problema de investigação','As personagens destacam relações que uma descrição de formas não esgota. Um banco pode ser apoio ao trabalho, ponto de encontro ou uma barreira no trajeto. Para interpretar essas experiências, Lia pode comparar narrativas e condições materiais, preservando suas diferenças.\nO relato não é uma prova de que todas as pessoas viveram o mesmo. Ouvir uma estudante do campo não permite afirmar como todos os estudantes do campo pensam. Valorizar conhecimentos e experiências inclui reconhecer sua diversidade.'),
    compare('Lugar e localização não são equivalentes','Informação de posição','“A praça está ao lado do cais.” Localiza uma relação entre formas, importante para situar o estudo.','Questão de experiência','“Como a ligação com o cais participa da rotina e dos significados da praça para os trabalhadores?” Investiga relações vividas, além da posição.'),
    text('O lugar não é uma ilha','A praça pode ser atravessada por decisões e circuitos de fora do município. Preços, meios de comunicação, transportes e relações de trabalho conectam o vivido a processos amplos. Estudar lugar não exige fechar a análise no que é próximo ou pequeno.\nA escala da experiência não equivale a uma proibição de investigar o mundo. Uma criança pode partir de um produto que conhece e perguntar de onde vem. Um estudante do Ensino Médio pode aprofundar as relações entre aquele lugar e cadeias de produção.'),
    table('Como o conceito participa da aula',['Produção inicial','Intervenção que amplia'],[
        ['Listar lembranças da praça.','Comparar sentidos e perguntar por que diferem.'],
        ['Dizer que todos gostam do mesmo lugar.','Confrontar experiências sem transformar uma fala em regra geral.'],
        ['Associar lugar apenas ao bairro.','Investigar conexões do vivido com processos em outras escalas.']]),
    call('Exemplo resolvido','“O lugar só existe quando há sentimentos positivos.” A frase reduz a diversidade da experiência. Um lugar também pode ser vivido por medo, conflito ou desconforto. A análise precisa compreender como esses sentidos são produzidos.'),
    text('Ponte para território','Na praça, as pessoas não apenas atribuem significados: também encontram regras e formas de controle. Perguntar quem decide esses usos leva à análise de território, sem apagar a dimensão da experiência.')
], 'Lugar ajuda a interpretar experiências, vínculos e significados, que podem ser diversos e conflitivos. Ele não se reduz à localização, à afeição ou a uma pequena área isolada das conexões com o mundo.',match('Relacione a pergunta ao foco',[
    ['Onde a praça fica em relação ao cais?','Relação de localização.'],
    ['Como a praça participa das memórias e rotinas?','Experiência e significado do lugar.'],
    ['Todos os trabalhadores vivem a praça da mesma maneira?','Diversidade que precisa ser investigada.'],
    ['Como decisões externas mudam a rotina local?','Conexão do lugar com processos mais amplos.']]))

lesson(5,'Território: poder, apropriação e acesso','Quem decide o que pode acontecer aqui?',21,[
    text('Uma mudança de regra cria outra pergunta','Na situação fictícia, uma proposta reserva parte da praça para armazenar mercadorias. Trabalhadores, moradores e responsáveis pela gestão discordam sobre horários e usos. O problema não se explica apenas pelo tamanho da área: é preciso analisar agentes, interesses e formas de controle.\nTerritório coloca em primeiro plano relações de poder na apropriação e no controle do espaço. Na contribuição de Rogério Haesbaert, a discussão abrange dimensões materiais e simbólicas. Não se restringe à superfície de um país nem se confunde automaticamente com propriedade legal.'),
    text('Distinguir controle e título de propriedade','Uma área pode ter propriedade formal definida e, ainda assim, usos disputados ou regulados por outros agentes. É necessário investigar quem estabelece normas, quem consegue fazê-las valer e como diferentes pessoas participam ou são excluídas.\nIsso não elimina a importância do Estado, dos limites e das normas jurídicas. Mostra que a análise territorial pode envolver relações em diferentes escalas, com atores e formas de poder que não se resumem ao mapa de países.'),
    table('No caso da praça, investigue relações',['Questão','Fonte ou evidência que poderia ajudar'],[
        ['Quem define os horários de uso?','Regras, registros de decisões e entrevistas contextualizadas.'],
        ['Quem consegue utilizar a área?','Observação dos usos, condições de acesso e relatos diversos.'],
        ['Que significados legitimam a disputa?','Argumentos sobre trabalho, memória, segurança e pertencimento.'],
        ['Como o controle muda ao longo do dia?','Comparação de horários, atividades e normas efetivamente praticadas.']]),
    compare('Caso resolvido: o muro','Afirmação inicial','“Sem muro não existe território.” A frase toma uma forma física como condição universal de uma relação de poder.','Análise','O controle pode operar por regras, horários, permissões e outras relações sem um muro visível. O estudo precisa identificar agentes e práticas que organizam o acesso.'),
    text('Material e simbólico podem se articular','O espaço usado para trabalhar também pode ser reconhecido como referência de identidade coletiva. Esse vínculo pode participar de disputas sobre usos e permanências. A dimensão simbólica não é um adorno separado das condições materiais, e o controle material não explica sozinho todos os significados.\nDiferentes territorialidades podem coexistir ou entrar em conflito. Uma pessoa também pode participar de relações com vários territórios. Isso não significa que todos tenham a mesma possibilidade de circulação, controle ou pertencimento; essas condições precisam ser analisadas.'),
    call('Transfira para o espaço rural','Em um conflito fictício sobre acesso a uma estrada que atravessa uma área produtiva, perguntar apenas onde a via passa é insuficiente. Investigue quem controla a passagem, quais normas e práticas participam e como isso afeta trabalho e circulação. Não deduza a situação jurídica sem documentos.'),
    text('O que avaliar no ensino?','Se a aprendizagem pretendida é usar território, pedir o nome dos agentes pode ser um início. Uma produção mais forte explica como uma regra ou uma prática expressa poder e afeta os usos do espaço. A análise deve examinar fontes e argumentos, sem exigir que o aluno concorde com a preferência do professor.\nNa próxima lição, a pergunta mudará: como construir recortes para compreender diferenças e articulações entre áreas? Território e região podem dialogar, mas não resolvem exatamente o mesmo problema.')
], 'Território destaca relações de poder, apropriação e controle do espaço, em dimensões materiais e simbólicas. Limites estatais e propriedade importam, mas não esgotam a análise. É preciso identificar agentes, práticas e efeitos sobre o acesso.',order('Organize uma análise territorial da praça',[
    'Identificar o uso ou acesso que está em questão.',
    'Investigar agentes, regras e práticas de controle.',
    'Confrontar interesses, significados e evidências dos usos.',
    'Explicar como essas relações organizam o espaço e afetam os participantes.' ]))

lesson(6,'Região: recortar com critérios e explicar diferenças','Por que dois mapas podem organizar as mesmas áreas de outro modo?',20,[
    text('A feira se relaciona com quais áreas?','Lia quer estudar de onde chegam os produtos. Um mapa de relevo mostra semelhanças entre terrenos; outro organiza localidades pelas conexões com mercados. Os recortes podem ser diferentes porque respondem a problemas e critérios distintos.\nRegião ajuda a compreender diferenciações e articulações do espaço a partir de um recorte construído e justificado. Regionalizar é estabelecer esses recortes com critérios. Não é apenas dividir um mapa em partes de tamanho parecido nem descobrir uma única separação natural válida para qualquer finalidade.'),
    picture('u13-regionalizacoes.png','A mesma base, duas perguntas','No esquema fictício, A a F são localidades. À esquerda, A, B e C compartilham a classe planície; D, E e F, colinas. À direita, A, D e E se conectam principalmente ao mercado X; B, C e F, ao Y. As cores representam os critérios, não dados de municípios reais.'),
    text('Resolva a aparente contradição','A e B pertencem ao mesmo grupo no critério do relevo, mas a grupos diferentes no critério das conexões. Não há contradição automática: os mapas selecionam relações diferentes. É necessário examinar dados, critérios e finalidade antes de julgar um deles como errado.\nIsso também não torna qualquer divisão igualmente adequada. Para estudar abastecimento, um recorte por fluxos pode revelar relações que uma classificação de relevo não foi feita para mostrar. A pertinência depende da pergunta e da consistência das informações.'),
    compare('Duas maneiras de construir o recorte','Ênfase em semelhanças','Agrupar áreas por características selecionadas, como determinada condição do relevo, pode ajudar a comparar diferenciações. A diversidade interna não desaparece.','Ênfase em articulações','Organizar recortes por conexões, fluxos e centralidades pode ajudar a interpretar como áreas se relacionam. Proximidade física e conexão funcional não são sempre equivalentes.'),
    text('Um exemplo institucional situado','A Divisão Regional do Brasil de 2017, do IBGE, usa Regiões Geográficas Imediatas e Intermediárias e considera articulações da rede urbana. É uma referência para compreender um trabalho de regionalização, não um convite a memorizar o mapa sem seus critérios. Aqui não reproduzimos limites ou resultados atuais de cada região.\nOutros recortes podem atender a planejamento, análise ambiental ou interpretação econômica. As divisões têm contexto, finalidade e efeitos sobre a leitura dos dados. Por isso, a legenda e o nome da região não substituem a explicação do critério.'),
    table('Leia um mapa regional com perguntas',['Pergunta','Cuidado de interpretação'],[
        ['Qual é o fenômeno estudado?','Não usar um recorte como resposta para todos os problemas.'],
        ['Que critério organiza as áreas?','Distinguir semelhança, conexão, limite administrativo e outras escolhas.'],
        ['Que informação foi usada e de quando?','Verificar alcance, contexto e comparabilidade dos dados.'],
        ['O que varia dentro da região?','Evitar transformar o grupo em área homogênea em todos os aspectos.']]),
    call('No ensino, troque a tarefa mecânica por uma justificativa','Colorir um recorte pode apoiar sua identificação. Para aprender a regionalizar, a turma precisa também aplicar ou comparar critérios e explicar o que cada divisão permite compreender. A cor organiza a representação; o critério sustenta o argumento.'),
    text('Ponte para redes e escalas','O recorte por mercados depende de conexões. Agora vamos analisar como pontos e fluxos formam redes e por que mudar a escala de análise altera as relações que precisamos investigar.')
], 'Região é um recorte justificado para interpretar diferenciações e articulações. Regionalizações variam com problema, critério, dados e contexto. Recortes diferentes não são automaticamente contraditórios nem igualmente adequados para toda pergunta.',match('Compare os recortes do esquema',[
    ['A e B no mapa do relevo.','Mesmo grupo: planície.'],
    ['A e B no mapa dos mercados.','Grupos diferentes: X e Y.'],
    ['A, D e E no critério das conexões.','Mesmo grupo de conexão principal: mercado X.'],
    ['Escolher o recorte mais pertinente.','Relacionar a pergunta aos critérios e aos dados.']]))

lesson(7,'Redes e escalas: conectar o lugar ao mundo','As relações não terminam no limite do mapa',20,[
    text('Siga um produto além da banca','Um produto da feira fictícia pode passar por local de produção, transporte, armazenamento e venda. O percurso envolve pontos conectados e fluxos de mercadorias, pessoas, dinheiro e informações. Rede ajuda a analisar essas conexões e sua organização.\nNão basta desenhar linhas entre todos os pontos: é preciso perguntar o que circula, por quais caminhos, em que condições e com que centralidades. Uma ligação existente no mapa pode ter frequência, custo ou capacidade diferentes de outra.'),
    text('Escala de análise é uma escolha do problema','Na praça, observamos usos e horários. No município, podemos comparar distribuição de serviços e conexões. Em uma rede mais ampla, investigamos fornecedores, mercados e decisões que ultrapassam o município. Mudar a escala de análise amplia ou reorganiza as relações consideradas; não é apenas aumentar a imagem na tela.\nO que se passa perto pode depender de processos distantes. Por isso, trabalhar diferentes escalas não exige terminar todos os estudos do bairro antes de falar do mundo. É possível articular recortes desde que a pergunta e as fontes orientem a passagem.'),
    call('Observe o que cada recorte revela','Antes da cena, preveja uma relação que o recorte da comunidade pode mostrar e outra que exige investigar conexões regionais. Depois use os três controles e confira o que ficou visível e o que permaneceu fora da explicação.'),
    anim('scale','Comunidade, município e rede regional','A cena existente trabalha acessos e circulação, com os controles “Comunidade”, “Município” e “Rede regional”. Use-a como comparação para pensar as conexões da feira. Ela não representa um mapa real da Feira da Ponte.'),
    text('Não confunda com escala cartográfica','Escala cartográfica expressa uma relação de redução entre representação e realidade. Por exemplo, 1:10.000 reduz menos e é uma escala maior que 1:100.000. Já a escala de análise se refere ao recorte e às relações usados para compreender um problema. As duas podem dialogar, mas não são a mesma definição.\nUm mapa ampliado na tela não passa, por esse gesto, a explicar decisões em outras escalas. Para analisar uma rede regional, podem ser necessárias fontes sobre conexões que o mapa local não contém.'),
    compare('Caso resolvido: dois pontos próximos','Conclusão precipitada','“Duas localidades próximas terão a mesma conexão principal.” A afirmação troca proximidade física por funcionamento da rede.','Análise','Rotas, serviços e condições podem orientar conexões diferentes. Precisamos examinar fluxos e trajetos, não deduzir a articulação apenas pela distância em linha reta.'),
    table('Qual pergunta exige quais relações?',['Pergunta','Recorte e informações úteis'],[
        ['Quem consegue usar a praça em certo horário?','Usos e controle no local, relacionados às normas pertinentes.'],
        ['Como comunidades se conectam ao mercado?','Rede de trajetos, frequência e condições de circulação.'],
        ['Como uma decisão externa altera o abastecimento?','Agentes e conexões que articulam o local a outras escalas.']]),
    call('Transfira para o ensino','Um bom exercício pode pedir que o aluno explique que relação desaparece quando recortamos só a praça. A resposta precisa indicar uma conexão concreta, como a chegada de mercadorias, e uma fonte para investigá-la. Dizer apenas “o global influencia” ainda deixa a explicação incompleta.')
], 'Redes articulam pontos e fluxos com condições e centralidades desiguais. Escala de análise organiza relações de um problema; escala cartográfica indica redução da representação. Proximidade e conexão não são equivalentes.',match('Associe o termo ao seu papel',[
    ['Pontos articulados por fluxos de produtos e informações.','Rede geográfica.'],
    ['Investigar conexões entre praça, município e fornecedores.','Articulação de escalas de análise.'],
    ['Relacionar um centímetro do mapa à distância real.','Escala cartográfica.'],
    ['Supor que os pontos mais próximos têm os mesmos fluxos.','Generalização que precisa ser confrontada com dados.']]))

lesson(8,'Natureza e sociedade: construir uma explicação integrada','Chuva, relevo e infraestrutura entram em relação',21,[
    text('A chuva volta ao problema, com outra pergunta','Depois de uma chuva, o trajeto até a feira fictícia apresenta dificuldades. Lia quer trabalhar conteúdos físico-naturais sem separar sua análise da organização social do espaço. Uma frase como “choveu, então todos foram igualmente afetados” precisa ser examinada.\nA presença do evento não informa sozinha seus efeitos. Relevo, características do solo, cobertura da superfície, drenagem, ocupação e condições de proteção podem participar da explicação. É necessário investigar como se combinam, em vez de atribuir tudo a uma causa isolada.'),
    text('Tempo atmosférico e clima não são sinônimos','Tempo atmosférico se refere às condições da atmosfera em um momento ou período considerado, como uma tarde chuvosa. Clima envolve padrões e variações caracterizados em uma duração longa. Uma chuva observada não basta para demonstrar o padrão climático de uma área ou uma mudança desse padrão.\nNo ensino, Lia pode confrontar um registro de um dia com séries de informações e perguntar que tipo de afirmação cada fonte permite. O mesmo cuidado vale para relevo e vegetação: reconhecer uma forma ou uma cobertura é diferente de explicar os processos e relações que a constituem.'),
    picture('u12-rio-guama.jpg','Uma imagem inicia perguntas; o diagnóstico exige outras fontes','Rio Guamá visto do campus da UFPA em 2019. A foto situa um ambiente real, mas não oferece, por si só, dados para diagnosticar risco, cheias ou condições de uma comunidade. O problema da feira permanece fictício.'),
    call('Preveja antes da comparação','Se a chuva for a mesma e as condições de acesso forem diferentes, os efeitos precisam ser iguais? Use os dois controles da cena e procure qual condição foi alterada. A cena não fornece previsão ou cálculo de risco.'),
    anim('inequality','Condições materiais participam dos efeitos','Compare “Acesso vulnerável” e “Infraestrutura melhorada”. O evento natural continua presente. Observe como a condição do trajeto modifica a situação representada; não conclua que qualquer obra elimina todos os problemas.'),
    picture('u13-natureza-sociedade.png','Uma relação que precisa ser investigada','Processo físico, exposição e vulnerabilidade ajudam a organizar perguntas sobre efeitos desiguais. O esquema é conceitual e não calcula risco nem descreve uma situação real específica.'),
    compare('Resolução: da frase geral à relação','Frase inicial','“As pessoas próximas ao rio terão o mesmo problema porque vivem no mesmo ambiente.” A frase transforma uma condição natural em destino social uniforme.','Explicação','Precisamos comparar condições físicas, usos, técnicas e acesso à proteção. Uma condição natural participa do problema, mas não determina sozinha a experiência e os efeitos para todos.'),
    text('O conteúdo precisa servir à interpretação','Ao ensinar chuva, solos, relevo ou uso da terra, Lia pode pedir que os alunos relacionem processos com informações do caso e indiquem o que ainda não sabem. Decorar uma lista de fatores sem mostrar sua relação conservaria a fragmentação.\nUma proposta de intervenção também exige julgamento: melhorar um acesso pode ter efeitos sobre outros usos ou trajetos. Para discutir alternativas, são necessárias fontes e critérios. Nesta unidade, o avanço de aprendizagem é construir uma explicação integrada, não emitir um diagnóstico técnico sobre um local real.')
], 'Conteúdos físico-naturais e sociais se articulam na explicação do espaço. Um evento não determina sozinho efeitos iguais; tempo atmosférico e clima pedem escalas temporais e evidências diferentes.',order('Construa a explicação do caso da chuva',[
    'Identificar o evento e o efeito que se pretende explicar.',
    'Comparar condições físicas, ocupação, acesso e proteção.',
    'Relacionar essas condições sem transformar um fator em causa única.',
    'Delimitar o que as fontes sustentam e o que ainda exige investigação.' ]))

lesson(9,'Campo, cidade, produção e população','Transforme temas em relações geográficas',22,[
    text('A mercadoria liga conteúdos que pareciam separados','Na feira fictícia, um alimento conecta produção rural, transporte, trabalho e consumo. Campo e cidade participam de relações de abastecimento, serviços, renda e circulação. Isso ajuda a estudar conteúdos sem apresentá-los como capítulos que nunca se encontram.\nCampo não é sinônimo de agricultura, nem cidade é um espaço sem natureza. Há usos e atividades diversos. Também não é adequado explicar o campo como atraso e a cidade como progresso automático: técnicas, condições de trabalho e acesso a serviços precisam ser investigados em sua diversidade.'),
    text('Agrícola e agrário destacam perguntas diferentes','Uma questão agrícola pode focalizar cultivo, produção e suas técnicas. A análise agrária pode destacar relações de acesso e uso da terra, trabalho e poder. Os problemas dialogam: quem pode produzir e em que condições participa do que se produz e de como a mercadoria circula.\nNo caso da feira, contar produtos vendidos não revela sozinho a situação dos trabalhadores ou a distribuição da terra. Lia precisa adequar as fontes ao tipo de relação que pretende explicar. Não deve transformar uma medida de produção em retrato completo da vida no campo.'),
    compare('Produção e rede, em um caso resolvido','Observação','O produto chega à banca por transporte fluvial e depois segue para outro mercado. A venda na praça é uma parte do circuito.','Explicação que amplia','É necessário investigar conexões entre locais, trabalho, armazenamento e decisões. Rede e escalas ajudam a relacionar produção, circulação e consumo, sem presumir que todos recebam os mesmos benefícios.'),
    text('Um conteúdo populacional também exige distinguir medidas','Lia apresenta dados hipotéticos de duas áreas. A tem 2.000 habitantes em 10 km²; B tem 1.000 habitantes em 2 km². Qual tem maior população? A. Qual tem maior densidade demográfica? É necessário dividir a população pela área: A tem 200 habitantes por km²; B, 500.\nPopulação total e densidade respondem a perguntas diferentes. Os valores médios não mostram como as pessoas se distribuem dentro de cada área nem explicam, sozinhos, suas condições de vida. Uma maior densidade não prova automaticamente menor renda ou pior acesso.'),
    table('Dados hipotéticos: calcule e interprete',['Área','Habitantes','Área em km²','Densidade média'],[
        ['A','2.000','10','200 hab./km²'],
        ['B','1.000','2','500 hab./km²']]),
    text('Como ligar o dado ao problema da feira?','Uma concentração de moradores pode levantar perguntas sobre demanda e distribuição dos pontos de venda. Para explicar o abastecimento, Lia ainda precisará estudar conexões, horários, capacidade e condições de acesso. A tabela é uma fonte; o conceito organiza o que ela pode contribuir para o problema.\nA mesma orientação vale para urbanização e mobilidade: localizar crescimento ou deslocamentos é relevante, mas explicar processos pede relações históricas, agentes e fontes. Conteúdos podem ser articulados por um problema, conservando a precisão de cada um.'),
    call('Transfira o raciocínio','“A tem mais habitantes, então é necessariamente mais densamente povoada.” O erro é usar um total como se já fosse uma relação com a área. Reconheça a pergunta, escolha a medida e só depois interprete o resultado. É o mesmo cuidado que você aprendeu ao distinguir distância e tempo na 1.2.'),
    text('Ponte para o raciocínio geográfico','Até aqui, você localizou, comparou, conectou e explicou diferenças. Na próxima lição, vamos explicitar essas operações para que o estudante aprenda a pensar com o conteúdo, em vez de apenas receber uma informação pronta.')
], 'Campo e cidade se articulam por produção, circulação, serviços e trabalho. Temas agrícolas, agrários e populacionais pedem perguntas e fontes precisas. População total e densidade não são equivalentes, e médias não explicam sozinhas condições de vida.',match('Associe o problema à relação a investigar',[
    ['Como um alimento chega aos mercados?','Produção, circulação, consumo e conexões.'],
    ['Quem acessa e controla a terra para produzir?','Relações agrárias de uso, trabalho e poder.'],
    ['Quantas pessoas vivem na área?','População total.'],
    ['Como o total se relaciona à superfície?','Densidade demográfica média.']]))

lesson(10,'Pensamento espacial e raciocínio geográfico','Use operações para construir a explicação',22,[
    text('Você já começou a fazer esse trabalho','Para entender a feira, localizou pontos, comparou usos, examinou diferenças e procurou conexões. Essas operações não são um apêndice ao conteúdo: participam da forma de construir sua interpretação. Dizer “a feira é importante” oferece uma conclusão; mostrar onde, como se articula e para quem funciona permite começar a sustentá-la.\nPensamento espacial envolve conceitos espaciais, representações e modos de raciocinar sobre relações. Não pertence exclusivamente à Geografia. O raciocínio geográfico mobiliza essas possibilidades para interpretar problemas de organização espacial e relações entre sociedade e natureza.'),
    text('Princípios como perguntas de trabalho','A seção de Geografia do Ensino Fundamental na BNCC de 2018 apresenta analogia, conexão, diferenciação, distribuição, extensão, localização e ordem. Aqui vamos estudá-los por perguntas autorais aplicadas à feira, sem copiar suas descrições como uma lista a memorizar.\nOs princípios se articulam e não devem ser identificados apenas por uma palavra solta. “Onde” pode iniciar uma localização; a tarefa precisa mostrar quais relações serão construídas com essa informação.'),
    table('Transforme o princípio em pergunta',['Princípio','Pergunta aplicada ao caso fictício'],[
        ['Localização','Onde ficam a feira e as conexões que permitem alcançá-la?'],
        ['Distribuição','Como os pontos de venda e os acessos se repartem na área?'],
        ['Extensão','Até onde se manifesta o fenômeno que estamos delimitando?'],
        ['Analogia','Que semelhanças ajudam a comparar essa feira com outra?'],
        ['Diferenciação','Que diferenças entre áreas precisam ser explicadas?'],
        ['Conexão','Como produção, transporte e venda se relacionam?'],
        ['Ordem','Como regras e relações sociais participam do arranjo espacial?']]),
    call('Mude a pergunta e observe','Na cena, experimente “Descrever”, “Medir padrões”, “Investigar poder” e “Ouvir experiências”. Identifique que fonte adicional cada pergunta exigiria. Os quatro controles não esgotam os conceitos nem substituem a explicação dos princípios.'),
    anim('lenses','Uma cena, diferentes relações em foco','Observe como a pergunta orienta o que investigar. Descrever formas pode ajudar a ler a paisagem; investigar controle contribui para analisar território; ouvir experiências amplia a análise de lugar. O recurso, sozinho, não determina a concepção ou o conceito usado.'),
    compare('Caso resolvido: do ponto ao circuito','Resposta inicial','“O mercado fica ao lado do cais.” Situa uma relação de localização. Ainda não explica o funcionamento do abastecimento.','Resposta ampliada','“A proximidade do cais participa da conexão com transportes, mas precisamos examinar trajetos, frequência e organização da venda.” A localização se articula a conexões e condições.'),
    text('O mapa precisa participar do raciocínio','Uma representação pode apoiar orientação, comparação e interpretação, mas copiar seus nomes não demonstra todas essas aprendizagens. Também não basta desenhar setas sem explicar o que representam. A tarefa deve exigir relações e permitir verificar como o aluno as construiu.\nAs próximas três lições mostram uma progressão possível no trabalho escolar. As operações aparecem em diferentes etapas; mudam apoios, fontes, complexidade das relações e autonomia. Não há uma idade a partir da qual se pode finalmente começar a pensar geograficamente.')
], 'O raciocínio geográfico se desenvolve ao localizar, comparar, conectar e explicar relações com fontes e representações. Os princípios orientam perguntas articuladas; não se resumem a reconhecer palavras ou copiar mapas.',match('Associe a pergunta ao princípio em destaque',[
    ['Como os pontos de venda se repartem pela área?','Distribuição.'],
    ['Até onde o fenômeno delimitado ocorre?','Extensão.'],
    ['Como transporte e abastecimento se articulam?','Conexão.'],
    ['Que diferenças aparecem entre as áreas?','Diferenciação.']]))

lesson(11,'Anos iniciais: ler, representar e comparar o vivido','Uma criança já pode investigar relações com apoio',20,[
    text('A situação próxima oferece perguntas, não um limite','Lia planeja uma proposta para os anos iniciais do Ensino Fundamental: como um alimento conhecido chega a um ponto de venda? Fotos, embalagens, desenhos e relatos selecionados podem ajudar a formular e comparar ideias. A contribuição de Helena Copetti Callai destaca a leitura do mundo e do espaço vivido na aprendizagem geográfica desde o início da escolarização.\nPartir do vivido não significa fechar a criança em família, escola e bairro, esperando concluir cada círculo antes de perguntar sobre relações mais amplas. Um produto presente na rotina pode conectar lugares diferentes. A mediação e a escolha das fontes tornam o problema acessível.'),
    text('Uma sequência possível, explicada','Lia apresenta duas imagens e pede que as crianças indiquem o que reconhecem e o que querem saber. Em seguida, organiza informações simples sobre uma origem e um trajeto fictícios. A turma representa pontos de referência e usa uma legenda combinada. Depois, compara os desenhos e explica como o alimento circulou.\nDesenhar não é um fim em si: permite discutir posição, referência, conexão e representação. Lia precisa explicitar que o desenho é uma maneira de representar o percurso, e que uma legenda ajuda outra pessoa a compreendê-lo.'),
    compare('Exemplo resolvido: direita de quem?','Dificuldade','Uma criança diz “a feira fica à direita”, mas outra observa a cena de frente e aponta para o lado oposto.','Mediação','Lia estabelece um ponto de referência e pede que expliquem de onde estão olhando. A divergência vira oportunidade de trabalhar orientação, em vez de classificar uma fala isolada como incapacidade.'),
    table('A representação tem uma finalidade',['Tarefa','Relação trabalhada','Evidência possível'],[
        ['Marcar escola, praça e feira com símbolos.','Localização relativa e legenda.','Outra pessoa reconhece os símbolos com a legenda.'],
        ['Comparar duas formas de chegar.','Trajeto, referência e conexão.','A criança explica um percurso e uma diferença.'],
        ['Investigar a origem de um produto conhecido.','Relação entre vivido e outros lugares.','A criança reconhece uma conexão com apoio das fontes.']]),
    text('Conceito aparece no uso, mesmo antes da definição completa','Uma criança pode começar a pensar lugar ao comparar vivências ou paisagem ao reconhecer e discutir transformações. O professor ajusta a linguagem e o suporte, preservando o sentido da relação. Exigir a repetição de uma definição abstrata não é a única forma de acompanhar essa aprendizagem.\nTambém não é adequado supor que os estudantes da mesma idade tenham idênticos conhecimentos, mobilidade ou experiências. Materiais acessíveis e situações que não obriguem exposição pessoal permitem que mais crianças participem da investigação.'),
    call('Como avaliar essa proposta?','Se o objetivo é representar e explicar um trajeto com referências, Lia examina a coerência da representação e da explicação, com os apoios combinados. A beleza do desenho não deve funcionar como medida de compreensão geográfica.'),
    text('O que a turma pode ampliar depois?','Nos anos seguintes, pode cruzar mais fontes, comparar recortes e construir explicações mais complexas. O ponto de partida não é descartado: suas relações são retomadas e reorganizadas. Essa continuidade orienta a próxima lição.')
], 'Nos anos iniciais, observar, representar, comparar e explicar com apoio pode desenvolver a leitura geográfica do mundo. Vivido e conexões amplas se articulam; a avaliação deve examinar as relações pretendidas, e não a beleza do produto.',order('Organize a proposta para os anos iniciais',[
    'Reconhecer conhecimentos e levantar perguntas com materiais acessíveis.',
    'Investigar informações simples sobre origem, pontos e trajeto.',
    'Representar e comparar percursos com referências e legenda.',
    'Explicar uma conexão e verificar se outra pessoa compreende a representação.' ]))

lesson(12,'Anos finais: cruzar fontes e explicar processos','Conteúdos se articulam por um problema',21,[
    text('A pergunta ganha mais relações e fontes','Para os anos finais do Ensino Fundamental, Lia retoma o abastecimento e propõe: por que localidades próximas se conectam de maneira diferente à feira? A turma pode cruzar mapas, dados de circulação, registros de condições físicas e relatos contextualizados. A proposta é um exemplo autoral, a ser adequado ao currículo e ao percurso dos estudantes.\nO avanço não depende apenas de aumentar a quantidade de nomes ou páginas. Está em articular informações, reconhecer limites e construir uma explicação mais ampla. Conteúdos de circulação, população, natureza e produção entram porque ajudam a responder ao problema.'),
    table('Do conteúdo à contribuição para explicar',['Conteúdo selecionado','Função na investigação'],[
        ['Cartografia e redes','Comparar posições, trajetos e conexões; ler fonte, legenda e recorte.'],
        ['Natureza e uso da terra','Investigar como condições físicas e formas de ocupação participam dos acessos.'],
        ['População e serviços','Examinar distribuição, medidas e oferta, sem deduzir acesso de um único total.'],
        ['Campo, cidade e trabalho','Relacionar produção, circulação, venda e agentes do circuito.']]),
    call('Acompanhe a passagem do relato à explicação','Use as quatro etapas da cena. Pergunte o que a turma acrescenta em cada passagem: uma questão investigável, uma relação conceitual ou uma explicação sustentada. Depois aplique esse raciocínio ao problema da feira.'),
    anim('mediation','Conceitos participam da mediação','A cena existente parte de um relato sobre chegar à escola. Nos controles “1. Relato”, “2. Pergunta”, “3. Conceito” e “4. Explicação”, observe como cotidiano e conceitos se articulam. O mesmo modo de organizar perguntas pode ser adaptado ao abastecimento.'),
    text('Lia enfrenta uma generalização da turma','Um grupo afirma: “O lugar mais próximo sempre tem melhor acesso”. Lia pede comparar mapas e informações sobre trajetos, espera e disponibilidade. Os alunos podem encontrar proximidade sem conexão frequente. A tarefa confronta uma relação automática com dados, sem simplesmente substituir a frase por outra a decorar.\nDepois, a turma precisa explicar como rede e escala ajudam a interpretar a diferença. Se acrescentar apenas palavras como território e região ao texto inicial, sem mostrar sua função, ainda precisará de mediação para usar os conceitos.'),
    picture('u13-objetivo-evidencia.png','Alinhe pergunta, tarefa e produção esperada','O exemplo de território mostra a mesma lógica: se a aprendizagem pretendida é explicar controle dos usos, atividade e avaliação precisam permitir examinar agentes, regras e acesso.'),
    text('Diferentes dimensões do conteúdo se articulam','Aprender envolve conceitos e relações, modos de investigar e posturas de estudo. Ler uma legenda, comparar dados e citar a fonte são modos de trabalhar; ouvir argumentos e revisar uma generalização participam de uma investigação responsável. Essas dimensões precisam ter uma função clara na proposta.\nLia pode oferecer textos com extensões diferentes, legendas acessíveis e apoio à leitura, mantendo a exigência de relacionar evidências. Adaptar o acesso ao material não significa abandonar o problema ou tratar a turma como um grupo de capacidades idênticas.'),
    compare('Avaliação resolvida','Tarefa pouco alinhada','Depois de investigar conexões e acesso, pedir somente os nomes das localidades mostra reconhecimento, mas não verifica a explicação pretendida.','Tarefa pertinente','Apresentar outro par de localidades e pedir uma justificativa com mapa e dados. A análise verifica se o aluno consegue usar a relação além do exemplo inicial.'),
    text('Ponte para o Ensino Médio','A investigação pode ser ampliada com conflitos de uso, decisões de agentes e alternativas. Argumentar exigirá explicitar critérios, confrontar fontes e considerar consequências em diferentes escalas.')
], 'Nos anos finais, ampliar a investigação envolve cruzar fontes e relacionar processos. O conteúdo ganha sentido em uma pergunta; a aprendizagem aparece na explicação e em seu uso em outro caso, com apoios adequados à turma.',order('Construa uma explicação sobre conexões diferentes',[
    'Delimitar uma diferença de acesso que possa ser investigada.',
    'Comparar mapas, dados e condições dos trajetos.',
    'Confrontar a generalização com conceitos e evidências.',
    'Usar a relação para justificar uma situação nova.' ]))

lesson(13,'Ensino Médio: conceitos para analisar e argumentar','Confronte agentes, escalas e alternativas',23,[
    text('A praça entra em uma decisão coletiva','Para uma proposta no Ensino Médio, Lia apresenta um conflito inteiramente fictício: ampliar uma área de armazenamento pode reorganizar o abastecimento, mas também reduzir usos da praça. Grupos de trabalhadores, moradores e gestores apresentam argumentos diferentes. Como analisar a proposta e suas consequências?\nA turma precisa mobilizar conceitos, comparar fontes e explicitar critérios. Território ajuda a investigar poder e acesso; lugar, as experiências e vínculos; paisagem e espaço geográfico, transformações de formas e relações; rede e escala, conexões e efeitos que ultrapassam a praça.'),
    text('Aprofundar é construir relações e autonomia','O Ensino Médio permite desenvolver investigações com mais variáveis, fontes e interpretações, considerando o percurso real dos estudantes. Isso não significa que crianças não argumentem ou que conceitos pertençam exclusivamente a uma etapa. Complexidade e suporte precisam ser planejados.\nA seção de Ciências Humanas e Sociais Aplicadas da BNCC de 2018 oferece uma referência de articulação de tempo, espaço, territórios, natureza, sociedade, política e trabalho. Aqui o documento é uma leitura situada para o exemplo; a organização e as normas do ensino serão tratadas na unidade 1.4.'),
    table('Compare argumentos sem aceitar a conclusão pronta',['Argumento fictício','Pergunta para examiná-lo'],[
        ['“O armazém aumentará o fluxo.”','Qual fluxo, para quais agentes e com que dados de capacidade e circulação?'],
        ['“A praça é importante para a memória.”','Que experiências e referências coletivas sustentam o argumento e como variam?'],
        ['“A mudança beneficia a cidade.”','Quem se beneficia, em quais condições e que usos podem ser prejudicados?'],
        ['“O problema se resolve só no município.”','Que decisões e conexões externas precisam entrar na análise?']]),
    compare('Argumento resolvido','Afirmação genérica','“A proposta é boa porque moderniza o espaço.” O termo modernizar não explica os critérios, os agentes nem a distribuição dos efeitos.','Argumento analisado','“A proposta precisa ser examinada pelos efeitos sobre circulação, trabalho e usos da praça, com fontes sobre quem decide e quem acessa a área.” Indica relações e evidências necessárias antes da conclusão.'),
    text('Confrontar alternativas com critérios explícitos','Lia pode pedir que os grupos comparem manter, ampliar ou reorganizar o uso em horários, desde que investiguem a viabilidade e as consequências das alternativas. Nenhuma opção é declarada correta apenas por seu rótulo. O trabalho é sustentar e delimitar o argumento com as fontes disponíveis.\nA avaliação não deve premiar concordância com a posição do professor. Deve examinar precisão conceitual, interpretação das evidências, relação entre escalas, consideração de perspectivas e coerência da conclusão. Quando faltarem dados, reconhecer o limite pode fortalecer o argumento.'),
    picture('u13-progressao.png','A progressão amplia relações e autonomia','As operações aparecem em todas as etapas. O esquema destaca possibilidades de aprofundamento; não é uma distribuição obrigatória de conceitos por idade ou uma sequência universal de aprendizagem.'),
    call('Transfira para outro conteúdo','Em um problema sobre energia ou uso da terra, não basta listar vantagens e desvantagens. Pergunte onde, por quais agentes, para quais usos e em que escalas os efeitos ocorrem. Conceitos geográficos ajudam a organizar uma posição sustentada.'),
    text('Ponte para a prova','Você já dispõe de um percurso para analisar conteúdo e ensino: problema, conceitos, fontes, mediação e evidências. Na última lição, vamos usar esse encadeamento para resolver questões e organizar uma resposta escrita.')
], 'No Ensino Médio, conceitos sustentam a análise de agentes, conflitos, alternativas e escalas. Aprofundar envolve autonomia e relações mais complexas, com avaliação da qualidade do argumento e de seus limites, sem exigir concordância com o professor.',match('Relacione a pergunta ao trabalho argumentativo',[
    ['Quem decide os usos e controla os acessos?','Analisar relações territoriais de poder.'],
    ['Que experiências sustentam o valor atribuído à praça?','Interpretar vínculos e significados de lugar.'],
    ['Como a decisão se articula a fornecedores de fora?','Relacionar redes e escalas.'],
    ['Que evidências faltam para concluir?','Delimitar o alcance do argumento.']]))

lesson(14,'Resolver casos e escrever com conceitos','A definição vira argumento quando explica uma relação',23,[
    text('Retome a feira com perguntas diferentes','Ao longo da unidade, o mesmo caso permitiu investigar formas, experiências, poder, recortes e conexões. Conceitos não são etiquetas que cada paisagem recebe uma única vez. Sua contribuição depende da pergunta e da relação que ajudam a explicar.\nPara a prova, leia o destaque do enunciado antes de escolher uma categoria. Depois examine o que os dados permitem concluir, o que ainda exige fonte e qual aprendizagem a proposta de ensino pretende desenvolver. As questões da unidade são autorais, não oficiais nem previsão da seleção.'),
    table('Compare sem transformar os conceitos em sinônimos',['Foco da pergunta','Conceito que contribui','O que precisa ser explicado'],[
        ['Formas percebidas e transformações.','Paisagem.','Que marcas aparecem e que processos precisam ser investigados.'],
        ['Experiências e significados.','Lugar.','Como se constroem e por que podem variar.'],
        ['Controle e apropriação dos usos.','Território.','Quem exerce poder, por quais práticas e com que efeitos.'],
        ['Recorte de diferenças e articulações.','Região.','Qual critério foi usado e para qual problema.'],
        ['Relações históricas entre formas e ações.','Espaço geográfico.','Como permanências e mudanças se articulam.']]),
    compare('Questão resolvida 1: dois recortes','Situação','Um mapa organiza localidades pelo relevo; outro, pelas conexões com mercados. Os grupos são diferentes. Um dos mapas está necessariamente errado?','Resolução','Identifique problema e critério. Recortes diferentes podem ser consistentes para finalidades diferentes. Verifique dados e justificativas; não escolha apenas o que parece mais familiar.'),
    compare('Questão resolvida 2: aprender território','Situação','Após investigar regras de uso da praça, a avaliação pede apenas copiar a definição de território. O que falta para examinar a aprendizagem pretendida?','Resolução','Uma tarefa em que o aluno explique agentes, práticas de controle e efeitos sobre o acesso, de preferência em outro caso. Repetir o termo não demonstra sozinho que consegue usá-lo.'),
    text('Construa um parágrafo que responda ao problema','Uma ideia central possível é: “Conceitos geográficos precisam funcionar como instrumentos para explicar relações, com mediação adequada ao percurso dos estudantes”. Essa frase orienta o argumento; as seguintes devem desenvolvê-lo com uma decisão concreta de ensino.\nPor exemplo: “Ao estudar uma praça, território permite investigar quem define os usos e como isso afeta o acesso. Comparar regras e experiências oferece fontes para a análise. A avaliação pode pedir uma justificativa sobre outra situação, examinando se o estudante usa o conceito além de repetir sua definição”. O exemplo mostra a função do conceito, da tarefa e da evidência.'),
    table('Organize a resposta escrita',['Movimento','O que fazer'],[
        ['Ideia central','Responder ao tema, sem abrir uma lista de definições.'],
        ['Precisão conceitual','Explicar os conceitos necessários na acepção usada.'],
        ['Decisão de ensino','Relacionar problema, conteúdo, fontes e mediação.'],
        ['Aprendizagem e limite','Indicar uma evidência e reconhecer o alcance da conclusão.']]),
    call('Revisão ativa antes do simulado','Explique sem consultar: por que paisagem não é só beleza? Por que lugar não exige apenas afeição? Como território vai além do mapa de países? Como o critério muda a regionalização? O que distingue escala de análise e cartográfica? Retome a lição do ponto que ainda não consegue exemplificar.'),
    text('Feche com uma transferência','Troque a feira por escola, área agrícola ou distribuição de serviços. Formule uma pergunta, selecione conceitos e diga que produção do aluno demonstraria aprendizagem. Essa transferência é um modo de verificar se as ideias se tornaram ferramentas de interpretação.\nO simulado reúne 20 casos comentados. A oficina de redação oferece 20 linhas de treino, critérios de autoavaliação e um modelo. Use os erros como indicação do raciocínio que precisa retomar, sem confundir o resultado desta unidade com o desempenho previsto na seleção.')
], 'Uma resposta consistente explica relações com conceitos, fontes e exemplos analisados. No ensino, articula problema, conteúdo, mediação e evidência de aprendizagem; na prova, conserva precisão e delimita conclusões.',order('Construa uma resposta sobre conceitos e ensino',[
    'Responder ao problema com uma ideia central.',
    'Explicar os conceitos que participam da análise.',
    'Analisar uma situação de ensino com fontes e mediação.',
    'Indicar evidência de aprendizagem e limites da conclusão.' ]))

questions=[]


def question(n,stem,correct,why,distractors,tag,pool='lesson'):
    assert len(distractors)==3
    count=sum(q['pool']==pool for q in questions)+1
    questions.append(dict(id=('f' if pool=='final' else 'q')+f'{count:02d}',lesson=f'l{n:02d}',
                          stem=stem,options=[correct]+[a for a,_ in distractors],answer=0,
                          feedback=[why]+[f for _,f in distractors],tag=tag,pool=pool,type='single'))


question(1,'Na proposta de Lia, qual escolha mostra um conceito funcionando como ferramenta de interpretação?',
 'Usar território para investigar quem decide os usos da praça e como isso afeta o acesso.',
 'O conceito organiza uma relação de poder e acesso que precisa ser explicada no caso.',[
 ('Acrescentar a palavra território à legenda, sem relacioná-la ao problema.','A presença do termo não demonstra que ele participa da interpretação das relações.'),
 ('Escolher uma fotografia colorida como objetivo completo da aula.','A fotografia é uma fonte ou recurso. Ainda é necessário definir a aprendizagem pretendida.'),
 ('Substituir o tema abastecimento por uma lista de nomes de categorias.','A lista não esclarece como as ideias ajudam a compreender o problema de estudo.')],'conceitos e interpretação')
question(1,'“Abastecimento de uma feira”, “rede” e “comparar conexões para explicar a circulação” indicam, respectivamente:',
 'Um recorte de conteúdo, um conceito e uma aprendizagem pretendida.',
 'O assunto define o recorte; rede ajuda a analisar conexões; a operação explicativa indica o que o aluno deverá aprender.',[
 ('Uma aprendizagem completa, um recurso e um nome de lugar.','O assunto não define sozinho a aprendizagem; rede é um conceito, e a comparação é uma operação.'),
 ('Três recursos materiais equivalentes.','Os termos têm funções diferentes no planejamento e não designam três suportes materiais.'),
 ('Três categorias que devem ser estudadas sem relação.','O caso articula recorte, ferramenta e finalidade; não propõe três categorias isoladas.')],'conteúdo conceito e objetivo')
question(1,'A turma investiga a mesma praça por suas formas, experiências e regras de acesso. Que interpretação é mais adequada?',
 'Conceitos diferentes podem contribuir para perguntas distintas sobre o mesmo espaço.',
 'A praça não pertence exclusivamente a uma categoria. A pergunta define quais relações entram em foco.',[
 ('Cada conceito exige estudar uma praça diferente.','A mudança de foco analítico não exige trocar o objeto empírico.'),
 ('A coexistência de perguntas demonstra que os conceitos são sinônimos.','Os conceitos podem dialogar mantendo funções e relações específicas.'),
 ('Uma fotografia determina qual conceito é permitido usar.','A função da fonte depende do problema e não impõe uma única categoria.')],'articulação dos conceitos')
question(1,'Uma avaliação pede explicar uma regra de uso da praça. Qual produção oferece evidência mais pertinente?',
 'Uma justificativa que identifique agentes, formas de controle e efeitos sobre o acesso.',
 'A produção usa a relação conceitual na situação, coerente com a aprendizagem escolhida.',[
 ('A repetição da definição, sem referência ao caso.','Repetir a definição informa reconhecimento verbal, mas não demonstra a aplicação pedida.'),
 ('O desenho com maior quantidade de cores.','O critério estético não verifica a explicação dos usos e do controle.'),
 ('Uma lista de nomes dos trabalhadores sem relações entre eles.','Identificar agentes pode iniciar a análise, mas a tarefa pede explicar suas relações.')],'evidência de aprendizagem')

question(2,'O armazém permanece no mesmo ponto, mas recebe novos fluxos e funções. O que esse caso permite analisar?',
 'Permanência de uma forma e transformação de relações e ações.',
 'Uma forma pode continuar enquanto seu uso e sua articulação com o espaço mudam.',[
 ('Ausência de mudança espacial, pois a construção é a mesma.','A forma material não resume todos os usos, ações e conexões.'),
 ('Mudança que dispensa investigar agentes e decisões.','Compreender o processo exige relacionar o funcionamento a agentes e condições.'),
 ('Separação completa entre materialidade e funcionamento.','O caso mostra articulação entre a forma existente e os novos usos.')],'objetos e ações')
question(2,'Qual pergunta articula objetos e ações no estudo de um cais?',
 'Como sua estrutura, os transportes e as decisões de uso participam da circulação?',
 'A pergunta relaciona condições materiais e ações em vez de analisar cada elemento como isolado.',[
 ('Quantos elementos posso listar sem discutir seus usos?','A listagem identifica formas, mas não constrói a articulação solicitada.'),
 ('Como ignorar a estrutura para estudar apenas a intenção dos usuários?','As ações encontram possibilidades e limites em condições materiais.'),
 ('Por que o cais produziria os mesmos efeitos sem qualquer uso social?','O funcionamento precisa ser compreendido na relação com ações e contextos.')],'relações espaciais')
question(2,'Para afirmar uma mudança entre duas fotografias, Lia precisa inicialmente:',
 'Conferir datas, enquadramento e condições de comparação.',
 'Uma interpretação temporal precisa de registros que sustentem o que está sendo comparado.',[
 ('Ordená-las pela aparência mais antiga das construções.','A aparência não substitui a identificação das datas e dos contextos.'),
 ('Escolher a imagem mais nítida como prova do momento mais recente.','Nitidez não demonstra a posição temporal de um registro.'),
 ('Considerar qualquer diferença visual como efeito do mesmo processo.','Diferenças de ângulo, período e situação podem exigir explicações distintas.')],'fontes e temporalidade')
question(2,'Uma escola mantém o prédio, mas altera horários, público e conexões. Qual análise é coerente?',
 'A edificação informa uma continuidade, sem demonstrar permanência de todas as relações.',
 'A explicação distingue a forma que permanece das ações e relações que podem mudar.',[
 ('O espaço da escola é idêntico em todos os aspectos.','Prédio igual não significa usos e conexões iguais.'),
 ('A materialidade perdeu qualquer importância para o estudo.','A construção continua participando das possibilidades e condições de uso.'),
 ('A mudança só pode ser reconhecida se houver demolição.','Transformações de funcionamento e relações também são relevantes.')],'permanências e mudanças')

question(3,'Uma fotografia mostra um galpão fechado. Qual afirmação respeita melhor o alcance da fonte?',
 'O registro permite observar o fechamento naquele momento; explicar o motivo exige outras informações.',
 'A leitura distingue uma condição visível de sua causa, que não pode ser presumida.',[
 ('O galpão encerrou definitivamente suas atividades por falta de renda.','A fotografia não prova duração do fechamento nem sua causa econômica.'),
 ('Todos os trabalhadores perderam o emprego depois do registro.','Trajetórias de trabalho e acontecimentos posteriores exigem outras fontes.'),
 ('A cena não tem valor para nenhuma pergunta geográfica.','A imagem pode contribuir para observação e formulação de questões, dentro de seus limites.')],'paisagem e evidência')
question(3,'Qual proposta amplia a leitura da paisagem além de classificá-la como bonita ou feia?',
 'Reconhecer formas e investigar processos e usos que ajudam a explicá-las.',
 'Paisagem permite analisar marcas e relações, sem se reduzir a um julgamento estético.',[
 ('Estudar apenas vistas sem construções.','Paisagens urbanas e produtivas também podem ser investigadas.'),
 ('Inferir a renda individual pela aparência de uma moradia.','A forma visível não sustenta sozinha uma conclusão sobre renda individual.'),
 ('Separar definitivamente elementos naturais e sociais, sem relações.','A explicação geográfica precisa investigar como esses elementos se articulam.')],'leitura da paisagem')
question(3,'Duas fotos datadas e comparáveis mostram substituição de árvores por pavimento. Qual é a conclusão inicial mais sustentada?',
 'Houve transformação nas formas registradas; causas e efeitos precisam ser investigados.',
 'A comparação sustenta a mudança visível, mas não todas as explicações sobre seu processo e suas consequências.',[
 ('A obra necessariamente melhorou a vida de todos.','Experiências e efeitos sociais não são demonstrados apenas pela aparência.'),
 ('A prefeitura tomou a decisão sem participação de outros agentes.','A identificação do processo decisório exige documentos e outras fontes.'),
 ('Não é possível reconhecer nenhuma transformação.','Quando as condições de comparação são adequadas, as mudanças visíveis são evidências relevantes.')],'mudança de paisagem')
question(3,'Uma imagem agrícola sugere perguntas sobre uso da terra. Para afirmar quem controla a área, o professor deve:',
 'Investigar agentes, práticas e documentos pertinentes à pergunta.',
 'A paisagem pode iniciar a questão, mas controle e propriedade não são deduzidos da aparência do plantio.',[
 ('Deduzir a propriedade pelo tamanho aparente das plantas.','O aspecto da cultura não identifica por si só proprietários e relações de controle.'),
 ('Considerar que toda área com o mesmo cultivo tem a mesma organização social.','Semelhança visível não elimina diferenças de trabalho, acesso e poder.'),
 ('Abandonar a pergunta porque fotos só servem para decorar conteúdos.','A imagem pode contribuir para formular e confrontar hipóteses com outras fontes.')],'paisagem e território')

question(4,'Três pessoas atribuem sentidos diferentes à praça. O conceito de lugar ajuda principalmente a:',
 'Investigar experiências e significados, reconhecendo sua diversidade.',
 'O foco está em como as relações vividas produzem sentidos, que não precisam ser idênticos.',[
 ('Determinar uma experiência média que substitua todos os relatos.','Uma média não esgota a diversidade dos significados e das condições.'),
 ('Restringir a análise a sentimentos agradáveis.','Memória, conflito e desconforto também podem participar da experiência.'),
 ('Provar que a praça está isolada de processos externos.','Os sentidos vividos podem se relacionar a conexões e decisões em outras escalas.')],'lugar e experiência')
question(4,'“A praça fica ao lado do cais” e “a praça é referência na rotina de trabalho” destacam:',
 'Uma relação de localização e uma relação de experiência, respectivamente.',
 'Posição e significado podem dialogar, mas não expressam a mesma função analítica.',[
 ('Duas medidas de densidade demográfica.','Nenhuma das frases relaciona população e área.'),
 ('Dois exemplos equivalentes de propriedade formal.','As frases não identificam título de propriedade nem seus documentos.'),
 ('Uma experiência inválida e uma posição cartográfica absoluta.','A primeira informa posição relativa; a segunda destaca a relação vivida.')],'lugar e localização')
question(4,'Uma estudante relata dificuldade para circular em uma praça que outras pessoas apreciam. Qual interpretação é adequada?',
 'As experiências podem diferir, e barreiras materiais precisam entrar na investigação.',
 'Reconhecer diferentes vivências evita transformar a experiência de um grupo em padrão universal.',[
 ('A praça deixa de ser lugar porque existe desconforto.','A experiência de lugar não exige apenas afeição ou satisfação.'),
 ('A maioria torna o relato da estudante geograficamente irrelevante.','Uma experiência distinta pode revelar relações e condições que outras falas não mostram.'),
 ('Todas as pessoas com a mesma condição terão uma experiência idêntica.','A diversidade precisa ser investigada, sem generalizar uma trajetória para todos.')],'diversidade de experiências')
question(4,'Como estudar lugar sem isolá-lo do mundo?',
 'Relacionar experiências locais a conexões, decisões e processos de outras escalas.',
 'O vivido pode ser compreendido em articulação com redes e relações mais amplas.',[
 ('Concluir o estudo de todos os detalhes locais antes de permitir qualquer conexão.','Uma sequência rígida de círculos não é condição para investigar relações entre escalas.'),
 ('Trocar os relatos por nomes de países sem explicar relações.','A mudança de tamanho do recorte não constrói, sozinha, uma conexão explicativa.'),
 ('Considerar que lugar significa apenas uma área de tamanho muito pequeno.','O conceito não se define apenas pela dimensão física da área.')],'lugar e conexões')

question(5,'Uma regra reserva a praça para certos usos em determinados horários. Que pergunta destaca território?',
 'Quem define e faz valer a regra, e como ela afeta o acesso dos participantes?',
 'O foco são relações de poder, controle e usos do espaço.',[
 ('Qual palavra descreve a cor predominante das construções?','A descrição de formas pode ajudar, mas não analisa a relação de controle destacada.'),
 ('Quantos habitantes há por quilômetro quadrado?','Densidade pode ser relevante a outro problema, mas não substitui a análise da regra.'),
 ('Qual é a escala numérica de um mapa da praça?','A redução cartográfica não identifica agentes e práticas de poder.')],'território e poder')
question(5,'Um aluno afirma: “Sem muro não há território”. Qual explicação enfrenta o limite?',
 'Controle e apropriação podem operar por regras, horários e práticas, sem um muro visível.',
 'A relação territorial não depende de uma única forma material universal.',[
 ('Todo território é apenas um sentimento privado sem condições materiais.','A dimensão simbólica pode se articular a usos e controles materiais.'),
 ('Território e mapa político de países são sempre a mesma coisa.','A análise pode abranger agentes e relações em diferentes escalas.'),
 ('Qualquer parede comprova, sozinha, quem exerce todo o poder no local.','Uma forma visível não esgota a identificação dos agentes e das práticas de controle.')],'controle e limites')
question(5,'Como interpretar a relação entre propriedade e território?',
 'A propriedade formal pode importar, mas usos, práticas e relações de poder precisam ser investigados.',
 'O título jurídico não esgota todas as formas de controle, apropriação e disputa pelo espaço.',[
 ('São termos intercambiáveis em toda análise geográfica.','Território não se reduz a uma condição jurídica de propriedade.'),
 ('A análise territorial exige ignorar normas e Estado.','Reconhecer outras formas de poder não elimina a importância de normas e agentes estatais.'),
 ('A aparência de um plantio comprova a situação jurídica da área.','Uma afirmação jurídica precisa de fontes pertinentes, não apenas de observação visual.')],'território e propriedade')
question(5,'Trabalhadores defendem a praça como local de renda e referência coletiva. Como analisar os dois argumentos?',
 'Investigar como condições materiais e significados participam da apropriação e da disputa.',
 'As dimensões podem se articular; renda e identidade não precisam ser tratadas como mundos separados.',[
 ('Eliminar o argumento de identidade porque não possui forma física própria.','Dimensões simbólicas podem participar de relações de poder e apropriação.'),
 ('Considerar que a existência de um vínculo elimina qualquer disputa material.','Vínculos e conflitos sobre acesso e trabalho podem coexistir.'),
 ('Concluir que todos os trabalhadores têm igual controle da área.','A igualdade de controle não pode ser presumida a partir de uma identidade compartilhada.')],'material e simbólico')

question(6,'No esquema da unidade, A e B são do mesmo grupo pelo relevo e de grupos distintos pelos mercados. Isso significa que:',
 'Os recortes usam critérios diferentes e precisam ser julgados por suas perguntas e dados.',
 'A mudança do critério pode mudar o agrupamento sem produzir contradição automática.',[
 ('Um dos mapas está necessariamente errado.','Antes de julgar, é preciso verificar finalidade, critério e consistência de cada recorte.'),
 ('Qualquer divisão é igualmente adequada para estudar abastecimento.','A pertinência depende da relação entre o critério e o problema.'),
 ('A e B mudaram fisicamente de posição entre os desenhos.','O esquema mantém as localidades e altera o critério de agrupamento.')],'critérios de regionalização')
question(6,'Para estudar conexões de abastecimento, qual justificativa favorece um recorte por fluxos?',
 'Ele pode revelar articulações entre localidades e mercados pertinentes ao problema.',
 'O critério é justificado pela relação que se pretende compreender, não por sua validade para qualquer finalidade.',[
 ('Ele elimina a necessidade de conferir os dados.','Todo critério precisa de informações consistentes e contextualizadas.'),
 ('Ele demonstra que o relevo não importa para nenhuma questão geográfica.','Critérios diferentes podem servir a perguntas diferentes, sem apagar outras relações.'),
 ('Ele torna todas as localidades iguais em todos os aspectos.','Um agrupamento por conexão não elimina a diversidade interna.')],'região e finalidade')
question(6,'Colorir regiões permite reconhecer recortes. Para ampliar essa atividade, Lia deveria pedir também:',
 'Uma explicação do critério, da finalidade e do que varia dentro dos grupos.',
 'A justificativa ajuda a aprender a regionalizar e evita tomar a região como homogeneidade absoluta.',[
 ('A escolha da cor preferida como único critério de agrupamento.','A cor representa uma classificação; não substitui sua justificativa geográfica.'),
 ('A memorização dos nomes sem relacioná-los à divisão.','Nomes podem situar o estudo, mas não explicam o recorte.'),
 ('A afirmação de que toda região tem o mesmo tamanho.','Tamanho igual não é condição universal de uma regionalização.')],'ensinar regionalização')
question(6,'Na referência de 2017 do IBGE, a regionalização por Regiões Geográficas Imediatas e Intermediárias permite discutir:',
 'Articulações da rede urbana como parte de uma construção de recortes para certas finalidades.',
 'O exemplo institucional mostra critérios e contexto de uma regionalização, sem exigir que ela responda a qualquer problema.',[
 ('Uma separação natural imutável, independente de processos sociais.','O trabalho de regionalização considera relações e transformações do território.'),
 ('O desaparecimento de toda diferença dentro de cada região.','O recorte não transforma seus componentes em realidades idênticas.'),
 ('A equivalência entre todos os limites regionais e a propriedade privada.','Regiões e propriedade expressam problemas e critérios distintos.')],'regionalização e contexto')

question(7,'Duas localidades próximas têm conexões principais com mercados diferentes. Qual hipótese orienta melhor a investigação?',
 'Rotas, serviços e condições de circulação podem diferenciar suas articulações.',
 'Proximidade física não determina sozinha o funcionamento da rede.',[
 ('A menor distância em linha reta garante a mesma conexão.','É necessário investigar trajetos e fluxos, em vez de deduzi-los apenas da posição.'),
 ('Um dos mercados não existe porque a conexão difere.','A diferença de fluxo não demonstra inexistência de um ponto da rede.'),
 ('A análise deve excluir a circulação e considerar apenas cores do mapa.','O problema envolve funcionamento e conexões, não uma preferência de representação.')],'rede e proximidade')
question(7,'O que distingue escala de análise de escala cartográfica?',
 'A primeira organiza recortes e relações do problema; a segunda expressa redução da representação.',
 'As duas podem se articular, mas não têm a mesma definição.',[
 ('A primeira se mede apenas em centímetros e a segunda é a experiência pessoal.','A redução numérica pertence à escala cartográfica; experiência não define sozinha uma escala.'),
 ('As duas significam exclusivamente dar zoom na tela.','Ampliar uma imagem não acrescenta automaticamente relações e fontes à análise.'),
 ('A primeira impede conexões entre lugares e a segunda explica todos os fluxos.','Nenhuma dessas propriedades corresponde às definições estudadas.')],'tipos de escala')
question(7,'Qual comparação de escalas cartográficas está correta?',
 '1:10.000 é maior que 1:100.000, pois reduz menos a realidade.',
 'A relação 1/10.000 é maior; nela, um centímetro representa uma distância real menor.',[
 ('1:100.000 é maior porque o denominador é maior.','O denominador maior indica maior redução, não maior escala cartográfica.'),
 ('As escalas são iguais se o mapa for visto no mesmo celular.','O tamanho da tela não torna equivalentes relações numéricas diferentes.'),
 ('1:10.000 significa que cada quilômetro real ocupa dez mil quilômetros no mapa.','A escala indica redução entre medidas correspondentes, não essa ampliação invertida.')],'escala cartográfica')
question(7,'Ao estudar apenas a praça, Lia não encontra as decisões dos fornecedores externos. Qual ampliação é pertinente?',
 'Investigar agentes e conexões em outras escalas com fontes adequadas.',
 'A mudança de análise acrescenta relações necessárias ao problema, além do recorte local.',[
 ('Aumentar o desenho sem acrescentar informações ou perguntas.','Zoom não substitui a investigação de relações que não constam da fonte.'),
 ('Concluir que o que ocorre fora não pode afetar o lugar.','O lugar pode participar de redes e decisões de outras escalas.'),
 ('Trocar os nomes da praça por nomes de continentes, sem construir conexões.','Mudar a lista de localizações não produz a relação explicativa necessária.')],'articulação de escalas')

question(8,'Uma fotografia registra uma tarde chuvosa. Qual conclusão respeita a distinção entre tempo atmosférico e clima?',
 'O registro informa uma condição daquele momento; caracterizar o clima exige informações de duração longa.',
 'Uma observação de tempo não basta para demonstrar sozinha o padrão climático da área.',[
 ('O registro comprova que todos os meses e anos têm a mesma condição.','Essa generalização temporal exige séries e outras informações.'),
 ('Tempo atmosférico é apenas a medida de duração da aula.','No problema, o termo se refere às condições da atmosfera.'),
 ('A chuva isolada comprova uma mudança climática e sua causa específica.','Caracterizar mudança e causas exige evidências que uma foto isolada não oferece.')],'tempo e clima')
question(8,'A mesma chuva alcança trajetos com condições de acesso diferentes. Qual explicação é mais consistente?',
 'Relacionar o evento às condições físicas, à ocupação e às formas de proteção e circulação.',
 'A análise integra fatores e evita transformar o evento em destino social uniforme.',[
 ('Afirmar efeitos iguais porque o evento é semelhante.','Condições diferentes podem participar de efeitos distintos.'),
 ('Excluir a chuva porque existem decisões sociais.','Reconhecer organização social não elimina a participação das condições naturais.'),
 ('Atribuir todo efeito ao comportamento de cada indivíduo.','Uma explicação precisa investigar também condições materiais, coletivas e históricas.')],'natureza e sociedade')
question(8,'Após comparar as duas opções da cena, o aluno afirma que uma obra elimina qualquer risco. Qual cuidado é necessário?',
 'Reconhecer que a cena ilustra uma relação e não fornece garantia ou cálculo de risco real.',
 'A comparação não autoriza universalizar resultados ou dispensar investigação das condições concretas.',[
 ('Aceitar a afirmação porque toda animação constitui uma previsão técnica.','O caráter visual do recurso não transforma um exemplo em modelo preditivo validado.'),
 ('Concluir que infraestrutura nunca participa dos efeitos.','A cena destaca justamente uma participação das condições de acesso e proteção.'),
 ('Trocar os dados ausentes por uma causa escolhida sem fonte.','Quando faltam informações, deve-se explicitar a necessidade de investigação.')],'alcance de modelos didáticos')
question(8,'Qual proposta ensina conteúdos físico-naturais de forma integrada ao problema da feira?',
 'Comparar como relevo, superfície, drenagem e usos participam das condições de circulação.',
 'Os conteúdos entram como relações que ajudam a explicar a situação estudada.',[
 ('Listar tipos de solo sem relacioná-los a nenhuma pergunta.','A listagem pode informar nomes, mas não constrói a explicação integrada pretendida.'),
 ('Tratar vegetação e pavimento como elementos sem qualquer relação com a sociedade.','Usos e transformações da superfície precisam ser analisados em sua articulação.'),
 ('Usar o nome do rio como explicação suficiente de todos os acessos.','Localizar um elemento não demonstra todas as relações que produzem as condições de acesso.')],'conteúdos físico-naturais')

question(9,'A tem 2.000 habitantes em 10 km²; B tem 1.000 em 2 km². Qual comparação está correta?',
 'A tem maior população total; B tem maior densidade média.',
 'A tem 200 hab./km² e B tem 500. O total e sua relação com a área respondem a perguntas diferentes.',[
 ('A tem maior população e maior densidade porque 2.000 é maior que 1.000.','A comparação de densidade precisa considerar também a área.'),
 ('B tem maior população total porque ocupa área menor.','Área menor não altera a comparação dos totais apresentados.'),
 ('As duas áreas têm densidade igual porque os totais são conhecidos.','É necessário dividir cada população pela superfície correspondente.')],'população e densidade')
question(9,'Uma média de densidade demográfica permite, sozinha, concluir que:',
 'Há uma relação entre total de habitantes e área, sem mostrar toda a distribuição interna.',
 'A medida é informativa, mas não identifica como a população se reparte em cada parte da área.',[
 ('Todos os pontos têm exatamente a mesma concentração de moradores.','Uma média não elimina diferenças de distribuição interna.'),
 ('Os habitantes têm a mesma renda e acesso a serviços.','Condições sociais e acesso exigem outras informações.'),
 ('A área de menor densidade não participa de nenhuma rede urbana.','A medida não demonstra ausência de conexões ou participação em redes.')],'limites das médias')
question(9,'Qual pergunta destaca uma relação agrária no estudo do abastecimento?',
 'Como o acesso à terra, o trabalho e as relações de poder participam das condições de produção?',
 'O foco examina relações sociais de uso e acesso à terra, em diálogo com a produção agrícola.',[
 ('Qual cor de embalagem aparece com maior frequência?','Essa observação não analisa as relações agrárias do problema.'),
 ('Quantas palavras tem o nome do cultivo?','Uma contagem de palavras não explica produção, trabalho ou acesso à terra.'),
 ('Qual é a legenda mais bonita do mapa?','A preferência estética não enfrenta a pergunta sobre relações sociais e fundiárias.')],'agrícola e agrário')
question(9,'Uma proposta relaciona alimento, transportes, serviços e consumo entre campo e cidade. Que interpretação ela favorece?',
 'Campo e cidade se articulam por relações diversas, sem equivaler a atraso e progresso automáticos.',
 'A análise investiga conexões e condições, evitando estereótipos que substituem a explicação.',[
 ('O campo só possui agricultura e a cidade não tem relações com a natureza.','Usos e relações são diversos nos dois contextos.'),
 ('A circulação apaga todas as diferenças de trabalho e acesso.','Conexões podem coexistir com condições e benefícios desiguais.'),
 ('O ponto de venda dispensa investigar as etapas anteriores do circuito.','A banca é parte de relações de produção e circulação que podem exigir outras escalas.')],'campo cidade e circuitos')

question(10,'“Como os pontos de venda se repartem pela área?” destaca qual princípio?',
 'Distribuição.',
 'A pergunta focaliza como os elementos se repartem, em vez de apenas indicar um ponto.',[
 ('Analogia, porque pede somente comparar semelhanças entre duas feiras.','A pergunta apresentada trata da repartição dos pontos, não dessa comparação.'),
 ('Conexão, porque já explica todas as ligações entre os fornecedores.','A distribuição pode dialogar com conexões, mas a pergunta não as explicou.'),
 ('Escala cartográfica, porque define a redução numérica.','A pergunta não apresenta uma relação de redução entre mapa e realidade.')],'distribuição')
question(10,'Qual pergunta coloca conexão em primeiro plano?',
 'Como produção, transporte e venda se articulam no circuito?',
 'A relação entre fenômenos e etapas do circuito é o destaque da pergunta.',[
 ('Qual é a cor predominante das fachadas?','A observação pode descrever a paisagem, mas não examina por si só as articulações.'),
 ('Quantas letras tem o nome da feira?','A contagem não constrói uma relação geográfica entre os fenômenos.'),
 ('Qual imagem parece mais bonita?','Uma preferência estética não explica a conexão entre produção e venda.')],'conexão')
question(10,'Uma turma mapeia até onde se observa um fenômeno definido. Qual princípio está especialmente em foco?',
 'Extensão.',
 'O problema envolve delimitar o alcance espacial da ocorrência estudada.',[
 ('População total, independentemente do fenômeno.','A pergunta de delimitação não é uma contagem genérica de habitantes.'),
 ('Experiência positiva obrigatória de lugar.','Extensão do fenômeno não depende de que os sentidos vividos sejam positivos.'),
 ('Propriedade formal de todas as áreas delimitadas.','Delimitar uma ocorrência não comprova a situação de propriedade das áreas.')],'extensão')
question(10,'O uso de um mapa, por si só, demonstra raciocínio geográfico?',
 'É preciso examinar quais perguntas, operações e relações o aluno constrói com a representação.',
 'O recurso pode apoiar a aprendizagem, mas sua presença não demonstra todas as operações pretendidas.',[
 ('Sim, qualquer cópia de nomes comprova interpretação de processos.','Reconhecer e copiar nomes não demonstra automaticamente explicar relações.'),
 ('Não, mapas não podem participar de uma explicação geográfica.','Mapas podem ser fontes e representações relevantes quando usados com perguntas e critérios.'),
 ('Sim, desde que o desenho use o maior número possível de cores.','A quantidade de cores não é evidência suficiente da compreensão.')],'representação e raciocínio')

question(11,'Uma proposta parte de um alimento conhecido para investigar sua origem. Nos anos iniciais, isso pode:',
 'Articular o vivido a outros lugares com fontes e mediação adequadas.',
 'O próximo pode iniciar conexões com processos mais amplos, sem uma sequência espacial rígida.',[
 ('Ser proibido até terminar todos os conteúdos de família e bairro.','Círculos sucessivos não são condição universal para construir conexões.'),
 ('Dispensar perguntas porque o cotidiano já fornece toda explicação pronta.','O vivido oferece conhecimentos e problemas que precisam ser elaborados.'),
 ('Exigir decorar uma definição acadêmica completa antes de observar.','A mediação pode construir relações com linguagem e apoios pertinentes ao percurso.')],'anos iniciais e conexões')
question(11,'Duas crianças apontam direitas diferentes porque observam a cena de posições opostas. O que Lia pode fazer?',
 'Explicitar o ponto de referência e pedir que expliquem de onde observam.',
 'A divergência permite trabalhar orientação e referência, em vez de presumir incapacidade.',[
 ('Escolher a fala da criança mais velha sem analisar a referência.','Idade não resolve o problema de perspectiva e orientação apresentado.'),
 ('Concluir que toda localização relativa é inútil.','A referência precisa ser explicitada para tornar a relação compreensível.'),
 ('Avaliar apenas o tamanho dos símbolos usados no desenho.','O critério não enfrenta a dificuldade de orientação destacada.')],'orientação e referência')
question(11,'O objetivo é representar um trajeto com referências e legenda. Qual critério é mais pertinente?',
 'Se a representação e a explicação permitem compreender o percurso com os apoios combinados.',
 'O critério acompanha as relações pretendidas na atividade, não uma preferência estética.',[
 ('A beleza do desenho como medida suficiente de compreensão.','Qualidade estética não comprova a relação espacial trabalhada.'),
 ('A quantidade de cores sem relação com os símbolos.','Cores precisam ter função na comunicação e na leitura da representação.'),
 ('A reprodução exata de um padrão adulto, independentemente do objetivo.','A exigência precisa considerar a finalidade, a mediação e o percurso da turma.')],'avaliação nos anos iniciais')
question(11,'Como um conceito pode participar da aprendizagem antes da repetição de uma definição completa?',
 'Pelo uso de relações em observações, representações e explicações com mediação.',
 'A aprendizagem conceitual pode começar no trabalho orientado com situações e relações.',[
 ('Pela eliminação de qualquer relação e manutenção de uma palavra isolada.','A palavra, sem sentido na tarefa, não demonstra elaboração da relação.'),
 ('Pela suposição de que crianças só podem memorizar formas.','A proposta pode desenvolver comparação e explicação com apoios pertinentes.'),
 ('Pela ausência de qualquer intervenção do professor.','A mediação ajuda a ampliar e organizar a compreensão construída pelos estudantes.')],'formação conceitual')

question(12,'Nos anos finais, qual proposta amplia a investigação sobre abastecimento?',
 'Cruzar mapas, dados e relatos para explicar conexões e condições distintas.',
 'O avanço está na articulação de fontes e relações pertinentes ao problema.',[
 ('Acrescentar nomes sem alterar a exigência de explicação.','Mais itens não demonstram, por si só, maior complexidade de relações.'),
 ('Usar conceitos apenas como palavras obrigatórias no texto.','É preciso mostrar sua função na análise, não só sua presença verbal.'),
 ('Dispensar as fontes porque a turma já estudou o tema.','Explicações precisam continuar sendo sustentadas e confrontadas.')],'aprofundamento nos anos finais')
question(12,'Após estudar conexões, uma avaliação pede justificar o acesso em outro par de localidades. Que função essa tarefa tem?',
 'Examinar o uso da relação além do exemplo inicial.',
 'A situação nova ajuda a distinguir compreensão de memorização de uma resposta.',[
 ('Garantir automaticamente que todo o conteúdo foi dominado para sempre.','Uma tarefa oferece evidências situadas, não uma garantia total e definitiva.'),
 ('Substituir a necessidade de interpretar a justificativa.','A resposta precisa ser examinada em relação aos critérios e ao objetivo.'),
 ('Avaliar somente o reconhecimento de nomes já copiados.','A tarefa solicita relações e justificativa em outra situação.')],'transferência e avaliação')
question(12,'A turma diz que a localidade mais próxima tem sempre melhor acesso. Qual mediação enfrenta a generalização?',
 'Comparar trajetos, espera e disponibilidade, pedindo uma explicação com os dados.',
 'A intervenção confronta a relação automática entre proximidade e acesso com outras condições.',[
 ('Trocar a frase por outra para copiar, sem examinar informações.','A substituição verbal não garante revisão do raciocínio.'),
 ('Considerar que a distância é a única informação que pode ser estudada.','A análise do acesso também pode exigir conexões, frequência e condições dos trajetos.'),
 ('Avaliar o grupo pela rapidez com que repete a afirmação.','A rapidez da repetição não demonstra a validade da explicação.')],'mediação e generalização')
question(12,'Ao oferecer materiais com diferentes apoios de leitura, Lia deve procurar:',
 'Tornar o conteúdo acessível, mantendo a construção das relações pretendidas.',
 'A adaptação pode ampliar a participação sem abandonar o problema intelectual da proposta.',[
 ('Tratar todas as trajetórias como idênticas para manter o mesmo suporte.','A diversidade da turma exige considerar condições e necessidades de acesso.'),
 ('Eliminar toda explicação e avaliar apenas preferência por imagens.','Acessibilidade não implica renunciar à aprendizagem geográfica pretendida.'),
 ('Supor que o material acessível dispensa qualquer mediação.','Suporte e intervenção do professor podem se articular na construção da compreensão.')],'apoios e aprendizagem')

question(13,'No conflito fictício sobre armazenamento e usos da praça, qual análise mobiliza território?',
 'Investigar quem decide, que práticas organizam os usos e como o acesso é afetado.',
 'O conceito ajuda a interpretar relações de poder e apropriação envolvidas na proposta.',[
 ('Escolher a proposta com a imagem mais recente.','Atualidade da imagem não demonstra adequação das relações e decisões.'),
 ('Contar os bancos como explicação suficiente da disputa.','A forma material pode importar, mas a contagem não esgota agentes e controle.'),
 ('Ignorar as regras porque existe um vínculo afetivo.','Significados e regras de uso podem se articular e precisam ser investigados.')],'conflito e território')
question(13,'Qual critério de avaliação é coerente com uma investigação argumentativa no Ensino Médio?',
 'Precisão conceitual, interpretação de evidências e coerência da conclusão.',
 'A avaliação examina a qualidade do argumento e o alcance de suas fontes.',[
 ('Concordância com a posição pessoal do professor.','A finalidade é analisar e sustentar posições com critérios, não reproduzir uma preferência.'),
 ('Quantidade de conceitos citados, sem avaliar sua função.','Uma lista extensa não substitui o uso pertinente e preciso das relações.'),
 ('Escolha obrigatória da alternativa chamada moderna.','O rótulo não demonstra efeitos, viabilidade ou distribuição de consequências.')],'argumentação e critérios')
question(13,'“A mudança beneficia a cidade.” Qual pergunta ajuda a desenvolver esse argumento?',
 'Quem se beneficia, em quais condições e com que efeitos sobre outros usos e grupos?',
 'A pergunta torna os sujeitos e as consequências analisáveis, em vez de presumir um benefício uniforme.',[
 ('Qual palavra torna a proposta mais atraente?','A escolha retórica não substitui investigar as consequências.'),
 ('Como evitar examinar as fontes para preservar a opinião inicial?','O argumento deve ser confrontado com evidências e perspectivas pertinentes.'),
 ('Por que uma média de moradores resolveria toda a decisão?','Um indicador isolado não esgota usos, agentes e efeitos de uma proposta.')],'análise de alternativas')
question(13,'O que pode caracterizar aprofundamento no Ensino Médio, sem tornar as operações exclusivas dessa etapa?',
 'Ampliar relações, fontes e autonomia na construção de argumentos.',
 'A complexidade e os apoios variam com o percurso; explicar e argumentar também podem aparecer em outras etapas.',[
 ('Proibir qualquer argumento no Ensino Fundamental.','A progressão não exige adiar toda elaboração até uma etapa final.'),
 ('Aumentar apenas o número de definições decoradas.','Quantidade de termos não demonstra articulação conceitual mais complexa.'),
 ('Dispensar os conhecimentos já construídos nas etapas anteriores.','Retomar e reorganizar relações pode sustentar a progressão.')],'progressão e autonomia')

question(14,'Um enunciado destaca quem controla os horários e permissões de uso de uma praça. Qual análise deve vir primeiro?',
 'Identificar a relação de poder em foco antes de associar o conceito pertinente.',
 'A função da decisão no enunciado orienta a escolha conceitual, evitando etiquetas por objetos.',[
 ('Associar toda praça automaticamente a lugar, independentemente da pergunta.','O mesmo espaço pode ser investigado por relações conceituais diferentes.'),
 ('Escolher região porque qualquer parte do espaço tem limites.','O foco apresentado é controle dos usos, não um critério de regionalização.'),
 ('Responder pela categoria com o nome mais longo.','O tamanho da palavra não é um critério de interpretação geográfica.')],'leitura de enunciados')
question(14,'Qual trecho usa um conceito para sustentar um argumento sobre ensinar?',
 '“Território permite investigar controle dos usos; comparar regras e agentes e justificar outro caso ajuda a verificar essa aprendizagem.”',
 'O trecho relaciona ferramenta conceitual, mediação e evidência de aprendizagem.',[
 ('“Todos os conceitos são importantes porque seus nomes aparecem no programa.”','A importância é afirmada sem mostrar como o conceito participa da explicação.'),
 ('“A turma usou muitas imagens, por isso compreendeu todas as categorias.”','A quantidade de recursos não demonstra o uso dos conceitos.'),
 ('“A praça é lugar, paisagem e território; basta repetir os termos para aprender.”','A coexistência de termos não explica sua função nem verifica a compreensão.')],'conceito e argumento')
question(14,'Dois recortes regionais diferem. Antes de apontar um erro, o candidato deve:',
 'Comparar problema, critério, dados e finalidade dos recortes.',
 'A diferença pode decorrer de escolhas analíticas justificadas, que precisam ser examinadas.',[
 ('Aceitar sempre o mapa com mais cores.','A representação visual não substitui os critérios e a consistência dos dados.'),
 ('Excluir a região que não coincidir com o recorte mais conhecido.','Familiaridade não é prova de adequação para toda finalidade.'),
 ('Concluir que regionalizar não exige qualquer justificativa.','A construção do recorte precisa ser sustentada por critérios e informações.')],'comparação de regionalizações')
question(14,'Qual organização favorece uma resposta escrita consistente?',
 'Ideia central, explicação conceitual, decisão analisada e evidência com limites.',
 'A sequência constrói um argumento que responde ao problema e mostra a função do exemplo.',[
 ('Lista de definições seguida de conclusão sem exemplo.','A listagem pode deixar sem explicação como os conceitos ajudam a enfrentar o problema.'),
 ('Opinião seguida de muitos nomes de autores sem relações.','Citar nomes não substitui desenvolver o raciocínio com precisão e evidências.'),
 ('Descrição estética da imagem como prova de toda aprendizagem.','A preferência visual não demonstra a relação conceitual pretendida.')],'escrita argumentativa')

# Vinte casos autorais para aplicação, com identificadores próprios.
def final(n,stem,correct,why,distractors,tag):
    question(n,stem,correct,why,distractors,tag,pool='final')


final(2,'Um armazém conserva sua estrutura, mas passa a integrar outro circuito de mercadorias. Um aluno afirma que a permanência da forma demonstra ausência de mudança espacial. Qual análise enfrenta o problema?',
 'Comparar como usos, ações e conexões se transformaram em relação à forma que permaneceu.',
 'A análise do espaço articula continuidade material e mudanças de funcionamento, em vez de tomar uma como prova da outra.',[
 ('Tratar o armazém apenas como paisagem antiga e encerrar a investigação na data da construção.','A data pode ser relevante, mas não explica as relações e os usos posteriores.'),
 ('Retirar a materialidade do estudo e explicar a circulação somente por intenções declaradas.','As ações se articulam a condições e formas materiais; não precisam ser isoladas delas.'),
 ('Identificar novos nomes de mercadorias e considerá-los suficientes para explicar todo o circuito.','Reconhecer produtos informa uma mudança, mas as conexões e sua organização ainda precisam ser explicadas.')],'formas ações e tempo')
final(3,'Duas fotografias da mesma praça, com datas e enquadramentos comparáveis, mostram uma área arborizada substituída por pavimento. Qual conclusão é sustentada inicialmente?',
 'O registro evidencia mudança nas formas; explicar a decisão e seus efeitos exige confrontar outras fontes.',
 'A comparação permite reconhecer a transformação visível sem deduzir todos os processos, agentes e resultados.',[
 ('A mudança comprova maior acesso para todos os usuários, pois o pavimento aparece nas duas perspectivas.','A presença da nova forma não comprova seus efeitos uniformes sobre diferentes usuários.'),
 ('A comparação identifica os agentes responsáveis e a ausência de participação na decisão.','Datas e enquadramentos não substituem documentos e fontes sobre o processo decisório.'),
 ('A imagem mais recente torna desnecessário investigar usos anteriores, pois o espaço atual se explica por suas formas.','A explicação pode exigir história, relações e ações, além da aparência presente.')],'paisagem e alcance da fonte')
final(4,'Uma trabalhadora vincula a praça à renda; outra pessoa relata barreiras e desconforto. Para analisar lugar, Lia deve:',
 'Relacionar os sentidos vividos às experiências e condições, investigando diferenças sem exigir afeição comum.',
 'Lugar não se reduz a sentimento positivo ou a uma vivência uniforme de todas as pessoas.',[
 ('Selecionar o relato mais frequente e usá-lo como representação suficiente de todas as experiências.','A frequência não elimina experiências distintas nem dispensa analisar suas condições.'),
 ('Restringir o estudo à posição da praça no mapa, porque o conflito de sentidos impede qualquer interpretação.','A localização situa o caso; a diversidade de sentidos é justamente uma questão investigável.'),
 ('Separar as vivências de qualquer conexão econômica, para preservar a análise no plano exclusivamente individual.','Experiências podem se constituir em relações sociais, materiais e conexões mais amplas.')],'lugar e diversidade')
final(5,'Uma praça pública recebe regras diferentes de uso ao longo do dia. Há disputa entre trabalhadores, moradores e responsáveis pela gestão. Qual investigação coloca território em foco?',
 'Examinar quem estabelece e faz valer as regras, as apropriações e seus efeitos sobre usos e acessos.',
 'O foco territorial está nas relações de poder e apropriação, que não se esgotam na identificação de uma superfície.',[
 ('Determinar o título formal da área e tomar essa informação como explicação suficiente de todas as práticas.','A situação jurídica pode importar, mas não esgota controle efetivo, usos e disputas.'),
 ('Mapear a extensão da praça e considerar que a medida demonstra como os agentes participam das decisões.','A medida espacial não comprova participação nem poder dos agentes.'),
 ('Comparar apenas lembranças agradáveis, pois a presença de vínculos transforma a regra em questão sem materialidade.','Significados podem se articular a regras e condições materiais, sem eliminar a análise do controle.')],'território e controle')
final(6,'Um estudo agrupa A, B e C por semelhança do relevo. Outro agrupa A, D e E por conexão com um mercado. Como avaliar os recortes?',
 'Confrontar os critérios, os dados e a finalidade de cada estudo, reconhecendo que os grupos podem diferir de modo consistente.',
 'Regionalizações diferentes podem ser justificadas por problemas diferentes; sua pertinência precisa ser demonstrada.',[
 ('Preferir o grupo por relevo em qualquer situação, pois critérios físico-naturais tornam o recorte independente da pergunta.','Um critério pode ser pertinente a certos problemas, sem validade automática para todos.'),
 ('Aceitar qualquer agrupamento porque regionalizar equivale a escolher livremente as cores.','A construção do recorte exige critérios e informações; não é uma decisão visual sem justificativa.'),
 ('Tratar os dois grupos como contraditórios porque uma localidade não pode participar de interpretações diferentes.','A mesma localidade pode integrar recortes distintos conforme as relações analisadas.')],'regionalização comparada')
final(7,'Dois mapas mantêm a mesma relação numérica de escala, mas a investigação passa a examinar decisões de fornecedores externos ao município. O que mudou necessariamente na análise descrita?',
 'As relações e os recortes do problema foram ampliados; isso não se define apenas pela redução cartográfica.',
 'Escala de análise envolve relações e recortes da explicação, enquanto escala cartográfica indica a redução da representação.',[
 ('A escala cartográfica aumentou, pois qualquer referência a fornecedores externos altera sua fração.','A relação numérica não se altera por acrescentar uma pergunta ou fonte à análise.'),
 ('A praça perdeu o caráter de lugar, pois relações locais deixam de existir quando são conectadas ao exterior.','As conexões podem ajudar a compreender o vivido, sem apagar o lugar.'),
 ('A investigação se tornou apenas uma mudança de zoom, dispensando novas informações sobre os agentes.','Examinar decisões externas pode exigir fontes que o mapa local não oferece.')],'escala de análise')
final(7,'Dois trajetos diferentes medem 2 cm em seus respectivos mapas. O primeiro mapa tem escala 1:25.000; o segundo, 1:250.000. Que comparação dos comprimentos reais está correta?',
 'Os comprimentos reais correspondem a 500 m e 5 km; a primeira escala é maior.',
 'No primeiro, 2 × 25.000 cm = 500 m; no segundo, 2 × 250.000 cm = 5 km. Menor redução corresponde à maior escala.',[
 ('Os comprimentos são iguais porque ambos medem 2 cm no papel.','É preciso aplicar a relação de redução de cada representação.'),
 ('Os comprimentos são 5 km e 500 m; o maior denominador indica menor distância real.','A relação foi invertida: maior denominador corresponde a maior distância real por centímetro.'),
 ('Os comprimentos são 500 m e 5 km, mas a segunda escala é maior pelo denominador.','Os comprimentos estão corretos; a comparação de escalas está invertida.')],'cálculo e escala')
final(8,'Após uma tarde chuvosa, um estudante afirma que o registro comprova uma mudança climática e explica sua causa. Que intervenção enfrenta a insuficiência da evidência?',
 'Distinguir a condição de tempo registrada dos padrões climáticos e investigar séries e outras evidências para a afirmação.',
 'Um evento isolado não demonstra sozinho um padrão, sua transformação ou uma causa específica.',[
 ('Substituir o registro por outra foto do mesmo dia e tratar a repetição visual como série climática.','Mais imagens do mesmo evento não constituem, por si só, evidência de duração longa.'),
 ('Concluir que registros de chuva não podem contribuir para nenhuma investigação do clima.','Registros podem participar de séries e estudos; o problema é o alcance da conclusão isolada.'),
 ('Aceitar a conclusão se a fotografia mostrar bastante água, pois intensidade visível e mudança de padrão são equivalentes.','A aparência do evento não demonstra a mudança de um padrão climático nem sua causa.')],'tempo clima e evidências')
final(8,'Uma chuva semelhante alcança dois trajetos com ocupação e proteção diferentes. Qual proposta constrói melhor uma explicação geográfica?',
 'Relacionar condições físicas, exposição e vulnerabilidade com usos, infraestrutura e história dos acessos.',
 'A explicação integra relações naturais e sociais e precisa de fontes para compreender seus efeitos concretos.',[
 ('Usar a chuva como explicação suficiente, acrescentando os nomes dos grupos sem examinar suas condições.','Nomear os grupos não corrige a redução do problema a um único fator.'),
 ('Explicar exclusivamente por escolhas individuais, pois a comparação de trajetos elimina a relevância do ambiente.','Decisões individuais não esgotam condições naturais, materiais e coletivas.'),
 ('Tomar a melhoria ilustrada na animação como previsão validada de que uma obra terá o mesmo resultado em todo local.','A cena é didática; não comprova resultados universais nem calcula risco real.')],'explicação integrada')
final(9,'C tem 1.200 habitantes em 4 km²; D tem 1.500 em 10 km². Qual leitura conserva o sentido das medidas?',
 'D tem maior população total; C tem maior densidade média, sem que isso revele sozinho a distribuição interna.',
 'C tem 300 hab./km² e D, 150. Totais, densidades e distribuição interna são informações relacionadas, mas distintas.',[
 ('D tem maior total e maior densidade, porque a comparação populacional dispensa a área.','A densidade exige relacionar cada total à superfície correspondente.'),
 ('C tem maior densidade, portanto todos os seus pontos têm mais moradores e menor renda.','Uma média não demonstra a repartição interna nem a renda dos habitantes.'),
 ('C tem maior população total por apresentar maior quociente, e D tem a distribuição mais uniforme.','O quociente representa densidade; a uniformidade interna não está informada.')],'densidade e interpretação')
final(9,'A turma estuda um alimento que passa por área de produção, cais, feira e outro mercado. Qual organização do conteúdo favorece uma explicação?',
 'Articular trabalho, circulação e consumo com agentes e conexões, verificando o que cada fonte permite afirmar.',
 'O problema relaciona conteúdos e escalas, sem tomar uma etapa como explicação suficiente do circuito.',[
 ('Tratar campo e cidade como blocos independentes e escolher apenas o ponto de venda para representar todas as relações.','A proposta apagaria conexões que o próprio percurso torna relevantes.'),
 ('Usar o volume vendido como indicador suficiente da distribuição de terra e da renda de cada trabalhador.','Medidas de venda não demonstram sozinhas relações fundiárias e condições individuais.'),
 ('Ordenar os lugares do mais atrasado ao mais moderno pela aparência das construções.','O julgamento substitui a investigação de técnicas, trabalho e condições por um estereótipo.')],'conteúdos e circuito')
final(10,'Os estudantes localizam mercados e depois investigam como transporte, armazenamento e venda se articulam. Qual interpretação descreve o avanço?',
 'A localização passa a integrar uma explicação de conexões, sustentada por informações sobre o funcionamento.',
 'Localizar é relevante e pode ser articulado a outras operações para construir o raciocínio geográfico.',[
 ('A segunda tarefa elimina qualquer função da primeira, pois localização e explicação não podem participar do mesmo estudo.','As operações podem se articular; localizar ajuda a situar relações que serão investigadas.'),
 ('A mudança consiste apenas em escrever a palavra conexão, mesmo que nenhuma relação seja examinada.','O uso da palavra precisa corresponder à construção de relações no caso.'),
 ('A posição dos mercados já comprova frequência e capacidade de todos os transportes.','Essas condições exigem informações que a posição, sozinha, não fornece.')],'princípios articulados')
final(11,'Nos anos iniciais, Lia parte de um alimento conhecido e usa imagens e um percurso fictício com legenda. Qual justificativa é mais consistente?',
 'A proposta articula vivido e conexões com outros lugares, com apoios que permitem representar e explicar relações.',
 'O cotidiano pode abrir relações amplas desde o início da escolarização, com mediação pertinente.',[
 ('A origem externa deve ser omitida até encerrar uma sequência fixa de família, escola, rua e bairro.','Não é necessário impor círculos espaciais rígidos para construir conexões.'),
 ('A familiaridade com o alimento garante que a criança já compreenda toda a rede e dispense investigação.','Conhecer o produto não equivale a explicar suas origens e conexões.'),
 ('A legenda deve ser julgada principalmente por sua beleza, pois a comunicação do trajeto é conteúdo exclusivo de etapas posteriores.','Representação e compreensão do trajeto podem ser trabalhadas com suporte adequado nos anos iniciais.')],'anos iniciais e alfabetização geográfica')
final(12,'Após comparar acessos, o aluno repete “B é melhor”. Lia muda os dados e pede uma justificativa sobre outro par de localidades. O que essa decisão procura examinar?',
 'Se o estudante usa as relações e os critérios além da resposta memorizada no primeiro caso.',
 'Uma nova situação acompanhada de justificativa oferece evidências sobre o alcance da compreensão.',[
 ('Se o estudante conserva a mesma letra, que deve permanecer correta quando os dados mudam.','A resposta depende dos dados e do critério; memorizar a letra não demonstra compreensão.'),
 ('Se o estudante prefere mapas a tabelas, tomando preferência como evidência suficiente de explicação.','Preferência não substitui a análise do raciocínio na justificativa.'),
 ('Se o estudante já domina definitivamente toda a Geografia, sem necessidade de interpretação de sua produção.','A tarefa permite uma conclusão delimitada; não garante domínio total e definitivo.')],'transferência e avaliação')
final(13,'No Ensino Médio, grupos defendem alternativas para os usos da praça. Qual critério de avaliação se alinha à aprendizagem geográfica pretendida?',
 'Analisar precisão dos conceitos, confronto de fontes, relações entre escalas e coerência dos argumentos.',
 'A qualidade da análise pode ser examinada sem tornar a posição do professor o resultado obrigatório.',[
 ('Dar maior nota ao grupo que defende a solução preferida pelo docente, mesmo sem apresentar fontes.','Concordância pessoal não demonstra a qualidade da interpretação geográfica.'),
 ('Contar quantas categorias foram citadas, sem examinar sua função em cada argumento.','Uma lista extensa pode conservar conceitos soltos, sem relações explicativas.'),
 ('Avaliar a apresentação visual como substituta suficiente da investigação de agentes e consequências.','A comunicação visual pode contribuir, mas não dispensa examinar o conteúdo do argumento.')],'avaliação de argumentos')
final(13,'Um grupo afirma: “O projeto é positivo porque amplia o fluxo de mercadorias”. Qual pergunta amplia a análise sem decidir previamente a posição final?',
 'Que fluxos e agentes são favorecidos, como isso afeta outros usos e que fontes sustentam as consequências?',
 'A pergunta explicita critérios e relações que o argumento inicial ainda não desenvolveu.',[
 ('Como confirmar a proposta usando apenas os exemplos favoráveis já selecionados?','A seleção unilateral pode impedir confrontar consequências e limites.'),
 ('Qual nome mais atraente substituiria projeto para assegurar concordância?','Um recurso retórico não resolve a investigação dos efeitos e dos critérios.'),
 ('Por que a existência do fluxo torna desnecessário examinar experiências e controle do espaço?','Circulação pode se articular a relações de poder e a experiências diversas.')],'análise de alternativas')
final(5,'Uma área tem propriedade formal definida, mas apresenta disputas de passagem, horários e usos. Qual leitura é pertinente?',
 'O dado jurídico participa da investigação, que também precisa examinar controle efetivo, práticas e apropriações.',
 'Propriedade não é sinônimo de todas as relações territoriais; normas e práticas precisam ser relacionadas no caso.',[
 ('O título esgota a explicação geográfica e dispensa examinar quem consegue circular.','A situação formal não demonstra por si só todas as condições e práticas de acesso.'),
 ('A existência da disputa torna normas e Estado irrelevantes para a análise.','Reconhecer outras relações de poder não apaga a importância de normas e agentes estatais.'),
 ('A ausência de um muro elimina a possibilidade de analisar território.','Controle pode operar por regras e práticas sem barreira física visível.')],'território e apropriação')
final(13,'Três propostas trabalham a praça em etapas diferentes: representar percursos com apoio; cruzar fontes sobre conexões; confrontar alternativas de uso e seus agentes. Como interpretar essa progressão?',
 'Como possibilidades de ampliar relações e autonomia, sem tornar as operações exclusivas de cada etapa.',
 'As propostas precisam ser adequadas ao percurso real; crianças também podem argumentar, e estudantes mais velhos podem precisar de apoio.',[
 ('Como distribuição fixa que proíbe explicar nos anos iniciais e representar no Ensino Médio.','A progressão não deve transformar operações em permissões exclusivas por idade.'),
 ('Como prova de que a simples troca do tema garante avanço, independentemente das relações construídas.','A complexidade depende do trabalho intelectual, das fontes e da mediação.'),
 ('Como motivo para abandonar os conhecimentos anteriores assim que a etapa muda.','Retomar e reorganizar relações pode sustentar novas aprendizagens.')],'progressão entre etapas')
final(14,'Qual trecho articula conceito, conteúdo e decisão de ensino em um argumento?',
 '“Ao estudar usos da praça, território ajuda a investigar poder e acesso. Comparar regras e agentes e justificar outro caso permite examinar essa aprendizagem.”',
 'O trecho mostra o que se estuda, como o conceito contribui e qual produção oferece evidência.',[
 ('“Os conteúdos são importantes porque existem muitas categorias e os estudantes precisam reconhecer seus nomes.”','O trecho não explica a função das ideias em uma interpretação ou decisão de ensino.'),
 ('“Toda praça pertence apenas ao conceito de lugar, por isso a avaliação deve cobrar uma única definição.”','O objeto pode ser analisado por perguntas diferentes; a aprendizagem não se limita a uma etiqueta.'),
 ('“Se a aula tem mapas e fotografias, a compreensão de todos os conceitos já pode ser considerada demonstrada.”','Recursos não comprovam sozinhos o raciocínio construído pelos alunos.')],'conceito conteúdo e evidência')
final(14,'Dois mapas de abastecimento apresentam agrupamentos distintos e usam dados de anos diferentes. Qual procedimento é mais adequado antes de concluir que um deles errou?',
 'Examinar critérios, datas, fontes e finalidade, distinguindo mudança de recorte e mudança do fenômeno.',
 'Diferenças podem decorrer de critérios ou transformações; a interpretação precisa conferir como cada mapa foi produzido.',[
 ('Escolher o mais recente sem ler os critérios, pois a data resolve todas as diferenças de finalidade.','Atualidade pode importar, mas não substitui compreender o problema e o recorte.'),
 ('Preferir o que coincide com limites administrativos, pois todo fluxo precisa terminar nesses limites.','Conexões podem atravessar limites administrativos; o critério precisa responder à pergunta.'),
 ('Considerar as divergências prova de que mapas não podem contribuir para investigar redes.','Mapas podem contribuir; é necessário interpretar condições de produção e alcance das informações.')],'fontes critérios e temporalidade')


flashcards=[dict(id=f'c{i:02d}',front=front,back=back) for i,(front,back) in enumerate([
    ('Conceito e conteúdo','Conteúdo é um recorte do que se estuda; conceito ajuda a organizar relações. No abastecimento, rede permite investigar conexões e território, controle dos usos.'),
    ('Categoria tem uma lista universal?','Autores e abordagens podem organizar os termos de modos diferentes. Nesta unidade, categorias são conceitos com papel amplo na análise geográfica.'),
    ('O mesmo objeto exige um só conceito?','Não. A praça pode ser investigada por formas, experiências, poder e conexões. A pergunta indica o foco, sem tornar os conceitos sinônimos.'),
    ('Espaço geográfico','Nesta leitura, relações entre sociedade e natureza são historicamente produzidas por trabalho, técnicas e ações. O espaço não é apenas um recipiente vazio.'),
    ('Objetos e ações em Milton Santos','Cais, estrada e armazém precisam ser relacionados a transportar, negociar, regular e trabalhar. Formas e ações se articulam.'),
    ('Forma permanece, função muda','O prédio do armazém pode continuar enquanto fluxos e usos mudam. Permanência material não prova ausência de transformação espacial.'),
    ('Paisagem','Formas e marcas perceptíveis podem iniciar a investigação de processos. Paisagem não é apenas beleza ou natureza sem sociedade.'),
    ('Fotografia e causa','Uma foto registra aspectos de um momento e ponto de vista. Explicar decisões, renda ou trajetórias exige outras fontes pertinentes.'),
    ('Comparar antes e depois','Conferir datas, enquadramentos e condições ajuda a sustentar uma comparação temporal. Aparência antiga e nitidez não são datas.'),
    ('Lugar','Experiências, vínculos e significados se constroem nas relações com o espaço. Podem envolver afeição, memória, conflito e desconforto.'),
    ('Lugar e localização','“Ao lado do cais” situa uma posição relativa; perguntar como o cais participa da rotina investiga uma relação vivida.'),
    ('Lugar é uma ilha?','Não. Experiências locais podem se articular a decisões, circuitos e processos de outras escalas.'),
    ('Território','Relações de poder, apropriação e controle do espaço, com dimensões materiais e simbólicas. Pergunte quem decide e quem acessa.'),
    ('Território precisa de muro?','Não necessariamente. Regras, horários e práticas também podem controlar usos. É preciso investigar a relação, não apenas a barreira.'),
    ('Território e propriedade','O título formal pode importar, mas não esgota controle efetivo e apropriações. Não deduza a situação jurídica apenas da paisagem.'),
    ('Região e regionalização','Recortes ajudam a interpretar diferenças e articulações. Regionalizar exige explicitar problema, critério, dados e finalidade.'),
    ('Recortes diferentes são contraditórios?','Não automaticamente. Relevo e conexões podem organizar grupos distintos; sua pertinência precisa ser julgada pela pergunta e pelas fontes.'),
    ('Diversidade dentro da região','Um grupo construído por certo critério não se torna homogêneo em todos os aspectos. Examine também variações internas.'),
    ('Rede geográfica','Pontos e fluxos se articulam com frequência, custo, capacidade e centralidades. Linhas desenhadas não explicam sozinhas o funcionamento.'),
    ('Proximidade e conexão','Dois pontos próximos podem ter conexões diferentes. Trajetos, serviços e condições precisam ser investigados.'),
    ('Escala de análise','Recorte e relações usados para compreender um problema. Articular praça, município e fornecedores é mais que dar zoom no mapa.'),
    ('Escala cartográfica','Relação de redução entre representação e realidade. 1:10.000 é maior que 1:100.000 porque reduz menos.'),
    ('Tempo atmosférico e clima','Um evento informa condições de tempo; padrões climáticos exigem informações de longa duração. Uma foto de chuva não prova uma mudança climática.'),
    ('Natureza e sociedade','Explicar efeitos desiguais pode exigir relacionar evento, condições físicas, ocupação, infraestrutura e proteção. Um fator não determina sozinho tudo.'),
    ('População total e densidade','Densidade média relaciona habitantes e área. A média não mostra toda a distribuição interna nem explica sozinha condições de vida.'),
    ('Campo e cidade','Produção, circulação, serviços e consumo articulam relações diversas. Evite equiparar campo a atraso e cidade a progresso automático.'),
    ('Raciocínio geográfico','Localizar, comparar, delimitar, conectar e explicar com fontes e representações. Os princípios funcionam em relações, não como palavras isoladas.'),
    ('Anos iniciais e o mundo','O vivido pode abrir conexões com outros lugares, com linguagem, fontes e apoios adequados. Não é obrigatório seguir círculos espaciais rígidos.'),
    ('Progressão entre etapas','Ampliar relações, fontes e autonomia sem reservar operações exclusivamente a uma idade. Os apoios dependem da turma e do problema.'),
    ('Evidência de uso do conceito','Uma justificativa sobre outro caso pode mostrar a função do conceito além de sua definição. Avalie precisão, fontes, relações e limites.')
],1)]

references=[
    dict(title='Edital PROFGEO-UFPA n. 03/2026 — Anexo III, item 1.3',author='UFPA / PROFGEO',year=2026,
         url=PAGE+'#edital',note='Fonte do título e do programa. PDF enviado pelo estudante; ingresso 2027. As leituras abaixo são complementares selecionadas, não bibliografia obrigatória declarada no item. A ficha liga à página oficial.'),
    dict(title='A natureza do espaço: técnica e tempo, razão e emoção',author='Milton Santos',year=1996,
         url=PAGE+'#espaco-geografico',note='Obra de referência para a articulação entre sistemas de objetos e de ações; ano da primeira edição. A ficha oferece acesso ao catálogo da Edusp. Exemplos da feira são aplicações autorais.'),
    dict(title='Lugar: uma perspectiva experiencial',author='Yi-Fu Tuan',year=2018,
         url=PAGE+'#lugar',note='Tradução na Geograficidade de texto original de 1973. Referência primária complementar para experiência e significados, sem exigir afeição uniforme.'),
    dict(title='Território e multiterritorialidade: um debate',author='Rogério Haesbaert',year=2007,
         url=PAGE+'#territorio',note='GEOgraphia, v. 9, n. 17 (2007); registro de publicação digital em 2010. Fonte primária complementar para poder, apropriação e dimensões materiais e simbólicas.'),
    dict(title='Divisão Regional do Brasil em Regiões Geográficas Imediatas e Regiões Geográficas Intermediárias: 2017',author='IBGE',year=2017,
         url=PAGE+'#regionalizacao',note='Exemplo institucional de construção de recortes por articulações da rede urbana. A unidade não reproduz limites ou resultados atuais de cada região.'),
    dict(title='Aprendendo a ler o mundo: a geografia nos anos iniciais do ensino fundamental',author='Helena Copetti Callai',year=2005,
         url='https://www.scielo.br/j/ccedes/a/7mpTx9mbrLG6Dd3FQhFqZYH/?lang=pt',note='Cadernos Cedes, v. 25, n. 66. Fonte primária complementar para leitura do espaço, alfabetização cartográfica e crítica à sequência rígida de círculos espaciais.'),
    dict(title='Cotidiano, mediação pedagógica e formação de conceitos',author='Lana de Souza Cavalcanti',year=2005,
         url='https://www.scielo.br/j/ccedes/a/WnXnVgTRQHZttxBQR44gt9x/?lang=pt',note='Cadernos Cedes, v. 25, n. 66. Fonte primária complementar para mediação e articulação entre conhecimentos cotidianos e científicos no ensino de Geografia.'),
    dict(title='Base Nacional Comum Curricular — Geografia e Ciências Humanas e Sociais Aplicadas',author='Ministério da Educação',year=2018,
         url=PAGE+'#bncc',note='Leitura delimitada aos princípios de raciocínio geográfico e às possibilidades de articulação entre conceitos. As propostas por etapa são autorais. Organização e normas do ensino serão aprofundadas na unidade 1.4.'),
    dict(title='Fontes e créditos dos recursos visuais da unidade 1.3',author='ProfGeo / Wikimedia Commons',year=2026,
         url=PAGE+'#recursos-visuais',note='Seis esquemas novos desenhados por código e três fotografias identificadas, retomadas do acervo das unidades anteriores. Todas as imagens e cenas são 16:9; exemplos, falas e dados fictícios estão identificados.')
]

essay=dict(title='Oficina de redação · conceitos como ferramentas para aprender Geografia',
           prompt='Discuta como conceitos e categorias geográficas podem orientar o estudo de conteúdos no Ensino Fundamental e no Ensino Médio. Explique pelo menos dois conceitos em uma situação de ensino, relacione problema, fontes e mediação e indique uma evidência de aprendizagem. Mostre como as relações ou os apoios podem ser aprofundados entre etapas, sem reduzir o ensino à repetição de definições.',
           maxLines=20,note='Proposta autoral de treino em até 20 linhas digitadas, com autoavaliação formativa. Não é questão oficial nem correção automática do conteúdo.',
           rubric=[
               'Apresentei uma ideia central que responde ao tema.',
               'Expliquei pelo menos dois conceitos com precisão, sem tratá-los como etiquetas equivalentes.',
               'Analisei uma situação concreta e mostrei a função dos conceitos no problema.',
               'Relacionei conteúdo, fontes, mediação e tarefa de aprendizagem.',
               'Indiquei uma evidência de uso do conceito além da repetição da definição.',
               'Expliquei um aprofundamento possível entre etapas sem criar proibições rígidas por idade.',
               'Delimitei o alcance das informações e escrevi com clareza em até 20 linhas.'
           ],model=(
               'Conceitos geográficos devem ajudar os estudantes a explicar relações espaciais. Seu ensino exige articular conteúdos, perguntas e fontes, com mediação adequada ao percurso da turma. Memorizar definições pode apoiar o estudo, mas não demonstra sozinho seu uso na interpretação.\n'
               'Ao investigar uma praça, paisagem permite reconhecer formas e levantar perguntas sobre transformações. Território coloca em foco quem define os usos e como regras e práticas afetam o acesso. As duas entradas dialogam, sem tornar os conceitos sinônimos.\n'
               'Nos anos iniciais, imagens e representações com referências podem apoiar observação e comparação. Nos anos finais, a turma pode cruzar mais fontes para explicar mudanças e conexões. No Ensino Médio, pode confrontar agentes, escalas e alternativas, sem reservar a argumentação apenas a essa etapa.\n'
               'A avaliação precisa verificar as relações pretendidas. Explicar uma regra de uso em outra situação oferece uma evidência mais pertinente que apenas copiar a definição de território. Fotografias e relatos também precisam ser examinados dentro de seus limites.\n'
               'Assim, a progressão amplia relações e autonomia, conservando apoios e critérios. Os conceitos se tornam instrumentos de leitura do mundo quando participam de explicações sustentadas e abertas à revisão.'
           ))


def save():
    path=ROOT/'content/catalog.json';catalog=json.loads(path.read_text())
    entry=next(e for m in catalog['modules'] for e in m['units'] if e['id']=='1.3')
    assert entry['revision']<=1,'Não sobrescreva uma revisão posterior.'
    for pool in ['lesson','final']:
        for i,q in enumerate(q for q in questions if q['pool']==pool):
            target=[2,0,3,1][i%4];shift=(target-q['answer'])%4
            pairs=list(zip(q['options'],q['feedback']))
            if shift:pairs=pairs[-shift:]+pairs[:-shift]
            q['options']=[a for a,_ in pairs];q['feedback']=[f for _,f in pairs];q['answer']=target
    assert len(lessons)==14 and len(questions)==76 and len(flashcards)==30
    assert sum(q['pool']=='final' for q in questions)==20
    assert all(sum(q['lesson']==l['id'] and q['pool']=='lesson' for q in questions)==4 for l in lessons)
    unit=dict(schemaVersion=1,id='1.3',moduleId='1',revision=1,title=TITLE,
              shortTitle='Conceitos para ler o espaço e ensinar',
              subtitle='Uma investigação acompanhada: conceitos, conteúdos, escalas e aprendizagem do Fundamental ao Médio.',
              editalItem='1.3',estimatedMinutes=sum(l['minutes'] for l in lessons),
              objectives=[
                  'Distinguir conceito, categoria, conteúdo, recurso e aprendizagem, explicando suas funções.',
                  'Usar espaço, paisagem, lugar, território e região em perguntas e casos analisados.',
                  'Relacionar redes, escalas, conteúdos físico-naturais e sociais em explicações sustentadas.',
                  'Interpretar mapas, fotos e dados reconhecendo critérios, contextos e limites das fontes.',
                  'Planejar progressão entre etapas e avaliar o uso dos conceitos em outra situação.',
                  'Resolver casos e escrever argumentos com conceitos, mediação e evidências de aprendizagem.'
              ],lessons=lessons,questions=questions,flashcards=flashcards,references=references,essay=essay)
    (ROOT/'content/units/1.3.json').write_text(json.dumps(unit,ensure_ascii=False,indent=2)+'\n')
    entry.update(status='published',revision=1)
    catalog['revision']=max(5,catalog['revision']);catalog['updatedAt']='2026-10-26'
    path.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
    print(f'Unidade 1.3: {len(lessons)} lições, 56 questões de prática, 20 casos no simulado, 30 cartões, {unit["estimatedMinutes"]} minutos sugeridos.')


if __name__=='__main__':save()
