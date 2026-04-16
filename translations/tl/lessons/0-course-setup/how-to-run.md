# Paano Patakbuhin ang Code

Ang kurikulum na ito ay naglalaman ng maraming mga executable na halimbawa at mga lab na nais mong patakbuhin. Upang magawa ito, kailangan mong magkaroon ng kakayahang magpatakbo ng Python code sa Jupyter Notebooks na ibinigay bilang bahagi ng kurikulum na ito. Mayroon kang ilang mga pagpipilian para mapatakbo ang code:

## Patakbuhin nang lokal sa iyong kompyuter

Upang patakbuhin ang code nang lokal sa iyong kompyuter, kinakailangan ang isang Python installation. Isang rekomendasyon ay ang pag-install ng **[miniconda](https://conda.io/en/latest/miniconda.html)** - ito ay isang medyo magaan na installation na sumusuporta sa `conda` package manager para sa iba't ibang Python **virtual environments**.

Pagkatapos mong i-install ang miniconda, i-clone ang repository at gumawa ng virtual environment na gagamitin para sa kurso na ito:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Paggamit ng Visual Studio Code na may Python Extension

Ang kurikulum na ito ay pinakamahusay gamitin kapag binuksan ito sa [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) kasama ang [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Kapag na-clone mo at na-open ang direktoryo sa VS Code, awtomatiko nitong ire-rekomenda sa iyo na i-install ang Python extensions. Kailangan mo ring i-install ang miniconda gaya ng ipinaliwanag sa itaas.

> **Note**: Kung ire-rekomenda ng VS Code na i-reopen ang repository sa isang container, dapat mong tanggihan ito upang gamitin ang lokal na Python installation.

### Paggamit ng Jupyter sa Browser

Maaari ka ring gumamit ng Jupyter environment mula sa browser sa iyong sariling kompyuter. Parehong ang klasikong Jupyter at JupyterHub ay nagbibigay ng maginhawang development environment na may auto-completion, pagkulay ng code, atbp.

Upang simulan ang Jupyter nang lokal, pumunta sa direktoryo ng kurso, at i-execute:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Pagkatapos ay maaari kang mag-navigate sa alinmang `.ipynb` na file, buksan ito at simulan ang pagtatrabaho.

### Pagpapatakbo sa container

Isang alternatibo sa pag-install ng Python ay ang pagpapatakbo ng code sa isang container. Dahil ang aming repository ay nagbibigay ng isang espesyal na `.devcontainer` na folder na nagsasaad kung paano bumuo ng isang container para sa repo na ito, nag-aalok ang VS Code ng pagkakataong i-reopen ang code sa loob ng isang container. Kakailanganin nito ang Docker installation, at mas kumplikado ito kaya inirerekomenda namin ito sa mga mas may karanasang gumagamit.

## Pagpapatakbo sa Cloud

Kung ayaw mong mag-install ng Python nang lokal, at may access ka sa ilang cloud resources - isang magandang alternatibo ay ang pagpapatakbo ng code sa cloud. May ilang paraan upang magawa ito:

* Paggamit ng **[GitHub Codespaces](https://github.com/features/codespaces)**, na isang virtual environment na nilikha para sa iyo sa GitHub, na maa-access sa pamamagitan ng VS Code browser interface. Kung may access ka sa Codespaces, maaari mong i-click lang ang **Code** button sa repo, simulan ang codespace, at agad na makapagtatrabaho.
* Paggamit ng **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. Nagbibigay ang [Binder](https://mybinder.org) ng libreng computing resources sa cloud para sa mga taong tulad mo upang subukan ang ilang code mula sa GitHub. Mayroong button sa front page upang buksan ang repository sa Binder - ito ay mabilis na magdadala sa iyo sa binder site, kung saan bubuuin ang underlying container at magsisimula ang Jupyter web interface nang walang patid.

> **Note**: Upang maiwasan ang maling paggamit, may mga web resources na hindi naa-access ng Binder. Maaaring pigilan nito ang ilang bahagi ng code na gumana na kumukuha ng mga modelo at/o dataset mula sa pampublikong Internet. Kailangan mong humanap ng mga alternatibong paraan. Gayundin, ang computing resources na ibinibigay ng Binder ay medyo basic lamang, kaya magiging mabagal ang training, lalong-lalo na sa mga huling aralin na mas kumplikado.

## Pagpapatakbo sa Cloud na may GPU

Ang ilang mga huling aralin sa kurikulum na ito ay lubos na makikinabang sa suporta ng GPU. Ang pagsasanay ng mga modelo, halimbawa, ay maaaring maging napakabagal kung wala ito. May ilang mga opsyon na maaari mong sundin, lalo na kung may access ka sa cloud sa pamamagitan ng [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), o sa pamamagitan ng iyong institusyon:

* Gumawa ng [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) at kumonekta dito gamit ang Jupyter. Maaari mong i-clone ang repo direkta sa makina, at simulan ang pag-aaral. Ang NC-series VMs ay may suporta para sa GPU.

> **Note**: Ang ilang subscription, kabilang ang Azure for Students, ay hindi awtomatikong nagbibigay ng suporta para sa GPU. Maaaring kailanganin mong humiling ng karagdagang GPU cores sa pamamagitan ng technical support request.

* Gumawa ng [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) at gamitin ang Notebook feature doon. [Itong video](https://azure-for-academics.github.io/quickstart/azureml-papers/) ay nagpapakita kung paano i-clone ang repository papunta sa Azure ML notebook at simulan ang paggamit nito.

Maaari mo ring gamitin ang Google Colab, na may kasamang libreng GPU support, at i-upload ang Jupyter Notebooks doon upang isa-isang patakbuhin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paliwanag**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kaming maging tumpak, pakatandaan na maaaring may mga pagkakamali o hindi pagkakatugma ang mga awtomatikong pagsasalin. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring manggaling sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->