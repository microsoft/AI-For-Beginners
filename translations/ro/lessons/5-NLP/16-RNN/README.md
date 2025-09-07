<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-25T21:33:18+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "ro"
}
-->
# Rețele Neuronale Recurente

## [Chestionar înainte de curs](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

În secțiunile anterioare, am utilizat reprezentări semantice bogate ale textului și un clasificator liniar simplu deasupra acestor embedding-uri. Această arhitectură captează sensul agregat al cuvintelor dintr-o propoziție, dar nu ia în considerare **ordinea** cuvintelor, deoarece operația de agregare deasupra embedding-urilor elimină această informație din textul original. Deoarece aceste modele nu pot modela ordonarea cuvintelor, ele nu pot rezolva sarcini mai complexe sau ambigue, cum ar fi generarea de text sau răspunsul la întrebări.

Pentru a capta sensul unei secvențe de text, trebuie să utilizăm o altă arhitectură de rețea neuronală, numită **rețea neuronală recurentă**, sau RNN. În RNN, trecem propoziția prin rețea un simbol la un moment dat, iar rețeaua produce un **statut**, pe care îl trecem din nou prin rețea împreună cu următorul simbol.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.ro.png)

> Imagine realizată de autor

Având secvența de intrare de tokeni X<sub>0</sub>,...,X<sub>n</sub>, RNN creează o secvență de blocuri de rețea neuronală și antrenează această secvență cap-coadă folosind backpropagation. Fiecare bloc de rețea primește o pereche (X<sub>i</sub>,S<sub>i</sub>) ca intrare și produce S<sub>i+1</sub> ca rezultat. Statutul final S<sub>n</sub> sau (ieșirea Y<sub>n</sub>) este transmis unui clasificator liniar pentru a produce rezultatul. Toate blocurile de rețea împărtășesc aceleași greutăți și sunt antrenate cap-coadă folosind o singură trecere de backpropagation.

Deoarece vectorii de statut S<sub>0</sub>,...,S<sub>n</sub> sunt trecuți prin rețea, aceasta poate învăța dependențele secvențiale dintre cuvinte. De exemplu, atunci când cuvântul *nu* apare undeva în secvență, rețeaua poate învăța să nege anumite elemente din vectorul de statut, rezultând o negare.

> ✅ Deoarece greutățile tuturor blocurilor RNN din imaginea de mai sus sunt împărtășite, aceeași imagine poate fi reprezentată ca un singur bloc (în dreapta) cu un circuit de feedback recurent, care transmite statutul de ieșire al rețelei înapoi la intrare.

## Anatomia unei Celule RNN

Să vedem cum este organizată o celulă RNN simplă. Aceasta acceptă statutul anterior S<sub>i-1</sub> și simbolul curent X<sub>i</sub> ca intrări și trebuie să producă statutul de ieșire S<sub>i</sub> (și, uneori, ne interesează și o altă ieșire Y<sub>i</sub>, ca în cazul rețelelor generative).

O celulă RNN simplă are două matrici de greutăți interne: una transformă un simbol de intrare (să o numim W), iar cealaltă transformă un statut de intrare (H). În acest caz, ieșirea rețelei este calculată ca σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), unde σ este funcția de activare și b este un bias suplimentar.

<img alt="Anatomia unei celule RNN" src="images/rnn-anatomy.png" width="50%"/>

> Imagine realizată de autor

În multe cazuri, tokenii de intrare sunt trecuți prin stratul de embedding înainte de a intra în RNN pentru a reduce dimensionalitatea. În acest caz, dacă dimensiunea vectorilor de intrare este *emb_size*, iar vectorul de statut este *hid_size* - dimensiunea lui W este *emb_size*×*hid_size*, iar dimensiunea lui H este *hid_size*×*hid_size*.

## Memorie pe Termen Lung și Scurt (LSTM)

Una dintre principalele probleme ale RNN-urilor clasice este așa-numita problemă a **gradientelor care dispar**. Deoarece RNN-urile sunt antrenate cap-coadă într-o singură trecere de backpropagation, este dificil să se propage eroarea către primele straturi ale rețelei, iar astfel rețeaua nu poate învăța relații între tokeni distanți. Una dintre modalitățile de a evita această problemă este introducerea **gestionării explicite a statutului** prin utilizarea așa-numitelor **porți**. Există două arhitecturi bine cunoscute de acest tip: **Memorie pe Termen Lung și Scurt** (LSTM) și **Unitatea de Releu Gated** (GRU).

