# Mély megerősítéses tanulás

A megerősítéses tanulás (RL) az egyik alapvető gépi tanulási paradigma, a felügyelt tanulás és a nem felügyelt tanulás mellett. Míg a felügyelt tanulás során ismert eredményekkel rendelkező adathalmazra támaszkodunk, az RL a **cselekvés általi tanuláson** alapul. Például, amikor először látunk egy számítógépes játékot, elkezdünk játszani, még akkor is, ha nem ismerjük a szabályokat, és hamarosan képesek vagyunk javítani a képességeinket pusztán a játék és a viselkedésünk módosítása révén.

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Az RL végrehajtásához szükségünk van:

* Egy **környezetre** vagy **szimulátorra**, amely meghatározza a játék szabályait. Képesnek kell lennünk kísérleteket futtatni a szimulátorban, és megfigyelni az eredményeket.
* Valamilyen **jutalomfüggvényre**, amely jelzi, mennyire volt sikeres a kísérletünk. Számítógépes játék tanulása esetén a jutalom a végső pontszámunk lenne.

A jutalomfüggvény alapján képesnek kell lennünk módosítani a viselkedésünket és javítani a képességeinket, hogy legközelebb jobban teljesítsünk. A fő különbség az RL és más gépi tanulási típusok között az, hogy az RL-ben általában nem tudjuk, hogy nyertünk vagy vesztettünk, amíg be nem fejezzük a játékot. Ezért nem mondhatjuk meg, hogy egy adott lépés önmagában jó-e vagy sem - csak a játék végén kapunk jutalmat.

Az RL során általában sok kísérletet hajtunk végre. Minden kísérlet során egyensúlyozni kell az eddig megtanult optimális stratégia követése (**kihasználás**) és az új lehetséges állapotok felfedezése (**felfedezés**) között.

## OpenAI Gym

