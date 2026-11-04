# Kaip paleisti kodą

Ši mokymo programa turi daug vykdomų pavyzdžių ir laboratorinių darbų, kuriuos norėsite paleisti. Tam reikia galimybės vykdyti Python kodą Jupyter sąsiuviniuose, pateiktuose kaip šios mokymo programos dalis. Yra keletas galimų būdų, kaip paleisti kodą:

## Paleisti lokaliai savo kompiuteryje

Norėdami paleisti kodą savo kompiuteryje lokaliai, reikia įdiegti Python. Vienas iš rekomenduojamų sprendimų yra įdiegti **[miniconda](https://conda.io/en/latest/miniconda.html)** - tai gana lengva diegimo versija, kuri palaiko `conda` paketų tvarkyklę, skirtą įvairioms Python **virtualioms aplinkoms**.

Įdiegę miniconda, nuklonuokite saugyklą ir sukurkite virtualią aplinką šiam kursui:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Windows pastaba**: jei kuriant aplinką nepavyksta įdiegti `gdk-pixbuf` ir atsiranda `UnicodeDecodeError` klaida, kuri nurodo `gbk` kodeką, įjunkite Python UTF-8 režimą savo terminale ir bandykite dar kartą. Naudokite savo terminalo sintaksę:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Komandos eilutė (`cmd.exe`) arba Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, įskaitant Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Jei nepavykusio bandymo metu liko `ai4beg` aplinka, išjunkite ją ir pašalinkite prieš bandydami dar kartą. Pirmiausia naudokite `conda deactivate` kai aplinka yra aktyvi:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Naudojant Visual Studio Code su Python plėtiniu

Šią mokymo programą geriausia naudoti atidarant ją [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) su [Python plėtiniu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Pastaba**: kai tik nuklonuosite ir atidarysite katalogą VS Code, jis automatiškai pasiūlys įdiegti Python plėtinius. Taip pat turėsite įdiegti miniconda, kaip aprašyta aukščiau.

> **Pastaba**: jei VS Code pasiūlys atidaryti saugyklą konteineryje, turėtumėte atsisakyti šio pasiūlymo, kad galėtumėte naudoti vietinę Python diegimą.

### Naudojant Jupyter naršyklėje

Taip pat galite naudoti Jupyter aplinką naršyklėje savo kompiuteryje. Tiek klasikinis Jupyter, tiek JupyterHub suteikia patogią kūrimo aplinką su automatinio užbaigimo funkcija, kodo paryškinimu ir pan.

Norėdami paleisti Jupyter lokaliai, eikite į kursų katalogą ir vykdykite:

```bash
jupyter notebook
```
arba
```bash
jupyterhub
```
Tuomet galite atidaryti bet kurį iš `.ipynb` failų ir pradėti darbą.

### Paleidimas konteineryje

Viena iš alternatyvų Python diegimui yra paleisti kodą konteineryje. Kadangi mūsų saugykla pateikia specialų `.devcontainer` katalogą, kuriame aprašyta kaip sukurti konteinerį šiai saugyklai, VS Code siūlo galimybę atidaryti kodą konteineryje. Tam reikės įdiegti Docker, ir ši parinktis yra sudėtingesnė, todėl rekomenduojame ją labiau patyrusiems vartotojams.

## Paleidimas debesyje

Jei nenorite lokaliai įdiegti Python ir turite prieigą prie debesies resursų, gera alternatyva būtų paleisti kodą debesyje. Galite rinktis kelis būdus:

* Naudojant **[GitHub Codespaces](https://github.com/features/codespaces)** – tai virtuali aplinka, sukurta jums GitHub platformoje, pasiekiama per VS Code naršyklės sąsają. Jei turite prieigą prie Codespaces, tiesiog paspauskite mygtuką **Code** saugykloje, sukurkite kodų erdvę ir pradėkite darbą per greitą laiką.
* Naudojant **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) suteikia nemokamus kompiuterinius resursus debesyje, skirtus jūsų kodo testavimui GitHub. Pradiniame puslapyje yra mygtukas, leidžiantis atidaryti saugyklą Binder aplinkoje – tai greitai nukreips jus į Binder svetainę, kuri automatiškai sukurs konteinerį ir pradės Jupyter žiniatinklio sąsają.

> **Pastaba**: norint išvengti piktnaudžiavimo, Binder blokuoja prieigą prie kai kurių interneto resursų. Tai gali trukdyti kai kuriems kodo fragmentams, kurie bando parsisiųsti modelius ir/ar duomenų rinkinius iš viešojo interneto, veikti. Gali tekti ieškoti apeinamojo sprendimo. Be to, Binder suteikiami kompiuteriniai resursai yra ganėtinai paprasti, todėl mokymasis vyksta lėtai, ypač vėlesniuose, sudėtingesniuose pamokose.

## Paleidimas debesyje su GPU

Kai kurios vėlesnės šios mokymo programos pamokos ženkliai pasinaudotų GPU palaikymu. Pavyzdžiui, modelio mokymas be to gali būti labai lėtas. Yra keletas galimų būdų, ypač jei turite prieigą prie debesies per [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) arba savo instituciją:

* Sukurkite [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ir prisijunkite prie jos per Jupyter. Galite tiesiogiai klonuoti saugyklą į šią mašiną ir pradėti mokytis. NC serijos VM turi GPU palaikymą.

> **Pastaba**: kai kurios prenumeratos, įskaitant Azure for Students, neturi GPU palaikymo pagal numatytuosius nustatymus. Gali reikėti pateikti techninio palaikymo užklausą dėl papildomų GPU branduolių.

* Sukurkite [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ir naudokite ten Notebook funkciją. [Šis vaizdo įrašas](https://azure-for-academics.github.io/quickstart/azureml-papers/) rodo, kaip klonuoti saugyklą į Azure ML sąsiuvinį ir pradėti jį naudoti.

Taip pat galite naudoti Google Colab, kuris suteikia nemokamą GPU palaikymą, ir ten įkelti Jupyter sąsiuvinius juos vykdyti po vieną.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->