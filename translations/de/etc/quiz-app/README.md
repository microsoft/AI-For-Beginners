# Quizfragen

Diese Quizfragen sind die Vor- und Nachbereitungsquizfragen für den KI-Lehrplan unter https://aka.ms/ai-beginners

## Hinzufügen eines übersetzten Quiz-Sets

Füge eine Quiz-Übersetzung hinzu, indem du passende Quizstrukturen in den Ordnern `assets/translations` erstellst. Die ursprünglichen Quizfragen befinden sich in `assets/translations/en`. Die Quizfragen sind nach Lektionen in mehrere Gruppen unterteilt. Achte darauf, die Nummerierung mit dem entsprechenden Quizabschnitt abzugleichen. Insgesamt gibt es 40 Quizfragen in diesem Lehrplan, beginnend mit der Nummer 0.

Nach dem Bearbeiten der Übersetzungen bearbeite die Datei `index.js` im Übersetzungsordner, um alle Dateien gemäß den Konventionen in `en` zu importieren.

Bearbeite die Datei `index.js` in `assets/translations`, um die neuen übersetzten Dateien zu importieren.

Bearbeite anschließend das Dropdown-Menü in `App.vue` in dieser App, um deine Sprache hinzuzufügen. Passe die lokalisierte Abkürzung an den Ordnernamen deiner Sprache an.

Schließlich bearbeite alle Quiz-Links in den übersetzten Lektionen, falls vorhanden, um diese Lokalisierung als Abfrageparameter hinzuzufügen: z. B. `?loc=fr`.

## Projektsetup

```
npm install
```

### Kompiliert und lädt für die Entwicklung neu

```
npm run serve
```

### Kompiliert und minimiert für die Produktion

```
npm run build
```

### Überprüft und behebt Dateien

```
npm run lint
```

### Konfiguration anpassen

Siehe [Konfigurationsreferenz](https://cli.vuejs.org/config/).

Credits: Dank an die ursprüngliche Version dieser Quiz-App: https://github.com/arpan45/simple-quiz-vue

## Bereitstellung auf Azure

Hier ist eine Schritt-für-Schritt-Anleitung, um dir den Einstieg zu erleichtern:

1. Forke ein GitHub-Repository  
Stelle sicher, dass sich der Code deiner statischen Web-App in deinem GitHub-Repository befindet. Forke dieses Repository.

2. Erstelle eine Azure Static Web App  
- Erstelle ein [Azure-Konto](http://azure.microsoft.com)  
- Gehe zum [Azure-Portal](https://portal.azure.com)  
- Klicke auf „Ressource erstellen“ und suche nach „Static Web App“.  
- Klicke auf „Erstellen“.

3. Konfiguriere die Static Web App  
- Grundlagen:  
  - Abonnement: Wähle dein Azure-Abonnement aus.  
  - Ressourcengruppe: Erstelle eine neue Ressourcengruppe oder verwende eine bestehende.  
  - Name: Gib deiner statischen Web-App einen Namen.  
  - Region: Wähle die Region, die deinen Nutzern am nächsten liegt.

- #### Bereitstellungsdetails:  
  - Quelle: Wähle „GitHub“.  
  - GitHub-Konto: Autorisiere Azure, auf dein GitHub-Konto zuzugreifen.  
  - Organisation: Wähle deine GitHub-Organisation aus.  
  - Repository: Wähle das Repository, das deine statische Web-App enthält.  
  - Branch: Wähle den Branch, von dem aus du bereitstellen möchtest.

- #### Build-Details:  
  - Build-Voreinstellungen: Wähle das Framework, mit dem deine App erstellt wurde (z. B. React, Angular, Vue usw.).  
  - App-Standort: Gib den Ordner an, der deinen App-Code enthält (z. B. /, wenn er sich im Root-Verzeichnis befindet).  
  - API-Standort: Falls du eine API hast, gib deren Standort an (optional).  
  - Ausgabe-Standort: Gib den Ordner an, in dem die Build-Ausgabe generiert wird (z. B. build oder dist).

4. Überprüfen und Erstellen  
Überprüfe deine Einstellungen und klicke auf „Erstellen“. Azure wird die erforderlichen Ressourcen einrichten und einen GitHub Actions-Workflow in deinem Repository erstellen.

5. GitHub Actions-Workflow  
Azure erstellt automatisch eine GitHub Actions-Workflow-Datei in deinem Repository (.github/workflows/azure-static-web-apps-<name>.yml). Dieser Workflow übernimmt den Build- und Bereitstellungsprozess.

6. Überwache die Bereitstellung  
Gehe zum Tab „Actions“ in deinem GitHub-Repository.  
Du solltest sehen, dass ein Workflow ausgeführt wird. Dieser Workflow wird deine statische Web-App auf Azure erstellen und bereitstellen.  
Sobald der Workflow abgeschlossen ist, ist deine App unter der bereitgestellten Azure-URL live.

### Beispiel für eine Workflow-Datei

Hier ist ein Beispiel, wie die GitHub Actions-Workflow-Datei aussehen könnte:  
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

### Zusätzliche Ressourcen  
- [Azure Static Web Apps Dokumentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Dokumentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.