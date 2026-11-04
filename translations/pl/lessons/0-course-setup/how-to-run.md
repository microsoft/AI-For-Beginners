# Jak Uruchomić Kod

Ten program nauczania zawiera wiele wykonalnych przykładów i laboratoriów, które zechcesz uruchomić. Aby to zrobić, potrzebujesz możliwości wykonywania kodu Python w Jupyter Notebooks dostarczonych jako część tego programu nauczania. Masz kilka opcji uruchamiania kodu:

## Uruchom lokalnie na swoim komputerze

Aby uruchomić kod lokalnie na swoim komputerze, potrzebna jest instalacja Pythona. Jedną z rekomendacji jest zainstalowanie **[miniconda](https://conda.io/en/latest/miniconda.html)** – jest to dość lekka instalacja wspierająca menedżera pakietów `conda` dla różnych **wirtualnych środowisk** Pythona.

Po zainstalowaniu miniconda, sklonuj repozytorium i utwórz wirtualne środowisko, które będzie używane do tego kursu:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Uwaga dla Windows**: Jeśli tworzenie środowiska zakończy się niepowodzeniem podczas instalowania `gdk-pixbuf` z komunikatem `UnicodeDecodeError` dotyczącym kodowania `gbk`, włącz tryb UTF-8 Pythona w swoim terminalu i spróbuj ponownie. Użyj składni odpowiedniej dla terminala, którego używasz:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Wiersz polecenia (`cmd.exe`) lub Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, w tym Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Jeśli nieudana próba pozostawiła środowisko `ai4beg`, wyłącz je i usuń to środowisko przed ponowną próbą. Użyj `conda deactivate` najpierw, gdy środowisko jest aktywne:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Korzystanie z Visual Studio Code z rozszerzeniem Python

Ten program nauczania najlepiej jest otworzyć w [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) z [rozszerzeniem Pythona](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Uwaga**: Po sklonowaniu i otwarciu katalogu w VS Code, automatycznie zostanie zasugerowana instalacja rozszerzeń Pythona. Trzeba także zainstalować minicondę, jak opisano powyżej.

> **Uwaga**: Jeśli VS Code zasugeruje ponowne otwarcie repozytorium w kontenerze, powinieneś odmówić, aby korzystać z lokalnej instalacji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz także używać środowiska Jupyter z poziomu przeglądarki na własnym komputerze. Zarówno klasyczny Jupyter, jak i JupyterHub oferują wygodne środowisko programistyczne z autouzupełnianiem, podświetlaniem składni itd.

Aby uruchomić Jupyter lokalnie, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```
lub
```bash
jupyterhub
```
Następnie możesz nawigować do dowolnego z plików `.ipynb`, otworzyć je i zacząć pracę.

### Uruchamianie w kontenerze

Alternatywą dla instalacji Pythona może być uruchomienie kodu w kontenerze. Ponieważ nasze repozytorium dostarcza specjalny katalog `.devcontainer`, który instruuje, jak zbudować kontener dla tego repozytorium, VS Code oferuje możliwość ponownego otwarcia kodu w kontenerze. Wymaga to zainstalowania Dockera i jest bardziej złożone, więc zalecamy to bardziej doświadczonym użytkownikom.

## Uruchamianie w chmurze

Jeśli nie chcesz instalować Pythona lokalnie, a masz dostęp do zasobów chmurowych – dobrą alternatywą jest uruchamianie kodu w chmurze. Istnieje kilka sposobów, jak to zrobić:

* Korzystanie z **[GitHub Codespaces](https://github.com/features/codespaces)**, czyli wirtualnego środowiska utworzonego dla Ciebie na GitHubie, dostępnego przez interfejs przeglądarki VS Code. Jeśli masz dostęp do Codespaces, wystarczy kliknąć przycisk **Code** w repozytorium, uruchomić codespace i szybko zacząć pracę.
* Korzystanie z **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) oferuje darmowe zasoby obliczeniowe w chmurze dla takich osób jak Ty, aby testować kod z GitHuba. Na stronie głównej jest przycisk do otwarcia repozytorium w Binder – powinien szybko przenieść Cię na stronę bindera, która zbuduje kontener i uruchomi dla Ciebie interfejs webowy Jupyter bez picu.

> **Uwaga**: Aby zapobiec nadużyciom, Binder ma zablokowany dostęp do niektórych zasobów internetowych. Może to uniemożliwić działanie części kodu, który pobiera modele i/lub zbiory danych z internetu. Może być konieczne znalezienie obejścia. Ponadto zasoby obliczeniowe oferowane przez Binder są dosyć podstawowe, więc trenowanie modeli będzie wolne, szczególnie w późniejszych, bardziej złożonych lekcjach.

## Uruchamianie w chmurze z GPU

Niektóre z późniejszych lekcji w tym programie nauczania bardzo skorzystają ze wsparcia GPU. Trening modeli może być w przeciwnym wypadku bardzo wolny. Masz kilka opcji, zwłaszcza jeśli masz dostęp do chmury przez [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) lub przez swoją instytucję:

* Utwórz [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) i połącz się z nią przez Jupyter. Możesz wtedy sklonować repozytorium bezpośrednio na maszynę i zacząć naukę. Maszyny NC-series mają wsparcie GPU.

> **Uwaga**: Niektóre subskrypcje, w tym Azure for Students, nie oferują wsparcia GPU od razu. Może być konieczne zgłoszenie prośby o dodatkowe rdzenie GPU do wsparcia technicznego.

* Utwórz [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) i użyj tam funkcji Notebook. [Ten film](https://azure-for-academics.github.io/quickstart/azureml-papers/) pokazuje, jak sklonować repozytorium do notebooka Azure ML i zacząć z niego korzystać.

Możesz też użyć Google Colab, który oferuje bezpłatne wsparcie GPU, i tam ładować Jupyter Notebooki do uruchomienia pojedynczo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->