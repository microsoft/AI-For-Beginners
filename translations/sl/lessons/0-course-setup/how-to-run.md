# Kako zagnati kodo

Ta učni načrt vsebuje veliko izvajalnih primerov in laboratorijskih vaj, ki jih boste želeli zagnati. Da bi to naredili, morate imeti možnost izvajanja Python kode v Jupyter beležnicah, ki so vključene v ta učni načrt. Za izvajanje kode imate več možnosti:

## Zagon lokalno na vašem računalniku

Za lokalni zagon kode na vašem računalniku je potrebna namestitev Pythona. Ena izmed priporočil je namestitev **[miniconda](https://conda.io/en/latest/miniconda.html)** – gre za dokaj lahko namestitev, ki podpira upravitelja paketov `conda` za različna Python **virtualna okolja**.

Ko namestite minicondo, klonirajte repozitorij in ustvarite virtualno okolje, ki bo uporabljeno za ta tečaj:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Uporaba Visual Studio Code z razširitvijo Python

Ta učni načrt je najbolje uporabljati, ko ga odprete v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) z [razširitvijo Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Opomba**: Ko klonirate in odprete mapo v VS Code, vam bo samodejno predlagal, da namestite Python razširitve. Prav tako boste morali namestiti minicondo, kot je opisano zgoraj.

> **Opomba**: Če vam VS Code predlaga, da ponovno odprete repozitorij v vsebniku, to zavrnite, da uporabite lokalno namestitev Pythona.

### Uporaba Jupyter v brskalniku

Lahko uporabite tudi Jupyter okolje prek brskalnika na vašem računalniku. Tako klasični Jupyter kot JupyterHub nudita priročno razvojno okolje z avtomatskim dokončevanjem, poudarkom kode itd.

Za zagon Juypterja lokalno pojdite v mapo s tečajem in izvedite:

```bash
jupyter notebook
```
ali
```bash
jupyterhub
```
Nato lahko odprete katerokoli `.ipynb` datoteko in začnete z delom.

### Zagon v vsebniku

Ena alternativa lokalni namestitvi Pythona je zagon kode v vsebniku. Ker naš repozitorij vsebuje posebno mapo `.devcontainer`, ki navodila za gradnjo vsebnika za ta repozitorij, VS Code ponuja možnost ponovnega odpiranja kode v vsebniku. To zahteva namestitev Dockerja in je nekoliko bolj zapleteno, zato priporočamo to bolj izkušenim uporabnikom.

## Zagon v oblaku

Če ne želite namestiti Pythona lokalno in imate dostop do oblačnih virov, je dobra alternativa zagon kode v oblaku. Obstaja več načinov, kako to storite:

* Uporaba **[GitHub Codespaces](https://github.com/features/codespaces)**, ki je virtualno okolje, ustvarjeno za vas na GitHubu, dostopno prek brskalniškega vmesnika VS Code. Če imate dostop do Codespaces, lahko preprosto kliknete gumb **Code** v repozitoriju, začnete codespace in kmalu zaženete okolje.
* Uporaba **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) nudi brezplačne računalniške vire v oblaku, da lahko uporabniki, kot ste vi, preizkusijo kodo na GitHubu. Na začetni strani je gumb za odpiranje repozitorija v Binderju – s tem boste hitro preusmerjeni na Binder spletno mesto, ki bo zgradilo osnovni vsebnik in brez težav zagnalo Jupyter spletni vmesnik.

> **Opomba**: Da bi preprečili zlorabe, Binder blokira dostop do določenih spletnih virov. To lahko prepreči delovanje nekaterih kod, ki nalagajo modele in/ali podatkovne nabore iz interneta. Morda boste morali poiskati kakšne rešitve. Prav tako so računalniški viri, ki jih nudi Binder, precej osnovni, zato bo učenje zanje počasnejše, zlasti v kasnejših, bolj zahtevnih lekcijah.

## Zagon v oblaku z GPU

Nekatere kasnejše lekcije tega učnega načrta bi zelo koristile podporo GPU. Na primer, treniranje modelov je drugače lahko zelo počasen proces. Nekaj možnosti imate še posebej, če imate dostop do oblačnih virov preko [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ali vaše institucije:

* Ustvarite [virtualni stroj za znanost o podatkih](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) in se povežite z njim prek Jupyter. Nato lahko klonirate repozitorij neposredno na stroj in začnete z učenjem. NC-serije VM-jev imajo podporo za GPU.

> **Opomba**: Nekatere naročnine, vključno z Azure for Students, ne zagotavljajo podpore za GPU privzeto. Morda boste morali preko tehnične podpore zaprositi za dodatna GPU jedra.

* Ustvarite [delovno okolje Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) in uporabite funkcijo beležnice tam. [Ta video](https://azure-for-academics.github.io/quickstart/azureml-papers/) prikazuje, kako klonirati repozitorij v Azure ML beležnico in začeti z uporabo.

Lahko uporabite tudi Google Colab, ki nudi nekaj brezplačne podpore za GPU, in naložite Jupyter beležnice, da jih izvajate eno za drugo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
To besedilo je bilo prevedeno z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvorno jeziku velja za zanesljiv vir. Za pomembne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne razlage, ki nastanejo zaradi uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->