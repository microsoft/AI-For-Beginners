# Kuinka Suorittaa Koodi

Tämä opetussuunnitelma sisältää paljon suoritettavia esimerkkejä ja labroja, joita haluat todennäköisesti suorittaa. Tätä varten sinun on pystyttävä suorittamaan Python-koodia Jupyter-muistikirjoissa, jotka kuuluvat osana tätä opetussuunnitelmaa. Koodin suorittamiseen on useita vaihtoehtoja:

## Suorita paikallisesti tietokoneellasi

Jotta voit suorittaa koodin paikallisesti tietokoneellasi, tarvitset Python-asennuksen. Yksi suositus on asentaa **[miniconda](https://conda.io/en/latest/miniconda.html)** – se on melko kevyt asennus, joka tukee `conda`-paketinhallintaa erilaisille Pythonin **virtuaaliympäristöille**.

Kun olet asentanut minicondan, kloonaa varasto ja luo virtuaaliympäristö tätä kurssia varten:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code ja Python-laajennus

Tätä opetussuunnitelmaa on parasta käyttää avaamalla se [Visual Studio Codessa](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) yhdessä [Python-laajennuksen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) kanssa.

> **Huomautus**: Kun kloonaat ja avaat hakemiston VS Codessa, se ehdottaa automaattisesti Python-laajennusten asentamista. Sinun on myös asennettava miniconda kuten yllä on kuvattu.

> **Huomautus**: Jos VS Code ehdottaa varaston uudelleenavaamista säiliössä, sinun tulisi kieltäytyä tästä käyttääksesi paikallista Python-asennusta.

### Jupyterin käyttäminen selaimessa

Voit käyttää Jupyter-ympäristöä myös selaimella omalla tietokoneellasi. Sekä perinteinen Jupyter että JupyterHub tarjoavat kätevän kehitysympäristön automaattisen täydennyksen, koodin korostuksen jne. kanssa.

Käynnistääksesi Jupyterin paikallisesti, siirry kurssin hakemistoon ja suorita:

```bash
jupyter notebook
```
tai
```bash
jupyterhub
```
Sen jälkeen voit siirtyä mihin tahansa `.ipynb`-tiedostoon, avata ne ja aloittaa työskentelyn.

### Suorittaminen säiliössä

Yksi vaihtoehto Python-asennukselle on suorittaa koodi säiliössä. Koska varastomme sisältää erityisen `.devcontainer`-kansion, joka ohjeistaa, miten säiliö rakennetaan tälle repositoriolle, VS Code tarjoaa mahdollisuuden avata koodin uudelleen säiliössä. Tämä vaatii Dockerin asennuksen ja on myös monimutkaisempi, joten suosittelemme tätä kokeneemmille käyttäjille.

## Suorittaminen pilvessä

Jos et halua asentaa Pythonia paikallisesti, mutta sinulla on pääsy joihinkin pilviresursseihin, hyvä vaihtoehto on suorittaa koodi pilvessä. Tämä onnistuu monella tavalla:

* Käyttämällä **[GitHub Codespaces](https://github.com/features/codespaces)** -ympäristöä, joka on sinulle luotu virtuaaliympäristö GitHubissa ja johon pääsee VS Code -selaimen kautta. Jos sinulla on pääsy Codespacesiin, voit vain klikata varastossa **Code**-painiketta, aloittaa codespacen ja päästä nopeasti alkuun.
* Käyttämällä **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) tarjoaa ilmaisia pilvilaskentaresursseja ihmisille, jotka haluavat kokeilla jotain koodia GitHubissa. Etusivulla on painike, jolla voi avata repositorion Binderissä – tämä vie sinut nopeasti Binder-sivustolle, joka rakentaa taustalla säiliön ja käynnistää sinulle Jupyter-verkko-rajapinnan saumattomasti.

> **Huomautus**: Väärinkäytösten estämiseksi Binderillä on estetty pääsy tiettyihin verkkoresursseihin. Tämä saattaa estää osaa koodista toimimasta, jos koodi hakee malleja ja/tai aineistoja julkisesta internetistä. Saatat tarvita kiertoteitä. Lisäksi Binderin tarjoamat laskentaresurssit ovat melko perustasoa, joten koulutus on hidasta, erityisesti myöhemmissä, vaativammissa leikkauksissa.

## Suorittaminen pilvessä GPU:n kanssa

Jotkut myöhemmistä tämän opetussuunnitelman oppitunneista hyötyvät suuresti GPU-tuesta. Mallin harjoittelu voi olla muuten tuskallisen hidasta. Vaihtoehtoja on muutamia, erityisesti jos sinulla on pääsy pilveen joko [Azure for Studentsin](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) kautta tai oppilaitoksesi kautta:

* Luo [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ja yhdistä siihen Jupylerin kautta. Voit sitten kloonata repo suoraan koneelle ja aloittaa oppimisen. NC-sarjan virtuaalikoneissa on GPU-tuki.

> **Huomautus**: Joihinkin tilauksiin, mukaan lukien Azure for Students, ei kuulu GPU-tukea oletuksena. Saatat joutua pyytämään lisä-GPU-ytimiä teknisen tuen pyynnöllä.

* Luo [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ja käytä siellä Notebook-ominaisuutta. [Tämä video](https://azure-for-academics.github.io/quickstart/azureml-papers/) näyttää, miten kloonataan repositorio Azure ML -muistikirjaan ja aloitetaan käyttö.

Voit myös käyttää Google Colabia, joka sisältää jonkin verran ilmaista GPU-tukea, ja ladata Jupyter-muistikirjat sinne suorittaaksesi ne yksi kerrallaan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta ota huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattilaisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->