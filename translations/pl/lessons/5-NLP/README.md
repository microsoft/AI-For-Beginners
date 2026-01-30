# Przetwarzanie Języka Naturalnego

![Podsumowanie zadań NLP w formie rysunku](../../../../lessons/sketchnotes/ai-nlp.png)

W tej sekcji skupimy się na wykorzystaniu sieci neuronowych do rozwiązywania zadań związanych z **Przetwarzaniem Języka Naturalnego (NLP)**. Istnieje wiele problemów NLP, które chcielibyśmy, aby komputery potrafiły rozwiązywać:

* **Klasyfikacja tekstu** to typowy problem klasyfikacyjny dotyczący sekwencji tekstowych. Przykłady obejmują klasyfikowanie wiadomości e-mail jako spam lub nie-spam, albo kategoryzowanie artykułów jako sport, biznes, polityka itp. Ponadto, podczas tworzenia chatbotów często musimy zrozumieć, co użytkownik chciał powiedzieć — w takim przypadku mamy do czynienia z **klasyfikacją intencji**. W klasyfikacji intencji często musimy radzić sobie z wieloma kategoriami.
* **Analiza sentymentu** to typowy problem regresji, w którym musimy przypisać liczbę (sentyment) odpowiadającą temu, jak pozytywne/negatywne jest znaczenie zdania. Bardziej zaawansowaną wersją analizy sentymentu jest **analiza sentymentu oparta na aspektach** (ABSA), gdzie przypisujemy sentyment nie do całego zdania, ale do jego różnych części (aspektów), np. *W tej restauracji podobała mi się kuchnia, ale atmosfera była okropna*.
* **Rozpoznawanie nazwanych jednostek** (NER) odnosi się do problemu wyodrębniania określonych jednostek z tekstu. Na przykład, musimy zrozumieć, że w zdaniu *Muszę polecieć do Paryża jutro* słowo *jutro* odnosi się do DATY, a *Paryż* to LOKALIZACJA.  
* **Ekstrakcja słów kluczowych** jest podobna do NER, ale musimy automatycznie wyodrębnić słowa istotne dla znaczenia zdania, bez wcześniejszego trenowania na określonych typach jednostek.
* **Grupowanie tekstu** może być przydatne, gdy chcemy pogrupować podobne zdania, na przykład podobne zgłoszenia w rozmowach z pomocą techniczną.
* **Odpowiadanie na pytania** odnosi się do zdolności modelu do udzielania odpowiedzi na konkretne pytanie. Model otrzymuje fragment tekstu i pytanie jako dane wejściowe, a jego zadaniem jest wskazanie miejsca w tekście, gdzie znajduje się odpowiedź (lub czasami wygenerowanie tekstu odpowiedzi).
* **Generowanie tekstu** to zdolność modelu do tworzenia nowego tekstu. Można to traktować jako zadanie klasyfikacyjne, które przewiduje kolejną literę/słowo na podstawie pewnej *podpowiedzi tekstowej*. Zaawansowane modele generowania tekstu, takie jak GPT-3, potrafią rozwiązywać inne zadania NLP, takie jak klasyfikacja, wykorzystując techniki zwane [programowaniem podpowiedzi](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) lub [inżynierią podpowiedzi](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29).
* **Podsumowywanie tekstu** to technika, w której chcemy, aby komputer "przeczytał" długi tekst i streścił go w kilku zdaniach.
* **Tłumaczenie maszynowe** można postrzegać jako połączenie rozumienia tekstu w jednym języku i generowania tekstu w innym.

Początkowo większość zadań NLP była rozwiązywana za pomocą tradycyjnych metod, takich jak gramatyki. Na przykład w tłumaczeniu maszynowym używano parserów do przekształcenia początkowego zdania w drzewo składniowe, następnie wyodrębniano wyższe struktury semantyczne, aby reprezentować znaczenie zdania, a na podstawie tego znaczenia i gramatyki języka docelowego generowano wynik. Obecnie wiele zadań NLP jest skuteczniej rozwiązywanych za pomocą sieci neuronowych.

