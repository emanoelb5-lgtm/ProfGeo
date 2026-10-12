# ProfGeo — continuidade do projeto

Este repositório contém um aplicativo Android de estudo individual para o ENA do mestrado em Ensino de Geografia. O pedido inicial exige didática, linguagem clara, exercícios inteiramente no app, exemplos, fotos reais e animações em pixel art ou código. Toda cena e imagem de estudo deve ser exibida em 16:9.

## Próxima unidade

- O plano vem do Anexo III do edital PROFGEO-UFPA n. 03/2026, ingresso 2027. Preserve os três módulos e os quinze tópicos.
- A unidade 1.1 está publicada. Quando o proprietário pedir “próxima unidade”, prossiga para o próximo item planejado, começando pela **1.2**.
- Leia `docs/CONTEUDO.md`, o catálogo e a unidade anterior. Desenvolva uma unidade completa, com progressão didática e feedback de todas as alternativas.
- Não faça aparecer uma unidade planejada como disponível antes de existir conteúdo real. Não apresente questões autorais como oficiais nem leituras selecionadas como bibliografia obrigatória do edital.
- Preserve IDs em correções, incremente revisões e publique JSON, imagens e pacotes. Novas unidades devem chegar pelo mecanismo de conteúdo, sem impor um APK novo quando o motor já suporta os recursos necessários.
- Confirme a execução do workflow de conteúdo e a publicação do catálogo e dos pacotes. Preserve notas, respostas, favoritos e redações existentes.

## Atualizações Android

- `applicationId` permanente: `br.com.emanuel.profgeo`.
- O certificado SHA-256 público da identidade persistente é **cfccadc639798f222b959225b2de81174fbba84ad4288cd0017bf189bdbd7a54**. Nunca substitua por um certificado gerado a cada execução.
- A chave e as credenciais são privadas; não estão neste repositório público. O proprietário tem o arquivo privado **ProfGeo-Assinatura-Persistente-Backup-Privado.zip**. Recupere essa identidade no fluxo privado autorizado e leia `docs/DESENVOLVIMENTO.md` para assinar o artefato compilado no Actions.
- Compile com GitHub Actions, aumente `versionCode` quando atualizar um APK publicado e use a mesma assinatura para instalação por cima. Não mande desinstalar para atualizar.
- Entregue um link realmente publicado e verificado para `ProfGeo.apk`. Mantenha README e Releases claros.
- Execute verificações adequadas às mudanças. A suíte atual cobre conteúdo, interações, persistência, tela de celular, instalação de unidade declarativa e rejeição de pacote inválido.
