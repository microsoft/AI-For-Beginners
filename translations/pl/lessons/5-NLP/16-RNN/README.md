<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-24T10:12:39+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "pl"
}
-->
# Recurrent Neural Networks

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/31)

W poprzednich sekcjach korzystaliśmy z bogatych semantycznych reprezentacji tekstu oraz prostego klasyfikatora liniowego na bazie osadzeń. Taka architektura pozwala uchwycić zagregowane znaczenie słów w zdaniu, ale nie uwzględnia **kolejności** słów, ponieważ operacja agregacji na osadzeniach usuwa tę informację z oryginalnego tekstu. Z tego powodu modele te nie są w stanie modelować kolejności słów, co uniemożliwia im rozwiązywanie bardziej złożonych lub niejednoznacznych zadań, takich jak generowanie tekstu czy odpowiadanie na pytania.

Aby uchwycić znaczenie sekwencji tekstu, musimy użyć innej architektury sieci neuronowej, zwanej **rekurencyjną siecią neuronową** (RNN). W RNN przekazujemy nasze zdanie przez sieć symbol po symbolu, a sieć generuje pewien **stan**, który następnie przekazujemy do sieci wraz z kolejnym symbolem.

![RNN](../../../../../lessons/5-NLP/16-RNN/images/rnn.png)

> Obraz autorstwa autora

Dla wejściowej sekwencji tokenów X<sub>0</sub>,...,X<sub>n</sub>, RNN tworzy sekwencję bloków sieci neuronowej i trenuje tę sekwencję end-to-end za pomocą propagacji wstecznej. Każdy blok sieci przyjmuje parę (X<sub>i</sub>,S<sub>i</sub>) jako wejście i generuje S<sub>i+1</sub> jako wynik. Końcowy stan S<sub>n</sub> lub (wyjście Y<sub>n</sub>) trafia do klasyfikatora liniowego, aby wygenerować wynik. Wszystkie bloki sieci mają te same wagi i są trenowane end-to-end za pomocą jednej propagacji wstecznej.

Dzięki temu, że wektory stanów S<sub>0</sub>,...,S<sub>n</sub> są przekazywane przez sieć, jest ona w stanie nauczyć się zależności sekwencyjnych między słowami. Na przykład, gdy słowo *not* pojawia się gdzieś w sekwencji, sieć może nauczyć się negować pewne elementy wektora stanu, co prowadzi do negacji.

> ✅ Ponieważ wagi wszystkich bloków RNN na powyższym obrazku są wspólne, ten sam obrazek można przedstawić jako jeden blok (po prawej) z pętlą sprzężenia zwrotnego, która przekazuje wyjściowy stan sieci z powrotem na wejście.

## Anatomia komórki RNN

Przyjrzyjmy się, jak zorganizowana jest prosta komórka RNN. Przyjmuje ona poprzedni stan S<sub>i-1</sub> oraz bieżący symbol X<sub>i</sub> jako wejścia i musi wygenerować wyjściowy stan S<sub>i</sub> (a czasami interesuje nas również inne wyjście Y<sub>i</sub>, jak w przypadku sieci generatywnych).

Prosta komórka RNN ma wewnątrz dwie macierze wag: jedna przekształca symbol wejściowy (nazwijmy ją W), a druga przekształca stan wejściowy (H). W takim przypadku wyjście sieci obliczane jest jako σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), gdzie σ to funkcja aktywacji, a b to dodatkowe przesunięcie.

<img alt="Anatomia komórki RNN" src="images/rnn-anatomy.png" width="50%"/>

> Obraz autorstwa autora

W wielu przypadkach tokeny wejściowe są przekazywane przez warstwę osadzeń przed wejściem do RNN, aby zmniejszyć wymiarowość. W takim przypadku, jeśli wymiar wektorów wejściowych to *emb_size*, a wektor stanu to *hid_size* - rozmiar W wynosi *emb_size*×*hid_size*, a rozmiar H wynosi *hid_size*×*hid_size*.

## Long Short Term Memory (LSTM)

Jednym z głównych problemów klasycznych RNN jest tzw. **problem zanikających gradientów**. Ponieważ RNN są trenowane end-to-end w jednej propagacji wstecznej, mają trudności z propagowaniem błędu do pierwszych warstw sieci, co uniemożliwia sieci naukę relacji między odległymi tokenami. Jednym ze sposobów uniknięcia tego problemu jest wprowadzenie **jawnego zarządzania stanem** za pomocą tzw. **bramek**. Istnieją dwie dobrze znane architektury tego typu: **Long Short Term Memory** (LSTM) oraz **Gated Relay Unit** (GRU).

