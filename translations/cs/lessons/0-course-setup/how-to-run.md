<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-26T00:35:12+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "cs"
}
-->
# Jak spustit kód

Tento kurz obsahuje mnoho spustitelných příkladů a cvičení, které budete chtít vyzkoušet. Abyste to mohli udělat, potřebujete možnost spouštět Python kód v Jupyter Noteboocích, které jsou součástí tohoto kurzu. Existuje několik možností, jak kód spustit:

## Spuštění lokálně na vašem počítači

Pro spuštění kódu lokálně na vašem počítači budete potřebovat nějakou verzi Pythonu. Osobně doporučuji nainstalovat **[miniconda](https://conda.io/en/latest/miniconda.html)** – jedná se o poměrně lehkou instalaci, která podporuje správce balíčků `conda` pro různé Python **virtuální prostředí**.

Po instalaci minicondy je potřeba naklonovat repozitář a vytvořit virtuální prostředí, které bude použito pro tento kurz:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Použití Visual Studio Code s rozšířením Python

Pravděpodobně nejlepší způsob, jak využít tento kurz, je otevřít ho v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Jakmile naklonujete a otevřete adresář ve VS Code, automaticky vám bude navrženo nainstalovat rozšíření pro Python. Budete také muset nainstalovat miniconda, jak je popsáno výše.

> **Note**: Pokud vám VS Code navrhne znovu otevřít repozitář v kontejneru, je potřeba tuto možnost odmítnout a použít lokální instalaci Pythonu.

### Použití Jupyteru v prohlížeči

Jupyter prostředí můžete také používat přímo z prohlížeče na vašem počítači. Ve skutečnosti jak klasický Jupyter, tak Jupyter Hub poskytují velmi pohodlné vývojové prostředí s automatickým doplňováním, zvýrazněním kódu atd.

Pro spuštění Jupyteru lokálně přejděte do adresáře kurzu a spusťte:

```bash
jupyter notebook
```
nebo
```bash
jupyterhub
```
Poté můžete přejít k libovolnému souboru `.ipynb`, otevřít ho a začít pracovat.

### Spuštění v kontejneru

Alternativou k instalaci Pythonu může být spuštění kódu v kontejneru. Jelikož náš repozitář obsahuje speciální složku `.devcontainer`, která určuje, jak vytvořit kontejner pro tento repozitář, VS Code vám nabídne znovu otevřít kód v kontejneru. To bude vyžadovat instalaci Dockeru a je také složitější, takže tuto možnost doporučujeme zkušenějším uživatelům.

## Spuštění v cloudu

Pokud nechcete instalovat Python lokálně a máte přístup k nějakým cloudovým zdrojům, dobrou alternativou může být spuštění kódu v cloudu. Existuje několik způsobů, jak to udělat:

* Použití **[GitHub Codespaces](https://github.com/features/codespaces)**, což je virtuální prostředí vytvořené pro vás na GitHubu, přístupné přes rozhraní prohlížeče VS Code. Pokud máte přístup ke Codespaces, stačí kliknout na tlačítko **Code** v repozitáři, spustit codespace a začít pracovat během chvilky.
* Použití **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) poskytuje zdarma výpočetní zdroje v cloudu pro uživatele, kteří chtějí vyzkoušet kód na GitHubu. Na úvodní stránce je tlačítko pro otevření repozitáře v Binderu – to vás rychle přesměruje na Binder, který vytvoří podkladový kontejner a bezproblémově spustí webové rozhraní Jupyteru.

> **Note**: Aby se zabránilo zneužití, Binder má blokovaný přístup k některým webovým zdrojům. To může zabránit fungování některého kódu, který stahuje modely nebo datové sady z veřejného internetu. Možná budete muset najít nějaké alternativy. Také výpočetní zdroje poskytované Binderem jsou poměrně základní, takže trénování bude pomalé, zejména v pozdějších složitějších lekcích.

## Spuštění v cloudu s GPU

Některé z pozdějších lekcí v tomto kurzu by velmi těžily z podpory GPU, protože jinak bude trénování bolestivě pomalé. Existuje několik možností, které můžete využít, zejména pokud máte přístup k cloudu buď přes [Azure pro studenty](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), nebo přes vaši instituci:

* Vytvořte [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) a připojte se k ní přes Jupyter. Poté můžete naklonovat repozitář přímo na stroj a začít se učit. NC-series VM mají podporu GPU.

> **Note**: Některé předplatné, včetně Azure pro studenty, neposkytují podporu GPU automaticky. Možná budete muset požádat o další GPU jádra prostřednictvím technické podpory.

* Vytvořte [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) a poté použijte funkci Notebook tam. [Toto video](https://azure-for-academics.github.io/quickstart/azureml-papers/) ukazuje, jak naklonovat repozitář do Azure ML notebooku a začít ho používat.

Můžete také použít Google Colab, který nabízí určitou bezplatnou podporu GPU, a nahrát tam Jupyter Notebooky, abyste je mohli spouštět jeden po druhém.

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.