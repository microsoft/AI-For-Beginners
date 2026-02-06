# Jak Uruchomić Kod

Ten program nauczania zawiera wiele wykonalnych przykładów i laboratoriów, które będziesz chciał uruchomić. Aby to zrobić, musisz mieć możliwość wykonywania kodu Python w Jupyter Notebooks dostarczonych w ramach tego programu nauczania. Masz kilka opcji uruchamiania kodu:

## Uruchamianie lokalnie na Twoim komputerze

Aby uruchomić kod lokalnie na Twoim komputerze, potrzebna jest instalacja Pythona. Jednym z rekomendowanych rozwiązań jest instalacja **[miniconda](https://conda.io/en/latest/miniconda.html)** - jest to raczej lekka instalacja, która wspiera menedżera pakietów `conda` do zarządzania różnymi **wirtualnymi środowiskami** Pythona.

Po zainstalowaniu minicondy, sklonuj repozytorium i utwórz wirtualne środowisko, które będzie używane na potrzeby tego kursu:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Korzystanie z Visual Studio Code z rozszerzeniem Python

Ten program nauczania najlepiej jest używać, otwierając go w [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) z [rozszerzeniem Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Uwaga**: Po sklonowaniu i otwarciu katalogu w VS Code, automatycznie zasugeruje Ci instalację rozszerzeń Pythona. Będziesz również musiał zainstalować minicondę, jak opisano powyżej.

> **Uwaga**: Jeśli VS Code zasugeruje ponowne otwarcie repozytorium w kontenerze, powinieneś odmówić tego, aby korzystać z lokalnej instalacji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz również skorzystać ze środowiska Jupyter w przeglądarce na własnym komputerze. Zarówno klasyczny Jupyter, jak i JupyterHub oferują wygodne środowisko deweloperskie z autouzupełnianiem, podświetlaniem kodu itp.

Aby uruchomić Jupyter lokalnie, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```
lub
```bash
jupyterhub
```
Następnie możesz przejść do dowolnego pliku `.ipynb`, otworzyć go i rozpocząć pracę.

### Uruchamianie w kontenerze

Alternatywą dla instalacji Pythona jest uruchomienie kodu w kontenerze. Nasze repozytorium dostarcza specjalny folder `.devcontainer`, który pokazuje, jak zbudować kontener dla tego repozytorium, a VS Code oferuje możliwość ponownego otwarcia kodu w kontenerze. Wymaga to instalacji Dockera i jest bardziej złożone, dlatego zalecamy to bardziej doświadczonym użytkownikom.

## Uruchamianie w Chmurze

Jeśli nie chcesz instalować Pythona lokalnie i masz dostęp do zasobów w chmurze, dobrą alternatywą jest uruchamianie kodu w chmurze. Istnieje kilka sposobów, aby to zrobić:

* Korzystanie z **[GitHub Codespaces](https://github.com/features/codespaces)** – jest to wirtualne środowisko utworzone dla Ciebie na GitHub, dostępne przez przeglądarkę VS Code. Jeśli masz dostęp do Codespaces, możesz po prostu kliknąć przycisk **Code** w repozytorium, uruchomić codespace i szybko zacząć pracę.
* Korzystanie z **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) oferuje darmowe zasoby obliczeniowe w chmurze, dla osób takich jak Ty, aby testować kod z GitHuba. Na stronie głównej jest przycisk umożliwiający otwarcie repozytorium w Binder – przeniesie Cię on szybko na stronę binder, która zbuduje pod spodem kontener i uruchomi interfejs Jupyter w przeglądarce bezproblemowo.

> **Uwaga**: Aby zapobiec nadużyciom, Binder ma zablokowany dostęp do niektórych zasobów sieciowych. Może to uniemożliwić działanie niektórych fragmentów kodu, które pobierają modele i/lub zbiory danych z publicznego internetu. Może być konieczne znalezienie obejść. Dodatkowo, zasoby obliczeniowe oferowane przez Binder są dość podstawowe, więc trening będzie powolny, szczególnie w późniejszych, bardziej złożonych lekcjach.

## Uruchamianie w Chmurze z GPU

Niektóre z późniejszych lekcji w tym programie nauczania bardzo skorzystałyby na wsparciu GPU. Trening modelu, na przykład, może być w przeciwnym razie bardzo powolny. Masz kilka opcji, szczególnie jeśli masz dostęp do chmury poprzez [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) lub poprzez Twoją instytucję:

* Utwórz [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) i połącz się z nią przez Jupyter. Możesz wtedy sklonować repozytorium bezpośrednio na tę maszynę i zacząć naukę. Maszyny wirtualne serii NC mają wsparcie GPU.

> **Uwaga**: Niektóre subskrypcje, w tym Azure for Students, nie zapewniają wsparcia GPU „od ręki”. Może być konieczne zgłoszenie zapytania o dodatkowe rdzenie GPU do pomocy technicznej.

* Utwórz [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) i użyj tam funkcji Notebook. [Ten film](https://azure-for-academics.github.io/quickstart/azureml-papers/) pokazuje, jak sklonować repozytorium do notatnika Azure ML i zacząć go używać.

Możesz również użyć Google Colab, który oferuje darmowe wsparcie GPU, i przesłać tam notatniki Jupyter, aby wykonywać je pojedynczo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że staramy się zapewnić dokładność, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uznany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->