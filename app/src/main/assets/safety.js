/* Native Android owns system insets; the web interface owns only its measured dock. */
(function(){
'use strict';
const native=window.ProfGeoAndroid;
let observer=null,lastNavHeight=76,keyboardOpen=false,focusTimer=0,baseline=innerHeight;
const editable=el=>!!el&&(el.tagName==='TEXTAREA'||el.tagName==='INPUT'&&el.type!=='checkbox'&&el.type!=='file');
function visibleInput(){
 const el=document.activeElement;if(!editable(el))return;
 const r=el.getBoundingClientRect(),visibleHeight=window.visualViewport?Math.min(innerHeight,visualViewport.height):innerHeight;
 const top=document.querySelector('.reader-header')?.getBoundingClientRect().bottom||22;
 if(r.bottom>visibleHeight-20||r.top<top+12)el.scrollIntoView({block:'center',behavior:'auto'});
}
function setKeyboard(open){keyboardOpen=!!open;document.body.classList.toggle('keyboard-open',keyboardOpen);if(keyboardOpen){clearTimeout(focusTimer);focusTimer=setTimeout(visibleInput,160)}}
window.onNativeInsets=function(zone){
 if(native)document.body.classList.add('native-safe-area');
 window.GeoSafeArea.insets=zone||{};
 setKeyboard(!!zone?.keyboardVisible);
};
function mount(){
 if(observer)observer.disconnect();
 const nav=document.querySelector('.nav');
 if(nav){const measure=()=>{const h=nav.getBoundingClientRect().height;if(h>0){lastNavHeight=Math.ceil(h);document.documentElement.style.setProperty('--nav-height',lastNavHeight+'px')}};measure();if(window.ResizeObserver){observer=new ResizeObserver(measure);observer.observe(nav)}}
 if(native){document.body.classList.add('native-safe-area');try{if(typeof native.getSafeZone==='function')window.onNativeInsets(JSON.parse(native.getSafeZone()))}catch{}}
}
function resized(){
 if(!native){const reduced=baseline-innerHeight>100||(window.visualViewport&&innerHeight-visualViewport.height>100);setKeyboard(editable(document.activeElement)&&reduced);if(!editable(document.activeElement))baseline=innerHeight}
 if(keyboardOpen){clearTimeout(focusTimer);focusTimer=setTimeout(visibleInput,180)}
}
document.addEventListener('focusin',e=>{if(editable(e.target)){clearTimeout(focusTimer);focusTimer=setTimeout(visibleInput,220)}});
document.addEventListener('focusout',()=>{if(!native)setTimeout(()=>{if(!editable(document.activeElement))setKeyboard(false)},120)});
window.addEventListener('resize',resized);
window.visualViewport?.addEventListener('resize',resized);
window.GeoSafeArea={insets:{},mount,ensureInputVisible:visibleInput,snapshot:()=>({keyboardOpen,navHeight:lastNavHeight,nativePadded:!!native})};
if(native)document.body.classList.add('native-safe-area');
})();
