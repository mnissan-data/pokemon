# -*- coding: utf-8 -*-
import json

DEX = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran♀","Nidorina","Nidoqueen","Nidoran♂","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
DEXNUM = {n:i+1 for i,n in enumerate(DEX)}

H=True; N=False
base = [
(1,"Alakazam","Psychic","Rare Holo",H),(2,"Blastoise","Water","Rare Holo",H),(3,"Chansey","Colorless","Rare Holo",H),
(4,"Charizard","Fire","Rare Holo",H),(5,"Clefairy","Colorless","Rare Holo",H),(6,"Gyarados","Water","Rare Holo",H),
(7,"Hitmonchan","Fighting","Rare Holo",H),(8,"Machamp","Fighting","Rare Holo",H),(9,"Magneton","Lightning","Rare Holo",H),
(10,"Mewtwo","Psychic","Rare Holo",H),(11,"Nidoking","Grass","Rare Holo",H),(12,"Ninetales","Fire","Rare Holo",H),
(13,"Poliwrath","Water","Rare Holo",H),(14,"Raichu","Lightning","Rare Holo",H),(15,"Venusaur","Grass","Rare Holo",H),
(16,"Zapdos","Lightning","Rare Holo",H),(17,"Beedrill","Grass","Rare",N),(18,"Dragonair","Colorless","Rare",N),
(19,"Dugtrio","Fighting","Rare",N),(20,"Electabuzz","Lightning","Rare",N),(21,"Electrode","Lightning","Rare",N),
(22,"Pidgeotto","Colorless","Rare",N),(23,"Arcanine","Fire","Uncommon",N),(24,"Charmeleon","Fire","Uncommon",N),
(25,"Dewgong","Water","Uncommon",N),(26,"Dratini","Colorless","Uncommon",N),(27,"Farfetch'd","Colorless","Uncommon",N),
(28,"Growlithe","Fire","Uncommon",N),(29,"Haunter","Psychic","Uncommon",N),(30,"Ivysaur","Grass","Uncommon",N),
(31,"Jynx","Psychic","Uncommon",N),(32,"Kadabra","Psychic","Uncommon",N),(33,"Kakuna","Grass","Uncommon",N),
(34,"Machoke","Fighting","Uncommon",N),(35,"Magikarp","Water","Uncommon",N),(36,"Magmar","Fire","Uncommon",N),
(37,"Nidorino","Grass","Uncommon",N),(38,"Poliwhirl","Water","Uncommon",N),(39,"Porygon","Colorless","Uncommon",N),
(40,"Raticate","Colorless","Uncommon",N),(41,"Seel","Water","Uncommon",N),(42,"Wartortle","Water","Uncommon",N),
(43,"Abra","Psychic","Common",N),(44,"Bulbasaur","Grass","Common",N),(45,"Caterpie","Grass","Common",N),
(46,"Charmander","Fire","Common",N),(47,"Diglett","Fighting","Common",N),(48,"Doduo","Colorless","Common",N),
(49,"Drowzee","Psychic","Common",N),(50,"Gastly","Psychic","Common",N),(51,"Koffing","Grass","Common",N),
(52,"Machop","Fighting","Common",N),(53,"Magnemite","Lightning","Common",N),(54,"Metapod","Grass","Common",N),
(55,"Nidoran♂","Grass","Common",N),(56,"Onix","Fighting","Common",N),(57,"Pidgey","Colorless","Common",N),
(58,"Pikachu","Lightning","Common",N),(59,"Poliwag","Water","Common",N),(60,"Ponyta","Fire","Common",N),
(61,"Rattata","Colorless","Common",N),(62,"Sandshrew","Fighting","Common",N),(63,"Squirtle","Water","Common",N),
(64,"Starmie","Water","Common",N),(65,"Staryu","Water","Common",N),(66,"Tangela","Grass","Common",N),
(67,"Voltorb","Lightning","Common",N),(68,"Vulpix","Fire","Common",N),(69,"Weedle","Grass","Common",N),
(70,"Clefairy Doll","Trainer","Rare",N),(71,"Computer Search","Trainer","Rare",N),(72,"Devolution Spray","Trainer","Rare",N),
(73,"Impostor Professor Oak","Trainer","Rare",N),(74,"Item Finder","Trainer","Rare",N),(75,"Lass","Trainer","Rare",N),
(76,"Pokémon Breeder","Trainer","Rare",N),(77,"Pokémon Trader","Trainer","Rare",N),(78,"Scoop Up","Trainer","Rare",N),
(79,"Super Energy Removal","Trainer","Rare",N),(80,"Defender","Trainer","Uncommon",N),(81,"Energy Retrieval","Trainer","Uncommon",N),
(82,"Full Heal","Trainer","Uncommon",N),(83,"Maintenance","Trainer","Uncommon",N),(84,"PlusPower","Trainer","Uncommon",N),
(85,"Pokémon Center","Trainer","Uncommon",N),(86,"Pokémon Flute","Trainer","Uncommon",N),(87,"Pokédex","Trainer","Uncommon",N),
(88,"Professor Oak","Trainer","Uncommon",N),(89,"Revive","Trainer","Uncommon",N),(90,"Super Potion","Trainer","Uncommon",N),
(91,"Bill","Trainer","Common",N),(92,"Energy Removal","Trainer","Common",N),(93,"Gust of Wind","Trainer","Common",N),
(94,"Potion","Trainer","Common",N),(95,"Switch","Trainer","Common",N),(96,"Double Colorless Energy","Colorless","Uncommon",N),
(97,"Fighting Energy","Fighting","Energy",N),(98,"Fire Energy","Fire","Energy",N),(99,"Grass Energy","Grass","Energy",N),
(100,"Lightning Energy","Lightning","Energy",N),(101,"Psychic Energy","Psychic","Energy",N),(102,"Water Energy","Water","Energy",N),
]
jungle = [
(1,"Clefable","Colorless","Rare Holo",H),(2,"Electrode","Lightning","Rare Holo",H),(3,"Flareon","Fire","Rare Holo",H),
(4,"Jolteon","Lightning","Rare Holo",H),(5,"Kangaskhan","Colorless","Rare Holo",H),(6,"Mr. Mime","Psychic","Rare Holo",H),
(7,"Nidoqueen","Grass","Rare Holo",H),(8,"Pidgeot","Colorless","Rare Holo",H),(9,"Pinsir","Grass","Rare Holo",H),
(10,"Scyther","Grass","Rare Holo",H),(11,"Snorlax","Colorless","Rare Holo",H),(12,"Vaporeon","Water","Rare Holo",H),
(13,"Venomoth","Grass","Rare Holo",H),(14,"Victreebel","Grass","Rare Holo",H),(15,"Vileplume","Grass","Rare Holo",H),
(16,"Wigglytuff","Colorless","Rare Holo",H),(17,"Clefable","Colorless","Rare",N),(18,"Electrode","Lightning","Rare",N),
(19,"Flareon","Fire","Rare",N),(20,"Jolteon","Lightning","Rare",N),(21,"Kangaskhan","Colorless","Rare",N),
(22,"Mr. Mime","Psychic","Rare",N),(23,"Nidoqueen","Grass","Rare",N),(24,"Pidgeot","Colorless","Rare",N),
(25,"Pinsir","Grass","Rare",N),(26,"Scyther","Grass","Rare",N),(27,"Snorlax","Colorless","Rare",N),
(28,"Vaporeon","Water","Rare",N),(29,"Venomoth","Grass","Rare",N),(30,"Victreebel","Grass","Rare",N),
(31,"Vileplume","Grass","Rare",N),(32,"Wigglytuff","Colorless","Rare",N),(33,"Butterfree","Grass","Uncommon",N),
(34,"Dodrio","Colorless","Uncommon",N),(35,"Exeggutor","Grass","Uncommon",N),(36,"Fearow","Colorless","Uncommon",N),
(37,"Gloom","Grass","Uncommon",N),(38,"Lickitung","Colorless","Uncommon",N),(39,"Marowak","Fighting","Uncommon",N),
(40,"Nidorina","Grass","Uncommon",N),(41,"Parasect","Grass","Uncommon",N),(42,"Persian","Colorless","Uncommon",N),
(43,"Primeape","Fighting","Uncommon",N),(44,"Rapidash","Fire","Uncommon",N),(45,"Rhydon","Fighting","Uncommon",N),
(46,"Seaking","Water","Uncommon",N),(47,"Tauros","Colorless","Uncommon",N),(48,"Weepinbell","Grass","Uncommon",N),
(49,"Bellsprout","Grass","Common",N),(50,"Cubone","Fighting","Common",N),(51,"Eevee","Colorless","Common",N),
(52,"Exeggcute","Grass","Common",N),(53,"Goldeen","Water","Common",N),(54,"Jigglypuff","Colorless","Common",N),
(55,"Mankey","Fighting","Common",N),(56,"Meowth","Colorless","Common",N),(57,"Nidoran♀","Grass","Common",N),
(58,"Oddish","Grass","Common",N),(59,"Paras","Grass","Common",N),(60,"Pikachu","Lightning","Common",N),
(61,"Rhyhorn","Fighting","Common",N),(62,"Spearow","Colorless","Common",N),(63,"Venonat","Grass","Common",N),
(64,"Poké Ball","Trainer","Common",N),
]
fossil = [
(1,"Aerodactyl","Fighting","Rare Holo",H),(2,"Articuno","Water","Rare Holo",H),(3,"Ditto","Colorless","Rare Holo",H),
(4,"Dragonite","Colorless","Rare Holo",H),(5,"Gengar","Psychic","Rare Holo",H),(6,"Haunter","Psychic","Rare Holo",H),
(7,"Hitmonlee","Fighting","Rare Holo",H),(8,"Hypno","Psychic","Rare Holo",H),(9,"Kabutops","Fighting","Rare Holo",H),
(10,"Lapras","Water","Rare Holo",H),(11,"Magneton","Lightning","Rare Holo",H),(12,"Moltres","Fire","Rare Holo",H),
(13,"Muk","Grass","Rare Holo",H),(14,"Raichu","Lightning","Rare Holo",H),(15,"Zapdos","Lightning","Rare Holo",H),
(16,"Aerodactyl","Fighting","Rare",N),(17,"Articuno","Water","Rare",N),(18,"Ditto","Colorless","Rare",N),
(19,"Dragonite","Colorless","Rare",N),(20,"Gengar","Psychic","Rare",N),(21,"Haunter","Psychic","Rare",N),
(22,"Hitmonlee","Fighting","Rare",N),(23,"Hypno","Psychic","Rare",N),(24,"Kabutops","Fighting","Rare",N),
(25,"Lapras","Water","Rare",N),(26,"Magneton","Lightning","Rare",N),(27,"Moltres","Fire","Rare",N),
(28,"Muk","Grass","Rare",N),(29,"Raichu","Lightning","Rare",N),(30,"Zapdos","Lightning","Rare",N),
(31,"Arbok","Grass","Uncommon",N),(32,"Cloyster","Water","Uncommon",N),(33,"Gastly","Psychic","Uncommon",N),
(34,"Golbat","Grass","Uncommon",N),(35,"Golduck","Water","Uncommon",N),(36,"Golem","Fighting","Uncommon",N),
(37,"Graveler","Fighting","Uncommon",N),(38,"Kingler","Water","Uncommon",N),(39,"Magmar","Fire","Uncommon",N),
(40,"Omastar","Water","Uncommon",N),(41,"Sandslash","Fighting","Uncommon",N),(42,"Seadra","Water","Uncommon",N),
(43,"Slowbro","Psychic","Uncommon",N),(44,"Tentacruel","Water","Uncommon",N),(45,"Weezing","Grass","Uncommon",N),
(46,"Ekans","Grass","Common",N),(47,"Geodude","Fighting","Common",N),(48,"Grimer","Grass","Common",N),
(49,"Horsea","Water","Common",N),(50,"Kabuto","Fighting","Common",N),(51,"Krabby","Water","Common",N),
(52,"Omanyte","Water","Common",N),(53,"Psyduck","Water","Common",N),(54,"Shellder","Water","Common",N),
(55,"Slowpoke","Psychic","Common",N),(56,"Tentacool","Water","Common",N),(57,"Zubat","Grass","Common",N),
(58,"Mr. Fuji","Trainer","Uncommon",N),(59,"Energy Search","Trainer","Common",N),(60,"Gambler","Trainer","Common",N),
(61,"Recycle","Trainer","Common",N),(62,"Mysterious Fossil","Trainer","Common",N),
]

