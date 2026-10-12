# Compilar, assinar e atualizar

## Ambiente

JDK 17; Gradle 8.9; Android SDK 35; Android Gradle Plugin 8.7.3; Kotlin 2.0.21. O Actions configura esse ambiente. Compilação local com SDK instalado:

```bash
python3 -m pip install Pillow
python3 tools/build_content.py --download-media
node --test tests/engine.test.cjs
gradle :app:assembleRelease :app:lintRelease
```

Os arquivos web são recursos locais do APK. `WebViewAssetLoader` utiliza origem HTTPS local, com carregamento de conteúdo externo bloqueado. A ponte nativa lê e salva progresso, busca pacotes com HTTPS e abre links específicos no navegador externo. Não há backend de respostas.

## Certificado persistente

A primeira versão usa uma chave exclusiva do aplicativo, gerada uma única vez. O backup privado contém o keystore e suas credenciais e fica fora do repositório público. **Não gere outra chave ao atualizar**, não publique o backup nem substitua a identidade por uma chave de depuração. Registre o SHA-256 público do certificado em `downloads/release.json` e preserve esse digest em todas as versões.

Fluxo sem segredos do Actions:

1. Compile no workflow **Android · compilar e testar**.
2. Baixe o artefato `ProfGeo-build-<commit>` aprovado. Ele contém `ProfGeo-unsigned.apk`, o conteúdo empacotado e `signing-tools/apksigner.jar`.
3. Recupere o backup privado de assinatura do **ProfGeo** pertencente ao proprietário. Use `tools/sign_build.py --build /caminho/artefato --signing /caminho/backup-extraido`.
4. O script verifica o certificado, assina e verifica o APK, conserva os arquivos de conteúdo gerados e prepara o download e os hashes.
5. Publique `downloads/ProfGeo.apk`, `downloads/ProfGeo.apk.sha256`, `downloads/release.json` e `content/app-release.json` em `main`.
6. O workflow **APK · verificar e publicar versão assinada** compara hash e certificado e publica o download em Releases.

Fluxo com segredos do Actions, quando configurados pelo proprietário: `PROFGEO_KEYSTORE_BASE64`, `PROFGEO_STORE_PASSWORD`, `PROFGEO_KEY_PASSWORD`, `PROFGEO_KEY_ALIAS` (valor `profgeo`). O workflow de compilação reconstitui o keystore apenas no runner, exporta as variáveis esperadas pelo Gradle e assina com a **mesma chave**. Nunca salve a chave ou senha em código, logs ou artefatos públicos.

## Atualizações do APK

Mantenha `applicationId = "br.com.emanuel.profgeo"`. Aumente `versionCode` e `versionName` em `app/build.gradle.kts`; atualize `content/app-release.json` e as notas da versão. Instale a nova versão sobre a anterior, sem desinstalar. O certificado e o identificador precisam ser os mesmos. Antes de mudanças grandes, use a exportação de progresso do app.

## Verificação

- Validação do catálogo, dos blocos, dos identificadores e dos feedbacks.
- Testes do motor de resposta, revisão espaçada, persistência e conteúdo declarativo.
- Testes de interface em tela de celular: leitura, animação, prática, simulado, escrita, fonte, tema e ausência de rolagem horizontal.
- Compilação e lint Android.
- Teste instrumentado no emulador Android 11: ponte nativa, conteúdo incluído, abertura das lições e persistência após recriar a atividade.
- Verificação criptográfica da assinatura e do SHA-256 antes da publicação.
