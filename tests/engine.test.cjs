const assert=require('node:assert/strict');const {test}=require('node:test');const fs=require('node:fs');const E=require('../app/src/main/assets/engine.js');const u=JSON.parse(fs.readFileSync('content/units/1.1.json'));
test('unidade 1.5 integra o módulo completo e mantém independentes os registros das quatro anteriores',()=>{
 const current=JSON.parse(fs.readFileSync('content/units/1.5.json'));E.validateUnit(current);
 assert.equal(current.title,'Pesquisa e produção do conhecimento no campo da Geografia Escolar');
 assert.equal(current.revision,1);assert.equal(current.lessons.length,14);assert.equal(current.flashcards.length,30);
 assert.equal(current.questions.filter(q=>q.pool==='lesson').length,56);assert.equal(current.questions.filter(q=>q.pool==='final').length,20);
 const state=E.fresh();
 for(const id of ['1.1','1.2','1.3','1.4']){
  const previous=JSON.parse(fs.readFileSync('content/units/'+id+'.json'));const q=previous.questions[0];E.answer(state,id,q,q.answer,100000);
  state.notes[id+':l01']='Nota anterior '+id;state.essays[id]={lines:['Texto '+id],rubric:[0]};state.favorites.push(id+':l01');state.completed[id+':l01']={at:1};
 }
 const old=structuredClone(state);
 for(const q of current.questions)E.answer(state,current.id,q,q.answer,100000);
 const restored=E.merge(JSON.parse(JSON.stringify(state)));
 for(const id of ['1.1','1.2','1.3','1.4']){
  assert.equal(restored.notes[id+':l01'],old.notes[id+':l01']);assert.deepEqual(restored.essays[id],old.essays[id]);
  for(const key of Object.keys(old.answers).filter(k=>k.startsWith(id+':')))assert.deepEqual(restored.answers[key],old.answers[key]);
 }
 assert.deepEqual(restored.favorites,old.favorites);assert.deepEqual(restored.completed,old.completed);
 assert.equal(E.errors(restored,current).length,0);assert.equal(Object.keys(restored.answers).filter(k=>k.startsWith('1.5:')).length,76);
});
test('conteúdo publicado é completo e coerente',()=>{E.validateUnit(u);assert.equal(u.revision,2);assert.equal(u.lessons.length,12);assert.equal(u.questions.filter(q=>q.pool==='final').length,20);assert.equal(u.questions.length,76);assert.equal(u.flashcards.length,24)});
test('revisão didática mantém o significado das respostas e os registros da primeira versão',()=>{
 const {execFileSync}=require('node:child_process');
 const old=JSON.parse(execFileSync('python3',['-c','import zipfile;z=zipfile.ZipFile("content/packages/1.1-r1.zip");print(z.read("unit.json").decode())'],{encoding:'utf8'}));
 const s=E.fresh();
 for(const q of old.questions){E.answer(s,old.id,q,q.answer,100000);const current=u.questions.find(x=>x.id===q.id);assert.ok(current);for(const field of ['stem','options','answer'])assert.deepEqual(current[field],q[field]);}
 s.completed['1.1:l06']={at:1};s.notes['1.1:l06']='Minha leitura anterior';s.favorites=['1.1:l06'];s.essays['1.1']={lines:['Texto já salvo'],rubric:[0,4]};
 const restored=E.merge(JSON.parse(JSON.stringify(s)));
 assert.equal(restored.notes['1.1:l06'],'Minha leitura anterior');assert.equal(E.progress(restored,u).done,1);assert.deepEqual(restored.favorites,s.favorites);assert.deepEqual(restored.essays,s.essays);
 for(const q of old.questions)assert.equal(restored.answers['1.1:'+q.id].correct,true);
 assert.ok(u.questions.filter(q=>q.pool==='final').every(q=>!old.questions.some(x=>x.id===q.id)));
 for(let i=0;i<old.essay.rubric.length;i++)assert.equal(u.essay.rubric[i],old.essay.rubric[i]);
});
test('revisão 2 da 1.2 conserva os 60 problemas antigos e o caderno, com simulado próprio',()=>{
 const current=JSON.parse(fs.readFileSync('content/units/1.2.json'));
 const {execFileSync}=require('node:child_process');
 const old=JSON.parse(execFileSync('python3',['-c','import zipfile;z=zipfile.ZipFile("content/packages/1.2-r1.zip");print(z.read("unit.json").decode())'],{encoding:'utf8'}));
 E.validateUnit(current);assert.equal(current.revision,2);assert.equal(current.questions.length,80);assert.equal(current.flashcards.length,30);
 const s=E.fresh();
 for(const q of old.questions){
  E.answer(s,old.id,q,q.answer,100000);
  const found=current.questions.find(x=>x.id===q.id);assert.ok(found);
  for(const field of ['lesson','stem','options','answer','feedback','tag','type'])assert.deepEqual(found[field],q[field]);
  assert.equal(found.pool,'lesson');
 }
 for(const lesson of old.lessons)assert.ok(current.lessons.some(l=>l.id===lesson.id));
 for(const card of old.flashcards)assert.equal(current.flashcards.find(c=>c.id===card.id).front,card.front);
 s.notes['1.2:l05']='Anotação feita antes da revisão';s.completed['1.2:l05']={at:1};s.favorites=['1.2:l05'];s.essays['1.2']={lines:['Texto anterior da 1.2'],rubric:[0,5]};s.notes['1.1:l01']='Anotação da 1.1';
 const restored=E.merge(JSON.parse(JSON.stringify(s)));
 for(const q of old.questions){assert.equal(restored.answers['1.2:'+q.id].choice,q.answer);assert.equal(restored.answers['1.2:'+q.id].correct,true);}
 assert.equal(restored.notes['1.2:l05'],s.notes['1.2:l05']);assert.equal(E.progress(restored,current).done,1);assert.deepEqual(restored.essays,s.essays);assert.deepEqual(restored.favorites,s.favorites);assert.equal(restored.notes['1.1:l01'],s.notes['1.1:l01']);
 assert.deepEqual(current.essay.rubric.slice(0,old.essay.rubric.length),old.essay.rubric);
 const exam=current.questions.filter(q=>q.pool==='final');assert.equal(exam.length,20);
 assert.ok(exam.every(q=>!old.questions.some(x=>x.id===q.id)));
});
test('um erro permanece para revisar; um novo acerto reinicia a progressão',()=>{const s=E.fresh(),q=u.questions[0],now=100000;E.answer(s,u.id,q,(q.answer+1)%q.options.length,now);assert.equal(E.errors(s,u).length,1);assert.equal(E.due(s,u,now+86400001).length,1);E.answer(s,u.id,q,q.answer,now+1000);assert.equal(E.errors(s,u).length,0);assert.equal(s.review['1.1:'+q.id].stage,1);E.answer(s,u.id,q,q.answer,now+2000);assert.equal(s.review['1.1:'+q.id].stage,2);assert.equal(s.review['1.1:'+q.id].due,now+2000+3*86400000)});
test('atualizar conteúdo conserva progresso por identificadores',()=>{const s=E.fresh();s.completed['1.1:l01']={at:1};s.notes['1.1:l01']='Exemplo de uma comunidade';s.essays['1.1']={lines:['Minha tese'],rubric:[0]};const restored=E.merge(JSON.parse(JSON.stringify(s)));assert.equal(E.progress(restored,u).done,1);assert.equal(restored.notes['1.1:l01'],s.notes['1.1:l01']);assert.deepEqual(restored.essays,s.essays)});
test('dados e imagens não podem executar conteúdo do repositório',()=>{assert.equal(E.escape('<img onerror="run()">'),'&lt;img onerror=&quot;run()&quot;&gt;');assert.equal(E.safeMedia('media/../../evil.js'),false);assert.equal(E.safeMedia('https://other.example/image.jpg'),false);assert.equal(E.safeMedia('media/foto.jpg'),true);const broken=structuredClone(u);broken.questions[0].answer=99;assert.throws(()=>E.validateUnit(broken));broken.questions[0].answer=1;broken.lessons[0].blocks[0].type='script';assert.throws(()=>E.validateUnit(broken))});
test('unidade 1.3 acrescenta um percurso completo sem colidir com o caderno anterior',()=>{
 const current=JSON.parse(fs.readFileSync('content/units/1.3.json'));
 const catalog=JSON.parse(fs.readFileSync('content/catalog.json'));
 E.validateUnit(current);assert.equal(current.revision,1);assert.equal(current.lessons.length,14);assert.equal(current.flashcards.length,30);
 assert.equal(current.questions.filter(q=>q.pool==='lesson').length,56);assert.equal(current.questions.filter(q=>q.pool==='final').length,20);
 assert.equal(catalog.modules.flatMap(m=>m.units).length,15);assert.equal(catalog.modules.flatMap(m=>m.units).filter(e=>e.status==='published').length,5);
 const state=E.fresh();state.notes['1.1:l01']='Nota da 1.1';state.notes['1.2:l05']='Nota da 1.2';state.essays['1.2']={lines:['Redação anterior'],rubric:[0,5]};
 const previous=JSON.parse(fs.readFileSync('content/units/1.2.json'));const old=previous.questions[0];E.answer(state,'1.2',old,old.answer,100000);
 for(const q of current.questions)E.answer(state,'1.3',q,q.answer,100000);
 const restored=E.merge(JSON.parse(JSON.stringify(state)));
 assert.equal(restored.notes['1.1:l01'],state.notes['1.1:l01']);assert.equal(restored.notes['1.2:l05'],state.notes['1.2:l05']);assert.deepEqual(restored.essays,state.essays);
 assert.equal(restored.answers['1.2:'+old.id].choice,old.answer);assert.equal(E.errors(restored,current).length,0);
 assert.equal(Object.keys(restored.answers).filter(k=>k.startsWith('1.3:')).length,76);
});
test('novas fontes não alteram os pacotes publicados das unidades anteriores',()=>{
 const crypto=require('node:crypto');const catalog=JSON.parse(fs.readFileSync('content/catalog.json'));
 for(const [id,expected] of [['1.1','e70370e03ae34d053fce834c499a5ca1b346bf2ddc82c07ff9d9593f9147ba43'],['1.2','f8c80aaccaab1474a70e79e4887f57eec818d0e9c37c2a3105c692e99b624ac5'],['1.3','99859ba818f31e02f94b6ce66e313eb4c7a49cade5794e4a6b651703b93182c1'],['1.4','4d81eccba2e3f9274eec4f172bef4d07ca8c132a98294818801fca275c722c5c']]){
  const entry=catalog.modules.flatMap(m=>m.units).find(e=>e.id===id);const bytes=fs.readFileSync('content/'+entry.package);
  assert.equal(crypto.createHash('sha256').update(bytes).digest('hex'),expected);assert.equal(entry.sha256,expected);
 }
 const {execFileSync}=require('node:child_process');
 const credits=JSON.parse(execFileSync('python3',['-c','import zipfile;z=zipfile.ZipFile("content/packages/1.3-r1.zip");print(z.read("media/CREDITS.txt").decode())'],{encoding:'utf8'}));
 const current=JSON.parse(fs.readFileSync('content/units/1.3.json'));const used=[...new Set(current.lessons.flatMap(l=>l.blocks.filter(b=>b.type==='photo').map(b=>b.src.split('/').at(-1))))].sort();
 assert.deepEqual(credits.map(c=>c.filename).sort(),used);
});
test('unidade 1.4 acrescenta conteúdo compatível e conserva o estudo das três anteriores',()=>{
 const current=JSON.parse(fs.readFileSync('content/units/1.4.json'));E.validateUnit(current);
 assert.equal(current.revision,1);assert.equal(current.lessons.length,14);assert.equal(current.questions.length,76);assert.equal(current.flashcards.length,30);assert.equal(current.questions.filter(q=>q.pool==='final').length,20);
 const state=E.fresh();
 for(const id of ['1.1','1.2','1.3']){
  const old=JSON.parse(fs.readFileSync('content/units/'+id+'.json'));const q=old.questions[0];E.answer(state,id,q,q.answer,100000);
  state.notes[id+':l01']='Nota da '+id;state.essays[id]={lines:['Texto anterior '+id],rubric:[0]};
 }
 const before=JSON.parse(JSON.stringify(state));for(const q of current.questions)E.answer(state,current.id,q,q.answer,100000);
 const restored=E.merge(JSON.parse(JSON.stringify(state)));assert.deepEqual(restored.notes,before.notes);assert.deepEqual(restored.essays,before.essays);
 for(const key of Object.keys(before.answers))assert.deepEqual(restored.answers[key],before.answers[key]);
 assert.equal(E.errors(restored,current).length,0);assert.equal(Object.keys(restored.answers).filter(k=>k.startsWith('1.4:')).length,76);
});
