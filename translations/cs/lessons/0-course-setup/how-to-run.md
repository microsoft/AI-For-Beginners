# Jak spustit kód

Tento učební plán obsahuje mnoho spustitelných příkladů a laboratorních úloh, které budete chtít spustit. Abyste to mohli udělat, potřebujete možnost spouštět kód Pythonu v Jupyter Noteboocích dodávaných jako součást tohoto učebního plánu. Máte několik možností, jak kód spustit:

## Spuštění lokálně na vašem počítači

Pro spuštění kódu lokálně na vašem počítači je potřeba instalace Pythonu. Jedním z doporučení je instalace **[miniconda](https://conda.io/en/latest/miniconda.html)** – je to poměrně lehká instalace, která podporuje správce balíčků `conda` pro různé Python **virtuální prostředí**.

Po instalaci minicondy si naklonujte repozitář a vytvořte virtuální prostředí, které budete používat pro tento kurz:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Poznámka pro Windows**: Pokud vytvoření prostředí selže při instalaci `gdk-pixbuf` s chybou `UnicodeDecodeError`, která zmiňuje `gbk` kodek, zapněte v terminálu režim UTF-8 pro Python a zkuste to znovu. Použijte syntaxi podle terminálu, který používáte:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Příkazový řádek (`cmd.exe`) nebo Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, včetně Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Pokud předchozí neúspěšný pokus zanechal za sebou `ai4beg` prostředí, deaktivujte ho a odstraňte toto prostředí před dalším pokusem. Při aktivním prostředí používejte nejprve `conda deactivate`:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Použití Visual Studio Code s Python rozšířením

Tento učební plán se nejlépe používá při otevření v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s [Python rozšířením](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Poznámka**: Jakmile naklonujete a otevřete adresář ve VS Code, automaticky vám nabídne instalaci Python rozšíření. Také je nutné nainstalovat miniconda, jak je popsáno výše.

> **Poznámka**: Pokud vám VS Code nabídne znovu otevřít repozitář v kontejneru, odmítněte to pro použití lokální instalace Pythonu.

### Použití Jupyter v prohlížeči

Můžete také použít Jupyter prostředí přímo z prohlížeče na vašem počítači. Klasický Jupyter i JupyterHub poskytují pohodlné vývojové prostředí s automatickým dokončováním, zvýrazněním kódu atd.

Pro spuštění Jupyter lokálně přejděte do adresáře kurzu a spusťte:

```bash
jupyter notebook
```
nebo
```bash
jupyterhub
```
Poté můžete přejít k jakémukoliv `.ipynb` souboru, otevřít ho a začít pracovat.

### Spuštění v kontejneru

Jednou z alternativ k instalaci Pythonu je spuštění kódu v kontejneru. Náš repozitář obsahuje speciální složku `.devcontainer`, která popisuje, jak vytvořit kontejner pro tento repozitář, VS Code umožňuje znovu otevřít kód v kontejneru. To vyžaduje instalaci Dockeru a také je to složitější, proto doporučujeme tuto možnost pokročilejším uživatelům.

## Spuštění v cloudu

Pokud nechcete instalovat Python lokálně a máte přístup ke cloudovým zdrojům, dobrou alternativou je spuštění kódu v cloudu. Existuje několik způsobů, jak to můžete udělat:

* Použití **[GitHub Codespaces](https://github.com/features/codespaces)**, což je virtuální prostředí vytvořené pro vás na GitHubu, přístupné přes VS Code v prohlížeči. Máte-li přístup k Codespaces, stačí kliknout na tlačítko **Code** v repozitáři, spustit codespace a rychle začít.
* Použití **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) nabízí zdarma výpočetní prostředky v cloudu pro uživatele, kteří chtějí vyzkoušet kód na GitHubu. Na úvodní stránce je tlačítko pro otevření repozitáře v Binderu – toto vás rychle přenese na stránku Binderu, která vytvoří podkladový kontejner a bez problémů spustí Jupyter webové rozhraní.

> **Poznámka**: Aby se předešlo zneužití, Binder blokuje přístup k některým webovým zdrojům. To může zabránit fungování části kódu, která načítá modely a/nebo datové sady z veřejného Internetu. Možná budete muset najít nějaká řešení. Také výpočetní zdroje poskytované Binderem jsou poměrně základní, takže trénink bude pomalý, zejména u pozdějších, složitějších lekcí.

## Spuštění v cloudu s GPU

Některé pozdější lekce v tomto učebním plánu by velmi profitovaly z podpory GPU. Trénování modelů může být jinak bolestivě pomalé. Existuje několik možností, jak postupovat, zejména pokud máte přístup do cloudu třeba přes [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) nebo přes vaši instituci:

* Vytvořte [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) a připojte se k ní přes Jupyter. Můžete si pak repozitář naklonovat přímo do stroje a začít se učit. Virtuální stroje řady NC podporují GPU.

> **Poznámka**: Některé předplatné, včetně Azure for Students, neposkytují GPU podporu přímo. Může být potřeba požádat o další GPU jádra technickou podporou.

* Vytvořte [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) a pak tam použijte funkci Notebook. [Toto video](https://azure-for-academics.github.io/quickstart/azureml-papers/) ukazuje, jak klonovat repozitář do Azure ML notebooku a začít ho používat.

Můžete také použít Google Colab, který nabízí základní podporu GPU zdarma, a nahrát tam Jupyter Noteboocy k jejich postupnému spuštění.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->