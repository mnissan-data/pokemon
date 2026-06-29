# -*- coding: utf-8 -*-
import json
cards = json.load(open("cards.json", encoding="utf-8"))
DATA = json.dumps(cards, ensure_ascii=False)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Pokémon Binder — Base · Jungle · Fossil</title>
<style>
:root{
  /* Official Pokémon brand palette */
  --pk-yellow:#FFCB05; --pk-yellow-d:#E6B800; --pk-gold2:#C7960A;
  --pk-blue:#2A75BB; --pk-blue-l:#3D7DCA; --pk-navy:#003A70; --pk-navy-d:#00264a;
  --pk-red:#EE1515; --pk-red-d:#CC0000;
  --red:var(--pk-red); --red2:var(--pk-red-d); --blue:var(--pk-blue); --gold:var(--pk-yellow); --gold2:var(--pk-yellow-d);
  --ink:#16243a; --paper:#f3f7ff; --line:#dbe5f3;
  /* Pokémon TCG energy-type colors */
  --grass:#4FA64B; --fire:#E84B2E; --water:#3A8FE0; --lightning:#F2C20E;
  --psychic:#8E4FB0; --fighting:#C77B33; --colorless:#B7B49E; --trainer:#C0567E; --energy:#8A95A2;
  /* ghost-binder purple */
  --pk-purple:#5b3c93; --pk-purple-d:#3a2566; --pk-purple-l:#8a63c6;
}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  color:var(--ink);background:
    radial-gradient(1100px 460px at 50% -180px, #ffcb0526, transparent),
    radial-gradient(900px 500px at 100% 0%, #2a75bb14, transparent),
    linear-gradient(180deg,#eaf2ff 0%, #f3f7ff 340px, #f3f7ff 100%);}
header.app{position:relative;padding:40px 20px 34px;text-align:center;color:#fff;overflow:hidden;
  border-bottom:7px solid var(--pk-yellow);box-shadow:0 8px 26px #2a1a4a55;
  background:
    radial-gradient(circle at 12% 22%, #9c7bd6 0 7%, transparent 8%),
    radial-gradient(circle at 84% 30%, #7a55b8 0 6%, transparent 7%),
    radial-gradient(circle at 68% 78%, #4d2f86 0 9%, transparent 10%),
    radial-gradient(circle at 30% 82%, #6e49ad 0 6%, transparent 7%),
    radial-gradient(circle at 50% 10%, #9c7bd633 0 24%, transparent 25%),
    radial-gradient(circle at 92% 88%, #3a2566 0 18%, transparent 19%),
    radial-gradient(900px 380px at 50% -120px, #b79be0aa, transparent),
    linear-gradient(160deg, var(--pk-purple) 0%, var(--pk-purple-d) 100%);}
/* ghost trio artwork */
header.app .ghosts{position:absolute;inset:0;pointer-events:none}
header.app .ghosts img{position:absolute;filter:drop-shadow(0 8px 14px #1a0e3380)}
header.app .ghosts .gengar{right:2%;bottom:-26px;height:190px;transform:rotate(4deg)}
header.app .ghosts .haunter{left:1%;bottom:-30px;height:150px;opacity:.92;transform:rotate(-6deg)}
header.app .ghosts .gastly{left:16%;top:-24px;height:96px;opacity:.5;transform:rotate(8deg)}
@media(max-width:760px){header.app .ghosts .gastly,header.app .ghosts .haunter{display:none}
  header.app .ghosts .gengar{height:120px;right:-2%}}
/* classic Pokemon logo lockup */
header.app .logo{position:relative;z-index:3}
header.app .logoimg{max-height:104px;max-width:88%;object-fit:contain;background:#fff;border-radius:16px;
  padding:8px 16px;box-shadow:0 6px 18px #0000004d;border:1px solid #ffffff66}
header.app h1{margin:0;font-family:"Arial Black","Arial Rounded MT Bold",Arial,sans-serif;
  font-size:clamp(40px,7vw,68px);font-weight:900;letter-spacing:1px;line-height:1;
  color:var(--pk-yellow);
  -webkit-text-stroke:4px #2a5cc0;paint-order:stroke fill;
  text-shadow:0 5px 0 #1c3f8f, 0 7px 0 #16306e, 0 10px 12px #00000066;}
header.app .banner{position:relative;z-index:3;display:inline-block;margin-top:14px;
  background:var(--pk-red);color:#fff;font-weight:800;letter-spacing:4px;font-size:14px;
  text-transform:uppercase;padding:7px 20px;border-radius:6px;border:2.5px solid #fff;
  box-shadow:0 4px 10px #00000055, inset 0 -3px 0 #00000022}
header.app .sub{position:relative;z-index:3;margin-top:14px;font-size:12px;opacity:.95;letter-spacing:3px;
  text-transform:uppercase;font-weight:700;color:#f3ecff}
header.app .catch{position:relative;z-index:3;margin-top:4px;font-size:12px;color:#ffe27a;font-style:italic;font-weight:700;letter-spacing:.5px}
.wrap{max-width:1180px;margin:0 auto;padding:18px 16px 80px}

/* metrics */
.hero{display:grid;grid-template-columns:1.1fr 2fr;gap:16px;margin:18px 0 8px}
@media(max-width:760px){.hero{grid-template-columns:1fr}}
.card-panel{background:#fff;border:1px solid var(--line);border-radius:18px;
  box-shadow:0 8px 24px #2336500f;padding:18px}
.big{display:flex;align-items:center;gap:18px}
.ring{--p:0;width:128px;height:128px;border-radius:50%;flex:0 0 auto;display:grid;place-items:center;
  background:conic-gradient(#111418 calc(var(--p)*1%), #e7ecf5 0);}
.ring .inner{width:100px;height:100px;border-radius:50%;background:#fff;display:grid;place-items:center;
  box-shadow:inset 0 0 0 1px var(--line)}
.ring .pct{font-size:30px;font-weight:800;line-height:1}
.ring .pl{font-size:10px;letter-spacing:1.5px;color:#7a8194;text-transform:uppercase;margin-top:3px}
.big .meta h2{margin:0 0 4px;font-size:17px}
.big .meta p{margin:2px 0;color:#5a6377;font-size:13px}
.big .meta b{color:var(--ink)}
.statgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
@media(max-width:520px){.statgrid{grid-template-columns:repeat(2,1fr)}}
.stat{background:linear-gradient(180deg,#ffffff,#fbfcff);border:1px solid var(--line);
  border-radius:14px;padding:11px 12px}
.stat .k{font-size:11px;text-transform:uppercase;letter-spacing:.6px;color:#7a8194;display:flex;justify-content:space-between}
.stat .v{font-size:20px;font-weight:800;margin:3px 0 7px}
.bar{height:8px;border-radius:6px;background:#e7ecf5;overflow:hidden}
/* default = Venusaur green (rarities: holo/rare/uncommon/common) */
.bar>span{display:block;height:100%;border-radius:6px;background:linear-gradient(90deg,#3E8E45,#6FC36A)}
.stat.holo .bar>span{background:linear-gradient(90deg,#3E8E45,#6FC36A)}
/* sets = booster-pack colors: Base=Charizard orange-red, Jungle=green, Fossil=purple */
.stat.base .bar>span{background:linear-gradient(90deg,#C8401A,#F26B2A)}
.stat.jungle .bar>span{background:linear-gradient(90deg,#15692F,#2E8B4E)}
.stat.fossil .bar>span{background:linear-gradient(90deg,#5B3E8E,#8A6BC0)}
/* totals (Pokémon /151 + Overall) = red, kept as-is */
.stat.tot .bar>span{background:linear-gradient(90deg,var(--pk-red-d),#ff4d4d)}
.stat.base .k span:last-child{color:#C8401A}
.stat.jungle .k span:last-child{color:#15692F}
.stat.fossil .k span:last-child{color:#6A4FA0}
.stat.tot{background:linear-gradient(180deg,#fff,#fff7f7);border-color:#f6d9d9}
.stat.tot .k span:last-child{color:var(--pk-red-d)}
.stat .sm{font-size:11px;color:#8a91a3;margin-top:5px}

/* controls */
.controls{display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between;
  position:sticky;top:0;z-index:30;background:#f4f6fbe6;backdrop-filter:blur(8px);
  padding:12px 6px;border-bottom:1px solid var(--line);margin-top:14px;border-radius:0 0 12px 12px}
.seg{display:flex;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;box-shadow:0 2px 8px #2336500a}
.seg button{border:0;background:transparent;padding:9px 13px;font-size:13px;font-weight:600;color:#5a6377;cursor:pointer;white-space:nowrap}
.seg button.on{background:var(--pk-blue);color:#fff}
.seg button.on[data-filt="have"]{background:#1f9d4d}
.seg button.on[data-filt="need"]{background:var(--pk-red)}
.seg .lbl{padding:9px 10px;font-size:11px;color:#9aa1b2;text-transform:uppercase;letter-spacing:1px;border-right:1px solid var(--line);display:flex;align-items:center}
.search{flex:1;min-width:160px;max-width:280px}
.search input{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:12px;font-size:14px;background:#fff}
.tinybtn{border:1px solid var(--line);background:#fff;border-radius:10px;padding:9px 12px;font-size:12px;font-weight:600;color:#5a6377;cursor:pointer}

/* binder */
.bindertitle{display:flex;align-items:center;gap:12px;margin:26px 4px 8px}
.bindertitle h3{margin:0;font-size:18px}
.bindertitle .chip{font-size:11px;font-weight:700;padding:3px 9px;border-radius:20px;background:#fff;border:1px solid var(--line);color:#5a6377}
.famnote{background:#fff;border:1px solid var(--line);border-left:4px solid var(--pk-purple-l);border-radius:12px;
  padding:11px 14px;margin:18px 4px 2px;font-size:12.5px;color:#5a6377;line-height:1.5;box-shadow:0 4px 12px #2336500a}
.page{background:linear-gradient(180deg,#ffffff,#f7f8fc);border:1px solid var(--line);border-radius:16px;
  padding:16px;margin:12px 0;box-shadow:0 10px 26px #2336500d;position:relative}
.page .pgnum{position:absolute;top:10px;right:14px;font-size:11px;color:#aeb4c4;font-weight:700;letter-spacing:1px}
.grid9{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
@media(max-width:560px){.grid9{gap:9px}}
.slot{position:relative;border-radius:12px;aspect-ratio:.715;cursor:pointer;
  background:#eef1f7;border:1px dashed #cfd5e3;overflow:hidden;transition:transform .12s, box-shadow .12s}
.slot:hover{transform:translateY(-3px);box-shadow:0 10px 20px #23365022}
.slot img{width:100%;height:100%;object-fit:contain;display:block;background:#fff}
.slot .ph{position:absolute;inset:0;display:none;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:8px;
  background:radial-gradient(circle at 50% 30%, #fff, #eef1f7);}
.slot.noimg .ph{display:flex}
.slot.noimg img{display:none}
.slot .ph .n{font-size:12px;font-weight:800;line-height:1.1}
.slot .ph .num{font-size:10px;color:#8a91a3;margin-top:3px}
.slot.need{filter:grayscale(.92) brightness(.97);opacity:.5}
.slot.need:hover{opacity:.78;filter:grayscale(.4)}
.slot .badge{position:absolute;top:6px;left:6px;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;
  font-size:12px;font-weight:900;color:#fff;box-shadow:0 2px 6px #00000033;z-index:2}
.slot.have .badge{background:#21b35a}
.slot.need .badge{background:#9aa1b2}
.slot .tag{position:absolute;bottom:0;left:0;right:0;font-size:9.5px;font-weight:700;color:#fff;
  padding:3px 6px;display:flex;justify-content:space-between;gap:4px;
  background:linear-gradient(180deg,transparent,#000000cc);z-index:2;letter-spacing:.3px}
.slot .holopip{position:absolute;top:6px;right:6px;font-size:9px;font-weight:800;color:#3b2d00;
  background:linear-gradient(135deg,#fff3a8,#ffd23f);padding:2px 6px;border-radius:10px;z-index:2;box-shadow:0 1px 4px #00000033}
.slot .firsted{position:absolute;top:6px;right:6px;font-size:8.5px;font-weight:900;color:#fff;letter-spacing:.3px;
  background:linear-gradient(135deg,#003a70,#2a75bb);padding:2px 6px;border-radius:10px;z-index:3;box-shadow:0 1px 4px #00000040;border:1px solid #ffffff66}
.slot.have.holo .firsted{top:28px}
.eldot{width:8px;height:8px;border-radius:50%;display:inline-block}
.empty{opacity:.35;border-style:dashed;cursor:default;background:repeating-linear-gradient(45deg,#f0f2f8,#f0f2f8 8px,#e9ecf4 8px,#e9ecf4 16px)}
.empty:hover{transform:none;box-shadow:none}
.slot.blank{background:transparent;border:none;cursor:default}
.slot.blank:hover{transform:none;box-shadow:none}
.foot{text-align:center;color:#9aa1b2;font-size:12px;margin-top:30px}
.legend{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin:6px 0 0;color:#7a8194;font-size:12px}
.legend span{display:inline-flex;align-items:center;gap:6px}
.swatch{width:13px;height:13px;border-radius:4px;display:inline-block;border:1px solid #0001}
.toast{position:fixed;bottom:18px;left:50%;transform:translateX(-50%) translateY(20px);opacity:0;
  background:#1b1f2a;color:#fff;padding:10px 16px;border-radius:12px;font-size:13px;font-weight:600;
  box-shadow:0 8px 24px #0004;transition:.25s;z-index:50;pointer-events:none}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

/* ---------- Mobile ---------- */
@media(max-width:640px){
  header.app{padding:22px 12px 20px;border-bottom-width:5px}
  header.app .logoimg{max-height:74px;padding:6px 12px}
  header.app .banner{font-size:12px;letter-spacing:2.5px;padding:6px 14px}
  header.app .sub{font-size:10px;letter-spacing:1.5px;margin-top:10px}
  header.app .catch{font-size:11px}
  header.app .ghosts .gengar{height:96px;right:-4%;bottom:-14px;opacity:.85}
  .wrap{padding:12px 9px 64px}
  .hero{gap:11px;margin:12px 0 4px}
  .card-panel{padding:13px;border-radius:14px}
  .big{gap:13px}
  .ring{width:100px;height:100px}
  .ring .inner{width:78px;height:78px}
  .ring .pct{font-size:23px}
  .big .meta h2{font-size:15px}
  .big .meta p{font-size:12px}
  .statgrid{grid-template-columns:repeat(2,1fr);gap:8px}
  .stat{padding:9px 10px}
  .stat .v{font-size:18px}
  .controls{flex-direction:column;align-items:stretch;gap:8px;padding:9px 4px;top:0}
  .seg{overflow-x:auto;max-width:100%;scrollbar-width:none}
  .seg::-webkit-scrollbar{display:none}
  .seg button{padding:9px 11px;font-size:12.5px}
  .seg .lbl{position:sticky;left:0;background:#fff;z-index:1}
  .search{max-width:100%}
  .tinybtn{align-self:flex-start}
  .legend{gap:9px 12px;font-size:11px}
  .bindertitle{margin:18px 2px 6px}
  .bindertitle h3{font-size:14px}
  .famnote{font-size:11.5px;padding:10px 12px}
  .grid9{gap:7px}
  .page{padding:9px;border-radius:12px}
  .page .pgnum{font-size:10px;top:7px;right:9px}
  .slot .tag{font-size:8.5px;padding:2px 4px}
  .slot .holopip{font-size:8px;padding:2px 5px}
}
@media(max-width:380px){
  .statgrid{grid-template-columns:repeat(2,1fr)}
  .big{flex-wrap:wrap;justify-content:center;text-align:center}
  .big .meta{width:100%}
}
</style>
</head>
<body>
<header class="app">
  <div class="ghosts">
    <img class="gastly" src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/92.png" alt="" onerror="this.style.display='none'"/>
    <img class="haunter" src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/93.png" alt="" onerror="this.style.display='none'"/>
    <img class="gengar" src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png" alt="" onerror="this.style.display='none'"/>
  </div>
  <div class="logo">
    <img id="logoImg" class="logoimg" src="pokemon_logo.png" alt="Pokémon"
         onerror="this.remove();var w=document.getElementById('logoWord');if(w)w.hidden=false;"/>
    <h1 id="logoWord" hidden>Pokémon</h1>
  </div>
  <div class="banner">Binder Tracker</div>
  <div class="sub">Base · Jungle · Fossil — Master Collection</div>
  <div class="catch">Gotta catch 'em all!</div>
</header>

<div class="wrap">
  <div class="hero">
    <div class="card-panel">
      <div class="big">
        <div class="ring" id="ring"><div class="inner"><div style="text-align:center">
          <div class="pct" id="ringPct">0%</div><div class="pl">Collected</div></div></div></div>
        <div class="meta">
          <h2 id="ownedLine">0 / 228 cards</h2>
          <p><b id="pokeLine">0</b> of 151 original Pokémon</p>
          <p id="needLine"><b>0</b> cards still needed</p>
          <p id="edLine" style="font-size:12px;color:#7a8aa0;margin-top:6px"></p>
        </div>
      </div>
    </div>
    <div class="card-panel">
      <div class="statgrid" id="statgrid"></div>
    </div>
  </div>

  <div class="controls">
    <div class="seg" id="sortSeg">
      <div class="lbl">Sort</div>
      <button data-sort="color" class="on">Type / Color</button>
      <button data-sort="dex">National Dex</button>
      <button data-sort="set">Set + #</button>
      <button data-sort="rarity">Rarity</button>
      <button data-sort="family">Evo Family</button>
      <button data-sort="familyv">Evo Vertical</button>
    </div>
    <div class="seg" id="filtSeg">
      <div class="lbl">Show</div>
      <button data-filt="all" class="on">All</button>
      <button data-filt="have">Owned</button>
      <button data-filt="need">Needed</button>
    </div>
    <div class="search"><input id="q" placeholder="Search a Pokémon…" /></div>
    <button class="tinybtn" id="resetBtn" title="Reset to your spreadsheet data">↺ Reset</button>
  </div>

  <div class="legend" id="legend"></div>

  <div id="binder"></div>
  <div class="foot">Card images © Pokémon / Wizards of the Coast, served via pokemontcg.io · Your checkmarks save automatically in this browser.</div>
</div>
<div class="toast" id="toast"></div>

<script>
const CARDS = __DATA__;
const ELCOLOR = {Fire:'var(--fire)',Water:'var(--water)',Grass:'var(--grass)',Lightning:'var(--lightning)',
  Psychic:'var(--psychic)',Fighting:'var(--fighting)',Colorless:'var(--colorless)',Trainer:'var(--trainer)',Energy:'var(--energy)'};
const COLOR_ORDER = ['Fire','Water','Grass','Lightning','Psychic','Fighting','Colorless','Trainer','Energy'];
// Pokémon TCG energy-style icons: colored disc + white glyph, recolored to the type palette
function typeBadge(el,px){
  const color=ELCOLOR[el]||'#9aa1b2';
  const G={
    Fire:`<path fill="#fff" d="M16 4c-3 6 4 8 1 13a5 5 0 1 1-7-1c-2 5 2 8 6 8 5 0 8-4 8-8 0-5-5-8-8-12z"/><path style="fill:${color}" d="M16 17c-2 2.5-3 4.5-1.6 6.4a3 3 0 0 0 4.8-.4c1-1.8 0-3.8-3.2-6z"/>`,
    Water:`<path fill="#fff" d="M16 5c0 0 9 10 9 15a9 9 0 1 1-18 0c0-5 9-15 9-15z"/><path fill="${color}" opacity=".22" d="M12 17a4 6 0 0 0 4 7c-3 0-5-2-5-5 0-1 .4-1.6 1-2z"/>`,
    Grass:`<path fill="#fff" d="M26 6C12 7 6 15 8 27c12-1 19-9 18-21z"/><path d="M12 24C16 18 20 13 23 9" stroke="${color}" stroke-width="1.7" fill="none" stroke-linecap="round"/>`,
    Lightning:`<polygon fill="#fff" points="18,3 7,18 14,18 13,29 25,12 17,12"/>`,
    Psychic:`<path fill="#fff" d="M4 16C9 9 23 9 28 16 23 23 9 23 4 16z"/><circle cx="16" cy="16" r="4.4" style="fill:${color}"/><circle cx="16" cy="16" r="1.7" fill="#fff"/>`,
    Fighting:`<rect x="9" y="11" width="14.5" height="13" rx="3" fill="#fff"/><rect x="12.4" y="11" width="1.5" height="7" rx=".7" style="fill:${color}"/><rect x="15.8" y="10.7" width="1.5" height="7.3" rx=".7" style="fill:${color}"/><rect x="19.2" y="11" width="1.5" height="7" rx=".7" style="fill:${color}"/><rect x="9.6" y="17.2" width="13.3" height="1.5" rx=".7" style="fill:${color}"/><rect x="5.4" y="17.2" width="5.4" height="4.6" rx="2.3" fill="#fff" transform="rotate(-20 8 19.5)"/>`,
    Colorless:`<path fill="#fff" d="M16 3c1 8 5 12 13 13-8 1-12 5-13 13-1-8-5-12-13-13 8-1 12-5 13-13z"/>`,
    Trainer:`<rect x="9" y="7" width="14" height="18" rx="2.5" fill="#fff"/><rect x="11.6" y="11" width="8.8" height="2" rx="1" style="fill:${color}"/><rect x="11.6" y="15" width="8.8" height="2" rx="1" style="fill:${color}"/><rect x="11.6" y="19" width="6" height="2" rx="1" style="fill:${color}"/>`,
    Energy:`<text x="16" y="22" text-anchor="middle" font-size="17" font-weight="900" fill="#fff" font-family="Arial,Helvetica,sans-serif">E</text>`
  };
  const g=G[el]||`<circle cx="16" cy="16" r="6" fill="#fff"/>`;
  return `<svg class="tib" width="${px}" height="${px}" viewBox="0 0 32 32" style="vertical-align:middle" aria-label="${el}">`+
    `<circle cx="16" cy="16" r="15" style="fill:${color}"/><circle cx="16" cy="16" r="15" fill="none" stroke="#0003" stroke-width="1"/>${g}</svg>`;
}
const RAR_ORDER = ['Rare Holo','Rare','Uncommon','Common','Energy'];
const KEY='pkmn-binder-v1';

// load saved overrides
let saved={};
try{saved=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){saved={}}
CARDS.forEach(c=>{c.id=c.set+'-'+c.num; if(c.id in saved){c.owned=!!saved[c.id];}});

let sortMode='color', filt='all', query='';

function persist(){localStorage.setItem(KEY, JSON.stringify(saved));}
function pct(a,b){return b? Math.round(a/b*100):0;}

function metrics(){
  const tot=CARDS.length, own=CARDS.filter(c=>c.owned).length;
  const bySet=s=>CARDS.filter(c=>c.set===s);
  const setStat=s=>{const a=bySet(s);return {o:a.filter(c=>c.owned).length,t:a.length};};
  const rar=r=>{const a=CARDS.filter(c=>c.rarity===r||(r==='Rare Holo'&&c.holo));return {o:a.filter(c=>c.owned).length,t:a.length};};
  const holo=CARDS.filter(c=>c.holo); const holoStat={o:holo.filter(c=>c.owned).length,t:holo.length};
  const rare=CARDS.filter(c=>c.rarity==='Rare'); const rareStat={o:rare.filter(c=>c.owned).length,t:rare.length};
  const unc=CARDS.filter(c=>c.rarity==='Uncommon'); const uncStat={o:unc.filter(c=>c.owned).length,t:unc.length};
  const com=CARDS.filter(c=>c.rarity==='Common'); const comStat={o:com.filter(c=>c.owned).length,t:com.length};
  const poke=new Set(CARDS.filter(c=>c.owned&&c.dex).map(c=>c.dex));
  return {tot,own,base:setStat('Base'),jungle:setStat('Jungle'),fossil:setStat('Fossil'),
    holo:holoStat,rare:rareStat,unc:uncStat,com:comStat,poke:poke.size};
}

function renderMetrics(){
  const m=metrics(); const p=pct(m.own,m.tot);
  document.getElementById('ring').style.setProperty('--p',p);
  document.getElementById('ringPct').textContent=p+'%';
  document.getElementById('ownedLine').textContent=m.own+' / '+m.tot+' cards';
  document.getElementById('pokeLine').textContent=m.poke;
  document.getElementById('needLine').innerHTML='<b>'+(m.tot-m.own)+'</b> cards still needed';
  const eds={};CARDS.filter(c=>c.owned&&c.edition).forEach(c=>{eds[c.edition]=(eds[c.edition]||0)+1;});
  const edParts=Object.entries(eds).sort((a,b)=>b[1]-a[1]).map(([k,v])=>v+' '+k);
  const spent=CARDS.filter(c=>c.owned&&c.pricePaid).reduce((s,c)=>s+c.pricePaid,0);
  document.getElementById('edLine').innerHTML=(edParts.join(' &middot; ')||'Unlimited')+
    (spent?(' &nbsp;·&nbsp; <b style="color:#15692F">$'+Math.round(spent).toLocaleString()+'</b> paid'):'');
  const cell=(cls,k,s)=>`<div class="stat ${cls}"><div class="k"><span>${k}</span><span>${pct(s.o,s.t)}%</span></div>
    <div class="v">${s.o}<span style="font-size:13px;color:#9aa1b2;font-weight:600">/${s.t}</span></div>
    <div class="bar"><span style="width:${pct(s.o,s.t)}%"></span></div></div>`;
  document.getElementById('statgrid').innerHTML=
    cell('base','Base Set',m.base)+cell('jungle','Jungle',m.jungle)+cell('fossil','Fossil',m.fossil)+
    cell('holo','Rare Holos',m.holo)+cell('','Rare',m.rare)+cell('','Uncommon',m.unc)+
    cell('','Common',m.com)+cell('tot','Pokémon /151',{o:m.poke,t:151})+
    cell('tot','Overall',{o:m.own,t:m.tot});
}

function sortCards(arr){
  const a=arr.slice();
  if(sortMode==='set'){
    const so={Base:0,Jungle:1,Fossil:2};
    a.sort((x,y)=>so[x.set]-so[y.set]||x.num-y.num);
  }else if(sortMode==='dex'){
    a.sort((x,y)=>{const dx=x.dex||999,dy=y.dex||999;return dx-dy||x.num-y.num||(x.holo?-1:1);});
  }else if(sortMode==='rarity'){
    const ro=r=>{const i=RAR_ORDER.indexOf(r);return i<0?9:i;};
    a.sort((x,y)=>{const rx=x.holo?0:ro(x.rarity),ry=y.holo?0:ro(y.rarity);
      return rx-ry||(x.dex||999)-(y.dex||999)||x.num-y.num;});
  }else{ // color
    const co=e=>{const i=COLOR_ORDER.indexOf(e);return i<0?9:i;};
    a.sort((x,y)=>co(x.element)-co(y.element)||(x.dex||999)-(y.dex||999)||x.num-y.num);
  }
  return a;
}

function pageLabel(c){
  if(sortMode==='set')return c.setLabel;
  if(sortMode==='color')return c.element;
  if(sortMode==='rarity')return c.holo?'Rare Holo':c.rarity;
  return null;
}

function filteredPool(){
  return CARDS.filter(c=>{
    if(filt==='have'&&!c.owned)return false;
    if(filt==='need'&&c.owned)return false;
    if(query){const q=query.toLowerCase();
      if(!(c.name.toLowerCase().includes(q)||c.setLabel.toLowerCase().includes(q)||String(c.num)===q))return false;}
    return true;
  });
}
function visible(){ return sortCards(filteredPool()); }

/* ---- Evolution Family layout ---- */
// Gen-1 evolution lines present in Base/Jungle/Fossil. Birds + Eeveelutions are special groups.
const FAMILIES=[
 [1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20],[21,22],[23,24],[25,26],[27,28],
 [29,30,31],[32,33,34],[35,36],[37,38],[39,40],[41,42],[43,44,45],[46,47],[48,49],[50,51],[52,53],
 [54,55],[56,57],[58,59],[60,61,62],[63,64,65],[66,67,68],[69,70,71],[72,73],[74,75,76],[77,78],
 [79,80],[81,82],[83],[84,85],[86,87],[88,89],[90,91],[92,93,94],[95],[96,97],[98,99],[100,101],
 [102,103],[104,105],[106],[107],[108],[109,110],[111,112],[113],[114],[115],[116,117],[118,119],
 [120,121],[122],[123],[124],[125],[126],[127],[128],[129,130],[131],[132],[134,135,136],[133],[137],
 [138,139],[140,141],[142],[143],[144,145,146],[147,148,149],[150]
];
const NAMEBYDEX={}; CARDS.forEach(c=>{if(c.dex&&!NAMEBYDEX[c.dex])NAMEBYDEX[c.dex]=c.name;});
const SETORD={Base:0,Jungle:1,Fossil:2};

function famLabel(fam){
  if(fam.includes(144))return 'Legendary Birds';
  if(fam.includes(133))return 'Eevee &amp; Eeveelutions';
  if(fam.length>1)return (NAMEBYDEX[fam[0]]||'?')+' line';
  return NAMEBYDEX[fam[0]]||'?';
}
function familyLayout(pool){
  const byDex={}; pool.forEach(c=>{if(c.dex){(byDex[c.dex]=byDex[c.dex]||[]).push(c);}});
  // one card per Pokémon: the holo if it exists (so the holo sits IN the evolution-line row),
  // otherwise the non-holo. Every other version (non-holo twins, extra prints) goes to Duplicates.
  function pick(dex){
    const cs=(byDex[dex]||[]).slice().sort((a,b)=>SETORD[a.set]-SETORD[b.set]||a.num-b.num);
    const holos=cs.filter(c=>c.holo), non=cs.filter(c=>!c.holo);
    const primary=holos[0]||non[0]||null;
    const extras=cs.filter(c=>c!==primary);
    return {primary,extras};
  }
  let groups=FAMILIES.map(fam=>{
    const members=fam.filter(d=>byDex[d]&&byDex[d].length);
    return {fam,members,size:members.length,base:fam[0]};
  }).filter(g=>g.size>0);
  groups.sort((a,b)=>b.size-a.size||a.base-b.base);

  // 3-member lines are exactly 3 cards -> they tile into perfectly full rows.
  // Pairs + singles are packed densely right after (no blank pockets).
  const trios=[]; const rest=[]; const misc=[];
  for(const g of groups){
    const picks=g.members.map(d=>pick(d));
    picks.forEach(p=>p.extras.forEach(e=>misc.push(e)));
    const cells=picks.map(p=>p.primary).filter(Boolean); // evolution line, one per Pokémon
    if(g.size>=3){ for(const c of cells)trios.push(c); }
    else { for(const c of cells)rest.push(c); }
  }
  const mainCells=trios.concat(rest);
  const te=pool.filter(c=>!c.dex).sort((a,b)=>SETORD[a.set]-SETORD[b.set]||a.num-b.num);
  misc.sort((a,b)=>(b.holo?1:0)-(a.holo?1:0)||(a.dex||999)-(b.dex||999)||SETORD[a.set]-SETORD[b.set]||a.num-b.num);
  return {mainCells,te,misc};
}

function imgFallback(el){
  if(!el.dataset.tried){el.dataset.tried='1';el.src=el.dataset.lo;}
  else{el.closest('.slot').classList.add('noimg');}
}
function slotHTML(c){
  const cls=(c.owned?'have':'need')+(c.holo?' holo':'');
  const dot=typeBadge(c.element,13);
  return `<div class="slot ${cls}" data-id="${c.id}" title="${c.name} · ${c.setLabel} #${c.num} · Unlimited">
    <div class="badge">${c.owned?'✓':''}</div>
    ${c.holo?'<div class="holopip">HOLO</div>':''}
    <img loading="lazy" src="${c.img.replace('.png','_hires.png')}" data-lo="${c.img}" alt="${c.name}"
      onerror="imgFallback(this)"/>
    <div class="ph"><div class="n">${c.name}</div><div class="num">${c.setLabel} · #${c.num}</div></div>
    <div class="tag"><span>${dot} ${c.name}</span><span>#${c.num}</span></div>
  </div>`;
}

let _pageNo=0;
// render a flat list of cards into 9-up pages (with optional swatch header)
function pagesFromList(list,opts){
  opts=opts||{}; let html='';
  if(opts.label){
    const sw=opts.icon?opts.icon:(opts.color?`<span style="width:14px;height:14px;border-radius:4px;background:${opts.color};display:inline-block;box-shadow:0 1px 3px #0002"></span>`:'');
    const real=list.filter(c=>c);
    html+=`<div class="bindertitle">${sw}<h3>${opts.label}</h3>`+
      (opts.chip!==false?`<span class="chip">${real.filter(c=>c.owned).length}/${real.length}</span>`:'')+`</div>`;
  }
  for(let i=0;i<list.length;i+=9){
    _pageNo++; const slice=list.slice(i,i+9);
    let cells=slice.map(c=>c?slotHTML(c):'<div class="slot blank"></div>').join('');
    html+=`<div class="page"><div class="pgnum">PAGE ${_pageNo}</div><div class="grid9">${cells}</div></div>`;
  }
  return html;
}

function renderFamilyHTML(){
  const {mainCells,te,misc}=familyLayout(filteredPool());
  let html='';
  if(mainCells.length||te.length||misc.length){
    html+=`<div class="famnote">Pokédex order, grouped by evolution family — full 3-stage lines first, then pairs and single-stage Pokémon. One card per Pokémon with the <b>holo shown in its evolution-line row</b>; non-holo twins and extra prints are collected under <b>Duplicates &amp; Variants</b>.</div>`;
  }
  if(mainCells.length){ html+=pagesFromList(mainCells,{label:'Pokémon — by evolution family (Pokédex order)'}); }
  if(te.length){ html+=pagesFromList(te,{label:'Trainers &amp; Energy'}); }
  if(misc.length){ html+=pagesFromList(misc,{label:'Duplicates &amp; Variants'}); }
  if(!html)html='<div class="page"><p style="text-align:center;color:#9aa1b2;padding:30px">No cards match.</p></div>';
  return html;
}

// ---- Vertical evolution layout: each evolution line is a COLUMN (base on top) ----
function familyVerticalLayout(pool){
  const byDex={}; pool.forEach(c=>{if(c.dex){(byDex[c.dex]=byDex[c.dex]||[]).push(c);}});
  function pick(dex){
    const cs=(byDex[dex]||[]).slice().sort((a,b)=>SETORD[a.set]-SETORD[b.set]||a.num-b.num);
    const holos=cs.filter(c=>c.holo), non=cs.filter(c=>!c.holo);
    const primary=holos[0]||non[0]||null;
    return {primary,extras:cs.filter(c=>c!==primary)};
  }
  let groups=FAMILIES.map(fam=>{
    const members=fam.filter(d=>byDex[d]&&byDex[d].length);
    return {members,size:members.length,base:fam[0]};
  }).filter(g=>g.size>0);
  groups.sort((a,b)=>b.size-a.size||a.base-b.base);

  const fams3=[]; const fams2=[]; const singles=[]; const misc=[];
  for(const g of groups){
    const picks=g.members.map(d=>pick(d));
    picks.forEach(p=>p.extras.forEach(e=>misc.push(e)));
    const line=picks.map(p=>p.primary).filter(Boolean); // one card per Pokémon, base→final
    if(line.length>=3)fams3.push(line);
    else if(line.length===2)fams2.push(line);
    else if(line.length===1)singles.push(line[0]);
  }
  const CO=el=>{const i=COLOR_ORDER.indexOf(el);return i<0?99:i;};
  // 3-stage lines first (Pokédex order) — each a full vertical column of 3
  const blocks3=[];
  for(let i=0;i<fams3.length;i+=3){
    const chunk=fams3.slice(i,i+3); const cells=[];
    for(let s=0;s<3;s++){ for(let j=0;j<3;j++){ cells.push(j<chunk.length?(chunk[j][s]||null):null); } }
    blocks3.push(cells);
  }
  // --- everything after the Dragonite page: group by colour ---
  // two-stage lines as vertical pairs, with a colour-matched single filling the bottom of each column
  fams2.sort((a,b)=>CO(a[0].element)-CO(b[0].element)||(a[0].dex||0)-(b[0].dex||0));
  singles.sort((a,b)=>CO(a.element)-CO(b.element)||(a.dex||0)-(b.dex||0));
  let singleQ=singles.slice();
  const columns=[]; // each = [top, mid, bottom]
  for(const pr of fams2){
    let idx=singleQ.findIndex(s=>s.element===pr[0].element);
    if(idx<0&&singleQ.length)idx=0;
    const s=idx>=0?singleQ.splice(idx,1)[0]:null;
    columns.push([pr[0],pr[1],s]);
  }
  for(let i=0;i<singleQ.length;i+=3){ columns.push([singleQ[i]||null,singleQ[i+1]||null,singleQ[i+2]||null]); }
  const postBlocks=[];
  for(let i=0;i<columns.length;i+=3){
    const ch=columns.slice(i,i+3); const cells=[];
    for(let r=0;r<3;r++){ for(let j=0;j<3;j++){ cells.push(j<ch.length?(ch[j][r]||null):null); } }
    postBlocks.push(cells);
  }
  // trainers/energy + duplicates also grouped by colour
  const te=pool.filter(c=>!c.dex).sort((a,b)=>CO(a.element)-CO(b.element)||SETORD[a.set]-SETORD[b.set]||a.num-b.num);
  misc.sort((a,b)=>CO(a.element)-CO(b.element)||(a.dex||999)-(b.dex||999)||SETORD[a.set]-SETORD[b.set]||a.num-b.num);
  return {blocks3,postBlocks,te,misc};
}
function pageBlock(cells){
  _pageNo++;
  const inner=cells.map(c=>c?slotHTML(c):'<div class="slot blank"></div>').join('');
  return `<div class="page"><div class="pgnum">PAGE ${_pageNo}</div><div class="grid9">${inner}</div></div>`;
}
function renderFamilyVHTML(){
  const {blocks3,postBlocks,te,misc}=familyVerticalLayout(filteredPool());
  let html='';
  if(blocks3.length||postBlocks.length||te.length||misc.length){
    html+=`<div class="famnote">Vertical evolution chart — each <b>column is one evolution line</b>, base on top and the holo final stage at the bottom. After the 3-stage lines (ending with Dratini → Dragonite), the rest is <b>grouped by colour/type</b>: two-stage lines sit as vertical pairs with a single filling the bottom of each column.</div>`;
  }
  if(blocks3.length){
    html+=`<div class="bindertitle"><h3>Evolution lines — 3 stages (vertical · Pokédex order)</h3></div>`;
    blocks3.forEach(b=>html+=pageBlock(b));
  }
  if(postBlocks.length){
    html+=`<div class="bindertitle"><h3>Two-stage lines &amp; singles (by colour)</h3></div>`;
    postBlocks.forEach(b=>html+=pageBlock(b));
  }
  if(te.length){ html+=pagesFromList(te,{label:'Trainers &amp; Energy (by colour)'}); }
  if(misc.length){ html+=pagesFromList(misc,{label:'Duplicates &amp; Variants (by colour)'}); }
  if(!html)html='<div class="page"><p style="text-align:center;color:#9aa1b2;padding:30px">No cards match.</p></div>';
  return html;
}

function render(){
  const binder=document.getElementById('binder');
  _pageNo=0;
  let html='';
  if(sortMode==='family'){
    html=renderFamilyHTML();
  }else if(sortMode==='familyv'){
    html=renderFamilyVHTML();
  }else{
    const arr=visible();
    if(!arr.length){binder.innerHTML='<div class="page"><p style="text-align:center;color:#9aa1b2;padding:30px">No cards match.</p></div>';return;}
    let groups=[];
    if(pageLabel(arr[0])!==null){
      const map=new Map();
      arr.forEach(c=>{const k=pageLabel(c);if(!map.has(k))map.set(k,[]);map.get(k).push(c);});
      groups=[...map.entries()];
    }else{ groups=[[null,arr]]; }
    for(const [label,list] of groups){
      let hopts={};
      if(label!==null){ hopts = (sortMode==='color') ? {label,icon:typeBadge(label,20)} : {label,color:(ELCOLOR[label]||'var(--gold2)')}; }
      html+=pagesFromList(list,hopts);
    }
  }
  binder.innerHTML=html;
  binder.querySelectorAll('.slot[data-id]').forEach(el=>{
    el.addEventListener('click',()=>toggle(el.dataset.id));
  });
}

let toastTimer;
function toast(msg){const t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');
  clearTimeout(toastTimer);toastTimer=setTimeout(()=>t.classList.remove('show'),1400);}

function toggle(id){
  const c=CARDS.find(x=>x.id===id);if(!c)return;
  c.owned=!c.owned; saved[id]=c.owned; persist();
  renderMetrics(); render();
  toast(c.owned?('✓ Added '+c.name):('Removed '+c.name));
}

// controls
document.getElementById('sortSeg').addEventListener('click',e=>{
  const b=e.target.closest('button[data-sort]');if(!b)return;
  sortMode=b.dataset.sort;[...e.currentTarget.querySelectorAll('button')].forEach(x=>x.classList.toggle('on',x===b));render();
});
document.getElementById('filtSeg').addEventListener('click',e=>{
  const b=e.target.closest('button[data-filt]');if(!b)return;
  filt=b.dataset.filt;[...e.currentTarget.querySelectorAll('button')].forEach(x=>x.classList.toggle('on',x===b));render();
});
document.getElementById('q').addEventListener('input',e=>{query=e.target.value.trim();render();});
document.getElementById('resetBtn').addEventListener('click',()=>{
  if(!confirm('Reset all checkmarks back to your original spreadsheet data?'))return;
  saved={};localStorage.removeItem(KEY);
  CARDS.forEach(c=>c.owned=c.orig);renderMetrics();render();toast('Reset to spreadsheet');
});

// keep original for reset
CARDS.forEach(c=>{c.orig = (c.id in saved)? undefined : c.owned;});
// recompute orig properly from data baseline:
(function(){const baseline={};CARDS.forEach(c=>{});})();

// legend with TCG energy icons
(function(){
  const types=['Fire','Water','Grass','Lightning','Psychic','Fighting','Colorless','Trainer'];
  document.getElementById('legend').innerHTML =
    types.map(t=>`<span>${typeBadge(t,18)} ${t}</span>`).join('')+
    '<span style="color:#9aa1b2">· tap a card to toggle owned</span>';
})();

renderMetrics();render();
</script>
</body>
</html>"""

# Fix the "orig" baseline: we need the original owned (from spreadsheet) before applying saved overrides.
# Simplest: inject an ORIG map of id->owned from the source data.
ORIG = {f"{c['set']}-{c['num']}": c['owned'] for c in cards}
HTML = HTML.replace("CARDS.forEach(c=>{c.orig = (c.id in saved)? undefined : c.owned;});\n// recompute orig properly from data baseline:\n(function(){const baseline={};CARDS.forEach(c=>{});})();",
                    "const ORIG=__ORIG__;\nCARDS.forEach(c=>{c.orig=!!ORIG[c.id];});")
HTML = HTML.replace("__DATA__", DATA).replace("__ORIG__", json.dumps(ORIG))

with open("pokemon_binder.html","w",encoding="utf-8") as f:
    f.write(HTML)
print("wrote pokemon_binder.html", len(HTML), "bytes")
