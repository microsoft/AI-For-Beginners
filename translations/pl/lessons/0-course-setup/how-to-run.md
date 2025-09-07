<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-24T10:48:55+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "pl"
}
-->
# Jak uruchomić kod

Ten kurs zawiera wiele przykładów do wykonania oraz laboratoriów, które możesz chcieć uruchomić. Aby to zrobić, musisz mieć możliwość wykonywania kodu Python w Jupyter Notebooks, które są częścią tego kursu. Masz kilka opcji uruchamiania kodu:

## Uruchamianie lokalnie na swoim komputerze

Aby uruchomić kod lokalnie na swoim komputerze, musisz mieć zainstalowaną jakąś wersję Pythona. Osobiście polecam zainstalowanie **[miniconda](https://conda.io/en/latest/miniconda.html)** – to lekka instalacja, która obsługuje menedżera pakietów `conda` dla różnych **wirtualnych środowisk** Pythona.

Po zainstalowaniu minicondy musisz sklonować repozytorium i utworzyć wirtualne środowisko, które będzie używane w tym kursie:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Korzystanie z Visual Studio Code z rozszerzeniem Python

Prawdopodobnie najlepszym sposobem korzystania z kursu jest otwarcie go w [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) z [rozszerzeniem Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Po sklonowaniu i otwarciu katalogu w VS Code, program automatycznie zasugeruje zainstalowanie rozszerzeń Pythona. Będziesz także musiał zainstalować minicondę, jak opisano powyżej.

> **Note**: Jeśli VS Code zasugeruje otwarcie repozytorium w kontenerze, musisz to odrzucić, aby używać lokalnej instalacji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz również korzystać ze środowiska Jupyter bezpośrednio w przeglądarce na swoim komputerze. Zarówno klasyczny Jupyter, jak i Jupyter Hub oferują wygodne środowisko programistyczne z autouzupełnianiem, podświetlaniem kodu itp.

Aby uruchomić Jupyter lokalnie, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```  
lub  
```bash
jupyterhub
```  
Następnie możesz przejść do dowolnego pliku `.ipynb`, otworzyć go i zacząć pracę.

### Uruchamianie w kontenerze

Alternatywą dla instalacji Pythona może być uruchamianie kodu w kontenerze. Ponieważ nasze repozytorium zawiera specjalny folder `.devcontainer`, który określa, jak zbudować kontener dla tego repozytorium, VS Code zaproponuje otwarcie kodu w kontenerze. Wymaga to instalacji Dockera i jest bardziej skomplikowane, więc polecamy to bardziej zaawansowanym użytkownikom.

## Uruchamianie w chmurze

Jeśli nie chcesz instalować Pythona lokalnie i masz dostęp do zasobów w chmurze, dobrą alternatywą jest uruchamianie kodu w chmurze. Istnieje kilka sposobów, aby to zrobić:

* Korzystanie z **[GitHub Codespaces](https://github.com/features/codespaces)**, które jest wirtualnym środowiskiem utworzonym dla Ciebie na GitHubie, dostępnym przez interfejs przeglądarkowy VS Code. Jeśli masz dostęp do Codespaces, wystarczy kliknąć przycisk **Code** w repozytorium, uruchomić Codespace i zacząć pracę w mgnieniu oka.
* Korzystanie z **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) to darmowe zasoby obliczeniowe w chmurze, które pozwalają testować kod z GitHuba. Na stronie głównej repozytorium znajdziesz przycisk do otwarcia go w Binderze – szybko przeniesie Cię na stronę Bindera, która zbuduje kontener i uruchomi interfejs Jupyter w przeglądarce.

> **Note**: Aby zapobiec nadużyciom, Binder ma zablokowany dostęp do niektórych zasobów sieciowych. Może to uniemożliwić działanie kodu, który pobiera modele i/lub zestawy danych z publicznego Internetu. Może być konieczne znalezienie obejść. Ponadto zasoby obliczeniowe Bindera są dość podstawowe, więc trening będzie wolny, szczególnie w późniejszych, bardziej złożonych lekcjach.

## Uruchamianie w chmurze z obsługą GPU

Niektóre z późniejszych lekcji w tym kursie znacznie skorzystają z obsługi GPU, ponieważ w przeciwnym razie trening będzie bardzo wolny. Istnieje kilka opcji, szczególnie jeśli masz dostęp do chmury, na przykład przez [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) lub swoją instytucję:

* Utwórz [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) i połącz się z nią przez Jupyter. Możesz wtedy sklonować repozytorium bezpośrednio na maszynę i rozpocząć naukę. Maszyny w serii NC mają obsługę GPU.

> **Note**: Niektóre subskrypcje, w tym Azure for Students, nie oferują obsługi GPU od razu. Może być konieczne złożenie wniosku o dodatkowe rdzenie GPU przez zgłoszenie do pomocy technicznej.

* Utwórz [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste), a następnie skorzystaj z funkcji Notebook. [Ten film](https://azure-for-academics.github.io/quickstart/azureml-papers/) pokazuje, jak sklonować repozytorium do notatnika Azure ML i zacząć z niego korzystać.

Możesz także skorzystać z Google Colab, który oferuje darmową obsługę GPU, i przesłać tam Jupyter Notebooks, aby wykonywać je krok po kroku.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.