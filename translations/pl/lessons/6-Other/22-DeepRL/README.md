# Deep Reinforcement Learning

Uczenie przez wzmacnianie (RL) jest uważane za jeden z podstawowych paradygmatów uczenia maszynowego, obok uczenia nadzorowanego i nienadzorowanego. Podczas gdy w uczeniu nadzorowanym opieramy się na zbiorze danych z określonymi wynikami, RL bazuje na **uczeniu się przez działanie**. Na przykład, gdy po raz pierwszy widzimy grę komputerową, zaczynamy grać, nawet nie znając zasad, a wkrótce jesteśmy w stanie poprawić swoje umiejętności dzięki samemu procesowi grania i dostosowywania swojego zachowania.

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Aby przeprowadzić RL, potrzebujemy:

* **Środowiska** lub **symulatora**, który ustala zasady gry. Powinniśmy być w stanie przeprowadzać eksperymenty w symulatorze i obserwować wyniki.
* **Funkcji nagrody**, która wskazuje, jak udany był nasz eksperyment. W przypadku nauki gry w grę komputerową, nagrodą byłby nasz końcowy wynik.

Na podstawie funkcji nagrody powinniśmy być w stanie dostosować swoje zachowanie i poprawić swoje umiejętności, aby następnym razem grać lepiej. Główna różnica między innymi typami uczenia maszynowego a RL polega na tym, że w RL zazwyczaj nie wiemy, czy wygrywamy, czy przegrywamy, dopóki nie zakończymy gry. Dlatego nie możemy stwierdzić, czy dany ruch sam w sobie jest dobry czy nie - nagrodę otrzymujemy dopiero na końcu gry.

Podczas RL zazwyczaj przeprowadzamy wiele eksperymentów. W każdym eksperymencie musimy balansować między podążaniem za optymalną strategią, którą dotychczas opracowaliśmy (**eksploatacja**), a eksplorowaniem nowych możliwych stanów (**eksploracja**).

## OpenAI Gym