![Imagine care arată un exemplu de celulă LSTM](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Sursa imaginii TBD

Rețeaua LSTM este organizată într-un mod similar cu RNN, dar există două stări care sunt transmise de la un strat la altul: statutul actual C și vectorul ascuns H. La fiecare unitate, vectorul ascuns H<sub>i</sub> este concatenat cu intrarea X<sub>i</sub>, iar acestea controlează ceea ce se întâmplă cu statutul C prin intermediul **porților**. Fiecare poartă este o rețea neuronală cu activare sigmoid (ieșire în intervalul [0,1]), care poate fi considerată ca o mască bitwise atunci când este înmulțită cu vectorul de statut. Există următoarele porți (de la stânga la dreapta în imaginea de mai sus):

* **Poarta de uitare** ia un vector ascuns și determină ce componente ale vectorului C trebuie uitate și care trebuie transmise mai departe.
* **Poarta de intrare** ia informații din vectorii de intrare și ascunși și le inserează în statut.
* **Poarta de ieșire** transformă statutul printr-un strat liniar cu activare *tanh*, apoi selectează unele dintre componentele sale folosind vectorul ascuns H<sub>i</sub> pentru a produce un nou statut C<sub>i+1</sub>.

Componentele statutului C pot fi considerate ca niște semnale care pot fi activate sau dezactivate. De exemplu, atunci când întâlnim un nume *Alice* în secvență, putem presupune că se referă la un personaj feminin și activăm semnalul în statut că avem un substantiv feminin în propoziție. Când întâlnim ulterior expresia *și Tom*, vom activa semnalul că avem un substantiv plural. Astfel, prin manipularea statutului, putem presupune că urmărim proprietățile gramaticale ale părților propoziției.

> ✅ O resursă excelentă pentru înțelegerea detaliilor interne ale LSTM este acest articol minunat [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) de Christopher Olah.

## RNN-uri Bidirecționale și Multistrat

Am discutat despre rețelele recurente care operează într-o singură direcție, de la începutul unei secvențe până la sfârșit. Pare natural, deoarece seamănă cu modul în care citim și ascultăm vorbirea. Totuși, deoarece în multe cazuri practice avem acces aleatoriu la secvența de intrare, ar putea avea sens să rulăm calculul recurent în ambele direcții. Astfel de rețele se numesc **RNN-uri bidirecționale**. Când lucrăm cu o rețea bidirecțională, vom avea nevoie de doi vectori de statut ascuns, câte unul pentru fiecare direcție.

O rețea recurentă, fie unidirecțională, fie bidirecțională, captează anumite modele dintr-o secvență și le poate stoca într-un vector de statut sau le poate transmite ca ieșire. La fel ca în cazul rețelelor convoluționale, putem construi un alt strat recurent deasupra primului pentru a capta modele de nivel superior și a construi din modelele de nivel inferior extrase de primul strat. Acest lucru ne conduce la noțiunea de **RNN multistrat**, care constă din două sau mai multe rețele recurente, unde ieșirea stratului anterior este transmisă stratului următor ca intrare.

![Imagine care arată un RNN multistrat cu LSTM](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.ro.jpg)

*Imagine din [acest articol minunat](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) de Fernando López*

## ✍️ Exerciții: Embedding-uri

Continuă învățarea în următoarele notebook-uri:

* [RNN-uri cu PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNN-uri cu TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Concluzie

În această unitate, am văzut că RNN-urile pot fi utilizate pentru clasificarea secvențelor, dar de fapt, ele pot gestiona multe alte sarcini, cum ar fi generarea de text, traducerea automată și altele. Vom analiza aceste sarcini în unitatea următoare.

## 🚀 Provocare

Citește literatură despre LSTM-uri și ia în considerare aplicațiile lor:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Chestionar după curs](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Recapitulare și Studiu Individual

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) de Christopher Olah.

## [Temă: Notebook-uri](assignment.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.