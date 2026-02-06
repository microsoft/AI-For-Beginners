# Sieci Multi-Modalne

Po sukcesie modeli transformerowych w rozwiązywaniu zadań NLP, podobne architektury zaczęto stosować w zadaniach związanych z wizją komputerową. Coraz większe zainteresowanie budzą modele, które *łączą* możliwości analizy obrazu i języka naturalnego. Jednym z takich podejść jest CLIP i DALL.E, opracowane przez OpenAI.

## Kontrastowe Uczenie Obrazów (CLIP)

Główna idea CLIP polega na porównywaniu tekstowych opisów z obrazami i określaniu, jak dobrze obraz odpowiada danemu opisowi.

![Architektura CLIP](../../../../../lessons/X-Extras/X1-MultiModal/images/clip-arch.png)

> *Obrazek z [tego wpisu na blogu](https://openai.com/blog/clip/)*

Model jest trenowany na obrazach pobranych z Internetu oraz ich podpisach. Dla każdej partii danych bierzemy N par (obraz, tekst) i przekształcamy je w reprezentacje wektorowe I, ..., I / T, ..., T. Te reprezentacje są następnie dopasowywane do siebie. Funkcja straty jest zdefiniowana tak, aby maksymalizować podobieństwo kosinusowe między wektorami odpowiadającymi jednej parze (np. I i T) oraz minimalizować podobieństwo kosinusowe między wszystkimi innymi parami. Dlatego to podejście nazywa się **kontrastowym**.

Biblioteka/model CLIP jest dostępna na [GitHub OpenAI](https://github.com/openai/CLIP). Podejście zostało opisane w [tym wpisie na blogu](https://openai.com/blog/clip/) oraz szczegółowo w [tym artykule](https://arxiv.org/pdf/2103.00020.pdf).

Po wstępnym przetrenowaniu modelu możemy podać mu partię obrazów i tekstowych opisów, a w wyniku otrzymamy tensor z prawdopodobieństwami. CLIP może być używany do kilku zadań:

**Klasyfikacja Obrazów**

Załóżmy, że musimy sklasyfikować obrazy, np. na koty, psy i ludzi. W takim przypadku możemy podać modelowi obraz oraz serię tekstowych opisów: "*obraz kota*", "*obraz psa*", "*obraz człowieka*". W wynikowym wektorze z 3 prawdopodobieństwami wystarczy wybrać indeks z najwyższą wartością.

![CLIP dla Klasyfikacji Obrazów](../../../../../lessons/X-Extras/X1-MultiModal/images/clip-class.png)

> *Obrazek z [tego wpisu na blogu](https://openai.com/blog/clip/)*

**Wyszukiwanie Obrazów na Podstawie Tekstu**

Możemy również zrobić odwrotnie. Jeśli mamy kolekcję obrazów, możemy przekazać ją do modelu wraz z tekstowym opisem – w wyniku otrzymamy obraz najbardziej odpowiadający danemu opisowi.

## ✍️ Przykład: [Użycie CLIP do Klasyfikacji Obrazów i Wyszukiwania Obrazów](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

Otwórz notebook [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb), aby zobaczyć CLIP w akcji.

## Generowanie Obrazów za pomocą VQGAN+CLIP

CLIP może być również używany do **generowania obrazów** na podstawie tekstowego opisu. Aby to zrobić, potrzebujemy **modelu generatora**, który będzie w stanie generować obrazy na podstawie wektora wejściowego. Jednym z takich modeli jest [VQGAN](https://compvis.github.io/taming-transformers/) (Vector-Quantized GAN).

Główne idee VQGAN, które odróżniają go od zwykłego [GAN](../../4-ComputerVision/10-GANs/README.md), to:
* Wykorzystanie autoregresyjnej architektury transformera do generowania sekwencji kontekstowo bogatych części wizualnych, które składają się na obraz. Te części wizualne są z kolei uczone przez [CNN](../../4-ComputerVision/07-ConvNets/README.md).
* Użycie dyskryminatora sub-obrazów, który wykrywa, czy części obrazu są "prawdziwe" czy "fałszywe" (w przeciwieństwie do podejścia "wszystko albo nic" w tradycyjnym GAN).

Więcej o VQGAN można dowiedzieć się na stronie [Taming Transformers](https://compvis.github.io/taming-transformers/).

Jedną z ważnych różnic między VQGAN a tradycyjnym GAN jest to, że ten ostatni może wygenerować przyzwoity obraz z dowolnego wektora wejściowego, podczas gdy VQGAN może wygenerować obraz, który nie będzie spójny. Dlatego proces tworzenia obrazu musi być dodatkowo kierowany, co można zrobić za pomocą CLIP.

![Architektura VQGAN+CLIP](../../../../../lessons/X-Extras/X1-MultiModal/images/vqgan.png)

Aby wygenerować obraz odpowiadający tekstowemu opisowi, zaczynamy od losowego wektora kodującego, który jest przekazywany przez VQGAN w celu wygenerowania obrazu. Następnie CLIP jest używany do stworzenia funkcji straty, która pokazuje, jak dobrze obraz odpowiada tekstowemu opisowi. Celem jest minimalizacja tej straty, wykorzystując propagację wsteczną do dostosowania parametrów wektora wejściowego.

Świetna biblioteka implementująca VQGAN+CLIP to [Pixray](http://github.com/pixray/pixray).

![Obraz wygenerowany przez Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.png) |  ![Obraz wygenerowany przez Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.png) | ![Obraz wygenerowany przez Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_oil_portrait_of_old_male_teacher_of_math.png)
----|----|----
Obraz wygenerowany na podstawie opisu *zbliżenie akwarelowego portretu młodego nauczyciela literatury z książką* | Obraz wygenerowany na podstawie opisu *zbliżenie olejnego portretu młodej nauczycielki informatyki z komputerem* | Obraz wygenerowany na podstawie opisu *zbliżenie olejnego portretu starszego nauczyciela matematyki przed tablicą*

> Obrazy z kolekcji **Artificial Teachers** autorstwa [Dmitry Soshnikov](http://soshnikov.com)

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E to wersja GPT-3 przeszkolona do generowania obrazów na podstawie opisów. Model został przeszkolony na 12 miliardach parametrów.

W przeciwieństwie do CLIP, DALL-E otrzymuje zarówno tekst, jak i obraz jako pojedynczy strumień tokenów dla obu typów danych. Dzięki temu można generować obrazy na podstawie wielu opisów.

### [DALL-E 2](https://openai.com/dall-e-2)
Główna różnica między DALL-E 1 a 2 polega na tym, że DALL-E 2 generuje bardziej realistyczne obrazy i dzieła sztuki.

Przykłady generowania obrazów za pomocą DALL-E:
![Obraz wygenerowany przez Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.png) |  ![Obraz wygenerowany przez Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.png) | ![Obraz wygenerowany przez Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.png)
----|----|----
Obraz wygenerowany na podstawie opisu *zbliżenie akwarelowego portretu młodego nauczyciela literatury z książką* | Obraz wygenerowany na podstawie opisu *zbliżenie olejnego portretu młodej nauczycielki informatyki z komputerem* | Obraz wygenerowany na podstawie opisu *zbliżenie olejnego portretu starszego nauczyciela matematyki przed tablicą*

## Źródła

* Artykuł o VQGAN: [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* Artykuł o CLIP: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.