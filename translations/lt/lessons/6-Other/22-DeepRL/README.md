<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dbacf9b1915612981d76059678e563e5",
  "translation_date": "2025-08-31T17:32:45+00:00",
  "source_file": "lessons/6-Other/22-DeepRL/README.md",
  "language_code": "lt"
}
-->
# Giliojo stiprinamojo mokymosi pagrindai

Stiprinamasis mokymasis (angl. Reinforcement Learning, RL) laikomas vienu iš pagrindinių mašininio mokymosi paradigmų, greta prižiūrimojo mokymosi (supervised learning) ir neprižiūrimojo mokymosi (unsupervised learning). Prižiūrimajame mokymesi remiamės duomenų rinkiniu su žinomais rezultatais, o RL pagrįstas **mokymusi per veiksmą**. Pavyzdžiui, kai pirmą kartą matome kompiuterinį žaidimą, pradedame jį žaisti net nežinodami taisyklių, ir netrukus galime pagerinti savo įgūdžius tiesiog žaisdami ir koreguodami savo elgesį.

## [Prieš paskaitą: testas](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Norint atlikti RL, mums reikia:

* **Aplinkos** arba **simuliatoriaus**, kuris nustato žaidimo taisykles. Turėtume turėti galimybę atlikti eksperimentus simuliatoriuje ir stebėti rezultatus.
* **Atlygio funkcijos**, kuri nurodo, kaip sėkmingai atliktas mūsų eksperimentas. Pavyzdžiui, mokantis žaisti kompiuterinį žaidimą, atlygis būtų mūsų galutinis rezultatas.

Remdamiesi atlygio funkcija, turėtume sugebėti koreguoti savo elgesį ir tobulinti įgūdžius, kad kitą kartą pasirodytume geriau. Pagrindinis skirtumas tarp kitų mašininio mokymosi tipų ir RL yra tas, kad RL atveju dažniausiai nežinome, ar laimėjome, ar pralaimėjome, kol nebaigiame žaidimo. Todėl negalime pasakyti, ar tam tikras veiksmas yra geras ar blogas - atlygį gauname tik žaidimo pabaigoje.

RL metu paprastai atliekame daug eksperimentų. Kiekvieno eksperimento metu turime rasti pusiausvyrą tarp jau išmoktos optimalios strategijos taikymo (**eksploatacija**) ir naujų galimų būsenų tyrinėjimo (**eksploracija**).

## OpenAI Gym