Az RL-hez kiváló eszköz az [OpenAI Gym](https://gym.openai.com/) - egy **szimulációs környezet**, amely számos különböző környezetet képes szimulálni, az Atari játékoktól kezdve a fizikai egyensúlyozási problémákig. Ez az egyik legnépszerűbb szimulációs környezet a megerősítéses tanulási algoritmusok képzéséhez, és a [OpenAI](https://openai.com/) tartja karban.

> **Note**: Az OpenAI Gym összes elérhető környezetét [itt](https://gym.openai.com/envs/#classic_control) tekintheti meg.

## CartPole egyensúlyozás

Valószínűleg mindannyian láttatok már modern egyensúlyozó eszközöket, mint például a *Segway* vagy *Gyroscooter*. Ezek képesek automatikusan egyensúlyozni, azáltal hogy a kerekeiket az accelerométer vagy giroszkóp jeleire reagálva állítják be. Ebben a részben megtanuljuk, hogyan oldjunk meg egy hasonló problémát - egy rúd egyensúlyozását. Ez hasonló ahhoz a helyzethez, amikor egy cirkuszi előadó egy rudat egyensúlyoz a kezén - de ez az egyensúlyozás csak 1D-ben történik.

Az egyensúlyozás egyszerűsített változata **CartPole** problémaként ismert. A CartPole világban van egy vízszintes csúszka, amely balra vagy jobbra mozoghat, és a cél az, hogy egy függőleges rudat egyensúlyozzunk a csúszka tetején, miközben az mozog.

<img alt="egy cartpole" src="../../../../../translated_images/hu/cartpole.f52a67f27e058170.webp" width="200"/>

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
* `env.step` egy szimulációs lépést hajt végre. Egy **akciót** kap az **akciótérből**, és visszaad egy **megfigyelést** (a megfigyelési térből), valamint egy jutalmat és egy befejezési jelzőt.

A fenti példában minden lépésnél véletlenszerű akciót hajtunk végre, ezért a kísérlet élettartama nagyon rövid:

![nem egyensúlyozó cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Az RL algoritmus célja egy modell - az úgynevezett **policy** &pi; - képzése, amely az adott állapotnak megfelelő akciót ad vissza. A policy-t tekinthetjük valószínűségi modellnek is, például bármely állapot *s* és akció *a* esetén visszaadja a valószínűséget &pi;(*a*|*s*), hogy *a*-t kellene választanunk *s* állapotban.

## Policy Gradients algoritmus

A policy modellezésének legnyilvánvalóbb módja egy neurális hálózat létrehozása, amely bemenetként az állapotokat veszi, és visszaadja a megfelelő akciókat (pontosabban az összes akció valószínűségeit). Bizonyos értelemben ez hasonló lenne egy normál osztályozási feladathoz, egy jelentős különbséggel - előre nem tudjuk, hogy mely akciókat kellene végrehajtanunk az egyes lépésekben.

Az ötlet itt az, hogy becsüljük meg ezeket a valószínűségeket. Létrehozunk egy **kumulatív jutalmak** vektort, amely megmutatja a teljes jutalmunkat az egyes kísérleti lépések során. Emellett alkalmazunk **jutalom diszkontálást**, azaz a korábbi jutalmakat egy &gamma;=0.99 együtthatóval szorozzuk meg, hogy csökkentsük a korábbi jutalmak szerepét. Ezután megerősítjük azokat a lépéseket a kísérleti úton, amelyek nagyobb jutalmakat eredményeznek.

> Tudjon meg többet a Policy Gradient algoritmusról, és nézze meg működés közben a [példa notebookban](CartPole-RL-TF.ipynb).

## Actor-Critic algoritmus

A Policy Gradients megközelítés továbbfejlesztett változata az **Actor-Critic**. Az alapötlet az, hogy a neurális hálózatot két dolog visszaadására képezzük ki:

* A policy, amely meghatározza, hogy melyik akciót kell végrehajtani. Ezt a részt **actor**-nak nevezzük.
* Az összes jutalom becslése, amelyet az adott állapotban várhatunk - ezt a részt **critic**-nak nevezzük.

Bizonyos értelemben ez az architektúra hasonlít egy [GAN](../../4-ComputerVision/10-GANs/README.md)-ra, ahol két hálózatot egymás ellen képezünk ki. Az actor-critic modellben az actor javasolja az akciót, amelyet végre kell hajtanunk, míg a critic kritikus szerepet tölt be, és becsüli az eredményt. Azonban a célunk az, hogy ezeket a hálózatokat összhangban képezzük ki.

Mivel ismerjük mind a valós kumulatív jutalmakat, mind a critic által a kísérlet során visszaadott eredményeket, viszonylag könnyű olyan veszteségfüggvényt létrehozni, amely minimalizálja a kettő közötti különbséget. Ez adja a **critic veszteséget**. Az **actor veszteséget** ugyanazzal a megközelítéssel számíthatjuk ki, mint a Policy Gradient algoritmusban.

Egy ilyen algoritmus futtatása után elvárhatjuk, hogy a CartPole így viselkedjen:

![egyensúlyozó cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Gyakorlatok: Policy Gradients és Actor-Critic RL

Folytassa a tanulást az alábbi notebookokban:

* [RL TensorFlow-ban](CartPole-RL-TF.ipynb)
* [RL PyTorch-ban](CartPole-RL-PyTorch.ipynb)

## Egyéb RL feladatok

A megerősítéses tanulás napjainkban gyorsan növekvő kutatási terület. Néhány érdekes példa a megerősítéses tanulásra:

* Számítógép tanítása **Atari játékok** játszására. A kihívás ebben a problémában az, hogy nincs egyszerű állapot, amely vektorként van ábrázolva, hanem egy képernyőkép - és a CNN-t kell használni, hogy ezt a képernyőképet vektorrá alakítsuk, vagy hogy jutalominformációt nyerjünk ki. Az Atari játékok elérhetők a Gym-ben.
* Számítógép tanítása táblás játékok, például sakk és go játszására. Nemrégiben olyan csúcstechnológiás programokat, mint az **Alpha Zero**, két ügynök egymás elleni játékával képezték ki, amelyek minden lépésnél javultak.
* Az iparban az RL-t szimulációból származó vezérlőrendszerek létrehozására használják. Egy szolgáltatás, a [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste), kifejezetten erre lett tervezve.

## Összegzés

Most megtanultuk, hogyan képezzünk ki ügynököket, hogy jó eredményeket érjenek el pusztán azáltal, hogy egy jutalomfüggvényt biztosítunk számukra, amely meghatározza a játék kívánt állapotát, és lehetőséget adunk nekik az intelligens keresési tér felfedezésére. Sikeresen kipróbáltunk két algoritmust, és viszonylag rövid idő alatt jó eredményt értünk el. Ez azonban csak az RL-be való utazás kezdete, és érdemes lehet egy külön tanfolyamot elvégezni, ha mélyebben szeretne elmerülni benne.

## 🚀 Kihívás

Fedezze fel az 'Egyéb RL feladatok' szakaszban felsorolt alkalmazásokat, és próbáljon meg egyet megvalósítani!

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Áttekintés és önálló tanulás

Tudjon meg többet a klasszikus megerősítéses tanulásról a [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md) segítségével.

Nézze meg [ezt a remek videót](https://www.youtube.com/watch?v=qv6UVOQ0F44), amely arról szól, hogyan tanulhat meg egy számítógép Super Mario-t játszani.

## Feladat: [Train a Mountain Car](lab/README.md)

A feladat során az lenne a célja, hogy egy másik Gym környezetet - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/) - képezzen ki.

---

