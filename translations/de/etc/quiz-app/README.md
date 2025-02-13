# Quizze

Diese Quizze sind die Vor- und Nach-Lecture-Quizze für das KI-Curriculum unter https://aka.ms/ai-beginners

## Hinzufügen eines übersetzten Quizsets

Fügen Sie eine Quizübersetzung hinzu, indem Sie passende Quizstrukturen in den `assets/translations`-Ordnern erstellen. Die kanonischen Quizze befinden sich in `assets/translations/en`. Die Quizze sind in mehrere Gruppen nach Lektionen unterteilt. Stellen Sie sicher, dass die Nummerierung mit dem entsprechenden Quizabschnitt übereinstimmt. In diesem Curriculum gibt es insgesamt 40 Quizze, beginnend bei 0.

Nach der Bearbeitung der Übersetzungen bearbeiten Sie die index.js-Datei im Übersetzungsordner, um alle Dateien gemäß den Konventionen in `en` zu importieren.

Bearbeiten Sie die `index.js`-Datei in `assets/translations`, um die neuen übersetzten Dateien zu importieren.

Dann bearbeiten Sie das Dropdown-Menü in `App.vue` in dieser App, um Ihre Sprache hinzuzufügen. Passen Sie die lokalisierte Abkürzung an den Ordnernamen Ihrer Sprache an.

Schließlich bearbeiten Sie alle Quizlinks in den übersetzten Lektionen, falls vorhanden, um diese Lokalisierung als Abfrageparameter einzuschließen: `?loc=fr` zum Beispiel.

## Projektsetup

```
npm install
```

### Kompiliert und lädt für die Entwicklung neu

```
npm run serve
```

### Konstruiert und minimiert für die Produktion

```
npm run build
```

### Linter und behebt Dateien

```
npm run lint
```

### Konfiguration anpassen

Siehe [Konfigurationsreferenz](https://cli.vuejs.org/config/).

Credits: Vielen Dank an die ursprüngliche Version dieser Quiz-App: https://github.com/arpan45/simple-quiz-vue

## Bereitstellung in Azure

Hier ist eine Schritt-für-Schritt-Anleitung, um Ihnen den Einstieg zu erleichtern:

1. Forken Sie ein GitHub-Repository
Stellen Sie sicher, dass Ihr Code für die statische Web-App in Ihrem GitHub-Repository vorhanden ist. Forken Sie dieses Repository.

2. Erstellen Sie eine Azure Static Web App
- Erstellen Sie ein [Azure-Konto](http://azure.microsoft.com)
- Gehen Sie zum [Azure-Portal](https://portal.azure.com)
- Klicken Sie auf „Ressource erstellen“ und suchen Sie nach „Static Web App“.
- Klicken Sie auf „Erstellen“.

3. Konfigurieren Sie die Static Web App
- Grundlagen: Abonnement: Wählen Sie Ihr Azure-Abonnement aus.
- Ressourcengruppe: Erstellen Sie eine neue Ressourcengruppe oder verwenden Sie eine vorhandene.
- Name: Geben Sie einen Namen für Ihre statische Web-App an.
- Region: Wählen Sie die Region, die Ihren Nutzern am nächsten ist.

- #### Bereitstellungsdetails:
- Quelle: Wählen Sie „GitHub“.
- GitHub-Konto: Autorisieren Sie Azure, auf Ihr GitHub-Konto zuzugreifen.
- Organisation: Wählen Sie Ihre GitHub-Organisation aus.
- Repository: Wählen Sie das Repository, das Ihre statische Web-App enthält.
- Branch: Wählen Sie den Branch aus, den Sie bereitstellen möchten.

- #### Build-Details:
- Build-Voreinstellungen: Wählen Sie das Framework, mit dem Ihre App erstellt wurde (z. B. React, Angular, Vue usw.).
- App-Standort: Geben Sie den Ordner an, der Ihren App-Code enthält (z. B. /, wenn es sich im Stammverzeichnis befindet).
- API-Standort: Wenn Sie eine API haben, geben Sie deren Standort an (optional).
- Ausgabeort: Geben Sie den Ordner an, in dem die Build-Ausgabe generiert wird (z. B. build oder dist).

4. Überprüfen und Erstellen
Überprüfen Sie Ihre Einstellungen und klicken Sie auf „Erstellen“. Azure wird die erforderlichen Ressourcen einrichten und einen GitHub Actions-Workflow in Ihrem Repository erstellen.

5. GitHub Actions Workflow
Azure wird automatisch eine GitHub Actions-Workflow-Datei in Ihrem Repository erstellen (.github/workflows/azure-static-web-apps-<name>.yml). Dieser Workflow wird den Build- und Bereitstellungsprozess verwalten.

6. Überwachen der Bereitstellung
Gehen Sie zum Tab „Aktionen“ in Ihrem GitHub-Repository. 
Sie sollten einen laufenden Workflow sehen. Dieser Workflow wird Ihre statische Web-App in Azure erstellen und bereitstellen. 
Sobald der Workflow abgeschlossen ist, wird Ihre App unter der angegebenen Azure-URL live sein.

### Beispiel-Workflow-Datei

Hier ist ein Beispiel dafür, wie die GitHub Actions-Workflow-Datei aussehen könnte:
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
- [Dokumentation zu Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [Dokumentation zu GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.