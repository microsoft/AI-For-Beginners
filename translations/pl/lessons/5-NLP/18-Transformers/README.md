<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7e617f0b8de85a43957a853aba09bfeb",
  "translation_date": "2025-08-24T10:18:50+00:00",
  "source_file": "lessons/5-NLP/18-Transformers/README.md",
  "language_code": "pl"
}
-->
# Mechanizmy uwagi i modele Transformer

## [Quiz przed wykładem](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

Jednym z najważniejszych problemów w dziedzinie NLP jest **tłumaczenie maszynowe**, kluczowe zadanie, które stanowi podstawę narzędzi takich jak Google Translate. W tej sekcji skupimy się na tłumaczeniu maszynowym, a bardziej ogólnie na każdym zadaniu typu *sequence-to-sequence* (nazywanym również **transdukcją zdań**).

W przypadku RNN, zadania sequence-to-sequence są realizowane za pomocą dwóch sieci rekurencyjnych, gdzie jedna sieć, **enkoder**, przekształca sekwencję wejściową w stan ukryty, a druga sieć, **dekoder**, rozwija ten stan ukryty w przetłumaczony wynik. Istnieje kilka problemów związanych z tym podejściem:

* Końcowy stan sieci enkodera ma trudności z zapamiętaniem początku zdania, co prowadzi do niskiej jakości modelu dla długich zdań.
* Wszystkie słowa w sekwencji mają taki sam wpływ na wynik. W rzeczywistości jednak konkretne słowa w sekwencji wejściowej często mają większy wpływ na sekwencyjne wyniki niż inne.

**Mechanizmy uwagi** umożliwiają ważenie kontekstowego wpływu każdego wektora wejściowego na każdą prognozę wyjściową RNN. Implementuje się to poprzez tworzenie skrótów między stanami pośrednimi wejściowego RNN a wyjściowego RNN. W ten sposób, generując symbol wyjściowy y<sub>t</sub>, uwzględniamy wszystkie stany ukryte wejściowe h<sub>i</sub>, z różnymi współczynnikami wag α<sub>t,i</sub>.

![Obraz przedstawiający model enkoder/dekoder z warstwą uwagi addytywnej](../../../../../lessons/5-NLP/18-Transformers/images/encoder-decoder-attention.png)

