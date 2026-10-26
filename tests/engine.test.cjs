const assert=require('node:assert/strict');const {test}=require('node:test');const fs=require('node:fs');const E=require('../app/src/main/assets/engine.js');const u=JSON.parse(fs.readFileSync('content/units/1.1.json'));
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
test('um erro permanece para revisar; um novo acerto reinicia a progressão',()=>{const s=E.fresh(),q=u.questions[0],now=100000;E.answer(s,u.id,q,(q.answer+1)%q.options.length,now);assert.equal(E.errors(s,u).length,1);assert.equal(E.due(s,u,now+86400001).length,1);E.answer(s,u.id,q,q.answer,now+1000);assert.equal(E.errors(s,u).length,0);assert.equal(s.review['1.1:'+q.id].stage,1);E.answer(s,u.id,q,q.answer,now+2000);assert.equal(s.review['1.1:'+q.id].stage,2);assert.equal(s.review['1.1:'+q.id].due,now+2000+3*86400000)});
test('atualizar conteúdo conserva progresso por identificadores',()=>{const s=E.fresh();s.completed['1.1:l01']={at:1};s.notes['1.1:l01']='Exemplo de uma comunidade';s.essays['1.1']={lines:['Minha tese'],rubric:[0]};const restored=E.merge(JSON.parse(JSON.stringify(s)));assert.equal(E.progress(restored,u).done,1);assert.equal(restored.notes['1.1:l01'],s.notes['1.1:l01']);assert.deepEqual(restored.essays,s.essays)});
test('dados e imagens não podem executar conteúdo do repositório',()=>{assert.equal(E.escape('<img onerror="run()">'),'&lt;img onerror=&quot;run()&quot;&gt;');assert.equal(E.safeMedia('media/../../evil.js'),false);assert.equal(E.safeMedia('https://other.example/image.jpg'),false);assert.equal(E.safeMedia('media/foto.jpg'),true);const broken=structuredClone(u);broken.questions[0].answer=99;assert.throws(()=>E.validateUnit(broken));broken.questions[0].answer=1;broken.lessons[0].blocks[0].type='script';assert.throws(()=>E.validateUnit(broken))});