> Wiele klasycznych metod NLP jest zaimplementowanych w bibliotece Python [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org). Dostępna jest świetna [Książka o NLTK](https://www.nltk.org/book/), która omawia, jak różne zadania NLP można rozwiązać za pomocą NLTK.

W naszym kursie skupimy się głównie na wykorzystaniu sieci neuronowych w NLP, a NLTK będziemy używać w razie potrzeby.

Nauczyliśmy się już, jak używać sieci neuronowych do pracy z danymi tabelarycznymi i obrazami. Główna różnica między tymi typami danych a tekstem polega na tym, że tekst jest sekwencją o zmiennej długości, podczas gdy rozmiar wejścia w przypadku obrazów jest znany z góry. Podczas gdy sieci konwolucyjne mogą wyodrębniać wzorce z danych wejściowych, wzorce w tekście są bardziej złożone. Na przykład negacja może być oddzielona od podmiotu przez dowolną liczbę słów (np. *Nie lubię pomarańczy* vs. *Nie lubię tych dużych kolorowych smacznych pomarańczy*), a mimo to powinna być interpretowana jako jeden wzorzec. Dlatego, aby przetwarzać język, musimy wprowadzić nowe typy sieci neuronowych, takie jak *sieci rekurencyjne* i *transformery*.

## Instalacja bibliotek

Jeśli korzystasz z lokalnej instalacji Pythona do uruchamiania tego kursu, możesz potrzebować zainstalować wszystkie wymagane biblioteki dla NLP za pomocą następujących poleceń:

**Dla PyTorch**
```bash
pip install -r requirements-torch.txt
```
**Dla TensorFlow**
```bash
pip install -r requirements-tf.txt
```

> Możesz wypróbować NLP z TensorFlow na [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste)

## Ostrzeżenie dotyczące GPU

W tej sekcji, w niektórych przykładach będziemy trenować dość duże modele.
* **Używaj komputera z obsługą GPU**: Zaleca się uruchamianie notebooków na komputerze z obsługą GPU, aby skrócić czas oczekiwania podczas pracy z dużymi modelami.
* **Ograniczenia pamięci GPU**: Uruchamianie na GPU może prowadzić do sytuacji, w których zabraknie pamięci GPU, zwłaszcza podczas trenowania dużych modeli.
* **Zużycie pamięci GPU**: Ilość pamięci GPU zużywanej podczas trenowania zależy od różnych czynników, w tym rozmiaru minibatcha.
* **Minimalizuj rozmiar minibatcha**: Jeśli napotkasz problemy z pamięcią GPU, rozważ zmniejszenie rozmiaru minibatcha w swoim kodzie jako potencjalne rozwiązanie.
* **Zwolnienie pamięci GPU w TensorFlow**: Starsze wersje TensorFlow mogą nie zwalniać pamięci GPU poprawnie podczas trenowania wielu modeli w jednym jądrze Pythona. Aby skutecznie zarządzać użyciem pamięci GPU, możesz skonfigurować TensorFlow tak, aby alokował pamięć GPU tylko w razie potrzeby.
* **Dodanie kodu**: Aby ustawić TensorFlow na dynamiczne przydzielanie pamięci GPU, dodaj poniższy kod do swoich notebooków:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

Jeśli interesuje Cię nauka NLP z perspektywy klasycznego ML, odwiedź [ten zestaw lekcji](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)

## W tej sekcji
W tej sekcji nauczymy się:

* [Reprezentowania tekstu jako tensory](13-TextRep/README.md)
* [Osadzeń słów](14-Emdeddings/README.md)
* [Modelowania języka](15-LanguageModeling/README.md)
* [Rekurencyjnych sieci neuronowych](16-RNN/README.md)
* [Sieci generatywnych](17-GenerativeNetworks/README.md)
* [Transformerów](18-Transformers/README.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.