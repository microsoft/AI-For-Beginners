# Paano Patakbuhin ang Code

Ang kurikulum na ito ay naglalaman ng maraming halimbawa at mga lab na nais mong patakbuhin. Upang gawin ito, kailangan mong magkaroon ng kakayahang patakbuhin ang Python code sa Jupyter Notebooks na bahagi ng kurikulum na ito. Mayroon kang ilang mga pagpipilian para sa pagpapatakbo ng code:

## Patakbuhin nang lokal sa iyong computer

Upang patakbuhin ang code nang lokal sa iyong computer, kailangan ang isang Python installation. Isang rekomendasyon ay ang mag-install ng **[miniconda](https://conda.io/en/latest/miniconda.html)** - ito ay isang magaan na installation na sumusuporta sa `conda` package manager para sa iba't ibang Python **virtual environments**.

Pagkatapos mong i-install ang miniconda, i-clone ang repository at gumawa ng virtual environment na gagamitin para sa kursong ito:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Tala para sa Windows**: Kung nabigo ang paggawa ng environment habang ini-install ang `gdk-pixbuf` gamit ang isang `UnicodeDecodeError` na binanggit ang `gbk` codec, i-enable ang UTF-8 mode ng Python sa iyong terminal at subukang muli. Gamitin ang syntax para sa terminal na iyong ginagamit:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Command Prompt (`cmd.exe`) o Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, kabilang ang Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Kung may naiwang nabigong pagtatangka sa environment na `ai4beg`, i-deactivate ito at alisin muna bago subukang muli. Gamitin muna ang `conda deactivate` kapag may aktibong environment:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Paggamit ng Visual Studio Code na may Python Extension

Ang kurikulum na ito ay pinakamainam gamitin kapag binuksan sa [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) na may kasamang [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Tala**: Kapag naka-clone at nabuksan mo ang direktoryo sa VS Code, awtomatiko nitong ipapayo na mag-install ng mga Python extensions. Kailangan mo ring i-install ang miniconda gaya ng nabanggit sa itaas.

> **Tala**: Kung iminungkahi ng VS Code na muling buksan ang repository sa isang container, dapat mong tanggihan ito upang magamit ang lokal na Python installation.

### Paggamit ng Jupyter sa Browser

Maaari ka ring gumamit ng Jupyter environment mula sa browser sa iyong sariling computer. Ang parehong klasikong Jupyter at JupyterHub ay nagbibigay ng maginhawang development environment na may auto-completion, code highlighting, atbp.

Upang simulan ang Jupyter nang lokal, pumunta sa direktoryo ng kurso, at patakbuhin:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Pagkatapos nito, maaari kang mag-navigate sa alinman sa mga `.ipynb` na file, buksan ang mga ito at simulan ang pagtatrabaho.

### Pagpapatakbo sa container

Isang alternatibo sa Python installation ay ang pagpapatakbo ng code sa isang container. Dahil ang aming repository ay naglalaman ng espesyal na `.devcontainer` na folder na nagtuturo kung paano gumawa ng container para sa repo na ito, nag-aalok ang VS Code ng pagkakataon na muling buksan ang code sa isang container. Kailangan nito ang Docker installation, at mas kumplikado ito, kaya inirerekomenda namin ito para sa mas mga bihasang gumagamit.

## Pagpapatakbo sa Cloud

Kung ayaw mong mag-install ng Python nang lokal, at may access ka sa ilang cloud resources - isang magandang alternatibo ay ang pagpapatakbo ng code sa cloud. Ilang paraan na maaari mong gawin ito:

* Paggamit ng **[GitHub Codespaces](https://github.com/features/codespaces)**, na isang virtual environment na nilikha para sa iyo sa GitHub, na naa-access sa pamamagitan ng VS Code browser interface. Kung may access ka sa Codespaces, maaari mo lamang pindutin ang **Code** button sa repo, simulan ang codespace, at agad na patakbuhin.
* Paggamit ng **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. Nagbibigay ang [Binder](https://mybinder.org) ng libreng computing resources sa cloud para sa mga katulad mo na gustong subukan ang ilang code sa GitHub. May button sa front page upang buksan ang repository sa Binder - ito ay mabilis na magdadala sa iyo sa site ng binder, na bubuo ng underlying container at sisimulan ang Jupyter web interface nang tuloy-tuloy.

> **Tala**: Upang maiwasan ang maling paggamit, may mga web resources na hindi naa-access ng Binder. Maaaring pigilan nito ang ilang code na kumuha ng mga modelo at/o datasets mula sa pampublikong Internet. Kailangan mo ng mga workaround. Gayundin, ang compute resources ng Binder ay medyo basic lang, kaya mabagal ang training, lalo na sa mga mas huling, mas kumplikadong leksyon.

## Pagpapatakbo sa Cloud gamit ang GPU

Ang ilang mga huling leksyon sa kurikulum na ito ay malaking pakinabang kung may suporta sa GPU. Halimbawa, ang pagsasanay ng modelo ay maaaring napakabagal kung wala ito. May ilang mga opsyon na maaari mong sundan, lalo na kung may access ka sa cloud sa pamamagitan ng [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), o sa pamamagitan ng iyong institusyon:

* Gumawa ng [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) at kumonekta dito sa pamamagitan ng Jupyter. Maaari mong i-clone ang repo mismo sa makina, at magsimulang matuto. Ang NC-series VMs ay may suporta sa GPU.

> **Tala**: Ang ilang subscriptions, kabilang ang Azure for Students, ay hindi agad nagbibigay ng suporta sa GPU. Maaari kang kailangang humiling ng dagdag na GPU cores sa pamamagitan ng technical support request.

* Gumawa ng [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) at gamitin ang Notebook feature doon. Ipinapakita ng [video na ito](https://azure-for-academics.github.io/quickstart/azureml-papers/) kung paano i-clone ang repository sa Azure ML notebook at simulan ang paggamit nito.

Maaari mo ring gamitin ang Google Colab, na may kasamang libreng GPU support, at i-upload doon ang Jupyter Notebooks para patakbuhin isa-isa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->