# Trénink Skip-Gram modelu

Laboratorní úloha z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úkol

V této laboratorní úloze vás vyzýváme k natrénování Word2Vec modelu pomocí techniky Skip-Gram. Natrénujte síť s embeddingem, která bude předpovídat sousední slova v $N$-tokenovém Skip-Gram okně. Můžete použít [kód z této lekce](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) a mírně jej upravit.

## Dataset

Můžete použít jakoukoli knihu. Na [Project Gutenberg](https://www.gutenberg.org/) najdete spoustu volně dostupných textů, například zde je přímý odkaz na [Alenčiny příhody v říši divů](https://www.gutenberg.org/files/11/11-0.txt) od Lewise Carrolla. Nebo můžete použít Shakespearovy hry, které můžete získat pomocí následujícího kódu:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Prozkoumejte!

Pokud máte čas a chcete se ponořit hlouběji do tématu, zkuste prozkoumat několik věcí:

* Jak velikost embeddingu ovlivňuje výsledky?
* Jak různé styly textu ovlivňují výsledek?
* Vezměte několik velmi odlišných typů slov a jejich synonym, získejte jejich vektorové reprezentace, aplikujte PCA pro redukci dimenzí na 2 a vykreslete je v 2D prostoru. Vidíte nějaké vzory?

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.