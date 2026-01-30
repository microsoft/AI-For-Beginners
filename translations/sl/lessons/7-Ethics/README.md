# Etična in odgovorna umetna inteligenca

Skoraj ste zaključili ta tečaj in upam, da zdaj jasno vidite, da je umetna inteligenca (UI) osnovana na številnih formalnih matematičnih metodah, ki nam omogočajo iskanje povezav v podatkih in učenje modelov za posnemanje določenih vidikov človeškega vedenja. V tem trenutku zgodovine umetno inteligenco obravnavamo kot zelo močno orodje za pridobivanje vzorcev iz podatkov in uporabo teh vzorcev za reševanje novih težav.

## [Predavanje kviz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Vendar pa v znanstveni fantastiki pogosto vidimo zgodbe, kjer UI predstavlja nevarnost za človeštvo. Običajno so te zgodbe osredotočene na nekakšen upor UI, ko UI odloči, da se bo soočila s človeškimi bitji. To nakazuje, da ima UI nekakšna čustva ali lahko sprejema odločitve, ki jih njeni razvijalci niso predvideli.

Vrsta UI, o kateri smo se učili v tem tečaju, ni nič drugega kot obsežna matrična aritmetika. To je zelo močno orodje, ki nam pomaga reševati naše težave, in kot vsako drugo močno orodje - lahko se uporablja za dobre ali slabe namene. Pomembno je, da se lahko tudi *zlorabi*.

## Načela odgovorne umetne inteligence

Da bi se izognili nenamerni ali namerni zlorabi UI, Microsoft navaja pomembna [načela odgovorne umetne inteligence](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Naslednji koncepti so temelj teh načel:

* **Pravičnost** je povezana s pomembnim problemom *pristranskosti modelov*, ki lahko nastane zaradi uporabe pristranskih podatkov za učenje. Na primer, ko poskušamo napovedati verjetnost, da bo oseba dobila službo razvijalca programske opreme, bo model verjetno dal prednost moškim - zgolj zato, ker je bil učni nabor verjetno pristranski v korist moške populacije. Potrebno je skrbno uravnotežiti učne podatke in raziskati model, da se izognemo pristranskostim ter zagotovimo, da model upošteva bolj relevantne značilnosti.
* **Zanesljivost in varnost**. Po svoji naravi lahko modeli UI delajo napake. Nevronska mreža vrača verjetnosti, kar moramo upoštevati pri sprejemanju odločitev. Vsak model ima določeno natančnost in priklic, kar moramo razumeti, da preprečimo škodo, ki jo lahko povzročijo napačni nasveti.
* **Zasebnost in varnost** imata nekatere specifične implikacije za UI. Na primer, ko uporabljamo določene podatke za učenje modela, ti podatki postanejo nekako "integrirani" v model. Po eni strani to povečuje varnost in zasebnost, po drugi strani pa moramo vedeti, kateri podatki so bili uporabljeni za učenje modela.
* **Vključenost** pomeni, da UI ne gradimo zato, da bi nadomestila ljudi, temveč da bi jih dopolnila in naredila naše delo bolj ustvarjalno. To je povezano tudi s pravičnostjo, saj so pri obravnavi premalo zastopanih skupnosti podatkovni nabori, ki jih zbiramo, pogosto pristranski, zato moramo zagotoviti, da so te skupnosti vključene in pravilno obravnavane z UI.
* **Transparentnost**. To vključuje zagotavljanje, da smo vedno jasni glede uporabe UI. Kjer je mogoče, želimo uporabljati sisteme UI, ki so *razložljivi*.
* **Odgovornost**. Ko modeli UI sprejemajo določene odločitve, ni vedno jasno, kdo je odgovoren za te odločitve. Moramo zagotoviti, da razumemo, kje leži odgovornost za odločitve UI. V večini primerov želimo vključiti ljudi v proces sprejemanja pomembnih odločitev, da so dejanske osebe odgovorne.

## Orodja za odgovorno umetno inteligenco

Microsoft je razvil [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox), ki vsebuje nabor orodij:

* Nadzorna plošča za razložljivost (InterpretML)
* Nadzorna plošča za pravičnost (FairLearn)
* Nadzorna plošča za analizo napak
* Nadzorna plošča za odgovorno UI, ki vključuje:

   - EconML - orodje za vzročno analizo, ki se osredotoča na vprašanja "kaj če"
   - DiCE - orodje za analizo kontrafaktov, ki omogoča vpogled v to, katere značilnosti je treba spremeniti, da bi vplivali na odločitev modela

Za več informacij o etiki UI obiščite [to lekcijo](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) v učnem načrtu strojnega učenja, ki vključuje naloge.

## Pregled in samostojno učenje

Opravite [učni modul](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste), da se naučite več o odgovorni umetni inteligenci.

## [Kviz po predavanju](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.