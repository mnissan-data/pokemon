# -*- coding: utf-8 -*-
import base64, csv, io, json

DEX = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran ♀","Nidorina","Nidoqueen","Nidoran ♂","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
DEXNUM = {n:i+1 for i,n in enumerate(DEX)}
SETMETA = {"Base Set":("Base","base1","Base Set"),"Jungle":("Jungle","base2","Jungle"),"Fossil":("Fossil","base3","Fossil")}
SETORD = {"Base":0,"Jungle":1,"Fossil":2}

raw = base64.b64decode(open("sheet.b64").read()).decode("utf-8")
rows = list(csv.reader(io.StringIO(raw)))
header = rows[0]
print("columns:", header[:8], "...")

def edition_of(v):
    v=(v or "").strip().lower()
    if "1st" in v: return "1st Edition"
    if "shadowless" in v: return "Shadowless"
    return "Unlimited"

cards=[]
for r in rows[1:]:
    if len(r) < 13 or not r[4].strip():
        continue
    owned = r[0].strip().lower()=="yes"
    version=r[1]; price=r[2].strip(); cond=r[3].strip()
    num=int(r[4]); setname=r[5].strip()
    if setname not in SETMETA: continue
    setkey, apiid, label = SETMETA[setname]
    name=r[6].strip()
    el1=r[7].strip()
    rarity=r[12].strip()
    holo = (rarity=="Rare Holo")
    if rarity.startswith("Energy"): rarity="Energy"
    element = el1 if el1 else "Trainer"
    dex = DEXNUM.get(name)
    cards.append({
        "set":setkey,"setLabel":label,"num":num,"name":name,
        "element":element,"rarity":rarity,"holo":holo,"dex":dex,
        "img":"https://images.pokemontcg.io/%s/%d.png"%(apiid,num),
        "owned":owned,"edition":edition_of(version),
        "condition":cond or None,
        "pricePaid":(float(price) if price not in ("","",None) else None),
    })

cards.sort(key=lambda c:(SETORD[c["set"]], c["num"]))
assert len(cards)==228, len(cards)
own=[c for c in cards if c["owned"]]
print("cards",len(cards),"owned",len(own))
for sk in ["Base","Jungle","Fossil"]:
    a=[c for c in cards if c["set"]==sk]
    print(" ",sk,len(a),"owned",sum(c["owned"] for c in a))
print("holo cards:",sum(c["holo"] for c in cards),"| holo owned:",sum(c["holo"] and c["owned"] for c in cards))
poke=set(c["dex"] for c in cards if c["owned"] and c["dex"])
print("unique pokemon owned:",len(poke))
eds={}
for c in own: eds[c["edition"]]=eds.get(c["edition"],0)+1
print("editions owned:",eds)
spent=sum(c["pricePaid"] for c in own if c["pricePaid"] is not None)
print("total price paid: $%.2f"%spent)
json.dump(cards, open("cards.json","w"), ensure_ascii=False)
print("wrote cards.json")
