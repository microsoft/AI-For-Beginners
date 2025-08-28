<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-28T19:49:04+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "fi"
}
-->
# Moniluokkainen luokittelu perceptronilla

Lab-tehtävä [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) -materiaalista.

## Tehtävä

Käyttäen tässä oppitunnissa kehittämäämme koodia MNIST-käsinkirjoitettujen numeroiden binääriluokitteluun, luo moniluokkainen luokitin, joka pystyy tunnistamaan minkä tahansa numeron. Laske luokittelutarkkuus sekä harjoitus- että testidatassa ja tulosta sekaannusmatriisi.

## Vinkkejä

1. Luo jokaiselle numerolle datasetti binääriluokittimelle, joka erottaa "tämän numeron vs. kaikki muut numerot".
1. Kouluta 10 erilaista perceptronia binääriluokittelua varten (yksi kutakin numeroa varten).
1. Määritä funktio, joka luokittelee syötteenä annetun numeron.

> **Vinkki**: Jos yhdistämme kaikkien 10 perceptronin painot yhdeksi matriisiksi, voimme soveltaa kaikkia 10 perceptronia syötenumeroihin yhdellä matriisikertolaskulla. Todennäköisin numero voidaan sitten löytää yksinkertaisesti soveltamalla `argmax`-operaatiota tulokseen.

## Aloitusnotebook

Aloita lab-tehtävä avaamalla [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.