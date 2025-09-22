<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bedc8e702db17260cfe824d58b6cfd4",
  "translation_date": "2025-08-25T20:55:55+00:00",
  "source_file": "lessons/4-ComputerVision/06-IntroCV/README.md",
  "language_code": "sw"
}
-->
# Utangulizi wa Maono ya Kompyuta

[Maono ya Kompyuta](https://wikipedia.org/wiki/Computer_vision) ni taaluma inayolenga kuwezesha kompyuta kuelewa kwa kiwango cha juu picha za kidijitali. Hii ni tafsiri pana, kwa sababu *kuelewa* kunaweza kumaanisha mambo mengi, ikiwa ni pamoja na kutambua kitu kwenye picha (**utambuzi wa kitu**), kuelewa kinachoendelea (**utambuzi wa tukio**), kuelezea picha kwa maandishi, au kujenga upya eneo kwa 3D. Pia kuna kazi maalum zinazohusiana na picha za binadamu: makadirio ya umri na hisia, utambuzi wa uso na utambulisho, na makadirio ya mkao wa 3D, kutaja chache.

## [Jaribio la kabla ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/11)

Moja ya kazi rahisi zaidi za maono ya kompyuta ni **uainishaji wa picha**.

Maono ya kompyuta mara nyingi huchukuliwa kuwa tawi la AI. Siku hizi, kazi nyingi za maono ya kompyuta zinatatuliwa kwa kutumia mitandao ya neva. Tutajifunza zaidi kuhusu aina maalum ya mitandao ya neva inayotumika kwa maono ya kompyuta, [mitandao ya neva ya convolutional](../07-ConvNets/README.md), katika sehemu hii.

Hata hivyo, kabla ya kupitisha picha kwenye mtandao wa neva, mara nyingi inafaa kutumia mbinu za kialgorithmu kuboresha picha.

Kuna maktaba kadhaa za Python zinazopatikana kwa usindikaji wa picha:

* **[imageio](https://imageio.readthedocs.io/en/stable/)** inaweza kutumika kusoma/kuandika miundo tofauti ya picha. Pia inaunga mkono ffmpeg, zana muhimu ya kubadilisha fremu za video kuwa picha.
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (pia inajulikana kama PIL) ni yenye nguvu zaidi, na pia inaunga mkono baadhi ya urekebishaji wa picha kama vile kubadilisha maumbo, kurekebisha rangi, na zaidi.
* **[OpenCV](https://opencv.org/)** ni maktaba yenye nguvu ya usindikaji wa picha iliyoandikwa kwa C++, ambayo imekuwa kiwango cha *de facto* kwa usindikaji wa picha. Ina kiolesura cha Python kinachofaa.
* **[dlib](http://dlib.net/)** ni maktaba ya C++ inayotekeleza algorithimu nyingi za ujifunzaji wa mashine, ikiwa ni pamoja na baadhi ya algorithimu za Maono ya Kompyuta. Pia ina kiolesura cha Python, na inaweza kutumika kwa kazi ngumu kama vile utambuzi wa uso na alama za uso.

## OpenCV

[OpenCV](https://opencv.org/) inachukuliwa kuwa kiwango cha *de facto* kwa usindikaji wa picha. Ina algorithimu nyingi muhimu, zilizotekelezwa kwa C++. Unaweza pia kuita OpenCV kutoka Python.

Mahali pazuri pa kujifunza OpenCV ni [kozi hii ya Jifunze OpenCV](https://learnopencv.com/getting-started-with-opencv/). Katika mtaala wetu, lengo letu si kujifunza OpenCV, bali kukuonyesha baadhi ya mifano ya wakati inaweza kutumika, na jinsi.

### Kupakia Picha

Picha katika Python zinaweza kuwakilishwa kwa urahisi na safu za NumPy. Kwa mfano, picha za kijivu zenye ukubwa wa pikseli 320x200 zingewekwa kwenye safu ya 200x320, na picha za rangi za vipimo hivyo hivyo zingekuwa na umbo la 200x320x3 (kwa njia 3 za rangi). Ili kupakia picha, unaweza kutumia msimbo ufuatao:

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

Kiasili, OpenCV hutumia usimbaji wa BGR (Blue-Green-Red) kwa picha za rangi, wakati zana zingine za Python hutumia RGB (Red-Green-Blue) ya jadi zaidi. Ili picha ionekane sawa, unahitaji kuibadilisha kuwa nafasi ya rangi ya RGB, ama kwa kubadilisha vipimo kwenye safu ya NumPy, au kwa kuita kazi ya OpenCV:

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

Kazi hiyo hiyo ya `cvtColor` inaweza kutumika kufanya mabadiliko mengine ya nafasi ya rangi kama vile kubadilisha picha kuwa kijivu au nafasi ya rangi ya HSV (Hue-Saturation-Value).

Unaweza pia kutumia OpenCV kupakia fremu za video moja baada ya nyingine - mfano umetolewa kwenye zoezi [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb).

### Usindikaji wa Picha

Kabla ya kulisha picha kwenye mtandao wa neva, unaweza kutaka kutumia hatua kadhaa za usindikaji wa awali. OpenCV inaweza kufanya mambo mengi, ikiwa ni pamoja na:

* **Kubadilisha ukubwa** wa picha kwa kutumia `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **Kufifisha** picha kwa kutumia `im = cv2.medianBlur(im,3)` au `im = cv2.GaussianBlur(im, (3,3), 0)`
* Kubadilisha **mwanga na utofauti** wa picha kunaweza kufanywa kwa kutumia manipulations za safu za NumPy, kama ilivyoelezwa [katika maelezo haya ya Stackoverflow](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* Kutumia [thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) kwa kuita kazi za `cv2.threshold`/`cv2.adaptiveThreshold`, ambayo mara nyingi inapendelewa kuliko kurekebisha mwanga au utofauti.
* Kutumia [mabadiliko tofauti](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html) kwenye picha:
    - **[Mabadiliko ya Affine](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** yanaweza kuwa muhimu ikiwa unahitaji kuchanganya mzunguko, kubadilisha ukubwa na kupinda picha na unajua eneo la chanzo na marudio la pointi tatu kwenye picha. Mabadiliko ya Affine huhifadhi mistari sambamba.
    - **[Mabadiliko ya Mtazamo](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** yanaweza kuwa muhimu unapojua nafasi za chanzo na marudio za pointi 4 kwenye picha. Kwa mfano, ukipiga picha ya hati ya mstatili kupitia kamera ya simu kutoka pembe fulani, na unataka kufanya picha ya mstatili ya hati yenyewe.
* Kuelewa harakati ndani ya picha kwa kutumia **[mtiririko wa macho](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)**.

## Mifano ya Kutumia Maono ya Kompyuta

Katika [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb), tunatoa mifano ya wakati maono ya kompyuta yanaweza kutumika kutekeleza kazi maalum:

* **Usindikaji wa awali wa picha ya kitabu cha Braille**. Tunazingatia jinsi tunavyoweza kutumia thresholding, utambuzi wa vipengele, mabadiliko ya mtazamo na manipulations za NumPy kutenganisha alama za Braille kwa uainishaji zaidi na mtandao wa neva.

![Picha ya Braille](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.sw.jpeg) | ![Picha ya Braille Iliyosindikwa](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.sw.png) | ![Alama za Braille](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.sw.png)
----|-----|-----

> Picha kutoka [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Kutambua harakati kwenye video kwa kutumia tofauti ya fremu**. Ikiwa kamera imetulia, basi fremu kutoka kwenye mlisho wa kamera zinapaswa kufanana sana. Kwa kuwa fremu zinawakilishwa kama safu, kwa kutoa tofauti ya safu hizo kwa fremu mbili mfululizo tutapata tofauti ya pikseli, ambayo inapaswa kuwa ndogo kwa fremu tuli, na kuwa kubwa zaidi mara kuna harakati kubwa kwenye picha.

![Picha ya fremu za video na tofauti za fremu](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.sw.png)

> Picha kutoka [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **Kutambua harakati kwa kutumia Mtiririko wa Macho**. [Mtiririko wa macho](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) hutuwezesha kuelewa jinsi pikseli za kibinafsi kwenye fremu za video zinavyohama. Kuna aina mbili za mtiririko wa macho:

   - **Mtiririko wa Macho wa Wingi** huhesabu uwanja wa vekta unaoonyesha kwa kila pikseli inakoelekea.
   - **Mtiririko wa Macho wa Sehemu** unategemea kuchukua vipengele vya kipekee kwenye picha (mfano, kingo), na kujenga mwelekeo wake kutoka fremu hadi fremu.

![Picha ya Mtiririko wa Macho](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.sw.png)

> Picha kutoka [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## ✍️ Notibuku za Mfano: OpenCV [jaribu OpenCV kwa Vitendo](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

Tufanye majaribio na OpenCV kwa kuchunguza [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## Hitimisho

Wakati mwingine, kazi ngumu kama vile utambuzi wa harakati au utambuzi wa ncha za vidole zinaweza kutatuliwa kwa kutumia maono ya kompyuta pekee. Kwa hivyo, ni muhimu sana kujua mbinu za msingi za maono ya kompyuta, na kile maktaba kama OpenCV zinaweza kufanya.

## 🚀 Changamoto

Tazama [video hii](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste) kutoka kipindi cha AI ili kujifunza kuhusu mradi wa Cortic Tigers na jinsi walivyojenga suluhisho la msingi wa vizuizi ili kurahisisha kazi za maono ya kompyuta kupitia roboti. Fanya utafiti juu ya miradi mingine kama hii inayosaidia wanafunzi wapya kuingia kwenye uwanja huu.

## [Jaribio la baada ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/12)

## Mapitio na Kujisomea

Soma zaidi kuhusu mtiririko wa macho [katika mafunzo haya mazuri](https://learnopencv.com/optical-flow-in-opencv/).

## [Kazi ya Nyumbani](lab/README.md)

Katika maabara hii, utachukua video yenye ishara rahisi, na lengo lako ni kutoa harakati za juu/chini/kushoto/kulia kwa kutumia mtiririko wa macho.

<img src="images/palm-movement.png" width="30%" alt="Fremu ya Harakati ya Kiganja"/>

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.