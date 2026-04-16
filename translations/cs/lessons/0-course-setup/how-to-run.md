# Jak spustit kód

Tento kurz obsahuje spoustu spustitelných příkladů a laboratorních cvičení, která budete chtít spustit. K tomu je potřeba mít možnost spouštět Python kód v Jupyter Noteboocích poskytnutých jako součást tohoto kurzu. Pro spuštění kódu máte několik možností:

## Spuštění lokálně na vašem počítači

Pro spuštění kódu lokálně na vašem počítači je potřeba mít nainstalovaný Python. Jedním z doporučení je instalace **[miniconda](https://conda.io/en/latest/miniconda.html)** – jedná se o poměrně lehkou instalaci, která podporuje správce balíčků `conda` pro různé Python **virtuální prostředí**.

Po instalaci minicondy si klonujte repozitář a vytvořte virtuální prostředí, které budete používat pro tento kurz:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Použití Visual Studio Code s Python rozšířením

Tento kurz je nejlepší používat, když jej otevřete v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s [Python rozšířením](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Poznámka**: Jakmile repozitář klonujete a otevřete ve VS Code, automaticky se vám nabídne instalace Python rozšíření. Také budete muset nainstalovat miniconda, jak je popsáno výše.

> **Poznámka**: Pokud vám VS Code nabídne znovu otevřít repozitář v kontejneru, měli byste to zamítnout, pokud chcete používat lokální Python instalaci.

### Použití Jupyter v prohlížeči

Můžete také používat prostředí Jupyter přímo v prohlížeči na vašem počítači. Jak klasický Jupyter, tak JupyterHub poskytují pohodlné vývojové prostředí s automatickým dokončováním, zvýrazňováním kódu atd.

Pro spuštění Jupyter lokálně přejděte do adresáře kurzu a spusťte:

```bash
jupyter notebook
```
nebo
```bash
jupyterhub
```
Poté můžete přejít k libovolnému souboru `.ipynb`, otevřít ho a začít pracovat.

### Spuštění v kontejneru

Jinou možností místo instalace Pythonu je spuštění kódu v kontejneru. Jelikož náš repozitář obsahuje speciální složku `.devcontainer`, která určuje, jak postavit kontejner pro tento repozitář, VS Code nabízí možnost znovu otevřít kód přímo v kontejneru. To ale vyžaduje instalaci Dockeru a je to složitější, takže toto doporučujeme spíše zkušenějším uživatelům.

## Spuštění v cloudu

Pokud nechcete Python instalovat lokálně a máte přístup k nějakým cloudovým zdrojům, dobrou alternativou je spuštění kódu v cloudu. Nabízí se několik variant:

* Použít **[GitHub Codespaces](https://github.com/features/codespaces)**, což je virtuální prostředí vytvořené pro vás na GitHubu, přístupné přes VS Code v prohlížeči. Pokud máte přístup ke Codespaces, stačí kliknout na tlačítko **Code** v repozitáři, spustit Codespace a hned můžete začít.
* Použít **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) nabízí zdarma výpočetní prostředky v cloudu, kde si můžete zkusit spustit nějaký kód z GitHubu. Na úvodní stránce je tlačítko pro otevření repozitáře v Binderu – to vás rychle převeze na stránku Binderu, která sestaví podkladový kontejner a bez problémů spustí webové rozhraní Jupyter.

> **Poznámka**: Pro zamezení zneužití má Binder blokovaný přístup k některým webovým zdrojům. Může se tak stát, že některé části kódu, které stahují modely nebo dataset z Internetu, nebudou fungovat. Budete si muset najít nějaké alternativy. Compute zdroje, které Binder poskytuje, jsou základní, takže trénování bude pomalé, zejména v pozdějších, složitějších lekcích.

## Spuštění v cloudu s GPU

Některé pokročilejší lekce v tomto kurzu by velmi výrazně profitovaly z podpory GPU. Trénování modelů by jinak mohlo být bolestivě pomalé. Máte pár možností, zejména pokud máte přístup do cloudu přes [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) nebo přes vaši instituci:

* Vytvořit [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) a připojit se k ní přes Jupyter. Pak si můžete přímo na této VM klonovat repozitář a začít se učit. NC série VM mají podporu GPU.

> **Poznámka**: Některé typy předplatného, včetně Azure for Students, GPU podporu hned v základu neposkytují. Může být potřeba požádat o další GPU jádra přes technickou podporu.

* Vytvořit [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) a využít tamní funkci Notebooks. [Toto video](https://azure-for-academics.github.io/quickstart/azureml-papers/) ukazuje, jak klonovat repozitář do Azure ML notebooku a začít jej používat.

Můžete také využít Google Colab, který nabízí nějakou výpočetní kapacitu s GPU zdarma, a do něj nahrávat Jupyter Notebooky a spouštět je jednotlivě.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nepochopení nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->