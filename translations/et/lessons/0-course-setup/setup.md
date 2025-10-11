<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4c545eb30765a49469ced84cfb4379f",
  "translation_date": "2025-10-11T11:35:36+00:00",
  "source_file": "lessons/0-course-setup/setup.md",
  "language_code": "et"
}
-->
# Alustamine selle õppekavaga

## Kas oled õpilane?

Alusta järgmiste ressurssidega:

* [Õpilaste keskuse leht](https://docs.microsoft.com/learn/student-hub?WT.mc_id=academic-77998-cacaste) Sellelt lehelt leiad algajatele mõeldud ressursid, õpilaste paketid ja isegi võimalusi saada tasuta sertifikaadi vautšer. See on leht, mida tasub järjehoidjatesse lisada ja aeg-ajalt kontrollida, kuna vahetame sisu vähemalt kord kuus.
* [Microsofti õpilaste saadikud](https://studentambassadors.microsoft.com?WT.mc_id=academic-77998-cacaste) Liitu ülemaailmse õpilaste saadikute kogukonnaga – see võib olla sinu tee Microsofti.

**Õpilased**, õppekava kasutamiseks on mitu võimalust. Esiteks võid lihtsalt lugeda teksti ja vaadata koodi otse GitHubis. Kui soovid koodi käivitada mõnes märkmikus, siis [loe meie juhiseid](./etc/how-to-run.md) ja leia rohkem nõuandeid, kuidas seda teha [sellest blogipostitusest](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

> **Note**: [Juhised, kuidas käivitada koodi selles õppekavas](./how-to-run.md)

## Iseseisev õpe

Kui soovid kursust võtta iseseisva õppe projektina, soovitame sul kogu repo oma GitHubi kontole fork'ida ja harjutusi iseseisvalt või grupiga täita:

* Alusta loengu-eelse testiga.
* Loe loengu sissejuhatavat teksti.
* Kui loengul on lisamärkmikud, vaata need läbi, lugedes ja käivitades koodi. Kui on olemas nii TensorFlow kui ka PyTorch märkmikud, võid keskenduda ühele neist – vali oma lemmik raamistik.
* Märkmikud sisaldavad sageli väljakutseid, mis nõuavad koodi veidi kohandamist, et katsetada.
* Tee loengu-järgne test.
* Kui mooduliga on seotud labor, täida ülesanne.
* Külastage [arutelufoorumit](https://github.com/microsoft/AI-For-Beginners/discussions), et "õppida valjult".

> Edasiseks õppeks soovitame järgida neid [Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-77998-cacaste) mooduleid ja õpiradu.

**Õpetajad**, oleme [lisanud mõned soovitused](/for-teachers.md), kuidas seda õppekava kasutada.

---

## Pedagoogika

Selle õppekava koostamisel oleme valinud kaks pedagoogilist põhimõtet: tagada, et see oleks praktiline **projektipõhine** ja sisaldaks **sagedasi teste**.

Tagades, et sisu on seotud projektidega, muutub protsess õpilastele kaasahaaravamaks ja kontseptsioonide omandamine paraneb. Lisaks seab madala panusega test enne tundi õpilase eesmärgi õppida teemat, samas kui teine test pärast tundi tagab edasise omandamise. See õppekava on loodud paindlikuks ja lõbusaks ning seda saab võtta tervikuna või osaliselt. Projektid algavad väikestest ja muutuvad 12-nädalase tsükli lõpuks järjest keerukamaks.

> **Märkus testide kohta**: Kõik testid on saadaval [selles rakenduses](https://red-field-0a6ddfd03.1.azurestaticapps.net/), kokku 50 testi, milles on igaühes kolm küsimust. Need on seotud õppetundidega, kuid testirakendust saab käivitada lokaalselt; järgige juhiseid kaustas `etc/quiz-app`.

## Võrguta juurdepääs

Seda dokumentatsiooni saab kasutada võrguühenduseta, kasutades [Docsify](https://docsify.js.org/#/). Fork'ige see repo, [installige Docsify](https://docsify.js.org/#/quickstart) oma kohalikku masinasse ja seejärel sisestage selle repo juurkaustas `docsify serve`. Veebisait teenindatakse pordil 3000 teie localhost'is: `localhost:3000`. Õppekava PDF on saadaval [sellel lingil](../../../../../../../../../etc/pdf/readme.pdf).

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.