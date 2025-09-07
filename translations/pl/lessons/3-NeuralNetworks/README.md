<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1c6b8c7c1778a35fc1139b7f2aecb7b3",
  "translation_date": "2025-08-24T10:39:47+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do sieci neuronowych

![Podsumowanie treści Wprowadzenie do Sieci Neuronowych w formie rysunku](../../../../lessons/sketchnotes/ai-neuralnetworks.png)

Jak omówiliśmy we wstępie, jednym ze sposobów osiągnięcia inteligencji jest trenowanie **modelu komputerowego** lub **sztucznego mózgu**. Od połowy XX wieku naukowcy próbowali różnych modeli matematycznych, aż w ostatnich latach ten kierunek okazał się niezwykle skuteczny. Takie matematyczne modele mózgu nazywane są **sieciami neuronowymi**.

> Czasami sieci neuronowe nazywane są *Sztucznymi Sieciami Neuronowymi* (Artificial Neural Networks, ANNs), aby podkreślić, że mówimy o modelach, a nie o rzeczywistych sieciach neuronów.

## Uczenie maszynowe

Sieci neuronowe są częścią większej dziedziny zwanej **Uczeniem Maszynowym**, której celem jest wykorzystanie danych do trenowania modeli komputerowych zdolnych do rozwiązywania problemów. Uczenie maszynowe stanowi dużą część sztucznej inteligencji, jednak w tym programie nauczania nie omawiamy klasycznego uczenia maszynowego.

> Odwiedź nasz osobny program nauczania **[Uczenie Maszynowe dla Początkujących](http://github.com/microsoft/ml-for-beginners)**, aby dowiedzieć się więcej o klasycznym uczeniu maszynowym.

W uczeniu maszynowym zakładamy, że mamy jakiś zbiór danych przykładów **X** oraz odpowiadające im wartości wyjściowe **Y**. Przykłady często są N-wymiarowymi wektorami składającymi się z **cech**, a wartości wyjściowe nazywane są **etykietami**.

Rozważymy dwa najczęstsze problemy uczenia maszynowego:

* **Klasyfikacja**, gdzie musimy sklasyfikować obiekt wejściowy do dwóch lub więcej klas.
* **Regresja**, gdzie musimy przewidzieć wartość liczbową dla każdego z próbek wejściowych.

> Reprezentując dane wejściowe i wyjściowe jako tensory, zbiór danych wejściowych jest macierzą o rozmiarze M×N, gdzie M to liczba próbek, a N to liczba cech. Etykiety wyjściowe Y są wektorem o rozmiarze M.

W tym programie nauczania skupimy się wyłącznie na modelach sieci neuronowych.

## Model neuronu

Z biologii wiemy, że nasz mózg składa się z komórek nerwowych, z których każda ma wiele "wejść" (aksonów) i jedno wyjście (dendryt). Aksony i dendryty mogą przewodzić sygnały elektryczne, a połączenia między aksonami a dendrytami mogą wykazywać różne stopnie przewodności (kontrolowane przez neuromediatory).

![Model neuronu](../../../../lessons/3-NeuralNetworks/images/synapse-wikipedia.jpg) | ![Model neuronu](../../../../lessons/3-NeuralNetworks/images/artneuron.png)
----|----
Prawdziwy neuron *([Obraz](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) z Wikipedii)* | Sztuczny neuron *(Obraz autora)*

Najprostszy matematyczny model neuronu zawiera kilka wejść X<sub>1</sub>, ..., X<sub>N</sub> oraz jedno wyjście Y, a także serię wag W<sub>1</sub>, ..., W<sub>N</sub>. Wyjście jest obliczane jako:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

gdzie f jest pewną nieliniową **funkcją aktywacji**.

> Wczesne modele neuronu zostały opisane w klasycznym artykule [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) autorstwa Warrena McCullocka i Waltera Pittsa w 1943 roku. Donald Hebb w swojej książce "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" zaproponował sposób, w jaki te sieci mogą być trenowane.

## W tej sekcji

W tej sekcji dowiemy się o:
* [Perceptronie](03-Perceptron/README.md), jednym z najwcześniejszych modeli sieci neuronowych do klasyfikacji dwuklasowej
* [Sieciach wielowarstwowych](04-OwnFramework/README.md) wraz z notatnikiem [jak zbudować własny framework](../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)
* [Frameworkach sieci neuronowych](05-Frameworks/README.md), z tymi notatnikami: [PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) i [Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [Przeuczeniu](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.