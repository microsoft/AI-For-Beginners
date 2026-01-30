# Skip-Gram-mallin kouluttaminen

Lab-tehtävä [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) -materiaalista.

## Tehtävä

Tässä laboratoriossa haastamme sinut kouluttamaan Word2Vec-mallin käyttämällä Skip-Gram-tekniikkaa. Kouluta verkko, jossa on upotus, ennustamaan naapurisanat $N$-tokenin levyisessä Skip-Gram-ikkunassa. Voit käyttää [tämän oppitunnin koodia](../CBoW-TF.ipynb) ja muokata sitä hieman.

## Datasetti

Voit käyttää mitä tahansa kirjaa. Löydät paljon ilmaisia tekstejä [Project Gutenberg](https://www.gutenberg.org/) -sivustolta, esimerkiksi suora linkki [Liisan seikkailut ihmemaassa](https://www.gutenberg.org/files/11/11-0.txt)) -kirjaan, kirjoittanut Lewis Carroll. Tai voit käyttää Shakespearen näytelmiä, jotka voit ladata seuraavalla koodilla:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Tutki!

Jos sinulla on aikaa ja haluat syventyä aiheeseen, kokeile tutkia seuraavia asioita:

* Miten upotuksen koko vaikuttaa tuloksiin?
* Miten erilaiset tekstityylit vaikuttavat tuloksiin?
* Ota useita hyvin erilaisia sanatyyppejä ja niiden synonyymejä, hanki niiden vektoriedustukset, sovella PCA:ta dimensioiden vähentämiseksi kahteen, ja piirrä ne 2D-tilaan. Näetkö mitään kuvioita?

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.