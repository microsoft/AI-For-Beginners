<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dbacf9b1915612981d76059678e563e5",
  "translation_date": "2025-08-25T23:29:53+00:00",
  "source_file": "lessons/6-Other/22-DeepRL/README.md",
  "language_code": "hu"
}
-->
# Mély megerősítéses tanulás

A megerősítéses tanulás (RL) az egyik alapvető gépi tanulási paradigma, a felügyelt tanulás és a nem felügyelt tanulás mellett. Míg a felügyelt tanulásnál ismert kimenetekkel rendelkező adathalmazra támaszkodunk, az RL a **cselekvés általi tanuláson** alapul. Például, amikor először látunk egy számítógépes játékot, elkezdünk játszani, még akkor is, ha nem ismerjük a szabályokat, és hamarosan képesek vagyunk javítani a képességeinken pusztán azáltal, hogy játszunk és alkalmazkodunk a viselkedésünkhöz.

## [Előadás előtti kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

Az RL végrehajtásához szükségünk van:

* Egy **környezetre** vagy **szimulátorra**, amely meghatározza a játék szabályait. Képesnek kell lennünk kísérleteket futtatni a szimulátorban, és megfigyelni az eredményeket.
* Valamilyen **jutalomfüggvényre**, amely jelzi, mennyire volt sikeres a kísérletünk. Számítógépes játék tanulása esetén a jutalom a végső pontszámunk lenne.

A jutalomfüggvény alapján képesnek kell lennünk módosítani a viselkedésünket és javítani a képességeinken, hogy legközelebb jobban teljesítsünk. A fő különbség az RL és más gépi tanulási típusok között az, hogy az RL-ben általában nem tudjuk, hogy nyertünk-e vagy vesztettünk-e, amíg be nem fejezzük a játékot. Ezért nem mondhatjuk meg, hogy egy adott lépés önmagában jó-e vagy sem - csak a játék végén kapunk jutalmat.

Az RL során általában sok kísérletet hajtunk végre. Minden kísérlet során egyensúlyozni kell az eddig tanult optimális stratégia követése (**kihasználás**) és az új lehetséges állapotok felfedezése (**felfedezés**) között.

## OpenAI Gym

