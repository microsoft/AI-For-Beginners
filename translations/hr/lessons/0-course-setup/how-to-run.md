# Kako pokrenuti kod

Ovaj nastavni plan sadrži mnogo izvršnih primjera i laboratorijskih vježbi koje želite pokrenuti. Da biste to učinili, morate imati mogućnost izvršavanja Python koda u Jupyter bilježnicama koje su dio ovog nastavnog plana. Imate nekoliko opcija za pokretanje koda:

## Pokretanje lokalno na vašem računalu

Da biste pokrenuli kod lokalno na vašem računalu, potrebna je Python instalacija. Jedan od prijedloga je instalirati **[miniconda](https://conda.io/en/latest/miniconda.html)** - to je prilično lagana instalacija koja podržava upravitelja paketa `conda` za različita Python **virtualna okruženja**.

Nakon što instalirate miniconda, klonirajte repozitorij i kreirajte virtualno okruženje koje će se koristiti za ovaj tečaj:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Korištenje Visual Studio Code s Python ekstenzijom

Ovaj nastavni plan najbolje je koristiti ako ga otvorite u [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s [Python ekstenzijom](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Napomena**: Kada klonirate i otvorite direktorij u VS Code-u, automatski će vam predložiti instalaciju Python ekstenzija. Također ćete morati instalirati miniconda kako je prethodno opisano.

> **Napomena**: Ako vam VS Code predloži ponovno otvaranje repozitorija u kontejneru, trebate to odbiti kako biste koristili lokalnu Python instalaciju.

### Korištenje Jupyter-a u pregledniku

Također možete koristiti Jupyter okruženje iz preglednika na vašem računalu. I klasični Jupyter i JupyterHub pružaju praktično razvojno okruženje s automatskim dovršavanjem, isticanjem koda itd.

Za pokretanje Jupyter-a lokalno, idite u direktorij tečaja i pokrenite:

```bash
jupyter notebook
```
ili
```bash
jupyterhub
```
Zatim možete navigirati do bilo koje `.ipynb` datoteke, otvoriti je i početi raditi.

### Pokretanje u kontejneru

Jedna alternativa Python instalaciji je pokretanje koda u kontejneru. Budući da naš repozitorij sadrži posebnu mapu `.devcontainer` koja daje upute kako izgraditi kontejner za ovaj repozitorij, VS Code nudi opciju ponovnog otvaranja koda u kontejneru. Za ovo je potrebna instalacija Dockera, a postupak može biti složeniji, pa to preporučujemo iskusnijim korisnicima.

## Pokretanje u oblaku

Ako ne želite instalirati Python lokalno, a imate pristup nekim resursima u oblaku - dobra alternativa je pokretanje koda u oblaku. Postoji nekoliko načina na koje to možete učiniti:

* Korištenje **[GitHub Codespaces](https://github.com/features/codespaces)**, što je virtualno okruženje kreirano za vas na GitHubu, dostupno putem VS Code sučelja u pregledniku. Ako imate pristup Codespaces, samo kliknite na gumb **Code** u repozitoriju, pokrenite codespace i brzo počnite raditi.
* Korištenje **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) nudi besplatne računalne resurse u oblaku za ljude poput vas da isprobaju kod s GitHuba. Na početnoj stranici postoji gumb za otvaranje repozitorija u Binderu - to će vas brzo dovesti na stranicu bindera, koji će izgraditi osnovni kontejner i pokrenuti Jupyter web sučelje bez prekida.

> **Napomena**: Da bi spriječio zlonamjernu upotrebu, Binder ima blokiran pristup nekim mrežnim resursima. To može spriječiti rad nekog koda koji dohvaća modele i/ili skupove podataka s javnog Interneta. Možda ćete trebati pronaći neke zaobilazne načine. Također, računski resursi koje Binder pruža su prilično osnovni, pa će treniranje biti sporo, osobito u kasnijim, složenijim lekcijama.

## Pokretanje u oblaku s GPU

Neke od kasnijih lekcija u ovom nastavnom planu značajno bi imale koristi od podrške za GPU. Na primjer, treniranje modela može biti izuzetno sporo bez toga. Postoji nekoliko opcija koje možete pratiti, osobito ako imate pristup oblaku putem [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ili preko vaše institucije:

* Kreirajte [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) i povežite se na nju putem Jupyter-a. Tada možete klonirati repozitorij direktno na tu mašinu i započeti učenje. NC-serija VM-ova ima podršku za GPU.

> **Napomena**: Neki pretplatnički planovi, uključujući Azure for Students, ne pružaju GPU podršku odmah. Možda ćete morati zatražiti dodatne GPU jezgre tehničkim zahtjevom za podršku.

* Kreirajte [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) i zatim koristite značajku Notebooka tamo. [Ovaj video](https://azure-for-academics.github.io/quickstart/azureml-papers/) pokazuje kako klonirati repozitorij u Azure ML bilježnicu i početi ga koristiti.

Također možete koristiti Google Colab, koji dolazi s besplatnom podrškom za GPU, i tamo učitati Jupyter bilježnice za izvršavanje jednu po jednu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o odricanju od odgovornosti**:
Ovaj je dokument preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se stručni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->