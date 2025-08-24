<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-24T10:22:21+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "pl"
}
-->
# Rozpoznawanie nazwanych jednostek

Do tej pory skupialiśmy się głównie na jednym zadaniu NLP - klasyfikacji. Istnieją jednak inne zadania NLP, które można realizować za pomocą sieci neuronowych. Jednym z takich zadań jest **[Rozpoznawanie nazwanych jednostek](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), które polega na identyfikacji konkretnych jednostek w tekście, takich jak miejsca, imiona i nazwiska, przedziały czasowe, wzory chemiczne i inne.

## [Quiz przed wykładem](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Przykład użycia NER

Załóżmy, że chcesz stworzyć czatbota obsługującego język naturalny, podobnego do Amazon Alexa lub Google Assistant. Inteligentne czatboty działają w ten sposób, że *rozumieją*, czego użytkownik chce, poprzez klasyfikację tekstu w zdaniu wejściowym. Wynikiem tej klasyfikacji jest tzw. **intencja**, która określa, co czatbot powinien zrobić.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Obraz autorstwa autora

Jednak użytkownik może podać pewne parametry w ramach swojej wypowiedzi. Na przykład, pytając o pogodę, może określić lokalizację lub datę. Bot powinien być w stanie zrozumieć te jednostki i odpowiednio wypełnić pola parametrów przed wykonaniem akcji. Właśnie tutaj wkracza NER.

> ✅ Innym przykładem może być [analiza naukowych artykułów medycznych](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Jednym z głównych zadań jest wyszukiwanie konkretnych terminów medycznych, takich jak choroby i substancje medyczne. Podczas gdy niewielką liczbę chorób można prawdopodobnie wyodrębnić za pomocą wyszukiwania podciągów, bardziej złożone jednostki, takie jak związki chemiczne i nazwy leków, wymagają bardziej zaawansowanego podejścia.

## NER jako klasyfikacja tokenów

Modele NER to w istocie **modele klasyfikacji tokenów**, ponieważ dla każdego z tokenów wejściowych musimy zdecydować, czy należy on do jakiejś jednostki, a jeśli tak - do której klasy jednostek.

Rozważmy następujący tytuł artykułu:

**Niedomykalność zastawki trójdzielnej** i **węglan litu** **toksyczność** u noworodka.

Jednostki w tym przypadku to:

* Niedomykalność zastawki trójdzielnej to choroba (`DIS`)
* Węglan litu to substancja chemiczna (`CHEM`)
* Toksyczność to również choroba (`DIS`)

Zauważ, że jedna jednostka może obejmować kilka tokenów. I, jak w tym przypadku, musimy rozróżnić dwie kolejne jednostki. Dlatego powszechnie stosuje się dwie klasy dla każdej jednostki - jedną określającą pierwszy token jednostki (często używa się prefiksu `B-`, od **b**eginning), a drugą - kontynuację jednostki (`I-`, od **i**nner token). Używamy również `O` jako klasy reprezentującej wszystkie **o**ther tokeny. Takie oznaczanie tokenów nazywa się [BIO tagging](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (lub IOB). Po oznaczeniu nasz tytuł wyglądałby tak:

Token | Tag
------|-----
Niedomykalność | B-DIS
zastawki | I-DIS
trójdzielnej | I-DIS
i | O
węglan | B-CHEM
litu | I-CHEM
toksyczność | B-DIS
u | O
noworodka | O
. | O

Ponieważ musimy zbudować jednoznaczną korespondencję między tokenami a klasami, możemy wytrenować prawostronny model sieci neuronowej **wielu-do-wielu** z tego obrazu:

![Obraz przedstawiający typowe wzorce rekurencyjnych sieci neuronowych.](../../../../../lessons/5-NLP/17-GenerativeNetworks/images/unreasonable-effectiveness-of-rnn.jpg)

> *Obraz z [tego wpisu na blogu](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) autorstwa [Andreja Karpathy'ego](http://karpathy.github.io/). Modele klasyfikacji tokenów NER odpowiadają architekturze sieci po prawej stronie tego obrazu.*

## Trenowanie modeli NER

Ponieważ model NER to w istocie model klasyfikacji tokenów, możemy użyć RNN, które już znamy, do tego zadania. W tym przypadku każdy blok sieci rekurencyjnej zwróci identyfikator tokenu. Poniższy przykładowy notebook pokazuje, jak wytrenować LSTM do klasyfikacji tokenów.

## ✍️ Przykładowe notebooki: NER

Kontynuuj naukę w poniższym notebooku:

* [NER z TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Podsumowanie

Model NER to **model klasyfikacji tokenów**, co oznacza, że można go używać do klasyfikacji tokenów. Jest to bardzo powszechne zadanie w NLP, pomagające rozpoznawać konkretne jednostki w tekście, w tym miejsca, imiona, daty i inne.

## 🚀 Wyzwanie

Wykonaj zadanie podlinkowane poniżej, aby wytrenować model rozpoznawania nazwanych jednostek dla terminów medycznych, a następnie wypróbuj go na innym zbiorze danych.

## [Quiz po wykładzie](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Przegląd i samodzielna nauka

Przeczytaj wpis na blogu [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) i zapoznaj się z sekcją Dalsza lektura w tym artykule, aby pogłębić swoją wiedzę.

## [Zadanie](lab/README.md)

W zadaniu do tej lekcji będziesz musiał wytrenować model rozpoznawania jednostek medycznych. Możesz zacząć od trenowania modelu LSTM, jak opisano w tej lekcji, a następnie przejść do użycia modelu transformera BERT. Przeczytaj [instrukcje](lab/README.md), aby poznać wszystkie szczegóły.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.