Puikus įrankis RL yra [OpenAI Gym](https://gym.openai.com/) - **simuliacijos aplinka**, galinti simuliuoti daugybę skirtingų aplinkų, pradedant Atari žaidimais ir baigiant fizikos uždaviniais, tokiais kaip stulpo balansavimas. Tai viena populiariausių simuliacijos aplinkų stiprinamojo mokymosi algoritmams treniruoti, kurią prižiūri [OpenAI](https://openai.com/).

> **Note**: Visas OpenAI Gym aplinkas galite rasti [čia](https://gym.openai.com/envs/#classic_control).

## CartPole Balansavimas

Tikriausiai visi esate matę šiuolaikinius balansavimo įrenginius, tokius kaip *Segway* ar *giroskuteriai*. Jie automatiškai balansuoja, reguliuodami savo ratus pagal signalus iš akselerometro ar giroskopo. Šioje dalyje išmoksime spręsti panašią problemą - stulpo balansavimą. Tai primena situaciją, kai cirko artistas bando išlaikyti stulpą ant rankos, tačiau šis balansavimas vyksta tik vienoje dimensijoje.

Supaprastinta balansavimo versija vadinama **CartPole** problema. CartPole pasaulyje turime horizontalų slankiklį, kuris gali judėti į kairę arba į dešinę, o tikslas yra išlaikyti vertikalų stulpą ant slankiklio, kai jis juda.

<img alt="a cartpole" src="images/cartpole.png" width="200"/>

Norint sukurti ir naudoti šią aplinką, reikia kelių Python kodo eilučių:

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

Kiekviena aplinka pasiekiama vienodai:
* `env.reset` pradeda naują eksperimentą
* `env.step` atlieka simuliacijos žingsnį. Jis gauna **veiksmą** iš **veiksmų erdvės** ir grąžina **stebėjimą** (iš stebėjimų erdvės), taip pat atlygį ir pabaigos vėliavėlę.

Aukščiau pateiktame pavyzdyje kiekviename žingsnyje atliekame atsitiktinį veiksmą, todėl eksperimento trukmė yra labai trumpa:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

RL algoritmo tikslas yra išmokyti modelį - vadinamąją **politiką** π - kuri grąžins veiksmą, atsižvelgiant į tam tikrą būseną. Taip pat galime laikyti politiką probabilistine, t. y. bet kuriai būsenai *s* ir veiksmui *a* ji grąžins tikimybę π(*a*|*s*), kad turėtume atlikti *a* būsenos *s* metu.

## Politikos gradientų algoritmas

Akivaizdžiausias būdas modeliuoti politiką yra sukurti neuroninį tinklą, kuris priims būsenas kaip įvestį ir grąžins atitinkamus veiksmus (arba veiksmų tikimybes). Tam tikra prasme tai būtų panašu į įprastą klasifikavimo užduotį, tačiau su esminiu skirtumu - iš anksto nežinome, kokius veiksmus turėtume atlikti kiekviename žingsnyje.

Idėja yra įvertinti šias tikimybes. Sukuriame **kaupiamųjų atlygių** vektorių, kuris rodo mūsų bendrą atlygį kiekviename eksperimento žingsnyje. Taip pat taikome **atlygio diskontavimą**, dauginant ankstesnius atlygius iš koeficiento γ=0.99, kad sumažintume ankstesnių atlygių svarbą. Tada sustipriname tuos žingsnius eksperimento kelyje, kurie duoda didesnius atlygius.

> Sužinokite daugiau apie politikos gradientų algoritmą ir pamatykite jį veiksmingą [pavyzdiniame užrašų knygelėje](CartPole-RL-TF.ipynb).

## Aktoriaus-kritiko algoritmas

Patobulinta politikos gradientų metodo versija vadinama **Aktoriaus-kritiko** metodu. Pagrindinė idėja yra ta, kad neuroninis tinklas būtų apmokytas grąžinti du dalykus:

* Politiką, kuri nustato, kokį veiksmą atlikti. Ši dalis vadinama **aktorius**.
* Bendro atlygio, kurį galime tikėtis gauti šioje būsenoje, įvertinimą - ši dalis vadinama **kritikas**.

Tam tikra prasme ši architektūra primena [GAN](../../4-ComputerVision/10-GANs/README.md), kur turime du tinklus, kurie mokomi vienas prieš kitą. Aktoriaus-kritiko modelyje aktorius siūlo veiksmą, kurį reikia atlikti, o kritikas bando būti kritiškas ir įvertinti rezultatą. Tačiau mūsų tikslas yra mokyti šiuos tinklus vieningai.

Kadangi eksperimento metu žinome tiek tikruosius kaupiamuosius atlygius, tiek kritiko grąžintus rezultatus, gana lengva sukurti nuostolių funkciją, kuri sumažintų skirtumą tarp jų. Tai suteiktų mums **kritiko nuostolį**. **Aktoriaus nuostolį** galime apskaičiuoti naudodami tą patį metodą kaip ir politikos gradientų algoritme.

Paleidę vieną iš šių algoritmų, galime tikėtis, kad mūsų CartPole elgsis taip:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Pratimai: Politikos gradientai ir aktoriaus-kritiko RL

Tęskite mokymąsi šiuose užrašų knygelėse:

* [RL TensorFlow aplinkoje](CartPole-RL-TF.ipynb)
* [RL PyTorch aplinkoje](CartPole-RL-PyTorch.ipynb)

## Kiti RL uždaviniai

Šiais laikais stiprinamasis mokymasis yra sparčiai auganti tyrimų sritis. Keletas įdomių stiprinamojo mokymosi pavyzdžių:

* Kompiuterio mokymas žaisti **Atari žaidimus**. Šio uždavinio iššūkis yra tas, kad neturime paprastos būsenos, pateiktos kaip vektorius, o tik ekrano nuotrauką - todėl turime naudoti CNN, kad konvertuotume šį ekrano vaizdą į požymių vektorių arba išgautume atlygio informaciją. Atari žaidimai yra prieinami Gym aplinkoje.
* Kompiuterio mokymas žaisti stalo žaidimus, tokius kaip šachmatai ir Go. Pastaruoju metu pažangiausios programos, tokios kaip **Alpha Zero**, buvo apmokytos nuo nulio, kai du agentai žaidė vienas prieš kitą ir tobulėjo kiekviename žingsnyje.
* Pramonėje RL naudojamas kuriant valdymo sistemas iš simuliacijų. Paslauga, vadinama [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste), yra specialiai tam skirta.

## Išvada

Dabar išmokome treniruoti agentus, kad jie pasiektų gerų rezultatų, tiesiog pateikdami jiems atlygio funkciją, apibrėžiančią norimą žaidimo būseną, ir suteikdami galimybę protingai tyrinėti paieškos erdvę. Sėkmingai išbandėme du algoritmus ir per gana trumpą laiką pasiekėme gerų rezultatų. Tačiau tai tik jūsų kelionės į RL pradžia, ir tikrai turėtumėte apsvarstyti galimybę lankyti atskirą kursą, jei norite gilintis.

## 🚀 Iššūkis

Išnagrinėkite taikymus, išvardytus skyriuje „Kiti RL uždaviniai“, ir pabandykite įgyvendinti vieną iš jų!

## [Po paskaitos: testas](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Peržiūra ir savarankiškas mokymasis

Sužinokite daugiau apie klasikinį stiprinamąjį mokymąsi mūsų [Mašininio mokymosi pradedantiesiems programoje](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Žiūrėkite [šį puikų vaizdo įrašą](https://www.youtube.com/watch?v=qv6UVOQ0F44), kuriame pasakojama, kaip kompiuteris gali išmokti žaisti Super Mario.

## Užduotis: [Treniruokite kalnų automobilį](lab/README.md)

Jūsų tikslas šios užduoties metu bus treniruoti kitą Gym aplinką - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.