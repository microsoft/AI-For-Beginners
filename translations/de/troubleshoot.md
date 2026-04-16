# AI-For-Beginners Fehlerbehebungshandbuch

Dieses Handbuch hilft Ihnen, häufige Probleme zu lösen, die beim Verwenden oder Beitragen zum [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)-Repository auftreten können. Jedes Problem enthält Hintergrundinformationen, Symptome, Erklärungen und Schritt-für-Schritt-Lösungen.

---

## Inhaltsverzeichnis

- [Allgemeine Probleme](../..)
- [Installationsprobleme](../..)
- [Konfigurationsprobleme](../..)
- [Notebooks ausführen](../..)
- [Leistungsprobleme](../..)
- [Probleme mit der Lehrbuch-Website](../..)
- [Probleme beim Beitragen](../..)
- [FAQ](../..)
- [Hilfe erhalten](../..)

---

## Allgemeine Probleme

### 1. Repository wird nicht richtig geklont

**Hintergrund:** Beim Klonen können Sie das Repository auf Ihren Computer kopieren.

**Symptome:**
- Fehler: `fatal: repository not found`
- Fehler: `Permission denied (publickey)`

**Mögliche Ursachen:**
- Falsche Repository-URL
- Unzureichende Berechtigungen
- SSH-Schlüssel nicht konfiguriert

**Lösungen:**
1. **Überprüfen Sie die Repository-URL.**  
   Verwenden Sie die HTTPS-URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Wechseln Sie zu HTTPS, wenn SSH fehlschlägt.**  
   Wenn Sie `Permission denied (publickey)` sehen, verwenden Sie stattdessen den oben genannten HTTPS-Link.
