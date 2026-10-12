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
    scenario.onActivity(a->{android.view.ViewGroup root=a.findViewById(android.R.id.content);WebView w=(WebView)root.getChildAt(0);w.evaluateJavascript(script,s->{value.set(s);ready.countDown();});});
    assertTrue(ready.await(8,TimeUnit.SECONDS));return value.get();
  }
  @Test public void nativeBundleLessonsAndStateSurviveRestart() throws Exception {
    try(ActivityScenario<MainActivity> scenario=ActivityScenario.launch(MainActivity.class)) {
      String ready="null";
      for(int i=0;i<40;i++){ready=js(scenario,"typeof GeoApp !== 'undefined' && !!GeoApp.getState() && document.querySelector('h1').textContent.includes('Compreender')");if("true".equals(ready))break;Thread.sleep(250);}
      assertEquals("true",ready);
      assertEquals("15",js(scenario,"JSON.parse(ProfGeoAndroid.getCatalog()).modules.reduce((n,m)=>n+m.units.length,0)"));
      assertEquals("56",js(scenario,"JSON.parse(ProfGeoAndroid.getUnit('1.1')).questions.length"));
      js(scenario,"GeoApp.action('lesson:1.1:l01')");Thread.sleep(500);
      assertEquals("true",js(scenario,"document.querySelector('canvas').width===320 && document.querySelector('canvas').height===180"));
      js(scenario,"document.getElementById('lesson-note').value='Teste de persistência';document.getElementById('lesson-note').dispatchEvent(new Event('input',{bubbles:true}))");
      assertEquals("true",js(scenario,"JSON.parse(ProfGeoAndroid.readState()).notes['1.1:l01']==='Teste de persistência'"));
      assertEquals("true",js(scenario,"document.querySelector('img')===null || document.querySelector('img').src.startsWith('https://appassets.androidplatform.net/')"));
      scenario.recreate();Thread.sleep(1200);
      assertEquals("true",js(scenario,"GeoApp.getState().notes['1.1:l01']==='Teste de persistência'"));
    }
  }
}
