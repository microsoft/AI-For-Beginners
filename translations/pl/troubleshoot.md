# Przewodnik rozwiązywania problemów AI-For-Beginners

Ten przewodnik pomoże Ci rozwiązać typowe problemy napotykane podczas korzystania lub współtworzenia repozytorium [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners). Każdy problem zawiera tło, objawy, wyjaśnienia oraz krok po kroku rozwiązania.

---

## Spis treści

- [Problemy ogólne](../..)
- [Problemy z instalacją](../..)
- [Problemy z konfiguracją](../..)
- [Uruchamianie notebooków](../..)
- [Problemy z wydajnością](../..)
- [Problemy z witryną podręcznika](../..)
- [Problemy z wkładem](../..)
- [FAQ](../..)
- [Uzyskiwanie pomocy](../..)

---

## Problemy ogólne

### 1. Repozytorium nie klonuje się poprawnie

**Tło:** Klonowanie pozwala na skopiowanie repozytorium na Twój komputer.

**Objawy:**
- Błąd: `fatal: repository not found`
- Błąd: `Permission denied (publickey)`

**Możliwe przyczyny:**
- Nieprawidłowy URL repozytorium
- Brak wystarczających uprawnień
- Nie skonfigurowane klucze SSH

**Rozwiązania:**
1. **Sprawdź URL repozytorium.**  
   Użyj URL HTTPS:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Przełącz na HTTPS, jeśli SSH zawodzi.**  
   Jeśli widzisz `Permission denied (publickey)`, użyj powyższego linku HTTPS zamiast SSH.
