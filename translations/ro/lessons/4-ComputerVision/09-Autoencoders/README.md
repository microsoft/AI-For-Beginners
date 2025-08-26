<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-25T22:30:06+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "ro"
}
-->
# Autoencodere

Când antrenăm CNN-uri, una dintre probleme este că avem nevoie de o cantitate mare de date etichetate. În cazul clasificării imaginilor, trebuie să separăm imaginile în clase diferite, ceea ce necesită un efort manual.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

Totuși, am putea dori să folosim date brute (neetichetate) pentru a antrena extractoare de caracteristici CNN, ceea ce se numește **învățare auto-supervizată**. În loc de etichete, vom folosi imaginile de antrenament atât ca intrare, cât și ca ieșire pentru rețea. Ideea principală a unui **autoencoder** este că vom avea o **rețea encoder** care transformă imaginea de intrare într-un spațiu **latent** (de obicei, este doar un vector de dimensiune mai mică), apoi o **rețea decoder**, al cărei scop este să reconstruiască imaginea originală.

> ✅ Un [autoencoder](https://wikipedia.org/wiki/Autoencoder) este „un tip de rețea neuronală artificială utilizată pentru a învăța codificări eficiente ale datelor neetichetate.”

Deoarece antrenăm un autoencoder pentru a captura cât mai multe informații din imaginea originală pentru o reconstrucție precisă, rețeaua încearcă să găsească cea mai bună **reprezentare** a imaginilor de intrare pentru a surprinde semnificația acestora.

![AutoEncoder Diagram](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.ro.jpg)

> Imagine de pe [blogul Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

## Scenarii pentru utilizarea Autoencoderelor

Deși reconstrucția imaginilor originale nu pare utilă în sine, există câteva scenarii în care autoencoderele sunt deosebit de utile:

* **Reducerea dimensiunii imaginilor pentru vizualizare** sau **antrenarea reprezentărilor imaginilor**. De obicei, autoencoderele oferă rezultate mai bune decât PCA, deoarece iau în considerare natura spațială a imaginilor și caracteristicile ierarhice.
* **Eliminarea zgomotului**, adică eliminarea zgomotului din imagine. Deoarece zgomotul conține multe informații inutile, autoencoderul nu poate încadra totul într-un spațiu latent relativ mic și, astfel, surprinde doar partea importantă a imaginii. Când antrenăm eliminatoare de zgomot, pornim de la imagini originale și folosim imagini cu zgomot adăugat artificial ca intrare pentru autoencoder.
* **Super-rezoluție**, creșterea rezoluției imaginilor. Pornim de la imagini de înaltă rezoluție și folosim imaginea cu rezoluție mai mică ca intrare pentru autoencoder.
* **Modele generative**. Odată ce antrenăm autoencoderul, partea de decoder poate fi utilizată pentru a crea noi obiecte pornind de la vectori latenti aleatori.

## Autoencodere Variationale (VAE)

Autoencoderele tradiționale reduc dimensiunea datelor de intrare într-un mod oarecare, identificând caracteristicile importante ale imaginilor de intrare. Totuși, vectorii latenti deseori nu au o semnificație clară. Cu alte cuvinte, luând ca exemplu dataset-ul MNIST, identificarea cifrelor corespunzătoare diferiților vectori latenti nu este o sarcină ușoară, deoarece vectorii latenti apropiați nu corespund neapărat acelorași cifre.

Pe de altă parte, pentru a antrena modele *generative*, este mai bine să avem o înțelegere a spațiului latent. Această idee ne conduce la **autoencoderul variational** (VAE).

VAE este un autoencoder care învață să prezică *distribuția statistică* a parametrilor latenti, așa-numita **distribuție latentă**. De exemplu, am putea dori ca vectorii latenti să fie distribuiți normal cu o medie z<sub>mean</sub> și o deviație standard z<sub>sigma</sub> (atât media, cât și deviația standard sunt vectori de o anumită dimensiune d). Encoderul din VAE învață să prezică acești parametri, iar decoderul ia un vector aleator din această distribuție pentru a reconstrui obiectul.

Pentru a rezuma:

 * Din vectorul de intrare, prezicem `z_mean` și `z_log_sigma` (în loc să prezicem deviația standard în sine, prezicem logaritmul acesteia)
 * Extragem un vector `sample` din distribuția N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * Decoderul încearcă să decodeze imaginea originală folosind `sample` ca vector de intrare

 <img src="images/vae.png" width="50%">

> Imagine din [acest articol](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) de Isaak Dykeman

Autoencoderele variationale folosesc o funcție de pierdere complexă care constă din două părți:

* **Pierdere de reconstrucție** este funcția de pierdere care arată cât de apropiată este imaginea reconstruită de țintă (poate fi Mean Squared Error sau MSE). Este aceeași funcție de pierdere ca în autoencoderele normale.
* **Pierdere KL**, care asigură că distribuțiile variabilelor latente rămân apropiate de distribuția normală. Se bazează pe noțiunea de [divergență Kullback-Leibler](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - o metrică pentru a estima cât de similare sunt două distribuții statistice.

Un avantaj important al VAE-urilor este că permit generarea de imagini noi relativ ușor, deoarece știm din ce distribuție să extragem vectorii latenti. De exemplu, dacă antrenăm un VAE cu vector latent 2D pe MNIST, putem varia componentele vectorului latent pentru a obține cifre diferite:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Imagine de [Dmitry Soshnikov](http://soshnikov.com)

Observați cum imaginile se îmbină între ele, pe măsură ce începem să obținem vectori latenti din diferite porțiuni ale spațiului parametrilor latenti. De asemenea, putem vizualiza acest spațiu în 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Imagine de [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Exerciții: Autoencodere

Aflați mai multe despre autoencodere în aceste notebook-uri corespunzătoare:

* [Autoencodere în TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoencodere în PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Proprietăți ale Autoencoderelor

* **Specifice datelor** - funcționează bine doar cu tipul de imagini pe care au fost antrenate. De exemplu, dacă antrenăm o rețea de super-rezoluție pe flori, aceasta nu va funcționa bine pe portrete. Acest lucru se datorează faptului că rețeaua poate produce imagini de rezoluție mai mare prin preluarea detaliilor fine din caracteristicile învățate din setul de date de antrenament.
* **Pierdere de informație** - imaginea reconstruită nu este aceeași cu imaginea originală. Natura pierderii este definită de *funcția de pierdere* utilizată în timpul antrenamentului.
* Funcționează pe **date neetichetate**

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## Concluzie

În această lecție, ați învățat despre diferitele tipuri de autoencodere disponibile pentru cercetătorii AI. Ați învățat cum să le construiți și cum să le utilizați pentru a reconstrui imagini. De asemenea, ați învățat despre VAE și cum să le utilizați pentru a genera imagini noi.

## 🚀 Provocare

În această lecție, ați învățat despre utilizarea autoencoderelor pentru imagini. Dar ele pot fi folosite și pentru muzică! Consultați proiectul Magenta [MusicVAE](https://magenta.tensorflow.org/music-vae), care folosește autoencodere pentru a învăța să reconstruiască muzică. Faceți câteva [experimente](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) cu această bibliotecă pentru a vedea ce puteți crea.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Recapitulare & Studiu Individual

Pentru referință, citiți mai multe despre autoencodere în aceste resurse:

* [Construirea Autoencoderelor în Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Articol pe NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Autoencodere Variationale Explicate](https://kvfrans.com/variational-autoencoders-explained/)
* [Autoencodere Variationale Condiționale](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Temă

La sfârșitul [acestui notebook folosind TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb), veți găsi o „sarcină” - folosiți aceasta ca temă.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.