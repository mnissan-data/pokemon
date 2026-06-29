# -*- coding: utf-8 -*-
import json, hashlib

cards = json.load(open("cards.json", encoding="utf-8"))

JP = {
"Bulbasaur":"フシギダネ","Ivysaur":"フシギソウ","Venusaur":"フシギバナ","Charmander":"ヒトカゲ","Charmeleon":"リザード",
"Charizard":"リザードン","Squirtle":"ゼニガメ","Wartortle":"カメール","Blastoise":"カメックス","Caterpie":"キャタピー",
"Metapod":"トランセル","Butterfree":"バタフリー","Weedle":"ビードル","Kakuna":"コクーン","Beedrill":"スピアー",
"Pidgey":"ポッポ","Pidgeotto":"ピジョン","Pidgeot":"ピジョット","Rattata":"コラッタ","Raticate":"ラッタ",
"Spearow":"オニスズメ","Fearow":"オニドリル","Ekans":"アーボ","Arbok":"アーボック","Pikachu":"ピカチュウ",
"Raichu":"ライチュウ","Sandshrew":"サンド","Sandslash":"サンドパン","Nidoran♀":"ニドラン♀","Nidorina":"ニドリーナ",
"Nidoqueen":"ニドクイン","Nidoran♂":"ニドラン♂","Nidorino":"ニドリーノ","Nidoking":"ニドキング","Clefairy":"ピッピ",
"Clefable":"ピクシー","Vulpix":"ロコン","Ninetales":"キュウコン","Jigglypuff":"プリン","Wigglytuff":"プクリン",
"Zubat":"ズバット","Golbat":"ゴルバット","Oddish":"ナゾノクサ","Gloom":"クサイハナ","Vileplume":"ラフレシア",
"Paras":"パラス","Parasect":"パラセクト","Venonat":"コンパン","Venomoth":"モルフォン","Diglett":"ディグダ",
"Dugtrio":"ダグトリオ","Meowth":"ニャース","Persian":"ペルシアン","Psyduck":"コダック","Golduck":"ゴルダック",
"Mankey":"マンキー","Primeape":"オコリザル","Growlithe":"ガーディ","Arcanine":"ウインディ","Poliwag":"ニョロモ",
"Poliwhirl":"ニョロゾ","Poliwrath":"ニョロボン","Abra":"ケーシィ","Kadabra":"ユンゲラー","Alakazam":"フーディン",
"Machop":"ワンリキー","Machoke":"ゴーリキー","Machamp":"カイリキー","Bellsprout":"マダツボミ","Weepinbell":"ウツドン",
"Victreebel":"ウツボット","Tentacool":"メノクラゲ","Tentacruel":"ドククラゲ","Geodude":"イシツブテ","Graveler":"ゴローン",
"Golem":"ゴローニャ","Ponyta":"ポニータ","Rapidash":"ギャロップ","Slowpoke":"ヤドン","Slowbro":"ヤドラン",
"Magnemite":"コイル","Magneton":"レアコイル","Farfetch'd":"カモネギ","Doduo":"ドードー","Dodrio":"ドードリオ",
"Seel":"パウワウ","Dewgong":"ジュゴン","Grimer":"ベトベター","Muk":"ベトベトン","Shellder":"シェルダー",
"Cloyster":"パルシェン","Gastly":"ゴース","Haunter":"ゴースト","Gengar":"ゲンガー","Onix":"イワーク",
"Drowzee":"スリープ","Hypno":"スリーパー","Krabby":"クラブ","Kingler":"キングラー","Voltorb":"ビリリダマ",
"Electrode":"マルマイン","Exeggcute":"タマタマ","Exeggutor":"ナッシー","Cubone":"カラカラ","Marowak":"ガラガラ",
"Hitmonlee":"サワムラー","Hitmonchan":"エビワラー","Lickitung":"ベロリンガ","Koffing":"ドガース","Weezing":"マタドガス",
"Rhyhorn":"サイホーン","Rhydon":"サイドン","Chansey":"ラッキー","Tangela":"モンジャラ","Kangaskhan":"ガルーラ",
"Horsea":"タッツー","Seadra":"シードラ","Goldeen":"トサキント","Seaking":"アズマオウ","Staryu":"ヒトデマン",
"Starmie":"スターミー","Mr. Mime":"バリヤード","Scyther":"ストライク","Jynx":"ルージュラ","Electabuzz":"エレブー",
"Magmar":"ブーバー","Pinsir":"カイロス","Tauros":"ケンタロス","Magikarp":"コイキング","Gyarados":"ギャラドス",
"Lapras":"ラプラス","Ditto":"メタモン","Eevee":"イーブイ","Vaporeon":"シャワーズ","Jolteon":"サンダース",
"Flareon":"ブースター","Porygon":"ポリゴン","Omanyte":"オムナイト","Omastar":"オムスター","Kabuto":"カブト",
"Kabutops":"カブトプス","Aerodactyl":"プテラ","Snorlax":"カビゴン","Articuno":"フリーザー","Zapdos":"サンダー",
"Moltres":"ファイヤー","Dratini":"ミニリュウ","Dragonair":"ハクリュー","Dragonite":"カイリュー","Mewtwo":"ミュウツー",
}

# marquee market values (illustrative, raw near-mint USD)
MARQUEE = {("Base",4):330,("Base",2):150,("Base",15):130,("Base",10):95,("Base",1):70,("Base",6):60,
("Base",16):75,("Base",3):55,("Base",12):45,("Base",11):55,("Base",9):40,("Base",7):45,("Base",8):60,
("Base",13):40,("Base",14):42,("Base",5):42,("Fossil",5):70,("Fossil",1):55,("Fossil",2):45,("Fossil",4):60,
("Jungle",10):40,("Jungle",12):38,("Jungle",11):55,("Jungle",9):35,("Jungle",5):30}

def price_for(c):
    key=(c["set"],c["num"])
    if key in MARQUEE: base=MARQUEE[key]
    else:
        r=c["rarity"]; h=hashlib.md5((c["set"]+str(c["num"])).encode()).hexdigest()
        n=int(h[:4],16)/65535.0
        if c["holo"]: base=25+n*70
        elif r=="Rare": base=8+n*22
        elif r=="Uncommon": base=2.5+n*6
        elif r=="Common": base=1+n*3
        elif r=="Energy": base=1+n*2
        else: base=1.5+n*6   # trainers
    return round(base,2)

for c in cards:
    c["price"]=price_for(c)
    c["jp"]=JP.get(c["name"], c["name"])
    # printing premiums (demo): unlimited = market, shadowless ~2.2x, 1st edition ~4x (only meaningful for vintage)
    c["printings"]={"Unlimited":c["price"],"Shadowless":round(c["price"]*2.2,2),"1st Edition":round(c["price"]*4,2)}

DATA=json.dumps(cards, ensure_ascii=False)
total_val=round(sum(c["price"] for c in cards if c["owned"]),2)
print("cards",len(cards),"owned value(demo) $",total_val)

HTML = open("explore_template.html", encoding="utf-8").read()
HTML = HTML.replace("__DATA__", DATA)
open("pokemon_explore.html","w",encoding="utf-8").write(HTML)
print("wrote pokemon_explore.html", len(HTML), "bytes")
