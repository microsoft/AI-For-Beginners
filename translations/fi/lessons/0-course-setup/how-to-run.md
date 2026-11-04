# Kuinka Suorittaa Koodi

Tämä opetussuunnitelma sisältää paljon suoritettavia esimerkkejä ja harjoituksia, joita haluat ehkä suorittaa. Tämän tekemiseen tarvitset mahdollisuuden suorittaa Python-koodia Jupyter-muistikirjoissa, jotka ovat osa tätä opetussuunnitelmaa. Koodin suorittamiseen sinulla on useita vaihtoehtoja:

## Suorita paikallisesti omalla tietokoneellasi

Koodin suorittamiseen paikallisesti tarvitaan Python asennettuna. Yksi suositus on asentaa **[miniconda](https://conda.io/en/latest/miniconda.html)** - se on melko kevyt asennus, joka tukee `conda`-paketinhallintaa eri Python **virtuaaliympäristöissä**.

Kun olet asentanut minicondan, kloonaa repositorio ja luo kurssille oma virtuaaliympäristö:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Windows-muistutus**: Jos ympäristön luominen epäonnistuu `gdk-pixbuf` asennuksen yhteydessä ja saat `UnicodeDecodeError`, joka mainitsee `gbk`-koodekin, ota Pythonin UTF-8 -tila käyttöön terminaalissasi ja yritä uudelleen. Käytä kyseessä olevan terminaalin syntaksia:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Komentokehote (`cmd.exe`) tai Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, mukaan lukien Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Jos epäonnistunut yritys jätti `ai4beg`-ympäristön jälkeensä, poista se käytöstä ja poista kyseinen ympäristö ennen uutta yrittämistä. Käytä ensin `conda deactivate`, kun ympäristö on aktiivinen:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Visual Studio Code ja Python-laajennus

Tätä opetussuunnitelmaa on parasta käyttää avaamalla se [Visual Studio Codessa](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) yhdessä [Python-laajennuksen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) kanssa.

> **Huom:** Kun kloonaat ja avaat hakemiston VS Codessa, se ehdottaa automaattisesti Python-laajennusten asentamista. Sinun pitää myös asentaa miniconda yllä kuvatulla tavalla.

> **Huom:** Jos VS Code ehdottaa repositorion uudelleen avaamista containerissa, sinun tulisi kieltäytyä, jos haluat käyttää paikallista Python-asennusta.

### Jupyterin käyttäminen selaimessa

Voit myös käyttää Jupyter-ympäristöä selaimessa omalla tietokoneellasi. Sekä klassinen Jupyter että JupyterHub tarjoavat kätevän kehitysympäristön, jossa on automaattinen täydennys, koodin korostus jne.

Jupyterin käynnistämiseksi paikallisesti mene kurssihakemistoon ja suorita:

```bash
jupyter notebook
```
tai
```bash
jupyterhub
```
Sen jälkeen voit siirtyä mihin tahansa `.ipynb`-tiedostoon, avata sen ja aloittaa työskentelyn.

### Suorittaminen containerissa

Vaihtoehtona Python-asennukselle on suorittaa koodi containerissa. Repomme sisältää erityisen `.devcontainer`-kansion, joka ohjeistaa containerin rakentamista tätä repositoriota varten, ja VS Code tarjoaa mahdollisuuden avata koodin uudelleen containerissa. Tämä vaatii Dockerin asentamisen ja on myös monimutkaisempi, joten suositamme tätä kokeneemmille käyttäjille.

## Suorittaminen pilvessä

Jos et halua asentaa Pythonia paikallisesti ja sinulla on pääsy pilvipalveluihin, hyvä vaihtoehto on suorittaa koodi pilvessä. Tämä onnistuu usealla eri tavalla:

* Käyttämällä **[GitHub Codespaces](https://github.com/features/codespaces)**, joka on sinulle GitHubissa luotu virtuaaliympäristö, johon pääsee VS Code -selainsovelluksen kautta. Jos sinulla on pääsy Codespaceseihin, voit yksinkertaisesti klikata **Code**-painiketta repossa, käynnistää codespacen ja aloittaa nopeasti.
* Käyttämällä **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) tarjoaa ilmaisia laskentaresursseja pilvessä, joiden avulla voit kokeilla GitHub-koodia. Etusivulla on painike repositorion avaamiseen Binderissä - tämä vie sinut nopeasti binder-sivustolle, joka rakentaa taustalle containerin ja käynnistää Jupyter verkkokäyttöliittymän saumattomasti.

> **Huom:** Binder estää joidenkin verkkopalveluiden pääsyn väärinkäytösten estämiseksi. Tämä saattaa estää joidenkin koodien toimimisen, jotka lataavat malleja ja/tai aineistoja yleisestä Internetistä. Saatat tarvita joitain kiertoteitä. Lisäksi Binderin tarjoamat laskentaresurssit ovat melko perustasoa, joten koulutus on hidasta, erityisesti myöhemmissä, monimutkaisemmissa oppitunneissa.

## Suorittaminen pilvessä GPU:lla

Joistakin tämän opetussuunnitelman myöhemmistä oppitunneista olisi hyötyä GPU-tuesta. Mallien koulutus voi muuten olla tuskastuttavan hidasta. Sinulla on muutamia vaihtoehtoja, erityisesti jos sinulla on pääsy pilveen esimerkiksi [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) kautta tai oppilaitoksesi kautta:

* Luo [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ja yhdistä siihen Jupyteriä käyttäen. Voit sitten kloonata repoon suoraan koneelle ja aloittaa opiskelun. NC-sarjan VM:illä on GPU-tuki.

> **Huom:** Joihinkin tilauksiin, mukaan lukien Azure for Students, ei kuulu GPU-tukea valmiina. Saatat joutua pyytämään lisä-GPU-ytimiä teknisen tuen kautta.

* Luo [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ja käytä sitten siellä Notebook-ominaisuutta. [Tämä video](https://azure-for-academics.github.io/quickstart/azureml-papers/) näyttää, kuinka kloonataan repositorio Azure ML -muistikirjaan ja aloitetaan sen käyttö.

Voit myös käyttää Google Colabia, joka tarjoaa ilmaisen GPU-tuen, ja ladata Jupyter-muistikirjoja sinne suoritettavaksi yksi kerrallaan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->