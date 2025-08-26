<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-25T21:57:00+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "sl"
}
-->
# Modeliranje jezika

Semantične vektorske predstavitve, kot sta Word2Vec in GloVe, so pravzaprav prvi korak k **modeliranju jezika** – ustvarjanju modelov, ki na nek način *razumejo* (ali *predstavljajo*) naravo jezika.

## [Predhodni kviz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

Glavna ideja modeliranja jezika je, da jih učimo na nenalepčenih podatkovnih zbirkah na nenadzorovan način. To je pomembno, ker imamo na voljo ogromne količine nenalepčenega besedila, medtem ko je količina nalepčenega besedila vedno omejena z vloženim trudom za označevanje. Najpogosteje lahko zgradimo jezikovne modele, ki lahko **napovedujejo manjkajoče besede** v besedilu, saj je enostavno naključno besedo v besedilu zakriti in jo uporabiti kot učni vzorec.

## Učenje vektorskih predstavitev

V prejšnjih primerih smo uporabljali vnaprej naučene semantične vektorske predstavitve, vendar je zanimivo videti, kako lahko te predstavitve sami naučimo. Obstaja več možnih pristopov:

* **N-gram** modeliranje jezika, kjer napovedujemo token na podlagi N prejšnjih tokenov (N-gram).
* **Neprekinjena vreča besed** (CBoW), kjer napovedujemo sredinski token $W_0$ v zaporedju tokenov $W_{-N}$, ..., $W_N$.
* **Skip-gram**, kjer iz sredinskega tokena $W_0$ napovedujemo množico sosednjih tokenov {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$}.

![slika iz članka o pretvorbi besed v vektorje](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.sl.png)

> Slika iz [tega članka](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Primeri zvezkov: Učenje CBoW modela

Nadaljujte z učenjem v naslednjih zvezkih:

* [Učenje CBoW Word2Vec z uporabo TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Učenje CBoW Word2Vec z uporabo PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Zaključek

V prejšnji lekciji smo videli, da vektorske predstavitve besed delujejo skoraj čarobno! Zdaj vemo, da učenje vektorskih predstavitev besed ni zelo zapletena naloga, in če je potrebno, lahko sami naučimo svoje vektorske predstavitve za besedila iz specifičnih domen.

## [Naknadni kviz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Pregled in samostojno učenje

* [Uradni PyTorch vodič za modeliranje jezika](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Uradni TensorFlow vodič za učenje Word2Vec modela](https://www.TensorFlow.org/tutorials/text/word2vec).
* Uporaba ogrodja **gensim** za učenje najpogosteje uporabljenih vektorskih predstavitev v nekaj vrsticah kode je opisana [v tej dokumentaciji](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Naloga: Naučite Skip-Gram model](lab/README.md)

V laboratorijski nalogi vas izzivamo, da spremenite kodo iz te lekcije in naučite Skip-Gram model namesto CBoW. [Preberite podrobnosti](lab/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.