# Giliojo stiprinamojo mokymosi pagrindai

Stiprinamasis mokymasis (RL) laikomas vienu iš pagrindinių mašininio mokymosi paradigmų, greta mokymosi su mokytoju ir mokymosi be mokytojo. Mokymosi su mokytoju metu remiamės duomenų rinkiniu su žinomais rezultatais, o RL pagrįstas **mokymusi per veiksmą**. Pavyzdžiui, kai pirmą kartą matome kompiuterinį žaidimą, pradedame jį žaisti, net nežinodami taisyklių, ir greitai galime tobulinti savo įgūdžius tiesiog žaisdami ir koreguodami savo elgesį.

## [Prieš paskaitos testas](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Norint atlikti RL, mums reikia:

* **Aplinkos** arba **simuliatoriaus**, kuris nustato žaidimo taisykles. Turėtume turėti galimybę atlikti eksperimentus simuliatoriuje ir stebėti rezultatus.
* **Atlygio funkcijos**, kuri nurodo, kaip sėkmingas buvo mūsų eksperimentas. Mokantis žaisti kompiuterinį žaidimą, atlygis būtų mūsų galutinis rezultatas.

Remdamiesi atlygio funkcija, turėtume sugebėti koreguoti savo elgesį ir tobulinti įgūdžius, kad kitą kartą žaistume geriau. Pagrindinis skirtumas tarp kitų mašininio mokymosi tipų ir RL yra tas, kad RL metu paprastai nežinome, ar laimime, ar pralaimime, kol nebaigiame žaidimo. Taigi negalime pasakyti, ar tam tikras veiksmas vienas pats yra geras ar ne - atlygį gauname tik žaidimo pabaigoje.

RL metu paprastai atliekame daug eksperimentų. Kiekvieno eksperimento metu turime rasti pusiausvyrą tarp optimalaus strategijos laikymosi, kurią iki šiol išmokome (**eksploatacija**), ir naujų galimų būsenų tyrinėjimo (**tyrinėjimas**).

## OpenAI Gym

