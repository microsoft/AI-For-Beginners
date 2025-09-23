<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-25T22:35:34+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "hr"
}
-->
# Segmentacija

Ranije smo učili o Detekciji objekata, koja nam omogućuje lociranje objekata na slici predviđanjem njihovih *bounding boxova*. Međutim, za neke zadatke ne trebamo samo bounding boxove, već i precizniju lokalizaciju objekata. Taj zadatak zove se **segmentacija**.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/23)

Segmentacija se može promatrati kao **klasifikacija piksela**, gdje za **svaki** piksel slike moramo predvidjeti njegovu klasu (*pozadina* je jedna od klasa). Postoje dva glavna algoritma za segmentaciju:

* **Semantička segmentacija** samo određuje klasu piksela, bez razlikovanja između različitih objekata iste klase.
* **Segmentacija instanci** dijeli klase na različite instance.

Kod segmentacije instanci, ove ovce su različiti objekti, dok kod semantičke segmentacije sve ovce pripadaju jednoj klasi.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Slika iz [ovog blog posta](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Postoje različite neuronske arhitekture za segmentaciju, ali sve imaju istu strukturu. Na neki način, slične su autoenkoderu o kojem ste ranije učili, ali umjesto rekonstrukcije originalne slike, naš cilj je rekonstrukcija **maske**. Dakle, mreža za segmentaciju ima sljedeće dijelove:

* **Encoder** izvlači značajke iz ulazne slike.
* **Decoder** transformira te značajke u **masku slike**, iste veličine i s brojem kanala koji odgovara broju klasa.

<img src="images/segm.png" width="80%">

> Slika iz [ove publikacije](https://arxiv.org/pdf/2001.05566.pdf)

Posebno treba spomenuti funkciju gubitka koja se koristi za segmentaciju. Kod klasičnih autoenkodera, potrebno je izmjeriti sličnost između dvije slike, za što se može koristiti srednja kvadratna pogreška (MSE). Kod segmentacije, svaki piksel u ciljnoj maski slike predstavlja broj klase (jednoznačno kodiran duž treće dimenzije), pa je potrebno koristiti funkcije gubitka specifične za klasifikaciju - gubitak unakrsne entropije, prosječan za sve piksele. Ako je maska binarna, koristi se **gubitak binarne unakrsne entropije** (BCE).

> ✅ Jednoznačno kodiranje je način kodiranja oznake klase u vektor duljine jednake broju klasa. Pogledajte [ovaj članak](https://datagy.io/sklearn-one-hot-encode/) o ovoj tehnici.

## Segmentacija u medicinskom snimanju

U ovoj lekciji vidjet ćemo segmentaciju u praksi treniranjem mreže za prepoznavanje ljudskih nevusa (poznatih i kao madeži) na medicinskim slikama. Koristit ćemo <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> bazu podataka</a> dermoskopskih slika kao izvor slika. Ovaj skup podataka sadrži 200 slika tri klase: tipični nevus, atipični nevus i melanom. Sve slike također sadrže odgovarajuću **masku** koja ocrtava nevus.

> ✅ Ova tehnika je posebno prikladna za ovu vrstu medicinskog snimanja, ali koje druge stvarne primjene možete zamisliti?

<img alt="navi" src="images/navi.png"/>

> Slika iz PH<sup>2</sup> baze podataka

Trenirat ćemo model za segmentaciju bilo kojeg nevusa od njegove pozadine.

## ✍️ Vježbe: Semantička segmentacija

Otvorite dolje navedene bilježnice kako biste saznali više o različitim arhitekturama za semantičku segmentaciju, vježbali rad s njima i vidjeli ih u praksi.

* [Semantic Segmentation Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Semantic Segmentation TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Zaključak

Segmentacija je vrlo moćna tehnika za klasifikaciju slika, koja ide dalje od bounding boxova do klasifikacije na razini piksela. To je tehnika koja se koristi u medicinskom snimanju, među ostalim primjenama.

## 🚀 Izazov

Segmentacija tijela samo je jedan od uobičajenih zadataka koje možemo raditi sa slikama ljudi. Drugi važni zadaci uključuju **detekciju kostura** i **detekciju poza**. Isprobajte [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) biblioteku kako biste vidjeli kako se detekcija poza može koristiti.

## Pregled i samostalno učenje

Ovaj [Wikipedia članak](https://wikipedia.org/wiki/Image_segmentation) nudi dobar pregled različitih primjena ove tehnike. Saznajte više o poddomenama segmentacije instanci i panoptičke segmentacije u ovom području istraživanja.

## [Zadatak](lab/README.md)

U ovom laboratorijskom zadatku pokušajte **segmentaciju ljudskog tijela** koristeći [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) s Kagglea.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.