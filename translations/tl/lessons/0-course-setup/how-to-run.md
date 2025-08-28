<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-28T02:28:26+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "tl"
}
-->
# Paano Patakbuhin ang Code

Ang kurikulum na ito ay naglalaman ng maraming mga executable na halimbawa at mga lab na nais mong patakbuhin. Upang magawa ito, kailangan mo ng kakayahang magpatakbo ng Python code sa Jupyter Notebooks na kasama sa kurikulum na ito. Mayroon kang ilang mga opsyon para patakbuhin ang code:

## Patakbuhin nang lokal sa iyong computer

Upang patakbuhin ang code nang lokal sa iyong computer, kailangan mong magkaroon ng ilang bersyon ng Python na naka-install. Personal kong inirerekomenda ang pag-install ng **[miniconda](https://conda.io/en/latest/miniconda.html)** - ito ay isang magaan na installation na sumusuporta sa `conda` package manager para sa iba't ibang Python **virtual environments**.

Pagkatapos mong i-install ang miniconda, kailangan mong i-clone ang repository at gumawa ng virtual environment na gagamitin para sa kursong ito:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Paggamit ng Visual Studio Code na may Python Extension

Marahil ang pinakamagandang paraan upang magamit ang kurikulum ay buksan ito sa [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) na may [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Kapag na-clone mo at binuksan ang direktoryo sa VS Code, awtomatiko nitong imumungkahi na i-install ang Python extensions. Kailangan mo ring i-install ang miniconda tulad ng inilarawan sa itaas.

> **Note**: Kung imumungkahi ng VS Code na i-reopen ang repository sa container, kailangan mong tanggihan ito upang magamit ang lokal na Python installation.

### Paggamit ng Jupyter sa Browser

Maaari mo ring gamitin ang Jupyter environment direkta mula sa browser sa iyong sariling computer. Sa katunayan, parehong classical Jupyter at Jupyter Hub ay nagbibigay ng maginhawang development environment na may auto-completion, code highlighting, at iba pa.

Upang simulan ang Jupyter nang lokal, pumunta sa direktoryo ng kurso, at i-execute:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Pagkatapos ay maaari kang mag-navigate sa alinman sa mga `.ipynb` files, buksan ang mga ito, at simulan ang paggawa.

### Pagpapatakbo sa Container

Isang alternatibo sa Python installation ay ang patakbuhin ang code sa container. Dahil ang aming repository ay naglalaman ng espesyal na `.devcontainer` folder na nagbibigay ng instruksyon kung paano bumuo ng container para sa repo na ito, ang VS Code ay mag-aalok sa iyo na i-reopen ang code sa container. Kakailanganin nito ang Docker installation, at medyo mas kumplikado, kaya inirerekomenda namin ito para sa mas may karanasan na mga user.

## Pagpapatakbo sa Cloud

Kung ayaw mong mag-install ng Python nang lokal, at may access ka sa ilang cloud resources - isang magandang alternatibo ay ang patakbuhin ang code sa cloud. Mayroong ilang mga paraan upang magawa ito:

* Paggamit ng **[GitHub Codespaces](https://github.com/features/codespaces)**, na isang virtual environment na ginawa para sa iyo sa GitHub, na naa-access sa pamamagitan ng VS Code browser interface. Kung may access ka sa Codespaces, maaari mo lamang i-click ang **Code** button sa repo, simulan ang isang codespace, at magsimula nang mabilis.
* Paggamit ng **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. Ang [Binder](https://mybinder.org) ay libreng computing resources na ibinibigay sa cloud para sa mga taong tulad mo upang subukan ang ilang code sa GitHub. Mayroong button sa front page upang buksan ang repository sa Binder - mabilis ka nitong dadalhin sa binder site, na magtatayo ng underlying container at magsisimula ng Jupyter web interface para sa iyo nang walang kahirap-hirap.

> **Note**: Upang maiwasan ang maling paggamit, ang Binder ay may access sa ilang web resources na naka-block. Maaaring pigilan nito ang ilang code na gumagana, lalo na kung kumukuha ng mga modelo at/o datasets mula sa pampublikong Internet. Maaaring kailanganin mong maghanap ng mga alternatibo. Gayundin, ang compute resources na ibinibigay ng Binder ay medyo basic, kaya ang training ay magiging mabagal, lalo na sa mga mas kumplikadong aralin.

## Pagpapatakbo sa Cloud na may GPU

Ang ilan sa mga huling aralin sa kurikulum na ito ay lubos na makikinabang mula sa GPU support, dahil kung hindi, ang training ay magiging sobrang bagal. Mayroong ilang mga opsyon na maaari mong sundan, lalo na kung may access ka sa cloud alinman sa pamamagitan ng [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), o sa pamamagitan ng iyong institusyon:

* Gumawa ng [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) at kumonekta dito sa pamamagitan ng Jupyter. Maaari mong i-clone ang repo direkta sa makina, at simulan ang pag-aaral. Ang NC-series VMs ay may GPU support.

> **Note**: Ang ilang mga subscription, kabilang ang Azure for Students, ay hindi nagbibigay ng GPU support nang default. Maaaring kailanganin mong humiling ng karagdagang GPU cores sa pamamagitan ng technical support request.

* Gumawa ng [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) at pagkatapos ay gamitin ang Notebook feature doon. [Ang video na ito](https://azure-for-academics.github.io/quickstart/azureml-papers/) ay nagpapakita kung paano i-clone ang repository sa Azure ML notebook at simulan ang paggamit nito.

Maaari mo ring gamitin ang Google Colab, na may kasamang libreng GPU support, at i-upload ang Jupyter Notebooks doon upang i-execute ang mga ito isa-isa.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.