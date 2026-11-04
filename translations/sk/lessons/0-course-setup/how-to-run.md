# Ako spustiť kód

Tento kurz obsahuje veľa spustiteľných príkladov a cvičení, ktoré budete chcieť spustiť. Na to potrebujete možnosť vykonávať Python kód v Jupyter Notebookoch, ktoré sú súčasťou tohto kurzu. Máte niekoľko možností, ako kód spustiť:

## Spustenie lokálne na vašom počítači

Ak chcete spustiť kód lokálne na vašom počítači, je potrebná inštalácia Pythonu. Jedným z odporúčaní je nainštalovať **[miniconda](https://conda.io/en/latest/miniconda.html)** - ide o pomerne ľahkú inštaláciu, ktorá podporuje správcu balíčkov `conda` na správu rôznych Python **virtuálnych prostredí**.

Po inštalácii minicondy si sklonujte repozitár a vytvorte virtuálne prostredie, ktoré budete používať počas kurzu:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Poznámka pre Windows**: Ak sa pri vytváraní prostredia pri inštalácii `gdk-pixbuf` objaví chyba s `UnicodeDecodeError`, ktorá spomína kodek `gbk`, zapnite v termináli Python UTF-8 režim a skúste to znova. Použite syntax terminálu, ktorý používate:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Príkazový riadok (`cmd.exe`) alebo Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, vrátane Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Ak sa pri predchádzajúcom neúspešnom pokuse vytvorilo prostredie `ai4beg`, deaktivujte ho a odstráňte pred novým pokusom. Použite najskôr `conda deactivate`, keď je prostredie aktívne:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Použitie Visual Studio Code s rozšírením Python

Tento kurz je najlepšie používať pri otvorení v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Poznámka**: Keď si klonujete a otvoríte adresár vo VS Code, automaticky vám ponúkne nainštalovať rozšírenia pre Python. Tiež budete musieť nainštalovať miniconda, ako je popísané vyššie.

> **Poznámka**: Ak vám VS Code navrhne znovu otvoriť repozitár v kontajneri, mali by ste to odmietnuť, aby ste používali lokálnu inštaláciu Pythonu.

### Použitie Jupytera v prehliadači

Môžete tiež použiť prostredie Jupyter priamo vo vašom prehliadači na vlastnom počítači. Klasický Jupyter aj JupyterHub poskytujú pohodlné vývojové prostredie s automatickým dopĺňaním, zvýrazňovaním kódu a podobne.

Ak chcete spustiť Jupyter lokálne, prejdite do adresára kurzu a spustite:

```bash
jupyter notebook
```
alebo
```bash
jupyterhub
```
Potom môžete prechádzať do ľubovoľných súborov `.ipynb`, otvoriť ich a začať pracovať.

### Spustenie v kontajneri

Alternatívou k inštalácii Pythonu by bolo spustiť kód v kontajneri. Náš repozitár obsahuje špeciálny `.devcontainer` priečinok, ktorý popisuje, ako zostaviť kontajner pre tento repozitár, a VS Code ponúka možnosť opätovného otvorenia kódu v kontajneri. To vyžaduje inštaláciu Dockeru a zároveň je to zložitejšie, takže to odporúčame skôr pokročilejším používateľom.

## Spustenie v Cloude

Ak nechcete inštalovať Python lokálne a máte prístup k nejakým cloudovým zdrojom, dobrou alternatívou je spustenie kódu v cloude. Existuje niekoľko spôsobov, ako to môžete urobiť:

* Použitie **[GitHub Codespaces](https://github.com/features/codespaces)**, čo je virtuálne prostredie vytvorené pre vás na GitHube, prístupné cez rozhranie VS Code v prehliadači. Ak máte prístup ku Codespaces, stačí kliknúť na tlačidlo **Code** v repozitári, spustiť codespace a môžete začať veľmi rýchlo.
* Použitie **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) ponúka bezplatné výpočtové prostriedky v cloude pre ľudí ako vy, aby otestovali kód z GitHubu. Na hlavnej stránke je tlačidlo na otvorenie repozitára v Binderi - toto vás rýchlo presmeruje na stránku Binder, ktorá vytvorí základný kontajner a bez problémov vám spustí webové rozhranie Jupyter.

> **Poznámka**: Aby sa zabránilo zneužitiu, Binder blokuje prístup k niektorým webovým zdrojom. To môže zabrániť fungovaniu časti kódu, ktorá sťahuje modely alebo dátové sady z verejného internetu. Budete možno musieť nájsť nejaké obchádzky. Tiež výpočtové zdroje poskytované Binderom sú dosť základné, takže trénovanie bude pomalé, najmä v neskorších, náročnejších lekciách.

## Spustenie v Cloude s GPU

Niektoré neskoršie lekcie v tomto kurze by výrazne profitovali z podpory GPU. Tréning modelov, napríklad, môže byť inak veľmi pomalý. Existuje niekoľko možností, ktoré môžete nasledovať, najmä ak máte prístup do cloudu cez [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) alebo cez vašu inštitúciu:

* Vytvorte [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) a pripojte sa k nej cez Jupyter. Môžete si potom naklonovať repozitár priamo do stroja a začať sa učiť. NC-series VM majú podporu GPU.

> **Poznámka**: Niektoré predplatné vrátane Azure for Students štandardne neprinášajú podporu GPU. Môžete potrebovať požiadať o pridanie GPU jadier prostredníctvom technickej podpory.

* Vytvorte [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) a potom využite funkciu Notebook tam. [Toto video](https://azure-for-academics.github.io/quickstart/azureml-papers/) ukazuje, ako klonovať repozitár do Azure ML notebooku a začať ho používať.

Môžete tiež použiť Google Colab, ktorý poskytuje nejakú bezplatnú podporu GPU, a nahrať tam Jupyter Notebooky na postupné vykonávanie.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->