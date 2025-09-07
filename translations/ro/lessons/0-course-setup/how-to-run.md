<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-26T00:35:53+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "ro"
}
-->
# Cum să rulezi codul

Acest curs conține multe exemple executabile și laboratoare pe care vei dori să le rulezi. Pentru a face acest lucru, ai nevoie de posibilitatea de a executa cod Python în Jupyter Notebooks, care sunt furnizate ca parte a acestui curs. Ai mai multe opțiuni pentru a rula codul:

## Rulează local pe computerul tău

Pentru a rula codul local pe computerul tău, trebuie să ai instalată o versiune de Python. Personal, recomand instalarea **[miniconda](https://conda.io/en/latest/miniconda.html)** - este o instalare destul de ușoară care suportă managerul de pachete `conda` pentru diferite **medii virtuale** Python.

După ce instalezi miniconda, trebuie să clonezi repository-ul și să creezi un mediu virtual care va fi folosit pentru acest curs:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Utilizarea Visual Studio Code cu extensia Python

Probabil cea mai bună metodă de a folosi acest curs este să-l deschizi în [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) cu [extensia Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: După ce clonezi și deschizi directorul în VS Code, acesta îți va sugera automat să instalezi extensiile Python. De asemenea, va trebui să instalezi miniconda, așa cum este descris mai sus.

> **Note**: Dacă VS Code îți sugerează să redeschizi repository-ul într-un container, trebuie să refuzi această opțiune pentru a folosi instalarea locală de Python.

### Utilizarea Jupyter în browser

Poți folosi și mediul Jupyter direct din browser pe computerul tău. De fapt, atât Jupyter clasic, cât și Jupyter Hub oferă un mediu de dezvoltare destul de convenabil, cu completare automată, evidențiere a codului etc.

Pentru a porni Jupyter local, mergi în directorul cursului și execută:

```bash
jupyter notebook
```  
sau  
```bash
jupyterhub
```  
Apoi poți naviga la orice fișier `.ipynb`, să-l deschizi și să începi să lucrezi.

### Rularea într-un container

O alternativă la instalarea Python ar fi rularea codului într-un container. Deoarece repository-ul nostru conține un folder special `.devcontainer` care indică cum să construiești un container pentru acest repository, VS Code îți va oferi opțiunea de a redeschide codul într-un container. Acest lucru va necesita instalarea Docker și va fi mai complex, așa că recomandăm această opțiune utilizatorilor mai experimentați.

## Rularea în cloud

Dacă nu dorești să instalezi Python local și ai acces la resurse cloud, o alternativă bună ar fi să rulezi codul în cloud. Există mai multe modalități de a face acest lucru:

* Utilizând **[GitHub Codespaces](https://github.com/features/codespaces)**, care este un mediu virtual creat pentru tine pe GitHub, accesibil prin interfața browserului VS Code. Dacă ai acces la Codespaces, poți pur și simplu să dai click pe butonul **Code** din repository, să pornești un codespace și să începi să lucrezi imediat.
* Utilizând **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) oferă resurse de calcul gratuite în cloud pentru a testa codul de pe GitHub. Există un buton pe pagina principală pentru a deschide repository-ul în Binder - acest lucru te va duce rapid pe site-ul Binder, care va construi containerul subiacente și va porni interfața web Jupyter pentru tine fără probleme.

> **Note**: Pentru a preveni utilizarea abuzivă, Binder are accesul la unele resurse web blocat. Acest lucru poate împiedica funcționarea unor coduri care descarcă modele și/sau seturi de date de pe Internet. Este posibil să fie nevoie să găsești soluții alternative. De asemenea, resursele de calcul oferite de Binder sunt destul de limitate, așa că antrenarea va fi lentă, mai ales în lecțiile mai complexe.

## Rularea în cloud cu GPU

Unele dintre lecțiile mai avansate din acest curs ar beneficia foarte mult de suportul GPU, deoarece altfel antrenarea va fi extrem de lentă. Există câteva opțiuni pe care le poți urma, mai ales dacă ai acces la cloud fie prin [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), fie prin instituția ta:

* Creează o [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) și conectează-te la ea prin Jupyter. Poți clona repository-ul direct pe mașină și să începi să înveți. Mașinile virtuale din seria NC au suport pentru GPU.

> **Note**: Unele abonamente, inclusiv Azure for Students, nu oferă suport pentru GPU implicit. Este posibil să fie nevoie să soliciți resurse GPU suplimentare printr-o cerere de suport tehnic.

* Creează un [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) și folosește funcția Notebook de acolo. [Acest video](https://azure-for-academics.github.io/quickstart/azureml-papers/) arată cum să clonezi un repository în notebook-ul Azure ML și să începi să-l folosești.

De asemenea, poți folosi Google Colab, care oferă suport gratuit pentru GPU, și să încarci Jupyter Notebooks acolo pentru a le executa pe rând.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.