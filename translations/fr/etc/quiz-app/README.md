# Quiz

Ces quiz sont les quiz pré- et post-cours pour le programme d'IA disponible sur https://aka.ms/ai-beginners

## Ajouter un ensemble de quiz traduit

Ajoutez une traduction de quiz en créant des structures de quiz correspondantes dans les dossiers `assets/translations`. Les quiz de référence se trouvent dans `assets/translations/en`. Les quiz sont divisés en plusieurs groupes par leçon. Assurez-vous d'aligner la numérotation avec la section de quiz appropriée. Il y a un total de 40 quiz dans ce programme, avec une numérotation commençant à 0.

Après avoir modifié les traductions, éditez le fichier index.js dans le dossier de traduction pour importer tous les fichiers en suivant les conventions de `en`.

Modifiez le fichier `index.js` dans `assets/translations` pour importer les nouveaux fichiers traduits.

Ensuite, modifiez le menu déroulant dans `App.vue` de cette application pour ajouter votre langue. Faites correspondre l'abréviation localisée au nom du dossier de votre langue.

Enfin, modifiez tous les liens des quiz dans les leçons traduites, si elles existent, pour inclure cette localisation comme paramètre de requête : `?loc=fr` par exemple.

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

### Analyse et correction des fichiers

```
npm run lint
```

### Personnaliser la configuration

Voir [Référence de configuration](https://cli.vuejs.org/config/).

Crédits : Merci à la version originale de cette application de quiz : https://github.com/arpan45/simple-quiz-vue

## Déploiement sur Azure

Voici un guide étape par étape pour vous aider à démarrer :

1. Forker un dépôt GitHub  
Assurez-vous que le code de votre application web statique se trouve dans votre dépôt GitHub. Forkez ce dépôt.

2. Créer une application web statique Azure  
- Créez un [compte Azure](http://azure.microsoft.com)  
- Accédez au [portail Azure](https://portal.azure.com)  
- Cliquez sur "Créer une ressource" et recherchez "Application Web Statique".  
- Cliquez sur "Créer".  

3. Configurer l'application web statique  
- **Informations de base** :  
  - Abonnement : Sélectionnez votre abonnement Azure.  
  - Groupe de ressources : Créez un nouveau groupe de ressources ou utilisez-en un existant.  
  - Nom : Donnez un nom à votre application web statique.  
  - Région : Choisissez la région la plus proche de vos utilisateurs.  

- **Détails du déploiement** :  
  - Source : Sélectionnez "GitHub".  
  - Compte GitHub : Autorisez Azure à accéder à votre compte GitHub.  
  - Organisation : Sélectionnez votre organisation GitHub.  
  - Dépôt : Choisissez le dépôt contenant votre application web statique.  
  - Branche : Sélectionnez la branche à partir de laquelle vous souhaitez déployer.  

- **Détails de la construction** :  
  - Préréglages de construction : Choisissez le framework avec lequel votre application est construite (par ex., React, Angular, Vue, etc.).  
  - Emplacement de l'application : Spécifiez le dossier contenant le code de votre application (par ex., / si c'est à la racine).  
  - Emplacement de l'API : Si vous avez une API, spécifiez son emplacement (optionnel).  
  - Emplacement de sortie : Spécifiez le dossier où la sortie de la construction est générée (par ex., build ou dist).  

4. Examiner et créer  
Examinez vos paramètres et cliquez sur "Créer". Azure configurera les ressources nécessaires et créera un workflow GitHub Actions dans votre dépôt.

5. Workflow GitHub Actions  
Azure créera automatiquement un fichier de workflow GitHub Actions dans votre dépôt (.github/workflows/azure-static-web-apps-<nom>.yml). Ce workflow gérera le processus de construction et de déploiement.

6. Surveiller le déploiement  
Accédez à l'onglet "Actions" dans votre dépôt GitHub.  
Vous devriez voir un workflow en cours d'exécution. Ce workflow construira et déploiera votre application web statique sur Azure.  
Une fois le workflow terminé, votre application sera en ligne à l'URL fournie par Azure.

### Exemple de fichier de workflow

Voici un exemple de ce à quoi pourrait ressembler le fichier de workflow GitHub Actions :  
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
- [Documentation GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.