owned = set()
for n in [4,7,8,16,26,27,28,29,30,31,32,33,34,35,36,37,38,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,61,62,63,64,65,67,68,69]:
    owned.add(("Base",n))
for n in [7,8,9,10,11,21,24,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,54,55,56,57]:
    owned.add(("Fossil",n))
for n in [2,5,10,12,14,25,31,34,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,60,61,62,63]:
    owned.add(("Jungle",n))

SETMETA = {"Base":("base1","Base Set"),"Jungle":("base2","Jungle"),"Fossil":("base3","Fossil")}
# The only 1st-edition cards owned; everything else is Unlimited (and not shadowless).
FIRST_ED = {("Base",8), ("Fossil",11)}
cards=[]
for setkey, rows in [("Base",base),("Jungle",jungle),("Fossil",fossil)]:
    apiid, label = SETMETA[setkey]
    for (num,name,el,rar,holo) in rows:
        cards.append({
            "set": setkey, "setLabel": label, "num": num, "name": name,
            "element": el, "rarity": rar, "holo": holo,
            "dex": DEXNUM.get(name),
            "img": "https://images.pokemontcg.io/%s/%d.png" % (apiid, num),
            "owned": (setkey, num) in owned,
            "edition": "1st Edition" if (setkey, num) in FIRST_ED else "Unlimited",
        })

assert len(cards)==228, len(cards)
assert sum(c["owned"] for c in cards)==111, sum(c["owned"] for c in cards)
print("cards", len(cards), "owned", sum(c["owned"] for c in cards))
for sk in ["Base","Jungle","Fossil"]:
    tot=[c for c in cards if c["set"]==sk]
    print(sk, len(tot), "owned", sum(c["owned"] for c in tot))
# unique pokemon owned (of 151)
poke_owned=set(c["dex"] for c in cards if c["owned"] and c["dex"])
print("unique pokemon owned", len(poke_owned))
with open("cards.json","w") as f:
    json.dump(cards,f,ensure_ascii=False)
print("wrote cards.json")
