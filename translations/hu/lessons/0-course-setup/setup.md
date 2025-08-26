<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4c545eb30765a49469ced84cfb4379f",
  "translation_date": "2025-08-26T00:40:22+00:00",
  "source_file": "lessons/0-course-setup/setup.md",
  "language_code": "hu"
}
-->
# Az oktatási anyag kezdő lépései

## Diák vagy?

Kezdd az alábbi forrásokkal:

* [Student Hub oldal](https://docs.microsoft.com/learn/student-hub?WT.mc_id=academic-77998-cacaste) Ezen az oldalon kezdő forrásokat, diákcsomagokat és akár ingyenes tanúsítvány-vouchert is találhatsz. Érdemes ezt az oldalt könyvjelzőzni és időnként visszanézni, mivel havonta frissítjük a tartalmat.
* [Microsoft Student Learn nagykövetek](https://studentambassadors.microsoft.com?WT.mc_id=academic-77998-cacaste) Csatlakozz egy globális diák nagyköveti közösséghez, ez lehet a belépőd a Microsoft világába.

**Diákok**, többféleképpen is használhatjátok az oktatási anyagot. Először is, egyszerűen olvashatjátok a szöveget és böngészhetitek a kódot közvetlenül a GitHubon. Ha futtatni szeretnétek a kódot bármelyik notebookban, [olvassátok el az útmutatónkat](./etc/how-to-run.md), és találjatok további tanácsokat [ebben a blogbejegyzésben](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

> **Note**: [Útmutató a kód futtatásához ebben az oktatási anyagban](./how-to-run.md)

## Önálló tanulás

Ha önálló tanulási projektként szeretnéd elvégezni a kurzust, javasoljuk, hogy forkold az egész repót a saját GitHub fiókodba, és végezd el a gyakorlatokat egyedül vagy csoportban:

* Kezdd egy előadás előtti kvízzel.
* Olvasd el az előadás bevezető szövegét.
* Ha az előadáshoz további notebookok tartoznak, nézd át őket, olvasd el és futtasd a kódot. Ha mind TensorFlow, mind PyTorch notebookok elérhetők, választhatsz közülük - döntsd el, melyik keretrendszer a kedvenced.
* A notebookok gyakran tartalmaznak kihívásokat, amelyek során a kódot kicsit módosítanod kell, hogy kísérletezz.
* Töltsd ki az előadás utáni kvízt.
* Ha a modulhoz labor is tartozik, végezd el a feladatot.
* Látogass el a [Vita fórumra](https://github.com/microsoft/AI-For-Beginners/discussions), hogy "hangosan tanulj".

> További tanuláshoz ajánljuk, hogy kövesd ezeket a [Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-77998-cacaste) modulokat és tanulási útvonalakat.

**Tanárok**, [néhány javaslatot is mellékeltünk](/for-teachers.md) az oktatási anyag használatához.

---

## Pedagógia

Két pedagógiai alapelvet választottunk az oktatási anyag összeállításakor: biztosítani, hogy az anyag **projektalapú** és **gyakori kvízeket** tartalmazzon.

Azáltal, hogy a tartalom projektekhez igazodik, a folyamat érdekesebbé válik a diákok számára, és a fogalmak jobban rögzülnek. Emellett egy alacsony tétű kvíz az óra előtt segít a diákoknak a téma iránti érdeklődés felkeltésében, míg egy második kvíz az óra után tovább erősíti a tanultakat. Ez az oktatási anyag rugalmas és szórakoztató, és teljes egészében vagy részleteiben is elvégezhető. A projektek kicsiben kezdődnek, és a 12 hetes ciklus végére egyre összetettebbé válnak.

> **Megjegyzés a kvízekről**: Minden kvíz [ebben az alkalmazásban](https://red-field-0a6ddfd03.1.azurestaticapps.net/) található, összesen 50 darab, három kérdéses kvíz. Az órákból elérhetők, de a kvíz alkalmazás helyben is futtatható; kövesd az `etc/quiz-app` mappában található utasításokat.

## Offline hozzáférés

Az oktatási anyagot offline is futtathatod a [Docsify](https://docsify.js.org/#/) segítségével. Forkold ezt a repót, [telepítsd a Docsify-t](https://docsify.js.org/#/quickstart) a saját gépedre, majd a repó gyökérmappájában írd be, hogy `docsify serve`. A weboldal a localhost 3000-es portján lesz elérhető: `localhost:3000`. Az oktatási anyag pdf formátumban is elérhető [ezen a linken](../../../../../../../../../etc/pdf/readme.pdf).

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.