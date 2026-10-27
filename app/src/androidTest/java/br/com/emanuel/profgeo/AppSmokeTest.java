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
  private void awaitJs(ActivityScenario<MainActivity> scenario,String predicate,String message) throws Exception {
    String actual="null";
    for(int i=0;i<60;i++) {
      actual=js(scenario,"(()=>{try{return !!("+predicate+");}catch(e){return false;}})()");
      if("true".equals(actual))return;
      Thread.sleep(200);
    }
    assertEquals(message,"true",actual);
  }
  @Test public void nativeBundleLessonsAndStateSurviveRestart() throws Exception {
    try(ActivityScenario<MainActivity> scenario=ActivityScenario.launch(MainActivity.class)) {
      String ready="null";
      for(int i=0;i<40;i++){ready=js(scenario,"typeof GeoApp !== 'undefined' && !!GeoApp.getState() && document.querySelector('h1').textContent.includes('Seu próximo passo')");if("true".equals(ready))break;Thread.sleep(250);}
      assertEquals("true",ready);
      assertEquals("15",js(scenario,"JSON.parse(ProfGeoAndroid.getCatalog()).modules.reduce((n,m)=>n+m.units.length,0)"));
      assertEquals("76",js(scenario,"JSON.parse(ProfGeoAndroid.getUnit('1.1')).questions.length"));
      assertEquals("2",js(scenario,"JSON.parse(ProfGeoAndroid.getUnit('1.1')).revision"));
      js(scenario,"GeoApp.action('lesson:1.1:l01')");Thread.sleep(500);
      assertEquals("true",js(scenario,"document.querySelector('canvas').width===640 && document.querySelector('canvas').height===360"));
      js(scenario,"GeoApp.getState().answers['1.1:q01']={choice:1,correct:true,attempts:2,lastAt:1};GeoApp.getState().essays['1.1']={lines:['Texto anterior à revisão didática'],rubric:[0,4]}");
      js(scenario,"document.getElementById('lesson-note').value='Teste de persistência';document.getElementById('lesson-note').dispatchEvent(new Event('input',{bubbles:true}))");
      assertEquals("true",js(scenario,"JSON.parse(ProfGeoAndroid.readState()).notes['1.1:l01']==='Teste de persistência'"));
      assertEquals("true",js(scenario,"document.querySelector('img')===null || document.querySelector('img').src.startsWith('https://appassets.androidplatform.net/')"));
      scenario.recreate();Thread.sleep(1200);
      assertEquals("true",js(scenario,"GeoApp.getState().notes['1.1:l01']==='Teste de persistência'"));
      assertEquals("true",js(scenario,"GeoApp.getState().answers['1.1:q01'].correct===true && GeoApp.getState().answers['1.1:q01'].choice===1"));
      assertEquals("true",js(scenario,"GeoApp.getState().essays['1.1'].lines[0]==='Texto anterior à revisão didática'"));
    }
  }
  @Test public void downloadedUnitOpensOfflineAndInvalidPackagesAreRejected() throws Exception {
    verifyDownloadedUnit("1.2",2,80,8,"Ensinar exige mais de um saber");
  }
  @Test public void unit13DownloadsWithItsOwnLessonsImagesAndNotebook() throws Exception {
    verifyDownloadedUnit("1.3",1,76,9,"Conceito, categoria e conteúdo: para que servem?");
  }
  @Test public void unit14DownloadsWithItsOwnLessonsImagesAndNotebook() throws Exception {
    verifyDownloadedUnit("1.4",1,76,9,"Qual documento responde à minha pergunta?");
  }
  @Test public void unit15DownloadsWithItsOwnLessonsImagesAndNotebook() throws Exception {
    verifyDownloadedUnit("1.5",1,76,9,"Quando uma dúvida da aula se torna pesquisa?");
  }
  private void verifyDownloadedUnit(final String unitId,int expectedRevision,int expectedQuestions,int expectedMedia,String lessonTitle) throws Exception {
    android.content.Context ctx=androidx.test.platform.app.InstrumentationRegistry.getInstrumentation().getTargetContext();
    String unit=org.json.JSONObject.quote(unitId);
    String source;
    try(java.io.InputStream in=ctx.getAssets().open("content/units/"+unitId+".json")) {
      java.io.ByteArrayOutputStream b=new java.io.ByteArrayOutputStream();byte[] buf=new byte[8192];int n;while((n=in.read(buf))!=-1)b.write(buf,0,n);source=b.toString("UTF-8");
    }
    org.json.JSONObject fixture=new org.json.JSONObject(source);
    assertEquals(expectedRevision,fixture.getInt("revision"));
    final int installedRevision=fixture.getInt("revision")+1;fixture.put("revision",installedRevision);
    assertEquals(expectedQuestions,fixture.getJSONArray("questions").length());
    java.util.Set<String> media=new java.util.TreeSet<>();
    org.json.JSONArray lessons=fixture.getJSONArray("lessons");
    for(int l=0;l<lessons.length();l++) {
      org.json.JSONArray blocks=lessons.getJSONObject(l).getJSONArray("blocks");
      for(int b=0;b<blocks.length();b++)if("photo".equals(blocks.getJSONObject(b).getString("type")))media.add(blocks.getJSONObject(b).getString("src"));
    }
    assertEquals(expectedMedia,media.size());
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
      awaitJs(scenario,"typeof GeoApp!=='undefined' && !!GeoApp.getState() && document.querySelector('h1') && document.querySelector('h1').textContent.includes('Seu próximo passo')","A tela inicial deve terminar de carregar antes da instalação da unidade "+unitId);
      java.util.concurrent.atomic.AtomicReference<Exception> failure=new java.util.concurrent.atomic.AtomicReference<>();
      scenario.onActivity(a->{try{java.lang.reflect.Method install=MainActivity.class.getDeclaredMethod("install",String.class,int.class,byte[].class);install.setAccessible(true);install.invoke(a,unitId,installedRevision,bytes.toByteArray());}catch(Exception e){failure.set(e);}});
      assertNull(failure.get());
      assertEquals(String.valueOf(expectedQuestions),js(scenario,"JSON.parse(ProfGeoAndroid.getUnit("+unit+")).questions.length"));
      assertEquals("true",js(scenario,"JSON.parse(ProfGeoAndroid.getUnit("+unit+"))._base.includes('/content/units/"+unitId+"/')"));
      for(String path:media)assertTrue(new java.io.File(ctx.getFilesDir(),"content/units/"+unitId+"/"+path).isFile());
      js(scenario,"GeoApp.action('lesson:"+unitId+":l01')");
      awaitJs(scenario,"document.querySelector('h1') && document.querySelector('h1').textContent==="+org.json.JSONObject.quote(lessonTitle),"A primeira lição da unidade "+unitId+" deve terminar de abrir");
      assertEquals("true",js(scenario,"document.querySelector('h1').textContent==="+org.json.JSONObject.quote(lessonTitle)));
      js(scenario,"document.querySelectorAll('figure img').forEach(i=>i.loading='eager')");
      String loaded="false";
      for(int i=0;i<20;i++){loaded=js(scenario,"[...document.querySelectorAll('figure img')].length===2 && [...document.querySelectorAll('figure img')].every(i=>i.complete&&i.naturalWidth===1280&&i.naturalHeight===720)");if("true".equals(loaded))break;Thread.sleep(250);}
      assertEquals("true",loaded);
      js(scenario,"GeoApp.getState().notes['1.1:l02']='Nota anterior preservada';document.getElementById('lesson-note').value='Nota da unidade baixada';document.getElementById('lesson-note').dispatchEvent(new Event('input',{bubbles:true}))");
      scenario.onActivity(a->{try{java.lang.reflect.Method install=MainActivity.class.getDeclaredMethod("install",String.class,int.class,byte[].class);install.setAccessible(true);install.invoke(a,unitId,installedRevision+1,attack.toByteArray());}catch(Exception expected){failure.set(expected);}});
      assertNotNull(failure.get());
      assertEquals(String.valueOf(installedRevision),js(scenario,"JSON.parse(ProfGeoAndroid.getUnit("+unit+")).revision"));
      assertFalse(new java.io.File(ctx.getFilesDir(),"outside.json").exists());
      scenario.recreate();
      awaitJs(scenario,"typeof GeoApp!=='undefined' && !!GeoApp.getState() && GeoApp.getState().notes['"+unitId+":l01']==='Nota da unidade baixada'","A nota da unidade "+unitId+" deve ser restaurada depois de reabrir");
      assertEquals("true",js(scenario,"JSON.parse(ProfGeoAndroid.getUnit("+unit+")).title==="+org.json.JSONObject.quote(fixture.getString("title"))));
      assertEquals("true",js(scenario,"GeoApp.getState().notes['"+unitId+":l01']==='Nota da unidade baixada'"));
      assertEquals("true",js(scenario,"GeoApp.getState().notes['1.1:l02']==='Nota anterior preservada'"));
    }
  }

}
