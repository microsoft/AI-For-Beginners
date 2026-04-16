# Gabay sa Pag-aayos ng AI-For-Beginners

Ang gabay na ito ay tumutulong sa iyo na lutasin ang mga karaniwang problema na nararanasan habang ginagamit o nag-aambag sa [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) repository. Ang bawat problema ay may kasamang background, sintomas, paliwanag, at mga hakbang sa solusyon.

---

## Nilalaman

- [Mga Pangkalahatang Isyu](../..)
- [Mga Isyu sa Pag-install](../..)
- [Mga Isyu sa Konpigurasyon](../..)
- [Pagpapatakbo ng mga Notebook](../..)
- [Mga Problema sa Performance](../..)
- [Mga Problema sa Website ng Textbook](../..)
- [Mga Isyu sa Pag-aambag](../..)
- [FAQ](../..)
- [Pagkuha ng Tulong](../..)

---

## Mga Pangkalahatang Isyu

### 1. Hindi Maayos na Nakokopya ang Repository

**Background:** Ang cloning ay nagbibigay-daan sa iyo na kopyahin ang repository sa iyong makina.

**Sintomas:**
- Error: `fatal: repository not found`
- Error: `Permission denied (publickey)`

**Mga Posibleng Sanhi:**
- Mali ang URL ng repository
- Kulang sa pahintulot
- Hindi naka-configure ang SSH keys

**Mga Solusyon:**
1. **Suriin ang URL ng repository.**  
   Gamitin ang HTTPS URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Lumipat sa HTTPS kung nabigo ang SSH.**  
   Kung makikita mo ang `Permission denied (publickey)`, gamitin ang HTTPS link sa itaas sa halip na SSH.
