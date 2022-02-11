# Quizzes

These quizzes are the pre- and post-lecture quizzes for the data science curriculum at https://aka.ms/datascience-beginners
## Adding a translated quiz set

Add a quiz translation by creating matching quiz structures in the `assets/translations` folders. The canonical quizzes are in `assets/translations/en`. The quizzes are broken into several groupings. Make sure to align the numbering with the proper quiz section. There are 40 quizzes total in this curriculum, with the count starting at 0.

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
