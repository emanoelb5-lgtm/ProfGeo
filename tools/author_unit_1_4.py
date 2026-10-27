"""Unidade 1.4: instrumentos curriculares, normas e decisões de ensino; fontes conferidas em 26/10/2026."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TITLE='Programas, documentos e regulamentações que disciplinam e orientam o ensino de Geografia'
PAGE='https://github.com/emanoelb5-lgtm/ProfGeo/blob/main/docs/UNIDADE_1_4.md'


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


lesson(1,'Qual documento responde à minha pergunta?','Comece por uma decisão da escola',18,[
    text('O problema que vai conectar a unidade','A professora Lia quer transformar o estudo da Feira da Ponte em uma sequência de Geografia. A equipe da Escola das Águas pergunta o que é obrigatório aprender, como considerar o contexto local, que regras organizam a etapa e como avaliar. Escola, feira, falas e decisões do caso são fictícias.\nNa 1.3, você usou conceitos para interpretar o espaço. Agora vai aprender a relacionar essas escolhas aos documentos que orientam e regulam o ensino. O objetivo é saber consultar, interpretar e justificar uma decisão, além de reconhecer siglas.'),
    text('A pergunta vem antes da lista de documentos','Se a dúvida é sobre o direito à educação e seus princípios, Lia consulta a Constituição e a legislação pertinente. Se quer localizar aprendizagens essenciais, examina a BNCC. Para compreender a organização da etapa, precisa também das Diretrizes Curriculares Nacionais e das normas do sistema. O currículo da rede e a proposta da escola participam da organização concreta do trabalho.\nNenhum desses instrumentos equivale automaticamente ao plano de uma aula. A professora ainda precisa definir problema, conceitos, fontes, mediação e evidências da aprendizagem. A existência de referências comuns não transforma todos os contextos em uma única situação escolar.'),
    picture('u14-instrumentos.png','Relacione a função ao instrumento','O esquema organiza funções. Não representa uma fila na qual todo documento posterior revoga o anterior. É necessário considerar natureza do ato, competência, alcance e compatibilidade entre as decisões.'),
    picture('u12-sala-aula.jpg','Uma sala real, um caso de estudo fictício','Foto da Escola Técnica de Paulínia em 2015, com conteúdo de História na lousa. A imagem não representa a Escola das Águas e não comprova seu currículo, planejamento ou aprendizagem.'),
    table('Leia a dúvida e escolha por onde começar',['Dúvida do caso','Referências pertinentes'],[
        ['Que direitos e princípios devem ser respeitados?','Constituição, LDB e demais normas aplicáveis.'],
        ['Que aprendizagem essencial será trabalhada?','BNCC, em articulação com currículo e etapa.'],
        ['Como o percurso se organiza nesta rede?','Normas e currículo do sistema ou da rede, para a oferta e o período.'],
        ['Como a escola assume esses compromissos?','Proposta pedagógica, PPP e regimento, em suas funções.'],
        ['Como ensinar e verificar uma relação nesta turma?','Plano de trabalho e de aula fundamentado nas referências.']]),
    compare('Primeiro caso resolvido','Frase inicial','“O livro traz esse capítulo, então ele é a lei que define toda a aula.” A frase confunde um material didático com a função de uma norma.','Raciocínio','O livro pode apoiar o trabalho. A decisão precisa ser relacionada às aprendizagens e aos instrumentos pertinentes; a ordem dos capítulos não substitui essa interpretação.'),
    call('Data de referência do estudo','Fontes oficiais conferidas em 26/10/2026. A unidade considera o novo PNE da Lei 15.388/2026 e as mudanças do Ensino Médio da Lei 14.945/2024, com DCNEM de 2024 e parâmetros de aprofundamento de 2025. Em questões históricas, respeite o período informado no enunciado.'),
    text('Seu percurso','Vamos estudar direitos, organização da educação, documentos curriculares e decisões da rede e da escola. Depois, analisaremos inclusão, planejamento de políticas, materiais e avaliações. Nas últimas lições, você terá casos resolvidos, um roteiro para ler atos e preparação para a escrita.')
], 'Uma decisão de ensino exige identificar a pergunta e a função de cada instrumento. Lei, diretriz, base curricular, currículo, proposta escolar, plano e material didático se articulam sem serem equivalentes.',match('Associe pergunta e função',[
    ['Quais direitos e princípios precisam ser respeitados?','Fundamentos constitucionais e legais.'],
    ['Quais aprendizagens essenciais estão em foco?','Referência curricular da BNCC.'],
    ['Como a escola organiza seus compromissos coletivos?','Proposta pedagógica e PPP.'],
    ['Que tarefa ajudará esta turma a aprender?','Planejamento do trabalho docente.']]))

lesson(2,'Constituição: o direito orienta as escolhas','A norma não é apenas uma formalidade do plano',19,[
    text('Quem consegue participar da investigação?','Lia propõe comparar paisagens, mas parte da turma não consegue acessar o único material escolhido. A pergunta não é apenas qual atividade parece interessante: é como assegurar condições de aprender e participar. A Constituição Federal de 1988 oferece fundamentos para examinar essa decisão.\nO art. 205 relaciona a educação ao desenvolvimento da pessoa, à cidadania e ao trabalho, atribuindo responsabilidades ao Estado e à família, com colaboração da sociedade. O art. 206 estabelece princípios como igualdade de condições de acesso e permanência, liberdade de aprender e ensinar e pluralismo de ideias e concepções pedagógicas.'),
    text('Do princípio à análise do caso','Igualdade de condições não significa oferecer um suporte que alguns não conseguem usar e considerar resolvido o direito. Lia precisa examinar barreiras, recursos e mediações. Os apoios concretos dependem das necessidades e das normas pertinentes, mas a pergunta sobre participação já muda o planejamento.\nLiberdade de ensinar e pluralismo também não equivalem a dispensar fontes, direitos ou responsabilidades profissionais. Uma discussão sobre território pode comparar posições e critérios, sem transformar a concordância com o professor em evidência de aprendizagem.'),
    compare('Caso resolvido: nota por concordância','Decisão proposta','“Quem defender a alternativa de uso da praça escolhida por Lia receberá a maior nota.” O critério exige adesão a uma preferência.','Decisão fundamentada','Avaliar precisão conceitual, interpretação das fontes e coerência do argumento. O aluno pode sustentar outra posição, desde que examine informações e respeite os direitos envolvidos.'),
    text('Base comum e diversidade não surgem do nada','O art. 210 prevê conteúdos mínimos para o Ensino Fundamental, com formação básica comum e respeito a valores culturais e artísticos nacionais e regionais. A LDB desenvolve a organização curricular, que será estudada a seguir. É importante não atribuir à Constituição a redação detalhada de cada habilidade da BNCC.\nO art. 211 trata da organização dos sistemas em regime de colaboração. Por isso, a educação envolve responsabilidades de diferentes entes e órgãos. Uma norma local deve ser compreendida na competência de quem a produz e em relação aos fundamentos superiores; não basta decidir pelo tamanho geográfico de seu título.'),
    anim('lived','Experiências diferentes pedem análise','Compare “Pessoa 1”, “Pessoa 2” e “Pessoa 3”. Os relatos fictícios ajudam a discutir perspectivas diferentes. Relacione a observação aos critérios de avaliação: examine o argumento e suas fontes, sem tomar uma vivência como padrão de todas as pessoas.'),
    table('Conecte fundamento e decisão',['Fundamento','Pergunta de planejamento'],[
        ['Acesso e permanência.','Que condições permitem participação e continuidade dos estudos?'],
        ['Liberdade e pluralismo.','Como confrontar interpretações sem cobrar adesão pessoal?'],
        ['Formação comum e respeito à diversidade.','Como articular aprendizagens e contextos culturais?'],
        ['Colaboração entre sistemas.','Quais normas e responsabilidades se aplicam a esta oferta?']]),
    call('Pare e justifique','“O professor tem autonomia, logo pode ignorar qualquer referência curricular.” O salto não é sustentado. Autonomia profissional envolve decisões justificadas dentro de direitos, normas e compromissos de aprendizagem.'),
    text('Ponte para a LDB','Os princípios ajudam a julgar o sentido da decisão, mas Lia também precisa conhecer as responsabilidades da escola e do professor e a articulação entre base comum e parte diversificada. Esse é o passo da próxima lição.')
], 'A Constituição fundamenta o direito à educação e os princípios do ensino. Liberdade, pluralismo, acesso e colaboração precisam orientar decisões concretas, sem substituir a leitura da legislação e das normas pertinentes.',match('Relacione a situação ao fundamento',[
    ['Examinar barreiras ao uso das fontes.','Condições de participação e aprendizagem.'],
    ['Avaliar argumentos em vez de concordância pessoal.','Liberdade de aprender e pluralismo.'],
    ['Articular formação comum e valores regionais.','Base comum com respeito à diversidade.'],
    ['Identificar responsabilidades entre entes e sistemas.','Regime de colaboração.']]))

lesson(3,'LDB: organizar currículo, responsabilidades e avaliação','A base comum se articula ao contexto',21,[
    text('A dúvida de Lia ganha uma regra de organização','Uma colega afirma que estudar o contexto da feira seria abandonar o currículo nacional. Outra propõe trabalhar somente informações locais e retirar as aprendizagens comuns. O art. 26 da Lei 9.394/1996, a LDB, ajuda a enfrentar as duas reduções.\nOs currículos da Educação Infantil, do Ensino Fundamental e do Ensino Médio devem ter base nacional comum, complementada pela parte diversificada relacionada às características regionais e locais da sociedade, da cultura, da economia e dos estudantes. As dimensões precisam se articular na formação.'),
    compare('O caso da feira, resolvido','Redução 1','“Só posso usar exemplos nacionais idênticos em todas as escolas.” A existência de uma base comum não determina uma única situação didática.','Redução 2','“Como a feira é local, posso excluir o direito às aprendizagens comuns.” Contextualizar não significa substituir toda a formação por curiosidades locais.'),
    text('Responsabilidades que se encontram','O art. 12 atribui à escola elaborar e executar sua proposta pedagógica, respeitando normas comuns e as do sistema. O art. 13 prevê participação docente nessa elaboração e um plano de trabalho relacionado à proposta. A aula não nasce isolada dos compromissos coletivos.\nLia pode selecionar fontes e intervenções, mas precisa justificar como contribuem para o percurso. Também participa de planejamento, avaliação e estratégias de recuperação. Essas responsabilidades não se resumem a preencher um formulário com códigos.'),
    table('LDB e função da decisão',['Referência','Aplicação ao caso'],[
        ['Art. 26: base comum e parte diversificada.','Comparar transformações de paisagem a partir de um contexto significativo.'],
        ['Arts. 12 e 13: proposta e plano de trabalho.','Articular a sequência de Lia aos compromissos da escola.'],
        ['Art. 24, V: avaliação e recuperação.','Examinar produções ao longo do percurso e planejar retomadas.']]),
    text('Avaliar ao longo do processo','Para o Ensino Fundamental e o Médio, o art. 24, V, prevê avaliação contínua e cumulativa, valorizando aspectos qualitativos sobre quantitativos e resultados ao longo do período sobre provas finais eventuais. Isso não proíbe usar notas ou provas; impede tratar uma medida isolada como se esgotasse o percurso.\nNo caso, Lia pode comparar hipóteses iniciais, justificativas durante a sequência e uma nova situação. O resultado permite identificar o que precisa retomar. A recuperação também exige organização, conforme normas e regimento, em vez de ser entendida apenas como outra prova no fim.'),
    call('Fonte consolidada, não fotografia de uma lei antiga','A LDB recebeu várias alterações. Para afirmar o que vale no recorte atual, leia a redação vigente do dispositivo e suas mudanças. O fato de a lei ter sido criada em 1996 não significa que todos os parágrafos permanecem com o texto original.'),
    text('Ponte para os documentos curriculares','A LDB estabelece organização e responsabilidades, mas não é uma coleção de planos de aula. Na próxima lição, vamos situar referências pedagógicas históricas e distinguir suas funções das bases e diretrizes normativas.')
], 'A LDB articula base comum e parte diversificada, proposta escolar e plano docente. Avaliação contínua e cumulativa exige acompanhar relações e dificuldades, com recuperação organizada; não significa abolir todo instrumento quantitativo.',order('Fundamente a sequência de Lia',[
    'Reconhecer a aprendizagem comum e o contexto a investigar.',
    'Relacionar a proposta ao currículo e aos compromissos da escola.',
    'Planejar intervenções e acompanhar produções ao longo da sequência.',
    'Analisar dificuldades e organizar retomadas e recuperação.' ]))

lesson(4,'PCN, orientações, DCN e BNCC: funções diferentes','Entenda o documento no seu tempo',19,[
    text('Uma estante com publicações de épocas distintas','Na escola fictícia, Lia encontra os Parâmetros Curriculares Nacionais de Geografia, de 1998, e materiais atuais da BNCC. Uma colega usa o título “nacional” para afirmar que os dois têm a mesma função jurídica. A identidade de uma palavra não resolve o problema.\nOs PCN são referências pedagógicas de um contexto histórico de construção curricular. Podem contribuir para estudar concepções e propostas de ensino. Não devem ser tratados como uma lei que fixa a mesma aula para todas as escolas nem como substitutos das referências normativas atuais.'),
    text('Orientar e regulamentar não são funções idênticas','As Orientações Curriculares para o Ensino Médio, publicadas pelo MEC em 2006, também participam da história do debate pedagógico. Uma reflexão de ensino pode ser discutida, mas regras atuais de organização exigem consultar os atos aplicáveis e sua redação. Um livro antigo não se torna regra atual porque foi produzido por um órgão público.\nDiretrizes Curriculares Nacionais fixadas por resolução do CNE têm função normativa no seu alcance. A BNCC é um documento normativo que define aprendizagens essenciais. Currículos das redes e propostas escolares concretizam decisões, considerando referências e competências dos respectivos sistemas.'),
    table('Use uma pergunta para distinguir',['Instrumento','Função no estudo'],[
        ['PCN e orientações pedagógicas.','Compreender propostas, concepções e debates em seu contexto histórico.'],
        ['DCN.','Examinar princípios e normas de organização da educação e das etapas.'],
        ['BNCC.','Identificar aprendizagens essenciais e sua organização.'],
        ['Currículo, PPP e planos.','Organizar e desenvolver o trabalho em redes, escolas e turmas.']]),
    compare('Questão histórica, resolvida','Enunciado sobre 1998','Se a pergunta analisa os PCN naquele contexto, a resposta deve considerar o documento e o período informado.','Enunciado sobre 2026','Se pede uma decisão atual, é necessário articular normas e referências atuais. Não se deve importar automaticamente uma organização de outra época.'),
    text('Uma ideia antiga pode ser discutida sem ganhar vigência nova','Lia pode confrontar uma proposta dos PCN com a formação de conceitos estudada na 1.3. O valor analítico da leitura não equivale a provar que todas as regras de uma etapa continuam iguais. A distinção permite estudar a história do ensino sem confundir passado e presente.\nDo mesmo modo, a data mais recente não torna qualquer publicação superior a uma lei. Antes de aplicar uma frase, identifique o tipo do instrumento, a competência do órgão, o assunto e os efeitos que pode produzir.'),
    call('Evite a fila simplificada','Constituição, lei, resolução, base curricular e plano escolar não são nomes intercambiáveis. Entre currículos, PPP e planos há articulação de decisões; isso não significa uma cadeia em que cada texto posterior revoga o anterior.'),
    text('Ponte para a BNCC','Agora vamos examinar como a BNCC participa de uma decisão concreta: transformar uma habilidade sobre paisagens em uma aprendizagem que o aluno consegue demonstrar.')
], 'PCN e orientações são referências pedagógicas situadas historicamente; DCN e BNCC têm funções normativas distintas. Para aplicar um documento, confira natureza, contexto, alcance e relação com os demais instrumentos.',match('Associe o uso à referência',[
    ['Investigar propostas pedagógicas de 1998.','PCN em seu contexto histórico.'],
    ['Examinar normas de organização de uma etapa.','Diretrizes Curriculares Nacionais aplicáveis.'],
    ['Localizar aprendizagens essenciais.','BNCC.'],
    ['Organizar decisões na rede e na escola.','Currículo e proposta pedagógica contextualizados.']]))

lesson(5,'BNCC de Geografia: da habilidade à tarefa','O código ajuda a localizar; a mediação ajuda a aprender',22,[
    text('A referência não entrega a aula pronta','Lia localiza a habilidade EF06GE01 na BNCC: comparar mudanças de paisagens e usos dos lugares de vivência em tempos distintos. A formulação exige uma relação de comparação, mas não escolhe automaticamente as fotos, o tempo da atividade ou a intervenção adequada à turma.\nNo código, EF indica Ensino Fundamental; 06, o ano; GE, Geografia; 01 identifica a habilidade naquele conjunto. A numeração não é um cronograma obrigatório de semanas nem uma escala automática de dificuldade. Ler o texto e suas relações é mais importante que reconhecer a sigla isoladamente.'),
    picture('u14-habilidade-aula.png','A habilidade precisa aparecer no trabalho do estudante','O exemplo é uma aplicação autoral relacionada à EF06GE01. Comparar registros datados e justificar permanências e mudanças é mais pertinente que apenas copiar o código no caderno.'),
    text('Competências, habilidades e objetos não são listas soltas','A BNCC articula competências gerais e específicas, unidades temáticas, objetos de conhecimento e habilidades. Uma competência envolve mobilizar conhecimentos, habilidades, atitudes e valores para enfrentar demandas. A habilidade explicita aprendizagens de modo mais delimitado no percurso.\nO objeto de conhecimento ajuda a situar o que será estudado; a unidade temática organiza relações do componente. Esses elementos precisam ser lidos em conjunto, sem transformar uma palavra em tarefa suficiente ou reduzir o documento a uma sequência de assuntos.'),
    table('Cinco unidades temáticas, uma investigação possível',['Unidade de Geografia no Fundamental','Pergunta autoral sobre a feira'],[
        ['O sujeito e seu lugar no mundo.','Como experiências e identidades se relacionam aos usos?'],
        ['Conexões e escalas.','Como a feira se articula a outros lugares?'],
        ['Mundo do trabalho.','Como produção e circulação são organizadas?'],
        ['Formas de representação e pensamento espacial.','Como mapas e registros ajudam a comparar relações?'],
        ['Natureza, ambientes e qualidade de vida.','Como condições naturais e usos participam do problema?']]),
    compare('Uma escolha resolvida','Tarefa insuficiente para este objetivo','Mostrar duas fotos sem identificação e pedir a mais bonita. A atividade não exige comparar transformações com evidências temporais.','Tarefa alinhada','Confrontar registros identificados, localizar uma mudança e uma permanência e justificar com as fontes. A interpretação ainda deve respeitar o alcance dos registros.'),
    text('Avalie o que foi escolhido como aprendizagem','Lia pode propor outra situação de mudança da paisagem e pedir uma justificativa. Isso ajuda a verificar o uso da relação além da repetição do exemplo. A avaliação não se resume à presença de “EF06GE01” no plano.\nA BNCC e o currículo se relacionam, mas não são sinônimos. Organizar progressão, contextualizar problemas e definir mediações exige trabalho curricular e docente. O exemplo da feira é uma possibilidade, não uma prescrição nacional para todas as turmas.'),
    call('Pergunta para a prova','“Como a BNCC é comum, todos devem ensinar o mesmo exemplo pelo mesmo método.” A conclusão não decorre da referência comum. É preciso assegurar aprendizagens e justificar escolhas dentro das normas e dos contextos.')
], 'Na BNCC, códigos localizam habilidades; sua leitura precisa ser articulada a competências, objetos e unidades temáticas. A aprendizagem exige tarefa e mediação pertinentes, com avaliação das relações construídas.',order('Transforme uma habilidade em proposta de aula',[
    'Ler a aprendizagem e suas relações no componente e no currículo.',
    'Selecionar problema, fontes e apoios adequados à turma.',
    'Orientar uma tarefa que exija a relação pretendida.',
    'Examinar a justificativa em outra situação e replanejar.' ]))

lesson(6,'Diretrizes e atos do CNE: ler natureza e alcance','Parecer e resolução precisam ser identificados por inteiro',19,[
    text('Por que uma habilidade não resolve a organização da etapa?','Lia encontrou uma aprendizagem da BNCC, mas ainda precisa conhecer princípios de organização da oferta e normas do sistema. As Diretrizes Curriculares Nacionais participam desse plano de decisão. Elas não se resumem à lista de habilidades do componente.\nEntre as referências estão a Resolução CNE/CEB 4/2010, de diretrizes gerais para a Educação Básica, e a CNE/CEB 7/2010, para o Ensino Fundamental de nove anos. Para o Ensino Médio, a unidade considera a CNE/CEB 2/2024, no quadro da reforma legal de 2024. A etapa e o assunto precisam ser identificados antes de aplicar uma regra.'),
    table('Identificações que não podem ser trocadas',['Ato','Assunto de referência'],[
        ['CNE/CP 2/2017.','Instituição e implantação da BNCC para Educação Infantil e Ensino Fundamental.'],
        ['CNE/CP 4/2018.','BNCC na etapa do Ensino Médio.'],
        ['CNE/CEB 2/2024.','Diretrizes Curriculares Nacionais para o Ensino Médio.'],
        ['CNE/CEB 4/2025.','Parâmetros para a oferta dos Itinerários Formativos de Aprofundamento.']]),
    text('O que muda entre parecer e resolução?','Um parecer analisa uma matéria e fundamenta uma posição do conselho. Uma resolução estabelece disposições normativas no âmbito da competência do órgão. Certos pareceres homologados também têm efeitos que precisam ser examinados em seu contexto. Por isso, não é adequado chamar todos os pareceres de lei nem descartá-los como textos sem qualquer relevância.\nLia deve verificar identificação, homologação quando pertinente, publicação, assunto e relação com os atos que concretizam as disposições. Uma notícia sobre uma proposta ou uma minuta não comprova, sozinha, que a regra já entrou em vigor.'),
    compare('Caso resolvido: “Resolução 4”','Problema da citação','Uma apostila apresenta apenas “Resolução 4”, sem órgão, ano ou assunto. O número se repete em diferentes contextos.','Raciocínio','Recuperar a identificação completa e ler o ato pertinente. Não se deve aplicar uma regra de itinerários ao Ensino Fundamental apenas porque os números coincidem.'),
    text('A competência também importa','Conselhos e órgãos de diferentes sistemas podem produzir normas complementares dentro de suas atribuições. Uma regra da rede não deve contrariar os fundamentos aplicáveis; ao mesmo tempo, uma orientação nacional genérica pode depender de decisões de organização do sistema.\nNão basta escolher sempre o documento com a data mais nova nem criar uma regra nacional a partir de uma matriz de outro estado. A leitura precisa ligar norma, competência e situação de aplicação.'),
    call('Confira a função no caso','Para definir a aprendizagem sobre paisagem, Lia consulta a BNCC e o currículo. Para examinar organização e condições de oferta, precisa também das diretrizes e normas pertinentes. Uma função não torna a outra dispensável.'),
    text('Ponte para o Ensino Médio','O exemplo mais sensível a mudanças recentes é o Ensino Médio. Vamos separar referência de aprendizagem, organização curricular e horas, sem transformar um material anterior à reforma em regra atual automática.')
], 'Diretrizes organizam princípios e normas em seu alcance. Identifique órgão, espécie, número, ano, assunto e efeitos dos atos; parecer, resolução, notícia e minuta não são documentos intercambiáveis.',match('Relacione instrumento e cuidado de leitura',[
    ['Parecer.','Examinar análise, fundamentação e efeitos no contexto pertinente.'],
    ['Resolução.','Ler disposições normativas e competência do órgão.'],
    ['Minuta ou anúncio de proposta.','Não presumir vigência pela circulação da notícia.'],
    ['Citação “Resolução 4”.','Recuperar órgão, ano e assunto para identificar o ato.']]))

lesson(7,'Ensino Médio: o que mudou e como ler a regra','Geografia, formação geral e aprofundamento',23,[
    text('Uma apostila antiga reaparece no planejamento','Um material anterior à reforma de 2024 apresenta sua organização de horas como regra universal atual. Lia precisa conferir a LDB consolidada e a Lei 14.945/2024 antes de aplicá-lo. A data do exemplo e o tipo de oferta também importam.\nA LDB, no art. 35-B, organiza o currículo do Ensino Médio em formação geral básica e itinerários formativos. O art. 35-D inclui Geografia na área de Ciências Humanas e Sociais Aplicadas, junto com Filosofia, História e Sociologia. Trabalhar por área não significa que o conhecimento geográfico deixou de integrar a formação.'),
    picture('u14-ensino-medio.png','A regra precisa ser relacionada à oferta','A regra geral prevê formação geral básica mínima de 2.400 horas e itinerários de, no mínimo, 600 horas. A formação técnica e profissional tem especificidades; os totais não definem sozinhos a grade semanal de Geografia.'),
    text('Leia as exceções junto com a regra','O art. 35-C prevê 2.400 horas mínimas de formação geral básica. No caso de formação técnica e profissional, seu parágrafo único prevê mínimo de 2.100 horas e admite até 300 horas da formação geral básica para aprofundar conteúdos da BNCC diretamente relacionados à formação técnica oferecida. O art. 36 também ressalva especificidades dessa oferta ao tratar dos itinerários.\nPara estudar, a primeira pergunta é: qual oferta o enunciado descreve? Não se deve transformar o número da regra geral em afirmação idêntica para qualquer modalidade ou composição, nem chamar o total da formação geral de carga exclusiva de Geografia.'),
    text('Diretrizes e implementação completam a leitura','A Resolução CNE/CEB 2/2024 estabelece as DCNEM no quadro das alterações legais. A CNE/CEB 4/2025 trata dos parâmetros de oferta dos Itinerários Formativos de Aprofundamento. A Lei 14.945/2024 previu iniciar a implementação curricular em 2025.\nAplicar a organização a uma turma exige verificar o percurso de implementação e as normas pertinentes do sistema, da rede e da oferta. A unidade não atribui uma grade semanal única a todas as escolas nem presume que um exemplo de outro estado valha para a turma de Lia.'),
    compare('Caso resolvido: o que o dado permite concluir?','Afirmação','“Há 2.400 horas de formação geral; portanto Geografia deve ter o mesmo número de aulas semanais em toda escola.”','Análise','O total se refere à formação geral básica. Para conhecer distribuição e organização concretas, é necessário examinar a matriz e as normas da oferta. A conclusão extrapola o dado apresentado.'),
    table('Perguntas para interpretar o caso',['Pergunta','Por que importa'],[
        ['Qual período está sendo analisado?','Distinguir uma regra histórica da referência atual.'],
        ['Qual é a oferta e há formação técnica?','Ler especificidades e não generalizar a regra.'],
        ['Qual matriz e regra de implementação se aplicam?','Conhecer a organização concreta da turma.'],
        ['O que a regra informa sobre Geografia?','Distinguir sua presença na formação da distribuição semanal local.']]),
    call('Integração com identidade conceitual','Um projeto de Ciências Humanas pode articular Geografia e outros componentes. A justificativa deve mostrar que relações geográficas serão aprendidas, com fontes, conceitos e critérios; a palavra interdisciplinar não substitui essa análise.')
], 'A reforma de 2024 exige ler a LDB atualizada, as DCNEM e a oferta concreta. Geografia integra Ciências Humanas e Sociais Aplicadas; totais de formação não equivalem a uma grade semanal nacional única, e a oferta técnica tem especificidades.',order('Leia uma regra do Ensino Médio antes de aplicá-la',[
    'Identificar período, turma e tipo de oferta.',
    'Consultar redação legal, diretrizes e especificidades pertinentes.',
    'Conferir implementação e matriz do sistema ou da rede.',
    'Justificar a decisão curricular sem extrapolar o alcance do dado.' ]))

lesson(8,'Currículos das redes: contextualizar com critérios','Uma referência nacional encontra territórios e percursos',20,[
    text('Uma aprendizagem comum, situações de estudo diferentes','Lia quer comparar paisagens a partir da feira. Outra escola pode partir de uma área agrícola ou de um bairro. Os exemplos podem ser diferentes e trabalhar relações comuns, desde que as escolhas sejam justificadas no currículo e no percurso dos estudantes.\nO currículo da rede organiza seleções, articulações e progressões em seu contexto. Ele precisa ser lido em relação às normas e à BNCC, e não como um conjunto de curiosidades que se acrescentam sem conexão ao restante da formação.'),
    picture('belem-feira.jpg','O contexto pode participar da pergunta de ensino','Ver-o-Peso, em Belém, fotografado por Cayambe. O registro é uma fonte para questões sobre paisagem, circulação ou trabalho. Não representa a feira inventada nem define, sozinho, o currículo de uma rede.'),
    text('Um documento do Pará, com recorte identificado','O Documento Curricular do Estado do Pará para Educação Infantil e Ensino Fundamental, edição de 2019, é um exemplo de referência produzida em contexto estadual. Ao estudá-lo, identifique a etapa e a edição; não transfira seu título para afirmar que ele apresenta a matriz atual do Ensino Médio.\nPara uma decisão concreta, é preciso conferir atos de adoção, documentos e alterações pertinentes ao sistema e à rede. O fato de uma escola estar em um estado não dispensa identificar a organização aplicável àquela oferta, inclusive relações entre sistemas e municípios.'),
    compare('Contextualização resolvida','Uma escolha inicial','“A turma conhece a feira, então basta listar produtos locais.” O reconhecimento do contexto não explicita ainda a aprendizagem geográfica.','Uma escolha desenvolvida','Usar registros da circulação para comparar conexões e justificar uma transformação da paisagem. O contexto oferece um problema e fontes para elaborar relações, em diálogo com o percurso curricular.'),
    text('A parte diversificada não tem valor menor','Na LDB, base comum e parte diversificada se articulam. Não são duas formações independentes, uma importante e outra decorativa. Questões regionais podem ajudar a compreender relações amplas, e o que é próximo não precisa ser tratado como simples ou homogêneo.\nLia deve evitar presumir que todos os estudantes conhecem a mesma feira ou vivem as mesmas experiências. Materiais e perguntas precisam permitir participação e ampliar o estudo além do relato de quem já conhece o local.'),
    anim('scale','Contextualizar também é construir conexões','Compare “Comunidade”, “Município” e “Rede regional”. A cena trabalha acessos e circulação; use-a para perguntar que relações uma proposta curricular pode construir entre o vivido e outros recortes. Os três controles não são níveis de autoridade normativa.'),
    table('Leia o currículo antes de aplicar',['Conferência','Efeito sobre a decisão'],[
        ['Etapa, rede e edição.','Evitar aplicar a referência de outra oferta como se fosse a mesma.'],
        ['Normas e atos pertinentes.','Compreender adoção, organização e atualizações.'],
        ['Relação entre aprendizagens e contexto.','Selecionar um caso que ajude a construir o objetivo.'],
        ['Progressão e conhecimentos da turma.','Planejar apoios e relações que serão ampliadas.']]),
    call('Transfira o raciocínio','Uma matriz publicada por outro estado pode ser objeto de comparação, mas não demonstra a grade da turma de Lia. Compare competências dos órgãos, etapa, período e oferta antes de transformar o exemplo em regra local.'),
    text('Ponte para a escola','A rede organiza referências, mas a escola também assume compromissos e define sua proposta. Vamos distinguir PPP, regimento e plano docente para compreender essa passagem.')
], 'Contextualizar é relacionar aprendizagens, problemas e fontes ao território e ao percurso da turma. Currículos devem ser lidos por etapa, rede, edição e atos pertinentes; um documento local não é automaticamente a regra de qualquer oferta.',match('Associe a leitura ao cuidado',[
    ['Documento do Pará de 2019 para Infantil e Fundamental.','Respeitar a etapa e a edição indicadas.'],
    ['Matriz de outro estado.','Usar para comparação sem presumir aplicação à rede de Lia.'],
    ['Escolha de um caso conhecido pela turma.','Relacionar contexto e aprendizagem, sem encerrar na lista local.'],
    ['Base comum e parte diversificada.','Articular a formação e o contexto.']]))

lesson(9,'PPP, regimento e plano: decidir na escola','Autonomia envolve compromissos e participação',20,[
    text('A equipe precisa conversar sobre seu projeto','Lia preparou a sequência, mas a escola já assumiu compromissos sobre participação, leitura de fontes e acompanhamento da aprendizagem. Como seu plano dialoga com eles? A proposta pedagógica e o projeto político-pedagógico, o PPP, participam dessa organização coletiva.\nO PPP expressa finalidades, contexto e compromissos do trabalho educativo. Deve orientar decisões e ser construído e acompanhado com participação, no âmbito das normas aplicáveis. Os arts. 12 a 14 da LDB ajudam a compreender responsabilidades da escola, do docente e da gestão democrática do ensino público.'),
    picture('u14-curriculo-ppp-plano.png','Uma decisão ganha forma em diferentes instrumentos','Currículo, PPP e plano têm funções que se articulam. Copiar o texto de um documento no outro não demonstra que a sequência foi planejada para a turma.'),
    table('Diferencie as funções no caso',['Instrumento','Pergunta que ajuda a responder'],[
        ['PPP ou proposta pedagógica.','Que finalidades e compromissos coletivos orientam o trabalho da escola?'],
        ['Regimento escolar.','Como se organizam regras, procedimentos e responsabilidades, conforme as normas?'],
        ['Plano de trabalho ou de ensino.','Como o docente organiza objetivos, percurso e avaliação em relação à proposta?'],
        ['Plano de aula.','Que intervenções e materiais serão usados nesta situação de aprendizagem?']]),
    compare('Uma regra escolar precisa de fundamento','Decisão precipitada','“O PPP decidiu, então podemos deixar de oferecer uma aprendizagem assegurada por norma.” A decisão coletiva foi tomada como autorização para contrariar direitos e referências aplicáveis.','Decisão fundamentada','Reexaminar a proposta, identificar as normas e construir uma organização compatível. A participação sustenta decisões, mas não transforma o PPP em poder de revogar uma lei.'),
    text('Autonomia não é ausência de vínculo','Lia pode ajustar fontes, linguagem e sequência, acompanhando as respostas. Precisa mostrar por que o ajuste contribui para a aprendizagem e como se relaciona aos compromissos escolares. A responsabilidade profissional não se resolve nem em obedecer mecanicamente a um formulário nem em escolher sem justificativa.\nO regimento também precisa ser lido em sua função. Uma regra de avaliação local deve ser confrontada com a LDB e as normas do sistema. O nome do documento não comprova que qualquer conteúdo nele escrito está correto ou atualizado.'),
    text('A avaliação devolve perguntas ao projeto','Se a turma participa, mas não compara fontes, Lia pode analisar a diferença entre os compromissos e as condições efetivas de aprendizagem. Isso pode levar ao replanejamento e a uma discussão coletiva sobre materiais, apoios e tempo.\nO PPP não se esgota na redação inicial. Acompanhá-lo envolve examinar se os compromissos orientam o trabalho e quais condições precisam ser construídas para realizá-los.'),
    call('Exemplo para a prova','“Como a proposta é coletiva, o professor não precisa elaborar plano de trabalho.” A conclusão apaga uma responsabilidade docente prevista na LDB. A articulação dos instrumentos exige decisões em diferentes planos.')
], 'PPP, regimento e planos organizam funções diferentes do trabalho escolar. Participação e autonomia se articulam a direitos, normas e responsabilidades; documentos coletivos precisam orientar e ser acompanhados na prática.',match('Associe instrumento e função',[
    ['PPP.','Finalidades e compromissos coletivos da escola.'],
    ['Regimento.','Organização de regras e procedimentos escolares.'],
    ['Plano de trabalho.','Percurso docente articulado à proposta pedagógica.'],
    ['Plano de aula.','Intervenções e tarefas da situação de aprendizagem.']]))

lesson(10,'Diversidade, ambiente e campo: direitos no currículo','Contextualizar também exige reconhecer sujeitos e barreiras',23,[
    text('O estudo geográfico envolve sujeitos e direitos','Lia quer investigar território e circulação. Precisa escolher fontes que reconheçam a diversidade e evitem representar grupos como se tivessem uma única história. A escolha curricular envolve direitos que não são opcionais apenas porque o tema parece distante do capítulo do livro.\nO art. 26-A da LDB, com a redação da Lei 11.645/2008, torna obrigatório o estudo da história e cultura afro-brasileira e indígena no Ensino Fundamental e no Médio, públicos e privados. A Lei 10.639/2003 integra a trajetória dessa inclusão. O estudo ocorre no âmbito do currículo, com destaque legal a certas áreas, sem restringi-lo somente a elas.'),
    text('A Geografia participa de uma abordagem contínua','Territórios, trabalho, produção do espaço e representações podem ser investigados com fontes e perspectivas diversas. Isso exige cuidado conceitual e histórico, evitando transformar povos e comunidades em ilustrações fixas de um passado sem presença contemporânea.\nA obrigação não se cumpre apenas por incluir um nome em uma data comemorativa. No caso, Lia pode confrontar mapas e narrativas sobre território e circulação, justificando a aprendizagem e reconhecendo limites e autoria das fontes.'),
    text('Educação ambiental como relação permanente','A Lei 9.795/1999 prevê educação ambiental integrada, contínua e permanente. Na Educação Básica, um projeto de Geografia deve construir relações ao longo do trabalho, em vez de depender apenas de uma atividade isolada. As alterações da Lei 14.926/2024 incluem temas como clima, biodiversidade e riscos e emergências socioambientais nos projetos institucionais e pedagógicos, segundo as diretrizes pertinentes.\nEstudar condições de acesso em períodos chuvosos pode relacionar natureza, ocupação e infraestrutura. A escolha exige fontes e objetivos; a presença de uma foto de rio não comprova por si só a abordagem ambiental.'),
    picture('u12-rio-guama.jpg','O contexto ajuda a formular uma questão','Rio Guamá visto do campus da UFPA em 2019. A fotografia é uma fonte identificada, não um diagnóstico sobre comunidades nem prova de como uma escola organiza o currículo.'),
    text('Educação do campo e inclusão pedem condições concretas','O art. 28 da LDB prevê adequações às peculiaridades da vida rural e de cada região, incluindo conteúdos e metodologias, organização escolar e calendário em relação a ciclos agrícolas e condições climáticas. A adequação precisa ser organizada pelos sistemas, respeitando as exigências aplicáveis; não é uma licença individual para cancelar direitos ou reduzir a formação.\nA Lei Brasileira de Inclusão, 13.146/2015, também exige considerar acesso, participação e aprendizagem, com eliminação de barreiras e apoios pertinentes. Adaptar um mapa ou oferecer outra forma de acesso ao material pode preservar a relação conceitual que se pretende ensinar.'),
    anim('inequality','Um tema ambiental pode virar problema de estudo','Compare as condições de acesso com os dois controles. Pergunte que fontes e relações a turma precisaria investigar. A cena é hipotética e não calcula risco; sua presença no plano não demonstra, sozinha, uma abordagem ambiental contínua.'),
    table('Direito e tarefa precisam se encontrar',['Problema','Decisão a justificar'],[
        ['Uma única narrativa apaga diferenças.','Confrontar fontes e sujeitos sem generalizar identidades.'],
        ['Uma atividade ambiental fica isolada.','Articular relações e acompanhamento ao longo do projeto.'],
        ['O material não pode ser usado por parte da turma.','Examinar barreiras e organizar apoios para a aprendizagem.'],
        ['A oferta do campo tem condições específicas.','Consultar normas e organizar adequações com responsabilidade.']]),
    call('Regra específica exige fonte específica','Etapas e modalidades podem ter diretrizes próprias. Para uma decisão sobre EJA, educação escolar indígena, quilombola ou outras ofertas, confira também a norma pertinente, sem transpor automaticamente uma matriz da oferta regular.')
], 'Direitos, diversidade e condições de acesso participam da organização curricular. A Geografia contribui para relações étnico-raciais e ambientais e deve considerar sujeitos, modalidades e apoios, com fontes e normas pertinentes.',match('Relacione referência e foco',[
    ['LDB, art. 26-A.','História e cultura afro-brasileira e indígena no currículo.'],
    ['Lei 9.795/1999 e alterações.','Educação ambiental integrada, contínua e permanente.'],
    ['LDB, art. 28.','Adequações da oferta para a população rural.'],
    ['Lei 13.146/2015.','Direitos da pessoa com deficiência e eliminação de barreiras.']]))

lesson(11,'PNE: objetivos, metas e estratégias de política','O plano nacional não é a sequência da aula',20,[
    text('Uma meta de política chega à conversa da escola','A equipe deseja melhorar condições de permanência e aprendizagem. Um colega pergunta se o PNE é o documento que determina os conteúdos de cada aula de Geografia. Para responder, precisamos distinguir o plano de política educacional do planejamento de ensino.\nA Lei 15.388, de 14 de abril de 2026, aprovou o novo Plano Nacional de Educação, com duração de dez anos a contar de sua publicação, em cumprimento ao art. 214 da Constituição. Ele organiza diretrizes, objetivos, metas e estratégias para políticas educacionais.'),
    picture('u14-pne.png','Dê sentido às funções do plano','O esquema retoma as funções descritas na lei de 2026. As perguntas são uma síntese autoral, não uma lista de metas oficiais ou uma prescrição de aula.'),
    text('Três termos que agora podem ser distinguidos','Objetivos indicam mudanças esperadas em relação a problemas educacionais. Metas oferecem referências qualitativas e quantitativas para verificar seu alcance em determinado intervalo. Estratégias são ações propostas aos governos para atingir objetivos e metas.\nEm um exemplo didático, melhorar condições de acesso seria uma mudança buscada; estabelecer referências para acompanhá-la no tempo teria função de meta; organizar ações de infraestrutura e apoio teria função de estratégia. Este exemplo explica funções e não reproduz uma meta específica do PNE.'),
    compare('Caso resolvido: meta e habilidade','Afirmação','“Uma meta do PNE substitui a habilidade da BNCC e define a tarefa da turma.” O raciocínio mistura decisões de política e de aprendizagem.','Análise','As políticas podem criar condições e compromissos para o ensino. A aula exige articular currículo, objetivos, mediação e avaliação; o plano nacional não entrega essa sequência pronta.'),
    text('A data evita um erro frequente','O PNE aprovado pela Lei 13.005/2014 teve sua vigência prorrogada até 31/12/2025 pela Lei 14.934/2024. No recorte atual desta unidade, não é correto apresentá-lo como se fosse o novo plano vigente de 2026. Para uma questão situada em 2018, o documento do período continua sendo uma referência histórica pertinente.\nDistinguir tempo de publicação, duração e período do problema é essencial para interpretar políticas. Uma apostila reeditada não demonstra, por si só, que seus dispositivos foram atualizados.'),
    table('Do plano à leitura crítica',['Pergunta','O que examinar'],[
        ['Qual problema de política está em foco?','Objetivos e diretrizes pertinentes.'],
        ['Como acompanhar a mudança?','Referências, prazos, indicadores e condições de análise.'],
        ['Que ações e responsabilidades participam?','Estratégias e organização de implementação.'],
        ['Como isso se relaciona à escola?','Condições e compromissos, em diálogo com currículo e proposta pedagógica.']]),
    call('Cuidado de interpretação','Uma meta pode envolver mais que uma porcentagem. O acompanhamento exige ler seu conteúdo, as referências e o período. Também não se deve confundir uma melhora observada em uma turma com o cumprimento de uma meta nacional.'),
    text('Ponte para materiais e avaliações','O plano de política pode se articular a programas e acompanhamento de resultados. Agora vamos distinguir o papel de materiais didáticos e matrizes de avaliação, que também não equivalem ao currículo completo.')
], 'O PNE de 2026 organiza políticas por diretrizes, objetivos, metas e estratégias, com duração legal definida. Não substitui currículo ou plano de aula. A leitura precisa distinguir o documento vigente e o contexto histórico da questão.',match('Associe a função ao termo',[
    ['Mudança esperada em um problema educacional.','Objetivo de política.'],
    ['Referências para verificar o alcance em um intervalo.','Meta.'],
    ['Ações propostas para atingir objetivos e metas.','Estratégias.'],
    ['Tarefas e mediação para uma turma.','Planejamento de ensino.']]))

lesson(12,'PNLD e avaliações: apoio e recorte','Livro e matriz não esgotam o currículo',20,[
    text('O material é um instrumento de trabalho','Lia encontra um capítulo que pode ajudar a investigar paisagens. Antes de seguir sua ordem, examina fontes, atividades, linguagem e relação com a aprendizagem escolhida. Um material didático pode apoiar o ensino e também precisa ser usado com julgamento profissional.\nO Programa Nacional do Livro e do Material Didático, PNLD, é disciplinado pelo Decreto 9.099/2017 e suas alterações, entre elas o Decreto 12.021/2024. Avaliar e disponibilizar materiais de apoio faz parte de sua função. A escolha e o uso precisam considerar regras e informações do ciclo pertinente.'),
    compare('Caso resolvido: o capítulo e o objetivo','Decisão automática','“O capítulo vem primeiro; portanto ele define sozinho a sequência da turma.” A ordem editorial foi tomada como uma norma curricular completa.','Decisão justificada','Lia examina o material em relação ao currículo, ao PPP e ao que os alunos precisam aprender. Pode organizar seu uso e complementações, respeitando as referências e os direitos envolvidos.'),
    text('Uma matriz de avaliação seleciona o que será observado','Sistemas e exames, como o Saeb e o Enem, têm finalidades e matrizes próprias. Uma matriz organiza um recorte para construir e interpretar instrumentos de avaliação. Esse recorte não representa, automaticamente, todos os conhecimentos, práticas e finalidades do currículo escolar.\nA leitura de resultados pode contribuir para investigar dificuldades. Não deve produzir a conclusão de que o conteúdo ausente de um teste perdeu seu valor curricular ou de que toda aula deve ser reduzida ao treinamento do formato de uma prova.'),
    table('Três funções que se relacionam',['Instrumento','Contribuição','Limite a reconhecer'],[
        ['Currículo.','Organiza uma proposta de formação e aprendizagens.','Não entrega, sozinho, cada intervenção da aula.'],
        ['Livro e material de apoio.','Oferecem fontes, explicações e atividades.','Não substituem todas as decisões e referências curriculares.'],
        ['Matriz de avaliação.','Delimita dimensões observadas por um instrumento.','Não esgota a formação escolar.']]),
    text('A evidência precisa ser relacionada ao objetivo','Se o teste informa que a turma localiza pontos, Lia pode usar o dado para planejar. Ainda precisa verificar se os estudantes conseguem explicar conexões, quando essa é a aprendizagem pretendida. Um resultado não permite concluir sobre todas as relações geográficas sem tarefas pertinentes.\nTambém é necessário conferir edição, etapa e finalidade da matriz. Não se pode aplicar uma referência de um exame como se fosse a mesma em todos os anos, sistemas e ofertas.'),
    call('Transfira para seu estudo para a seleção','As questões deste app ajudam a praticar interpretações do programa do edital. Seu resultado nesta unidade é uma evidência de treino, não uma previsão da nota ou substituição do estudo dos demais itens.'),
    text('Ponte para a leitura dos atos','Você já distinguiu documentos de política, referências curriculares, propostas da escola, materiais e avaliações. Vamos reunir um modo de conferir a norma e resolver casos de aplicação.')
], 'O PNLD disponibiliza apoio didático dentro de regras e ciclos; livros precisam de uso fundamentado. Matrizes de avaliação recortam dimensões do ensino e não substituem o currículo completo nem toda a evidência de aprendizagem.',match('Associe instrumento e contribuição',[
    ['PNLD.','Avaliação e disponibilização de materiais de apoio, conforme regras do programa.'],
    ['Livro didático.','Fontes, explicações e atividades a usar com julgamento.'],
    ['Matriz de avaliação.','Recorte para construir e interpretar um instrumento.'],
    ['Currículo.','Organização de uma proposta de formação e aprendizagem.']]))

lesson(13,'Ler uma norma antes de aplicá-la','Identificação, alcance, tempo e consequência',22,[
    text('Uma frase copiada precisa ser devolvida ao contexto','Um grupo apresenta uma frase retirada de uma apostila e diz que ela obriga toda escola a organizar a mesma grade. Lia precisa reconstruir a origem da afirmação antes de usá-la. Ser apresentada como norma não basta para demonstrar sua identidade ou seu alcance.\nO primeiro passo é recuperar espécie, órgão, número, ano e assunto. Depois, localizar o texto oficial e examinar a redação do dispositivo, as alterações e a vigência. Também é necessário identificar etapa, modalidade, território e competência relacionados à decisão.'),
    picture('u14-ler-norma.png','Quatro perguntas organizam a conferência','O esquema é um roteiro de estudo, não uma norma adicional. Cada resposta deve ser relacionada ao caso e sustentada pelo instrumento pertinente.'),
    table('Reconstrua a aplicação',['Conferência','Exemplo de erro que ajuda a evitar'],[
        ['Identificação completa.','Aplicar outra resolução com o mesmo número.'],
        ['Etapa, modalidade e rede.','Tomar uma matriz de outra oferta como regra da turma.'],
        ['Redação, vigência e transição.','Usar um dispositivo alterado como se estivesse intacto.'],
        ['Efeito que o texto realmente produz.','Deduzir uma grade semanal de um total geral de horas.']]),
    compare('Caso resolvido: novo título, texto antigo','Situação','Uma apostila de 2026 repete uma organização do Ensino Médio anterior à Lei 14.945/2024 e não explica o período de aplicação.','Raciocínio','A data da capa não comprova atualização do conteúdo. É preciso confrontar o dispositivo e a situação de oferta com fontes oficiais e regras pertinentes, sem transferir o texto automaticamente para a turma.'),
    text('Vigência, implementação e situação concreta','Uma lei pode fixar quando entra em vigor e também estabelecer implementação ou transição. Essas funções precisam ser distinguidas. A aplicação de uma organização curricular a certa turma exige ler o dispositivo e as normas pertinentes ao percurso, em vez de presumir mudança instantânea e idêntica em qualquer escola.\nTambém não é adequado aplicar uma norma futura apenas porque ela foi anunciada. Notícias, projetos e minutas podem informar o debate; a obrigação precisa ser relacionada ao ato e aos efeitos juridicamente pertinentes.'),
    text('Responda apenas o que as informações permitem','Suponha que o caso informe a carga total da formação geral, mas não a matriz da rede. Você pode reconhecer a função do total e indicar que falta fonte para afirmar horas semanais de Geografia. Essa delimitação demonstra leitura, não falta de conhecimento.\nO mesmo vale para uma norma local: conhecer seu texto não prova, sozinho, que o órgão tinha competência para criar qualquer regra. A análise precisa considerar os fundamentos e o conjunto normativo aplicável.'),
    call('Registre a referência junto com a interpretação','Ao estudar, anote identificação, dispositivo, função e uma consequência para o ensino. Isso ajuda mais que guardar somente o número da lei, e facilita retomar a fonte quando houver alteração.'),
    text('Ponte para a prova','Na última lição, você vai resolver um caso integrado e organizar um argumento sobre documentos e ensino de Geografia. Use o roteiro para sustentar as relações e evitar listas de siglas sem função.')
], 'Aplicar uma norma exige identificação completa, leitura oficial, alcance, redação e tempo de aplicação. A conclusão deve respeitar o que o dispositivo informa e o que depende de outras decisões e fontes.',order('Confira a afirmação normativa',[
    'Recuperar identificação, órgão e assunto do instrumento.',
    'Ler texto oficial, alterações e regras temporais pertinentes.',
    'Relacionar etapa, oferta, rede e competência ao caso.',
    'Justificar a consequência e indicar informações que ainda faltam.' ]))

lesson(14,'Casos de prova e argumento escrito','A sigla só ajuda quando sua função fica clara',23,[
    text('Retome a decisão de Lia com o percurso completo','Lia quer que a turma explique mudanças na paisagem a partir de registros da feira. Precisa assegurar participação, articular aprendizagem e contexto, planejar tarefas e avaliar justificativas. Cada documento contribui para uma dimensão dessa decisão.\nConstituição e LDB fundamentam direitos e organização. DCN e BNCC têm funções normativas próprias. Currículo, PPP e planos organizam o trabalho. Programas, materiais e avaliações contribuem sem substituir toda a formação. A análise precisa mostrar essas funções, respeitando tempo e alcance.'),
    compare('Questão resolvida 1: base comum e aula','Enunciado','“Como a BNCC é comum, basta copiar EF06GE01 para que todas as turmas aprendam pela mesma sequência.”','Resolução','A base comum não comprova uma única mediação. É preciso interpretar a aprendizagem, escolher fontes, organizar comparação e analisar produções. O código identifica a habilidade, não executa o ensino.'),
    compare('Questão resolvida 2: norma e consequência','Enunciado','“O total da formação geral básica determina sozinho quantas aulas semanais de Geografia uma turma terá.”','Resolução','Identifique o alcance do dado. A carga total se refere à formação; distribuição semanal exige consultar matriz e normas da oferta. Não se deve inventar a informação ausente.'),
    call('Use a cena para pensar o planejamento','Avance por relato, pergunta, conceito e explicação. Depois relacione a progressão a uma aprendizagem e aos instrumentos que participam do plano. A cena é didática e não representa a execução automática de uma habilidade da BNCC.'),
    anim('mediation','Uma referência se realiza em decisões de mediação','Os quatro controles mostram uma passagem do relato sobre acesso à escola à explicação com relações geográficas. O exemplo pode ser analisado no planejamento, com atenção às aprendizagens, aos apoios e às evidências.'),
    text('Construa uma tese e desenvolva sua função','Uma ideia central possível é: “Referências curriculares e normas orientam direitos e aprendizagens, mas sua realização exige interpretação e planejamento no contexto escolar”. Depois explique como essa relação aparece em uma decisão de Geografia.\nPor exemplo: “Ao comparar paisagens, Lia mobiliza uma aprendizagem da BNCC e a articula ao currículo e à proposta da escola. Seleciona fontes datadas, orienta justificativas e examina outra situação. As produções permitem avaliar se os alunos usam a relação, enquanto apoios e retomadas procuram assegurar participação e aprendizagem”. O exemplo sustenta a tese.'),
    table('Quatro movimentos para escrever',['Movimento','O que desenvolver'],[
        ['Responder ao problema.','Apresentar a relação entre documento, direito e ensino.'],
        ['Distinguir instrumentos.','Explicar funções pertinentes, sem trocar lei, base, currículo e plano.'],
        ['Analisar uma decisão.','Mostrar aprendizagem, fontes, mediação e condições de participação.'],
        ['Avaliar e delimitar.','Indicar evidência e respeitar o alcance e a data das informações.']]),
    call('Revisão ativa','Explique sem consultar: por que PCN e BNCC não são instrumentos equivalentes? Como LDB articula base comum e parte diversificada? O que a regra geral do Ensino Médio não permite concluir sozinha? Qual é o PNE do recorte de 2026? Como livro e matriz se relacionam ao currículo?'),
    text('Da unidade ao treino','O simulado contém vinte casos autorais com comentários para todas as alternativas. A oficina propõe uma redação de até vinte linhas com autoavaliação e um modelo. Os exercícios treinam o raciocínio, sem se apresentar como questões oficiais ou previsão da seleção.\nSe a resposta ficou em uma lista de siglas, retome a função de cada instrumento no caso. O avanço está em explicar a relação entre referências, decisões e aprendizagem com precisão e fontes.')
], 'Uma resposta consistente relaciona instrumentos, direitos e decisões de ensino. Explique funções, use um caso analisado e indique evidência de aprendizagem, respeitando período, competência e alcance das fontes.',order('Organize um argumento fundamentado',[
    'Responder ao tema com uma ideia central.',
    'Explicar as funções dos instrumentos pertinentes.',
    'Analisar uma decisão de ensino com fontes e mediação.',
    'Indicar evidência de aprendizagem e delimitar a conclusão.' ]))



questions=[]


def question(n,stem,correct,why,distractors,tag,pool='lesson'):
    assert len(distractors)==3
    count=sum(q['pool']==pool for q in questions)+1
    questions.append(dict(id=('f' if pool=='final' else 'q')+f'{count:02d}',lesson=f'l{n:02d}',
                          stem=stem,options=[correct]+[a for a,_ in distractors],answer=0,
                          feedback=[why]+[f for _,f in distractors],tag=tag,pool=pool,type='single'))


question(1,'Lia quer identificar uma aprendizagem essencial de Geografia. Por onde deve começar, articulando depois o planejamento?',
 'Pela BNCC e pelo currículo pertinente à etapa e à rede.',
 'A referência de aprendizagem precisa ser interpretada no percurso curricular e convertida em tarefa e mediação.',[
 ('Pela ordem dos capítulos do livro, tomada como lei.','A organização editorial não equivale a uma norma curricular completa.'),
 ('Por uma meta nacional, considerada uma habilidade pronta.','Meta de política e habilidade curricular têm funções diferentes.'),
 ('Pelo número de uma resolução sem ano ou assunto.','A identificação incompleta impede conhecer o instrumento e sua aplicação.')],'funções dos documentos')
question(1,'O que distingue um plano de aula de uma referência curricular?',
 'O plano organiza intervenções e tarefas para realizar uma aprendizagem em uma situação concreta.',
 'A referência orienta a aprendizagem, mas não escolhe automaticamente todos os materiais e apoios.',[
 ('O plano pode revogar qualquer norma porque é mais próximo da turma.','A autonomia do planejamento não autoriza contrariar direitos e normas aplicáveis.'),
 ('O plano é apenas a transcrição de códigos sem decisões de ensino.','Planejar exige organizar tarefas, mediações e critérios de acompanhamento.'),
 ('A referência já determina um único exemplo para todas as turmas.','Uma aprendizagem comum pode ser trabalhada em contextos e propostas diferentes.')],'referência e planejamento')
question(1,'Uma colega diz que o livro define sozinho o que é obrigatório ensinar. Qual análise é adequada?',
 'O livro é apoio; seu uso deve ser relacionado a currículo, normas e aprendizagem.',
 'A existência de um capítulo não o transforma em toda a referência normativa e curricular.',[
 ('A aprovação do material elimina qualquer decisão docente.','O professor precisa interpretar fontes e tarefas em relação à turma e ao objetivo.'),
 ('O livro não pode contribuir para nenhuma aprendizagem.','Materiais podem apoiar o ensino quando usados com critérios e mediação.'),
 ('Qualquer livro recente substitui a LDB consolidada.','Data editorial e função de uma lei não são equivalentes.')],'material e norma')
question(1,'Antes de aplicar uma frase apresentada como norma, é necessário:',
 'Identificar ato, órgão, período, assunto e alcance pertinente ao caso.',
 'A aplicação depende da natureza do instrumento e da situação que regula.',[
 ('Escolher o documento mais colorido como fonte definitiva.','A apresentação visual não comprova identidade nem vigência normativa.'),
 ('Presumir que todo texto nacional é uma lei.','Há documentos nacionais de naturezas e efeitos diferentes.'),
 ('Usar apenas a data da capa para decidir que tudo está atualizado.','O conteúdo precisa ser confrontado com a fonte e suas alterações.')],'leitura inicial de atos')

question(2,'Um material único não pode ser usado por parte da turma. A igualdade de condições exige que Lia:',
 'Examine barreiras e organize recursos e mediações pertinentes à participação e à aprendizagem.',
 'Oferecer um suporte idêntico não demonstra que todos possuem condições efetivas de usá-lo.',[
 ('Considere o acesso resolvido porque o arquivo foi disponibilizado.','Disponibilidade nominal não elimina barreiras de uso e participação.'),
 ('Abandone a aprendizagem para evitar qualquer adaptação.','Apoios podem ampliar o acesso ao conhecimento, em vez de suprimi-lo.'),
 ('Avalie somente quem já consegue usar o suporte original.','A decisão não enfrenta as condições de participação dos demais estudantes.')],'direito e participação')
question(2,'Qual critério respeita melhor liberdade e pluralismo em um debate de Geografia?',
 'Precisão conceitual, fontes e coerência dos argumentos, sem nota por concordância pessoal.',
 'A aprendizagem pode ser examinada sem exigir adesão à preferência do professor.',[
 ('Maior nota para a posição escolhida por Lia.','A adesão pessoal não comprova a qualidade da interpretação.'),
 ('Aceitar qualquer afirmação como verdadeira por ser opinião.','Pluralismo não dispensa o exame das fontes e da consistência das explicações.'),
 ('Impedir todas as perguntas que apresentem perspectivas diferentes.','Confrontar interpretações pode participar do trabalho com conhecimentos e direitos.')],'pluralismo e avaliação')
question(2,'No art. 205 da Constituição, o direito à educação relaciona-se a:',
 'Desenvolvimento da pessoa, cidadania e trabalho, com responsabilidades e colaboração social.',
 'A finalidade educativa é ampla e não se reduz a uma única dimensão de treinamento.',[
 ('Preparação exclusiva para uma prova padronizada.','A formação prevista não se esgota no desempenho em um instrumento.'),
 ('Escolha individual que elimina responsabilidades do Estado.','O dispositivo atribui deveres e não transforma a educação em responsabilidade apenas individual.'),
 ('Um método único que deve ser repetido em qualquer aula.','A finalidade constitucional não entrega uma metodologia idêntica para todos os contextos.')],'fundamentos constitucionais')
question(2,'A autonomia docente, em uma leitura fundamentada, envolve:',
 'Decisões profissionais justificadas em relação a direitos, normas e aprendizagens.',
 'Autonomia se articula a responsabilidade e julgamento, sem equivaler à ausência de referências.',[
 ('Poder de excluir qualquer aprendizagem assegurada por norma.','A decisão individual não autoriza cancelar direitos e referências aplicáveis.'),
 ('Ausência de toda escolha, pois cada aula já vem pronta.','As referências não substituem todas as decisões de mediação e planejamento.'),
 ('Obrigação de avaliar estudantes pela posição do professor.','O critério precisa ser relacionado à aprendizagem e à qualidade do argumento.')],'autonomia e direitos')

question(3,'A articulação prevista no art. 26 da LDB permite analisar o estudo da feira como:',
 'Uma contextualização que deve dialogar com a base comum e o percurso curricular.',
 'Base comum e parte diversificada se articulam, sem reduzir a formação a exemplos idênticos ou curiosidades isoladas.',[
 ('Um tema local que dispensa toda aprendizagem comum.','Contextualizar não significa excluir direitos e relações da formação comum.'),
 ('Um tema proibido porque não seria igual em todas as escolas.','A base comum não impõe uma única situação de estudo.'),
 ('Uma atividade complementar sem relação com qualquer objetivo.','A pertinência exige mostrar a aprendizagem que o contexto ajuda a construir.')],'base comum e contexto')
question(3,'Segundo as responsabilidades discutidas nos arts. 12 e 13 da LDB, a relação entre proposta e plano é:',
 'A escola elabora e executa sua proposta, com participação docente; o plano de trabalho se articula a ela.',
 'As responsabilidades se encontram na organização do trabalho e não se substituem mutuamente.',[
 ('O professor fica dispensado de planejar quando existe proposta coletiva.','A proposta não elimina a elaboração e o cumprimento do plano de trabalho docente.'),
 ('A escola não pode ter proposta porque cada aula é independente.','A legislação atribui responsabilidades à instituição e aos profissionais.'),
 ('O plano docente pode contrariar qualquer compromisso ou norma.','As escolhas precisam ser justificadas no conjunto das referências aplicáveis.')],'responsabilidades de planejamento')
question(3,'Avaliação contínua e cumulativa, no recorte do art. 24, V, da LDB, significa:',
 'Acompanhar o desempenho e valorizar aspectos qualitativos e resultados do percurso.',
 'O dispositivo não reduz a avaliação a uma prova final e também não proíbe todo uso de notas e provas.',[
 ('Proibir qualquer instrumento quantitativo em toda situação.','A prevalência qualitativa não é uma proibição genérica de notas ou medidas.'),
 ('Considerar uma única nota final suficiente para todo o percurso.','A regra destaca continuidade, cumulação e resultados ao longo do período.'),
 ('Registrar apenas presença sem examinar a aprendizagem.','Frequência e evidência de aprendizagem não são a mesma dimensão.')],'avaliação na LDB')
question(3,'Para afirmar o que a LDB dispõe no recorte atual, Lia deve:',
 'Consultar a redação consolidada e as alterações pertinentes ao dispositivo.',
 'A lei recebeu mudanças, e seu ano de origem não comprova que cada artigo conserva a redação inicial.',[
 ('Usar sempre o primeiro texto publicado em 1996.','Uma redação histórica pode não ser a que se aplica à situação atual.'),
 ('Confiar apenas na data de impressão de uma apostila.','A capa não demonstra atualização normativa do conteúdo.'),
 ('Considerar qualquer resumo mais recente superior à lei.','A síntese pode ajudar, mas não substitui a conferência da fonte e de seu alcance.')],'redação consolidada')

question(4,'Qual leitura distingue PCN e BNCC?',
 'Os PCN são referências pedagógicas históricas; a BNCC define aprendizagens essenciais em função normativa.',
 'A comparação preserva natureza e contexto, sem tornar os instrumentos equivalentes pelo caráter nacional.',[
 ('Ambos são leis com as mesmas funções e efeitos.','A palavra nacional não torna idêntica a natureza dos documentos.'),
 ('A BNCC determina cada aula e elimina o currículo da rede.','Ela não entrega uma única metodologia nem substitui todas as decisões curriculares.'),
 ('Os PCN não podem ser objeto de estudo porque são antigos.','Referências históricas podem contribuir para analisar concepções e propostas de ensino.')],'PCN e BNCC')
question(4,'Uma questão analisa os PCN de Geografia em 1998. O candidato deve:',
 'Interpretar o documento e o problema no contexto temporal indicado.',
 'O recorte histórico da questão não deve ser substituído automaticamente por uma regra posterior.',[
 ('Responder como se a pergunta fosse sobre a matriz de 2026.','Isso pode produzir anacronismo e não enfrentar o problema proposto.'),
 ('Ignorar o documento porque toda fonte anterior perdeu valor de análise.','Antiguidade não elimina a possibilidade de estudo histórico e pedagógico.'),
 ('Transformar qualquer proposta do texto em obrigação atual universal.','Valor de estudo e vigência normativa não são equivalentes.')],'contexto histórico')
question(4,'A leitura das orientações pedagógicas de 2006 pode contribuir para:',
 'Discutir propostas e concepções, confrontando sua aplicação com normas e contexto pertinentes.',
 'Uma referência histórica pode participar da reflexão sem comprovar que toda organização permanece atual.',[
 ('Fixar, sozinha, a grade atual de qualquer escola.','Organização curricular atual exige consultar atos e matrizes aplicáveis.'),
 ('Dispensar a identificação da etapa e do assunto.','O alcance da leitura depende também desses elementos.'),
 ('Demonstrar que toda publicação oficial tem força idêntica a uma lei.','Órgãos públicos produzem instrumentos de naturezas e efeitos diversos.')],'orientações e vigência')
question(4,'Qual pergunta distingue melhor DCN de plano de aula?',
 'Que princípios e normas organizam a etapa e como o plano se fundamenta neles?',
 'As diretrizes têm função normativa; a aula exige decisões de aprendizagem em situação concreta.',[
 ('Qual dos dois é mais novo e por isso revoga automaticamente o outro?','Data não resolve, sozinha, natureza, competência e efeitos.'),
 ('Qual deles pode ser ignorado porque as funções são diferentes?','Funções distintas podem ser complementares na decisão.'),
 ('Por que toda diretriz já escolhe o material que Lia usará amanhã?','A norma de organização não entrega automaticamente cada intervenção e recurso.')],'diretriz e aula')

question(5,'No código EF06GE01, o número 01:',
 'Identifica a habilidade naquele conjunto, sem impor sozinho a semana ou a ordem de dificuldade.',
 'É preciso ler a formulação e suas relações; a numeração não substitui o planejamento.',[
 ('Determina que a habilidade só pode ser ensinada na primeira semana.','O código não é esse cronograma obrigatório.'),
 ('Define uma nota mínima de aprovação.','A identificação curricular não expressa um critério numérico de avaliação.'),
 ('Substitui a necessidade de compreender o texto da habilidade.','Reconhecer uma sigla não demonstra interpretar a aprendizagem.')],'código da habilidade')
question(5,'Qual tarefa se relaciona melhor ao exemplo da EF06GE01?',
 'Comparar registros identificados e justificar mudanças e permanências de paisagens e usos no tempo.',
 'A tarefa exige a relação de comparação, respeitando as condições e o alcance das fontes.',[
 ('Escolher a foto mais bonita, sem examinar datas e usos.','A preferência estética não realiza a comparação temporal pretendida.'),
 ('Copiar o código e encerrar a sequência.','A cópia não demonstra o uso da relação na interpretação.'),
 ('Usar qualquer par de imagens como antes e depois sem identificação.','A leitura temporal exige conferir registros e condições de comparação.')],'habilidade e tarefa')
question(5,'As unidades temáticas de Geografia no Fundamental devem ser lidas:',
 'Em articulação com objetos, habilidades e competências, com função nas perguntas de estudo.',
 'A organização ajuda a construir relações e não se resume a uma lista de nomes independentes.',[
 ('Como cinco temas que nunca podem aparecer na mesma investigação.','Um problema pode articular relações de diferentes unidades, com planejamento coerente.'),
 ('Como a ordem obrigatória de todos os capítulos do livro.','A estrutura curricular não se confunde automaticamente com a organização editorial.'),
 ('Como substitutas de qualquer habilidade específica.','Os elementos cumprem funções relacionadas, não intercambiáveis.')],'organização da BNCC')
question(5,'Registrar uma habilidade no plano comprova que a turma aprendeu?',
 'É necessário examinar tarefas e produções que demonstrem a relação pretendida.',
 'A referência registrada precisa se realizar em mediação e evidências de aprendizagem.',[
 ('Sim, porque o código realiza a mediação automaticamente.','O código não orienta sozinho a interpretação e o trabalho do aluno.'),
 ('Sim, se a turma copiou a mesma frase.','Repetir uma formulação não comprova seu uso em outra situação.'),
 ('Não há como verificar aprendizagem de conceitos com tarefas.','Produções e justificativas pertinentes podem oferecer evidências delimitadas.')],'BNCC e evidência')

question(6,'Uma citação diz apenas “Resolução 4”. Qual procedimento é adequado?',
 'Recuperar órgão, ano, assunto e texto oficial antes de aplicar a regra.',
 'O número pode se repetir; a identificação precisa ser suficiente para localizar o instrumento.',[
 ('Aplicar a primeira resolução encontrada em qualquer busca.','Pode ser outro ato, de outro órgão, período ou assunto.'),
 ('Assumir que todas as resoluções de mesmo número têm efeitos idênticos.','A identidade numérica não define conteúdo nem competência.'),
 ('Considerar que o título abreviado já informa a etapa.','O fragmento não permite essa conclusão sobre o alcance.')],'identificação dos atos')
question(6,'Qual distinção entre parecer e resolução é mais adequada?',
 'Parecer analisa e fundamenta; resolução dispõe normativamente, devendo-se conferir os efeitos e o contexto dos atos.',
 'A distinção evita chamá-los de lei ou ignorar efeitos de pareceres homologados pertinentes.',[
 ('Todo parecer é sempre uma lei que revoga a LDB.','A natureza do instrumento e a competência do órgão não permitem essa generalização.'),
 ('Nenhum parecer pode ter qualquer efeito relevante.','É preciso examinar homologação, contexto e efeitos juridicamente pertinentes.'),
 ('A resolução dispensa identificar a competência do órgão.','A função normativa continua relacionada ao alcance das atribuições.')],'parecer e resolução')
question(6,'Uma notícia anuncia que uma proposta foi discutida. Isso comprova, sozinho, uma obrigação vigente?',
 'É necessário localizar o ato e verificar publicação, efeitos e condições de vigência.',
 'Anúncio, debate e minuta não equivalem automaticamente a uma norma aplicável.',[
 ('Sim, porque qualquer notícia é uma publicação normativa.','Divulgar um debate não produz por si só o efeito de um ato normativo.'),
 ('Sim, desde que o título use a palavra obrigatório.','A força da afirmação depende da fonte e do ato, não apenas do vocabulário.'),
 ('Não se deve consultar fonte oficial porque a notícia é mais recente.','A conferência do instrumento e de seus efeitos continua necessária.')],'publicação e efeitos')
question(6,'A Resolução CNE/CEB 2/2024 e a CNE/CEB 4/2025 tratam, no recorte estudado, de:',
 'DCNEM e parâmetros de oferta dos Itinerários Formativos de Aprofundamento, respectivamente.',
 'A identificação conserva assunto, órgão e ano dos dois instrumentos do Ensino Médio.',[
 ('PCN de 1998 e plano de aula da escola.','Os títulos e as funções desses instrumentos não correspondem às resoluções citadas.'),
 ('Duas matrizes semanais idênticas para todo o Ensino Fundamental.','Os atos referidos têm outro alcance e não demonstram uma grade idêntica de Fundamental.'),
 ('Revogação de toda aprendizagem da BNCC por um livro didático.','Os atos não equivalem a uma decisão editorial ou à afirmação apresentada.')],'atos do Ensino Médio')

question(7,'No art. 35-D da LDB, Geografia integra:',
 'Ciências Humanas e Sociais Aplicadas, com Filosofia, História e Sociologia.',
 'A organização por área não significa ausência do conhecimento geográfico na formação.',[
 ('Apenas uma atividade opcional sem relação com a formação geral.','O dispositivo inclui Geografia na composição da área.'),
 ('Uma área exclusiva com carga semanal nacional deduzida do nome.','A denominação não define sozinha uma distribuição semanal.'),
 ('O PNLD, que é o único instrumento que pode oferecer Geografia.','Programa de materiais e organização das áreas têm funções diferentes.')],'Geografia no Ensino Médio')
question(7,'Na regra geral estudada após a Lei 14.945/2024, a formação geral básica tem mínimo de:',
 '2.400 horas, articulando BNCC e parte diversificada.',
 'O art. 35-C fixa essa regra e apresenta especificidade para a formação técnica e profissional.',[
 ('2.400 horas exclusivas de Geografia.','O total se refere à formação geral básica, não a um único componente.'),
 ('600 horas como regra geral da formação completa.','600 horas se relacionam ao mínimo dos itinerários, com ressalvas da oferta técnica.'),
 ('Um total definido somente pela ordem de capítulos do livro.','A organização legal não é determinada pela estrutura editorial.')],'formação geral básica')
question(7,'A regra geral do total de horas permite afirmar uma grade semanal única de Geografia?',
 'É necessário consultar matriz e normas da oferta para conhecer a distribuição concreta.',
 'O total da formação não fornece sozinho a organização semanal do componente.',[
 ('Sim, porque o número total se divide igualmente por qualquer disciplina.','A distribuição igual não decorre automaticamente da norma citada.'),
 ('Sim, porque todas as redes usam o mesmo exemplo de aula.','Aprendizagens comuns não comprovam metodologia ou grade idêntica.'),
 ('Não existe qualquer referência legal à Geografia.','O art. 35-D inclui o componente na área de Ciências Humanas e Sociais Aplicadas.')],'carga horária e matriz')
question(7,'Como tratar a oferta técnica e profissional ao ler o art. 35-C?',
 'Ler a especificidade de 2.100 horas mínimas e as condições previstas no parágrafo único.',
 'A lei prevê situação própria, inclusive possibilidade de até 300 horas para aprofundamento relacionado à formação técnica.',[
 ('Aplicar 2.400 horas de modo idêntico sem ler a oferta.','A generalização ignora a especificidade expressa do dispositivo.'),
 ('Considerar obrigatórias exatamente 300 horas adicionais em qualquer caso.','O texto prevê possibilidade de destinação de até 300 horas dentro das condições descritas, não essa regra universal.'),
 ('Deduzir que a formação técnica elimina toda a BNCC.','A especificidade não equivale a apagar as aprendizagens e exigências pertinentes.')],'regra e especificidade')

question(8,'O Documento Curricular do Pará de 2019 citado na unidade corresponde a:',
 'Educação Infantil e Ensino Fundamental, no recorte da edição identificada.',
 'É necessário respeitar etapa e edição antes de atribuir ao texto outra função.',[
 ('Uma comprovação da grade atual de qualquer turma do Ensino Médio.','O título e o recorte não sustentam essa extrapolação.'),
 ('Uma lei federal que dispensa a leitura da BNCC.','Documento curricular e legislação federal não são equivalentes.'),
 ('Uma matriz aplicável automaticamente a qualquer rede do país.','Aplicação exige conhecer oferta, sistema, rede e atos pertinentes.')],'documento do Pará')
question(8,'Qual proposta realiza contextualização curricular com mais fundamento?',
 'Usar a feira para construir uma comparação pertinente ao objetivo e ao percurso da turma.',
 'O contexto contribui para uma aprendizagem, em vez de encerrar a aula no reconhecimento local.',[
 ('Listar produtos conhecidos sem relacioná-los a nenhuma pergunta.','A familiaridade não demonstra a construção das relações pretendidas.'),
 ('Excluir a base comum porque a feira é local.','Parte diversificada e base comum precisam se articular.'),
 ('Presumir que todos os estudantes possuem a mesma experiência.','A diversidade de trajetórias deve participar da escolha de materiais e apoios.')],'contextualização')
question(8,'Uma matriz de outro estado pode ser usada para:',
 'Comparar organizações, sem presumir que ela define a oferta da turma de Lia.',
 'O estudo comparado precisa distinguir competência, rede, período e etapa.',[
 ('Fixar automaticamente a grade da rede de Lia.','A matriz de outro contexto não demonstra essa aplicação.'),
 ('Dispensar a leitura das normas locais pertinentes.','É necessário conhecer os instrumentos da oferta em questão.'),
 ('Provar que todas as redes têm decisões idênticas.','Referências comuns não tornam todos os percursos e organizações equivalentes.')],'alcance de matrizes')
question(8,'Na articulação entre base comum e parte diversificada, é adequado:',
 'Relacionar formação e contexto sem tratar a parte diversificada como decorativa.',
 'As dimensões contribuem para a formação e devem ser interpretadas em conjunto.',[
 ('Criar duas formações independentes, uma sem relação com a outra.','A separação rígida não corresponde à articulação discutida.'),
 ('Considerar todo tema próximo simples e homogêneo.','O vivido pode conter diversidade e relações complexas.'),
 ('Proibir qualquer conexão do local com processos amplos.','Contextualização pode construir relações entre lugares e escalas.')],'base e diversidade')

question(9,'O PPP ajuda a responder principalmente:',
 'Que finalidades e compromissos coletivos orientam o trabalho da escola?',
 'O projeto se relaciona ao contexto, à participação e à orientação do trabalho educativo.',[
 ('Qual lei federal a escola pode revogar?','O PPP não tem essa competência normativa.'),
 ('Qual é o único recurso permitido em toda aula?','O projeto não equivale a um material obrigatório universal.'),
 ('Como dispensar qualquer acompanhamento da proposta?','Compromissos precisam ser examinados e acompanhados na prática.')],'função do PPP')
question(9,'Qual distinção entre regimento e plano de aula é adequada?',
 'Regimento organiza regras e procedimentos; plano de aula organiza intervenções da situação de aprendizagem.',
 'As funções se articulam sem transformar os instrumentos em cópias equivalentes.',[
 ('Regimento é uma lista de habilidades da BNCC.','A função de organização escolar não se reduz à identificação de habilidades.'),
 ('Plano de aula substitui todas as normas da escola.','O planejamento deve ser relacionado aos instrumentos e direitos pertinentes.'),
 ('Os dois dispensam verificar a aprendizagem.','A organização do trabalho e suas decisões precisam favorecer e acompanhar o aprender.')],'regimento e plano')
question(9,'Uma decisão coletiva do PPP pode contrariar uma aprendizagem assegurada por norma?',
 'A proposta deve ser reexaminada e organizada de modo compatível com os direitos e normas aplicáveis.',
 'Participação não transforma o documento escolar em autorização para revogar uma lei.',[
 ('Sim, porque qualquer decisão coletiva tem força superior à legislação.','O processo de participação não produz essa competência jurídica.'),
 ('Sim, se a decisão estiver em um documento com muitas assinaturas.','Assinaturas não substituem a análise de validade e alcance.'),
 ('O PPP deve ser abandonado em vez de articulado às referências.','A proposta pode e deve orientar o trabalho, com fundamento e revisão pertinente.')],'participação e normas')
question(9,'As respostas dos alunos mostram que um compromisso do PPP não está se realizando. Qual encaminhamento é pertinente?',
 'Analisar condições e intervenções, replanejando e discutindo necessidades coletivas.',
 'Acompanhamento permite relacionar o projeto ao trabalho efetivo e às condições de aprendizagem.',[
 ('Considerar o texto cumprido apenas porque foi escrito.','A existência do registro não demonstra realização do compromisso.'),
 ('Excluir a dificuldade da discussão para conservar a aparência de sucesso.','O resultado precisa ser interpretado para orientar novas decisões.'),
 ('Dispensar o plano docente porque o problema é coletivo.','A responsabilidade coletiva não elimina decisões e responsabilidades de planejamento.')],'acompanhamento do projeto')

question(10,'A história e cultura afro-brasileira e indígena, no art. 26-A da LDB, devem ser estudadas:',
 'No âmbito do currículo do Fundamental e do Médio, sem restrição apenas às áreas destacadas no texto legal.',
 'O destaque a certas áreas não elimina a contribuição de Geografia e de outros componentes.',[
 ('Somente em uma data comemorativa, como cumprimento suficiente.','A abordagem curricular não se esgota em uma atividade isolada.'),
 ('Apenas quando o livro da turma incluir uma imagem de povos indígenas.','A obrigação não depende da presença de uma ilustração específica.'),
 ('Como histórias uniformes de grupos sem presença no presente.','A abordagem deve reconhecer diversidade histórica e contemporânea, com fontes e sujeitos.')],'relações étnico-raciais')
question(10,'A educação ambiental discutida na Lei 9.795/1999 pede, na Educação Básica:',
 'Uma prática integrada, contínua e permanente, articulada ao trabalho educativo.',
 'Projetos precisam construir relações e acompanhamento, e não depender apenas de um evento isolado.',[
 ('Uma foto de rio como prova suficiente de toda a abordagem.','A presença da imagem não demonstra objetivos, relações e continuidade.'),
 ('A exclusão de temas como clima e biodiversidade dos projetos.','A legislação e suas alterações incluem essas relações e temas no trabalho pertinente.'),
 ('Uma única atividade sem conexão com a aprendizagem da turma.','Isolamento não corresponde à integração e permanência discutidas.')],'educação ambiental')
question(10,'No art. 28 da LDB, adequações à vida rural e à região devem ser entendidas como:',
 'Organização de conteúdos, metodologias e condições da oferta pelos sistemas, respeitando exigências aplicáveis.',
 'Reconhecer peculiaridades não autoriza cancelar direitos ou reduzir a formação por escolha individual.',[
 ('Licença para qualquer professor suprimir o calendário sem regra.','A adequação exige organização e responsabilidade no âmbito pertinente.'),
 ('Proibição de usar conhecimentos comuns em escolas do campo.','Contexto e formação se articulam, sem essa exclusão genérica.'),
 ('Presunção de que todos os estudantes do campo vivem da mesma forma.','As condições e trajetórias precisam ser investigadas em sua diversidade.')],'educação do campo')
question(10,'Adaptar uma fonte que parte da turma não consegue usar deve procurar:',
 'Eliminar barreiras e assegurar participação e aprendizagem, com apoios pertinentes.',
 'A acessibilidade pode preservar a exigência conceitual e ampliar condições de participação.',[
 ('Abandonar toda relação geográfica para evitar apoio específico.','Adaptar o acesso não equivale a renunciar à aprendizagem.'),
 ('Avaliar apenas quem usa o suporte original sem dificuldade.','A escolha não enfrenta as barreiras dos demais participantes.'),
 ('Considerar a deficiência uma explicação suficiente de qualquer resultado.','É necessário examinar condições, mediações e evidências, sem reduzir a pessoa a um rótulo.')],'inclusão e barreiras')

question(11,'No recorte de 26/10/2026 desta unidade, o novo PNE foi aprovado pela:',
 'Lei 15.388/2026, com duração de dez anos a contar da publicação.',
 'A identificação distingue o novo plano da lei de 2014 e de sua prorrogação.',[
 ('Lei 13.005/2014, automaticamente prorrogada por mais dez anos sem outro ato.','A prorrogação de 2024 foi até 31/12/2025; o novo plano foi aprovado em 2026.'),
 ('Resolução CNE/CEB 4/2025, que é o plano nacional de metas.','O ato trata dos parâmetros dos itinerários de aprofundamento, não da aprovação do PNE.'),
 ('Ordem de capítulos escolhida pelo PNLD.','Material de apoio não é a lei que aprova o plano de política educacional.')],'PNE de 2026')
question(11,'Objetivos, metas e estratégias, no PNE, permitem distinguir:',
 'Mudanças buscadas, referências para verificar alcance no tempo e ações propostas aos governos.',
 'As funções se articulam no planejamento da política sem equivaler a uma sequência de aula.',[
 ('Três nomes idênticos para a habilidade de uma turma.','O plano de política tem outra função e escala de decisão.'),
 ('Somente porcentagens que dispensam ler os problemas.','Metas e objetivos precisam ser interpretados em seu conteúdo e contexto.'),
 ('Capítulos de um livro que todos devem seguir na mesma semana.','O PNE não estabelece essa organização automática do ensino.')],'funções do PNE')
question(11,'Uma questão sobre política educacional em 2018 cita o PNE de 2014. Como interpretar a referência?',
 'Considerar o documento pertinente ao período, sem substituí-lo automaticamente pelo plano de 2026.',
 'O recorte histórico orienta a leitura; vigência atual e pertinência histórica são questões diferentes.',[
 ('Descartar a referência porque o estudo ocorre em 2026.','Isso apagaria o contexto temporal informado no enunciado.'),
 ('Concluir que o PNE de 2014 é o novo plano vigente de 2026.','O novo PNE foi aprovado pela Lei 15.388/2026.'),
 ('Usar a data da reimpressão para provar que o dispositivo nunca mudou.','A capa não comprova atualização nem vigência de um conteúdo.')],'tempo e política')
question(11,'A melhora de uma turma demonstra, sozinha, o cumprimento de uma meta nacional?',
 'É preciso examinar o alcance, as referências e o período da meta, além das evidências pertinentes.',
 'Uma produção local e uma conclusão de política nacional têm amplitudes diferentes.',[
 ('Sim, porque qualquer resultado local representa todo o país.','A generalização ultrapassa o alcance da evidência apresentada.'),
 ('Sim, se a atividade usou a sigla PNE no título.','O nome não altera o alcance do resultado observado.'),
 ('Resultados escolares nunca podem contribuir para estudar políticas.','Eles podem contribuir, desde que interpretados com critérios e fontes adequados.')],'alcance das evidências')

question(12,'O PNLD, no recorte estudado, contribui principalmente para:',
 'Avaliar e disponibilizar materiais de apoio à prática educativa, segundo as regras do programa.',
 'Essa função não equivale a substituir currículo, proposta escolar e planejamento.',[
 ('Definir sozinho a sequência de cada aula de Geografia.','O uso dos materiais exige articulação com as aprendizagens e o contexto.'),
 ('Revogar dispositivos da LDB pela escolha de uma coleção.','Uma decisão de material não produz esse efeito legal.'),
 ('Garantir aprendizagem apenas pela entrega dos livros.','Disponibilização precisa se realizar em condições de uso e mediação.')],'função do PNLD')
question(12,'A matriz de uma avaliação deve ser interpretada como:',
 'Um recorte para construir e interpretar instrumentos, sem equivaler ao currículo completo.',
 'A seleção de dimensões observadas não esgota todas as finalidades e aprendizagens escolares.',[
 ('A totalidade de tudo que a escola tem direito e dever de ensinar.','Currículo e formação não se reduzem ao recorte de um instrumento.'),
 ('Uma prova de que conteúdos ausentes perderam todo valor.','Ausência no teste não demonstra ausência de pertinência curricular.'),
 ('Uma referência idêntica para todos os exames e anos.','Finalidades, etapas e edições precisam ser conferidas.')],'matriz e currículo')
question(12,'O teste informa que os estudantes localizam pontos. Para concluir sobre explicação de conexões, Lia deve:',
 'Examinar produções em que eles relacionem informações e justifiquem conexões.',
 'Uma evidência de localização não comprova sozinha todas as operações de explicação.',[
 ('Usar o acerto de nomes como prova suficiente de todo raciocínio.','Reconhecimento de pontos e explicação de relações não são equivalentes.'),
 ('Descartar os resultados porque nenhuma avaliação informa algo útil.','Resultados podem ajudar, desde que se reconheça seu alcance.'),
 ('Exigir apenas a repetição da letra correta do primeiro exercício.','A memorização da resposta não demonstra uso da relação.')],'avaliação e inferência')
question(12,'Como escolher e usar uma atividade de livro para a sequência?',
 'Examinar sua relação com objetivo, fontes, currículo e condições de aprendizagem.',
 'O julgamento docente conecta o apoio oferecido pelo material à tarefa necessária para a turma.',[
 ('Seguir a ordem editorial sem considerar conhecimentos anteriores.','A ordem pode não corresponder ao percurso e às necessidades da turma.'),
 ('Escolher apenas pela quantidade de imagens.','Recursos visuais precisam de função na aprendizagem e de interpretação das fontes.'),
 ('Presumir que a atividade já demonstra o que todos aprenderam.','Aprendizagem precisa ser acompanhada nas produções e explicações.')],'uso do material')

question(13,'Uma apostila de 2026 reproduz dispositivo anterior à alteração legal. Qual é o cuidado central?',
 'Confrontar conteúdo, redação e alcance com a fonte oficial e o período de aplicação.',
 'A data da capa não demonstra atualização de cada dispositivo.',[
 ('Considerar todo conteúdo vigente pelo ano de impressão.','Reedição e atualização normativa não são a mesma coisa.'),
 ('Aplicar a frase apenas porque está destacada em negrito.','Destaque visual não comprova vigência ou competência.'),
 ('Desconsiderar qualquer fonte oficial que explique alterações.','A conferência das mudanças é necessária para interpretar a situação.')],'atualização de fontes')
question(13,'Vigência e implementação devem ser tratadas como:',
 'Funções temporais que precisam ser lidas no ato e nas regras pertinentes à oferta.',
 'A aplicação a uma turma pode exigir conferir transição e organização do sistema.',[
 ('Prova de mudança idêntica e instantânea em toda situação.','A conclusão pode ignorar condições e regras temporais expressas.'),
 ('Permissão para ignorar toda norma já publicada.','É preciso verificar os efeitos, não dispensar automaticamente a leitura.'),
 ('Termos que a data de uma notícia resolve sozinha.','O anúncio não substitui os dispositivos que regulam esses efeitos.')],'vigência e implementação')
question(13,'O enunciado não informa a matriz semanal da rede. O candidato deve:',
 'Delimitar a conclusão e indicar a referência necessária, sem inventar a distribuição.',
 'Ler o alcance das informações é parte do raciocínio fundamentado.',[
 ('Dividir qualquer total igualmente por todas as disciplinas.','Essa operação não decorre automaticamente da norma ou dos dados.'),
 ('Atribuir a todas as escolas a matriz encontrada em outro estado.','A referência de outra oferta não demonstra aplicação ao caso.'),
 ('Concluir que Geografia não integra a formação.','A falta da grade no enunciado não apaga a referência legal ao componente.')],'limite da conclusão')
question(13,'Que registro de estudo ajuda a retomar uma norma com precisão?',
 'Identificação, dispositivo, função, período e consequência para a decisão analisada.',
 'O registro permite reconstruir o raciocínio e conferir futuras alterações.',[
 ('Apenas o número, sem órgão ou ano.','A identificação pode coincidir com outros atos e assuntos.'),
 ('Uma frase sem indicação da origem.','A ausência de fonte dificulta verificar natureza e aplicação.'),
 ('Uma conclusão universal sem registrar o caso.','A consequência pode depender de etapa, oferta e contexto temporal.')],'registro fundamentado')

question(14,'Qual argumento articula documento e decisão de ensino?',
 'Uma habilidade orienta a comparação; Lia seleciona fontes e avalia justificativas em relação ao currículo e à proposta escolar.',
 'O argumento explica funções e mostra a realização da referência em planejamento e evidências.',[
 ('A habilidade foi copiada, então a aprendizagem está comprovada.','A identificação não demonstra a relação construída pelos estudantes.'),
 ('O livro foi entregue, portanto todo o currículo foi realizado.','Disponibilização não comprova uso, mediação e aprendizagem.'),
 ('O PPP existe, então nenhuma outra norma precisa ser lida.','Os instrumentos se articulam e têm funções e alcances distintos.')],'documento e ensino')
question(14,'Antes de responder a um caso normativo, qual leitura é mais consistente?',
 'Identificar problema, período, oferta e função dos instrumentos citados.',
 'A interpretação precisa relacionar a norma e o alcance de seus efeitos ao caso.',[
 ('Escolher a sigla mais repetida sem examinar o enunciado.','Frequência de uma palavra não define a função requerida.'),
 ('Assumir que todo caso histórico usa a redação atual.','O período explícito pode exigir outra referência histórica.'),
 ('Transformar o exemplo local em regra nacional sem conferir fonte.','A generalização exige examinar competência e abrangência.')],'interpretação de casos')
question(14,'Uma redação que apenas lista Constituição, LDB e BNCC precisa ser desenvolvida por:',
 'Explicação das funções e análise de uma decisão concreta com evidência de aprendizagem.',
 'A lista se torna argumento quando mostra relações e consequências no problema proposto.',[
 ('Mais siglas sem função ou relação com o exemplo.','A quantidade não substitui a construção do raciocínio.'),
 ('Uma opinião sem fontes sobre qual documento parece melhor.','Preferência não explica natureza, alcance e aplicação.'),
 ('Uma previsão de nota baseada somente no número de leis citadas.','Citar atos não demonstra sozinho precisão e qualidade da argumentação.')],'escrita argumentativa')
question(14,'Como interpretar o resultado do simulado autoral desta unidade?',
 'Como evidência de treino que orienta revisão, sem prever a nota da seleção.',
 'O exercício cobre o recorte da unidade e não equivale ao programa completo ou à prova oficial.',[
 ('Como garantia de desempenho idêntico na seleção.','Questões, condições e abrangência da avaliação oficial são diferentes.'),
 ('Como substituição do estudo das demais unidades.','O programa tem outros itens que não se esgotam neste treino.'),
 ('Como comprovação de que os enunciados são oficiais.','Os casos foram produzidos para estudo e identificados como autorais.')],'uso do treino')


def final(n,stem,correct,why,distractors,tag):
    question(n,stem,correct,why,distractors,tag,pool='final')


final(1,'Lia quer que uma turma compare paisagens em tempos diferentes. Qual encaminhamento articula melhor as referências ao trabalho docente?',
 'Interpretar a habilidade e o currículo, relacioná-los à proposta escolar e planejar fontes, comparação e avaliação.',
 'A decisão realiza funções distintas em um percurso: referência, organização e mediação, com evidências da aprendizagem.',[
 ('Reproduzir apenas o código da BNCC, pois a identificação já determina a aprendizagem de cada estudante.','O código localiza a habilidade; não executa a tarefa nem demonstra compreensão.'),
 ('Escolher o capítulo mais recente e usá-lo como fundamento suficiente de toda obrigação curricular.','A data do material não transforma a organização editorial em referência normativa completa.'),
 ('Selecionar somente relatos locais e afastar a base comum porque o contexto é conhecido.','Contextualização e formação comum precisam se articular, sem essa exclusão.')],'articulação de instrumentos')
final(2,'O PPP aprova uma regra que exige concordância com a posição do professor para obter nota alta em um debate. Como examinar a decisão?',
 'Confrontar o critério com direitos e princípios e avaliar conceitos, fontes e argumentos, revendo a regra incompatível.',
 'A participação na proposta escolar não dá poder de cancelar fundamentos de liberdade e pluralismo.',[
 ('Considerar a regra válida porque a decisão coletiva substitui todos os fundamentos externos à escola.','O PPP deve respeitar direitos e normas aplicáveis; a forma coletiva não resolve qualquer incompatibilidade.'),
 ('Aceitar qualquer afirmação como verdadeira, sem avaliar evidências, para garantir o pluralismo.','Pluralismo não exige abandonar critérios de conhecimento e consistência.'),
 ('Evitar toda discussão de perspectivas para impedir que surjam posições diferentes.','Confrontar interpretações pode participar da aprendizagem, com critérios e respeito aos direitos.')],'pluralismo e PPP')
final(12,'Uma coleção do PNLD organiza capítulos em ordem diferente do percurso que a turma necessita. Qual análise é mais adequada?',
 'O material é apoio e pode ser organizado e complementado em relação ao currículo, à proposta escolar e à aprendizagem.',
 'A ordem editorial não substitui julgamento sobre objetivos, fontes, condições e progressão.',[
 ('A aprovação da coleção torna obrigatória a mesma ordem em todas as aulas, dispensando o currículo.','A função do programa não equivale a essa determinação completa da mediação.'),
 ('Qualquer divergência de ordem prova que o material é ilegal e deve ser descartado sem exame.','A adequação do uso exige análise; a diferença, sozinha, não sustenta essa conclusão.'),
 ('O livro deve substituir a proposta da escola porque foi publicado em data posterior.','Data editorial e função normativa ou pedagógica não produzem essa substituição automática.')],'material e decisão docente')
final(5,'O plano de Lia cita EF06GE01, mas a tarefa pede escolher a foto mais bonita sem datas ou análise dos usos. Qual revisão enfrenta diretamente o problema?',
 'Propor comparação de registros identificados e justificativas sobre mudanças e permanências, com mediação e critérios.',
 'A tarefa passa a exigir a relação da aprendizagem, em vez de usar o código como comprovação suficiente.',[
 ('Acrescentar mais códigos ao plano, preservando a tarefa sem comparação.','A quantidade de identificações não corrige a relação ausente na atividade.'),
 ('Repetir a definição de paisagem como evidência suficiente de comparação temporal.','A repetição de um conceito não demonstra o uso das fontes para comparar momentos.'),
 ('Considerar que toda imagem se torna um registro temporal adequado por ser usada na aula.','É necessário examinar identificação e condições de comparação, não apenas a presença da imagem.')],'habilidade tarefa e evidência')
final(4,'Uma questão trata dos PCN em 1998; outra pede interpretar uma decisão escolar atual. Qual leitura conserva o papel dos documentos?',
 'Analisar o contexto histórico na primeira e articular referências e normas atuais pertinentes na segunda.',
 'Pertinência histórica não equivale a declarar a mesma função e vigência para todas as situações.',[
 ('Usar sempre o documento mais novo, mesmo que a primeira pergunta peça analisar outra época.','Isso pode apagar o recorte histórico explícito do problema.'),
 ('Tomar os PCN como lei atual que fixa a sequência de qualquer escola.','O instrumento pedagógico não tem essa função universal atribuída.'),
 ('Descartar qualquer contribuição dos PCN porque a referência é anterior à BNCC.','Uma leitura histórica e pedagógica continua possível, com distinção de contexto e efeitos.')],'tempo e natureza documental')
final(6,'Uma notícia informa que um parecer discutiu nova organização curricular. Antes de apresentá-la como obrigação vigente, é necessário:',
 'Identificar o instrumento, sua homologação quando pertinente e os atos, publicação e efeitos relacionados à regra.',
 'Debate, fundamentação e norma aplicável precisam ser distinguidos e ligados ao caso.',[
 ('Usar a notícia como substituta suficiente do texto, porque seu título contém a palavra obrigatório.','O vocabulário da notícia não produz por si só a vigência e o alcance de um ato.'),
 ('Considerar todo parecer irrelevante, sem examinar seu contexto e efeitos.','Pareceres homologados podem ter efeitos pertinentes; a rejeição genérica também é inadequada.'),
 ('Tratar parecer e lei como nomes equivalentes e aplicar a frase a qualquer etapa.','Natureza, competência e abrangência dos instrumentos são diferentes.')],'parecer notícia e norma')
final(7,'O enunciado descreve a regra geral de formação do Ensino Médio após a Lei 14.945/2024, sem oferta técnica. Qual afirmação é sustentada?',
 'A formação geral básica tem mínimo de 2.400 horas e os itinerários, mínimo de 600; isso não fixa sozinho a grade semanal de Geografia.',
 'Os totais referem-se à composição da formação. A distribuição concreta exige as referências da oferta.',[
 ('As 2.400 horas pertencem exclusivamente a Geografia e devem ser repartidas igualmente entre os anos.','A carga citada não é de um único componente nem impõe essa divisão.'),
 ('O mínimo de 600 horas corresponde a toda a formação geral básica.','O valor está relacionado aos itinerários, não ao total geral básico da regra apresentada.'),
 ('A organização em áreas significa que Geografia foi excluída da formação.','O art. 35-D inclui Geografia em Ciências Humanas e Sociais Aplicadas.')],'regra geral do Ensino Médio')
final(7,'Um resumo aplica a qualquer oferta técnica os mesmos números da regra geral e afirma que sempre são necessárias 300 horas extras. Qual leitura enfrenta o erro?',
 'Consultar a especificidade legal: mínimo de 2.100 horas de formação geral e possibilidade de destinar até 300 de suas horas ao aprofundamento relacionado à formação técnica.',
 'O parágrafo único do art. 35-C apresenta condições próprias; não estabelece a obrigação universal de acrescentar exatamente 300 horas.',[
 ('Considerar o título formação técnica como dispensa de qualquer aprendizagem da BNCC.','A especificidade da composição não elimina as exigências e aprendizagens pertinentes.'),
 ('Manter os números sem ler a oferta, porque a data posterior da apostila resolve a aplicação.','Uma capa recente não corrige a generalização nem substitui a fonte.'),
 ('Dividir as 300 horas igualmente entre Geografia e História por não haver matriz no enunciado.','Essa divisão não decorre do dispositivo e inventa a informação ausente.')],'especificidade técnica')
final(11,'Em outubro de 2026, um candidato apresenta o PNE de 2014 como se tivesse sido prorrogado automaticamente por mais dez anos. Qual correção é pertinente?',
 'A prorrogação da Lei 14.934/2024 foi até 31/12/2025; o novo PNE foi aprovado pela Lei 15.388/2026, com dez anos a contar da publicação.',
 'A identificação e a duração precisam ser relacionadas aos atos, não deduzidas de uma extensão automática.',[
 ('O PNE só passa a existir quando cada professor escolhe o livro da turma.','A aprovação do plano é uma decisão legal de política, não uma escolha de material.'),
 ('O plano de 2026 vale como currículo integral de cada aula e substitui toda habilidade.','O plano de política e o planejamento de ensino têm funções diferentes.'),
 ('O documento de 2014 perde qualquer pertinência para uma questão histórica sobre 2018.','Vigência atual e análise do documento de um período histórico não se confundem.')],'atualização do PNE')
final(11,'Um exemplo didático distingue a mudança buscada, referências para acompanhá-la em certo prazo e ações governamentais para alcançá-la. No estudo do PNE, essas funções correspondem a:',
 'Objetivo, meta e estratégia, respectivamente.',
 'A distinção segue as funções de planejamento da política; o exemplo não precisa ser tomado como uma meta oficial específica.',[
 ('Habilidade, capítulo de livro e código da BNCC.','Esses instrumentos não expressam as funções de política descritas.'),
 ('Três nomes da mesma tarefa de aula, sem diferenças de função.','A mudança, seu acompanhamento e as ações têm funções articuladas, mas distintas.'),
 ('Regimento, fotografia e prova final.','A sequência não corresponde ao papel dos elementos apresentados.')],'objetivos metas estratégias')
final(13,'Uma lei prevê vigência e também regras de implementação. Para determinar a organização aplicável a uma turma, é adequado:',
 'Conferir os dispositivos temporais e as normas pertinentes ao sistema, à oferta e ao percurso da turma.',
 'Aplicação concreta não deve ser deduzida de uma mudança idêntica e instantânea em qualquer situação.',[
 ('Usar somente a data da notícia, sem ler o ato e as regras de transição.','O anúncio não substitui as disposições que regulam os efeitos.'),
 ('Ignorar toda norma enquanto existir alguma implementação em andamento.','É necessário interpretar efeitos e etapas, não suspender genericamente a leitura.'),
 ('Aplicar uma regra futura não publicada porque o projeto parece definitivo.','Proposta e obrigação vigente precisam ser distinguidas.')],'vigência e implementação')
final(8,'Lia recebe o Documento Curricular do Pará de 2019 para Educação Infantil e Ensino Fundamental e precisa organizar uma turma de Ensino Médio em 2026. Qual conclusão é sustentada?',
 'A referência pode ser estudada em seu alcance; a organização da turma exige documentos e normas pertinentes à etapa e ao período.',
 'O título e a edição não comprovam uma matriz atual de outra etapa.',[
 ('O fato de citar o mesmo estado torna o documento suficiente para qualquer etapa e ano.','Coincidência territorial não resolve diferenças de oferta, tempo e função.'),
 ('O documento substitui a LDB porque é mais localizado.','Proximidade do contexto não produz essa competência normativa.'),
 ('Por ser de 2019, o documento nunca pode contribuir para uma análise pedagógica.','Uma referência pode ser estudada historicamente e no seu alcance sem ser aplicada indevidamente.')],'documento e etapa')
final(8,'Um colega usa uma matriz de outro estado para afirmar quantas aulas de Geografia Lia terá por semana. Qual análise é mais consistente?',
 'A matriz pode ser comparada, mas é necessário conferir a organização pertinente à rede, à oferta e ao período de Lia.',
 'O exemplo externo não demonstra a distribuição da turma em questão.',[
 ('A matriz é suficiente porque qualquer regra estadual tem abrangência nacional.','A competência e a abrangência precisam ser examinadas.'),
 ('A matriz dispensa todo exame da base e das diretrizes por ser mais detalhada.','Detalhamento não elimina a articulação e a compatibilidade entre os instrumentos.'),
 ('A distribuição deve ser inventada dividindo o total em parcelas iguais.','A operação não decorre das informações normativas e curriculares apresentadas.')],'alcance da matriz local')
final(10,'Uma escola pretende cumprir o art. 26-A da LDB apenas com uma imagem em uma data comemorativa, sem relação com o currículo. Qual revisão é mais pertinente?',
 'Organizar abordagem curricular com fontes, sujeitos e relações, reconhecendo a contribuição da Geografia e a diversidade histórica e contemporânea.',
 'A exigência não se esgota na presença de uma ilustração isolada ou numa representação uniforme dos grupos.',[
 ('Restringir a abordagem somente às áreas mencionadas com destaque e proibir contribuição de Geografia.','O destaque legal não exclui o trabalho no âmbito de todo o currículo.'),
 ('Usar a mesma narrativa como retrato completo de qualquer povo ou comunidade.','A generalização apaga diferenças e exige confronto com fontes e sujeitos.'),
 ('Adiar toda abordagem até que o livro apresente uma seção específica.','A obrigação curricular não depende dessa condição editorial.')],'direitos e relações étnico-raciais')
final(10,'O plano registra educação ambiental, mas prevê apenas mostrar uma foto de rio sem pergunta, continuidade ou avaliação. O que falta desenvolver?',
 'Relações e objetivos integrados ao percurso, com fontes, mediação e acompanhamento, em coerência com a prática contínua e permanente.',
 'O registro do tema e a presença de um recurso não demonstram a realização da abordagem curricular.',[
 ('Uma declaração de que nenhuma outra aula poderá discutir o ambiente.','A exclusão contraria a integração e permanência estudadas.'),
 ('A afirmação de que a foto já comprova todos os efeitos e riscos locais.','Uma imagem isolada não produz esse diagnóstico ou explicação completa.'),
 ('A troca do código da habilidade por uma lei, sem alterar o trabalho dos alunos.','Mudar a identificação no plano não constrói sozinho as relações de aprendizagem.')],'educação ambiental e planejamento')
final(10,'Uma escola do campo precisa adequar sua organização a condições regionais. À luz do art. 28 da LDB, qual encaminhamento é adequado?',
 'Consultar as referências e organizar adequações de conteúdos, metodologias e condições da oferta no âmbito responsável, preservando os direitos.',
 'A adequação reconhece peculiaridades com responsabilidade; não equivale a reduzir a formação por decisão isolada.',[
 ('Permitir que qualquer docente elimine dias e aprendizagens sem verificar norma ou organização do sistema.','O dispositivo não autoriza essa supressão individual e irrestrita.'),
 ('Tratar todos os estudantes rurais como portadores das mesmas experiências e necessidades.','A diversidade das condições deve ser investigada, não presumida.'),
 ('Excluir todas as aprendizagens comuns, porque a parte diversificada é independente.','Contexto e formação comum precisam ser articulados.')],'adequações e direitos')
final(2,'Parte da turma não consegue usar o mapa escolhido. Qual decisão articula melhor o direito à participação e o objetivo conceitual?',
 'Examinar as barreiras e organizar apoios ou fontes acessíveis que permitam construir e avaliar a relação pretendida.',
 'Adequar o acesso pode preservar a aprendizagem e ampliar participação, sem reduzir o estudante a um rótulo.',[
 ('Manter o suporte sem ajuste, tomando o mesmo arquivo como prova de condições iguais.','Disponibilidade idêntica não garante possibilidade efetiva de uso.'),
 ('Abandonar qualquer relação geográfica para quem encontra dificuldade com o suporte.','A dificuldade de acesso pede análise e apoio, não exclusão automática da aprendizagem.'),
 ('Avaliar apenas rapidez de leitura visual, embora o objetivo seja explicar conexões.','O critério não se alinha necessariamente à relação conceitual escolhida.')],'acessibilidade e aprendizagem')
final(12,'Uma matriz de avaliação não inclui uma relação presente no currículo. Um grupo propõe retirar essa relação de todas as aulas. Qual análise enfrenta a proposta?',
 'A matriz é um recorte de avaliação; sua seleção não esgota a formação nem prova a perda de pertinência curricular.',
 'Os instrumentos têm funções distintas, e resultados devem ser interpretados no seu alcance.',[
 ('Todo currículo deve ser reduzido exatamente aos itens do teste, porque avaliar equivale a formar integralmente.','O recorte de um instrumento não representa a totalidade dos direitos e finalidades educativas.'),
 ('A ausência do item comprova que nenhuma fonte ou conceito relacionado tem valor de estudo.','Essa conclusão extrapola o que a matriz informa.'),
 ('Nenhum resultado de avaliação pode contribuir para replanejar.','Resultados podem ser úteis quando articulados ao objetivo e a outras evidências.')],'matriz e formação')
final(9,'A equipe escreveu compromissos no PPP, mas as produções indicam que a turma ainda não compara fontes. Qual decisão é mais coerente?',
 'Examinar intervenções e condições, replanejar e discutir apoios coletivos para realizar os compromissos.',
 'O acompanhamento liga o documento à aprendizagem e permite revisar escolhas e condições.',[
 ('Considerar a aprendizagem comprovada pela existência do texto coletivo.','Um registro de intenção não demonstra o que os estudantes conseguem fazer.'),
 ('Excluir as respostas que desafiam a expectativa e manter somente exemplos favoráveis.','A seleção impede examinar dificuldades e o alcance da interpretação.'),
 ('Dispensar o plano de trabalho docente porque há proposta escolar.','As funções se articulam; a proposta não elimina a responsabilidade de planejar.')],'projeto e acompanhamento')
final(14,'Qual trecho desenvolve um argumento sobre normas e ensino de Geografia?',
 '“A habilidade orienta uma comparação; o currículo e o PPP situam o percurso. A professora seleciona fontes, media a análise e examina justificativas em outro caso.”',
 'O trecho explica a contribuição dos instrumentos e a relaciona a mediação e evidência de aprendizagem.',[
 ('“Constituição, LDB e BNCC são importantes porque possuem siglas que devem aparecer no plano.”','A frase não explica funções nem consequências para o problema de ensino.'),
 ('“A data mais recente de uma apostila basta para confirmar a vigência de todo o seu conteúdo.”','A atualização precisa ser conferida nos atos e dispositivos pertinentes.'),
 ('“Se o plano cita muitos números de leis, o domínio dos alunos já está demonstrado.”','Quantidade de referências não comprova a relação aprendida.')],'argumentação fundamentada')


flashcards=[dict(id=f'c{i:02d}',front=a,back=b) for i,(a,b) in enumerate([
 ('Qual documento consultar?','Identifique a pergunta: direito, organização, aprendizagem, currículo, proposta da escola ou mediação. Os instrumentos têm funções articuladas, não idênticas.'),
 ('Constituição, arts. 205 e 206','Finalidades e princípios do ensino fundamentam decisões sobre participação, pluralismo e aprendizagem. Não fornecem um método único de aula.'),
 ('Autonomia docente','Decisões profissionais precisam de justificativa e relação com direitos, normas e aprendizagens. Autonomia não dispensa responsabilidade.'),
 ('LDB consolidada','Consulte a redação e as alterações do dispositivo. O ano de origem da lei não comprova que todos os parágrafos continuam com o texto inicial.'),
 ('Base comum e parte diversificada','O art. 26 da LDB articula formação e características regionais e locais. Contextualizar não significa excluir a aprendizagem comum.'),
 ('LDB, arts. 12 e 13','A escola elabora e executa a proposta, com participação docente; o plano de trabalho se articula a ela. Uma função não elimina a outra.'),
 ('Avaliação contínua e cumulativa','O art. 24, V, valoriza o percurso e aspectos qualitativos. Não proíbe todo uso de notas nem reduz a aprendizagem a uma prova final.'),
 ('PCN','Referências pedagógicas históricas podem contribuir para analisar concepções e propostas. Não são uma lei que determina a mesma aula para todos.'),
 ('Orientações de 2006','Podem ser estudadas em seu contexto. Valor pedagógico de uma leitura não comprova que toda organização normativa permanece atual.'),
 ('DCN e BNCC','Diretrizes organizam princípios e normas no seu alcance; a BNCC define aprendizagens essenciais. As funções se articulam sem equivalência.'),
 ('Código EF06GE01','EF: Fundamental; 06: ano; GE: Geografia; 01: identificação no conjunto. O número não é uma semana obrigatória nem a aprendizagem já realizada.'),
 ('Habilidade e tarefa','Interpretar a relação, selecionar fontes e apoios e pedir produção pertinente. Copiar o código não substitui a mediação.'),
 ('Competência e habilidade','Competência mobiliza conhecimentos, habilidades, atitudes e valores; a habilidade explicita aprendizagens mais delimitadas no percurso. Leia suas relações.'),
 ('Parecer e resolução','Parecer analisa e fundamenta; resolução dispõe normativamente. Confira competência, homologação quando pertinente e efeitos do ato.'),
 ('Identificação completa','Órgão, espécie, número, ano e assunto. Um número isolado pode identificar documentos diferentes.'),
 ('Geografia na LDB, art. 35-D','Integra Ciências Humanas e Sociais Aplicadas com Filosofia, História e Sociologia. Integração por área não significa ausência do componente.'),
 ('Ensino Médio: regra geral de horas','Após a Lei 14.945/2024, FGB mínima de 2.400 horas e itinerários de, no mínimo, 600, com especificidades da oferta técnica e profissional.'),
 ('Oferta técnica e formação geral','O art. 35-C prevê mínimo de 2.100 horas e possibilidade de destinar até 300 de suas horas ao aprofundamento da BNCC ligado à formação técnica oferecida.'),
 ('Total de horas e grade semanal','O total da formação não define sozinho a distribuição de aulas de Geografia. Consulte matriz e normas pertinentes à oferta.'),
 ('Currículo da rede','Leia etapa, edição, atos e organização aplicável. Uma matriz de outro estado não demonstra a organização da turma.'),
 ('PPP, regimento e planos','PPP expressa compromissos coletivos; regimento organiza regras e procedimentos; planos organizam percurso e intervenções. Devem respeitar normas e direitos.'),
 ('História e cultura afro-brasileira e indígena','O art. 26-A da LDB prevê estudo no currículo do Fundamental e do Médio. O destaque a certas áreas não exclui a contribuição da Geografia.'),
 ('Educação ambiental','Lei 9.795/1999: integrada, contínua e permanente. A Lei 14.926/2024 inclui temas como clima, biodiversidade e riscos nos projetos pertinentes.'),
 ('Educação do campo','Art. 28 da LDB: adequações a peculiaridades rurais e regionais com organização responsável. Não é autorização individual para cancelar direitos.'),
 ('Inclusão e barreiras','Apoios e acessibilidade precisam permitir participação e aprendizagem. Mesmo arquivo para todos não significa condições iguais de uso.'),
 ('PNE no recorte de 2026','Lei 15.388/2026: novo plano com dez anos a contar da publicação. O PNE de 2014 teve prorrogação até 31/12/2025 pela Lei 14.934/2024.'),
 ('Objetivo, meta e estratégia','Mudança buscada; referências de alcance em um intervalo; ações propostas aos governos. Não são três nomes de uma tarefa de aula.'),
 ('PNLD','Programa de avaliação e disponibilização de apoio didático, conforme regras e ciclo. O material não substitui currículo e julgamento docente.'),
 ('Matriz de avaliação','Recorte para construir e interpretar instrumentos. Não equivale à totalidade da formação e das aprendizagens escolares.'),
 ('Aplicar uma norma','Confira identificação, fonte oficial, redação, tempo, alcance e oferta. Conclua dentro do que as informações permitem, indicando o que ainda exige outra fonte.')
],1)]


def ref(title,year,anchor,note,author='Brasil / órgão responsável'):
    return dict(title=title,author=author,year=year,url=PAGE+'#'+anchor,note=note)


references=[
 ref('Edital PROFGEO-UFPA n. 03/2026 — Anexo III, item 1.4',2026,'edital','Fonte do programa; PDF fornecido pelo estudante. Fontes selecionadas para estudo, sem atribuir ao edital uma lista obrigatória que ele não apresenta.','UFPA / PROFGEO'),
 ref('Constituição da República Federativa do Brasil — educação',1988,'constituicao','Arts. 205, 206, 210, 211 e 214; leitura do texto consolidado para os fundamentos e funções discutidos.'),
 ref('Lei 9.394/1996 — LDB, redação consolidada',1996,'ldb','Recortes: arts. 12 a 14, 24, 26, 26-A, 28 e 35-B a 36. Conferência em 26/10/2026; a lei recebeu alterações.'),
 ref('Parâmetros Curriculares Nacionais: Geografia',1998,'pcn-e-orientacoes','Terceiro e quarto ciclos do Ensino Fundamental. Leitura histórica e pedagógica, sem tratar o texto como equivalente à BNCC.','MEC / Secretaria de Educação Fundamental'),
 ref('Orientações curriculares para o Ensino Médio: Ciências Humanas e suas Tecnologias',2006,'pcn-e-orientacoes','Volume 3, com Geografia. Referência histórica de orientação pedagógica, sem inferir vigência atual de toda organização.','MEC / Secretaria de Educação Básica'),
 ref('Resoluções CNE/CEB 4/2010 e 7/2010',2010,'diretrizes','Diretrizes gerais para Educação Básica e diretrizes do Ensino Fundamental de nove anos. Confira etapa e alcance.','Conselho Nacional de Educação'),
 ref('Base Nacional Comum Curricular',2018,'bncc','Documento de aprendizagem; exemplo EF06GE01 e organização de Geografia no Fundamental. Resoluções CNE/CP 2/2017 e 4/2018 situam a instituição da BNCC.','Ministério da Educação'),
 ref('Lei 14.945/2024 — alterações na organização do Ensino Médio',2024,'ensino-medio','Leia em articulação com LDB consolidada, oferta e implementação. FGB, itinerários e especificidades técnicas não são grades semanais universais.'),
 ref('Resolução CNE/CEB 2/2024 — DCNEM',2024,'ensino-medio','Diretrizes Curriculares Nacionais para o Ensino Médio, de 13/11/2024. Texto oficial e cópia em secretaria estadual indicados na ficha.','Conselho Nacional de Educação'),
 ref('Resolução CNE/CEB 4/2025 — Itinerários Formativos de Aprofundamento',2025,'ensino-medio','Parâmetros Nacionais para Oferta dos IFAs, de 12/05/2025. A unidade usa sua identificação e função, sem inventar uma matriz da rede.','Conselho Nacional de Educação'),
 ref('Documento Curricular do Estado do Pará — Educação Infantil e Ensino Fundamental',2019,'para','Exemplo identificado por etapa e edição. Não é apresentado como matriz atual do Ensino Médio nem como adoção automática em qualquer rede.','Pará / Secretaria de Estado de Educação'),
 ref('Leis 10.639/2003 e 11.645/2008 — relações étnico-raciais no currículo',2008,'direitos','Leitura relacionada ao art. 26-A da LDB: contribuição curricular da Geografia sem restringir a abordagem a uma ilustração ou data.'),
 ref('Lei 9.795/1999, com alterações da Lei 14.926/2024',2024,'direitos','Política Nacional de Educação Ambiental. Recorte de integração, continuidade e temas nos projetos institucionais e pedagógicos.'),
 ref('Lei 13.146/2015 — Lei Brasileira de Inclusão',2015,'direitos','Recorte de direito à educação, participação, aprendizagem e condições de acessibilidade.'),
 ref('Lei 15.388/2026 — Plano Nacional de Educação',2026,'pne','Plano atual no recorte da unidade: dez anos a contar da publicação. Funções de objetivos, metas e estratégias.'),
 ref('Lei 14.934/2024 — prorrogação do PNE de 2014',2024,'pne','Prorrogação até 31/12/2025, distinguida da aprovação do novo plano de 2026.'),
 ref('Decreto 9.099/2017, com alterações do Decreto 12.021/2024',2024,'materiais-e-avaliacao','Programa Nacional do Livro e do Material Didático: apoio didático, regras e uso fundamentado.'),
 ref('Saeb — matrizes e escalas',2026,'materiais-e-avaliacao','Página institucional consultada para a função das matrizes; o ano indica a consulta, não a origem de todas as matrizes.','Inep'),
 ref('Créditos e recursos visuais da unidade 1.4',2026,'recursos-visuais','Seis esquemas novos, três fotos identificadas e quatro cenas existentes contextualizadas; todos em 16:9.','ProfGeo / Wikimedia Commons')
]

essay=dict(title='Oficina de redação · das referências à aprendizagem em Geografia',
 prompt='Analise como documentos curriculares e normas orientam o ensino de Geografia sem substituir o planejamento docente. Distinga pelo menos dois instrumentos, analise uma decisão de ensino com contexto, fontes e mediação e indique uma evidência de aprendizagem. Considere o alcance e o período das referências utilizadas.',
 maxLines=20,note='Tema autoral, em até 20 linhas digitadas, com autoavaliação formativa. Não é questão oficial nem correção automática do conteúdo.',
 rubric=[
  'Apresentei uma ideia central que responde ao tema.',
  'Distingui pelo menos dois instrumentos por sua função, sem limitar-me às siglas.',
  'Respeitei período, etapa e alcance das referências que utilizei.',
  'Analisei uma decisão concreta de ensino de Geografia.',
  'Relacionei aprendizagem, contexto, fontes e mediação.',
  'Indiquei uma evidência de uso das relações, além de copiar o código ou a definição.',
  'Delimitei as conclusões e escrevi com clareza em até 20 linhas.'
 ],model=(
  'Normas e referências curriculares orientam direitos e aprendizagens, mas sua realização exige interpretação e planejamento. Reconhecer a função dos documentos é necessário para não confundir uma base comum com uma aula pronta.\n'
  'A LDB articula base nacional comum e parte diversificada, além de relacionar proposta escolar e plano de trabalho. A BNCC define aprendizagens essenciais. Currículo e PPP situam compromissos e organização, sem autorizar a supressão dos direitos previstos nas normas.\n'
  'Ao comparar mudanças de paisagens, a professora pode usar um contexto significativo, selecionar registros identificados e orientar justificativas. A aprendizagem escolhida participa da tarefa; a simples presença de um código no plano não demonstra que os alunos construíram a relação.\n'
  'Apresentar outra situação e examinar mudanças, permanências e fontes oferece evidências para avaliar e replanejar. Também é necessário organizar apoios e enfrentar barreiras para ampliar participação e aprendizagem.\n'
  'Assim, a autonomia docente se realiza em escolhas fundamentadas e acompanhadas. A interpretação deve respeitar período, etapa, competência e alcance das fontes, evitando transformar uma regra geral ou um material de apoio em solução automática para qualquer escola.'
 ))


def save():
    path=ROOT/'content/catalog.json';catalog=json.loads(path.read_text())
    entry=next(e for m in catalog['modules'] for e in m['units'] if e['id']=='1.4')
    assert entry['revision']<=1,'Não sobrescreva uma revisão posterior.'
    for pool in ['lesson','final']:
        for i,q in enumerate(q for q in questions if q['pool']==pool):
            target=[2,0,3,1][i%4];shift=(target-q['answer'])%4;pairs=list(zip(q['options'],q['feedback']))
            if shift:pairs=pairs[-shift:]+pairs[:-shift]
            q['options']=[a for a,_ in pairs];q['feedback']=[f for _,f in pairs];q['answer']=target
    assert len(lessons)==14 and len(questions)==76 and len(flashcards)==30
    assert sum(q['pool']=='final' for q in questions)==20
    assert all(sum(q['lesson']==l['id'] and q['pool']=='lesson' for q in questions)==4 for l in lessons)
    unit=dict(schemaVersion=1,id='1.4',moduleId='1',revision=1,title=TITLE,
              shortTitle='Das normas às decisões de ensinar',
              subtitle='Documentos, direitos e currículo com casos resolvidos; fontes conferidas em 26/10/2026.',
              editalItem='1.4',legalAsOf='2026-10-26',estimatedMinutes=sum(l['minutes'] for l in lessons),
              objectives=[
               'Distinguir funções de leis, diretrizes, bases, currículos, propostas, materiais e avaliações.',
               'Interpretar identidade, competência, alcance, redação e tempo de aplicação dos atos.',
               'Articular BNCC, contexto, currículo, PPP e planejamento de Geografia.',
               'Reconhecer mudanças do Ensino Médio e o PNE de 2026 sem generalizar regras de oferta.',
               'Relacionar direitos, diversidade, acessibilidade e condições do campo às decisões curriculares.',
               'Resolver casos e argumentar com fontes, mediação e evidências de aprendizagem.'
              ],lessons=lessons,questions=questions,flashcards=flashcards,references=references,essay=essay)
    (ROOT/'content/units/1.4.json').write_text(json.dumps(unit,ensure_ascii=False,indent=2)+'\n')
    entry.update(status='published',revision=1);catalog['revision']=max(6,catalog['revision']);catalog['updatedAt']='2026-10-26'
    path.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
    print(f'Unidade 1.4: 14 lições, 56 questões de prática, 20 casos no simulado, 30 cartões, {unit["estimatedMinutes"]} minutos sugeridos.')


if __name__=='__main__':save()


