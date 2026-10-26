# ProfGeo — continuidade do projeto

Este repositório contém um aplicativo Android de estudo individual para o ENA do mestrado em Ensino de Geografia. O pedido inicial exige didática, linguagem clara, exercícios inteiramente no app, exemplos, fotos reais e animações em pixel art ou código. Toda cena e imagem de estudo deve ser exibida em 16:9.

## Próxima unidade

- O plano vem do Anexo III do edital PROFGEO-UFPA n. 03/2026, ingresso 2027. Preserve os três módulos e os quinze tópicos.
- As unidades 1.1 e 1.2 estão publicadas. Quando o proprietário pedir “próxima unidade”, prossiga para o próximo item planejado, começando pela **1.3**.
- Leia `docs/CONTEUDO.md`, o catálogo e a unidade anterior. Desenvolva uma unidade completa, com progressão didática e feedback de todas as alternativas.
- Não faça aparecer uma unidade planejada como disponível antes de existir conteúdo real. Não apresente questões autorais como oficiais nem leituras selecionadas como bibliografia obrigatória do edital.
- Preserve IDs em correções, incremente revisões e publique JSON, imagens e pacotes. Novas unidades devem chegar pelo mecanismo de conteúdo, sem impor um APK novo quando o motor já suporta os recursos necessários.
- Confirme a execução do workflow de conteúdo e a publicação do catálogo e dos pacotes. Preserve notas, respostas, favoritos e redações existentes.

## Atualizações Android

- A unidade 1.1 está na revisão didática **2**: 12 lições, 56 questões de prática, 20 casos novos no simulado e 24 cartões. `tools/author_unit_1_1.py` chama `tools/rewrite_unit_1_1.py`, que conserva os problemas anteriores a partir de `content/packages/1.1-r1.zip`. Preserve esse registro e não reutilize IDs antigos para problemas novos.
- A unidade 1.2 também está na revisão didática **2**: 12 lições com a professora fictícia Lia, 60 questões de prática, 20 casos novos no simulado, 30 cartões e 12 atividades. `tools/author_unit_1_2.py` chama `tools/rewrite_unit_1_2.py`; preserve `content/packages/1.2-r1.zip` como base imutável dos 60 problemas anteriores. O catálogo está na revisão **4**. O roteiro está em `docs/UNIDADE_1_2.md`.
- Ao produzir ou revisar material, explique o raciocínio com um caso acompanhado, articule as lições e faça a passagem entre conceito, interpretação geográfica e ensino. Explique termos no contexto e mostre resoluções antes de exigir aplicação autônoma. Não substitua esse encadeamento por listas de definições.

- `applicationId` permanente: `br.com.emanuel.profgeo`.
- O certificado SHA-256 público da identidade persistente é **cfccadc639798f222b959225b2de81174fbba84ad4288cd0017bf189bdbd7a54**. Nunca substitua por um certificado gerado a cada execução.
- A chave e as credenciais são privadas; não estão neste repositório público. O proprietário tem o arquivo privado **ProfGeo-Assinatura-Persistente-Backup-Privado.zip**. Recupere essa identidade no fluxo privado autorizado e leia `docs/DESENVOLVIMENTO.md` para assinar o artefato compilado no Actions.
- Compile com GitHub Actions, aumente `versionCode` quando atualizar um APK publicado e use a mesma assinatura para instalação por cima. Não mande desinstalar para atualizar.
- Entregue um link realmente publicado e verificado para `ProfGeo.apk`. Mantenha README e Releases claros.
- Execute verificações adequadas às mudanças. A suíte atual cobre conteúdo, interações, persistência, tela de celular, instalação de unidade declarativa e rejeição de pacote inválido.

## Interface e áreas seguras

- Desde 1.1.1, `animation-art.js` desenha as sete cenas em 640 × 360 (16:9), com cenários em cache. `animations.js` conserva os controles e as explicações e pausa os frames fora da tela ou em segundo plano. Preserve a redução de movimento.

- A partir de 1.1.0, o contêiner nativo `safeRoot` aplica barras do sistema, câmera e teclado e consome os insets. Não reaplique recuos na própria WebView.
- `body.native-safe-area` zera os recuos CSS de sistema, porque já foram descontados pelo Android. Preserve essa regra para evitar duplicação.
- `safety.js` mede a altura da navegação flutuante e reserva espaço correspondente no conteúdo. Evite substituir por um espaço fixo, que pode cortar botões com fonte maior ou tela horizontal.
- Ao abrir o teclado, a navegação e o cabeçalho de leitura recolhem e o campo ativo permanece visível. Não remova os testes de escrita e restauração.
- Confira alterações de layout em telas de 320 a 915 pixels, com fonte máxima, tema escuro e teclado. A suíte instrumentada também verifica recuos e teclado no Android 11 e 15.
