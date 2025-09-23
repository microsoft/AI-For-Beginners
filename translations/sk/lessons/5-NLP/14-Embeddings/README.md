<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-25T21:38:56+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "sk"
}
-->
# Vstavané reprezentácie (Embeddings)

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/27)

Pri trénovaní klasifikátorov založených na BoW alebo TF/IDF sme pracovali s vysokodimenzionálnymi vektormi bag-of-words s dĺžkou `vocab_size` a explicitne sme prevádzali nízkodimenzionálne pozičné reprezentácie na riedke one-hot reprezentácie. Táto one-hot reprezentácia však nie je pamäťovo efektívna. Navyše, každé slovo je spracované nezávisle od ostatných, t. j. one-hot kódované vektory nevyjadrujú žiadnu sémantickú podobnosť medzi slovami.

Myšlienka **vstavanej reprezentácie (embedding)** spočíva v tom, že slová sú reprezentované nízkodimenzionálnymi hustými vektormi, ktoré určitým spôsobom odrážajú sémantický význam slova. Neskôr si povieme, ako vytvoriť zmysluplné vstavané reprezentácie slov, ale zatiaľ ich môžeme chápať ako spôsob zníženia dimenzionality vektorov slov.

Vstavaná vrstva teda prijíma slovo ako vstup a produkuje výstupný vektor so špecifikovanou veľkosťou `embedding_size`. V istom zmysle je to veľmi podobné vrstve `Linear`, ale namiesto prijímania one-hot kódovaného vektora dokáže prijať číslo slova ako vstup, čím sa vyhneme vytváraniu veľkých one-hot kódovaných vektorov.

Použitím vstavanej vrstvy ako prvej vrstvy v našej klasifikačnej sieti môžeme prejsť z modelu bag-of-words na model **embedding bag**, kde najprv každé slovo v texte prevedieme na zodpovedajúcu vstavanú reprezentáciu a potom vypočítame nejakú agregačnú funkciu nad všetkými týmito reprezentáciami, ako napríklad `sum`, `average` alebo `max`.

![Obrázok znázorňujúci klasifikátor s použitím vstavanej reprezentácie pre päť slov v sekvencii.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.sk.png)

> Obrázok od autora

## ✍️ Cvičenia: Vstavané reprezentácie

Pokračujte v učení v nasledujúcich notebookoch:
* [Vstavané reprezentácie s PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Vstavané reprezentácie s TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Sémantické vstavané reprezentácie: Word2Vec

Hoci sa vstavaná vrstva naučila mapovať slová na vektorové reprezentácie, tieto reprezentácie nemusia nevyhnutne niesť veľa sémantického významu. Bolo by užitočné naučiť sa vektorovú reprezentáciu, kde podobné slová alebo synonymá zodpovedajú vektorom, ktoré sú si blízke podľa nejakej vektorovej vzdialenosti (napr. Euklidovskej vzdialenosti).

Na to potrebujeme predtrénovať náš model vstavanej reprezentácie na veľkej zbierke textov špecifickým spôsobom. Jedným zo spôsobov trénovania sémantických vstavaných reprezentácií je metóda [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Táto metóda je založená na dvoch hlavných architektúrach, ktoré sa používajú na vytváranie distribuovaných reprezentácií slov:

 - **Continuous bag-of-words** (CBoW) — v tejto architektúre trénujeme model na predpovedanie slova na základe okolitých slov v kontexte. Pri n-grame $(W_{-2},W_{-1},W_0,W_1,W_2)$ je cieľom modelu predpovedať $W_0$ na základe $(W_{-2},W_{-1},W_1,W_2)$.
 - **Continuous skip-gram** je opakom CBoW. Model používa okolitý kontextový rámec slov na predpovedanie aktuálneho slova.

CBoW je rýchlejší, zatiaľ čo skip-gram je pomalší, ale lepšie reprezentuje zriedkavé slová.

![Obrázok znázorňujúci algoritmy CBoW a Skip-Gram na prevod slov na vektory.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.sk.png)

> Obrázok z [tohto článku](https://arxiv.org/pdf/1301.3781.pdf)

Predtrénované vstavané reprezentácie Word2Vec (ako aj iné podobné modely, napríklad GloVe) môžu byť použité namiesto vstavanej vrstvy v neurónových sieťach. Musíme sa však vysporiadať so slovníkmi, pretože slovník použitý na predtrénovanie Word2Vec/GloVe sa pravdepodobne líši od slovníka v našom textovom korpuse. Pozrite si vyššie uvedené notebooky, aby ste zistili, ako tento problém vyriešiť.

## Kontextové vstavané reprezentácie

Jedným z hlavných obmedzení tradičných predtrénovaných vstavaných reprezentácií, ako je Word2Vec, je problém rozlíšenia významu slova. Hoci predtrénované vstavané reprezentácie dokážu zachytiť určitý význam slov v kontexte, každý možný význam slova je zakódovaný do tej istej reprezentácie. To môže spôsobiť problémy v následných modeloch, pretože mnohé slová, ako napríklad slovo „hrať“, majú rôzne významy v závislosti od kontextu, v ktorom sa používajú.

Napríklad slovo „hrať“ má v týchto dvoch vetách úplne odlišný význam:

- Išiel som na **hru** do divadla.
- Ján chce **hrať** so svojimi priateľmi.

Predtrénované vstavané reprezentácie vyššie reprezentujú oba tieto významy slova „hrať“ v tej istej reprezentácii. Na prekonanie tohto obmedzenia potrebujeme vytvoriť vstavané reprezentácie založené na **jazykovom modeli**, ktorý je trénovaný na veľkom korpuse textov a „vie“, ako sa slová môžu skladať v rôznych kontextoch. Diskusia o kontextových vstavaných reprezentáciách presahuje rámec tohto tutoriálu, ale vrátime sa k nim pri diskusii o jazykových modeloch neskôr v kurze.

## Záver

V tejto lekcii ste sa naučili, ako vytvárať a používať vstavané vrstvy v TensorFlow a PyTorch na lepšie vyjadrenie sémantického významu slov.

## 🚀 Výzva

Word2Vec bol použitý na niektoré zaujímavé aplikácie, vrátane generovania textov piesní a poézie. Pozrite si [tento článok](https://www.politetype.com/blog/word2vec-color-poems), ktorý popisuje, ako autor použil Word2Vec na generovanie poézie. Pozrite si aj [toto video od Dana Shiffmanna](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain), kde nájdete iné vysvetlenie tejto techniky. Potom sa pokúste aplikovať tieto techniky na svoj vlastný textový korpus, možno získaný z Kaggle.

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/28)

## Prehľad a samostatné štúdium

Prečítajte si tento článok o Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Úloha: Notebooky](assignment.md)

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.