> Model enkoder-dekoder z mechanizmem uwagi addytywnej w [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), cytowany z [tego wpisu na blogu](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

Macierz uwagi {α<sub>i,j</sub>} reprezentuje stopień, w jakim określone słowa wejściowe wpływają na generowanie danego słowa w sekwencji wyjściowej. Poniżej znajduje się przykład takiej macierzy:

![Obraz przedstawiający przykładowe dopasowanie znalezione przez RNNsearch-50, zaczerpnięte z Bahdanau - arviz.org](../../../../../lessons/5-NLP/18-Transformers/images/bahdanau-fig3.png)

> Rysunek z [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Fig.3)

Mechanizmy uwagi są odpowiedzialne za dużą część obecnego lub bliskiego obecnemu stanu sztuki w NLP. Dodanie uwagi znacznie zwiększa jednak liczbę parametrów modelu, co prowadzi do problemów ze skalowaniem RNN. Kluczowym ograniczeniem skalowania RNN jest to, że rekurencyjny charakter modeli utrudnia grupowanie i równoległe trenowanie. W RNN każdy element sekwencji musi być przetwarzany w kolejności sekwencyjnej, co oznacza, że nie można go łatwo zrównoleglić.

![Enkoder Dekoder z Uwagą](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Rysunek z [Bloga Google](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

Zastosowanie mechanizmów uwagi w połączeniu z tym ograniczeniem doprowadziło do powstania obecnych modeli Transformer, takich jak BERT czy Open-GPT3, które znamy i używamy dzisiaj.

## Modele Transformer

Jednym z głównych pomysłów stojących za modelami Transformer jest unikanie sekwencyjnego charakteru RNN i stworzenie modelu, który można zrównoleglić podczas trenowania. Osiąga się to poprzez wdrożenie dwóch pomysłów:

* kodowanie pozycji
* zastosowanie mechanizmu samouwagi do wychwytywania wzorców zamiast RNN (lub CNN) (dlatego artykuł wprowadzający transformery nosi tytuł *[Attention is all you need](https://arxiv.org/abs/1706.03762)*)

### Kodowanie/Osadzanie Pozycji

Pomysł kodowania pozycji jest następujący:  
1. W przypadku RNN względna pozycja tokenów jest reprezentowana przez liczbę kroków, więc nie musi być jawnie reprezentowana.  
2. Jednak po przejściu na uwagę musimy znać względne pozycje tokenów w sekwencji.  
3. Aby uzyskać kodowanie pozycji, uzupełniamy naszą sekwencję tokenów o sekwencję pozycji tokenów w sekwencji (np. sekwencję liczb 0,1, ...).  
4. Następnie mieszamy pozycję tokenu z wektorem osadzania tokenu. Aby przekształcić pozycję (liczbę całkowitą) w wektor, możemy użyć różnych podejść:

* Osadzanie trenowalne, podobne do osadzania tokenów. To podejście rozważamy tutaj. Stosujemy warstwy osadzania zarówno na tokenach, jak i ich pozycjach, uzyskując wektory osadzania o tych samych wymiarach, które następnie dodajemy do siebie.
* Funkcja kodowania pozycji stała, jak zaproponowano w oryginalnym artykule.

<img src="images/pos-embedding.png" width="50%"/>

> Obraz autorstwa autora

Rezultat, który uzyskujemy dzięki osadzaniu pozycji, osadza zarówno oryginalny token, jak i jego pozycję w sekwencji.

### Samouwaga z Wieloma Głowami

Następnie musimy wychwycić pewne wzorce w naszej sekwencji. Aby to zrobić, transformery używają mechanizmu **samouwagi**, który w zasadzie jest uwagą zastosowaną do tej samej sekwencji jako wejście i wyjście. Zastosowanie samouwagi pozwala nam uwzględnić **kontekst** w zdaniu i zobaczyć, które słowa są ze sobą powiązane. Na przykład pozwala nam zobaczyć, które słowa są odniesieniami do innych, takich jak *to*, oraz uwzględnić kontekst:

![](../../../../../lessons/5-NLP/18-Transformers/images/CoreferenceResolution.png)

> Obraz z [Bloga Google](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

W transformatorach używamy **uwagi z wieloma głowami**, aby dać sieci możliwość wychwytywania różnych typów zależności, np. relacji między słowami długoterminowych vs. krótkoterminowych, koreferencji vs. czegoś innego itd.

[Notebook TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb) zawiera więcej szczegółów na temat implementacji warstw transformera.

### Uwagi Enkoder-Dekoder

W transformatorach uwaga jest stosowana w dwóch miejscach:

* Do wychwytywania wzorców w tekście wejściowym za pomocą samouwagi
* Do tłumaczenia sekwencji - jest to warstwa uwagi między enkoderem a dekoderem.

Uwagi enkoder-dekoder są bardzo podobne do mechanizmu uwagi stosowanego w RNN, jak opisano na początku tej sekcji. Ten animowany diagram wyjaśnia rolę uwagi enkoder-dekoder.

![Animowany GIF pokazujący, jak przeprowadzane są oceny w modelach transformera.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Ponieważ każda pozycja wejściowa jest mapowana niezależnie na każdą pozycję wyjściową, transformery mogą lepiej zrównoleglić niż RNN, co umożliwia tworzenie znacznie większych i bardziej ekspresyjnych modeli językowych. Każda głowa uwagi może być używana do nauki różnych relacji między słowami, co poprawia zadania przetwarzania języka naturalnego.

## BERT

**BERT** (Bidirectional Encoder Representations from Transformers) to bardzo duża wielowarstwowa sieć transformera z 12 warstwami dla *BERT-base* i 24 dla *BERT-large*. Model jest najpierw wstępnie trenowany na dużym korpusie danych tekstowych (Wikipedia + książki) za pomocą uczenia niesuperwizowanego (przewidywanie zamaskowanych słów w zdaniu). Podczas wstępnego trenowania model przyswaja znaczące poziomy zrozumienia języka, które można następnie wykorzystać z innymi zestawami danych za pomocą dostrajania. Ten proces nazywa się **uczeniem transferowym**.

![obrazek z http://jalammar.github.io/illustrated-bert/](../../../../../lessons/5-NLP/18-Transformers/images/jalammarBERT-language-modeling-masked-lm.png)

> Obraz [źródło](http://jalammar.github.io/illustrated-bert/)

## ✍️ Ćwiczenia: Transformery

Kontynuuj naukę w poniższych notebookach:

* [Transformery w PyTorch](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [Transformery w TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## Podsumowanie

W tej lekcji dowiedziałeś się o Transformerach i Mechanizmach Uwagi, które są niezbędnymi narzędziami w zestawie narzędzi NLP. Istnieje wiele wariacji architektur Transformer, w tym BERT, DistilBERT, BigBird, OpenGPT3 i inne, które można dostrajać. Pakiet [HuggingFace](https://github.com/huggingface/) zapewnia repozytorium do trenowania wielu z tych architektur zarówno w PyTorch, jak i TensorFlow.

## 🚀 Wyzwanie

## [Quiz po wykładzie](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## Przegląd i Samodzielna Nauka

* [Wpis na blogu](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), wyjaśniający klasyczny artykuł [Attention is all you need](https://arxiv.org/abs/1706.03762) o transformatorach.
* [Seria wpisów na blogu](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) o transformatorach, wyjaśniająca szczegóły architektury.

## [Zadanie](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.