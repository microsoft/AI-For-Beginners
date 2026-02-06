# Tréning Skip-Gram modelu

Laboratórna úloha z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úloha

V tejto úlohe vás vyzývame, aby ste natrénovali Word2Vec model pomocou techniky Skip-Gram. Natrénujte sieť s embeddingom na predpovedanie susedných slov v $N$-tokenovom širokom Skip-Gram okne. Môžete použiť [kód z tejto lekcie](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) a mierne ho upraviť.

## Dataset

Môžete použiť akúkoľvek knihu. Na stránke [Project Gutenberg](https://www.gutenberg.org/) nájdete množstvo voľne dostupných textov, napríklad priamy odkaz na [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt) od Lewisa Carrolla. Alebo môžete použiť Shakespearove hry, ktoré môžete získať pomocou nasledujúceho kódu:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Preskúmajte!

Ak máte čas a chcete sa do témy ponoriť hlbšie, skúste preskúmať niekoľko vecí:

* Ako ovplyvňuje veľkosť embeddingu výsledky?
* Ako ovplyvňujú rôzne štýly textu výsledok?
* Vezmite niekoľko veľmi odlišných typov slov a ich synonymá, získajte ich vektorové reprezentácie, aplikujte PCA na zníženie dimenzií na 2 a zobrazte ich v 2D priestore. Vidíte nejaké vzory?

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.