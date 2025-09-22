<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-25T22:34:28+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "ro"
}
-->
# Segmentare

Am învățat anterior despre Detectarea Obiectelor, care ne permite să localizăm obiecte în imagine prin prezicerea *casetelor de delimitare*. Totuși, pentru unele sarcini, nu avem nevoie doar de casete de delimitare, ci și de o localizare mai precisă a obiectelor. Această sarcină se numește **segmentare**.

## [Chestionar înainte de lecție](https://ff-quizzes.netlify.app/en/ai/quiz/23)

Segmentarea poate fi privită ca o **clasificare a pixelilor**, în care pentru **fiecare** pixel al imaginii trebuie să prezicem clasa sa (*fundalul* fiind una dintre clase). Există două algoritmi principali de segmentare:

* **Segmentarea semantică** indică doar clasa pixelului, fără a face distincție între diferite obiecte din aceeași clasă.
* **Segmentarea pe instanțe** împarte clasele în instanțe diferite.

De exemplu, pentru segmentarea pe instanțe, aceste oi sunt obiecte diferite, dar pentru segmentarea semantică toate oile sunt reprezentate de o singură clasă.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Imagine din [acest articol de blog](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Există diferite arhitecturi neuronale pentru segmentare, dar toate au aceeași structură. Într-un fel, este similar cu autoencoder-ul despre care ai învățat anterior, dar în loc să deconstruim imaginea originală, scopul nostru este să deconstruim o **mască**. Astfel, o rețea de segmentare are următoarele părți:

* **Encoder** extrage caracteristici din imaginea de intrare.
* **Decoder** transformă aceste caracteristici în **imaginea măștii**, cu aceeași dimensiune și un număr de canale corespunzător numărului de clase.

<img src="images/segm.png" width="80%">

> Imagine din [această publicație](https://arxiv.org/pdf/2001.05566.pdf)

Trebuie să menționăm în mod special funcția de pierdere utilizată pentru segmentare. Când folosim autoencodere clasice, trebuie să măsurăm similaritatea dintre două imagini, iar pentru aceasta putem folosi eroarea pătratică medie (MSE). În segmentare, fiecare pixel din imaginea țintă a măștii reprezintă numărul clasei (codificat one-hot pe a treia dimensiune), așa că trebuie să folosim funcții de pierdere specifice clasificării - pierderea cross-entropy, mediată pe toți pixelii. Dacă masca este binară, se folosește **binary cross-entropy loss** (BCE).

> ✅ Codificarea one-hot este o metodă de a codifica o etichetă de clasă într-un vector de lungime egală cu numărul de clase. Consultă [acest articol](https://datagy.io/sklearn-one-hot-encode/) pentru mai multe detalii despre această tehnică.

## Segmentarea în Imagistica Medicală

În această lecție, vom vedea segmentarea în acțiune, antrenând o rețea pentru a recunoaște nevi umani (cunoscuți și sub numele de alunițe) în imagini medicale. Vom folosi <a href="https://www.fc.up.pt/addi/ph2%20database.html">Baza de Date PH<sup>2</sup></a> de imagini dermatoscopice ca sursă de imagini. Acest set de date conține 200 de imagini din trei clase: nev tipic, nev atipic și melanom. Toate imaginile conțin, de asemenea, o **mască** corespunzătoare care conturează nevul.

> ✅ Această tehnică este deosebit de potrivită pentru acest tip de imagistică medicală, dar ce alte aplicații din lumea reală ai putea imagina?

<img alt="navi" src="images/navi.png"/>

> Imagine din Baza de Date PH<sup>2</sup>

Vom antrena un model pentru a segmenta orice nev din fundalul său.

## ✍️ Exerciții: Segmentare Semantică

Deschide notebook-urile de mai jos pentru a învăța mai multe despre diferite arhitecturi de segmentare semantică, pentru a exersa lucrul cu ele și pentru a le vedea în acțiune.

* [Segmentare Semantică Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Segmentare Semantică TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Chestionar după lecție](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Concluzie

Segmentarea este o tehnică foarte puternică pentru clasificarea imaginilor, mergând dincolo de casetele de delimitare până la clasificarea la nivel de pixel. Este o tehnică utilizată în imagistica medicală, printre alte aplicații.

## 🚀 Provocare

Segmentarea corpului este doar una dintre sarcinile comune pe care le putem realiza cu imagini ale oamenilor. Alte sarcini importante includ **detectarea scheletului** și **detectarea posturii**. Încearcă biblioteca [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) pentru a vedea cum poate fi utilizată detectarea posturii.

## Recapitulare și Studiu Individual

Acest [articol de pe Wikipedia](https://wikipedia.org/wiki/Image_segmentation) oferă o bună prezentare generală a diferitelor aplicații ale acestei tehnici. Află mai multe pe cont propriu despre subdomeniile Segmentării pe Instanțe și Segmentării Panoptice în acest domeniu de cercetare.

## [Temă](lab/README.md)

În acest laborator, încearcă **segmentarea corpului uman** folosind [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) de pe Kaggle.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.