const {test,expect}=require('@playwright/test');
test('percurso completo, correção, anotações, redação e restauração',async({page})=>{
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('/');await expect(page.getByText('Compreender.')).toBeVisible();
 await page.getByRole('button',{name:/Começar a unidade/}).click();
 await expect(page.locator('.lesson-item')).toHaveCount(12);
 await page.locator('.lesson-item').first().click();
 await expect(page.locator('canvas')).toBeVisible();
 const dimensions=await page.locator('canvas').evaluate(c=>[c.width,c.height]);expect(dimensions).toEqual([320,180]);
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
