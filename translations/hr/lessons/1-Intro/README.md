<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-25T22:22:43+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "hr"
}
-->
> Slika autora [Dmitry Soshnikov](http://soshnikov.com)

S vremenom su računalni resursi postali jeftiniji, a dostupno je i više podataka, pa su pristupi temeljenim na neuronskim mrežama počeli pokazivati izvrsne rezultate u natjecanju s ljudima u mnogim područjima, poput računalnog vida ili razumijevanja govora. U posljednjem desetljeću, pojam Umjetna Inteligencija uglavnom se koristi kao sinonim za neuronske mreže, jer većina uspjeha AI-a o kojima čujemo temelji se na njima.

Možemo promatrati kako su se pristupi mijenjali, primjerice, u stvaranju računalnog programa za igranje šaha:

* Rani šahovski programi temeljili su se na pretraživanju – program je eksplicitno pokušavao procijeniti moguće poteze protivnika za određeni broj sljedećih poteza i odabrao optimalan potez na temelju najbolje pozicije koja se može postići u nekoliko poteza. To je dovelo do razvoja tzv. [alpha-beta rezanja](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) algoritma pretraživanja.
* Strategije pretraživanja dobro funkcioniraju prema kraju igre, gdje je prostor pretraživanja ograničen malim brojem mogućih poteza. Međutim, na početku igre prostor pretraživanja je ogroman, a algoritam se može poboljšati učenjem iz postojećih partija između ljudskih igrača. Kasniji eksperimenti koristili su tzv. [razmišljanje temeljeno na slučajevima](https://en.wikipedia.org/wiki/Case-based_reasoning), gdje je program tražio slučajeve u bazi znanja vrlo slične trenutnoj poziciji u igri.
* Moderni programi koji pobjeđuju ljudske igrače temelje se na neuronskim mrežama i [pojačanom učenju](https://en.wikipedia.org/wiki/Reinforcement_learning), gdje programi uče igrati isključivo igrajući dugo vremena sami protiv sebe i učeći iz vlastitih pogrešaka – slično kao što ljudi uče igrati šah. Međutim, računalni program može odigrati mnogo više partija u puno kraćem vremenu i tako učiti mnogo brže.

✅ Istražite malo o drugim igrama koje su igrali AI sustavi.

Slično tome, možemo vidjeti kako se pristup stvaranju "programa za razgovor" (koji bi mogli proći Turingov test) mijenjao:

* Rani programi ove vrste, poput [Elize](https://en.wikipedia.org/wiki/ELIZA), temeljili su se na vrlo jednostavnim gramatičkim pravilima i preformulaciji ulazne rečenice u pitanje.
* Moderni asistenti, poput Cortane, Siri ili Google Assistanta, hibridni su sustavi koji koriste neuronske mreže za pretvaranje govora u tekst i prepoznavanje naše namjere, a zatim primjenjuju neko zaključivanje ili eksplicitne algoritme za izvršavanje potrebnih radnji.
* U budućnosti možemo očekivati potpuno neuronski model koji će samostalno upravljati dijalogom. Nedavne GPT i [Turing-NLG](https://turing.microsoft.com/) obitelji neuronskih mreža pokazuju veliki uspjeh u tome.

> Slika Dmitry Soshnikov, [fotografija](https://unsplash.com/photos/r8LmVbUKgns) od [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Nedavna istraživanja o umjetnoj inteligenciji

Ogroman rast istraživanja neuronskih mreža započeo je oko 2010. godine, kada su postali dostupni veliki javni skupovi podataka. Velika zbirka slika nazvana [ImageNet](https://en.wikipedia.org/wiki/ImageNet), koja sadrži oko 14 milijuna anotiranih slika, dala je povod za [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![ILSVRC Točnost](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Slika od [Dmitry Soshnikov](http://soshnikov.com)

Godine 2012., [Konvolucijske neuronske mreže](../4-ComputerVision/07-ConvNets/README.md) prvi su put korištene u klasifikaciji slika, što je dovelo do značajnog smanjenja pogrešaka u klasifikaciji (s gotovo 30% na 16,4%). Godine 2015., ResNet arhitektura iz Microsoft Research [postigla je točnost na razini ljudske sposobnosti](https://doi.org/10.1109/ICCV.2015.123).

Od tada, neuronske mreže pokazale su vrlo uspješno ponašanje u mnogim zadacima:

---

Godina | Postignuta ljudska razina
-----|--------
2015 | [Klasifikacija slika](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Prepoznavanje govora u razgovoru](https://arxiv.org/abs/1610.05256)
2018 | [Automatski strojni prijevod](https://arxiv.org/abs/1803.05567) (kineski na engleski)
2020 | [Opisivanje slika](https://arxiv.org/abs/2009.13682)

Tijekom posljednjih nekoliko godina svjedočili smo velikim uspjesima s velikim jezičnim modelima, poput BERT-a i GPT-3. To se dogodilo uglavnom zbog činjenice da postoji mnogo općih tekstualnih podataka koji omogućuju treniranje modela za hvatanje strukture i značenja tekstova, njihovo pred-treniranje na općim zbirkama tekstova, a zatim specijalizaciju tih modela za specifičnije zadatke. Više ćemo naučiti o [Obradi prirodnog jezika](../5-NLP/README.md) kasnije u ovom tečaju.

## 🚀 Izazov

Provedite istraživanje na internetu kako biste utvrdili gdje se, prema vašem mišljenju, umjetna inteligencija najefikasnije koristi. Je li to u aplikaciji za mapiranje, nekoj usluzi za pretvaranje govora u tekst ili videoigri? Istražite kako je sustav izgrađen.

## [Kviz nakon predavanja](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Pregled i samostalno učenje

Pregledajte povijest umjetne inteligencije i strojnog učenja čitajući [ovu lekciju](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Uzmite jedan element iz sketchnote-a na vrhu te lekcije ili ove i istražite ga detaljnije kako biste razumjeli kulturni kontekst koji je utjecao na njegov razvoj.

**Zadatak**: [Game Jam](assignment.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.