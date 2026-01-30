# Jezikovno modeliranje

Semantične vektorske predstavitve, kot sta Word2Vec in GloVe, so pravzaprav prvi korak k **jezikovnemu modeliranju** – ustvarjanju modelov, ki nekako *razumejo* (ali *predstavljajo*) naravo jezika.

## [Predhodni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Glavna ideja jezikovnega modeliranja je, da jih treniramo na nenalepčenih podatkovnih nizih na nesuperviziran način. To je pomembno, ker imamo na voljo ogromne količine nenalepčenega besedila, medtem ko je količina nalepčenega besedila vedno omejena z vloženim trudom pri označevanju. Najpogosteje lahko zgradimo jezikovne modele, ki lahko **napovedujejo manjkajoče besede** v besedilu, saj je enostavno naključno besedo v besedilu zakriti in jo uporabiti kot učni vzorec.

## Učenje vektorskih predstavitev

V prejšnjih primerih smo uporabljali že vnaprej naučene semantične vektorske predstavitve, vendar je zanimivo videti, kako lahko te predstavitve treniramo. Obstaja več možnih pristopov:

* **N-gram** jezikovno modeliranje, kjer napovedujemo token z upoštevanjem N prejšnjih tokenov (N-gram).
* **Neprekinjena vreča besed** (CBoW), kjer napovedujemo srednji token $W_0$ v zaporedju tokenov $W_{-N}$, ..., $W_N$.
* **Skip-gram**, kjer napovedujemo niz sosednjih tokenov {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} iz srednjega tokena $W_0$.

![slika iz članka o pretvorbi besed v vektorje](../../../../../translated_images/sl/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Slika iz [tega članka](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Primeri zvezkov: Učenje CBoW modela

Nadaljujte z učenjem v naslednjih zvezkih:

* [Učenje CBoW Word2Vec z TensorFlow](CBoW-TF.ipynb)
* [Učenje CBoW Word2Vec z PyTorch](CBoW-PyTorch.ipynb)

## Zaključek

V prejšnji lekciji smo videli, da vektorske predstavitve besed delujejo kot čarovnija! Zdaj vemo, da učenje vektorskih predstavitev besed ni zelo zapletena naloga, in bi morali biti sposobni naučiti svoje vektorske predstavitve za besedila specifična za določeno področje, če je to potrebno.

## [Naknadni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Pregled in samostojno učenje

* [Uradni PyTorch vodič o jezikovnem modeliranju](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Uradni TensorFlow vodič o učenju Word2Vec modela](https://www.TensorFlow.org/tutorials/text/word2vec).
* Uporaba ogrodja **gensim** za učenje najpogosteje uporabljenih vektorskih predstavitev v nekaj vrsticah kode je opisana [v tej dokumentaciji](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Naloga: Naučite Skip-Gram model](lab/README.md)

V laboratoriju vas izzivamo, da spremenite kodo iz te lekcije in naučite Skip-Gram model namesto CBoW. [Preberite podrobnosti](lab/README.md)

---