Puikus įrankis RL yra [OpenAI Gym](https://gym.openai.com/) - **simuliacijos aplinka**, galinti simuliuoti daugybę skirtingų aplinkų, pradedant Atari žaidimais ir baigiant fizikos uždaviniais, tokiais kaip stulpelio balansavimas. Tai viena populiariausių simuliacijos aplinkų stiprinamojo mokymosi algoritmams treniruoti, kurią prižiūri [OpenAI](https://openai.com/).

> **Note**: Visas OpenAI Gym aplinkas galite peržiūrėti [čia](https://gym.openai.com/envs/#classic_control).

## CartPole Balansavimas

Tikriausiai visi esate matę modernius balansavimo įrenginius, tokius kaip *Segway* ar *Giroskuteriai*. Jie sugeba automatiškai balansuoti, reguliuodami savo ratus pagal signalą iš akselerometro ar giroskopo. Šioje dalyje išmoksime išspręsti panašią problemą - stulpelio balansavimą. Tai panašu į situaciją, kai cirko atlikėjas turi balansuoti stulpelį ant savo rankos - tačiau šis balansavimas vyksta tik 1D.

Supaprastinta balansavimo versija vadinama **CartPole** problema. CartPole pasaulyje turime horizontalų slankiklį, kuris gali judėti į kairę arba į dešinę, o tikslas yra balansuoti vertikalų stulpelį ant slankiklio, kai jis juda.

<img alt="cartpole" src="../../../../../translated_images/lt/cartpole.f52a67f27e058170.webp" width="200"/>

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
* `env.step` atlieka simuliacijos žingsnį. Jis gauna **veiksmą** iš **veiksmų erdvės** ir grąžina **stebėjimą** (iš stebėjimų erdvės), taip pat atlygį ir nutraukimo vėliavą.

Pavyzdyje aukščiau kiekviename žingsnyje atliekame atsitiktinį veiksmą, todėl eksperimento trukmė yra labai trumpa:

![nebalansuojantis cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

RL algoritmo tikslas yra išmokyti modelį - vadinamąją **politiką** &pi; - kuri grąžins veiksmą, atsižvelgiant į tam tikrą būseną. Taip pat galime laikyti politiką probabilistine, t.y., bet kuriai būsenai *s* ir veiksmui *a* ji grąžins tikimybę &pi;(*a*|*s*), kad turėtume atlikti *a* būsenos *s* metu.

## Politikos gradientų algoritmas

Akivaizdžiausias būdas modeliuoti politiką yra sukurti neuroninį tinklą, kuris priims būsenas kaip įvestį ir grąžins atitinkamus veiksmus (arba veiksmų tikimybes). Tam tikra prasme tai būtų panašu į įprastą klasifikavimo užduotį, su pagrindiniu skirtumu - iš anksto nežinome, kokius veiksmus turėtume atlikti kiekviename žingsnyje.

Idėja čia yra įvertinti tas tikimybes. Sukuriame **kaupiamųjų atlygių** vektorių, kuris rodo mūsų bendrą atlygį kiekviename eksperimento žingsnyje. Taip pat taikome **atlygio diskontavimą**, dauginant ankstesnius atlygius iš tam tikro koeficiento &gamma;=0.99, kad sumažintume ankstesnių atlygių svarbą. Tada sustipriname tuos žingsnius eksperimento kelyje, kurie duoda didesnius atlygius.

> Sužinokite daugiau apie politikos gradientų algoritmą ir pamatykite jį veiksmuose [pavyzdiniame užrašų knygelėje](CartPole-RL-TF.ipynb).

## Aktoriaus-kritiko algoritmas

Patobulinta politikos gradientų metodo versija vadinama **Aktoriaus-kritiko** metodu. Pagrindinė idėja yra ta, kad neuroninis tinklas būtų apmokytas grąžinti du dalykus:

* Politiką, kuri nustato, kokį veiksmą atlikti. Ši dalis vadinama **aktorius**.
* Bendro atlygio, kurį galime tikėtis gauti šioje būsenoje, įvertinimą - ši dalis vadinama **kritikas**.

Tam tikra prasme ši architektūra primena [GAN](../../4-ComputerVision/10-GANs/README.md), kur turime du tinklus, kurie treniruojami vienas prieš kitą. Aktoriaus-kritiko modelyje aktorius siūlo veiksmą, kurį turime atlikti, o kritikas bando būti kritiškas ir įvertinti rezultatą. Tačiau mūsų tikslas yra treniruoti šiuos tinklus kartu.

Kadangi eksperimento metu žinome tiek tikrus kaupiamuosius atlygius, tiek kritiko grąžintus rezultatus, palyginti lengva sukurti nuostolių funkciją, kuri sumažintų skirtumą tarp jų. Tai suteiktų mums **kritiko nuostolį**. **Aktoriaus nuostolį** galime apskaičiuoti naudodami tą patį metodą kaip ir politikos gradientų algoritme.

Po vieno iš šių algoritmų paleidimo galime tikėtis, kad mūsų CartPole elgsis taip:

![balansuojantis cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Pratimai: Politikos gradientai ir aktoriaus-kritiko RL

Tęskite mokymąsi šiuose užrašų knygelėse:

* [RL su TensorFlow](CartPole-RL-TF.ipynb)
* [RL su PyTorch](CartPole-RL-PyTorch.ipynb)

## Kiti RL uždaviniai

Stiprinamasis mokymasis šiandien yra sparčiai auganti tyrimų sritis. Keletas įdomių stiprinamojo mokymosi pavyzdžių:

* Kompiuterio mokymas žaisti **Atari žaidimus**. Šio uždavinio sudėtingumas yra tas, kad neturime paprastos būsenos, pateiktos kaip vektorius, o turime ekrano nuotrauką - ir turime naudoti CNN, kad konvertuotume šį ekrano vaizdą į požymių vektorių arba išgautume atlygio informaciją. Atari žaidimai yra prieinami Gym.
* Kompiuterio mokymas žaisti stalo žaidimus, tokius kaip šachmatai ir Go. Neseniai pažangiausios programos, tokios kaip **Alpha Zero**, buvo apmokytos nuo nulio, kai du agentai žaidė vienas prieš kitą ir tobulėjo kiekviename žingsnyje.
* Pramonėje RL naudojamas kurti valdymo sistemas iš simuliacijos. Paslauga, vadinama [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste), yra specialiai tam sukurta.

## Išvada

Dabar išmokome treniruoti agentus, kad jie pasiektų gerų rezultatų, tiesiog suteikdami jiems atlygio funkciją, apibrėžiančią norimą žaidimo būseną, ir suteikdami jiems galimybę protingai tyrinėti paieškos erdvę. Sėkmingai išbandėme du algoritmus ir pasiekėme gerą rezultatą per palyginti trumpą laiką. Tačiau tai tik jūsų kelionės į RL pradžia, ir tikrai turėtumėte apsvarstyti galimybę lankyti atskirą kursą, jei norite gilintis.

## 🚀 Iššūkis

Ištyrinėkite taikymus, išvardytus skiltyje „Kiti RL uždaviniai“, ir pabandykite įgyvendinti vieną!

## [Po paskaitos testas](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Apžvalga ir savarankiškas mokymasis

Sužinokite daugiau apie klasikinį stiprinamąjį mokymąsi mūsų [Mašininio mokymosi pradedantiesiems programoje](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Žiūrėkite [puikų vaizdo įrašą](https://www.youtube.com/watch?v=qv6UVOQ0F44), kuriame pasakojama, kaip kompiuteris gali išmokti žaisti Super Mario.

## Užduotis: [Treniruokite kalnų automobilį](lab/README.md)

Jūsų tikslas šios užduoties metu būtų treniruoti kitą Gym aplinką - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

