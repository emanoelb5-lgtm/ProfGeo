(function(root){
'use strict';
const DAY=86400000;
const E={
 fresh(){return {schemaVersion:1,completed:{},last:null,answers:{},review:{},notes:{},essays:{},favorites:[],sessions:[],settings:{font:17,dark:false,motion:true,autoSync:true,dailyMinutes:25},studyDays:{}}},
 merge(raw){const base=E.fresh();if(!raw||typeof raw!=='object'||Array.isArray(raw))return base;for(const k of ['completed','answers','review','notes','essays','studyDays'])if(raw[k]&&typeof raw[k]==='object'&&!Array.isArray(raw[k]))base[k]=raw[k];for(const k of ['favorites','sessions'])if(Array.isArray(raw[k]))base[k]=raw[k];if(raw.last&&typeof raw.last==='object')base.last=raw.last;if(raw.settings&&typeof raw.settings==='object')Object.assign(base.settings,raw.settings);base.settings.font=Math.max(15,Math.min(24,Number(base.settings.font)||17));base.settings.dailyMinutes=Math.max(5,Math.min(180,Number(base.settings.dailyMinutes)||25));return base},
 validateUnit(u){if(!u||u.schemaVersion!==1||!/^\d{1,2}\.\d{1,2}$/.test(u.id)||!Number.isInteger(u.revision)||u.revision<1||!Array.isArray(u.lessons)||!u.lessons.length||!Array.isArray(u.questions)||!u.questions.length)throw Error('Unidade incompatível.');const ids=new Set();for(const l of u.lessons){if(ids.has(l.id)||!Array.isArray(l.blocks)||!l.blocks.length)throw Error('Lição inválida.');ids.add(l.id);for(const b of l.blocks)if(!['text','callout','list','photo','animation','compare','table'].includes(b.type))throw Error('Recurso exige uma versão mais nova do app.')}const qs=new Set();for(const q of u.questions){if(qs.has(q.id)||!Array.isArray(q.options)||q.options.length<2||!Number.isInteger(q.answer)||q.answer<0||q.answer>=q.options.length||!Array.isArray(q.feedback)||q.feedback.length!==q.options.length)throw Error('Exercício inválido.');qs.add(q.id)}return u},
 key(u,q){return `${u}:${q}`},
 answer(s,u,q,choice,now=Date.now()){if(!Number.isInteger(choice)||choice<0||choice>=q.options.length)throw Error('Escolha inválida');const k=E.key(u,q.id),correct=choice===q.answer,prev=s.answers[k];s.answers[k]={choice,correct,attempts:(prev?.attempts||0)+1,lastAt:now};const r=s.review[k]||{stage:0};r.stage=correct?Math.min(3,(r.stage||0)+1):0;r.due=now+[1,1,3,7][r.stage]*DAY;r.unit=u;r.question=q.id;r.lastCorrect=correct;s.review[k]=r;const day=new Date(now).toLocaleDateString('en-CA');s.studyDays[day]=(s.studyDays[day]||0)+1;return correct},
 progress(s,u){const done=u.lessons.filter(l=>s.completed[E.key(u.id,l.id)]).length;return {done,total:u.lessons.length,percent:Math.round(done/u.lessons.length*100)}},
 errors(s,u){return u.questions.filter(q=>s.answers[E.key(u.id,q.id)]?.correct===false)},
 due(s,u,now=Date.now()){return u.questions.filter(q=>{const r=s.review[E.key(u.id,q.id)];return r&&r.due<=now})},
 shuffle(a,seed=Math.random){const b=[...a];for(let i=b.length-1;i>0;i--){const j=Math.floor(seed()*(i+1));[b[i],b[j]]=[b[j],b[i]]}return b},
 safeMedia(src){return typeof src==='string'&&/^media\/[a-zA-Z0-9._/-]+$/.test(src)&&!src.includes('..')},
 escape(v){return String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
};root.GeoEngine=E;if(typeof module!=='undefined'&&module.exports)module.exports=E;
})(typeof window!=='undefined'?window:globalThis);
