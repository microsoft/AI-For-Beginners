# Wstępnie Wytrenowane Duże Modele Językowe

We wszystkich naszych wcześniejszych zadaniach trenowaliśmy sieć neuronową, aby wykonywała określone zadanie, korzystając z oznaczonego zbioru danych. W przypadku dużych modeli transformatorowych, takich jak BERT, wykorzystujemy modelowanie języka w trybie samonadzorowanym, aby zbudować model językowy, który następnie jest specjalizowany do konkretnych zadań za pomocą dalszego treningu specyficznego dla danej dziedziny. Jednakże wykazano, że duże modele językowe mogą również rozwiązywać wiele zadań bez jakiegokolwiek treningu specyficznego dla dziedziny. Rodzina modeli zdolnych do tego nazywa się **GPT**: Generative Pre-Trained Transformer.

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Generowanie Tekstu i Perpleksja

Pomysł, że sieć neuronowa może wykonywać ogólne zadania bez dodatkowego treningu, został przedstawiony w artykule [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Główna idea polega na tym, że wiele innych zadań można modelować za pomocą **generowania tekstu**, ponieważ rozumienie tekstu zasadniczo oznacza umiejętność jego tworzenia. Ponieważ model jest trenowany na ogromnej ilości tekstu obejmującego ludzką wiedzę, staje się również kompetentny w szerokim zakresie tematów.

> Rozumienie i umiejętność tworzenia tekstu wiąże się również z posiadaniem wiedzy o otaczającym nas świecie. Ludzie w dużej mierze uczą się poprzez czytanie, a sieć GPT jest pod tym względem podobna.

Sieci generujące tekst działają poprzez przewidywanie prawdopodobieństwa następnego słowa $$P(w_N)$$. Jednak bezwarunkowe prawdopodobieństwo następnego słowa jest równe częstotliwości tego słowa w korpusie tekstu. GPT potrafi podać nam **warunkowe prawdopodobieństwo** następnego słowa, biorąc pod uwagę poprzednie: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Więcej o prawdopodobieństwach możesz przeczytać w naszym [Kursie Data Science dla Początkujących](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Jakość modelu generującego tekst można określić za pomocą **perpleksji**. Jest to wewnętrzna metryka, która pozwala nam mierzyć jakość modelu bez użycia jakiegokolwiek zbioru danych specyficznego dla zadania. Opiera się na pojęciu *prawdopodobieństwa zdania* - model przypisuje wysokie prawdopodobieństwo zdaniu, które prawdopodobnie jest prawdziwe (tj. model nie jest **zdezorientowany**), oraz niskie prawdopodobieństwo zdaniom, które mają mniej sensu (np. *Can it does what?*). Gdy podajemy naszemu modelowi zdania z rzeczywistego korpusu tekstu, oczekujemy, że będą miały wysokie prawdopodobieństwo i niską **perpleksję**. Matematycznie jest to zdefiniowane jako znormalizowane odwrotne prawdopodobieństwo zbioru testowego:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Możesz eksperymentować z generowaniem tekstu, korzystając z [edytora tekstu opartego na GPT od Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. W tym edytorze zaczynasz pisać swój tekst, a po naciśnięciu **[TAB]** otrzymasz kilka opcji uzupełnienia. Jeśli są zbyt krótkie lub nie jesteś z nich zadowolony - naciśnij [TAB] ponownie, aby uzyskać więcej opcji, w tym dłuższe fragmenty tekstu.

## GPT jako Rodzina

GPT to nie jeden model, lecz raczej kolekcja modeli opracowanych i wytrenowanych przez [OpenAI](https://openai.com).

W ramach modeli GPT mamy:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Model językowy z maksymalnie 1,5 miliarda parametrów. | Model językowy z maksymalnie 175 miliardami parametrów. | 100T parametrów, akceptuje zarówno obrazy, jak i tekst jako wejście, a generuje tekst jako wyjście. |

Modele GPT-3 i GPT-4 są dostępne [jako usługa kognitywna od Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) oraz jako [API OpenAI](https://openai.com/api/).

## Inżynieria Podpowiedzi (Prompt Engineering)

Ponieważ GPT zostało wytrenowane na ogromnych ilościach danych, aby rozumieć język i kod, generuje odpowiedzi w odpowiedzi na wejścia (podpowiedzi). Podpowiedzi to zapytania lub instrukcje dla GPT, które określają, jakie zadania model ma wykonać. Aby uzyskać pożądany wynik, należy stworzyć najbardziej efektywną podpowiedź, co wiąże się z wyborem odpowiednich słów, formatów, fraz, a nawet symboli. To podejście nazywa się [Inżynierią Podpowiedzi](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Ta dokumentacja](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) dostarcza więcej informacji na temat inżynierii podpowiedzi.

## ✍️ Przykładowy Notebook: [Zabawa z OpenAI-GPT](GPT-PyTorch.ipynb)

Kontynuuj naukę w poniższych notebookach:

* [Generowanie tekstu za pomocą OpenAI-GPT i Hugging Face Transformers](GPT-PyTorch.ipynb)

## Podsumowanie

Nowe ogólne wstępnie wytrenowane modele językowe nie tylko modelują strukturę języka, ale także zawierają ogromne ilości naturalnego języka. Dzięki temu mogą być skutecznie wykorzystywane do rozwiązywania niektórych zadań NLP w trybie zero-shot lub few-shot.

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

