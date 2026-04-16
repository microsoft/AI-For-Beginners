# Ihmiskehon segmentointi

Lab-tehtävä [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) -materiaalista.

## Tehtävä

Videotuotannossa, esimerkiksi säätiedotuksissa, tarvitaan usein ihmisen kuvaa leikattavaksi kamerasta ja sijoitettavaksi jonkin muun materiaalin päälle. Tämä tehdään yleensä **chroma key** -tekniikoilla, joissa ihminen kuvataan yhtenäisen värisen taustan edessä, joka sitten poistetaan. Tässä laboratoriossa koulutamme neuroverkkopohjaisen mallin leikkaamaan ihmisen siluetin.

## Datasetti

Käytämme [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) -datasettiä Kagglesta. Lataa datasetti manuaalisesti Kagglesta.

## Aloitusnotebook

Aloita laboratorio avaamalla [BodySegmentation.ipynb](BodySegmentation.ipynb)

## Oppimispisteet

Kehon segmentointi on vain yksi yleisistä tehtävistä, joita voimme tehdä ihmisten kuvien kanssa. Muita tärkeitä tehtäviä ovat **luurangon tunnistus** ja **asennon tunnistus**. Tutustu [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) -kirjastoon nähdäksesi, miten nämä tehtävät voidaan toteuttaa.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.