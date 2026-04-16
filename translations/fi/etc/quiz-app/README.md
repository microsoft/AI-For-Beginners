# Visailut

Nämä visailut ovat AI-opetussuunnitelman ennen ja jälkeen luentojen tehtäviä osoitteessa https://aka.ms/ai-beginners

## Käännetyn visailusarjan lisääminen

Lisää visailukäännös luomalla vastaavat visailurakenteet `assets/translations`-kansioihin. Alkuperäiset visailut löytyvät `assets/translations/en`-kansiosta. Visailut on jaettu useisiin ryhmiin oppituntien mukaan. Varmista, että numerointi vastaa oikeaa visailuosaa. Tässä opetussuunnitelmassa on yhteensä 40 visailua, ja numerointi alkaa nollasta.

Kun olet muokannut käännöksiä, muokkaa käännöskansion `index.js`-tiedostoa tuodaksesi kaikki tiedostot `en`-kansion käytäntöjen mukaisesti.

Muokkaa `assets/translations`-kansion `index.js`-tiedostoa tuodaksesi uudet käännetyt tiedostot.

Lisäksi muokkaa tämän sovelluksen `App.vue`-tiedoston pudotusvalikkoa lisätäksesi kielesi. Varmista, että paikallinen lyhenne vastaa kielesi kansion nimeä.

Lopuksi muokkaa kaikkia käännettyjen oppituntien visailulinkkejä, jos niitä on, lisäämällä lokalisaatio kyselyparametrina: esimerkiksi `?loc=fr`.

## Projektin asennus

```
npm install
```

### Kääntää ja päivittää automaattisesti kehitystä varten

```
npm run serve
```

### Kääntää ja minimoi tuotantoa varten

```
npm run build
```

### Tarkistaa ja korjaa tiedostoja

```
npm run lint
```

### Mukauta asetuksia

Katso [Configuration Reference](https://cli.vuejs.org/config/).

Kiitokset: Alkuperäisen version tästä visailusovelluksesta on tehnyt: https://github.com/arpan45/simple-quiz-vue

## Julkaisu Azureen

Tässä on vaiheittainen opas, joka auttaa sinua pääsemään alkuun:

1. Haarauta GitHub-repositorio
Varmista, että staattisen verkkosovelluksesi koodi on GitHub-repositoriossasi. Haarauta tämä repositorio.

2. Luo Azure Static Web App
- Luo [Azure-tili](http://azure.microsoft.com)
- Siirry [Azure-portaaliin](https://portal.azure.com) 
- Klikkaa “Create a resource” ja etsi “Static Web App”.
- Klikkaa “Create”.

3. Määritä Static Web App
- Perustiedot: Tilauksen valinta: Valitse Azure-tilauksesi.
- Resurssiryhmä: Luo uusi resurssiryhmä tai käytä olemassa olevaa.
- Nimi: Anna staattiselle verkkosovelluksellesi nimi.
- Alue: Valitse alue, joka on lähimpänä käyttäjiäsi.

- #### Julkaisun tiedot:
- Lähde: Valitse “GitHub”.
- GitHub-tili: Valtuuta Azure käyttämään GitHub-tiliäsi.
- Organisaatio: Valitse GitHub-organisaatiosi.
- Repositorio: Valitse repositorio, joka sisältää staattisen verkkosovelluksesi.
- Haara: Valitse haara, josta haluat julkaista.

- #### Rakennuksen tiedot:
- Rakennusasetukset: Valitse kehys, jolla sovelluksesi on rakennettu (esim. React, Angular, Vue jne.).
- Sovelluksen sijainti: Määritä kansio, joka sisältää sovelluskoodisi (esim. / jos se on juurihakemistossa).
- API-sijainti: Jos sinulla on API, määritä sen sijainti (valinnainen).
- Tulosteen sijainti: Määritä kansio, johon rakennuksen tuloste luodaan (esim. build tai dist).

4. Tarkista ja luo
Tarkista asetuksesi ja klikkaa “Create”. Azure luo tarvittavat resurssit ja luo GitHub Actions -työnkulun repositoriossasi.

5. GitHub Actions -työnkulku
Azure luo automaattisesti GitHub Actions -työnkulun tiedoston repositoriossasi (.github/workflows/azure-static-web-apps-<name>.yml). Tämä työnkulku hoitaa rakennus- ja julkaisuprosessin.

6. Seuraa julkaisua
Siirry GitHub-repositoriosi “Actions”-välilehteen.
Näet työnkulun käynnissä. Tämä työnkulku rakentaa ja julkaisee staattisen verkkosovelluksesi Azureen.
Kun työnkulku on valmis, sovelluksesi on käytettävissä annetussa Azure-URL-osoitteessa.

### Esimerkki työnkulun tiedostosta

Tässä on esimerkki GitHub Actions -työnkulun tiedostosta:
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

### Lisäresurssit
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [GitHub Actions Documentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.