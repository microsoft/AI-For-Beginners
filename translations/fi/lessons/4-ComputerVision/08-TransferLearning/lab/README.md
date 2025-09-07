<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7765935c35fcee69b9fe2d0cfd6963e2",
  "translation_date": "2025-08-28T19:29:15+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/lab/README.md",
  "language_code": "fi"
}
-->
# Oxfordin lemmikkien luokittelu siirtämällä oppimista hyödyntäen

Lab-tehtävä [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) -materiaalista.

## Tehtävä

Kuvittele, että sinun täytyy kehittää sovellus lemmikkien päiväkodille kaikkien lemmikkien luetteloimiseksi. Yksi tällaisen sovelluksen hienoista ominaisuuksista olisi kyky tunnistaa automaattisesti lemmikin rotu valokuvasta. Tässä tehtävässä käytämme siirtämällä oppimista luokitellaksemme oikeiden lemmikkien kuvia [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) -lemmikkidatasta.

## Datasetti

Käytämme alkuperäistä [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) -lemmikkidatasettiä, joka sisältää 35 erilaista koira- ja kissarotua.

Datasetin lataamiseen käytä seuraavaa koodinpätkää:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Aloitusnotebook

Aloita lab-työ avaamalla [OxfordPets.ipynb](OxfordPets.ipynb)

## Yhteenveto

Siirtämällä oppiminen ja valmiiksi koulutetut verkot mahdollistavat todellisten kuvien luokitteluongelmien ratkaisemisen suhteellisen helposti. Kuitenkin valmiiksi koulutetut verkot toimivat hyvin samankaltaisilla kuvilla, ja jos alamme luokitella hyvin erilaisia kuvia (esim. lääketieteellisiä kuvia), tulokset todennäköisesti heikkenevät huomattavasti.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.