# Ako spustiť kód

Tento učebný plán obsahuje veľa vykonateľných príkladov a laboratórií, ktoré by ste chceli spustiť. Aby ste to mohli urobiť, potrebujete možnosť vykonávať Python kód v Jupyter Notebookoch poskytovaných ako súčasť tohto učebného plánu. Máte niekoľko možností, ako spustiť kód:

## Spustiť lokálne na vašom počítači

Na spustenie kódu lokálne na vašom počítači je potrebná inštalácia Pythonu. Jedným z odporúčaní je inštalovať **[miniconda](https://conda.io/en/latest/miniconda.html)** - ide o pomerne ľahkú inštaláciu, ktorá podporuje správcu balíčkov `conda` pre rôzne Python **virtuálne prostredia**.

Po nainštalovaní minicondy si naklonujte repozitár a vytvorte virtuálne prostredie, ktoré bude použité pre tento kurz:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Použitie Visual Studio Code s rozšírením Python

Tento učebný plán je najlepšie používať pri jeho otvorení v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s rozšírením [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Poznámka**: Po naklonovaní a otvorení adresára vo VS Code vám automaticky navrhne inštaláciu rozšírení Python. Tiež budete musieť nainštalovať miniconda, ako je to popísané vyššie.

> **Poznámka**: Ak vám VS Code navrhne znovu otvoriť repozitár v kontajneri, mali by ste to odmietnuť, aby ste použili lokálnu inštaláciu Pythonu.

### Použitie Jupyter v prehliadači

Môžete tiež použiť Jupyter prostredie z prehliadača na vašom vlastnom počítači. Klasický Jupyter aj JupyterHub poskytujú pohodlné vývojové prostredie s automatickým dopĺňaním, zvýrazňovaním kódu atď.

Na spustenie Jupyter lokálne choďte do adresára kurzu a spustite:

```bash
jupyter notebook
```
alebo
```bash
jupyterhub
```
Potom môžete prechádzať k ľubovoľnému súboru `.ipynb`, otvoriť ho a začať pracovať.

### Spustenie v kontajneri

Jednou z alternatív k inštalácii Pythonu je spustiť kód v kontajneri. Keďže náš repozitár obsahuje špeciálny priečinok `.devcontainer`, ktorý ukazuje, ako zostaviť kontajner pre tento repozitár, VS Code ponúka možnosť znova otvoriť kód v kontajneri. Toto vyžaduje inštaláciu Dockeru a tiež je to zložitejšie, preto to odporúčame skúsenejším používateľom.

## Spustenie v cloude

Ak nechcete inštalovať Python lokálne a máte prístup ku cloudovým zdrojom - dobrá alternatíva je spustiť kód v cloude. Existuje niekoľko spôsobov, ako to urobiť:

* Použitie **[GitHub Codespaces](https://github.com/features/codespaces)**, čo je virtuálne prostredie vytvorené pre vás na GitHube, prístupné cez rozhranie VS Code v prehliadači. Ak máte prístup ku Codespaces, môžete jednoducho kliknúť na tlačidlo **Code** v repozitári, spustiť codespace a začať bez zbytočného čakania.
* Použitie **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) ponúka bezplatné výpočtové zdroje poskytované v cloude pre ľudí ako vy, ktorí chcú otestovať nejaký kód na GitHube. Na úvodnej stránke je tlačidlo na otvorenie repozitára v Bindri - to vás rýchlo zavedie na stránku Bindra, ktorá zostaví podkladový kontajner a spustí pre vás webové rozhranie Jupyter bez prerušenia.

> **Poznámka**: Aby sa predišlo zneužitiu, Binder má prístup k niektorým webovým zdrojom zablokovaný. To môže zabrániť správnej funkcii niektorého kódu, ktorý sťahuje modely a/alebo dátové sady z verejného internetu. Môžete potrebovať nájsť nejaké obchádzky. Tiež výpočtové zdroje poskytované Binderom sú pomerne základné, takže tréning bude pomalý, zvlášť v neskorších, komplexnejších lekciách.

## Spustenie v cloude s GPU

Niektoré z neskorších lekcií v tomto učebnom pláne by výrazne profitovali z podpory GPU. Tréning modelov môže byť inak bolestivo pomalý. Existuje niekoľko možností, ktoré môžete sledovať, najmä ak máte prístup ku cloudu buď cez [Azure pre študentov](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), alebo cez vašu inštitúciu:

* Vytvorte [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) a pripojte sa k nej cez Jupyter. Môžete si potom naklonovať repozitár priamo na stroj a začať sa učiť. VM série NC majú podporu GPU.

> **Poznámka**: Niektoré predplatné, vrátane Azure pre študentov, neposkytujú podporu GPU automaticky. Môžete potrebovať požiadať o ďalšie GPU jadrá cez technickú podporu.

* Vytvorte [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) a potom použite funkciu Notebook tam. [Toto video](https://azure-for-academics.github.io/quickstart/azureml-papers/) ukazuje, ako naklonovať repozitár do Azure ML notebooku a začať ho používať.

Môžete tiež použiť Google Colab, ktorý má nejakú bezplatnú podporu GPU, a nahrať tam Jupyter Notebooky na ich postupné spustenie.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím berte na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pri kritických informáciách sa odporúča profesionálny ľudský preklad. Nepreberáme zodpovednosť za akékoľvek nedorozumenia alebo mylné výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->