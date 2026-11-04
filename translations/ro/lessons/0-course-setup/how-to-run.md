# Cum să Rulezi Codul

Acest curriculum conține multe exemple și laboratoare executabile pe care le vei dori să le rulezi. Pentru a face acest lucru, ai nevoie de capacitatea de a executa cod Python în Jupyter Notebooks furnizate ca parte a acestui curriculum. Ai mai multe opțiuni pentru a rula codul:

## Rulează local pe calculatorul tău

Pentru a rula codul local pe calculatorul tău, este necesară o instalare Python. O recomandare este să instalezi **[miniconda](https://conda.io/en/latest/miniconda.html)** - este o instalare destul de ușoară care suportă managerul de pachete `conda` pentru diferite **medii virtuale** Python.

După ce instalezi miniconda, clonează depozitul și creează un mediu virtual care să fie folosit pentru acest curs:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Notă Windows**: Dacă crearea mediului eșuează în timp ce instalezi `gdk-pixbuf` cu un `UnicodeDecodeError` care menționează codec-ul `gbk`, activează modul UTF-8 al Python în terminalul tău și încearcă din nou. Folosește sintaxa pentru terminalul pe care îl utilizezi:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Command Prompt (`cmd.exe`) sau Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, inclusiv Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Dacă o încercare eșuată a lăsat în urmă mediul `ai4beg`, dezactivează-l și elimină acel mediu înainte de a încerca din nou. Folosește mai întâi `conda deactivate` când un mediu este activ:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Folosind Visual Studio Code cu Extensia Python

Acest curriculum este folosit cel mai bine deschizându-l în [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) cu [Extensia Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Notă**: Odată ce clonezi și deschizi directorul în VS Code, acesta îți va sugera automat să instalezi extensiile Python. Va trebui să instalezi și miniconda, așa cum este descris mai sus.

> **Notă**: Dacă VS Code îți sugerează să redeschizi depozitul într-un container, ar trebui să refuzi acest lucru pentru a utiliza instalarea locală Python.

### Folosind Jupyter în Browser

Poți folosi de asemenea un mediu Jupyter din browser pe calculatorul tău. Atât Jupyter clasic, cât și JupyterHub oferă un mediu de dezvoltare convenabil cu completare automată, evidențierea codului etc.

Pentru a porni Jupyter local, mergi în directorul cursului și execută:

```bash
jupyter notebook
```
sau
```bash
jupyterhub
```
Poți apoi naviga la oricare dintre fișierele `.ipynb`, să le deschizi și să începi să lucrezi.

### Rulare în container

O alternativă la instalarea Python ar fi să rulezi codul într-un container. Deoarece depozitul nostru oferă un folder special `.devcontainer` care oferă instrucțiuni de construire a unui container pentru acest repo, VS Code oferă oportunitatea de a redeschide codul într-un container. Aceasta va necesita instalarea Docker și ar fi mai complexă, deci recomandăm această opțiune utilizatorilor mai experimentați.

## Rulare în Cloud

Dacă nu dorești să instalezi Python local și ai acces la unele resurse cloud - o alternativă bună ar fi să rulezi codul în cloud. Există mai multe moduri de a face acest lucru:

* Folosind **[GitHub Codespaces](https://github.com/features/codespaces)**, care este un mediu virtual creat pentru tine pe GitHub, accesibil printr-o interfață de browser VS Code. Dacă ai acces la Codespaces, poți pur și simplu să apeși butonul **Code** în repo, să pornești un codespace și să începi să lucrezi în cel mai scurt timp.
* Folosind **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) oferă resurse gratuite de calcul puse la dispoziție în cloud pentru persoane ca tine care vor să testeze cod pe GitHub. Există un buton pe pagina principală pentru a deschide depozitul în Binder - acest lucru ar trebui să te ducă rapid pe site-ul Binder, unde se va construi un container de bază și se va porni o interfață web Jupyter fără probleme.

> **Notă**: Pentru a preveni utilizarea necorespunzătoare, Binder are accesul la unele resurse web blocat. Acest lucru poate împiedica funcționarea unor părți din cod, care descarcă modele și/sau seturi de date de pe Internetul public. Este posibil să trebuiască să găsești unele soluții alternative. De asemenea, resursele de calcul oferite de Binder sunt destul de de bază, deci antrenarea va fi lentă, mai ales în lecțiile ulterioare, mai complexe.

## Rularea în Cloud cu GPU

Unele dintre lecțiile ulterioare din acest curriculum ar beneficia foarte mult de suport GPU. Antrenamentul modelelor, de exemplu, poate fi dureros de lent altfel. Există câteva opțiuni pe care le poți urma, mai ales dacă ai acces la cloud fie prin [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), fie prin instituția ta:

* Creează [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) și conectează-te la ea prin Jupyter. Poți apoi clona depozitul direct pe mașina virtuală și începe să înveți. Mașinile virtuale din seria NC au suport GPU.

> **Notă**: Unele abonamente, inclusiv Azure for Students, nu oferă suport GPU din start. Este posibil să trebuiască să soliciți procesoare GPU suplimentare printr-o cerere de suport tehnic.

* Creează [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) și folosește acolo funcția Notebook. [Acest video](https://azure-for-academics.github.io/quickstart/azureml-papers/) arată cum să clonezi un depozit în notebook-ul Azure ML și să începi să îl folosești.

Poți de asemenea să folosești Google Colab, care oferă un anumit suport gratuit pentru GPU, și să încarci acolo Jupyter Notebooks pentru execuție pe rând.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->