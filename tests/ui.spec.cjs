const {test,expect}=require('@playwright/test');
test('percurso completo, correção, anotações, redação e restauração',async({page})=>{
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('/');await expect(page.getByRole('heading',{name:'Seu próximo passo.',exact:true})).toBeVisible();
 await page.getByRole('button',{name:/Começar a unidade/}).click();
 await expect(page.locator('.lesson-item')).toHaveCount(12);
 await page.locator('.lesson-item').first().click();
 await expect(page.locator('canvas')).toBeVisible();
 const dimensions=await page.locator('canvas').evaluate(c=>[c.width,c.height]);expect(dimensions).toEqual([640,360]);
 await page.getByRole('button',{name:'Infraestrutura melhorada'}).click();await expect(page.locator('.anim-description')).toContainText('melhoria');
 await page.locator('#lesson-note').fill('O evento natural interage com condições sociais.');
 await page.getByRole('button',{name:/Praticar esta lição/}).click();
 await page.locator('.option').nth(0).click();await page.getByRole('button',{name:'Confirmar resposta'}).click();
 await expect(page.locator('.feedback')).toContainText('Vamos entender');
 await expect(page.locator('.option.correct')).toHaveCount(1);
 await page.getByRole('button',{name:/Próxima questão/}).click();await page.locator('.option').nth(1).click();await page.getByRole('button',{name:'Confirmar resposta'}).click();
 await page.getByRole('button',{name:/Próxima questão/}).click();await page.locator('.option').nth(0).click();await page.getByRole('button',{name:'Confirmar resposta'}).click();await page.getByRole('button',{name:'Ver meu resultado'}).click();
 const state=await page.evaluate(()=>GeoApp.getState());expect(Object.keys(state.completed)).toHaveLength(1);expect(state.notes['1.1:l01']).toContain('condições');
 await page.getByRole('button',{name:'Ir à oficina de redação'}).click();await page.locator('[data-essayline]').first().fill('O ensino pode ampliar a compreensão de relações espaciais.');await page.locator('[data-rubric]').first().check();
 await page.getByRole('button',{name:'Ajustes',exact:true}).click();await page.locator('#font-size').selectOption('21');await page.locator('#dark-mode').check();
 await page.reload();await expect(page.getByText('Retomar estudo')).toBeVisible();
 expect(await page.evaluate(()=>GeoApp.getState().settings.font)).toBe(21);
 expect(await page.evaluate(()=>GeoApp.getState().essays['1.1'].lines[0])).toContain('relações espaciais');
 expect(errors).toEqual([]);
});
test('simulado de 20 questões, exercício de associação e conteúdo seguro',async({page})=>{
 await page.goto('/');await page.evaluate(()=>GeoApp.action('lesson:1.1:l02'));await expect(page.locator('[data-match]')).toHaveCount(4);
 await page.getByRole('button',{name:'Conferir associações'}).click();await expect(page.locator('#practice-result')).toContainText('0 de 4');
 await page.evaluate(()=>GeoApp.action('final:1.1'));await expect(page.getByText('1 / 20',{exact:true})).toBeVisible();
 for(let i=0;i<20;i++){const qid=await page.locator('.question-card h2').textContent();const answer=await page.evaluate(stem=>GeoApp.getUnit('1.1').then(u=>u.questions.find(q=>q.stem===stem).answer),qid);await page.locator('.option').nth(answer).click();await page.getByRole('button',{name:'Confirmar resposta'}).click();await page.getByRole('button',{name:i===19?'Ver meu resultado':'Próxima questão',exact:true}).click()}
 await expect(page.locator('.score')).toContainText('20');const s=await page.evaluate(()=>GeoApp.getState());expect(s.sessions.at(-1).correct).toBe(20);
 await page.evaluate(()=>{localStorage.setItem('profgeo.state',JSON.stringify({...GeoApp.getState(),notes:{'1.1:l01':'<img src=x onerror="window.bad=1">'}}))});await page.reload();await page.evaluate(()=>GeoApp.action('lesson:1.1:l01'));await expect(page.locator('#lesson-note')).toHaveValue('<img src=x onerror="window.bad=1">');expect(await page.evaluate(()=>window.bad)).toBeUndefined();
});
test('as telas não causam rolagem horizontal em celular',async({page})=>{await page.goto('/');for(const action of ['nav:home','nav:modules','unit:1.1','lesson:1.1:l10','nav:review','essay:1.1','nav:settings']){await page.evaluate(a=>GeoApp.action(a),action);await page.waitForTimeout(80);expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1)).toBeTruthy()}});

