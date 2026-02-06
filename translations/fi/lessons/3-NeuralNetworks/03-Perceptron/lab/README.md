# Moniluokkainen luokittelu perceptronilla

Lab-tehtävä [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) -materiaalista.

## Tehtävä

Käyttämällä tämän oppitunnin aikana kehitettyä koodia MNIST-käsinkirjoitettujen numeroiden binääriluokitteluun, luo moniluokkainen luokitin, joka pystyy tunnistamaan minkä tahansa numeron. Laske luokittelutarkkuus sekä koulutus- että testidatassa ja tulosta sekaannusmatriisi.

## Vinkkejä

1. Luo jokaiselle numerolle datasetti binääriluokittimelle, joka erottaa "tämän numeron vs. kaikki muut numerot"
1. Kouluta 10 eri perceptronia binääriluokittelua varten (yksi kutakin numeroa varten)
1. Määrittele funktio, joka luokittelee syötteenä annetun numeron

> **Vinkki**: Jos yhdistämme kaikkien 10 perceptronin painot yhdeksi matriisiksi, voimme soveltaa kaikkia 10 perceptronia syötteenä annettuihin numeroihin yhdellä matriisikertolaskulla. Todennäköisin numero voidaan sitten löytää käyttämällä `argmax`-operaatiota tuloksessa.

## Aloitusnotebook

Aloita lab-tehtävä avaamalla [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.