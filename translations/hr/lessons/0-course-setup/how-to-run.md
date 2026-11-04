# Kako pokrenuti kod

Ovaj nastavni plan sadrži puno izvršnih primjera i laboratorija koje ćete htjeti pokrenuti. Da biste to mogli učiniti, potrebna vam je mogućnost izvršavanja Python koda u Jupyter bilježnicama koje su dio ovog nastavnog plana. Imate nekoliko opcija za pokretanje koda:

## Pokrenite lokalno na svom računalu

Da biste pokrenuli kod lokalno na svom računalu, potrebna je instalacija Pythona. Jedan od prijedloga je instalirati **[miniconda](https://conda.io/en/latest/miniconda.html)** - to je prilično lagana instalacija koja podržava upravitelj paketa `conda` za razne Python **virtualne okoline**.

Nakon što instalirate miniconda, klonirajte repozitorij i kreirajte virtualno okruženje koje će se koristiti za ovaj tečaj:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Napomena za Windows**: Ako stvaranje okoline ne uspije tijekom instalacije `gdk-pixbuf` s `UnicodeDecodeError` u kojem se spominje `gbk` codec, omogućite UTF-8 mod Pythona u vašem terminalu i pokušajte ponovo. Koristite sintaksu za terminal koji koristite:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Command Prompt (`cmd.exe`) ili Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, uključujući Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Ako je neuspjeli pokušaj ostavio `ai4beg` okruženje, deaktivirajte ga i uklonite to okruženje prije ponovnog pokušaja. Upotrijebite `conda deactivate` prvo dok je okruženje aktivno:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Korištenje Visual Studio Codea s Python ekstenzijom

Ovaj nastavni plan je najbolje koristiti kad ga otvorite u [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s [Python ekstenzijom](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Napomena**: Kada klonirate i otvorite direktorij u VS Codeu, automatski će vam predložiti instalaciju Python ekstenzija. Također ćete morati instalirati miniconda kao što je ranije opisano.

> **Napomena**: Ako vam VS Code predloži ponovno otvaranje repozitorija u kontejneru, trebali biste to odbiti kako biste koristili lokalnu Python instalaciju.

### Korištenje Jupyter-a u pregledniku

Također možete koristiti Jupyter okruženje iz preglednika na vašem računalu. Klasični Jupyter i JupyterHub pružaju zgodno razvojno okruženje s automatskim dovršavanjem, isticanjem koda itd.

Da biste pokrenuli Jupyter lokalno, idite u direktorij tečaja i izvršite:

```bash
jupyter notebook
```
ili
```bash
jupyterhub
```
Tada možete pristupiti bilo kojoj od `.ipynb` datoteka, otvoriti ih i početi raditi.

### Pokretanje u kontejneru

Jedna alternativa instalaciji Pythona bila bi pokretanje koda u kontejneru. Budući da naš repozitorij sadrži posebnu mapu `.devcontainer` koja daje upute kako izgraditi kontejner za ovaj repozitorij, VS Code nudi mogućnost ponovnog otvaranja koda u kontejneru. To zahtijeva instalaciju Dockera i također je složenije, pa to preporučujemo iskusnijim korisnicima.

## Pokretanje u oblaku

Ako ne želite instalirati Python lokalno i imate pristup nekim resursima u oblaku - dobra alternativa je pokretati kod u oblaku. Postoji nekoliko načina na koje to možete učiniti:

* Korištenje **[GitHub Codespaces](https://github.com/features/codespaces)**, što je virtualno okruženje kreirano za vas na GitHubu, pristupačno putem VS Code pregledničkog sučelja. Ako imate pristup Codespaces, jednostavno možete kliknuti na gumb **Code** u repozitoriju, pokrenuti codespace i započeti bez odgode.
* Korištenje **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) nudi besplatne računalne resurse u oblaku za ljude poput vas za testiranje nekog koda na GitHubu. Na početnoj stranici postoji gumb za otvaranje repozitorija u Binderu – to bi vas brzo trebalo odvesti na Binder stranicu, koja će izgraditi temeljan spremnik i besprijekorno pokrenuti Jupyter web sučelje za vas.

> **Napomena**: Kako bi se spriječila zlouporaba, Binder ima blokiran pristup nekim mrežnim resursima. To može spriječiti da neki kod radi, osobito onaj koji preuzima modele i/ili skupove podataka s javnog Interneta. Možda ćete trebati pronaći neka zaobilazna rješenja. Također, računalni resursi koje pruža Binder su prilično osnovni, pa će treniranje biti sporo, osobito u kasnijim, složenijim lekcijama.

## Pokretanje u oblaku s GPU-om

Neke od kasnijih lekcija u ovom kurikulumu bi itekako imale koristi od podrške za GPU. Na primjer, treniranje modela može biti iznimno sporo bez toga. Postoji nekoliko opcija koje možete slijediti, osobito ako imate pristup oblaku bilo kroz [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ili kroz vašu instituciju:

* Kreirajte [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) i povežite se na nju putem Jupytera. Tada možete klonirati repozitorij direktno na stroj i započeti s učenjem. NC-serija VM-ova podržava GPU.

> **Napomena**: Neke pretplate, uključujući Azure for Students, ne pružaju podršku za GPU odmah. Možda ćete morati zatražiti dodatne GPU jezgre putem zahtjeva za tehničku podršku.

* Kreirajte [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) i zatim koristite značajku bilježnice tamo. [Ovaj video](https://azure-for-academics.github.io/quickstart/azureml-papers/) pokazuje kako klonirati repozitorij u Azure ML bilježnicu i početi ga koristiti.

Također možete koristiti Google Colab, koji dolazi s besplatnom podrškom za GPU, i tamo učitavati Jupyter bilježnice za izvođenje jednu po jednu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->