<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-31T17:43:26+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "lt"
}
-->
# Generatyviniai priešiniai tinklai

Ankstesniame skyriuje sužinojome apie **generatyvinius modelius**: modelius, kurie gali generuoti naujus vaizdus, panašius į tuos, kurie yra mokymo duomenų rinkinyje. VAE buvo geras generatyvinio modelio pavyzdys.

## [Klausimynas prieš paskaitą](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Tačiau, jei bandysime generuoti kažką tikrai prasmingo, pavyzdžiui, paveikslą su tinkama raiška, naudojant VAE, pastebėsime, kad mokymas nesusikoncentruoja gerai. Šiam tikslui turėtume išmokti apie kitą architektūrą, specialiai skirtą generatyviniams modeliams - **Generatyviniai priešiniai tinklai**, arba GAN.

Pagrindinė GAN idėja yra turėti du neuroninius tinklus, kurie bus mokomi vienas prieš kitą:

<img src="images/gan_architecture.png" width="70%"/>

> Vaizdas sukurtas [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Šiek tiek terminologijos:
> * **Generatorius** yra tinklas, kuris paima atsitiktinį vektorių ir sukuria vaizdą kaip rezultatą.
> * **Diskriminatorius** yra tinklas, kuris paima vaizdą ir turi nustatyti, ar tai tikras vaizdas (iš mokymo duomenų rinkinio), ar jis buvo sukurtas generatoriaus. Iš esmės tai yra vaizdų klasifikatorius.

### Diskriminatorius

Diskriminatoriaus architektūra nesiskiria nuo įprasto vaizdų klasifikavimo tinklo. Paprasčiausiu atveju tai gali būti visiškai sujungtas klasifikatorius, tačiau dažniausiai tai bus [konvoliucinis tinklas](../07-ConvNets/README.md).

> ✅ GAN, pagrįstas konvoliuciniais tinklais, vadinamas [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

CNN diskriminatorius susideda iš šių sluoksnių: keli konvoliuciniai+apjungimo sluoksniai (su mažėjančiu erdviniu dydžiu) ir vienas ar daugiau visiškai sujungtų sluoksnių, kad būtų gautas "funkcijų vektorius", galutinis dvejetainis klasifikatorius.

> ✅ „Apjungimas“ šiame kontekste yra technika, kuri sumažina vaizdo dydį. „Apjungimo sluoksniai sumažina duomenų matmenis, sujungdami neuronų grupių iš vieno sluoksnio išvestis į vieną neuroną kitame sluoksnyje.“ - [šaltinis](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generatorius

Generatorius yra šiek tiek sudėtingesnis. Jį galima laikyti atvirkštiniu diskriminatoriumi. Pradedant nuo latentinio vektoriaus (vietoj funkcijų vektoriaus), jis turi visiškai sujungtą sluoksnį, kad konvertuotų jį į reikiamą dydį/formą, po to eina dekonvoliuciniai+didinimo sluoksniai. Tai panašu į *dekoderio* dalį [autoenkoderyje](../09-Autoencoders/README.md).

> ✅ Kadangi konvoliucinis sluoksnis įgyvendinamas kaip linijinis filtras, einantis per vaizdą, dekonvoliucija iš esmės yra panaši į konvoliuciją ir gali būti įgyvendinta naudojant tą pačią sluoksnio logiką.

<img src="images/gan_arch_detail.png" width="70%"/>

> Vaizdas sukurtas [Dmitry Soshnikov](http://soshnikov.com)

### GAN mokymas

GAN vadinami **priešiniais**, nes generatorius ir diskriminatorius nuolat konkuruoja tarpusavyje. Šios konkurencijos metu tiek generatorius, tiek diskriminatorius tobulėja, todėl tinklas išmoksta generuoti vis geresnius vaizdus.

Mokymas vyksta dviem etapais:

* **Diskriminatoriaus mokymas**. Ši užduotis yra gana paprasta: mes generuojame vaizdų partiją su generatoriumi, pažymime juos 0, kas reiškia netikrus vaizdus, ir paimame vaizdų partiją iš įvesties duomenų rinkinio (su žyma 1, tikras vaizdas). Mes gauname tam tikrą *diskriminatoriaus nuostolį* ir atliekame atgalinį skaičiavimą.
* **Generatoriaus mokymas**. Tai šiek tiek sudėtingiau, nes mes tiesiogiai nežinome, kokio rezultato tikimės iš generatoriaus. Mes paimame visą GAN tinklą, sudarytą iš generatoriaus ir diskriminatoriaus, pateikiame jam atsitiktinius vektorius ir tikimės, kad rezultatas bus 1 (atitinkantis tikrus vaizdus). Tada užšaldome diskriminatoriaus parametrus (nenorime, kad jis būtų mokomas šiame žingsnyje) ir atliekame atgalinį skaičiavimą.

Šio proceso metu tiek generatoriaus, tiek diskriminatoriaus nuostoliai reikšmingai nemažėja. Idealiu atveju jie turėtų svyruoti, atspindėdami abiejų tinklų veikimo gerėjimą.

## ✍️ Pratimai: GAN

* [GAN užrašų knygelė TensorFlow/Keras](GANTF.ipynb)
* [GAN užrašų knygelė PyTorch](GANPyTorch.ipynb)

### Problemos su GAN mokymu

GAN yra žinomi kaip ypač sunkiai mokomi. Štai kelios problemos:

* **Režimo susiliejimas**. Šiuo terminu apibūdinama situacija, kai generatorius išmoksta generuoti vieną sėkmingą vaizdą, kuris apgauna diskriminatorių, o ne įvairius skirtingus vaizdus.
* **Jautrumas hiperparametrams**. Dažnai galima pastebėti, kad GAN visai nesusikoncentruoja, o tada staiga sumažėja mokymosi greitis, dėl ko pasiekiama konvergencija.
* **Balanso palaikymas** tarp generatoriaus ir diskriminatoriaus. Daugeliu atvejų diskriminatoriaus nuostolis gali greitai nukristi iki nulio, dėl ko generatorius nebegali toliau mokytis. Norint tai įveikti, galima pabandyti nustatyti skirtingus mokymosi greičius generatoriui ir diskriminatoriui arba praleisti diskriminatoriaus mokymą, jei nuostolis jau yra per mažas.
* Mokymas **aukštos raiškos** vaizdams. Tai atspindi tą pačią problemą kaip ir su autoenkoderiais, kai per daug konvoliucinio tinklo sluoksnių rekonstrukcija sukelia artefaktus. Ši problema paprastai sprendžiama vadinamuoju **progresyviu augimu**, kai pirmiausia keli sluoksniai mokomi su mažos raiškos vaizdais, o tada sluoksniai „atrakinami“ arba pridedami. Kitas sprendimas būtų pridėti papildomas jungtis tarp sluoksnių ir mokyti kelias raiškas vienu metu - daugiau informacijos rasite šiame [Multi-Scale Gradient GANs straipsnyje](https://arxiv.org/abs/1903.06048).

## Stiliaus perkėlimas

GAN yra puikus būdas generuoti meninius vaizdus. Kitas įdomus metodas yra vadinamasis **stiliaus perkėlimas**, kuris paima vieną **turinio vaizdą** ir perpiešia jį kitu stiliumi, pritaikydamas filtrus iš **stiliaus vaizdo**.

Kaip tai veikia:
* Pradedame nuo atsitiktinio triukšmo vaizdo (arba nuo turinio vaizdo, bet supratimui lengviau pradėti nuo atsitiktinio triukšmo).
* Mūsų tikslas būtų sukurti tokį vaizdą, kuris būtų artimas tiek turinio vaizdui, tiek stiliaus vaizdui. Tai būtų nustatoma pagal dvi nuostolių funkcijas:
   - **Turinio nuostolis** apskaičiuojamas remiantis funkcijomis, išgautomis CNN tam tikruose sluoksniuose iš dabartinio vaizdo ir turinio vaizdo.
   - **Stiliaus nuostolis** apskaičiuojamas tarp dabartinio vaizdo ir stiliaus vaizdo sumaniai naudojant Gramo matricas (daugiau informacijos rasite [pavyzdinėje užrašų knygelėje](StyleTransfer.ipynb)).
* Kad vaizdas būtų lygesnis ir pašalintų triukšmą, taip pat įvedame **variacijos nuostolį**, kuris apskaičiuoja vidutinį atstumą tarp kaimyninių pikselių.
* Pagrindinis optimizavimo ciklas koreguoja dabartinį vaizdą, naudodamas gradientinį nusileidimą (ar kitą optimizavimo algoritmą), kad sumažintų bendrą nuostolį, kuris yra visų trijų nuostolių svertinė suma.

## ✍️ Pavyzdys: [Stiliaus perkėlimas](StyleTransfer.ipynb)

## [Klausimynas po paskaitos](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Išvada

Šioje pamokoje sužinojote apie GAN ir kaip juos mokyti. Taip pat sužinojote apie specifinius iššūkius, su kuriais gali susidurti šio tipo neuroniniai tinklai, ir keletą strategijų, kaip juos įveikti.

## 🚀 Iššūkis

Išbandykite [Stiliaus perkėlimo užrašų knygelę](StyleTransfer.ipynb), naudodami savo vaizdus.

## Peržiūra ir savarankiškas mokymasis

Daugiau informacijos apie GAN galite rasti šiuose šaltiniuose:

* Marco Pasini, [10 pamokų, kurias išmokau mokydamas GAN vienerius metus](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), *de facto* GAN architektūra, kurią verta apsvarstyti.
* [Generatyvinio meno kūrimas naudojant GAN Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Užduotis

Peržiūrėkite vieną iš dviejų užrašų knygelių, susijusių su šia pamoka, ir iš naujo apmokykite GAN naudodami savo vaizdus. Ką galite sukurti?

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.