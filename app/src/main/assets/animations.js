(function(){
'use strict';
const scenes={
 inequality:{choices:['Acesso vulnerável','Infraestrutura melhorada'],explanations:['A chuva intensa alcança as duas áreas. Na cena hipotética, o trajeto sem infraestrutura apresenta mais obstáculos. Observe que o evento natural interage com condições de acesso e proteção.','A melhoria representada facilita o acesso da segunda área. O efeito ilustra a participação de escolhas e infraestrutura; não é previsão de risco nem significa que uma obra elimina todos os problemas.']},
 river:{choices:['Rio como destino','Rio + práticas sociais'],explanations:['A explicação “o rio determina como todos vivem” transforma uma condição em destino. Ela deixa de examinar técnicas, escolhas, história e diferenças entre grupos.','Grupos podem mobilizar técnicas e práticas distintas diante do mesmo rio. As condições naturais continuam relevantes, mas se relacionam com ações e organização social.']},
 quantitative:{choices:['Rota pelo rio','Rota pela estrada'],explanations:['Rota hipotética A: 8 km e 45 minutos. Uma distância menor pode exigir mais tempo, dependendo do meio de transporte e das condições do trajeto.','Rota hipotética B: 15 km e 25 minutos. Compare distância e tempo: as medidas descrevem aspectos diferentes. Um modelo precisa considerar seus pressupostos.']},
 lived:{choices:['Pessoa 1','Pessoa 2','Pessoa 3'],explanations:['Relato fictício: “Aqui encontro pessoas com quem trabalho e organizo minha rotina.” A praça é vivida como parte das relações de trabalho.','Relato fictício: “Venho conversar com meus amigos; sinto que faço parte deste lugar.” A experiência destaca encontro e pertencimento.','Relato fictício: “Lembro da infância, mas hoje sinto dificuldade para circular aqui.” Memória e desconforto podem coexistir. Um lugar não tem o mesmo sentido para todos.']},
 mediation:{choices:['1. Relato','2. Pergunta','3. Conceito','4. Explicação'],explanations:['Ponto de partida: “No período de chuva, fica difícil chegar à escola.” O relato oferece uma referência cotidiana para investigar.','Intervenção: “Quais trajetos e grupos são mais afetados? Como isso se relaciona com infraestrutura e circulação?” A pergunta orienta a investigação.','Mediação: o professor mobiliza redes, acesso e circulação para comparar fontes e ampliar a interpretação. O conceito não é uma definição solta.','Avanço: os estudantes relacionam condições naturais, infraestrutura e decisões a diferenças de acesso. A nova explicação pode ser avaliada por conceitos e evidências.']},
 scale:{choices:['Comunidade','Município','Rede regional'],explanations:['Na comunidade, observamos trajetos e pontos de acesso. Esse recorte revela experiências e condições próximas, mas não mostra todas as conexões.','No município, comparamos comunidades, serviços e circulação. Aparecem diferenças e relações que ultrapassam um trajeto específico.','Na rede regional, investigamos fluxos, mercados e decisões em outras escalas. O lugar participa de relações mais amplas e não é uma ilha.']},
 lenses:{choices:['Descrever','Medir padrões','Investigar poder','Ouvir experiências'],explanations:['Pergunta: que formas e usos caracterizam a paisagem? Observar e descrever ajuda a reconhecer elementos e diferenciações; é um passo da investigação.','Pergunta: como variam fluxos, distâncias e tempos? Medidas e modelos ajudam a investigar padrões, com critérios e limites.','Pergunta: como trabalho, decisões e relações de poder organizam o circuito? Outras fontes são necessárias para construir uma análise crítica.','Pergunta: que sentidos as pessoas atribuem ao lugar? Relatos e representações podem ampliar o conhecimento das experiências vividas.']}
};

let cleanup=null;
window.GeoAnimations={
 stop(){if(cleanup){cleanup();cleanup=null}},
 mount(motion=true){
  this.stop();
  const reduce=matchMedia('(prefers-reduced-motion: reduce)');
  const start=performance.now();
  let active=true,lastFrame=-100,frameId=0,observer=null;
  const nodes=[...document.querySelectorAll('[data-animation]')].map(el=>{
   const kind=el.dataset.animation,scene=scenes[kind];if(!scene)return null;
   const canvas=el.querySelector('canvas'),ctx=canvas.getContext('2d',{alpha:false});
   const info=el.querySelector('.anim-description'),controls=el.querySelector('.anim-controls');
   const backgrounds=new Map();let choice=0;
   controls.replaceChildren();
   const item={canvas,visible:false,paint(t=0){
    if(!backgrounds.has(choice))backgrounds.set(choice,GeoPixelScenes.terrain(kind,choice));
    GeoPixelScenes.paint(ctx,kind,choice,t,backgrounds.get(choice));
   }};
   const choose=i=>{
    choice=i;info.textContent=scene.explanations[choice];
    [...controls.children].forEach((button,n)=>{
     button.classList.toggle('selected',n===choice);
     button.setAttribute('aria-pressed',String(n===choice));
    });
    item.paint();
   };
   scene.choices.forEach((text,i)=>{
    const button=document.createElement('button');button.type='button';button.className='chip';
    button.textContent=text;button.onclick=()=>choose(i);controls.appendChild(button);
   });
   choose(0);
   return item;
  }).filter(Boolean);
  const animated=()=>motion&&!reduce.matches&&!document.hidden;
  const schedule=()=>{if(active&&!frameId&&animated()&&nodes.some(n=>n.visible))frameId=requestAnimationFrame(frame)};
  function frame(now){
   frameId=0;if(!active||!animated())return;
   if(now-lastFrame>=1000/24){lastFrame=now;const t=(now-start)/1000;
    nodes.forEach(n=>{if(n.visible)n.paint(t)});
   }
   schedule();
  }
  function bounds(){
   nodes.forEach(n=>{const r=n.canvas.getBoundingClientRect();n.visible=r.bottom>0&&r.top<innerHeight&&r.right>0&&r.left<innerWidth});
   schedule();
  }
  function visibility(){
   if(frameId){cancelAnimationFrame(frameId);frameId=0}
   if(!reduce.matches)bounds();else nodes.forEach(n=>n.paint());
  }
  if(window.IntersectionObserver){
   observer=new IntersectionObserver(entries=>{
    entries.forEach(e=>{const n=nodes.find(n=>n.canvas===e.target);if(n)n.visible=e.isIntersecting});
    schedule();
   });
   nodes.forEach(n=>observer.observe(n.canvas));
  }
  document.addEventListener('visibilitychange',visibility);
  window.addEventListener('resize',bounds);
  window.addEventListener('scroll',bounds,{passive:true});
  if(reduce.addEventListener)reduce.addEventListener('change',visibility);else reduce.addListener(visibility);
  cleanup=()=>{
   active=false;if(frameId)cancelAnimationFrame(frameId);observer?.disconnect();
   document.removeEventListener('visibilitychange',visibility);
   window.removeEventListener('resize',bounds);window.removeEventListener('scroll',bounds);
   if(reduce.removeEventListener)reduce.removeEventListener('change',visibility);else reduce.removeListener(visibility);
  };
  bounds();
 }
};
})();