Az RL-hez nagyszerű eszköz az [OpenAI Gym](https://gym.openai.com/) - egy **szimulációs környezet**, amely számos különböző környezetet képes szimulálni, az Atari játékoktól kezdve a fizikai egyensúlyozási problémákig. Ez az egyik legnépszerűbb szimulációs környezet a megerősítéses tanulási algoritmusok képzéséhez, és a [OpenAI](https://openai.com/) tartja karban.

> **Note**: Az OpenAI Gym összes elérhető környezetét [itt](https://gym.openai.com/envs/#classic_control) tekintheti meg.

## CartPole egyensúlyozás

Valószínűleg mindannyian láttatok már modern egyensúlyozó eszközöket, mint például a *Segway* vagy *Gyroscooter*. Ezek képesek automatikusan egyensúlyozni, azáltal, hogy a kerekeiket az accelerométer vagy giroszkóp jeleire reagálva állítják be. Ebben a részben megtanuljuk, hogyan oldjunk meg egy hasonló problémát - egy rúd egyensúlyozását. Ez hasonló ahhoz a helyzethez, amikor egy cirkuszi előadó egy rudat próbál egyensúlyozni a kezén - de ez az egyensúlyozás csak 1D-ben történik.

Az egyensúlyozás egyszerűsített változata **CartPole** problémaként ismert. A CartPole világban van egy vízszintes csúszka, amely balra vagy jobbra mozoghat, és a cél az, hogy egy függőleges rudat egyensúlyozzunk a csúszka tetején, miközben az mozog.

<img alt="egy cartpole" src="images/cartpole.png" width="200"/>

Ennek a környezetnek a létrehozásához és használatához néhány Python kódsorra van szükség:

```python
import gym
env = gym.make("CartPole-v1")

env.reset()
done = False
total_reward = 0
while not done:
   env.render()
   action = env.action_space.sample()
   observaton, reward, done, info = env.step(action)
   total_reward += reward

print(f"Total reward: {total_reward}")
```

Minden környezet pontosan ugyanúgy érhető el:
* `env.reset` új kísérletet indít
* `env.step` szimulációs lépést hajt végre. Egy **akciót** kap az **akciótérből**, és visszaad egy **megfigyelést** (a megfigyelési térből), valamint egy jutalmat és egy befejezési jelzőt.

A fenti példában minden lépésnél véletlenszerű akciót hajtunk végre, ezért a kísérlet élettartama nagyon rövid:

![nem egyensúlyozó cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Az RL algoritmus célja egy modell - az úgynevezett **politika** π - képzése, amely az adott állapothoz tartozó akciót adja vissza. A politikát tekinthetjük valószínűségi modellnek is, például bármely állapot *s* és akció *a* esetén visszaadja a valószínűséget π(*a*|*s*), hogy az *s* állapotban az *a* akciót kellene végrehajtanunk.

## Policy Gradients algoritmus

A politika modellezésének legnyilvánvalóbb módja egy neurális hálózat létrehozása, amely bemenetként az állapotokat kapja, és visszaadja a megfelelő akciókat (pontosabban az összes akció valószínűségeit). Bizonyos értelemben ez hasonló lenne egy normál osztályozási feladathoz, egy jelentős különbséggel - előre nem tudjuk, hogy mely akciókat kellene végrehajtanunk az egyes lépésekben.

Az ötlet itt az, hogy becsüljük meg ezeket a valószínűségeket. Létrehozunk egy **kumulatív jutalmak** vektort, amely megmutatja a kísérlet minden lépésénél elért teljes jutalmat. Emellett alkalmazunk **jutalom diszkontálást**, azaz a korábbi jutalmakat egy γ=0.99 együtthatóval szorozzuk meg, hogy csökkentsük a korábbi jutalmak szerepét. Ezután megerősítjük azokat a lépéseket a kísérleti útvonal mentén, amelyek nagyobb jutalmakat eredményeznek.

> Tudjon meg többet a Policy Gradient algoritmusról, és nézze meg működés közben a [példa notebookban](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb).

## Actor-Critic algoritmus

A Policy Gradients megközelítés továbbfejlesztett változata az **Actor-Critic**. A mögöttes fő ötlet az, hogy a neurális hálózatot két dolog visszaadására képezzük:

* A politika, amely meghatározza, hogy melyik akciót kell végrehajtani. Ezt a részt **színésznek** (actor) nevezzük.
* Az állapotban várható teljes jutalom becslése - ezt a részt **kritikusnak** (critic) nevezzük.

Bizonyos értelemben ez az architektúra hasonlít egy [GAN](../../4-ComputerVision/10-GANs/README.md)-ra, ahol két hálózatot egymás ellen képezünk. Az actor-critic modellben a színész javasolja a végrehajtandó akciót, míg a kritikus megpróbál kritikus lenni, és megbecsülni az eredményt. Azonban a célunk az, hogy ezeket a hálózatokat összhangban képezzük.

Mivel ismerjük mind a valós kumulatív jutalmakat, mind a kritikus által a kísérlet során visszaadott eredményeket, viszonylag könnyű olyan veszteségfüggvényt létrehozni, amely minimalizálja a kettő közötti különbséget. Ez adja a **kritikus veszteséget**. Az **színész veszteséget** ugyanazzal a megközelítéssel számíthatjuk ki, mint a Policy Gradient algoritmusban.

Egy ilyen algoritmus futtatása után elvárhatjuk, hogy a CartPole így viselkedjen:

![egyensúlyozó cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Gyakorlatok: Policy Gradients és Actor-Critic RL

Folytassa a tanulást az alábbi notebookokban:

* [RL TensorFlow-ban](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [RL PyTorch-ban](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Egyéb RL feladatok

A megerősítéses tanulás manapság gyorsan növekvő kutatási terület. Néhány érdekes példa a megerősítéses tanulásra:

* Számítógép tanítása **Atari játékok** játszására. Ennek a problémának a kihívása, hogy nem egyszerű állapotot kapunk vektorként, hanem egy képernyőképet - és CNN-t kell használnunk, hogy ezt a képernyőképet vektorrá alakítsuk, vagy hogy jutalominformációt nyerjünk ki. Az Atari játékok elérhetők a Gym-ben.
* Számítógép tanítása táblás játékok, például sakk és go játszására. A legújabb csúcstechnológiás programok, mint például **Alpha Zero**, két ügynök egymás elleni játékával, és minden lépésnél való fejlődéssel lettek kiképezve.
* Az iparban az RL-t szimulációból származó vezérlőrendszerek létrehozására használják. Egy [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) nevű szolgáltatás kifejezetten erre lett tervezve.

## Összegzés

Most megtanultuk, hogyan képezzünk ügynököket, hogy jó eredményeket érjenek el pusztán azáltal, hogy egy jutalomfüggvényt biztosítunk nekik, amely meghatározza a játék kívánt állapotát, és lehetőséget adunk nekik az intelligens keresési tér felfedezésére. Sikeresen kipróbáltunk két algoritmust, és viszonylag rövid idő alatt jó eredményt értünk el. Ez azonban csak a kezdete az RL-be való utazásának, és mindenképpen érdemes egy külön tanfolyamot elvégezni, ha mélyebben szeretne belemerülni.

## 🚀 Kihívás

Fedezze fel az 'Egyéb RL feladatok' szakaszban felsorolt alkalmazásokat, és próbáljon meg egyet megvalósítani!

## [Előadás utáni kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Áttekintés és önálló tanulás

Tudjon meg többet a klasszikus megerősítéses tanulásról a [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md) segítségével.

Nézze meg [ezt a nagyszerű videót](https://www.youtube.com/watch?v=qv6UVOQ0F44), amely arról szól, hogyan tanulhat meg egy számítógép Super Mario-t játszani.

## Feladat: [Train a Mountain Car](lab/README.md)

A feladat során az lenne a célja, hogy egy másik Gym környezetet - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/) - képezzen ki.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.