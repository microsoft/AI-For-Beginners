# Quizzes

These quizzes are the pre- and post-lecture quizzes for the AI curriculum at https://aka.ms/ai-beginners

## Adding a translated quiz set

Add a quiz translation by creating matching quiz structures in the `assets/translations` folders. The canonical quizzes are in `assets/translations/en`. The quizzes are broken into several groupings by lesson. Make sure to align the numbering with the proper quiz section. There are 40 quizzes total in this curriculum, with the count starting at 0.

After editing the translations, edit the index.js file in the translation folder to import all the files following the conventions in `en`.

Edit the `index.js` file in `assets/translations` to import the new translated files.

Then, edit the dropdown in `App.vue` in this app to add your language. Match the localized abbreviation to the folder name for your language.

Finally, edit all the quiz links in the translated lessons, if they exist, to include this localization as a query parameter: `?loc=fr` for example.

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

Credits: Thanks to the original version of this quiz app: https://github.com/arpan45/simple-quiz-vue

## Deploying to Azure

Here’s a step-by-step guide to help you get started:

1. Fork the a GitHub Repository
Ensure your static web app code is in your GitHub repository. Fork this repository.

2. Create an Azure Static Web App
- Create and [Azure account](http://azure.microsoft.com)
- Go to the [Azure portal](https://portal.azure.com) 
- Click on “Create a resource” and search for “Static Web App”.
- Click “Create”.

3. Configure the Static Web App
- Basics: Subscription: Select your Azure subscription.
- Resource Group: Create a new resource group or use an existing one.
- Name: Provide a name for your static web app.
- Region: Choose the region closest to your users.

- #### Deployment Details:
- Source: Select “GitHub”.
- GitHub Account: Authorize Azure to access your GitHub account.
- Organization: Select your GitHub organization.
- Repository: Choose the repository containing your static web app.
- Branch: Select the branch you want to deploy from.

- #### Build Details:
- Build Presets: Choose the framework your app is built with (e.g., React, Angular, Vue, etc.).
- App Location: Specify the folder containing your app code (e.g., / if it’s in the root).
- API Location: If you have an API, specify its location (optional).
- Output Location: Specify the folder where the build output is generated (e.g., build or dist).

4. Review and Create
Review your settings and click “Create”. Azure will set up the necessary resources and create a GitHub Actions workflow in your repository.

5. GitHub Actions Workflow
Azure will automatically create a GitHub Actions workflow file in your repository (.github/workflows/azure-static-web-apps-<name>.yml). This workflow will handle the build and deployment process.

6. Monitor the Deployment
Go to the “Actions” tab in your GitHub repository.
You should see a workflow running. This workflow will build and deploy your static web app to Azure.
Once the workflow completes, your app will be live on the provided Azure URL.

### Example Workflow File

Here’s an example of what the GitHub Actions workflow file might look like:
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

### Additional Resources
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [GitHub Actions Documentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)
