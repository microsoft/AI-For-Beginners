# Rețele Pre-antrenate și Învățarea prin Transfer

Antrenarea CNN-urilor poate dura mult timp și necesită o cantitate mare de date. Totuși, o mare parte din timp este petrecut în învățarea celor mai bune filtre de nivel scăzut pe care o rețea le poate folosi pentru a extrage modele din imagini. O întrebare naturală apare - putem folosi o rețea neuronală antrenată pe un set de date și să o adaptăm pentru a clasifica imagini diferite fără a necesita un proces complet de antrenare?

## [Chestionar înainte de lecție](https://ff-quizzes.netlify.app/en/ai/quiz/15)

Această abordare se numește **învățare prin transfer**, deoarece transferăm o parte din cunoștințele unui model de rețea neuronală către altul. În învățarea prin transfer, de obicei începem cu un model pre-antrenat, care a fost antrenat pe un set mare de imagini, cum ar fi **ImageNet**. Aceste modele pot deja să extragă caracteristici diferite din imagini generice, iar în multe cazuri, construirea unui clasificator pe baza acestor caracteristici extrase poate oferi un rezultat bun.

> ✅ Învățarea prin transfer este un termen întâlnit și în alte domenii academice, cum ar fi Educația. Se referă la procesul de aplicare a cunoștințelor dintr-un domeniu în altul.

## Modele Pre-antrenate ca Extractoare de Caracteristici

Rețelele convoluționale despre care am vorbit în secțiunea anterioară conțineau un număr de straturi, fiecare dintre ele fiind destinat să extragă anumite caracteristici din imagine, începând de la combinații de pixeli de nivel scăzut (cum ar fi linii orizontale/verticale sau trăsături), până la combinații de caracteristici de nivel înalt, corespunzătoare unor lucruri precum un ochi sau o flacără. Dacă antrenăm un CNN pe un set de date suficient de mare, cu imagini generice și diverse, rețeaua ar trebui să învețe să extragă aceste caracteristici comune.

Atât Keras, cât și PyTorch conțin funcții pentru a încărca cu ușurință greutăți pre-antrenate ale rețelelor neuronale pentru unele arhitecturi comune, majoritatea fiind antrenate pe imagini din ImageNet. Cele mai utilizate sunt descrise pe pagina [Arhitecturi CNN](../07-ConvNets/CNN_Architectures.md) din lecția anterioară. În special, poate fi util să folosiți una dintre următoarele:

* **VGG-16/VGG-19**, care sunt modele relativ simple, dar oferă o acuratețe bună. Deseori, utilizarea VGG ca primă încercare este o alegere bună pentru a vedea cum funcționează învățarea prin transfer.
* **ResNet** este o familie de modele propuse de Microsoft Research în 2015. Acestea au mai multe straturi și, prin urmare, necesită mai multe resurse.
* **MobileNet** este o familie de modele cu dimensiuni reduse, potrivite pentru dispozitive mobile. Folosiți-le dacă aveți resurse limitate și puteți sacrifica puțin din acuratețe.

Iată caracteristici extrase dintr-o imagine cu o pisică de către rețeaua VGG-16:

![Caracteristici extrase de VGG-16](../../../../../translated_images/ro/features.6291f9c7ba3a0b95.webp)

## Setul de Date Pisici vs. Câini

În acest exemplu, vom folosi un set de date cu [Pisici și Câini](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), care este foarte apropiat de un scenariu real de clasificare a imaginilor.

## ✍️ Exercițiu: Învățarea prin Transfer

Să vedem învățarea prin transfer în acțiune în caietele corespunzătoare:

* [Învățarea prin Transfer - PyTorch](TransferLearningPyTorch.ipynb)
* [Învățarea prin Transfer - TensorFlow](TransferLearningTF.ipynb)

## Vizualizarea Pisicii Adversariale

Rețeaua neuronală pre-antrenată conține diferite modele în "creierul" său, inclusiv noțiuni de **pisică ideală** (precum și câine ideal, zebră ideală etc.). Ar fi interesant să **vizualizăm această imagine**. Totuși, nu este simplu, deoarece modelele sunt răspândite în greutățile rețelei și sunt organizate într-o structură ierarhică.

