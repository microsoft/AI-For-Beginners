# Cum să Rulați Codul

Acest curriculum conține multe exemple și laboratoare executabile pe care veți dori să le rulați. Pentru a face acest lucru, aveți nevoie de posibilitatea de a executa cod Python în Jupyter Notebooks furnizate ca parte a acestui curriculum. Aveți mai multe opțiuni pentru a rula codul:

## Rulare locală pe calculatorul dvs.

Pentru a rula codul local pe calculatorul dvs., este necesară o instalare Python. O recomandare este să instalați **[miniconda](https://conda.io/en/latest/miniconda.html)** - este o instalare relativ ușoară care suportă managerul de pachete `conda` pentru diferite **medii virtuale** Python.

După ce instalați miniconda, clonați depozitul și creați un mediu virtual care să fie folosit pentru acest curs:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Utilizarea Visual Studio Code cu Extensia Python

Acest curriculum este cel mai bine folosit atunci când îl deschideți în [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) cu [Extensia Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Notă**: Odată ce clonați și deschideți directorul în VS Code, acesta vă va sugera automat să instalați extensiile pentru Python. Va trebui, de asemenea, să instalați miniconda așa cum este descris mai sus.

> **Notă**: Dacă VS Code vă sugerează să redeschideți depozitul într-un container, ar trebui să refuzați această opțiune pentru a folosi instalarea locală Python.

### Utilizarea Jupyter în Browser

Puteți, de asemenea, să folosiți un mediu Jupyter din browser pe propriul calculator. Atât Jupyter clasic, cât și JupyterHub oferă un mediu convenabil de dezvoltare cu completare automată, evidențierea codului, etc.

Pentru a porni Jupyter local, navigați în directorul cursului și executați:

```bash
jupyter notebook
```
sau
```bash
jupyterhub
```
Apoi puteți naviga la oricare din fișierele `.ipynb`, să le deschideți și să începeți să lucrați.

### Rulare în container

O alternativă la instalarea Python ar fi să rulați codul într-un container. Deoarece depozitul nostru oferă un folder special `.devcontainer` care indică cum să construiți un container pentru acest repo, VS Code oferă oportunitatea de a redeschide codul în container. Aceasta va necesita instalarea Docker și ar fi mai complexă, așadar recomandăm acest lucru utilizatorilor mai experimentați.

## Rulare în Cloud

Dacă nu doriți să instalați Python local și aveți acces la unele resurse cloud – o alternativă bună este să rulați codul în cloud. Există mai multe moduri în care puteți face asta:

* Utilizând **[GitHub Codespaces](https://github.com/features/codespaces)**, care este un mediu virtual creat pentru dvs. pe GitHub, accesibil printr-o interfață VS Code în browser. Dacă aveți acces la Codespaces, puteți face pur și simplu clic pe butonul **Code** din repo, începeți un codespace și porniți rapid.
* Utilizând **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) oferă resurse de calcul gratuite furnizate în cloud pentru persoane ca dvs. să testeze cod de pe GitHub. Există un buton pe pagina principală pentru a deschide depozitul în Binder – asta vă va duce rapid pe site-ul Binder, care va construi un container de bază și va porni o interfață web Jupyter pentru dvs. fără probleme.

> **Notă**: Pentru a preveni utilizarea neadecvată, Binder are acces blocat la unele resurse web. Acest lucru poate împiedica funcționarea unor coduri care descarcă modele și/sau seturi de date de pe Internetul public. Va trebui să găsiți unele soluții alternative. În plus, resursele de calcul oferite de Binder sunt destul de simple, deci antrenamentul va fi lent, mai ales în lecțiile mai complexe ulterioare.

## Rulare în Cloud cu GPU

Unele dintre lecțiile ulterioare din acest curriculum ar beneficia foarte mult de suport GPU. Antrenarea modelului, de exemplu, poate fi dureros de lentă altfel. Există câteva opțiuni pe care le puteți urma, mai ales dacă aveți acces la cloud prin [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) sau prin instituția dvs.:

* Creați [Mașină Virtuală pentru Data Science](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) și conectați-vă la ea prin Jupyter. Puteți apoi să clonați repo direct pe mașină și să începeți să învățați. Mașinile virtuale din seria NC au suport GPU.

> **Notă**: Unele abonamente, inclusiv Azure for Students, nu oferă suport GPU din start. Este posibil să trebuiască să solicitați nuclee GPU suplimentare printr-o cerere de asistență tehnică.

* Creați [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) și apoi folosiți funcția Notebook acolo. [Acest video](https://azure-for-academics.github.io/quickstart/azureml-papers/) arată cum să clonați un depozit într-un notebook Azure ML și să începeți să îl folosiți.

De asemenea, puteți folosi Google Colab, care vine cu suport GPU gratuit și puteți încărca acolo Jupyter Notebooks pentru a le executa unul câte unul.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm nicio responsabilitate pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->