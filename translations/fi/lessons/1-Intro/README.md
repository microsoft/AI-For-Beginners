<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-28T19:42:43+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "fi"
}
-->
> Kuva: [Dmitry Soshnikov](http://soshnikov.com)

Ajan myötä laskentateho on halventunut ja saatavilla olevan datan määrä kasvanut, mikä on mahdollistanut neuroverkkojen erinomaisen suorituskyvyn monilla alueilla, kuten tietokonenäkö ja puheen ymmärtäminen. Viimeisen vuosikymmenen aikana termi "tekoäly" on enimmäkseen yhdistetty neuroverkkoihin, koska suurin osa tekoälyn menestyksistä, joista kuulemme, perustuu niihin.

Voimme havaita, kuinka lähestymistavat ovat muuttuneet esimerkiksi shakkia pelaavan tietokoneohjelman luomisessa:

* Varhaiset shakkiohjelmat perustuivat hakuun – ohjelma yritti eksplisiittisesti arvioida vastustajan mahdollisia siirtoja tietyn määrän seuraavia siirtoja ja valitsi optimaalisen siirron sen perusteella, mikä paras asema voidaan saavuttaa muutamassa siirrossa. Tämä johti niin sanotun [alpha-beta karsinnan](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) hakualgoritmin kehittämiseen.
* Hakustrategiat toimivat hyvin pelin loppuvaiheessa, jossa hakutila on rajattu pienellä määrällä mahdollisia siirtoja. Kuitenkin pelin alussa hakutila on valtava, ja algoritmia voidaan parantaa oppimalla olemassa olevista ihmispelaajien peleistä. Myöhemmät kokeilut hyödynsivät niin sanottua [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning) -lähestymistapaa, jossa ohjelma etsi tietokannasta tapauksia, jotka ovat hyvin samankaltaisia kuin nykyinen peliasema.
* Modernit ohjelmat, jotka voittavat ihmispelaajat, perustuvat neuroverkkoihin ja [vahvistusoppimiseen](https://en.wikipedia.org/wiki/Reinforcement_learning), jossa ohjelmat oppivat pelaamaan pelaamalla pitkään itseään vastaan ja oppimalla omista virheistään – aivan kuten ihmiset oppivat pelaamaan shakkia. Tietokoneohjelma voi kuitenkin pelata paljon enemmän pelejä paljon lyhyemmässä ajassa ja oppia siten paljon nopeammin.

✅ Tee hieman tutkimusta muista peleistä, joita tekoäly on pelannut.

Samoin voimme nähdä, kuinka lähestymistavat "puhuvien ohjelmien" (jotka saattavat läpäistä Turingin testin) luomiseen ovat muuttuneet:

* Varhaiset ohjelmat, kuten [Eliza](https://en.wikipedia.org/wiki/ELIZA), perustuivat hyvin yksinkertaisiin kielioppisääntöihin ja syötteen lauseen muotoiluun kysymykseksi.
* Modernit avustajat, kuten Cortana, Siri tai Google Assistant, ovat kaikki hybridijärjestelmiä, jotka käyttävät neuroverkkoja muuntamaan puheen tekstiksi ja tunnistamaan käyttäjän tarkoituksen, ja sen jälkeen hyödyntävät päättelyä tai eksplisiittisiä algoritmeja suorittaakseen vaaditut toiminnot.
* Tulevaisuudessa voimme odottaa täysin neuroverkkoihin perustuvaa mallia, joka käsittelee dialogia itsenäisesti. Viimeisimmät GPT- ja [Turing-NLG](https://turing.microsoft.com/) -neuroverkkojen perheet ovat osoittaneet suurta menestystä tässä.

> Kuva: Dmitry Soshnikov, [valokuva](https://unsplash.com/photos/r8LmVbUKgns) Marina Abrosimovalta, [Unsplash](https://unsplash.com/@abrosimova_marina_foto)

## Viimeaikainen tekoälytutkimus

Neuroverkkojen tutkimuksen valtava kasvu alkoi noin vuonna 2010, kun suuret julkiset tietoaineistot tulivat saataville. Suuri kokoelma kuvia nimeltä [ImageNet](https://en.wikipedia.org/wiki/ImageNet), joka sisältää noin 14 miljoonaa annotoitua kuvaa, synnytti [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![ILSVRC Tarkkuus](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Kuva: [Dmitry Soshnikov](http://soshnikov.com)

Vuonna 2012 [Konvoluutioneuroverkkoja](../4-ComputerVision/07-ConvNets/README.md) käytettiin ensimmäistä kertaa kuvien luokittelussa, mikä johti merkittävään virheiden vähenemiseen (lähes 30 %:sta 16,4 %:iin). Vuonna 2015 Microsoft Researchin ResNet-arkkitehtuuri [saavutti ihmisen tasoisen tarkkuuden](https://doi.org/10.1109/ICCV.2015.123).

Sen jälkeen neuroverkot ovat osoittaneet erittäin menestyksekästä toimintaa monissa tehtävissä:

---

Vuosi | Ihmisen taso saavutettu
-----|--------
2015 | [Kuvien luokittelu](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Puheentunnistus keskusteluissa](https://arxiv.org/abs/1610.05256)
2018 | [Automaattinen konekäännös](https://arxiv.org/abs/1803.05567) (kiinasta englantiin)
2020 | [Kuvatekstien luominen](https://arxiv.org/abs/2009.13682)

Viime vuosina olemme nähneet suuria edistysaskeleita suurten kielimallien, kuten BERT ja GPT-3, kanssa. Tämä on tapahtunut pääasiassa siksi, että saatavilla on paljon yleistä tekstidataa, joka mahdollistaa mallien kouluttamisen tekstien rakenteen ja merkityksen ymmärtämiseen, niiden esikouluttamisen yleisillä tekstikokoelmilla ja mallien erikoistamisen tarkempiin tehtäviin. Opimme lisää [luonnollisen kielen käsittelystä](../5-NLP/README.md) myöhemmin tässä kurssissa.

## 🚀 Haaste

Tutki internetiä ja päätä, missä mielestäsi tekoälyä käytetään tehokkaimmin. Onko se karttasovelluksessa, puheesta tekstiksi -palvelussa vai videopelissä? Tutki, miten järjestelmä on rakennettu.

## [Luennon jälkeinen kysely](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Kertaus ja itseopiskelu

Kertaa tekoälyn ja koneoppimisen historiaa lukemalla [tämä oppitunti](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Valitse jokin elementti tämän oppitunnin tai sen alussa olevan sketchnoten sisällöstä ja tutki sitä syvällisemmin ymmärtääksesi sen kehitystä ohjaavaa kulttuurista kontekstia.

**Tehtävä**: [Game Jam](assignment.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.