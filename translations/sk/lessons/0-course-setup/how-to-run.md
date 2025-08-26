<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-26T00:35:29+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "sk"
}
-->
# Ako spustiť kód

Tento kurz obsahuje množstvo spustiteľných príkladov a cvičení, ktoré si budete chcieť vyskúšať. Na to, aby ste to mohli urobiť, potrebujete možnosť spúšťať Python kód v Jupyter Notebooks, ktoré sú súčasťou tohto kurzu. Existuje niekoľko možností, ako kód spustiť:

## Spustenie lokálne na vašom počítači

Ak chcete kód spustiť lokálne na svojom počítači, budete potrebovať nainštalovanú nejakú verziu Pythonu. Osobne odporúčam nainštalovať **[miniconda](https://conda.io/en/latest/miniconda.html)** - je to pomerne ľahká inštalácia, ktorá podporuje správcu balíčkov `conda` pre rôzne Python **virtuálne prostredia**.

Po nainštalovaní minicondy budete musieť naklonovať repozitár a vytvoriť virtuálne prostredie, ktoré sa bude používať pre tento kurz:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Použitie Visual Studio Code s rozšírením Python

Pravdepodobne najlepší spôsob, ako používať tento kurz, je otvoriť ho v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s [rozšírením Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Po naklonovaní a otvorení adresára vo VS Code vám editor automaticky navrhne nainštalovať rozšírenia pre Python. Budete tiež musieť nainštalovať miniconda, ako je popísané vyššie.

> **Note**: Ak vám VS Code navrhne otvoriť repozitár v kontajneri, musíte to odmietnuť, aby ste mohli použiť lokálnu inštaláciu Pythonu.

### Použitie Jupyter v prehliadači

Jupyter prostredie môžete používať aj priamo z prehliadača na svojom počítači. V skutočnosti, klasický Jupyter aj Jupyter Hub poskytujú veľmi pohodlné vývojové prostredie s automatickým dopĺňaním, zvýrazňovaním kódu a podobne.

Ak chcete spustiť Jupyter lokálne, prejdite do adresára kurzu a spustite:

```bash
jupyter notebook
```  
alebo  
```bash
jupyterhub
```  
Potom môžete prejsť na akýkoľvek `.ipynb` súbor, otvoriť ho a začať pracovať.

### Spustenie v kontajneri

Alternatívou k inštalácii Pythonu by mohlo byť spustenie kódu v kontajneri. Keďže náš repozitár obsahuje špeciálny priečinok `.devcontainer`, ktorý určuje, ako zostaviť kontajner pre tento repozitár, VS Code vám ponúkne možnosť otvoriť kód v kontajneri. To bude vyžadovať inštaláciu Dockeru a je to o niečo zložitejšie, takže to odporúčame skúsenejším používateľom.

## Spustenie v cloude

Ak nechcete inštalovať Python lokálne a máte prístup k nejakým cloudovým zdrojom, dobrou alternatívou by mohlo byť spustenie kódu v cloude. Existuje niekoľko spôsobov, ako to urobiť:

* Použitie **[GitHub Codespaces](https://github.com/features/codespaces)**, čo je virtuálne prostredie vytvorené pre vás na GitHube, prístupné cez prehliadačové rozhranie VS Code. Ak máte prístup k Codespaces, stačí kliknúť na tlačidlo **Code** v repozitári, spustiť codespace a môžete začať pracovať okamžite.
* Použitie **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) je bezplatný výpočtový zdroj poskytovaný v cloude pre ľudí, ako ste vy, na testovanie kódu na GitHube. Na úvodnej stránke je tlačidlo na otvorenie repozitára v Bindri - to vás rýchlo presmeruje na stránku Binder, ktorá zostaví podkladový kontajner a spustí Jupyter webové rozhranie pre vás bez problémov.

> **Note**: Aby sa zabránilo zneužitiu, Binder má prístup k niektorým webovým zdrojom zablokovaný. To môže zabrániť fungovaniu niektorého kódu, ktorý sťahuje modely a/alebo datasety z verejného internetu. Možno budete musieť nájsť nejaké obchádzky. Tiež, výpočtové zdroje poskytované Binderom sú pomerne základné, takže tréning bude pomalý, najmä v neskorších, zložitejších lekciách.

## Spustenie v cloude s GPU

Niektoré z neskorších lekcií v tomto kurze by veľmi profitovali z podpory GPU, pretože inak bude tréning bolestivo pomalý. Existuje niekoľko možností, ktoré môžete využiť, najmä ak máte prístup k cloudu buď cez [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), alebo cez vašu inštitúciu:

* Vytvorte [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) a pripojte sa k nej cez Jupyter. Potom môžete naklonovať repozitár priamo na stroj a začať sa učiť. NC-series VM majú podporu GPU.

> **Note**: Niektoré predplatné, vrátane Azure for Students, neposkytujú podporu GPU automaticky. Možno budete musieť požiadať o ďalšie GPU jadrá prostredníctvom technickej podpory.

* Vytvorte [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) a potom použite funkciu Notebook tam. [Toto video](https://azure-for-academics.github.io/quickstart/azureml-papers/) ukazuje, ako naklonovať repozitár do Azure ML notebooku a začať ho používať.

Môžete tiež použiť Google Colab, ktorý ponúka určitú bezplatnú podporu GPU, a nahrať tam Jupyter Notebooks, aby ste ich mohli spúšťať jeden po druhom.

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.