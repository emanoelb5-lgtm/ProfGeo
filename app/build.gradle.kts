plugins { id("com.android.application"); id("org.jetbrains.kotlin.android") }
android {
    namespace = "br.com.emanuel.profgeo"
    compileSdk = 35
    defaultConfig {
        applicationId = "br.com.emanuel.profgeo"
        minSdk = 26
        targetSdk = 35
        versionCode = 2
        versionName = "1.1.0"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }
    val keyPath = System.getenv("PROFGEO_KEYSTORE")
    signingConfigs {
        if (!keyPath.isNullOrBlank()) create("persistentRelease") {
            storeFile = file(keyPath)
            storePassword = System.getenv("PROFGEO_STORE_PASSWORD")
            keyAlias = "profgeo"
            keyPassword = System.getenv("PROFGEO_KEY_PASSWORD")
        }
    }
    buildTypes {
        release {
            isMinifyEnabled = false
            if (!keyPath.isNullOrBlank()) signingConfig = signingConfigs.getByName("persistentRelease")
        }
    }
    compileOptions { sourceCompatibility = JavaVersion.VERSION_17; targetCompatibility = JavaVersion.VERSION_17 }
    kotlinOptions { jvmTarget = "17" }
    buildFeatures { buildConfig = true }
}
dependencies {
    implementation("androidx.core:core:1.15.0")
    implementation("androidx.webkit:webkit:1.12.1")
    androidTestImplementation("androidx.test:runner:1.6.2")
    androidTestImplementation("androidx.test.ext:junit:1.2.1")
    androidTestImplementation("androidx.test:core:1.6.1")
}