test('área segura mantém navegação e últimas ações acessíveis com fonte grande',async({page})=>{
 for(const viewport of [{width:320,height:568},{width:360,height:800},{width:412,height:915},{width:915,height:412}]){
  await page.setViewportSize(viewport);await page.goto('/');
  await page.evaluate(()=>{document.documentElement.style.setProperty('--safe-top','28px');document.documentElement.style.setProperty('--safe-bottom','24px');document.documentElement.style.setProperty('--safe-left','18px');document.documentElement.style.setProperty('--safe-right','12px')});
  for(const font of ['17','24']){
   await page.evaluate(()=>GeoApp.action('nav:settings'));await page.locator('#font-size').selectOption(font);
   for(const route of ['nav:home','lesson:1.1:l10','essay:1.1','nav:settings']){
    await page.evaluate(a=>GeoApp.action(a),route);await page.waitForTimeout(80);
    const geometry=await page.evaluate(()=>{const nav=document.querySelector('.nav'),r=nav.getBoundingClientRect();return {width:document.documentElement.scrollWidth,viewport:innerWidth,top:r.top,bottom:r.bottom,left:r.left,right:r.right,height:r.height,reserve:parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nav-height')),buttons:[...nav.querySelectorAll('button')].map(b=>{const r=b.getBoundingClientRect();return {left:r.left,right:r.right,top:r.top,bottom:r.bottom,height:r.height}})}});
    expect(geometry.width).toBeLessThanOrEqual(viewport.width+1);expect(geometry.left).toBeGreaterThanOrEqual(18);expect(geometry.right).toBeLessThanOrEqual(viewport.width-12);expect(geometry.bottom).toBeLessThanOrEqual(viewport.height-24);expect(geometry.height).toBeLessThanOrEqual(geometry.reserve+1);
    for(const b of geometry.buttons){expect(b.height).toBeGreaterThanOrEqual(48);expect(b.left).toBeGreaterThanOrEqual(geometry.left);expect(b.right).toBeLessThanOrEqual(geometry.right);expect(b.bottom).toBeLessThanOrEqual(geometry.bottom)}
    await page.evaluate(()=>window.scrollTo(0,document.documentElement.scrollHeight));await page.waitForTimeout(60);
    const last=page.locator('main.shell [data-action]').last();if(await last.count()){const r=await last.boundingBox(),n=await page.locator('.nav').boundingBox();expect(r.y+r.height).toBeLessThanOrEqual(n.y-8)}
   }
  }
 }
});
test('teclado libera a área de escrita e restaura a navegação ao fechar',async({page})=>{
 await page.goto('/');await page.evaluate(()=>GeoApp.action('lesson:1.1:l01'));
 await page.setViewportSize({width:412,height:430});await page.locator('#lesson-note').focus();
 await page.evaluate(()=>onNativeInsets({keyboardVisible:true,top:28,bottom:24,keyboard:300}));
 await expect(page.locator('.nav')).toBeHidden();await expect(page.locator('.reader-header')).toBeHidden();
 await page.waitForTimeout(220);const r=await page.locator('#lesson-note').boundingBox();expect(r.y).toBeGreaterThanOrEqual(0);expect(r.y+r.height).toBeLessThanOrEqual(430);
 await page.locator('#lesson-note').fill('Minha anotação permanece ao abrir e fechar o teclado.');
 await page.evaluate(()=>onNativeInsets({keyboardVisible:false,top:28,bottom:24,keyboard:0}));await page.setViewportSize({width:412,height:915});await expect(page.locator('.nav')).toBeVisible();await expect(page.locator('#lesson-note')).toHaveValue('Minha anotação permanece ao abrir e fechar o teclado.');
});
test('capturas do novo visual para revisão',async({page})=>{
 await page.setViewportSize({width:412,height:915});await page.goto('/');await page.screenshot({path:'dist/ui-home.png'});
 await page.evaluate(()=>GeoApp.action('unit:1.1'));await page.screenshot({path:'dist/ui-unit.png'});
 await page.evaluate(()=>GeoApp.action('lesson:1.1:l01'));await page.screenshot({path:'dist/ui-reader.png'});
 await page.evaluate(()=>GeoApp.action('nav:settings'));await page.locator('#dark-mode').check();await page.evaluate(()=>GeoApp.action('nav:home'));await page.screenshot({path:'dist/ui-home-dark.png'});
});

test('as sete cenas mantêm escolhas didáticas, detalhes e proporção 16:9',async({page})=>{
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.emulateMedia({reducedMotion:'reduce'});await page.goto('/');
 const scenes=[['l01','inequality',2],['l03','river',2],['l05','quantitative',2],['l07','lived',3],['l09','mediation',4],['l10','scale',3],['l11','lenses',4]];
 const fs=require('node:fs');fs.mkdirSync('dist',{recursive:true});
 for(const [lesson,kind,count] of scenes){
  await page.evaluate(a=>GeoApp.action(a),'lesson:1.1:'+lesson);
  const canvas=page.locator('canvas');await canvas.scrollIntoViewIfNeeded();
  const controls=page.locator('.anim-controls .chip');await expect(controls).toHaveCount(count);
  expect(await canvas.evaluate(c=>[c.width,c.height])).toEqual([640,360]);
  let previous=await canvas.evaluate(c=>c.toDataURL());
  for(let i=1;i<count;i++){
   await controls.nth(i).click();await expect(controls.nth(i)).toHaveAttribute('aria-pressed','true');
   await expect(page.locator('.anim-controls [aria-pressed="true"]')).toHaveCount(1);
   const next=await canvas.evaluate(c=>c.toDataURL());expect(next).not.toBe(previous);previous=next;
   expect((await page.locator('.anim-description').textContent()).length).toBeGreaterThan(90);
  }
  fs.writeFileSync('dist/animation-'+kind+'.png',Buffer.from(previous.split(',')[1],'base64'));
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1)).toBeTruthy();
 }
 expect(errors).toEqual([]);
});

test('movimento pausa fora da tela e a redução de movimento conserva a interação',async({page})=>{
 await page.emulateMedia({reducedMotion:'no-preference'});await page.goto('/');
 await page.evaluate(()=>GeoApp.action('lesson:1.1:l01'));
 const canvas=page.locator('canvas');await canvas.scrollIntoViewIfNeeded();
 const frame=await canvas.evaluate(c=>c.toDataURL());
 await expect.poll(()=>canvas.evaluate(c=>c.toDataURL())).not.toBe(frame);
 await page.evaluate(()=>window.scrollTo(0,document.documentElement.scrollHeight));await page.waitForTimeout(150);
 expect(await canvas.evaluate(c=>{const r=c.getBoundingClientRect();return r.bottom<0||r.top>innerHeight})).toBeTruthy();
 const hidden=await canvas.evaluate(c=>c.toDataURL());await page.waitForTimeout(180);
 expect(await canvas.evaluate(c=>c.toDataURL())).toBe(hidden);
 await canvas.scrollIntoViewIfNeeded();await page.emulateMedia({reducedMotion:'reduce'});
 await page.waitForTimeout(100);const still=await canvas.evaluate(c=>c.toDataURL());
 await page.waitForTimeout(180);expect(await canvas.evaluate(c=>c.toDataURL())).toBe(still);
 await page.getByRole('button',{name:'Infraestrutura melhorada',exact:true}).click();
 await expect(page.locator('.anim-description')).toContainText('melhoria');
 expect(await canvas.evaluate(c=>c.toDataURL())).not.toBe(still);
 await page.evaluate(()=>GeoAnimations.mount(false));await expect(page.locator('.anim-controls .chip')).toHaveCount(2);
});
