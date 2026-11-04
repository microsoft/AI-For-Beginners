# Kako zagnati kodo

Ta učni načrt vsebuje veliko izvajalnih primerov in laboratorijskih vaj, ki jih boste želeli zagnati. Za to potrebujete sposobnost izvajanja Python kode v Jupyter zvezkih, ki so priloženi temu učnemu načrtu. Za zagon kode imate več možnosti:

## Zagon lokalno na vašem računalniku

Za zagon kode lokalno na vašem računalniku potrebujete nameščen Python. Ena izmed priporočil je namestitev **[miniconda](https://conda.io/en/latest/miniconda.html)** - to je dokaj lahka namestitev, ki podpira upravljalnik paketov `conda` za različna Python **virtualna okolja**.

Ko namestite minicondo, klonirajte repozitorij in ustvarite virtualno okolje za uporabo v tem tečaju:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Opomba za Windows**: Če ustvarjanje okolja spodleti med nameščanjem `gdk-pixbuf` z `UnicodeDecodeError`, ki omenja `gbk` kodočenje, omogočite UTF-8 način v Pythonu v vaši terminalski lupini in poskusite znova. Uporabite sintakso za terminal, ki ga uporabljate:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Ukazni poziv (`cmd.exe`) ali Anaconda poziv:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, vključno z Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Če je neuspešen poskus pustil za sabo `ai4beg` okolje, ga deaktivirajte in odstranite, preden poskusite znova. Najprej uporabite `conda deactivate`, kadar je okolje aktivno:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Uporaba Visual Studio Code z Python razširitvijo

Ta učni načrt je najbolje uporabljati tako, da ga odprete v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) z [Python razširitvijo](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Opomba**: Ko klonirate in odprete imenik v VS Code, vam bo samodejno predlagal namestitev Python razširitev. Prav tako boste morali namestiti minicondo, kot je opisano zgoraj.

> **Opomba**: Če vam VS Code predlaga ponovno odpiranje repozitorija v vsebniku, to zavrnite, da boste uporabljali lokalno namestitev Pythona.

### Uporaba Jupyter v brskalniku

Jupyter okolje lahko uporabite tudi iz brskalnika na vašem računalniku. Tako klasični Jupyter kot JupyterHub nudita priročno razvojno okolje z avtomatskim dopolnjevanjem, poudarjanjem kode itd.

Za zagon Jupyter lokalno pojdite v imenik tečaja in izvedite:

```bash
jupyter notebook
```
ali
```bash
jupyterhub
```
Nato lahko odprete katerokoli od `.ipynb` datotek, jih odprete in začnete z delom.

### Zagon v vsebniku

Ena alternativa namestitvi Pythona je zagon kode v vsebniku. Ker naš repozitorij vsebuje posebno `.devcontainer` mapo, ki vsebuje navodila za gradnjo vsebnika za ta repozitorij, VS Code omogoča ponovno odprtje kode v vsebniku. To zahteva namestitev Dockerja in je bolj kompleksno, zato to priporočamo bolj izkušenim uporabnikom.

## Zagon v oblaku

Če ne želite namestiti Pythona lokalno in imate dostop do oblačnih virov, je dobra alternativa zagon kode v oblaku. Obstaja več načinov, kako to storiti:

* Uporaba **[GitHub Codespaces](https://github.com/features/codespaces)**, ki je virtualno okolje, ustvarjeno za vas na GitHubu, dostopno preko VS Code brskalniškega vmesnika. Če imate dostop do Codespaces, lahko preprosto kliknete gumb **Code** v repozitoriju, začnete codespace in hitro začnete z delom.
* Uporaba **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) ponuja brezplačne računalniške vire v oblaku, da lahko preizkusite kodo na GitHubu. Na uvodni strani je gumb za odprtje repozitorija v Binderju - to vas hitro pripelje do Binder strani, ki bo zgradila osnovni vsebnik in brezhibno zagnala Jupyter spletni vmesnik.

> **Opomba**: Da bi preprečili zlorabe, ima Binder blokiran dostop do nekaterih spletnih virov. To lahko prepreči delovanje nekaterih delov kode, ki pridobivajo modele in/ali podatkovne zbirke z javnega interneta. Morda boste morali poiskati rešitve. Prav tako so računalniški viri, ki jih nudi Binder, dokaj osnovni, zato bo učenje počasno, še posebej v poznejših, bolj zahtevnih lekcijah.

## Zagon v oblaku z GPU-jem

Nekatere poznejše lekcije v tem učnem načrtu bi zelo koristile GPU podporo. Na primer, učenje modela je lahko sicer zelo počasno. Na voljo imate nekaj možnosti, še posebej če imate dostop do oblaka preko [Azure za študente](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ali preko vaše institucije:

* Ustvarite [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) in se povežite nanjo preko Jupyterja. Na stroj lahko neposredno klonirate repozitorij in začnete z učenjem. NC-serija VM-jev ima podporo za GPU.

> **Opomba**: Nekatere naročnine, vključno z Azure za študente, ne nudijo podpore za GPU takoj. Morda boste morali zahtevati dodatna GPU jedra s tehnično podporo.

* Ustvarite [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) in nato uporabite funkcijo Notebook tam. [Ta video](https://azure-for-academics.github.io/quickstart/azureml-papers/) prikazuje, kako klonirati repozitorij v Azure ML notebook in ga začeti uporabljati.

Lahko pa uporabite Google Colab, ki ima nekaj brezplačne GPU podpore, in tam naložite Jupyter zvezke za izvedbo enega za drugim.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->