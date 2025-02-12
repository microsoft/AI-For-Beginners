# Quiz

Ces quiz sont les quiz pré et post-conférence pour le programme d'IA à https://aka.ms/ai-beginners

## Ajouter un ensemble de quiz traduit

Ajoutez une traduction de quiz en créant des structures de quiz correspondantes dans les dossiers `assets/translations`. Les quiz canoniques se trouvent dans `assets/translations/en`. Les quiz sont répartis en plusieurs groupes par leçon. Assurez-vous d'aligner la numérotation avec la section de quiz appropriée. Il y a un total de 40 quiz dans ce programme, le compte commençant à 0.

Après avoir modifié les traductions, éditez le fichier index.js dans le dossier de traduction pour importer tous les fichiers selon les conventions de `en`.

Modifiez le fichier `index.js` dans `assets/translations` pour importer les nouveaux fichiers traduits.

Ensuite, modifiez le menu déroulant dans `App.vue` dans cette application pour ajouter votre langue. Faites correspondre l'abréviation localisée au nom du dossier pour votre langue.

Enfin, modifiez tous les liens de quiz dans les leçons traduites, s'ils existent, pour inclure cette localisation en tant que paramètre de requête : `?loc=fr` par exemple.

## Configuration du projet

```
npm install
```

### Compilation et rechargement à chaud pour le développement

```
npm run serve
```

### Compilation et minification pour la production

```
npm run build
```

### Vérifie et corrige les fichiers

```
npm run lint
```

### Personnaliser la configuration

Voir [Référence de configuration](https://cli.vuejs.org/config/).

Crédits : Merci à la version originale de cette application de quiz : https://github.com/arpan45/simple-quiz-vue

## Déploiement sur Azure

Voici un guide étape par étape pour vous aider à commencer :

1. Forkez un dépôt GitHub
Assurez-vous que le code de votre application web statique est dans votre dépôt GitHub. Forkez ce dépôt.

2. Créez une application web statique Azure
- Créez un [compte Azure](http://azure.microsoft.com)
- Allez sur le [portail Azure](https://portal.azure.com) 
- Cliquez sur « Créer une ressource » et recherchez « Application web statique ».
- Cliquez sur « Créer ».

3. Configurez l'application web statique
- Bases : Abonnement : Sélectionnez votre abonnement Azure.
- Groupe de ressources : Créez un nouveau groupe de ressources ou utilisez un groupe existant.
- Nom : Fournissez un nom pour votre application web statique.
- Région : Choisissez la région la plus proche de vos utilisateurs.

- #### Détails du déploiement :
- Source : Sélectionnez « GitHub ».
- Compte GitHub : Autorisez Azure à accéder à votre compte GitHub.
- Organisation : Sélectionnez votre organisation GitHub.
- Dépôt : Choisissez le dépôt contenant votre application web statique.
- Branche : Sélectionnez la branche à partir de laquelle vous souhaitez déployer.

- #### Détails de la construction :
- Préréglages de construction : Choisissez le framework avec lequel votre application est construite (par exemple, React, Angular, Vue, etc.).
- Emplacement de l'application : Spécifiez le dossier contenant le code de votre application (par exemple, / s'il est à la racine).
- Emplacement de l'API : Si vous avez une API, spécifiez son emplacement (facultatif).
- Emplacement de sortie : Spécifiez le dossier où la sortie de la construction est générée (par exemple, build ou dist).

4. Examinez et créez
Examinez vos paramètres et cliquez sur « Créer ». Azure configurera les ressources nécessaires et créera un flux de travail GitHub Actions dans votre dépôt.

5. Flux de travail GitHub Actions
Azure créera automatiquement un fichier de flux de travail GitHub Actions dans votre dépôt (.github/workflows/azure-static-web-apps-<name>.yml). Ce flux de travail gérera le processus de construction et de déploiement.

6. Surveillez le déploiement
Allez dans l'onglet « Actions » de votre dépôt GitHub.
Vous devriez voir un flux de travail en cours d'exécution. Ce flux de travail construira et déploiera votre application web statique sur Azure.
Une fois le flux de travail terminé, votre application sera en ligne sur l'URL Azure fournie.

### Exemple de fichier de flux de travail

Voici un exemple de ce à quoi le fichier de flux de travail GitHub Actions pourrait ressembler :
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

### Ressources supplémentaires
- [Documentation des applications web statiques Azure](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [Documentation de GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'IA. Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue natale doit être considéré comme la source autoritaire. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.