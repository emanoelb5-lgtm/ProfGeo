package br.com.emanuel.profgeo

import android.app.Activity
import android.content.Intent
import android.graphics.Color
import android.net.Uri
import android.os.Bundle
import android.view.View
import android.view.WindowManager
import android.widget.FrameLayout
import android.webkit.JavascriptInterface
import android.webkit.WebResourceRequest
import android.webkit.WebResourceResponse
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.webkit.WebViewAssetLoader
import androidx.core.view.ViewCompat
import androidx.core.view.WindowCompat
import androidx.core.view.WindowInsetsCompat
import org.json.JSONArray
import org.json.JSONObject
import java.io.ByteArrayInputStream
import java.io.File
import java.net.HttpURLConnection
import java.net.URL
import java.security.MessageDigest
import java.util.concurrent.Executors
import java.util.concurrent.atomic.AtomicBoolean
import java.util.zip.ZipInputStream

class MainActivity : Activity() {
    private lateinit var web: WebView
    private lateinit var safeRoot: FrameLayout
    @Volatile private var safeZone = "{}"
    private var darkTheme = false
    private val executor = Executors.newSingleThreadExecutor()
    private val busy = AtomicBoolean(false)
    private val prefs by lazy { getSharedPreferences("profgeo", MODE_PRIVATE) }
    private val root by lazy { File(filesDir, "content").apply { mkdirs() } }
    private var pendingExport = ""
    private val origin = "https://appassets.androidplatform.net"
    private val remote = "https://raw.githubusercontent.com/emanoelb5-lgtm/ProfGeo/main/content/"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        WindowCompat.setDecorFitsSystemWindows(window, false)
        window.setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_ADJUST_RESIZE)
        if (android.os.Build.VERSION.SDK_INT >= 28) {
            window.attributes = window.attributes.apply {
                layoutInDisplayCutoutMode = WindowManager.LayoutParams.LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES
            }
        }
        safeRoot = FrameLayout(this)
        safeRoot.clipToPadding = true
        web = WebView(this)
        web.setBackgroundColor(Color.rgb(247, 248, 242))
        web.isVerticalScrollBarEnabled = false
        web.overScrollMode = View.OVER_SCROLL_NEVER
        web.settings.apply {
            javaScriptEnabled = true
            domStorageEnabled = true
            allowFileAccess = false
            allowContentAccess = false
            mixedContentMode = WebSettings.MIXED_CONTENT_NEVER_ALLOW
            setSupportMultipleWindows(false)
        }
        WebView.setWebContentsDebuggingEnabled(BuildConfig.DEBUG)
        val loader = WebViewAssetLoader.Builder()
            .addPathHandler("/assets/", WebViewAssetLoader.AssetsPathHandler(this))
            .addPathHandler("/content/", WebViewAssetLoader.PathHandler { path ->
                if (path.contains("..") || path.contains("\\")) return@PathHandler response(403)
                val f = File(root, path)
                if (!f.canonicalPath.startsWith(root.canonicalPath + "/")) return@PathHandler response(403)
                val mime = when (f.extension.lowercase()) { "json" -> "application/json"; "jpg", "jpeg" -> "image/jpeg"; "png" -> "image/png"; "webp" -> "image/webp"; else -> "text/plain" }
                try {
                    val input = if (f.isFile) f.inputStream() else assets.open("content/$path")
                    WebResourceResponse(mime, if (mime.startsWith("image/")) null else "UTF-8", input)
                } catch (_: Exception) { response(404) }
            }).build()
        web.webViewClient = object : WebViewClient() {
            override fun shouldInterceptRequest(view: WebView?, request: WebResourceRequest): WebResourceResponse? {
                val u = request.url
                if (u.scheme != "https" || u.host != "appassets.androidplatform.net") return response(403)
                return loader.shouldInterceptRequest(u) ?: response(404)
            }
            override fun shouldOverrideUrlLoading(view: WebView?, request: WebResourceRequest): Boolean {
                if (request.url.host == "appassets.androidplatform.net") return false
                return true
            }
            override fun onPageFinished(view: WebView?, url: String?) {
                super.onPageFinished(view, url)
                emit("onNativeInsets", JSONObject(safeZone))
            }
        }
        web.addJavascriptInterface(Bridge(), "ProfGeoAndroid")
        safeRoot.addView(web, FrameLayout.LayoutParams(FrameLayout.LayoutParams.MATCH_PARENT, FrameLayout.LayoutParams.MATCH_PARENT))
        setContentView(safeRoot)
        ViewCompat.setOnApplyWindowInsetsListener(safeRoot) { rootView, insets ->
            val bars = insets.getInsets(WindowInsetsCompat.Type.systemBars() or WindowInsetsCompat.Type.displayCutout())
            val keyboard = insets.getInsets(WindowInsetsCompat.Type.ime())
            val imeVisible = insets.isVisible(WindowInsetsCompat.Type.ime())
            val bottom = if (imeVisible) maxOf(bars.bottom, keyboard.bottom) else bars.bottom
            if (rootView.paddingLeft != bars.left || rootView.paddingTop != bars.top || rootView.paddingRight != bars.right || rootView.paddingBottom != bottom) {
                rootView.setPadding(bars.left, bars.top, bars.right, bottom)
            }
            val zone = JSONObject().put("top", bars.top).put("left", bars.left).put("right", bars.right)
                .put("bottom", bars.bottom).put("keyboard", keyboard.bottom).put("keyboardVisible", imeVisible)
                .put("density", resources.displayMetrics.density.toDouble()).toString()
            if (zone != safeZone) { safeZone = zone; emit("onNativeInsets", JSONObject(zone)) }
            // The native container owns the safe area. Do not let WebView apply it a second time.
            WindowInsetsCompat.CONSUMED
        }
        applyNativeTheme(false)
        ViewCompat.requestApplyInsets(safeRoot)
        web.loadUrl("$origin/assets/index.html")
    }

    @Suppress("DEPRECATION")
    private fun applyNativeTheme(dark: Boolean) {
        darkTheme = dark
        val background = if (dark) Color.rgb(16, 32, 30) else Color.rgb(247, 248, 242)
        safeRoot.setBackgroundColor(background)
        web.setBackgroundColor(background)
        window.statusBarColor = Color.TRANSPARENT
        window.navigationBarColor = if (android.os.Build.VERSION.SDK_INT == 26) Color.rgb(18, 62, 54) else Color.TRANSPARENT
        if (android.os.Build.VERSION.SDK_INT >= 29) window.isNavigationBarContrastEnforced = false
        WindowCompat.getInsetsController(window, web).apply {
            isAppearanceLightStatusBars = !dark
            isAppearanceLightNavigationBars = !dark
        }
    }

    private fun response(code: Int) = WebResourceResponse("text/plain", "UTF-8", code, if (code == 403) "Forbidden" else "Not Found", emptyMap(), ByteArrayInputStream(byteArrayOf()))
    private fun emit(name: String, value: JSONObject) = runOnUiThread { if (!isDestroyed) web.evaluateJavascript("window.$name && window.$name(${value});", null) }
    private fun bundledCatalog() = JSONObject(assets.open("content/catalog.json").bufferedReader().use { it.readText() })
    private fun readCatalog(): JSONObject = try { JSONObject(File(root, "catalog.json").readText()) } catch (_: Exception) { bundledCatalog() }
    private fun unit(id: String): JSONObject {
        require(id.matches(Regex("[1-9][0-9]?\\.[1-9][0-9]?")))
        val f = File(root, "units/$id/unit.json")
        val local = if (f.isFile) JSONObject(f.readText()).put("_base", "$origin/content/units/$id/") else null
        val bundled = try { JSONObject(assets.open("content/units/$id.json").bufferedReader().use { it.readText() }).put("_base", "$origin/assets/content/") } catch (_: Exception) { null }
        return if (local != null && (bundled == null || local.getInt("revision") > bundled.getInt("revision"))) local else bundled ?: error("Unidade indisponível")
    }
    private fun fetch(path: String, limit: Int): ByteArray {
        require(path.matches(Regex("[a-zA-Z0-9._/-]+")) && !path.contains(".."))
        val c = URL(remote + path).openConnection() as HttpURLConnection
        c.connectTimeout = 15000; c.readTimeout = 25000; c.instanceFollowRedirects = false
        c.setRequestProperty("User-Agent", "ProfGeo/${BuildConfig.VERSION_NAME}")
        c.setRequestProperty("Cache-Control", "no-cache")
        try {
            require(c.responseCode == 200) { "Não foi possível acessar o repositório (${c.responseCode})." }
            c.inputStream.use { input ->
                val output = java.io.ByteArrayOutputStream()
                val buf = ByteArray(8192)
                while (true) { val n = input.read(buf); if (n < 0) break; require(output.size() + n <= limit) { "Arquivo acima do limite permitido." }; output.write(buf, 0, n) }
                return output.toByteArray()
            }
        } finally { c.disconnect() }
    }
    private fun validateUnit(j: JSONObject, id: String, revision: Int) {
        require(j.getInt("schemaVersion") == 1 && j.getString("id") == id && j.getInt("revision") == revision)
        require(j.getString("title").length in 1..250)
        val lessons = j.getJSONArray("lessons")
        require(lessons.length() in 1..100)
        val ids = HashSet<String>()
        for (i in 0 until lessons.length()) {
            val lesson = lessons.getJSONObject(i)
            require(ids.add(lesson.getString("id")))
            require(lesson.getJSONArray("blocks").length() in 1..100)
            val blocks = lesson.getJSONArray("blocks")
            for (b in 0 until blocks.length()) require(blocks.getJSONObject(b).getString("type") in setOf("text", "callout", "list", "photo", "animation", "compare", "table"))
        }
        val qs = j.getJSONArray("questions"); require(qs.length() in 1..500)
        val qids = HashSet<String>()
        for (i in 0 until qs.length()) {
            val q = qs.getJSONObject(i); require(qids.add(q.getString("id")))
            val opts = q.getJSONArray("options"); require(opts.length() in 2..6)
            require(q.getInt("answer") in 0 until opts.length())
            require(q.getJSONArray("feedback").length() == opts.length())
        }
    }
    private fun install(id: String, revision: Int, bytes: ByteArray) {
        val stage = File(root, "stage-$id").apply { deleteRecursively(); mkdirs() }
        try {
            var total = 0; var count = 0
            ZipInputStream(ByteArrayInputStream(bytes)).use { zip ->
                while (true) {
                    val e = zip.nextEntry ?: break
                    require(++count < 500)
                    val f = File(stage, e.name)
                    require(f.canonicalPath.startsWith(stage.canonicalPath + "/") && !e.name.contains("\\"))
                    if (e.isDirectory) { f.mkdirs(); continue }
                    require(f.extension.lowercase() in setOf("json", "jpg", "jpeg", "png", "webp", "txt"))
                    f.parentFile?.mkdirs()
                    f.outputStream().use { output ->
                        val buf = ByteArray(8192)
                        while (true) { val n = zip.read(buf); if (n < 0) break; total += n; require(total < 32 * 1024 * 1024); output.write(buf, 0, n) }
                    }
                }
            }
            validateUnit(JSONObject(File(stage, "unit.json").readText()), id, revision)
            val target = File(root, "units/$id"); target.parentFile?.mkdirs()
            val old = File(root, "old-$id").apply { deleteRecursively() }
            if (target.exists()) require(target.renameTo(old))
            if (!stage.renameTo(target)) { old.renameTo(target); error("Não foi possível salvar a unidade.") }
            old.deleteRecursively()
        } finally { stage.deleteRecursively() }
    }
    private fun sync() {
        if (!busy.compareAndSet(false, true)) return
        executor.execute {
            var count = 0
            try {
                val catalog = JSONObject(String(fetch("catalog.json", 512 * 1024), Charsets.UTF_8))
                require(catalog.getInt("schemaVersion") == 1)
                require(catalog.optInt("minAppVersion", 1) <= BuildConfig.VERSION_CODE) { "Há conteúdo que precisa de uma versão mais nova do app." }
                val all = catalog.getJSONArray("modules"); require(all.length() in 1..30)
                val seen = HashSet<String>()
                for (m in 0 until all.length()) {
                    val entries = all.getJSONObject(m).getJSONArray("units")
                    require(entries.length() <= 100)
                    for (n in 0 until entries.length()) {
                        val entry = entries.getJSONObject(n); val id = entry.getString("id")
                        require(id.matches(Regex("[1-9][0-9]?\\.[1-9][0-9]?")) && seen.add(id))
                        if (entry.getString("status") != "published") continue
                        val revision = entry.getInt("revision"); require(revision > 0)
                        val current = try { unit(id).getInt("revision") } catch (_: Exception) { 0 }
                        if (revision <= current) continue
                        val bytes = fetch(entry.getString("package"), 8 * 1024 * 1024)
                        val digest = MessageDigest.getInstance("SHA-256").digest(bytes).joinToString("") { "%02x".format(it) }
                        require(digest == entry.getString("sha256")) { "O conteúdo recebido não passou na verificação de integridade." }
                        install(id, revision, bytes); count++
                    }
                }
                val dest = File(root, "catalog.json")
                val temp = File(root, "catalog.new"); temp.writeText(catalog.toString()); require(temp.renameTo(dest))
                prefs.edit().putLong("lastSync", System.currentTimeMillis()).apply()
                emit("onNativeSync", JSONObject().put("ok", true).put("count", count).put("catalog", catalog).put("checkedAt", System.currentTimeMillis()))
            } catch (e: Exception) {
                emit("onNativeSync", JSONObject().put("ok", false).put("message", e.message ?: "Sem conexão. Você pode continuar estudando o conteúdo salvo."))
            } finally { busy.set(false) }
        }
    }
    inner class Bridge {
        @JavascriptInterface fun getCatalog() = readCatalog().toString()
        @JavascriptInterface fun getUnit(id: String): String = try { unit(id).toString() } catch (_: Exception) { "null" }
        @JavascriptInterface fun readState() = prefs.getString("state", "{}") ?: "{}"
        @JavascriptInterface fun writeState(value: String) { if (value.toByteArray().size <= 2 * 1024 * 1024) try { JSONObject(value); prefs.edit().putString("state", value).apply() } catch (_: Exception) {} }
        @JavascriptInterface fun syncUnits() = sync()
        @JavascriptInterface fun shouldSync() = System.currentTimeMillis() - prefs.getLong("lastSync", 0) > 6 * 60 * 60 * 1000
        @JavascriptInterface fun version() = BuildConfig.VERSION_NAME
        @JavascriptInterface fun getSafeZone() = safeZone
        @JavascriptInterface fun setAppearance(dark: Boolean) = runOnUiThread { if (dark != darkTheme) applyNativeTheme(dark) }
        @JavascriptInterface fun hideKeyboard() = runOnUiThread {
            (getSystemService(INPUT_METHOD_SERVICE) as android.view.inputmethod.InputMethodManager)
                .hideSoftInputFromWindow(web.windowToken, 0)
        }
        @JavascriptInterface fun closeApp() = runOnUiThread { finish() }
        @JavascriptInterface fun openLink(link: String) {
            val u = Uri.parse(link)
            if (u.scheme == "https" && (u.host == "github.com" || u.host == "raw.githubusercontent.com" || u.host == "www.profgeo.propesp.ufpa.br" || u.host == "www.scielo.br" || u.host == "educa.ibge.gov.br" || u.host == "commons.wikimedia.org" || u.host == "revistas.usp.br" || u.host == "uesc.br")) runOnUiThread { try { startActivity(Intent(Intent.ACTION_VIEW, u)) } catch (_: Exception) {} }
        }
        @JavascriptInterface fun checkAppUpdate() {
            executor.execute {
                try { val j = JSONObject(String(fetch("app-release.json", 64 * 1024), Charsets.UTF_8)); emit("onNativeUpdate", j.put("available", j.getInt("versionCode") > BuildConfig.VERSION_CODE)) }
                catch (_: Exception) { emit("onNativeUpdate", JSONObject().put("error", "Não foi possível verificar. Tente novamente com internet.")) }
            }
        }
        @JavascriptInterface fun exportBackup(value: String) {
            if (value.toByteArray().size > 2 * 1024 * 1024) return
            pendingExport = value
            runOnUiThread { @Suppress("DEPRECATION") startActivityForResult(Intent(Intent.ACTION_CREATE_DOCUMENT).apply { type = "application/json"; addCategory(Intent.CATEGORY_OPENABLE); putExtra(Intent.EXTRA_TITLE, "ProfGeo-progresso.json") }, 101) }
        }
        @JavascriptInterface fun importBackup() = runOnUiThread { @Suppress("DEPRECATION") startActivityForResult(Intent(Intent.ACTION_OPEN_DOCUMENT).apply { type = "application/json"; addCategory(Intent.CATEGORY_OPENABLE) }, 102) }
    }
    @Deprecated("Legacy back callback") override fun onBackPressed() { web.evaluateJavascript("window.nativeBack && window.nativeBack();", null) }
    @Deprecated("Legacy document callback") override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (resultCode != RESULT_OK) return
        val uri = data?.data ?: return
        try {
            if (requestCode == 101) { contentResolver.openOutputStream(uri)?.use { it.write(pendingExport.toByteArray()) }; emit("onNativeBackup", JSONObject().put("ok", true).put("message", "Cópia de segurança salva.")) }
            else if (requestCode == 102) {
                val bytes = contentResolver.openInputStream(uri)?.use { input ->
                    val out = java.io.ByteArrayOutputStream(); val buffer = ByteArray(8192)
                    while (out.size() <= 2 * 1024 * 1024) { val n = input.read(buffer); if (n < 0) break; out.write(buffer, 0, n) }
                    out.toByteArray()
                } ?: return
                require(bytes.size <= 2 * 1024 * 1024)
                emit("onNativeImport", JSONObject(String(bytes, Charsets.UTF_8)))
            }
        } catch (_: Exception) { emit("onNativeBackup", JSONObject().put("ok", false).put("message", "Não foi possível abrir ou salvar esse arquivo.")) }
    }
    override fun onDestroy() { web.removeJavascriptInterface("ProfGeoAndroid"); web.destroy(); executor.shutdown(); super.onDestroy() }
}
