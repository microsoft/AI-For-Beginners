<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-25T22:19:27+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "ro"
}
-->
> Imagine de [Dmitry Soshnikov](http://soshnikov.com)

Pe măsură ce timpul a trecut, resursele de calcul au devenit mai ieftine, iar mai multe date au devenit disponibile, astfel încât abordările bazate pe rețele neuronale au început să demonstreze performanțe remarcabile, concurând cu ființele umane în multe domenii, cum ar fi viziunea computerizată sau înțelegerea vorbirii. În ultimul deceniu, termenul Inteligență Artificială a fost folosit în mare parte ca sinonim pentru Rețele Neuronale, deoarece majoritatea succeselor AI despre care auzim se bazează pe acestea.

Putem observa cum s-au schimbat abordările, de exemplu, în crearea unui program de calculator pentru jocul de șah:

* Programele de șah timpurii se bazau pe căutare – un program încerca explicit să estimeze mișcările posibile ale adversarului pentru un număr dat de mișcări viitoare și selecta o mișcare optimă pe baza poziției optime care putea fi atinsă în câteva mișcări. Acest lucru a dus la dezvoltarea algoritmului de căutare numit [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Strategiile de căutare funcționează bine spre sfârșitul jocului, unde spațiul de căutare este limitat de un număr mic de mișcări posibile. Totuși, la începutul jocului, spațiul de căutare este uriaș, iar algoritmul poate fi îmbunătățit prin învățarea din meciurile existente între jucători umani. Experimentele ulterioare au utilizat așa-numita [raționare bazată pe cazuri](https://en.wikipedia.org/wiki/Case-based_reasoning), unde programul căuta cazuri în baza de cunoștințe foarte similare cu poziția actuală din joc.
* Programele moderne care câștigă împotriva jucătorilor umani se bazează pe rețele neuronale și [învățare prin întărire](https://en.wikipedia.org/wiki/Reinforcement_learning), unde programele învață să joace exclusiv jucând mult timp împotriva lor însele și învățând din propriile greșeli – exact cum fac ființele umane atunci când învață să joace șah. Totuși, un program de calculator poate juca mult mai multe jocuri într-un timp mult mai scurt și, astfel, poate învăța mult mai rapid.

✅ Cercetează puțin despre alte jocuri care au fost jucate de AI.

În mod similar, putem vedea cum s-a schimbat abordarea în crearea programelor „vorbitoare” (care ar putea trece testul Turing):

* Programele timpurii de acest tip, cum ar fi [Eliza](https://en.wikipedia.org/wiki/ELIZA), se bazau pe reguli gramaticale foarte simple și reformularea propoziției de intrare într-o întrebare.
* Asistenții moderni, cum ar fi Cortana, Siri sau Google Assistant, sunt sisteme hibride care folosesc rețele neuronale pentru a converti vorbirea în text și a recunoaște intenția noastră, apoi utilizează raționamente sau algoritmi expliciți pentru a efectua acțiunile necesare.
* În viitor, ne putem aștepta la un model complet bazat pe rețele neuronale care să gestioneze dialogul de unul singur. Familia recentă de rețele neuronale GPT și [Turing-NLG](https://turing.microsoft.com/) demonstrează un mare succes în acest sens.

> Imagine realizată de Dmitry Soshnikov, [fotografie](https://unsplash.com/photos/r8LmVbUKgns) de [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Cercetări recente în domeniul AI

Creșterea semnificativă a cercetărilor în rețele neuronale a început în jurul anului 2010, când seturi mari de date publice au devenit disponibile. O colecție vastă de imagini numită [ImageNet](https://en.wikipedia.org/wiki/ImageNet), care conține aproximativ 14 milioane de imagini adnotate, a dat naștere competiției [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![Acuratețea ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Imagine realizată de [Dmitry Soshnikov](http://soshnikov.com)

În 2012, [Rețelele Neuronale Convoluționale](../4-ComputerVision/07-ConvNets/README.md) au fost utilizate pentru prima dată în clasificarea imaginilor, ceea ce a dus la o scădere semnificativă a erorilor de clasificare (de la aproape 30% la 16,4%). În 2015, arhitectura ResNet de la Microsoft Research [a atins un nivel de acuratețe similar cu cel uman](https://doi.org/10.1109/ICCV.2015.123).

De atunci, rețelele neuronale au demonstrat un comportament extrem de eficient în multe sarcini:

---

Anul | Paritate cu nivelul uman atins
-----|------------------------------
2015 | [Clasificarea imaginilor](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Recunoașterea vorbirii conversaționale](https://arxiv.org/abs/1610.05256)
2018 | [Traducerea automată a textelor](https://arxiv.org/abs/1803.05567) (chineză-engleză)
2020 | [Generarea de descrieri pentru imagini](https://arxiv.org/abs/2009.13682)

În ultimii ani, am fost martorii unor succese uriașe cu modelele mari de limbaj, precum BERT și GPT-3. Acest lucru s-a întâmplat în principal datorită faptului că există o cantitate mare de date textuale generale disponibile, care permit antrenarea modelelor pentru a înțelege structura și semnificația textelor, pre-antrenarea lor pe colecții generale de texte și apoi specializarea acestor modele pentru sarcini mai specifice. Vom învăța mai multe despre [Procesarea Limbajului Natural](../5-NLP/README.md) mai târziu în acest curs.

## 🚀 Provocare

Fă un tur al internetului pentru a determina unde consideri că AI este utilizată cel mai eficient. Este într-o aplicație de hărți, un serviciu de conversie vorbire-text sau un joc video? Cercetează cum a fost construit sistemul.

## [Chestionar post-lectură](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Recapitulare și studiu individual

Revizuiește istoria AI și ML citind [această lecție](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Alege un element din schița de la începutul acelei lecții sau din aceasta și cercetează-l mai în detaliu pentru a înțelege contextul cultural care a influențat evoluția sa.

**Temă**: [Game Jam](assignment.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.