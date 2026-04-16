# Syvävahvistusoppiminen

Vahvistusoppiminen (RL) nähdään yhtenä koneoppimisen perusparadigmoista, yhdessä ohjatun oppimisen ja ohjaamattoman oppimisen kanssa. Siinä missä ohjatussa oppimisessa tukeudumme tunnettuja tuloksia sisältävään aineistoon, RL perustuu **oppimiseen tekemällä**. Esimerkiksi, kun näemme ensimmäistä kertaa tietokonepelin, alamme pelata sitä, vaikka emme tiedä sääntöjä, ja pian pystymme parantamaan taitojamme pelkästään pelaamalla ja mukauttamalla käyttäytymistämme.

## [Esiluentovisa](https://ff-quizzes.netlify.app/en/ai/quiz/43)

RL:n suorittamiseen tarvitsemme:

* **Ympäristön** tai **simulaattorin**, joka määrittää pelin säännöt. Meidän tulisi pystyä suorittamaan kokeita simulaattorissa ja tarkkailemaan tuloksia.
* **Palkkiofunktion**, joka osoittaa, kuinka onnistunut kokeemme oli. Esimerkiksi tietokonepelin pelaamisen oppimisessa palkkio olisi lopullinen pistemäärämme.

Palkkiofunktion perusteella meidän tulisi pystyä mukauttamaan käyttäytymistämme ja parantamaan taitojamme, jotta seuraavalla kerralla pelaamme paremmin. Suurin ero RL:n ja muiden koneoppimisen tyyppien välillä on se, että RL:ssä emme yleensä tiedä, voitammeko vai häviämme, ennen kuin peli on ohi. Näin ollen emme voi sanoa, onko tietty siirto yksinään hyvä vai ei – saamme palkkion vasta pelin lopussa.

RL:n aikana suoritamme tyypillisesti monia kokeita. Jokaisen kokeen aikana meidän on tasapainotettava tähän mennessä oppimamme optimaalisen strategian noudattaminen (**hyödyntäminen**) ja uusien mahdollisten tilojen tutkiminen (**tutkiminen**).

## OpenAI Gym

