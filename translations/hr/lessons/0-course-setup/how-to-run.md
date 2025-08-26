<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-26T00:37:05+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "hr"
}
-->
# Kako pokrenuti kod

Ovaj kurikulum sadrži mnogo primjera i laboratorijskih vježbi koje možete pokrenuti. Da biste to učinili, trebate mogućnost izvršavanja Python koda u Jupyter Notebooks koji su dio ovog kurikuluma. Postoji nekoliko opcija za pokretanje koda:

## Pokretanje lokalno na vašem računalu

Za pokretanje koda lokalno na vašem računalu, trebate imati instaliranu neku verziju Pythona. Osobno preporučujem instalaciju **[miniconda](https://conda.io/en/latest/miniconda.html)** - to je prilično lagana instalacija koja podržava `conda` upravitelj paketa za različita Python **virtualna okruženja**.

Nakon što instalirate miniconda, trebate klonirati repozitorij i stvoriti virtualno okruženje koje će se koristiti za ovaj tečaj:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Korištenje Visual Studio Code-a s Python ekstenzijom

Vjerojatno najbolji način za korištenje kurikuluma je otvaranje u [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s [Python ekstenzijom](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Napomena**: Kada klonirate i otvorite direktorij u VS Code-u, automatski će vam se predložiti instalacija Python ekstenzija. Također ćete morati instalirati miniconda kako je gore opisano.

> **Napomena**: Ako vam VS Code predloži ponovno otvaranje repozitorija u kontejneru, trebate to odbiti kako biste koristili lokalnu Python instalaciju.

### Korištenje Jupytera u pregledniku

Također možete koristiti Jupyter okruženje izravno iz preglednika na vašem računalu. Zapravo, i klasični Jupyter i Jupyter Hub pružaju prilično praktično razvojno okruženje s automatskim dovršavanjem, isticanjem koda itd.

Za pokretanje Jupytera lokalno, idite u direktorij tečaja i izvršite:

```bash
jupyter notebook
```
ili
```bash
jupyterhub
```
Zatim možete navigirati do bilo koje `.ipynb` datoteke, otvoriti je i početi raditi.

### Pokretanje u kontejneru

Jedna alternativa Python instalaciji je pokretanje koda u kontejneru. Budući da naš repozitorij sadrži posebnu `.devcontainer` mapu koja daje upute za izgradnju kontejnera za ovaj repozitorij, VS Code će vam ponuditi ponovno otvaranje koda u kontejneru. Ovo će zahtijevati instalaciju Dockera, a također će biti složenije, pa ovo preporučujemo iskusnijim korisnicima.

## Pokretanje u oblaku

Ako ne želite instalirati Python lokalno i imate pristup nekim resursima u oblaku, dobra alternativa je pokretanje koda u oblaku. Postoji nekoliko načina kako to možete učiniti:

* Korištenje **[GitHub Codespaces](https://github.com/features/codespaces)**, što je virtualno okruženje stvoreno za vas na GitHubu, dostupno putem VS Code sučelja u pregledniku. Ako imate pristup Codespaces, možete jednostavno kliknuti gumb **Code** u repozitoriju, pokrenuti Codespace i započeti rad u trenu.
* Korištenje **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) pruža besplatne računalne resurse u oblaku za ljude poput vas kako bi isprobali neki kod na GitHubu. Na početnoj stranici postoji gumb za otvaranje repozitorija u Binderu - ovo bi vas brzo trebalo odvesti na Binder stranicu, koja će izgraditi temeljni kontejner i besprijekorno pokrenuti Jupyter web sučelje.

> **Napomena**: Kako bi se spriječila zloupotreba, Binder ima ograničen pristup nekim web resursima. Ovo može spriječiti rad nekog koda koji preuzima modele i/ili skupove podataka s javnog interneta. Možda ćete morati pronaći neka zaobilazna rješenja. Također, računalni resursi koje pruža Binder su prilično osnovni, pa će treniranje biti sporo, posebno u kasnijim, složenijim lekcijama.

## Pokretanje u oblaku s GPU-om

Neke od kasnijih lekcija u ovom kurikulumu značajno bi koristile podršku za GPU, jer bi inače treniranje bilo bolno sporo. Postoji nekoliko opcija koje možete slijediti, posebno ako imate pristup oblaku putem [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ili putem vaše institucije:

* Stvorite [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) i povežite se s njom putem Jupytera. Zatim možete klonirati repozitorij izravno na stroj i započeti učenje. NC-serija VM-ova ima podršku za GPU.

> **Napomena**: Neke pretplate, uključujući Azure for Students, ne pružaju GPU podršku odmah. Možda ćete morati zatražiti dodatne GPU jezgre putem zahtjeva za tehničku podršku.

* Stvorite [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) i zatim koristite značajku Notebook tamo. [Ovaj video](https://azure-for-academics.github.io/quickstart/azureml-papers/) pokazuje kako klonirati repozitorij u Azure ML notebook i početi ga koristiti.

Također možete koristiti Google Colab, koji dolazi s određenom besplatnom GPU podrškom, i tamo učitati Jupyter Notebooks kako biste ih izvršavali jedan po jedan.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.