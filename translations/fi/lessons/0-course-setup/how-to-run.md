<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-28T19:19:29+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "fi"
}
-->
# Kuinka suorittaa koodi

Tämä opintokokonaisuus sisältää paljon suoritettavia esimerkkejä ja harjoituksia, joita haluat varmasti kokeilla. Jotta voit tehdä tämän, sinun täytyy pystyä suorittamaan Python-koodia Jupyter Notebooks -ympäristössä, joka on osa tätä opintokokonaisuutta. Sinulla on useita vaihtoehtoja koodin suorittamiseen:

## Suorita paikallisesti omalla tietokoneellasi

Jos haluat suorittaa koodin paikallisesti omalla tietokoneellasi, sinun täytyy asentaa jokin versio Pythonista. Suosittelen henkilökohtaisesti asentamaan **[miniconda](https://conda.io/en/latest/miniconda.html)** - se on kevyt asennus, joka tukee `conda`-pakettien hallintaa eri Pythonin **virtuaaliympäristöille**.

Kun olet asentanut minicondan, sinun täytyy kloonata arkisto ja luoda virtuaaliympäristö, jota käytetään tässä kurssissa:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code Python-laajennuksella

Todennäköisesti paras tapa käyttää opintokokonaisuutta on avata se [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) -ohjelmassa, jossa on [Python-laajennus](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Huomio**: Kun kloonaat ja avaat hakemiston VS Code -ohjelmassa, se ehdottaa automaattisesti Python-laajennusten asentamista. Sinun täytyy myös asentaa miniconda yllä kuvatulla tavalla.

> **Huomio**: Jos VS Code ehdottaa arkiston avaamista kontissa, sinun täytyy hylätä tämä ja käyttää paikallista Python-asennusta.

### Jupyter-selaimen käyttö

Voit myös käyttää Jupyter-ympäristöä suoraan selaimessa omalla tietokoneellasi. Itse asiassa sekä klassinen Jupyter että Jupyter Hub tarjoavat varsin kätevän kehitysympäristön automaattisen täydennyksen, koodin korostuksen jne. kanssa.

Jotta voit käynnistää Jupyterin paikallisesti, siirry kurssin hakemistoon ja suorita:

```bash
jupyter notebook
```  
tai  
```bash
jupyterhub
```  
Tämän jälkeen voit navigoida mihin tahansa `.ipynb`-tiedostoon, avata sen ja aloittaa työskentelyn.

### Suorittaminen kontissa

Vaihtoehtona Python-asennukselle voit suorittaa koodin kontissa. Koska arkistomme sisältää erityisen `.devcontainer`-kansion, joka ohjeistaa konttien rakentamista tätä arkistoa varten, VS Code tarjoaa mahdollisuuden avata koodi kontissa. Tämä vaatii Dockerin asennuksen ja on hieman monimutkaisempaa, joten suosittelemme tätä kokeneemmille käyttäjille.

## Suorittaminen pilvessä

Jos et halua asentaa Pythonia paikallisesti ja sinulla on pääsy pilvipalveluihin, hyvä vaihtoehto on suorittaa koodi pilvessä. Tässä on muutamia tapoja tehdä tämä:

* Käyttämällä **[GitHub Codespaces](https://github.com/features/codespaces)**, joka on virtuaaliympäristö GitHubissa, ja se on käytettävissä VS Code -selaimen käyttöliittymän kautta. Jos sinulla on pääsy Codespacesiin, voit vain klikata **Code**-painiketta arkistossa, käynnistää Codespacesin ja aloittaa nopeasti.

* Käyttämällä **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) tarjoaa ilmaisia pilvilaskentaresursseja, joiden avulla voit testata GitHubissa olevaa koodia. Etusivulla on painike, jolla voit avata arkiston Binderissa - tämä vie sinut Binder-sivustolle, joka rakentaa taustalla olevan kontin ja käynnistää Jupyterin verkkokäyttöliittymän saumattomasti.

> **Huomio**: Binder estää pääsyn joihinkin verkkoresursseihin väärinkäytön estämiseksi. Tämä saattaa estää koodin toiminnan, joka hakee malleja ja/tai datakokonaisuuksia julkisesta Internetistä. Saatat joutua etsimään kiertotapoja. Lisäksi Binderin tarjoamat laskentaresurssit ovat melko perustasoisia, joten koulutus on hidasta, erityisesti myöhemmissä monimutkaisemmissa oppitunneissa.

## Suorittaminen pilvessä GPU:n kanssa

Jotkut tämän opintokokonaisuuden myöhemmistä oppitunneista hyötyvät suuresti GPU-tuesta, koska muuten koulutus on tuskallisen hidasta. Tässä on muutamia vaihtoehtoja, erityisesti jos sinulla on pääsy pilveen joko [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) -palvelun tai oppilaitoksesi kautta:

* Luo [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ja yhdistä siihen Jupyterin kautta. Voit sitten kloonata arkiston suoraan koneelle ja aloittaa opiskelun. NC-sarjan virtuaalikoneet tukevat GPU:ta.

> **Huomio**: Jotkut tilaukset, mukaan lukien Azure for Students, eivät tarjoa GPU-tukea oletuksena. Saatat joutua pyytämään lisä-GPU-ytimiä teknisen tuen kautta.

* Luo [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ja käytä siellä Notebook-ominaisuutta. [Tämä video](https://azure-for-academics.github.io/quickstart/azureml-papers/) näyttää, kuinka arkisto kloonataan Azure ML -muistikirjaan ja aloitetaan sen käyttö.

Voit myös käyttää Google Colabia, joka tarjoaa jonkin verran ilmaista GPU-tukea, ja ladata Jupyter Notebooks -tiedostoja sinne suorittaaksesi ne yksi kerrallaan.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.