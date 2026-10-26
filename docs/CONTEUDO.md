# Criar e publicar a próxima unidade

O app lê **conteúdo declarativo**. Não baixa nem executa JavaScript, HTML ou APKs dentro dos pacotes de estudo. Uma unidade nova utiliza funções já existentes no aplicativo.

## Passos editoriais

1. Leia `content/catalog.json` e escolha o próximo item com `status: planned`; a próxima unidade é **1.4**. As unidades 1.1, 1.2 e 1.3 já estão disponíveis.
2. Desenvolva conteúdo completo, progressivo, com linguagem clara e exemplos pertinentes. Use fontes primárias, identifique a bibliografia complementar e verifique legislação ou documentos em suas versões vigentes.
3. Salve `content/units/1.4.json`. Use `schemaVersion: 1`, `id: "1.4"`, `moduleId: "1"`, `revision: 1`, título fiel ao edital, objetivos, lições, questões, cartões, referências e oficina escrita.
4. Preserve identificadores de lições e exercícios quando corrigir uma unidade já publicada. Aumente `revision` ao modificar o conteúdo. Não reutilize um ID de questão para um problema diferente.
5. No catálogo, mude a unidade correspondente para `status: "published"` e informe sua revisão. Incremente a revisão do catálogo e sua data.
6. Acrescente imagens em `content/media`, ou fontes de download em `content/media-sources.json`. Imagens e animações devem ser exibidas em **16:9**. Preserve créditos e licenças; casos inventados devem estar claramente identificados.
7. Execute `python3 tools/build_content.py --download-media` e `node --test tests/engine.test.cjs`. Confira as telas e os exercícios, principalmente enunciado, resposta e feedback.
8. Publique os arquivos em `main`. O workflow de conteúdo valida e gera `content/packages/1.4-r1.zip`, atualiza tamanho e SHA-256 no catálogo e publica os arquivos.
9. No app, **Ajustes → Buscar novas unidades**. Confira o download, abra a unidade, desligue a internet e verifique que ela permanece disponível.

## Estrutura de uma unidade

Use `content/units/1.1.json`, `content/units/1.2.json` e `content/units/1.3.json` como exemplos funcionais. Campos principais:

A 1.1 foi reescrita na revisão 2: use seu encadeamento entre problema, explicação, caso resolvido, ensino e prática como referência didática. O roteiro está em `docs/UNIDADE_1_1_REFEITA.md`. O pacote r1 da 1.1 é mantido como registro para preservar a identidade e o sentido das questões antigas.

A 1.2 também está na revisão 2, com uma aula acompanhada e explicação dos saberes nas decisões de uma professora fictícia. O roteiro está em `docs/UNIDADE_1_2.md`. Seu pacote r1 preserva os 60 problemas anteriores, agora na prática; os 20 casos do novo simulado têm IDs próprios. As autorias vigentes de ambas as unidades leem suas bases r1. Não remova nem reconstrua esses registros históricos com os scripts atuais.

A 1.3 tem 14 lições sobre conceitos, categorias e conteúdos, com investigação acompanhada e exemplos por etapa escolar. O roteiro está em `docs/UNIDADE_1_3.md`. Os esquemas são gerados em 16:9 por `tools/illustrate_unit_1_3.py` e a autoria está em `tools/author_unit_1_3.py`.

Ao acrescentar fontes, preserve os pacotes anteriores cujos conteúdos, imagens e créditos pertinentes não mudaram. O empacotador valida as imagens em toda execução e conserva os bytes de um pacote reutilizável. Pacotes novos incluem somente créditos dos arquivos usados. Os testes verificam os hashes publicados da 1.1-r2 e da 1.2-r2, evitando que um acréscimo de créditos globais altere unidades sem necessidade.

| Campo | Contrato |
|---|---|
| `schemaVersion` | `1`; uma mudança de contrato exige versão nova do motor. |
| `id`, `moduleId`, `editalItem` | Identificadores estáveis que correspondem ao plano. |
| `revision` | Inteiro crescente; atualizações só são baixadas quando maior que a revisão instalada. |
| `lessons` | `id`, `title`, `kicker`, `minutes`, `blocks`, `summary` e `practice` opcional. |
| `questions` | `id`, `lesson`, `stem`, `options`, `answer`, `feedback`, `tag`, `pool` e `type`. |
| `answer` | Índice baseado em zero; a lista de feedback tem o mesmo comprimento da lista de alternativas. |
| `pool` | `lesson` para prática após leitura; `final` para simulado da unidade. |
| `flashcards` | `id`, `front`, `back`. |
| `references` | Título, autoria, ano quando aplicável, URL opcional, papel da fonte. |
| `essay` | Tema, limite, observação formativa, critérios de autoavaliação e texto de exemplo. |

Blocos disponíveis: `text`, `callout`, `list`, `photo`, `animation`, `compare`, `table`. Fotos usam caminhos relativos `media/foto.jpg`, sem endereços remotos no texto da unidade. Animações disponíveis: `inequality`, `river`, `quantitative`, `lived`, `mediation`, `scale`, `lenses`. Para criar uma animação nova com um comportamento diferente, atualize o código do aplicativo e gere um novo APK com o mesmo certificado.

Atividades em `practice`: `match`, com pares `[enunciado, associação correta]`; `order`, com etapas em sua sequência correta. As questões objetivas podem ter de 2 a 6 alternativas, com uma resposta correta e explicação para cada alternativa.

## Download e preservação

O catálogo é consultado em `https://raw.githubusercontent.com/emanoelb5-lgtm/ProfGeo/main/content/catalog.json`. Pacotes devem permanecer nessa árvore. Limites: 8 MiB por download de unidade, menos de 32 MiB descompactados, até 499 entradas. Caminhos que saiam da pasta, extensões executáveis, schema incompatível e hashes incorretos são rejeitados. A instalação de cada pacote é preparada em uma pasta temporária antes da substituição da versão anterior; o catálogo só é substituído após a busca terminar com sucesso.

Progresso, respostas, cartões, favoritos, notas e redações ficam separados dos arquivos de conteúdo. Uma busca com falha conserva os estudos instalados. A disponibilidade de uma atualização exige conexão; o estudo de unidades salvas funciona offline.