3. **SSH-Schlüssel konfigurieren (optional).**  
   Wenn Sie SSH verwenden möchten, folgen Sie [GitHubs SSH-Anleitung](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Installationsprobleme

### 2. Probleme mit der Python-Umgebung

**Hintergrund:** Das Repository basiert auf Python und verschiedenen Bibliotheken.

**Symptome:**
- Fehler: `ModuleNotFoundError: No module named '<package>'`
- Importfehler beim Ausführen von Skripten oder Notebooks

**Mögliche Ursachen:**
- Abhängigkeiten nicht installiert
- Falsche Python-Version

**Lösungen:**
1. **Richten Sie eine virtuelle Umgebung ein.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Installieren Sie die Abhängigkeiten.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Überprüfen Sie die Python-Version.**  
   Verwenden Sie Python 3.7 oder neuer.  
   ```bash
   python --version
   ```

### 3. Jupyter ist nicht installiert

**Hintergrund:** Notebooks sind eine zentrale Lernressource.

**Symptome:**
- Fehler: `jupyter: command not found`
- Notebooks lassen sich nicht starten

**Mögliche Ursachen:**
- Jupyter ist nicht installiert

**Lösungen:**
1. **Installieren Sie Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   oder, wenn Sie Anaconda verwenden:
   ```bash
   conda install notebook
   ```
2. **Starten Sie Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Konflikte bei Abhängigkeitsversionen

**Hintergrund:** Projekte können fehlschlagen, wenn Paketversionen nicht übereinstimmen.

**Symptome:**
- Fehler oder Warnungen zu inkompatiblen Versionen

**Mögliche Ursachen:**
- Alte oder widersprüchliche Python-Pakete

**Lösungen:**
1. **Installieren Sie in einer sauberen Umgebung.**  
   Löschen Sie alte venv/conda-Umgebungen und erstellen Sie eine neue.
2. **Verwenden Sie genaue Versionen.**  
   Führen Sie immer aus:
   ```bash
   pip install -r requirements.txt
   ```
   Wenn dies fehlschlägt, installieren Sie fehlende Pakete manuell, wie im README beschrieben.

---

## Konfigurationsprobleme

### 5. Umgebungsvariablen nicht gesetzt

**Hintergrund:** Einige Module benötigen Schlüssel, Tokens oder Konfigurationseinstellungen.

**Symptome:**
- Fehler: `KeyError` oder Warnungen zu fehlender Konfiguration

**Mögliche Ursachen:**
- Erforderliche Umgebungsvariablen nicht gesetzt

**Lösungen:**
1. **Überprüfen Sie `.env.example` oder ähnliche Dateien.**
2. **Erstellen Sie eine `.env`-Datei und füllen Sie die erforderlichen Werte aus.**
3. **Laden Sie Ihr Terminal oder Ihre IDE neu, nachdem Sie Umgebungsvariablen gesetzt haben.**

---

## Notebooks ausführen

### 6. Notebook lässt sich nicht öffnen oder ausführen

**Hintergrund:** Jupyter-Notebooks benötigen eine ordnungsgemäße Einrichtung.

**Symptome:**
- Notebook lässt sich nicht starten
- Browser öffnet sich nicht automatisch

**Mögliche Ursachen:**
- Jupyter ist nicht installiert
- Probleme mit der Browserkonfiguration

**Lösungen:**
1. **Installieren Sie Jupyter (siehe Installationsprobleme oben).**
2. **Öffnen Sie Notebooks manuell.**
   - Kopieren Sie die URL aus dem Terminal (z. B. `http://localhost:8888/?token=...`) und fügen Sie sie in Ihren Browser ein.

### 7. Kernel stürzt ab oder friert ein

**Hintergrund:** Notebook-Kernel können aufgrund von Ressourcenbeschränkungen oder Codefehlern abstürzen.

**Symptome:**
- Kernel stirbt oder startet wiederholt neu
- Speicherfehler

**Mögliche Ursachen:**
- Große Datensätze
- Inkompatibler Code oder Pakete

**Lösungen:**
1. **Starten Sie den Kernel neu.**  
   Verwenden Sie die Schaltfläche "Kernel neu starten" in Jupyter.
2. **Überprüfen Sie die Speichernutzung.**  
   Schließen Sie nicht benötigte Anwendungen.
3. **Führen Sie Notebooks auf Cloud-Plattformen aus.**  
   Verwenden Sie [Google Colab](https://colab.research.google.com/) oder [Azure Notebooks](https://notebooks.azure.com/).

---

## Leistungsprobleme

### 8. Notebooks laufen langsam

**Hintergrund:** Einige KI-Aufgaben erfordern erheblichen Speicher und CPU.

**Symptome:**
- Langsame Ausführung
- Laptop-Lüfter läuft laut

**Mögliche Ursachen:**
- Große Datensätze oder Modelle
- Begrenzte Systemressourcen

**Lösungen:**
1. **Verwenden Sie eine Cloud-Plattform.**
   - Laden Sie das Notebook auf Colab oder Azure Notebooks hoch.
2. **Reduzieren Sie die Datensatzgröße.**
   - Verwenden Sie Beispieldaten zum Üben.
3. **Schließen Sie unnötige Programme.**
   - Geben Sie Systemspeicher frei.

---

## Probleme mit der Lehrbuch-Website

### 9. Kapitel lädt nicht

**Hintergrund:** Das Online-Lehrbuch zeigt Lektionen und Kapitel an.

**Symptome:**
- Ein Kapitel (z. B. Transformers/BERT) fehlt oder lässt sich nicht öffnen

**Bekanntes Problem:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): „18 Transformers. BERT. kann auf der Lehrbuch-Website nicht geöffnet werden.“ Verursacht durch einen Dateinamenfehler (`READMEtransformers.md` statt `README.md`).

**Lösungen:**
1. **Überprüfen Sie Dateinamenfehler.**  
   Wenn Sie Mitwirkender sind, stellen Sie sicher, dass Kapiteldateien `README.md` heißen.
2. **Melden Sie fehlende Dateien.**  
   Öffnen Sie ein GitHub-Issue mit dem Kapitelnamen und den Fehlerdetails.

---

## Probleme beim Beitragen

### 10. PR wird nicht akzeptiert oder Builds schlagen fehl

**Hintergrund:** Beiträge müssen Tests bestehen und Richtlinien einhalten.

**Symptome:**
- Pull-Request abgelehnt
- CI/CD-Pipeline-Fehler

**Mögliche Ursachen:**
- Fehlende Tests
- Nicht eingehaltene Codierungsstandards

**Lösungen:**
1. **Lesen Sie die Beitragsrichtlinien.**
   - Befolgen Sie die [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) des Repositorys.
2. **Führen Sie Tests lokal aus, bevor Sie Änderungen hochladen.**
3. **Überprüfen Sie Linting-Regeln oder Formatierungsanforderungen.**

---

## FAQ

### Wo finde ich Hilfe zu spezifischen Modulen?
- Jedes Modul hat normalerweise eine eigene README-Datei. Beginnen Sie dort mit Einrichtung und Nutzungstipps.

### Wie melde ich einen Fehler oder fordere ein Feature an?
- [Öffnen Sie ein GitHub-Issue](https://github.com/microsoft/AI-For-Beginners/issues/new) mit einer klaren Beschreibung und Schritten zur Reproduktion.

### Kann ich um Hilfe bitten, wenn mein Problem nicht aufgeführt ist?
- Ja! Suchen Sie zuerst nach bestehenden Issues, und wenn Sie Ihr Problem nicht finden, erstellen Sie ein neues Issue.

---

## Hilfe erhalten

- **Issues überprüfen:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Fragen stellen:** Verwenden Sie GitHub Discussions oder öffnen Sie ein Issue.
- **Community:** Siehe Repository-Links für Chat-/Forum-Optionen.

---

_Letzte Aktualisierung: 20.09.2025_

---

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.