# Skip-Gram mudeli treenimine

Laboriülesanne [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) materjalidest.

## Ülesanne

Selles laboris kutsume teid üles treenima Word2Vec mudelit, kasutades Skip-Gram tehnikat. Treenige võrgustik koos sisseehitatud vektoritega, et ennustada naabersõnu $N$-sõna laiuses Skip-Gram aknas. Võite kasutada [selle tunni koodi](../CBoW-TF.ipynb) ja seda veidi kohandada.

## Andmestik

Võite kasutada ükskõik millist raamatut. Palju tasuta tekste leiate [Project Gutenberg](https://www.gutenberg.org/) lehelt, näiteks siin on otselink Lewis Carrolli teosele [Alice Imedemaal](https://www.gutenberg.org/files/11/11-0.txt). Või võite kasutada Shakespeare'i näidendeid, mille saate järgmise koodi abil:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Uurige!

Kui teil on aega ja soovite teemasse süveneda, proovige uurida mitmeid asju:

* Kuidas mõjutab sisseehitatud vektori suurus tulemusi?
* Kuidas mõjutavad erinevad tekstistiilid tulemust?
* Võtke mitu väga erinevat tüüpi sõna ja nende sünonüümid, hankige nende vektorrepresentatsioonid, rakendage PCA, et vähendada dimensioonid 2-le, ja kujutage need 2D-ruumis graafiliselt. Kas näete mingeid mustreid?

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.