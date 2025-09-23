<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-25T22:17:34+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "cs"
}
-->
> Obrázek od [Dmitry Soshnikov](http://soshnikov.com)

S postupem času se výpočetní zdroje staly levnějšími a dostupnost dat se zvýšila, což umožnilo přístupům založeným na neuronových sítích dosahovat skvělých výsledků v konkurenci s lidskými schopnostmi v mnoha oblastech, jako je počítačové vidění nebo porozumění řeči. V posledním desetiletí se termín Umělá inteligence často používá jako synonymum pro neuronové sítě, protože většina úspěchů AI, o kterých slyšíme, je založena právě na nich.

Můžeme pozorovat, jak se přístupy měnily, například při tvorbě počítačového programu hrajícího šachy:

* Rané šachové programy byly založeny na vyhledávání – program se explicitně snažil odhadnout možné tahy soupeře pro daný počet následujících tahů a vybral optimální tah na základě nejlepší pozice, kterou lze dosáhnout během několika tahů. To vedlo k vývoji tzv. [alpha-beta ořezávacího](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) vyhledávacího algoritmu.
* Strategie vyhledávání fungují dobře ke konci hry, kdy je vyhledávací prostor omezen malým počtem možných tahů. Na začátku hry je však vyhledávací prostor obrovský a algoritmus lze zlepšit učením z existujících zápasů mezi lidskými hráči. Následné experimenty využívaly tzv. [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), kde program hledal případy v databázi znalostí, které jsou velmi podobné aktuální pozici ve hře.
* Moderní programy, které porážejí lidské hráče, jsou založeny na neuronových sítích a [posilovaném učení](https://en.wikipedia.org/wiki/Reinforcement_learning), kde se programy učí hrát výhradně tím, že dlouho hrají samy proti sobě a učí se ze svých vlastních chyb – podobně jako lidé, když se učí hrát šachy. Počítačový program však může odehrát mnohem více her za mnohem kratší dobu, a tím se učí mnohem rychleji.

✅ Udělejte si malý průzkum o dalších hrách, které byly hrány AI.

Podobně můžeme vidět, jak se přístup k vytváření „mluvících programů“ (které by mohly projít Turingovým testem) změnil:

* Rané programy tohoto typu, jako například [Eliza](https://en.wikipedia.org/wiki/ELIZA), byly založeny na velmi jednoduchých gramatických pravidlech a přeformulování vstupní věty do otázky.
* Moderní asistenti, jako Cortana, Siri nebo Google Assistant, jsou hybridní systémy, které využívají neuronové sítě k převodu řeči na text a rozpoznání našeho záměru, a poté používají určité formy logického uvažování nebo explicitní algoritmy k provedení požadovaných akcí.
* V budoucnu můžeme očekávat kompletní model založený na neuronových sítích, který bude schopen samostatně zvládnout dialog. Nedávné rodiny neuronových sítí GPT a [Turing-NLG](https://turing.microsoft.com/) ukazují v této oblasti velký úspěch.

> Obrázek od Dmitry Soshnikov, [fotografie](https://unsplash.com/photos/r8LmVbUKgns) od [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Nedávný výzkum v oblasti AI

Obrovský nárůst výzkumu neuronových sítí začal kolem roku 2010, kdy se začaly objevovat velké veřejné datové sady. Obrovská sbírka obrázků nazvaná [ImageNet](https://en.wikipedia.org/wiki/ImageNet), která obsahuje přibližně 14 milionů anotovaných obrázků, dala vzniknout [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![Přesnost ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Obrázek od [Dmitry Soshnikov](http://soshnikov.com)

V roce 2012 byly [Konvoluční neuronové sítě](../4-ComputerVision/07-ConvNets/README.md) poprvé použity pro klasifikaci obrázků, což vedlo k výraznému snížení chybovosti klasifikace (z téměř 30 % na 16,4 %). V roce 2015 architektura ResNet od Microsoft Research [dosáhla úrovně přesnosti srovnatelné s člověkem](https://doi.org/10.1109/ICCV.2015.123).

Od té doby neuronové sítě prokázaly velmi úspěšné chování v mnoha úlohách:

---

Rok | Dosažení úrovně srovnatelné s člověkem
-----|--------
2015 | [Klasifikace obrázků](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Rozpoznávání konverzační řeči](https://arxiv.org/abs/1610.05256)
2018 | [Automatický strojový překlad](https://arxiv.org/abs/1803.05567) (z čínštiny do angličtiny)
2020 | [Popisování obrázků](https://arxiv.org/abs/2009.13682)

V posledních několika letech jsme byli svědky obrovských úspěchů s velkými jazykovými modely, jako jsou BERT a GPT-3. To se stalo především díky tomu, že je k dispozici velké množství obecných textových dat, která nám umožňují trénovat modely tak, aby zachytily strukturu a význam textů, předtrénovat je na obecných textových kolekcích a poté tyto modely specializovat na konkrétnější úkoly. O [zpracování přirozeného jazyka](../5-NLP/README.md) se dozvíme více později v tomto kurzu.

## 🚀 Výzva

Prozkoumejte internet a určete, kde je podle vás AI nejefektivněji využívána. Je to v mapovací aplikaci, nějaké službě převodu řeči na text nebo ve videohře? Zjistěte, jak byl tento systém vytvořen.

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Přehled a samostudium

Projděte si historii AI a ML přečtením [této lekce](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Vyberte si prvek ze sketchnotu na začátku této lekce nebo této a prozkoumejte jej podrobněji, abyste pochopili kulturní kontext, který ovlivnil jeho vývoj.

**Úkol**: [Game Jam](assignment.md)

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.