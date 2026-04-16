# Quizy

Te quizy to quizy przed i po wykładach w ramach programu nauczania AI dostępnego na https://aka.ms/ai-beginners

## Dodawanie przetłumaczonego zestawu quizów

Dodaj tłumaczenie quizu, tworząc odpowiadające struktury quizów w folderach `assets/translations`. Kanoniczne quizy znajdują się w `assets/translations/en`. Quizy są podzielone na kilka grup według lekcji. Upewnij się, że numeracja jest zgodna z odpowiednią sekcją quizu. W całym programie nauczania znajduje się 40 quizów, a numeracja zaczyna się od 0.

Po edycji tłumaczeń, edytuj plik index.js w folderze tłumaczeń, aby zaimportować wszystkie pliki zgodnie z konwencjami w `en`.

Edytuj plik `index.js` w `assets/translations`, aby zaimportować nowe przetłumaczone pliki.

Następnie edytuj rozwijane menu w `App.vue` w tej aplikacji, aby dodać swój język. Dopasuj lokalizowaną skróconą nazwę do nazwy folderu dla swojego języka.

Na koniec edytuj wszystkie linki do quizów w przetłumaczonych lekcjach, jeśli istnieją, aby dodać tę lokalizację jako parametr zapytania: `?loc=fr` na przykład.

## Konfiguracja projektu

```
npm install
```

### Kompilacja i automatyczne odświeżanie dla rozwoju

```
npm run serve
```

### Kompilacja i minimalizacja dla produkcji

```
npm run build
```

### Lintowanie i poprawianie plików

```
npm run lint
```

### Dostosowanie konfiguracji

Zobacz [Configuration Reference](https://cli.vuejs.org/config/).

Podziękowania: Podziękowania dla oryginalnej wersji tej aplikacji quizowej: https://github.com/arpan45/simple-quiz-vue

## Wdrażanie na Azure

Oto przewodnik krok po kroku, który pomoże Ci zacząć:

1. Forkowanie repozytorium GitHub
Upewnij się, że kod Twojej aplikacji statycznej znajduje się w Twoim repozytorium GitHub. Zrób fork tego repozytorium.

2. Utwórz statyczną aplikację webową na Azure
- Utwórz [konto Azure](http://azure.microsoft.com)
- Przejdź do [portalu Azure](https://portal.azure.com) 
- Kliknij „Utwórz zasób” i wyszukaj „Static Web App”.
- Kliknij „Utwórz”.

3. Konfiguracja statycznej aplikacji webowej
- Podstawowe: Subskrypcja: Wybierz swoją subskrypcję Azure.
- Grupa zasobów: Utwórz nową grupę zasobów lub użyj istniejącej.
- Nazwa: Podaj nazwę dla swojej statycznej aplikacji webowej.
- Region: Wybierz region najbliższy Twoim użytkownikom.

- #### Szczegóły wdrożenia:
- Źródło: Wybierz „GitHub”.
- Konto GitHub: Autoryzuj Azure do uzyskania dostępu do Twojego konta GitHub.
- Organizacja: Wybierz swoją organizację GitHub.
- Repozytorium: Wybierz repozytorium zawierające kod Twojej statycznej aplikacji webowej.
- Gałąź: Wybierz gałąź, z której chcesz wdrażać.

- #### Szczegóły kompilacji:
- Presety kompilacji: Wybierz framework, na którym oparta jest Twoja aplikacja (np. React, Angular, Vue, itd.).
- Lokalizacja aplikacji: Określ folder zawierający kod Twojej aplikacji (np. / jeśli znajduje się w głównym katalogu).
- Lokalizacja API: Jeśli masz API, określ jego lokalizację (opcjonalne).
- Lokalizacja wyników: Określ folder, w którym generowane są wyniki kompilacji (np. build lub dist).

4. Przegląd i utworzenie
Przejrzyj swoje ustawienia i kliknij „Utwórz”. Azure skonfiguruje niezbędne zasoby i utworzy plik workflow GitHub Actions w Twoim repozytorium.

5. Workflow GitHub Actions
Azure automatycznie utworzy plik workflow GitHub Actions w Twoim repozytorium (.github/workflows/azure-static-web-apps-<name>.yml). Ten workflow zajmie się procesem kompilacji i wdrożenia.

6. Monitorowanie wdrożenia
Przejdź do zakładki „Actions” w swoim repozytorium GitHub.
Powinieneś zobaczyć uruchomiony workflow. Ten workflow skompiluje i wdroży Twoją statyczną aplikację webową na Azure.
Po zakończeniu workflow Twoja aplikacja będzie dostępna pod podanym URL-em Azure.

### Przykładowy plik workflow

Oto przykład, jak może wyglądać plik workflow GitHub Actions:
name: Azure Static Web Apps CI/CD
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "etc/quiz-app # App source code path"
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```

### Dodatkowe zasoby
- [Dokumentacja Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [Dokumentacja GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.