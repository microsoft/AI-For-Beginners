<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-25T22:35:50+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "sl"
}
-->
# Segmentacija

Prej smo se naučili o zaznavanju objektov, ki nam omogoča lociranje objektov na sliki z napovedovanjem njihovih *omejevalnih okvirjev*. Vendar pa za nekatere naloge ne potrebujemo le omejevalnih okvirjev, temveč tudi bolj natančno lokalizacijo objektov. Ta naloga se imenuje **segmentacija**.

## [Pre-učni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/23)

Segmentacijo lahko obravnavamo kot **klasifikacijo pikslov**, kjer moramo za **vsak** piksel slike napovedati njegov razred (*ozadje* je eden od razredov). Obstajata dva glavna algoritma za segmentacijo:

* **Semantična segmentacija** določa le razred pikslov in ne razlikuje med različnimi objekti istega razreda.
* **Segmentacija primerkov** razdeli razrede na različne primerke.

Pri segmentaciji primerkov so te ovce različni objekti, medtem ko pri semantični segmentaciji vse ovce predstavljajo en razred.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Slika iz [tega blog prispevka](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Obstajajo različne nevronske arhitekture za segmentacijo, vendar imajo vse enako strukturo. Na nek način je podobno avtoenkoderju, o katerem ste se že učili, vendar namesto razgradnje izvirne slike naš cilj postane razgradnja **maske**. Tako ima segmentacijsko omrežje naslednje dele:

* **Kodirnik** izlušči značilnosti iz vhodne slike.
* **Dekodirnik** pretvori te značilnosti v **sliko maske**, ki ima enako velikost in število kanalov, ki ustreza številu razredov.

<img src="images/segm.png" width="80%">

> Slika iz [te publikacije](https://arxiv.org/pdf/2001.05566.pdf)

Posebej je treba omeniti funkcijo izgube, ki se uporablja za segmentacijo. Pri uporabi klasičnih avtoenkoderjev moramo izmeriti podobnost med dvema slikama, za kar lahko uporabimo povprečno kvadratno napako (MSE). Pri segmentaciji vsak piksel v ciljni sliki maske predstavlja številko razreda (ena-vroče kodirano vzdolž tretje dimenzije), zato moramo uporabiti funkcije izgube, specifične za klasifikacijo - funkcijo izgube križne entropije, povprečeno čez vse piksle. Če je maska binarna, se uporablja **funkcija izgube binarne križne entropije** (BCE).

> ✅ Ena-vroče kodiranje je način kodiranja oznake razreda v vektor dolžine, ki ustreza številu razredov. Oglejte si [ta članek](https://datagy.io/sklearn-one-hot-encode/) o tej tehniki.

## Segmentacija v medicinskem slikanju

V tej lekciji bomo videli segmentacijo v praksi, tako da bomo trenirali omrežje za prepoznavanje človeških nevusov (znanih tudi kot znamenja) na medicinskih slikah. Uporabili bomo <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> podatkovno zbirko</a> dermoskopskih slik kot vir slik. Ta podatkovna zbirka vsebuje 200 slik treh razredov: tipični nevus, atipični nevus in melanom. Vse slike vsebujejo tudi ustrezno **masko**, ki označuje nevus.

> ✅ Ta tehnika je še posebej primerna za tovrstno medicinsko slikanje, vendar katere druge aplikacije iz resničnega sveta si lahko zamislite?

<img alt="navi" src="images/navi.png"/>

> Slika iz PH<sup>2</sup> podatkovne zbirke

Trenirali bomo model za segmentacijo nevusa iz ozadja.

## ✍️ Vaje: Semantična segmentacija

Odprite spodnje zvezke, da se naučite več o različnih arhitekturah semantične segmentacije, vadite delo z njimi in jih vidite v praksi.

* [Semantična segmentacija Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Semantična segmentacija TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Po-učni kviz](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Zaključek

Segmentacija je zelo močna tehnika za klasifikacijo slik, ki presega omejevalne okvirje in omogoča klasifikacijo na ravni pikslov. To je tehnika, ki se uporablja v medicinskem slikanju in drugih aplikacijah.

## 🚀 Izziv

Segmentacija telesa je le ena izmed pogostih nalog, ki jih lahko izvedemo s slikami ljudi. Druge pomembne naloge vključujejo **zaznavanje skeleta** in **zaznavanje drže**. Preizkusite knjižnico [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), da vidite, kako se lahko uporablja zaznavanje drže.

## Pregled in samostojno učenje

Ta [članek na Wikipediji](https://wikipedia.org/wiki/Image_segmentation) ponuja dober pregled različnih aplikacij te tehnike. Naučite se več o poddomenah segmentacije primerkov in panoptične segmentacije na tem področju raziskovanja.

## [Naloga](lab/README.md)

V tem laboratoriju poskusite **segmentacijo človeškega telesa** z uporabo [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) iz Kaggle.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.