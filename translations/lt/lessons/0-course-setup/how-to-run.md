# Kaip paleisti kodą

Ši mokymo programa apima daug vykdomų pavyzdžių ir laboratorinių darbų, kuriuos norėsite paleisti. Tam jums reikalinga galimybė vykdyti Python kodą Jupyter užrašinėse, pateiktose kaip šios mokymo programos dalis. Turite keletą galimybių kodui paleisti:

## Paleisti vietoje savo kompiuteryje

Norėdami paleisti kodą vietoje savo kompiuteryje, reikia įdiegti Python. Vienas iš rekomenduojamų sprendimų yra įdiegti **[miniconda](https://conda.io/en/latest/miniconda.html)** – tai gana lengvas diegimas, palaikantis `conda` paketo tvarkyklę skirtingoms Python **virtualioms aplinkoms**.

Įdiegę minicondą, klonuokite saugyklą ir susikurkite virtualią aplinką, kuri bus naudojama šiam kursui:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Naudojant Visual Studio Code su Python plėtiniu

Ši mokymo programa geriausiai naudojama atidarius ją [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) su [Python plėtiniu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Pastaba**: Kai klonuojate ir atidarote katalogą VS Code, jis automatiškai pasiūlys įdiegti Python plėtinius. Taip pat turėsite įdiegti minicondą, kaip aprašyta aukščiau.

> **Pastaba**: Jei VS Code pasiūlys jums iš naujo atidaryti saugyklą konteineryje, turėtumėte tai atmesti, kad naudotumėte vietinę Python diegimą.

### Naudojant Jupyter naršyklėje

Taip pat galite naudoti Jupyter aplinką per naršyklę savo kompiuteryje. Tiek klasikinis Jupyter, tiek JupyterHub suteikia patogią kūrimo aplinką su automatinio pildymo galimybėmis, kodo paryškinimu ir kita.

Norėdami paleisti Jupyter vietoje, eikite į kurso katalogą ir vykdykite:

```bash
jupyter notebook
```
arba
```bash
jupyterhub
```
Tada galite pereiti į bet kurį `.ipynb` failą, atidaryti jį ir pradėti darbą.

### Paleidimas konteineryje

Viena iš alternatyvų Python diegimui būtų kodą paleisti konteineryje. Kadangi mūsų saugykloje yra specialus `.devcontainer` aplankas, kuris nurodo, kaip sukurti konteinerį šiai saugyklai, VS Code siūlo galimybę iš naujo atidaryti kodą konteineryje. Tai reikalauja Docker diegimo ir yra sudėtingiau, todėl rekomenduojame tai labiau pažengusiems vartotojams.

## Paleidimas debesyje

Jei nenorite diegti Python vietoje ir turite prieigą prie debesijos – gera alternatyva būtų paleisti kodą debesyje. Yra keletas būdų, kaip tai padaryti:

* Naudojant **[GitHub Codespaces](https://github.com/features/codespaces)** – tai virtuali aplinka, sukurta jums GitHub platformoje, pasiekiama per VS Code naršyklės sąsają. Jei turite prieigą prie Codespaces, tiesiog spustelėkite **Code** mygtuką saugykloje, paleiskite codespace ir pradėkite darbą vos per kelias minutes.
* Naudojant **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) suteikia nemokamas skaičiavimo išteklių debesyje žmonėms, kaip jūs, norintiems išbandyti kodą iš GitHub. Pagrindiniame puslapyje yra mygtukas, leidžiantis atidaryti saugyklą Binder platformoje – tai greitai nuves į Binder svetainę, kuri sukurs fono konteinerį ir sklandžiai paleis Jupyter interneto sąsają.

> **Pastaba**: Siekiant išvengti piktnaudžiavimo, Binder prieiga prie kai kurių interneto išteklių yra blokuojama. Tai gali trukdyti veikti kai kuriems kodams, kurie parsisiunčia modelius ir/ar duomenų rinkinius iš viešojo interneto. Gali tekti ieškoti sprendimų. Taip pat Binderyje teikiami skaičiavimo ištekliai yra pakankamai baziniai, todėl modelių mokymas bus lėtas, ypač vėlesniuose sudėtingesniuose pamokų etapuose.

## Paleidimas debesyje su GPU palaikymu

Kai kurios vėlesnės pamokos šioje mokymo programoje labai naudos GPU palaikymą. Pavyzdžiui, modelių mokymas kitu atveju gali būti labai lėtas. Galite rinktis kelis variantus, ypač jei turite prieigą prie debesijos per [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) arba per savo instituciją:

* Sukurkite [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ir prisijunkite prie jos per Jupyter. Tuomet galite klonuoti saugyklą tiesiai į mašiną ir pradėti mokytis. NC serijos VM turi GPU palaikymą.

> **Pastaba**: Kai kurios prenumeratos, įskaitant Azure for Students, pagal nutylėjimą GPU palaikymo neteikia. Gali prireikti pateikti techninės pagalbos užklausą dėl papildomų GPU branduolių.

* Sukurkite [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ir naudokite ten Notebook funkciją. [Šis vaizdo įrašas](https://azure-for-academics.github.io/quickstart/azureml-papers/) rodo, kaip klonuoti saugyklą į Azure ML užrašinę ir pradėti ją naudoti.

Taip pat galite naudoti Google Colab, kuris suteikia nemokamą GPU palaikymą, ir įkelti Jupyter užrašines po vieną, kad jas vykdytumėte.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų arba netikslumų. Originalus dokumentas gimtąja kalba turi būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->