Erinomainen työkalu RL:ään on [OpenAI Gym](https://gym.openai.com/) - **simulaatioympäristö**, joka voi simuloida monia erilaisia ympäristöjä, alkaen Atari-peleistä aina fysiikkaan, kuten tangon tasapainottamiseen. Se on yksi suosituimmista simulaatioympäristöistä vahvistusoppimisalgoritmien kouluttamiseen, ja sitä ylläpitää [OpenAI](https://openai.com/).

> **Note**: Voit nähdä kaikki OpenAI Gymin tarjoamat ympäristöt [täältä](https://gym.openai.com/envs/#classic_control).

## CartPole-tasapainotus

Olette varmasti nähneet moderneja tasapainolaitteita, kuten *Segway* tai *Gyroscooters*. Ne pystyvät automaattisesti tasapainottamaan itsensä säätämällä pyöriään kiihtyvyysmittarin tai gyroskoopin signaalin perusteella. Tässä osiossa opimme ratkaisemaan vastaavan ongelman – tangon tasapainottamisen. Se muistuttaa tilannetta, jossa sirkustaiteilija tasapainottaa tankoa kädellään – mutta tässä tapauksessa tasapainotus tapahtuu vain yhdessä ulottuvuudessa.

Yksinkertaistettu versio tasapainottamisesta tunnetaan nimellä **CartPole-ongelma**. CartPole-maailmassa meillä on vaakasuuntainen liukusäädin, joka voi liikkua vasemmalle tai oikealle, ja tavoitteena on tasapainottaa pystysuora tanko liukusäätimen päällä sen liikkuessa.

<img alt="cartpole" src="../../../../../translated_images/fi/cartpole.f52a67f27e058170.webp" width="200"/>

Tämän ympäristön luomiseen ja käyttämiseen tarvitsemme muutaman rivin Python-koodia:

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

Jokaiseen ympäristöön pääsee käsiksi samalla tavalla:
* `env.reset` aloittaa uuden kokeen
* `env.step` suorittaa simulaatioaskeleen. Se vastaanottaa **toiminnon** **toimintatilasta** ja palauttaa **havainnon** (havaintotilasta), sekä palkkion ja lopetuslipun.

Yllä olevassa esimerkissä suoritamme satunnaisen toiminnon jokaisessa askeleessa, minkä vuoksi kokeen kesto on hyvin lyhyt:

![tasapainoton cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

RL-algoritmin tavoitteena on kouluttaa malli – niin kutsuttu **politiikka** &pi; – joka palauttaa toiminnon tiettyyn tilaan vastauksena. Voimme myös pitää politiikkaa todennäköisyyspohjaisena, eli mille tahansa tilalle *s* ja toiminnolle *a* se palauttaa todennäköisyyden &pi;(*a*|*s*), että meidän tulisi valita *a* tilassa *s*.

## Politiikkagradienttialgoritmi

Ilmeisin tapa mallintaa politiikka on luoda neuroverkko, joka ottaa syötteenä tilat ja palauttaa vastaavat toiminnot (tai pikemminkin kaikkien toimintojen todennäköisyydet). Tietyssä mielessä se olisi samanlainen kuin tavallinen luokittelutehtävä, mutta merkittävä ero on siinä, että emme tiedä etukäteen, mitä toimintoja meidän tulisi suorittaa kussakin vaiheessa.

Ajatuksena on arvioida näitä todennäköisyyksiä. Rakennamme **kumulatiivisten palkkioiden** vektorin, joka osoittaa kokonaispalkkiomme kussakin kokeen vaiheessa. Sovellamme myös **palkkioiden diskonttausta** kertomalla aikaisemmat palkkiot kertoimella &gamma;=0.99, jotta aikaisempien palkkioiden merkitys vähenee. Sitten vahvistamme niitä kokeen vaiheita, jotka tuottavat suurempia palkkioita.

> Lue lisää Politiikkagradienttialgoritmista ja katso se toiminnassa [esimerkkivihkossa](CartPole-RL-TF.ipynb).

## Actor-Critic-algoritmi

Parannettu versio Politiikkagradienttimenetelmästä tunnetaan nimellä **Actor-Critic**. Sen perusidea on, että neuroverkko koulutetaan palauttamaan kaksi asiaa:

* Politiikka, joka määrittää, mikä toiminto suoritetaan. Tätä osaa kutsutaan **actoriksi**.
* Arvio siitä, kuinka suuren kokonaispalkkion voimme odottaa saavuttavamme tässä tilassa – tätä osaa kutsutaan **criticiksi**.

Tietyssä mielessä tämä arkkitehtuuri muistuttaa [GAN:ia](../../4-ComputerVision/10-GANs/README.md), jossa meillä on kaksi verkkoa, jotka koulutetaan toisiaan vastaan. Actor-Critic-mallissa actor ehdottaa toimintoa, joka meidän tulisi suorittaa, ja critic yrittää olla kriittinen ja arvioida tuloksen. Tavoitteenamme on kuitenkin kouluttaa nämä verkot yhdessä.

Koska tiedämme sekä todelliset kumulatiiviset palkkiot että criticin kokeen aikana palauttamat tulokset, on suhteellisen helppoa rakentaa häviöfunktio, joka minimoi niiden välisen eron. Tämä antaa meille **critic-häviön**. Voimme laskea **actor-häviön** käyttämällä samaa lähestymistapaa kuin politiikkagradienttialgoritmissa.

Kun olemme suorittaneet jonkin näistä algoritmeista, voimme odottaa CartPolen käyttäytyvän näin:

![tasapainottava cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Harjoitukset: Politiikkagradientit ja Actor-Critic RL

Jatka oppimista seuraavissa vihkoissa:

* [RL TensorFlow'ssa](CartPole-RL-TF.ipynb)
* [RL PyTorchissa](CartPole-RL-PyTorch.ipynb)

## Muut RL-tehtävät

Vahvistusoppiminen on nykyään nopeasti kasvava tutkimusalue. Joitakin mielenkiintoisia vahvistusoppimisen sovelluksia ovat:

* Tietokoneen opettaminen pelaamaan **Atari-pelejä**. Tämän ongelman haastava osa on, että meillä ei ole yksinkertaista tilaa, joka olisi esitetty vektorina, vaan pikemminkin kuvakaappaus – ja meidän on käytettävä CNN:ää muuntamaan tämä kuvaruutu ominaisuusvektoriksi tai palkkiotiedon poimimiseen. Atari-pelit ovat saatavilla Gymissä.
* Tietokoneen opettaminen pelaamaan lautapelejä, kuten shakkia ja Go:ta. Viime aikoina huipputason ohjelmat, kuten **Alpha Zero**, on koulutettu alusta alkaen kahden agentin pelatessa toisiaan vastaan ja parantaessa joka askeleella.
* Teollisuudessa RL:ää käytetään ohjausjärjestelmien luomiseen simulaatiosta. Palvelu nimeltä [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) on suunniteltu erityisesti tähän tarkoitukseen.

## Yhteenveto

Olemme nyt oppineet kouluttamaan agentteja saavuttamaan hyviä tuloksia pelkästään tarjoamalla heille palkkiofunktion, joka määrittää pelin toivotun tilan, ja antamalla heille mahdollisuuden tutkia älykkäästi hakutilaa. Olemme kokeilleet kahta algoritmia ja saavuttaneet hyviä tuloksia suhteellisen lyhyessä ajassa. Tämä on kuitenkin vasta alkua matkallesi RL:n parissa, ja sinun kannattaa ehdottomasti harkita erillisen kurssin suorittamista, jos haluat syventyä aiheeseen.

## 🚀 Haaste

Tutustu "Muut RL-tehtävät" -osiossa lueteltuihin sovelluksiin ja yritä toteuttaa yksi niistä!

## [Jälkiluentovisa](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Kertaus ja itseopiskelu

Lue lisää klassisesta vahvistusoppimisesta [Koneoppiminen aloittelijoille -opetussuunnitelmastamme](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Katso [tämä loistava video](https://www.youtube.com/watch?v=qv6UVOQ0F44), jossa kerrotaan, kuinka tietokone voi oppia pelaamaan Super Mariota.

## Tehtävä: [Kouluta Mountain Car](lab/README.md)

Tavoitteenasi tässä tehtävässä on kouluttaa toinen Gym-ympäristö – [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

