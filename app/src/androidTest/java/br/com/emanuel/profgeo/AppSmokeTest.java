package br.com.emanuel.profgeo;
import android.webkit.WebView;
import androidx.test.core.app.ActivityScenario;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicReference;
import org.junit.Test;
import org.junit.runner.RunWith;
import static org.junit.Assert.*;
@RunWith(AndroidJUnit4.class)
public class AppSmokeTest {
  private String js(ActivityScenario<MainActivity> scenario, String script) throws Exception {
    AtomicReference<String> value=new AtomicReference<>();CountDownLatch ready=new CountDownLatch(1);
    scenario.onActivity(a->{android.view.ViewGroup root=a.findViewById(android.R.id.content);WebView w=(WebView)((android.view.ViewGroup)root.getChildAt(0)).getChildAt(0);w.evaluateJavascript(script,s->{value.set(s);ready.countDown();});});
    assertTrue(ready.await(8,TimeUnit.SECONDS));return value.get();
  }
  @Test public void nativeBundleLessonsAndStateSurviveRestart() throws Exception {
    try(ActivityScenario<MainActivity> scenario=ActivityScenario.launch(MainActivity.class)) {
      String ready="null";
      for(int i=0;i<40;i++){ready=js(scenario,"typeof GeoApp !== 'undefined' && !!GeoApp.getState() && document.querySelector('h1').textContent.includes('Seu próximo passo')");if("true".equals(ready))break;Thread.sleep(250);}
      assertEquals("true",ready);
      assertEquals("15",js(scenario,"JSON.parse(ProfGeoAndroid.getCatalog()).modules.reduce((n,m)=>n+m.units.length,0)"));
      assertEquals("56",js(scenario,"JSON.parse(ProfGeoAndroid.getUnit('1.1')).questions.length"));
      js(scenario,"GeoApp.action('lesson:1.1:l01')");Thread.sleep(500);
      assertEquals("true",js(scenario,"document.querySelector('canvas').width===640 && document.querySelector('canvas').height===360"));
      js(scenario,"document.getElementById('lesson-note').value='Teste de persistência';document.getElementById('lesson-note').dispatchEvent(new Event('input',{bubbles:true}))");
      assertEquals("true",js(scenario,"JSON.parse(ProfGeoAndroid.readState()).notes['1.1:l01']==='Teste de persistência'"));
      assertEquals("true",js(scenario,"document.querySelector('img')===null || document.querySelector('img').src.startsWith('https://appassets.androidplatform.net/')"));
      scenario.recreate();Thread.sleep(1200);
      assertEquals("true",js(scenario,"GeoApp.getState().notes['1.1:l01']==='Teste de persistência'"));
    }
  }
  @Test public void downloadedUnitOpensOfflineAndInvalidPackagesAreRejected() throws Exception {
    android.content.Context ctx=androidx.test.platform.app.InstrumentationRegistry.getInstrumentation().getTargetContext();
    String source;
    try(java.io.InputStream in=ctx.getAssets().open("content/units/1.2.json")) {
      java.io.ByteArrayOutputStream b=new java.io.ByteArrayOutputStream();byte[] buf=new byte[8192];int n;while((n=in.read(buf))!=-1)b.write(buf,0,n);source=b.toString("UTF-8");
    }
    org.json.JSONObject fixture=new org.json.JSONObject(source);fixture.put("revision",2);
    assertEquals(60,fixture.getJSONArray("questions").length());
    java.util.Set<String> media=new java.util.TreeSet<>();
    org.json.JSONArray lessons=fixture.getJSONArray("lessons");
    for(int l=0;l<lessons.length();l++) {
      org.json.JSONArray blocks=lessons.getJSONObject(l).getJSONArray("blocks");
      for(int b=0;b<blocks.length();b++)if("photo".equals(blocks.getJSONObject(b).getString("type")))media.add(blocks.getJSONObject(b).getString("src"));
    }
    assertEquals(8,media.size());
    java.io.ByteArrayOutputStream bytes=new java.io.ByteArrayOutputStream();
    try(java.util.zip.ZipOutputStream z=new java.util.zip.ZipOutputStream(bytes)) {
      z.putNextEntry(new java.util.zip.ZipEntry("unit.json"));z.write(fixture.toString().getBytes(java.nio.charset.StandardCharsets.UTF_8));z.closeEntry();
      for(String path:media) {
        z.putNextEntry(new java.util.zip.ZipEntry(path));
        try(java.io.InputStream in=ctx.getAssets().open("content/"+path)) {byte[] buf=new byte[8192];int n;while((n=in.read(buf))!=-1)z.write(buf,0,n);}
        z.closeEntry();
      }
    }
    java.io.ByteArrayOutputStream attack=new java.io.ByteArrayOutputStream();
    try(java.util.zip.ZipOutputStream z=new java.util.zip.ZipOutputStream(attack)) {z.putNextEntry(new java.util.zip.ZipEntry("../../outside.json"));z.write("{}".getBytes());z.closeEntry();}
    try(ActivityScenario<MainActivity> scenario=ActivityScenario.launch(MainActivity.class)) {
      java.util.concurrent.atomic.AtomicReference<Exception> failure=new java.util.concurrent.atomic.AtomicReference<>();
      scenario.onActivity(a->{try{java.lang.reflect.Method install=MainActivity.class.getDeclaredMethod("install",String.class,int.class,byte[].class);install.setAccessible(true);install.invoke(a,"1.2",2,bytes.toByteArray());}catch(Exception e){failure.set(e);}});
      assertNull(failure.get());
      Thread.sleep(1000);
      assertEquals("60",js(scenario,"JSON.parse(ProfGeoAndroid.getUnit('1.2')).questions.length"));
      assertEquals("true",js(scenario,"JSON.parse(ProfGeoAndroid.getUnit('1.2'))._base.includes('/content/units/1.2/')"));
      for(String path:media)assertTrue(new java.io.File(ctx.getFilesDir(),"content/units/1.2/"+path).isFile());
      js(scenario,"GeoApp.action('lesson:1.2:l01')");Thread.sleep(700);
      assertEquals("true",js(scenario,"document.querySelector('h1').textContent==='Ensinar exige mais de um saber'"));
      js(scenario,"document.querySelectorAll('figure img').forEach(i=>i.loading='eager')");
      String loaded="false";
      for(int i=0;i<20;i++){loaded=js(scenario,"[...document.querySelectorAll('figure img')].length===2 && [...document.querySelectorAll('figure img')].every(i=>i.complete&&i.naturalWidth===1280&&i.naturalHeight===720)");if("true".equals(loaded))break;Thread.sleep(250);}
      assertEquals("true",loaded);
      js(scenario,"document.getElementById('lesson-note').value='Nota da unidade baixada';document.getElementById('lesson-note').dispatchEvent(new Event('input',{bubbles:true}))");
      scenario.onActivity(a->{try{java.lang.reflect.Method install=MainActivity.class.getDeclaredMethod("install",String.class,int.class,byte[].class);install.setAccessible(true);install.invoke(a,"1.2",3,attack.toByteArray());}catch(Exception expected){failure.set(expected);}});
      assertNotNull(failure.get());
      assertEquals("2",js(scenario,"JSON.parse(ProfGeoAndroid.getUnit('1.2')).revision"));
      assertFalse(new java.io.File(ctx.getFilesDir(),"outside.json").exists());
      scenario.recreate();Thread.sleep(1000);
      assertEquals("true",js(scenario,"JSON.parse(ProfGeoAndroid.getUnit('1.2')).title.startsWith('Saberes disciplinares')"));
      assertEquals("true",js(scenario,"GeoApp.getState().notes['1.2:l01']==='Nota da unidade baixada'"));
    }
  }

}
