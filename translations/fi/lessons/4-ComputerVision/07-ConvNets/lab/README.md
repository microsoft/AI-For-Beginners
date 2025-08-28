<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-28T19:25:54+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "fi"
}
-->
# Lemmikkien kasvojen luokittelu

Lab-tehtävä [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) -materiaalista.

## Tehtävä

Kuvittele, että sinun täytyy kehittää sovellus lemmikkien hoitopaikalle kaikkien lemmikkien luetteloimista varten. Yksi tällaisen sovelluksen hienoista ominaisuuksista olisi rodun automaattinen tunnistaminen valokuvasta. Tämä voidaan onnistuneesti toteuttaa käyttämällä neuroverkkoja.

Sinun täytyy kouluttaa konvoluutio-neuroverkko luokittelemaan eri kissojen ja koirien rodut käyttäen **Pet Faces** -datakokonaisuutta.

## Datakokonaisuus

Käytämme **Pet Faces** -datakokonaisuutta, joka on johdettu [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) lemmikkien datakokonaisuudesta. Se sisältää 35 eri koirien ja kissojen rotua.

![Datakokonaisuus, jonka kanssa työskentelemme](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.fi.png)

Ladataksesi datakokonaisuuden, käytä tätä koodinpätkää:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Aloitus Notebook

Aloita lab-työskentely avaamalla [PetFaces.ipynb](PetFaces.ipynb)

## Lopputulos

Olet ratkaissut suhteellisen monimutkaisen kuvaluokittelutehtävän alusta asti! Luokkia oli melko paljon, ja silti onnistuit saavuttamaan kohtuullisen tarkkuuden! On myös järkevää mitata top-k tarkkuutta, koska on helppo sekoittaa joitakin luokkia, jotka eivät ole selvästi erilaisia edes ihmisille.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.