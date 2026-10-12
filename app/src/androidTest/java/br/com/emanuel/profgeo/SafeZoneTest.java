package br.com.emanuel.profgeo;
import android.graphics.Rect;
import android.view.ViewGroup;
import android.webkit.WebView;
import android.widget.FrameLayout;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.test.core.app.ActivityScenario;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicReference;
import org.junit.Test;
import org.junit.runner.RunWith;
import static org.junit.Assert.*;
@RunWith(AndroidJUnit4.class)
public class SafeZoneTest {
 private WebView web(MainActivity a){ViewGroup root=a.findViewById(android.R.id.content);return (WebView)((ViewGroup)root.getChildAt(0)).getChildAt(0);}
 private FrameLayout container(MainActivity a){ViewGroup root=a.findViewById(android.R.id.content);return (FrameLayout)root.getChildAt(0);}
 private String js(ActivityScenario<MainActivity> scenario,String code)throws Exception{AtomicReference<String> result=new AtomicReference<>();CountDownLatch latch=new CountDownLatch(1);scenario.onActivity(a->web(a).evaluateJavascript(code,v->{result.set(v);latch.countDown();}));assertTrue(latch.await(8,TimeUnit.SECONDS));return result.get();}
 private void ready(ActivityScenario<MainActivity> s)throws Exception{for(int i=0;i<60;i++){if("true".equals(js(s,"typeof GeoApp!=='undefined' && !!GeoApp.getState() && typeof GeoSafeArea!=='undefined'")))return;Thread.sleep(200);}fail("A interface não ficou pronta");}
 @Test public void cutoutAndBarsAreConsumedOnceAndDockFitsViewport()throws Exception{
  try(ActivityScenario<MainActivity> s=ActivityScenario.launch(MainActivity.class)){
   ready(s);
   s.onActivity(a->{FrameLayout root=container(a);WindowInsetsCompat fake=new WindowInsetsCompat.Builder().setInsets(WindowInsetsCompat.Type.systemBars(),Insets.of(0,32,0,48)).setInsets(WindowInsetsCompat.Type.displayCutout(),Insets.of(44,72,18,0)).setInsets(WindowInsetsCompat.Type.ime(),Insets.NONE).setVisible(WindowInsetsCompat.Type.ime(),false).build();ViewCompat.dispatchApplyWindowInsets(root,fake);});
   Thread.sleep(350);
   assertEquals("true",js(s,"(()=>{let z=JSON.parse(ProfGeoAndroid.getSafeZone());return z.top===72 && z.left===44 && z.right===18 && z.bottom===48})()"));
   assertEquals("true",js(s,"getComputedStyle(document.body).getPropertyValue('--safe-top').trim()==='0px' && GeoSafeArea.snapshot().nativePadded"));
   assertEquals("true",js(s,"(()=>{let r=document.querySelector('.nav').getBoundingClientRect();return r.left>=8 && r.right<=innerWidth-8 && r.bottom<=innerHeight-8 && document.documentElement.scrollWidth<=innerWidth+1})()"));
   s.onActivity(a->{FrameLayout r=container(a);assertEquals(72,r.getPaddingTop());assertEquals(44,r.getPaddingLeft());assertEquals(18,r.getPaddingRight());assertEquals(48,r.getPaddingBottom());assertEquals(0,web(a).getPaddingTop());assertEquals(0,web(a).getPaddingBottom());ViewCompat.requestApplyInsets(r);});
  }
 }
 @Test public void realKeyboardKeepsNoteVisibleWithoutNavigationOverlap()throws Exception{
  try(ActivityScenario<MainActivity> s=ActivityScenario.launch(MainActivity.class)){
   ready(s);js(s,"GeoApp.action('lesson:1.1:l01')");Thread.sleep(450);
   js(s,"document.getElementById('lesson-note').focus()");
   s.onActivity(a->{WebView w=web(a);w.requestFocus();((android.view.inputmethod.InputMethodManager)a.getSystemService(android.content.Context.INPUT_METHOD_SERVICE)).showSoftInput(w,android.view.inputmethod.InputMethodManager.SHOW_IMPLICIT);});
   boolean shown=false;for(int i=0;i<50;i++){if("true".equals(js(s,"JSON.parse(ProfGeoAndroid.getSafeZone()).keyboardVisible===true"))){shown=true;break;}Thread.sleep(150);}assertTrue("O teclado real deve produzir insets",shown);
   Thread.sleep(350);assertEquals("true",js(s,"getComputedStyle(document.querySelector('.nav')).display==='none' && GeoSafeArea.snapshot().keyboardOpen"));
   assertEquals("true",js(s,"(()=>{let r=document.getElementById('lesson-note').getBoundingClientRect();return r.top>=0 && r.bottom<=innerHeight+1})()"));
   s.onActivity(a->{FrameLayout r=container(a);WebView w=web(a);int[] xy=new int[2];w.getLocationOnScreen(xy);WindowInsetsCompat wi=ViewCompat.getRootWindowInsets(r);int keyboard=wi.getInsets(WindowInsetsCompat.Type.ime()).bottom;int height=a.getWindow().getDecorView().getHeight();assertTrue("A WebView não pode ficar sob o teclado",xy[1]+w.getHeight()<=height-keyboard+4);assertTrue("O teclado não pode ser descontado duas vezes",w.getHeight()>height-keyboard-r.getPaddingTop()-80);});
   js(s,"document.activeElement.blur();ProfGeoAndroid.hideKeyboard()");for(int i=0;i<50;i++){if("true".equals(js(s,"JSON.parse(ProfGeoAndroid.getSafeZone()).keyboardVisible===false")))break;Thread.sleep(100);}Thread.sleep(200);
   assertEquals("true",js(s,"getComputedStyle(document.querySelector('.nav')).display!=='none'"));
  }
 }
}