3. **I-configure ang SSH keys (opsyonal).**  
   Kung nais mong gumamit ng SSH, sundin ang [GitHub's SSH guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Mga Isyu sa Pag-install

### 2. Mga Problema sa Python Environment

**Background:** Ang repository ay umaasa sa Python at iba't ibang libraries.

**Sintomas:**
- Error: `ModuleNotFoundError: No module named '<package>'`
- Mga error sa import kapag nagpapatakbo ng mga script o notebook

**Mga Posibleng Sanhi:**
- Hindi naka-install ang mga dependencies
- Mali ang bersyon ng Python

**Mga Solusyon:**
1. **Mag-set up ng virtual environment.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **I-install ang mga dependencies.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Suriin ang bersyon ng Python.**  
   Gamitin ang Python 3.7 o mas bago.  
   ```bash
   python --version
   ```

### 3. Hindi Naka-install ang Jupyter

**Background:** Ang mga notebook ay pangunahing mapagkukunan ng pag-aaral.

**Sintomas:**
- Error: `jupyter: command not found`
- Hindi gumagana ang mga notebook

**Mga Posibleng Sanhi:**
- Hindi naka-install ang Jupyter

**Mga Solusyon:**
1. **I-install ang Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   o, kung gumagamit ng Anaconda:
   ```bash
   conda install notebook
   ```
2. **Simulan ang Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Mga Salungatan sa Bersyon ng Dependency

**Background:** Ang mga proyekto ay maaaring masira kung hindi tugma ang mga bersyon ng package.

**Sintomas:**
- Mga error o babala tungkol sa hindi tugmang bersyon

**Mga Posibleng Sanhi:**
- Luma o salungat na mga package ng Python

**Mga Solusyon:**
1. **I-install sa malinis na environment.**  
   Tanggalin ang lumang venv/conda env at gumawa ng bago.
2. **Gamitin ang eksaktong bersyon.**  
   Palaging patakbuhin:
   ```bash
   pip install -r requirements.txt
   ```
   Kung nabigo ito, manu-manong i-install ang mga nawawalang package ayon sa README.

---

## Mga Isyu sa Konpigurasyon

### 5. Hindi Naka-set ang Environment Variables

**Background:** Ang ilang mga module ay maaaring mangailangan ng mga key, token, o mga setting ng config.

**Sintomas:**
- Error: `KeyError` o mga babala tungkol sa nawawalang configuration

**Mga Posibleng Sanhi:**
- Hindi naka-set ang kinakailangang environment variables

**Mga Solusyon:**
1. **Suriin ang `.env.example` o mga katulad na file.**
2. **Gumawa ng `.env` file at punan ang kinakailangang mga halaga.**
3. **I-reload ang iyong terminal o IDE pagkatapos i-set ang environment variables.**

---

## Pagpapatakbo ng mga Notebook

### 6. Hindi Nagbubukas o Gumagana ang Notebook

**Background:** Ang Jupyter notebooks ay nangangailangan ng tamang setup.

**Sintomas:**
- Hindi gumagana ang notebook
- Hindi awtomatikong nagbubukas ang browser

**Mga Posibleng Sanhi:**
- Hindi naka-install ang Jupyter
- Mga isyu sa configuration ng browser

**Mga Solusyon:**
1. **I-install ang Jupyter (tingnan ang Mga Isyu sa Pag-install sa itaas).**
2. **Manu-manong buksan ang mga notebook.**
   - Kopyahin ang URL mula sa terminal (hal., `http://localhost:8888/?token=...`) at i-paste ito sa iyong browser.

### 7. Kernel Nagka-crash o Nagha-hang

**Background:** Ang mga kernel ng notebook ay maaaring mag-crash dahil sa limitasyon ng resources o mga error sa code.

**Sintomas:**
- Ang kernel ay namamatay o paulit-ulit na nagre-restart
- Mga error sa out-of-memory

**Mga Posibleng Sanhi:**
- Malalaking dataset
- Hindi tugmang code o mga package

**Mga Solusyon:**
1. **I-restart ang kernel.**  
   Gamitin ang "Restart Kernel" button sa Jupyter.
2. **Suriin ang paggamit ng memory.**  
   Isara ang mga hindi ginagamit na application.
3. **Patakbuhin ang mga notebook sa cloud platforms.**  
   Gamitin ang [Google Colab](https://colab.research.google.com/) o [Azure Notebooks](https://notebooks.azure.com/).

---

## Mga Problema sa Performance

### 8. Mabagal ang Pagpapatakbo ng Notebook

**Background:** Ang ilang mga AI task ay nangangailangan ng malaking memorya at CPU.

**Sintomas:**
- Mabagal na execution
- Maingay ang fan ng laptop

**Mga Posibleng Sanhi:**
- Malalaking dataset o modelo
- Limitadong resources ng sistema

**Mga Solusyon:**
1. **Gumamit ng cloud platform.**
   - I-upload ang notebook sa Colab o Azure Notebooks.
2. **Bawasan ang laki ng dataset.**
   - Gamitin ang sample data para sa pagsasanay.
3. **Isara ang mga hindi kinakailangang programa.**
   - Palayain ang RAM ng sistema.

---

## Mga Problema sa Website ng Textbook

### 9. Hindi Naglo-load ang Chapter

**Background:** Ang online textbook ay nagpapakita ng mga aralin at kabanata.

**Sintomas:**
- Isang kabanata (hal., Transformers/BERT) ay nawawala o hindi nagbubukas

**Kilalang Isyu:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. can't be opened on the textbook website.” Dulot ng error sa filename (`READMEtransformers.md` sa halip na `README.md`).

**Mga Solusyon:**
1. **Suriin ang mga error sa pag-renaming ng file.**  
   Kung ikaw ay isang contributor, tiyakin na ang mga file ng kabanata ay pinangalanang `README.md`.
2. **I-report ang mga nawawalang file.**  
   Magbukas ng GitHub issue na may pangalan ng kabanata at mga detalye ng error.

---

## Mga Isyu sa Pag-aambag

### 10. Hindi Tinanggap ang PR o Nabigo ang Builds

**Background:** Ang mga kontribusyon ay kailangang pumasa sa mga pagsusulit at sumunod sa mga alituntunin.

**Sintomas:**
- Tinanggihan ang pull request
- Mga error sa CI/CD pipeline

**Mga Posibleng Sanhi:**
- Nabigong mga pagsusulit
- Hindi pagsunod sa coding standards

**Mga Solusyon:**
1. **Basahin ang mga alituntunin sa kontribusyon.**
   - Sundin ang [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) ng repository.
2. **Patakbuhin ang mga pagsusulit nang lokal bago mag-push.**
3. **Suriin ang mga linting rules o mga kinakailangan sa formatting.**

---

## FAQ

### Saan ko mahahanap ang tulong para sa mga partikular na module?
- Ang bawat module ay karaniwang may sariling README. Simulan doon para sa mga tip sa setup at paggamit.

### Paano ako magre-report ng bug o magre-request ng feature?
- [Magbukas ng GitHub Issue](https://github.com/microsoft/AI-For-Beginners/issues/new) na may malinaw na paglalarawan at mga hakbang para maulit ang problema.

### Maaari ba akong humingi ng tulong kung ang aking problema ay hindi nakalista?
- Oo! Hanapin muna ang mga umiiral na isyu, at kung hindi mo makita ang iyong problema, gumawa ng bagong isyu.

---

## Pagkuha ng Tulong

- **Suriin ang Mga Isyu:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Magtanong:** Gamitin ang GitHub Discussions o magbukas ng isyu.
- **Komunidad:** Tingnan ang mga link ng repository para sa chat/forum options.

---

_Huling Na-update: 2025-09-20_

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.