Świetnym narzędziem do RL jest [OpenAI Gym](https://gym.openai.com/) - **środowisko symulacyjne**, które może symulować wiele różnych środowisk, począwszy od gier Atari, aż po fizykę związaną z balansowaniem drążka. Jest to jedno z najpopularniejszych środowisk symulacyjnych do trenowania algorytmów uczenia przez wzmacnianie i jest utrzymywane przez [OpenAI](https://openai.com/).

> **Note**: Możesz zobaczyć wszystkie dostępne środowiska OpenAI Gym [tutaj](https://gym.openai.com/envs/#classic_control).

## Balansowanie CartPole

Prawdopodobnie wszyscy widzieliście nowoczesne urządzenia balansujące, takie jak *Segway* czy *Gyroscooters*. Są one w stanie automatycznie balansować, dostosowując swoje koła w odpowiedzi na sygnał z akcelerometru lub żyroskopu. W tej sekcji nauczymy się, jak rozwiązać podobny problem - balansowanie drążka. Jest to podobne do sytuacji, gdy artysta cyrkowy musi balansować drążek na swojej dłoni - ale to balansowanie drążka odbywa się tylko w 1D.

Uproszczona wersja balansowania jest znana jako problem **CartPole**. W świecie CartPole mamy poziomy suwak, który może poruszać się w lewo lub w prawo, a celem jest balansowanie pionowego drążka na szczycie suwaka podczas jego ruchu.

<img alt="a cartpole" src="../../../../../translated_images/pl/cartpole.f52a67f27e058170.webp" width="200"/>

Aby stworzyć i używać tego środowiska, potrzebujemy kilku linii kodu w Pythonie:

```python
import gym
env = gym.make("CartPole-v1")

env.reset()
done = False
total_reward = 0
while not done:
   env.render()
   action = env.action_space.sample()
   observaton, reward, done, info = env.step(action)
   total_reward += reward

print(f"Total reward: {total_reward}")
```

Każde środowisko można obsługiwać dokładnie w ten sam sposób:
* `env.reset` rozpoczyna nowy eksperyment
* `env.step` wykonuje krok symulacji. Otrzymuje **akcję** z **przestrzeni akcji** i zwraca **obserwację** (z przestrzeni obserwacji), a także nagrodę i flagę zakończenia.

W powyższym przykładzie wykonujemy losową akcję na każdym kroku, dlatego życie eksperymentu jest bardzo krótkie:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Celem algorytmu RL jest wytrenowanie modelu - tzw. **polityki** &pi; - która zwróci akcję w odpowiedzi na dany stan. Możemy również rozważyć politykę jako probabilistyczną, np. dla każdego stanu *s* i akcji *a* zwróci prawdopodobieństwo &pi;(*a*|*s*), że powinniśmy podjąć *a* w stanie *s*.

## Algorytm Policy Gradients

Najbardziej oczywistym sposobem modelowania polityki jest stworzenie sieci neuronowej, która przyjmie stany jako wejście i zwróci odpowiadające akcje (a właściwie prawdopodobieństwa wszystkich akcji). W pewnym sensie byłoby to podobne do normalnego zadania klasyfikacji, z jedną istotną różnicą - nie wiemy z góry, jakie akcje powinniśmy podjąć na każdym z kroków.

Pomysł polega na oszacowaniu tych prawdopodobieństw. Budujemy wektor **skumulowanych nagród**, który pokazuje naszą całkowitą nagrodę na każdym kroku eksperymentu. Stosujemy również **dyskontowanie nagród**, mnożąc wcześniejsze nagrody przez współczynnik &gamma;=0.99, aby zmniejszyć rolę wcześniejszych nagród. Następnie wzmacniamy te kroki na ścieżce eksperymentu, które przynoszą większe nagrody.

> Dowiedz się więcej o algorytmie Policy Gradient i zobacz go w akcji w [przykładowym notebooku](CartPole-RL-TF.ipynb).

## Algorytm Actor-Critic

Ulepszona wersja podejścia Policy Gradients nazywa się **Actor-Critic**. Główna idea polega na tym, że sieć neuronowa będzie trenowana, aby zwracać dwie rzeczy:

* Politykę, która określa, jaką akcję podjąć. Ta część nazywa się **aktor**
* Szacowanie całkowitej nagrody, którą możemy oczekiwać w danym stanie - ta część nazywa się **krytyk**.

W pewnym sensie ta architektura przypomina [GAN](../../4-ComputerVision/10-GANs/README.md), gdzie mamy dwie sieci trenowane przeciwko sobie. W modelu actor-critic aktor proponuje akcję, którą powinniśmy podjąć, a krytyk stara się być krytyczny i oszacować wynik. Jednak naszym celem jest trenowanie tych sieci w harmonii.

Ponieważ znamy zarówno rzeczywiste skumulowane nagrody, jak i wyniki zwracane przez krytyka podczas eksperymentu, stosunkowo łatwo jest zbudować funkcję straty, która zminimalizuje różnicę między nimi. To da nam **stratę krytyka**. Możemy obliczyć **stratę aktora**, używając tego samego podejścia co w algorytmie Policy Gradient.

Po uruchomieniu jednego z tych algorytmów możemy oczekiwać, że nasz CartPole będzie zachowywał się tak:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Ćwiczenia: Policy Gradients i Actor-Critic RL

Kontynuuj naukę w poniższych notebookach:

* [RL w TensorFlow](CartPole-RL-TF.ipynb)
* [RL w PyTorch](CartPole-RL-PyTorch.ipynb)

## Inne zadania RL

Uczenie przez wzmacnianie jest obecnie szybko rozwijającą się dziedziną badań. Niektóre interesujące przykłady uczenia przez wzmacnianie to:

* Nauka komputera gry w **gry Atari**. Wyzwanie w tym problemie polega na tym, że nie mamy prostego stanu reprezentowanego jako wektor, lecz raczej zrzut ekranu - i musimy użyć CNN, aby przekształcić obraz ekranu w wektor cech lub wyodrębnić informacje o nagrodach. Gry Atari są dostępne w Gym.
* Nauka komputera gry w gry planszowe, takie jak szachy i Go. Ostatnio programy na najwyższym poziomie, takie jak **Alpha Zero**, były trenowane od podstaw przez dwóch agentów grających przeciwko sobie i poprawiających się na każdym kroku.
* W przemyśle RL jest używane do tworzenia systemów sterowania na podstawie symulacji. Usługa [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) jest specjalnie zaprojektowana do tego celu.

## Podsumowanie

Nauczyliśmy się teraz, jak trenować agentów, aby osiągali dobre wyniki, zapewniając im jedynie funkcję nagrody, która definiuje pożądany stan gry, oraz dając im możliwość inteligentnego eksplorowania przestrzeni wyszukiwania. Z powodzeniem wypróbowaliśmy dwa algorytmy i osiągnęliśmy dobry wynik w stosunkowo krótkim czasie. Jednak to dopiero początek Twojej podróży w RL, i zdecydowanie warto rozważyć udział w osobnym kursie, jeśli chcesz zgłębić temat.

## 🚀 Wyzwanie

Zbadaj aplikacje wymienione w sekcji "Inne zadania RL" i spróbuj zaimplementować jedną z nich!

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Przegląd i samodzielna nauka

Dowiedz się więcej o klasycznym uczeniu przez wzmacnianie w naszym [Kursie dla początkujących z uczenia maszynowego](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Obejrzyj [ten świetny film](https://www.youtube.com/watch?v=qv6UVOQ0F44) o tym, jak komputer może nauczyć się grać w Super Mario.

## Zadanie: [Trenuj Mountain Car](lab/README.md)

Twoim celem w tym zadaniu będzie wytrenowanie innego środowiska Gym - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

