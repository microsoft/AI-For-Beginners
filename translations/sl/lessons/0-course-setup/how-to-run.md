<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-26T00:37:25+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "sl"
}
-->
# Kako zagnati kodo

Ta učni načrt vsebuje veliko primerov kode in laboratorijskih vaj, ki jih boste želeli zagnati. Da bi to storili, potrebujete možnost izvajanja Python kode v Jupyter Notebookih, ki so del tega učnega načrta. Na voljo imate več možnosti za zagon kode:

## Zagon lokalno na vašem računalniku

Za zagon kode lokalno na vašem računalniku morate imeti nameščeno neko različico Pythona. Osebno priporočam namestitev **[miniconda](https://conda.io/en/latest/miniconda.html)** - gre za precej lahkotno namestitev, ki podpira upravitelja paketov `conda` za različna Python **virtualna okolja**.

Ko namestite minicondo, morate klonirati repozitorij in ustvariti virtualno okolje, ki ga boste uporabljali za ta tečaj:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Uporaba Visual Studio Code z razširitvijo za Python

Verjetno je najboljši način za uporabo učnega načrta, da ga odprete v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) z [razširitvijo za Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Ko klonirate in odprete mapo v VS Code, vam bo samodejno predlagal namestitev razširitev za Python. Prav tako boste morali namestiti minicondo, kot je opisano zgoraj.

> **Note**: Če vam VS Code predlaga, da ponovno odprete repozitorij v vsebniku, morate to zavrniti, da uporabite lokalno namestitev Pythona.

### Uporaba Jupyterja v brskalniku

Jupyter okolje lahko uporabljate tudi neposredno iz brskalnika na vašem računalniku. Pravzaprav tako klasični Jupyter kot Jupyter Hub nudita precej priročno razvojno okolje z avtomatskim dopolnjevanjem, označevanjem kode itd.

Za zagon Jupyterja lokalno pojdite v mapo tečaja in izvedite:

```bash
jupyter notebook
```
ali
```bash
jupyterhub
```
Nato lahko odprete katero koli `.ipynb` datoteko, jo odprete in začnete delati.

### Zagon v vsebniku

Alternativa namestitvi Pythona je zagon kode v vsebniku. Ker naš repozitorij vsebuje posebno mapo `.devcontainer`, ki določa, kako zgraditi vsebnik za ta repozitorij, vam bo VS Code ponudil možnost, da kodo ponovno odprete v vsebniku. To bo zahtevalo namestitev Dockerja in je nekoliko bolj zapleteno, zato to priporočamo bolj izkušenim uporabnikom.

## Zagon v oblaku

Če ne želite namestiti Pythona lokalno in imate dostop do nekaterih oblačnih virov, je dobra alternativa zagon kode v oblaku. Obstaja več načinov, kako to storiti:

* Uporaba **[GitHub Codespaces](https://github.com/features/codespaces)**, ki je virtualno okolje, ustvarjeno za vas na GitHubu, dostopno prek brskalniškega vmesnika VS Code. Če imate dostop do Codespaces, lahko preprosto kliknete gumb **Code** v repozitoriju, zaženete Codespace in začnete delovati v trenutku.
* Uporaba **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) je brezplačen računalniški vir v oblaku, namenjen ljudem, kot ste vi, za testiranje kode na GitHubu. Na začetni strani je gumb za odpiranje repozitorija v Binderju - to vas bo hitro pripeljalo na Binderjevo stran, ki bo zgradila osnovni vsebnik in brez težav zagnala Jupyterjev spletni vmesnik.

> **Note**: Da bi preprečili zlorabo, ima Binder dostop do nekaterih spletnih virov blokiran. To lahko prepreči delovanje kode, ki pridobiva modele in/ali podatkovne nabore z javnega interneta. Morda boste morali poiskati nekatere rešitve. Poleg tega so računalniški viri, ki jih ponuja Binder, precej osnovni, zato bo učenje počasno, zlasti pri kasnejših bolj zapletenih lekcijah.

## Zagon v oblaku z GPU

Nekatere kasnejše lekcije v tem učnem načrtu bodo močno koristile podpori za GPU, saj bo sicer učenje boleče počasno. Na voljo imate nekaj možnosti, še posebej, če imate dostop do oblaka bodisi prek [Azure za študente](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) bodisi prek vaše institucije:

* Ustvarite [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) in se povežite z njo prek Jupyterja. Nato lahko klonirate repozitorij neposredno na stroj in začnete z učenjem. NC-serija VM-jev ima podporo za GPU.

> **Note**: Nekatere naročnine, vključno z Azure za študente, ne zagotavljajo podpore za GPU takoj. Morda boste morali zaprositi za dodatna GPU jedra prek tehnične podpore.

* Ustvarite [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) in nato uporabite funkcijo Notebook tam. [Ta video](https://azure-for-academics.github.io/quickstart/azureml-papers/) prikazuje, kako klonirati repozitorij v Azure ML Notebook in ga začeti uporabljati.

Lahko uporabite tudi Google Colab, ki ponuja nekaj brezplačne podpore za GPU, in naložite Jupyter Notebooke tja, da jih izvajate enega za drugim.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.