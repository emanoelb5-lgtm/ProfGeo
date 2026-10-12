/* Original pixel scenery, drawn locally. No network or image assets required. */
(function(){
'use strict';
const W=640,H=360;
const P={ink:'#193e39',sky:'#d7eee6',cloud:'#f7f5e8',cream:'#f1e5c9',sand:'#d8c4a0',wood:'#927055',woodDark:'#614d3b',roof:'#b75f46',roofLight:'#d98862',green:'#427661',leaf:'#709568',leafLight:'#a8bb76',water:'#579a94',waterLight:'#a2ccc1',road:'#84918a',gold:'#e7c47b',blue:'#607d93'};
function R(c,x,y,w,h,color){c.fillStyle=color;c.fillRect(Math.round(x),Math.round(y),Math.round(w),Math.round(h))}
function F(c,points,color){c.fillStyle=color;c.beginPath();points.forEach(([x,y],i)=>i?c.lineTo(Math.round(x),Math.round(y)):c.moveTo(Math.round(x),Math.round(y)));c.closePath();c.fill()}
function L(c,points,color,width=2){c.strokeStyle=color;c.lineWidth=width;c.lineCap='square';c.lineJoin='bevel';c.beginPath();points.forEach(([x,y],i)=>i?c.lineTo(Math.round(x),Math.round(y)):c.moveTo(Math.round(x),Math.round(y)));c.stroke()}
function disk(c,x,y,r,color){for(let k=-r;k<r;k+=2){const half=Math.floor(Math.sqrt(Math.max(0,r*r-k*k)));R(c,x-half,y+k,half*2,2,color)}}
function label(c,text,x,y,size=16,color=P.ink){c.font=`600 ${size}px Arial`;c.fillStyle=color;c.fillText(text,Math.round(x),Math.round(y))}
function patch(c,text,x,y,size=15,color=P.ink,fill='#f7f4e8'){c.font=`600 ${size}px Arial`;const w=Math.ceil(c.measureText(text).width)+22;R(c,x+3,y,w-6,27,fill);R(c,x,y+3,w,21,fill);label(c,text,x+11,y+19,size,color);return w}
function shadow(c,x,y,w){R(c,x+6,y,w-12,3,'#314d3920');R(c,x,y+3,w,4,'#314d3930');R(c,x+7,y+7,w-14,2,'#314d3918')}
function cloud(c,x,y,s=1,rain=false){const a=rain?'#a9c2c2':'#f6f5e9',b=rain?'#bed0cc':'#fffbed';R(c,x,y+12*s,83*s,12*s,a);R(c,x+12*s,y+3*s,28*s,19*s,b);R(c,x+36*s,y,24*s,24*s,b);R(c,x+61*s,y+8*s,17*s,13*s,b)}
function sky(c,rain=false){
 const shades=rain?['#b4caca','#bdd2ce','#c9dcd3','#d1e1d2']:['#c9e5dc','#d5ece1','#e0eee1','#ecf0dc'];
 shades.forEach((color,i)=>R(c,0,i*47,W,48,color));
 if(!rain){disk(c,531,72,33,'#f1e6b5');disk(c,531,72,24,'#f5d999');R(c,510,51,16,2,'#fff0c4')}
 cloud(c,58,57,1.1,rain);cloud(c,354,36,.8,rain);cloud(c,217,81,.6,rain);
 F(c,[[0,170],[44,143],[80,148],[110,137],[152,163],[191,142],[233,147],[270,125],[317,155],[365,143],[399,151],[440,133],[493,148],[535,131],[588,150],[640,140],[640,219],[0,219]],rain?'#88a394':'#a9c1a0');
 F(c,[[0,184],[62,172],[101,184],[144,165],[202,186],[252,175],[304,189],[343,169],[399,181],[461,165],[523,184],[580,173],[640,178],[640,223],[0,223]],'#83a68a');
}
function ground(c,y=194){R(c,0,y,W,H-y,'#afbf8b');R(c,0,y+2,W,3,'#bed09a');for(let i=0;i<165;i++){const x=(i*97+19)%640,gy=y+((i*41+11)%(360-y));R(c,x,gy,3+(i%4),2,i%3===0?'#c8d49f':'#98ae79')}}
function tree(c,x,y,s=1,palm=false){
 c.save();c.translate(x,y);c.scale(s,s);shadow(c,-8,79,53);
 R(c,17,34,9,46,'#715d45');R(c,20,34,3,46,'#a28a5d');R(c,15,77,15,4,'#5c583e');
 if(palm){F(c,[[21,17],[-13,15],[-28,37],[6,26],[20,22]],P.green);F(c,[[22,17],[49,9],[67,27],[42,24],[24,22]],P.green);F(c,[[21,18],[28,-2],[43,-9],[35,15],[24,23]],P.leaf);F(c,[[21,19],[-4,-1],[-17,4],[9,16],[20,25]],P.leafLight);R(c,18,23,13,8,P.woodDark)}
 else{F(c,[[3,18],[12,5],[31,2],[43,11],[47,28],[43,43],[31,50],[5,43],[-5,31]],'#345d49');F(c,[[1,18],[13,8],[32,7],[41,15],[39,32],[21,43],[1,36]],P.green);R(c,8,12,17,9,P.leaf);R(c,1,22,12,9,P.leaf);R(c,23,8,10,5,P.leafLight);R(c,25,26,11,9,'#598960');R(c,6,33,8,5,'#80a467')}
 c.restore();
}
function plant(c,x,y){L(c,[[x,y],[x-7,y-14]],P.green,3);L(c,[[x,y],[x+6,y-17]],P.leaf,3);L(c,[[x,y],[x+13,y-8]],P.green,3);R(c,x-2,y-7,3,8,P.wood)}
function windowBox(c,x,y){R(c,x,y,16,17,P.woodDark);R(c,x+2,y+2,12,12,'#668e8c');R(c,x+3,y+3,5,5,'#acd5c4');R(c,x+7,y+1,2,15,P.cream);R(c,x-1,y+16,18,3,'#c7b281')}
function house(c,x,y,color=P.cream,stilt=false){
 shadow(c,x-4,y+84,94);if(stilt){for(const dx of [7,34,66]){R(c,x+dx,y+64,5,37,P.woodDark);R(c,x+dx,y+67,2,31,P.wood)}}
 R(c,x,y+24,77,55,color);R(c,x+61,y+26,16,53,'#c3b391');R(c,x+1,y+25,5,54,'#fff1d2');
 for(let dy=32;dy<78;dy+=8)R(c,x+7,y+dy,54,1,'#baa987');
 F(c,[[x-8,y+28],[x+35,y],[x+85,y+28]],P.woodDark);F(c,[[x-7,y+24],[x+35,y-3],[x+84,y+24]],P.roof);F(c,[[x+35,y-3],[x+84,y+24],[x+69,y+24],[x+29,y+1]],'#994c3c');
 for(let i=0;i<4;i++)L(c,[[x+10+i*9,y+17-i*5],[x+53+i*5,y+21]],P.roofLight,2);
 R(c,x-7,y+24,91,4,'#7d4736');windowBox(c,x+10,y+37);windowBox(c,x+46,y+37);
 R(c,x+30,y+48,15,31,P.woodDark);R(c,x+33,y+51,9,27,P.wood);R(c,x+40,y+64,2,2,P.gold);R(c,x-2,y+78,83,5,P.wood);R(c,x+25,y+83,27,4,P.sand);
}
function school(c,x,y,s=1){
 c.save();c.translate(x,y);c.scale(s,s);shadow(c,-6,85,124);R(c,0,22,114,62,P.cream);R(c,99,24,15,60,'#c4b58e');R(c,4,27,4,48,'#fff4d6');R(c,0,71,114,13,'#b98767');
 for(let row=0;row<2;row++)for(let col=0;col<9;col++)R(c,6+col*12+(row%2)*4,73+row*5,9,1,'#925c4c');
 F(c,[[-8,23],[55,-3],[122,23]],P.roof);F(c,[[55,-3],[122,23],[105,23],[47,1]],'#8d4b3c');R(c,-8,23,130,5,'#6c4234');
 R(c,37,31,41,17,'#fff3d8');label(c,'ESCOLA',41,43,10);windowBox(c,12,42);windowBox(c,85,42);R(c,45,51,24,33,P.ink);R(c,47,54,9,30,'#437c6a');R(c,58,54,9,30,'#386c5f');R(c,40,84,33,5,P.sand);R(c,36,89,40,3,'#f0dab0');
 c.restore();
}
function road(c,points,width=14){L(c,points,'#6b7b72',width+5);L(c,points,'#9ba399',width);c.save();c.setLineDash([9,12]);L(c,points,'#e7e4ca',2);c.restore()}
function waterBase(c,y=233,h=127){R(c,0,y,W,h,P.water);R(c,0,y,W,4,'#3e8078');R(c,0,y+4,W,3,'#76aca1');for(let i=0;i<36;i++)R(c,(i*97)%620,y+15+(i*31)%(h-20),15+i%13,2,i%3?'#6bafa4':'#447f7c')}
function waves(c,t,y=240,h=100){for(let i=0;i<20;i++){const x=((i*79+t*(4+i%3))%676)-25,wy=y+9+(i*23)%h;R(c,x,wy,12+i%13,2,'#9bccba75');R(c,x+7,wy+5,9,1,'#bee0ce55')}}
function pier(c,x,y){for(const dx of [3,31,61]){R(c,x+dx,y+1,5,35,P.woodDark);R(c,x+dx,y,2,35,P.wood)}R(c,x,y,76,9,P.wood);for(let dx=5;dx<72;dx+=8)R(c,x+dx,y,1,9,'#c9ae7d');R(c,x,y-10,3,20,P.woodDark);R(c,x+69,y-10,3,20,P.woodDark)}
function person(c,x,y,color,t=0,options={}){
 const {walk=false,selected=false,teacher=false,skin='#ba8b62',seed=0}=options;
 const step=walk?Math.sin(t*7+seed):0,bob=walk?Math.abs(step)*1.7:Math.sin(t*2+seed)*.6;
 if(selected){disk(c,x+10,y+38,19,'#e8c87955');L(c,[[x-9,y+38],[x-6,y+45],[x+27,y+45],[x+30,y+38]],P.gold,2)}else shadow(c,x-3,y+37,28);
 R(c,x+2,y+24,7,13+step*2,'#344c47');R(c,x+12,y+24,7,13-step*2,'#344c47');R(c,x+1,y+36+step*2,9,3,P.woodDark);R(c,x+12,y+36-step*2,9,3,P.woodDark);
 R(c,x+1,y+10+bob,19,18,color);R(c,x+3,y+12+bob,3,15,'#ffffff30');R(c,x+15,y+12+bob,5,16,'#17332a35');R(c,x-2,y+13+bob,4,12+step,skin);
 R(c,x+20,y+(teacher?9:13)+bob,4,teacher?8:12-step,skin);if(teacher)R(c,x+23,y+8+bob,9,4,skin);
 if(!teacher){R(c,x+17,y+14+bob,6,12,'#c58c55');R(c,x+18,y+14+bob,2,11,P.gold)}
 R(c,x+5,y-4+bob,12,13,skin);R(c,x+14,y-2+bob,3,9,'#976343');R(c,x+4,y-5+bob,14,4,'#403d34');R(c,x+4,y-1+bob,3,5,'#403d34');R(c,x+14,y+1+bob,2,2,P.ink);R(c,x+10,y+9+bob,6,3,skin);
}
function boat(c,x,y,t=0,small=false){
 c.save();c.translate(Math.round(x),Math.round(y+Math.sin(t*2)*1.5));if(small)c.scale(.7,.7);
 R(c,-15,31,25,2,'#c6ded09a');R(c,-8,36,32,2,'#add4c191');R(c,10,39,38,1,'#b8dccc');
 F(c,[[0,23],[76,23],[66,35],[10,35]],P.woodDark);F(c,[[3,23],[72,23],[65,30],[12,30]],P.roof);R(c,8,25,57,3,P.roofLight);R(c,22,8,32,15,P.cream);R(c,20,5,36,4,'#365f52');R(c,26,11,12,8,P.blue);R(c,41,11,8,8,'#88b8b0');R(c,64,17,6,8,P.ink);R(c,9,17,8,6,P.wood);R(c,32,9,2,10,'#d6c6a0');
 c.restore();
}
function bus(c,x,y,t=0){
 shadow(c,x-3,y+32,69);disk(c,x+12,y+29,7,P.ink);disk(c,x+48,y+29,7,P.ink);disk(c,x+12,y+29,3,'#b9beb0');disk(c,x+48,y+29,3,'#b9beb0');R(c,x,y,59,27,'#c7864e');R(c,x+2,y+2,54,11,P.gold);R(c,x+3,y+19,52,3,'#f4dca1');
 for(let i=0;i<4;i++){R(c,x+6+i*12,y+5,9,9,'#507c7c');R(c,x+7+i*12,y+5,7,2,'#a5d1ba')}R(c,x+49,y+13,6,14,P.woodDark);R(c,x+57,y+19,3,4,'#ffeba9');
}
function birds(c,t){for(let i=0;i<2;i++){const x=((t*9+i*91)%740)-40,y=105+i*14;L(c,[[x-4,y+Math.sin(t*3+i)*2],[x,y+3],[x+4,y+Math.sin(t*3+i)*2]],'#446c6066',2)}}
function rain(c,t){for(let i=0;i<58;i++){const x=(i*83+t*16)%670-15,y=55+((i*43+t*76)%276);L(c,[[x,y],[x-4,y+8]],'#7c9b9a88',2)}for(let i=0;i<8;i++){const x=35+i*77;R(c,x,302+((i*7)%22),5+Math.floor((t*4+i)%3)*3,1,'#bfd8c2')}}
function arrow(c,x,y,angle,color=P.gold){c.save();c.translate(x,y);c.rotate(angle);F(c,[[-5,-5],[6,0],[-5,5],[-2,0]],color);c.restore()}
function flow(c,points,t,color=P.gold){L(c,points,color+'65',3);for(let i=0;i<points.length-1;i++){const [a,b]=[points[i],points[i+1]],u=(t*.4+i*.17)%1;const x=a[0]+(b[0]-a[0])*u,y=a[1]+(b[1]-a[1])*u;disk(c,x,y,4,color);arrow(c,x,y,Math.atan2(b[1]-a[1],b[0]-a[0]),color)}}
function streetLamp(c,x,y){R(c,x,y,4,60,P.ink);R(c,x-8,y-4,21,5,P.woodDark);R(c,x-5,y+1,14,12,P.gold);R(c,x-3,y+2,10,8,'#ffebc3');R(c,x-3,y+59,11,4,P.woodDark)}
function bench(c,x,y){R(c,x,y,63,8,P.wood);R(c,x+2,y+10,61,6,'#ab8559');R(c,x+4,y+16,4,13,P.woodDark);R(c,x+54,y+16,4,13,P.woodDark);R(c,x+3,y-5,4,18,P.woodDark);R(c,x+56,y-5,4,18,P.woodDark)}
function stall(c,x,y,color){
 shadow(c,x-5,y+72,97);R(c,x+3,y+14,4,58,P.woodDark);R(c,x+75,y+14,4,58,P.woodDark);R(c,x+2,y+34,78,32,'#b79462');R(c,x+8,y+38,66,24,'#d0b27e');R(c,x+2,y+31,80,7,P.woodDark);
 F(c,[[x-7,y+12],[x+7,y],[x+73,y],[x+90,y+12]],color);R(c,x-7,y+12,97,10,color);for(let i=0;i<6;i++)R(c,x-5+i*16,y+12,8,10,P.cream);R(c,x-7,y+21,97,3,'#385545');
 for(let i=0;i<10;i++){const px=x+10+i*6;R(c,px,y+25-(i%3)*2,5,6,['#dfb65d','#739c58','#bd7954'][i%3]);R(c,px+1,y+24-(i%3)*2,2,2,'#d3de90')}
 R(c,x+10,y+45,22,11,'#aa8054');R(c,x+13,y+47,16,2,'#e1c389');R(c,x+49,y+46,19,15,P.wood);R(c,x+52,y+48,13,2,P.sand);
}
function terrain(kind,choice){
 const canvas=document.createElement('canvas');canvas.width=W;canvas.height=H;const c=canvas.getContext('2d',{alpha:false});c.imageSmoothingEnabled=false;
 sky(c,kind==='inequality');ground(c);
 if(kind==='inequality'){
  tree(c,12,130,1.25);tree(c,566,130,1.1,true);house(c,68,145);house(c,480,145,'#dcd7b9');school(c,269,134);
  F(c,[[0,294],[102,282],[177,307],[286,291],[361,297],[426,281],[531,296],[640,278],[640,360],[0,360]],'#8fb0a1');
  road(c,[[110,233],[211,260],[319,225]],12);
  if(choice){road(c,[[522,233],[421,260],[334,225]],12);L(c,[[411,275],[520,246]],P.woodDark,3);for(let i=0;i<5;i++)R(c,421+i*20,257-i*5,3,18,P.wood);R(c,457,271,35,4,'#71958a')}
  else{L(c,[[522,238],[423,263],[334,228]],'#a3906e',13);for(let i=0;i<6;i++){R(c,360+i*28,247+(i%2)*12,18,4,'#77a699');R(c,356+i*27,253+(i%3)*8,22,2,'#a3c5b0')}}
  patch(c,'ÁREA A',72,116);patch(c,'ÁREA B',482,116);plant(c,32,298);plant(c,594,308);
 }else if(kind==='river'||kind==='quantitative'){
  tree(c,0,126,1.22,true);tree(c,176,122,.8);tree(c,581,126,1.1,true);house(c,66,126);school(c,482,120);road(c,[[143,211],[302,196],[481,211]],14);waterBase(c,246,114);pier(c,115,241);
  if(kind==='quantitative'||choice) pier(c,460,240);
  R(c,0,236,640,9,'#b7b485');R(c,2,237,107,2,'#d4cda3');R(c,539,237,101,2,'#d4cda3');plant(c,28,233);plant(c,599,234);
 }else if(kind==='lived'){
  F(c,[[56,242],[187,186],[457,186],[587,242],[606,359],[35,359]],'#d6caab');
  for(let i=0;i<7;i++)L(c,[[65-i*3,245+i*18],[572+i*3,245+i*18]],'#c1b493',1);
  for(let i=0;i<8;i++)L(c,[[190+i*39,199],[101+i*66,359]],'#e8ddbf',1);
  tree(c,60,138,1.4);tree(c,511,135,1.35);tree(c,160,152,.8);tree(c,448,159,.65);bench(c,287,209);streetLamp(c,130,180);streetLamp(c,492,180);
  R(c,210,177,212,8,'#759579');R(c,218,184,195,9,'#b4c19a');for(let i=0;i<10;i++)R(c,225+i*18,171,5,6,i%2?P.gold:'#bd7954');plant(c,44,325);plant(c,586,331);
 }else if(kind==='mediation'){
  school(c,421,117,1.45);tree(c,555,128,1.05,true);tree(c,23,133,.9);road(c,[[202,299],[367,282],[463,247]],17);
  R(c,63,135,205,130,P.woodDark);R(c,68,140,195,119,'#315c50');R(c,68,252,195,7,'#6f7050');R(c,82,265,6,32,P.woodDark);R(c,243,265,6,32,P.woodDark);R(c,228,249,19,3,'#efebd5');
  if(choice===0){label(c,'OBSERVAR',89,173,19,'#f1ead5');label(c,'O COTIDIANO',89,201,17,'#d4ddb9');L(c,[[90,220],[125,214],[156,224],[190,215],[232,218]],'#adccc0',3)}
  if(choice===1){label(c,'QUEM?',89,173,21,'#f1ead5');label(c,'ONDE? POR QUÊ?',89,204,17,'#d4ddb9');label(c,'?',221,240,29,P.gold)}
  if(choice===2){label(c,'REDES',88,168,17,'#f1ead5');label(c,'ACESSO',157,203,16,'#f1ead5');label(c,'CIRCULAÇÃO',88,233,15,'#d4ddb9');L(c,[[110,178],[170,185],[113,210]],P.gold,2)}
  if(choice===3){label(c,'RELACIONAR',87,173,19,'#f1ead5');label(c,'IDEIAS + FONTES',87,204,16,'#d4ddb9');L(c,[[102,224],[111,233],[135,215]],P.gold,4)}
  plant(c,26,308);plant(c,604,313);
 }else if(kind==='scale'){
  R(c,0,57,W,303,'#b5c9a0');F(c,[[0,244],[133,252],[261,206],[370,225],[496,174],[640,184],[640,218],[499,211],[369,252],[258,239],[130,282],[0,278]],'#6eaaa1');
  for(let i=0;i<45;i++)tree(c,(i*101)%630,83+(i*37)%239,.28+(i%3)*.08);
  if(choice===0){road(c,[[176,224],[307,207],[445,232]],19);house(c,96,151);school(c,434,164);house(c,277,111,'#e6d8b8');tree(c,334,235,.85,true);patch(c,'CASAS',96,127);patch(c,'ESCOLA',435,138)}
  else if(choice===1){road(c,[[92,142],[226,206],[359,154],[499,245]],11);road(c,[[226,206],[195,304],[349,278],[499,245]],11);for(const [x,y] of [[57,99],[186,157],[323,107],[461,197]]){c.save();c.translate(x,y);c.scale(.65,.65);house(c,0,0);c.restore()}school(c,310,234,.72);patch(c,'COMUNIDADES',25,70);patch(c,'SERVIÇOS',343,313)}
  else{const points=[[70,194],[226,120],[384,206],[555,131]];L(c,points,'#456f60',5);L(c,[[226,120],[264,301],[384,206]],'#456f60',4);for(let i=0;i<points.length;i++){const [x,y]=points[i];disk(c,x,y,24,'#edf1d7');disk(c,x,y,17,P.green);R(c,x-8,y-9,6,15,'#aac796');R(c,x+1,y-12,7,18,'#c9daab');patch(c,['Local','Cidade A','Cidade B','Mercado'][i],x-26,y+30,14)}patch(c,'Esquema de relações',19,316,14)}
 }else if(kind==='lenses'){
  R(c,0,197,W,66,'#d4c6a5');for(let i=0;i<24;i++)R(c,(i*83)%638,204+(i%4)*13,28,1,'#bbaa88');waterBase(c,266,94);tree(c,4,111,1.03,true);school(c,503,107,.76);
  for(let i=0;i<5;i++)stall(c,51+i*107,157,[P.roof,P.green,P.blue,'#b99856',P.roof][i]);pier(c,518,262);R(c,0,259,510,7,P.wood);for(let i=0;i<20;i++)R(c,i*26,259,2,7,'#c7ae83');plant(c,24,249);
 }
 return canvas;
}
const titles={inequality:['Uma chuva, duas condições','Infraestrutura e acesso'],river:['Condição não é destino','Condições + práticas sociais'],quantitative:['Distância e tempo','Distância e tempo'],lived:['Trabalho e rotina','Encontro e pertencimento','Memória e circulação'],mediation:['1 · Partir do relato','2 · Investigar a pergunta','3 · Mobilizar conceitos','4 · Construir explicações'],scale:['Na comunidade','No município','Na rede regional'],lenses:['Observar formas e usos','Medir e comparar fluxos','Investigar relações de poder','Ouvir experiências']};
function paint(c,kind,choice,t,background){
 c.setTransform(1,0,0,1,0,0);c.imageSmoothingEnabled=false;c.drawImage(background,0,0);
 if(kind==='inequality'){
  person(c,155+Math.sin(t*.55)*15,222,P.roof,t,{walk:true,seed:1});person(c,choice?411+Math.sin(t*.55)*15:443,228,P.blue,t,{walk:!!choice,seed:3});rain(c,t);
  if(choice)flow(c,[[528,283],[460,300],[387,296]],t,'#d4dcc0');
 }else if(kind==='river'||kind==='quantitative'){
  waves(c,t,253,90);boat(c,174+((t*(kind==='quantitative'?18:12))%222),276,t);person(c,155,202,P.roof,t,{seed:1});person(c,465,201,P.blue,t,{seed:3});
  if(kind==='quantitative'){
   if(choice===1){bus(c,168+(t*33)%236,175,t);flow(c,[[151,215],[301,200],[480,215]],t,P.gold)}else flow(c,[[150,309],[291,315],[487,309]],t,P.gold);
   patch(c,choice?'ESTRADA · 15 km / 25 min':'RIO · 8 km / 45 min',18,320,17);
  }else if(choice){person(c,474,219,P.green,t,{teacher:true,seed:2});flow(c,[[191,318],[298,320],[482,305]],t,P.gold);patch(c,'Técnicas · escolhas · organização',18,320,15)}else{patch(c,'Só o rio explica tudo?',225,140,17);patch(c,'Uma condição a investigar',18,320,15)}birds(c,t);
 }else if(kind==='lived'){
  for(let i=0;i<3;i++)person(c,[204,316,436][i],[233,242,234][i],[P.roof,P.green,P.blue][i],t,{selected:i===choice,seed:i,skin:i===1?'#9e714f':'#c99b72'});
  patch(c,['Organizo minha rotina','Sinto que pertenço','Lembro, mas preciso de acesso'][choice],choice===2?302:144+choice*83,choice===1?198:186,14);
  for(let i=0;i<3;i++)patch(c,String(i+1),[198,310,430][i],289,14);
  birds(c,t);
 }else if(kind==='mediation'){
  person(c,310,243,P.roof,t,{seed:1});person(c,350,255,P.green,t,{seed:2,skin:'#9e714f'});person(c,396,228,P.blue,t,{teacher:true,seed:3});
  for(let i=0;i<4;i++){R(c,205+i*58,323,45,6,i<=choice?P.green:'#d8d9b5');label(c,String(i+1),222+i*58,316,14,i<=choice?P.ink:'#7e9976')}
  if(choice===0)patch(c,'Como chegar à escola?',288,180,15);if(choice>=2)flow(c,[[295,230],[365,203],[442,210]],t,P.gold);birds(c,t);
 }else if(kind==='scale'){
  if(choice===0){person(c,269+Math.sin(t*.5)*37,204,P.roof,t,{walk:true});flow(c,[[186,238],[308,221],[438,244]],t,P.gold)}
  if(choice===1){flow(c,[[103,151],[229,211],[358,160],[501,250]],t,P.gold);flow(c,[[229,211],[199,306],[349,283]],t,P.gold)}
  if(choice===2){flow(c,[[70,194],[226,120],[384,206],[555,131]],t,P.gold);flow(c,[[226,120],[264,301],[384,206]],t,'#f0e5b9')}
 }else if(kind==='lenses'){
  waves(c,t,274,74);boat(c,41+(t*15)%371,289,t,true);
  for(let i=0;i<5;i++)person(c,76+i*107,216,[P.blue,P.roof,P.green][i%3],t,{seed:i,selected:choice===3&&i===2,skin:i%2?'#a57653':'#c3946b'});
  if(choice===0){for(let i=0;i<3;i++){const x=46+i*214;L(c,[[x,170],[x,152],[x+18,152]],P.gold,3);L(c,[[x+98,211],[x+98,228],[x+80,228]],P.gold,3)}}
  if(choice===1)flow(c,[[96,238],[285,240],[490,237],[548,291]],t,P.gold);
  if(choice===2){flow(c,[[113,148],[275,122],[482,147]],t,P.gold);patch(c,'TRABALHO',24,95,14);patch(c,'DECISÕES',258,95,14);patch(c,'ACESSO',505,95,14)}
  if(choice===3){patch(c,'Encontro',256,118,14);patch(c,'Memória',413,124,14)}birds(c,t);
 }
 // Titles remain short; the lesson's full explanation stays outside the canvas.
 patch(c,titles[kind][choice],16,17,18);
 if(['inequality','quantitative'].includes(kind))patch(c,'Hipotético',516,20,12,'#536557','#edf1dc');
}
window.GeoPixelScenes={width:W,height:H,terrain,paint};
})();
