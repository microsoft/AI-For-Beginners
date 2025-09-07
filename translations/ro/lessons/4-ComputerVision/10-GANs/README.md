<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-25T22:39:42+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "ro"
}
-->
# Rețele Generative Adversariale

În secțiunea anterioară, am învățat despre **modelele generative**: modele care pot genera imagini noi similare cu cele din setul de date de antrenament. VAE a fost un exemplu bun de model generativ.

## [Chestionar înainte de lecție](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Totuși, dacă încercăm să generăm ceva cu adevărat semnificativ, cum ar fi o pictură la o rezoluție rezonabilă, folosind VAE, vom observa că antrenamentul nu converge bine. Pentru acest caz de utilizare, ar trebui să învățăm despre o altă arhitectură specifică modelelor generative - **Rețele Generative Adversariale**, sau GAN-uri.

Ideea principală a unui GAN este să aibă două rețele neuronale care sunt antrenate una împotriva celeilalte:

<img src="images/gan_architecture.png" width="70%"/>

> Imagine de [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Un pic de vocabular:
> * **Generatorul** este o rețea care primește un vector aleator și produce o imagine ca rezultat.
> * **Discriminatorul** este o rețea care primește o imagine și trebuie să determine dacă este o imagine reală (din setul de date de antrenament) sau dacă a fost generată de un generator. Practic, este un clasificator de imagini.

### Discriminatorul

Arhitectura discriminatorului nu diferă de o rețea obișnuită de clasificare a imaginilor. În cel mai simplu caz, poate fi un clasificator complet conectat, dar cel mai probabil va fi o [rețea convoluțională](../07-ConvNets/README.md).

> ✅ Un GAN bazat pe rețele convoluționale se numește [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Un discriminator CNN constă din următoarele straturi: mai multe convoluții + pooling-uri (cu dimensiuni spațiale în scădere) și unul sau mai multe straturi complet conectate pentru a obține "vectorul de caracteristici", urmate de un clasificator binar final.

> ✅ Un 'pooling' în acest context este o tehnică ce reduce dimensiunea imaginii. "Straturile de pooling reduc dimensiunile datelor prin combinarea ieșirilor unor clustere de neuroni dintr-un strat într-un singur neuron în stratul următor." - [sursa](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generatorul

Un generator este puțin mai complicat. Îl puteți considera ca fiind un discriminator inversat. Pornind de la un vector latent (în locul unui vector de caracteristici), are un strat complet conectat pentru a-l converti în dimensiunea/forma necesară, urmat de deconvoluții + upscaling. Acest lucru este similar cu partea de *decodor* a unui [autoencoder](../09-Autoencoders/README.md).

> ✅ Deoarece stratul de convoluție este implementat ca un filtru liniar care parcurge imaginea, deconvoluția este esențial similară cu convoluția și poate fi implementată folosind aceeași logică de strat.

<img src="images/gan_arch_detail.png" width="70%"/>

> Imagine de [Dmitry Soshnikov](http://soshnikov.com)

### Antrenarea GAN-ului

GAN-urile sunt numite **adversariale** deoarece există o competiție constantă între generator și discriminator. În timpul acestei competiții, atât generatorul, cât și discriminatorul se îmbunătățesc, astfel încât rețeaua învață să producă imagini din ce în ce mai bune.

Antrenamentul are loc în două etape:

* **Antrenarea discriminatorului**. Această sarcină este destul de simplă: generăm un lot de imagini cu ajutorul generatorului, le etichetăm cu 0, ceea ce înseamnă imagine falsă, și luăm un lot de imagini din setul de date de intrare (cu eticheta 1, imagine reală). Obținem o *pierdere a discriminatorului* și efectuăm backpropagation.
* **Antrenarea generatorului**. Aceasta este puțin mai complicată, deoarece nu cunoaștem direct ieșirea așteptată pentru generator. Luăm întreaga rețea GAN formată dintr-un generator urmat de un discriminator, o alimentăm cu niște vectori aleatori și ne așteptăm ca rezultatul să fie 1 (corespunzător imaginilor reale). Apoi înghețăm parametrii discriminatorului (nu dorim să fie antrenat în acest pas) și efectuăm backpropagation.

În timpul acestui proces, pierderile generatorului și discriminatorului nu scad semnificativ. În situația ideală, acestea ar trebui să oscileze, corespunzând îmbunătățirii performanței ambelor rețele.

## ✍️ Exerciții: GAN-uri

* [Carnet GAN în TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [Carnet GAN în PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Probleme cu antrenarea GAN-urilor

GAN-urile sunt cunoscute pentru dificultatea lor de antrenare. Iată câteva probleme:

* **Colapsul modului**. Prin acest termen înțelegem că generatorul învață să producă o singură imagine de succes care păcălește discriminatorul, fără a genera o varietate de imagini diferite.
* **Sensibilitate la hiperparametri**. Adesea se poate observa că un GAN nu converge deloc, iar apoi o scădere bruscă a ratei de învățare duce la convergență.
* Menținerea unui **echilibru** între generator și discriminator. În multe cazuri, pierderea discriminatorului poate scădea la zero relativ repede, ceea ce face ca generatorul să nu mai poată fi antrenat. Pentru a depăși acest lucru, putem încerca să setăm rate de învățare diferite pentru generator și discriminator sau să sărim peste antrenamentul discriminatorului dacă pierderea este deja prea mică.
* Antrenarea pentru **rezoluție înaltă**. Reflectând aceeași problemă ca în cazul autoencoderelor, această problemă apare deoarece reconstruirea prea multor straturi ale unei rețele convoluționale duce la artefacte. Această problemă este de obicei rezolvată prin așa-numita **creștere progresivă**, în care mai întâi câteva straturi sunt antrenate pe imagini de rezoluție mică, iar apoi straturile sunt "deblocate" sau adăugate. O altă soluție ar fi adăugarea de conexiuni suplimentare între straturi și antrenarea mai multor rezoluții simultan - vedeți acest [articol despre GAN-uri cu gradient multi-scală](https://arxiv.org/abs/1903.06048) pentru detalii.

## Transfer de stil

GAN-urile sunt o metodă excelentă pentru a genera imagini artistice. O altă tehnică interesantă este așa-numitul **transfer de stil**, care ia o **imagine de conținut** și o re-desenază într-un stil diferit, aplicând filtre dintr-o **imagine de stil**.

Cum funcționează:
* Începem cu o imagine de zgomot aleator (sau cu o imagine de conținut, dar pentru înțelegere este mai ușor să începem cu zgomot aleator).
* Scopul nostru este să creăm o imagine care să fie apropiată atât de imaginea de conținut, cât și de imaginea de stil. Acest lucru este determinat de două funcții de pierdere:
   - **Pierderea de conținut** este calculată pe baza caracteristicilor extrase de CNN la anumite straturi din imaginea curentă și imaginea de conținut.
   - **Pierderea de stil** este calculată între imaginea curentă și imaginea de stil într-un mod inteligent folosind matrici Gram (mai multe detalii în [carnetul de exemplu](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)).
* Pentru a face imaginea mai netedă și a elimina zgomotul, introducem și **Pierderea de variație**, care calculează distanța medie între pixelii vecini.
* Bucla principală de optimizare ajustează imaginea curentă folosind gradient descent (sau un alt algoritm de optimizare) pentru a minimiza pierderea totală, care este o sumă ponderată a tuturor celor trei pierderi.

## ✍️ Exemplu: [Transfer de stil](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Chestionar după lecție](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Concluzie

În această lecție, ați învățat despre GAN-uri și cum să le antrenați. De asemenea, ați învățat despre provocările speciale pe care acest tip de rețea neuronală le poate întâmpina și câteva strategii pentru a le depăși.

## 🚀 Provocare

Parcurgeți [carnetul de Transfer de Stil](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) folosind propriile imagini.

## Recapitulare și studiu individual

Pentru referință, citiți mai multe despre GAN-uri în aceste resurse:

* Marco Pasini, [10 lecții învățate antrenând GAN-uri timp de un an](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), o arhitectură GAN *de facto* de luat în considerare
* [Crearea artei generative folosind GAN-uri pe Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Temă

Revedeți unul dintre cele două carnete asociate acestei lecții și reantrenați GAN-ul pe imaginile proprii. Ce puteți crea?

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.