![Obraz przedstawiający przykład komórki LSTM](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Źródło obrazu TBD

Sieć LSTM jest zorganizowana w sposób podobny do RNN, ale istnieją dwa stany, które są przekazywane z warstwy do warstwy: rzeczywisty stan C oraz ukryty wektor H. W każdej jednostce ukryty wektor H<sub>i</sub> jest konkatenowany z wejściem X<sub>i</sub>, a one kontrolują, co dzieje się ze stanem C za pomocą **bramek**. Każda bramka to sieć neuronowa z aktywacją sigmoid (wyjście w zakresie [0,1]), którą można traktować jako maskę bitową przy mnożeniu przez wektor stanu. Na obrazku powyżej znajdują się następujące bramki (od lewej do prawej):

* **Bramka zapominania** bierze ukryty wektor i określa, które komponenty wektora C należy zapomnieć, a które przekazać dalej.
* **Bramka wejściowa** pobiera pewne informacje z wejścia i ukrytych wektorów i wprowadza je do stanu.
* **Bramka wyjściowa** przekształca stan za pomocą warstwy liniowej z aktywacją *tanh*, a następnie wybiera niektóre z jego komponentów za pomocą ukrytego wektora H<sub>i</sub>, aby wygenerować nowy stan C<sub>i+1</sub>.

Komponenty stanu C można traktować jako pewne flagi, które można włączać i wyłączać. Na przykład, gdy w sekwencji napotkamy imię *Alice*, możemy założyć, że odnosi się ono do postaci kobiecej i podnieść flagę w stanie, że mamy rzeczownik żeński w zdaniu. Gdy dalej napotkamy frazę *and Tom*, podniesiemy flagę, że mamy rzeczownik w liczbie mnogiej. W ten sposób manipulując stanem możemy teoretycznie śledzić właściwości gramatyczne części zdania.

> ✅ Doskonałym źródłem do zrozumienia wewnętrznego działania LSTM jest ten świetny artykuł [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) autorstwa Christophera Olaha.

## Dwukierunkowe i wielowarstwowe RNN

Omówiliśmy sieci rekurencyjne, które działają w jednym kierunku, od początku sekwencji do końca. Wydaje się to naturalne, ponieważ przypomina sposób, w jaki czytamy i słuchamy mowy. Jednakże, ponieważ w wielu praktycznych przypadkach mamy losowy dostęp do sekwencji wejściowej, może mieć sens uruchomienie obliczeń rekurencyjnych w obu kierunkach. Takie sieci nazywane są **dwukierunkowymi** RNN. W przypadku sieci dwukierunkowej potrzebne będą dwa ukryte wektory stanu, po jednym dla każdego kierunku.

Sieć rekurencyjna, jedno- lub dwukierunkowa, wychwytuje pewne wzorce w sekwencji i może je przechowywać w wektorze stanu lub przekazywać na wyjście. Podobnie jak w przypadku sieci konwolucyjnych, możemy zbudować kolejną warstwę rekurencyjną na szczycie pierwszej, aby uchwycić wzorce wyższego poziomu i budować na bazie wzorców niskiego poziomu wyodrębnionych przez pierwszą warstwę. Prowadzi to do pojęcia **wielowarstwowego RNN**, który składa się z dwóch lub więcej sieci rekurencyjnych, gdzie wyjście poprzedniej warstwy jest przekazywane do następnej warstwy jako wejście.

![Obraz przedstawiający wielowarstwowy LSTM RNN](../../../../../lessons/5-NLP/16-RNN/images/multi-layer-lstm.jpg)

*Obraz z [tego wspaniałego artykułu](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) autorstwa Fernando Lópeza*

## ✍️ Ćwiczenia: Osadzenia

Kontynuuj naukę w poniższych notatnikach:

* [RNNs with PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNNs with TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Podsumowanie

W tej jednostce zobaczyliśmy, że RNN mogą być używane do klasyfikacji sekwencji, ale w rzeczywistości mogą obsługiwać wiele innych zadań, takich jak generowanie tekstu, tłumaczenie maszynowe i inne. Rozważymy te zadania w następnej jednostce.

## 🚀 Wyzwanie

Przeczytaj literaturę na temat LSTM i rozważ ich zastosowania:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/32)

## Przegląd i samodzielna nauka

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) autorstwa Christophera Olaha.

## [Zadanie: Notatniki](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.