O abordare pe care o putem adopta este să începem cu o imagine aleatorie și apoi să folosim tehnica de optimizare **gradient descent** pentru a ajusta acea imagine astfel încât rețeaua să înceapă să creadă că este o pisică.

![Buclă de Optimizare a Imaginilor](../../../../../translated_images/ro/ideal-cat-loop.999fbb8ff306e044.webp)

Totuși, dacă facem acest lucru, vom obține ceva foarte asemănător cu un zgomot aleatoriu. Acest lucru se întâmplă deoarece *există multe moduri prin care rețeaua poate crede că imaginea de intrare este o pisică*, inclusiv unele care nu au sens vizual. Deși aceste imagini conțin multe modele tipice pentru o pisică, nu există nimic care să le constrângă să fie distincte vizual.

Pentru a îmbunătăți rezultatul, putem adăuga un alt termen în funcția de pierdere, numit **pierdere de variație**. Este o metrică care arată cât de similari sunt pixelii vecini ai imaginii. Minimizarea pierderii de variație face imaginea mai netedă și elimină zgomotul - dezvăluind astfel modele mai atractive vizual. Iată un exemplu de astfel de imagini "ideale", care sunt clasificate ca pisică și ca zebră cu o probabilitate mare:

![Pisică Ideală](../../../../../translated_images/ro/ideal-cat.203dd4597643d6b0.webp) | ![Zebră Ideală](../../../../../translated_images/ro/ideal-zebra.7f70e8b54ee15a7a.webp)
-----|-----
 *Pisică Ideală* | *Zebră Ideală*

O abordare similară poate fi utilizată pentru a efectua așa-numitele **atacuri adversariale** asupra unei rețele neuronale. Să presupunem că dorim să păcălim o rețea neuronală și să facem un câine să arate ca o pisică. Dacă luăm imaginea unui câine, care este recunoscută de rețea ca fiind un câine, putem apoi să o ajustăm puțin folosind optimizarea gradient descent, până când rețeaua începe să o clasifice ca fiind o pisică:

![Imaginea unui Câine](../../../../../translated_images/ro/original-dog.8f68a67d2fe0911f.webp) | ![Imaginea unui câine clasificat ca pisică](../../../../../translated_images/ro/adversarial-dog.d9fc7773b0142b89.webp)
-----|-----
*Imagine originală a unui câine* | *Imaginea unui câine clasificat ca pisică*

Consultați codul pentru a reproduce rezultatele de mai sus în următorul caiet:

* [Pisică Ideală și Adversarială - TensorFlow](AdversarialCat_TF.ipynb)

## Concluzie

Folosind învățarea prin transfer, puteți crea rapid un clasificator pentru o sarcină personalizată de clasificare a obiectelor și obține o acuratețe ridicată. Puteți observa că sarcinile mai complexe pe care le rezolvăm acum necesită o putere de calcul mai mare și nu pot fi rezolvate ușor pe CPU. În unitatea următoare, vom încerca să folosim o implementare mai ușoară pentru a antrena același model folosind resurse de calcul mai reduse, ceea ce duce la o acuratețe doar ușor mai scăzută.

## 🚀 Provocare

În caietele însoțitoare, există note la final despre cum funcționează cel mai bine transferul de cunoștințe cu date de antrenament oarecum similare (poate un nou tip de animal). Faceți câteva experimente cu tipuri complet noi de imagini pentru a vedea cât de bine sau prost performează modelele voastre de transfer de cunoștințe.

## [Chestionar după lecție](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Recapitulare și Studiu Individual

Citiți [TrainingTricks.md](TrainingTricks.md) pentru a aprofunda cunoștințele despre alte moduri de a vă antrena modelele.

## [Temă](lab/README.md)

În acest laborator, vom folosi setul de date real [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) cu 35 de rase de pisici și câini și vom construi un clasificator bazat pe învățarea prin transfer.

---