3. **Skonfiguruj klucze SSH (opcjonalnie).**  
   Jeśli chcesz używać SSH, postępuj zgodnie z [przewodnikiem SSH GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Problemy z instalacją

### 2. Problemy z środowiskiem Python

**Tło:** Repozytorium opiera się na Pythonie i różnych bibliotekach.

**Objawy:**
- Błąd: `ModuleNotFoundError: No module named '<package>'`
- Błędy importu podczas uruchamiania skryptów lub notebooków

**Możliwe przyczyny:**
- Nie zainstalowane zależności
- Nieprawidłowa wersja Pythona

**Rozwiązania:**
1. **Utwórz wirtualne środowisko.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Zainstaluj zależności.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Sprawdź wersję Pythona.**  
   Użyj Pythona 3.7 lub nowszego.  
   ```bash
   python --version
   ```

### 3. Jupyter nie jest zainstalowany

**Tło:** Notebooki są kluczowym zasobem edukacyjnym.

**Objawy:**
- Błąd: `jupyter: command not found`
- Notebooki nie uruchamiają się

**Możliwe przyczyny:**
- Jupyter nie jest zainstalowany

**Rozwiązania:**
1. **Zainstaluj Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   lub, jeśli używasz Anacondy:
   ```bash
   conda install notebook
   ```
2. **Uruchom Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Konflikty wersji zależności

**Tło:** Projekty mogą przestać działać, jeśli wersje pakietów są niezgodne.

**Objawy:**
- Błędy lub ostrzeżenia dotyczące niekompatybilnych wersji

**Możliwe przyczyny:**
- Stare lub konfliktujące pakiety Pythona

**Rozwiązania:**
1. **Zainstaluj w czystym środowisku.**  
   Usuń stare venv/conda env i utwórz nowe.
2. **Używaj dokładnych wersji.**  
   Zawsze uruchamiaj:
   ```bash
   pip install -r requirements.txt
   ```
   Jeśli to zawiedzie, ręcznie zainstaluj brakujące pakiety zgodnie z README.

---

## Problemy z konfiguracją

### 5. Zmienne środowiskowe nie są ustawione

**Tło:** Niektóre moduły mogą wymagać kluczy, tokenów lub ustawień konfiguracyjnych.

**Objawy:**
- Błąd: `KeyError` lub ostrzeżenia o brakującej konfiguracji

**Możliwe przyczyny:**
- Wymagane zmienne środowiskowe nie są ustawione

**Rozwiązania:**
1. **Sprawdź pliki `.env.example` lub podobne.**
2. **Utwórz plik `.env` i wypełnij wymagane wartości.**
3. **Przeładuj terminal lub IDE po ustawieniu zmiennych środowiskowych.**

---

## Uruchamianie notebooków

### 6. Notebook nie otwiera się lub nie działa

**Tło:** Notebooki Jupyter wymagają odpowiedniej konfiguracji.

**Objawy:**
- Notebook nie uruchamia się
- Przeglądarka nie otwiera się automatycznie

**Możliwe przyczyny:**
- Jupyter nie jest zainstalowany
- Problemy z konfiguracją przeglądarki

**Rozwiązania:**
1. **Zainstaluj Jupyter (patrz Problemy z instalacją powyżej).**
2. **Otwórz notebooki ręcznie.**
   - Skopiuj URL z terminala (np. `http://localhost:8888/?token=...`) i wklej go do przeglądarki.

### 7. Kernel się zawiesza lub crashuje

**Tło:** Kernels notebooków mogą się zawieszać z powodu ograniczeń zasobów lub błędów w kodzie.

**Objawy:**
- Kernel umiera lub restartuje się wielokrotnie
- Błędy związane z brakiem pamięci

**Możliwe przyczyny:**
- Duże zestawy danych
- Niekompatybilny kod lub pakiety

**Rozwiązania:**
1. **Zrestartuj kernel.**  
   Użyj przycisku "Restart Kernel" w Jupyter.
2. **Sprawdź użycie pamięci.**  
   Zamknij nieużywane aplikacje.
3. **Uruchamiaj notebooki na platformach chmurowych.**  
   Użyj [Google Colab](https://colab.research.google.com/) lub [Azure Notebooks](https://notebooks.azure.com/).

---

## Problemy z wydajnością

### 8. Notebooki działają wolno

**Tło:** Niektóre zadania AI wymagają dużej ilości pamięci i CPU.

**Objawy:**
- Wolne wykonywanie
- Głośna praca wentylatora laptopa

**Możliwe przyczyny:**
- Duże zestawy danych lub modele
- Ograniczone zasoby systemowe

**Rozwiązania:**
1. **Użyj platformy chmurowej.**
   - Prześlij notebook na Colab lub Azure Notebooks.
2. **Zmniejsz rozmiar zestawu danych.**
   - Użyj danych próbnych do ćwiczeń.
3. **Zamknij niepotrzebne programy.**
   - Zwolnij pamięć RAM systemu.

---

## Problemy z witryną podręcznika

### 9. Rozdział się nie ładuje

**Tło:** Podręcznik online wyświetla lekcje i rozdziały.

**Objawy:**
- Rozdział (np. Transformers/BERT) jest brakujący lub nie otwiera się

**Znany problem:**  
- [Problem #303](https://github.com/microsoft/AI-For-Beginners/issues/303): „18 Transformers. BERT. nie można otworzyć na stronie podręcznika.” Spowodowane błędem nazwy pliku (`READMEtransformers.md` zamiast `README.md`).

**Rozwiązania:**
1. **Sprawdź błędy w nazwach plików.**  
   Jeśli jesteś współtwórcą, upewnij się, że pliki rozdziałów są nazwane `README.md`.
2. **Zgłoś brakujące pliki.**  
   Otwórz problem na GitHub z nazwą rozdziału i szczegółami błędu.

---

## Problemy z wkładem

### 10. PR nie został zaakceptowany lub buildy zawiodły

**Tło:** Wkłady muszą przejść testy i spełniać wytyczne.

**Objawy:**
- Pull request odrzucony
- Błędy w pipeline CI/CD

**Możliwe przyczyny:**
- Nieudane testy
- Nieprzestrzeganie standardów kodowania

**Rozwiązania:**
1. **Przeczytaj wytyczne dotyczące wkładu.**
   - Postępuj zgodnie z [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) repozytorium.
2. **Uruchom testy lokalnie przed przesłaniem.**
3. **Sprawdź zasady lintingu lub wymagania dotyczące formatowania.**

---

## FAQ

### Gdzie mogę znaleźć pomoc dla konkretnych modułów?
- Każdy moduł zazwyczaj ma własny README. Zacznij tam, aby uzyskać wskazówki dotyczące konfiguracji i użytkowania.

### Jak zgłosić błąd lub poprosić o funkcję?
- [Otwórz problem na GitHub](https://github.com/microsoft/AI-For-Beginners/issues/new) z jasnym opisem i krokami do odtworzenia.

### Czy mogę poprosić o pomoc, jeśli mój problem nie jest wymieniony?
- Tak! Najpierw przeszukaj istniejące problemy, a jeśli nie znajdziesz swojego problemu, utwórz nowy.

---

## Uzyskiwanie pomocy

- **Sprawdź problemy:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Zadaj pytania:** Użyj GitHub Discussions lub otwórz problem.
- **Społeczność:** Zobacz linki repozytorium do opcji czatu/forum.

---

_Ostatnia aktualizacja: 2025-09-20_

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.