# Etička i odgovorna umjetna inteligencija

Skoro ste završili ovaj tečaj i nadam se da sada jasno vidite da se umjetna inteligencija temelji na nizu formalnih matematičkih metoda koje nam omogućuju pronalaženje odnosa u podacima i treniranje modela za repliciranje nekih aspekata ljudskog ponašanja. U ovom trenutku povijesti smatramo umjetnu inteligenciju vrlo moćnim alatom za izdvajanje uzoraka iz podataka i primjenu tih uzoraka za rješavanje novih problema.

## [Kviz prije predavanja](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Međutim, u znanstvenoj fantastici često vidimo priče u kojima umjetna inteligencija predstavlja opasnost za čovječanstvo. Obično su te priče usredotočene na neku vrstu pobune umjetne inteligencije, kada AI odluči suprotstaviti se ljudima. To implicira da AI ima neku vrstu emocija ili može donositi odluke koje njezini programeri nisu predvidjeli.

Vrsta umjetne inteligencije o kojoj smo učili u ovom tečaju nije ništa drugo nego velika matriksna aritmetika. To je vrlo moćan alat koji nam pomaže u rješavanju problema, i kao svaki drugi moćan alat - može se koristiti u dobre i loše svrhe. Važno je napomenuti da se može i *zloupotrijebiti*.

## Načela odgovorne umjetne inteligencije

Kako bismo izbjegli slučajnu ili namjernu zloupotrebu umjetne inteligencije, Microsoft ističe važna [Načela odgovorne umjetne inteligencije](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Sljedeći koncepti čine temelj tih načela:

* **Pravednost** je povezana s važnim problemom *pristranosti modela*, koja može nastati korištenjem pristranih podataka za treniranje. Na primjer, kada pokušavamo predvidjeti vjerojatnost zapošljavanja osobe kao softverskog inženjera, model će vjerojatno dati prednost muškarcima - samo zato što je skup podataka za treniranje vjerojatno bio pristran prema muškoj populaciji. Moramo pažljivo uravnotežiti podatke za treniranje i istražiti model kako bismo izbjegli pristranosti te osigurali da model uzima u obzir relevantnije značajke.
* **Pouzdanost i sigurnost**. Po svojoj prirodi, AI modeli mogu griješiti. Neuronska mreža vraća vjerojatnosti, i to moramo uzeti u obzir pri donošenju odluka. Svaki model ima određenu preciznost i odziv, i to moramo razumjeti kako bismo spriječili štetu koju pogrešni savjeti mogu uzrokovati.
* **Privatnost i sigurnost** imaju specifične implikacije za umjetnu inteligenciju. Na primjer, kada koristimo neke podatke za treniranje modela, ti podaci na neki način postaju "integrirani" u model. S jedne strane, to povećava sigurnost i privatnost, a s druge strane - moramo se sjetiti na kojim je podacima model treniran.
* **Uključivost** znači da ne gradimo umjetnu inteligenciju kako bismo zamijenili ljude, već kako bismo ih nadopunili i učinili naš rad kreativnijim. To je također povezano s pravednošću, jer kada se bavimo nedovoljno zastupljenim zajednicama, većina podataka koje prikupljamo vjerojatno će biti pristrana, i moramo osigurati da su te zajednice uključene i ispravno obrađene od strane umjetne inteligencije.
* **Transparentnost**. Ovo uključuje osiguravanje da uvijek jasno komuniciramo kada se koristi umjetna inteligencija. Također, gdje god je to moguće, želimo koristiti AI sustave koji su *interpretabilni*.
* **Odgovornost**. Kada AI modeli donose neke odluke, nije uvijek jasno tko je odgovoran za te odluke. Moramo osigurati da razumijemo gdje leži odgovornost za odluke umjetne inteligencije. U većini slučajeva želimo uključiti ljude u proces donošenja važnih odluka, kako bi stvarne osobe bile odgovorne.

## Alati za odgovornu umjetnu inteligenciju

Microsoft je razvio [Alatni okvir za odgovornu umjetnu inteligenciju](https://github.com/microsoft/responsible-ai-toolbox) koji sadrži niz alata:

* Nadzorna ploča za interpretabilnost (InterpretML)
* Nadzorna ploča za pravednost (FairLearn)
* Nadzorna ploča za analizu pogrešaka
* Nadzorna ploča za odgovornu umjetnu inteligenciju koja uključuje:

   - EconML - alat za uzročnu analizu, koji se fokusira na pitanja "što ako"
   - DiCE - alat za kontrafaktualnu analizu koji vam omogućuje da vidite koje značajke treba promijeniti kako bi se utjecalo na odluku modela

Za više informacija o etici umjetne inteligencije, posjetite [ovu lekciju](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) u kurikulumu strojnog učenja koja uključuje zadatke.

## Pregled i samostalno učenje

Prođite kroz ovaj [Put učenja](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) kako biste saznali više o odgovornoj umjetnoj inteligenciji.

## [Kviz nakon predavanja](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.