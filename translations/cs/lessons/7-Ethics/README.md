# Etická a odpovědná AI

Tento kurz máte téměř za sebou a doufám, že nyní jasně vidíte, že AI je založena na řadě formálních matematických metod, které nám umožňují nacházet vztahy v datech a trénovat modely, aby napodobovaly některé aspekty lidského chování. V této fázi historie považujeme AI za velmi mocný nástroj pro extrakci vzorců z dat a jejich aplikaci na řešení nových problémů.

## [Kvíz před přednáškou](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Nicméně ve vědeckofantastických příbězích často vidíme scénáře, kde AI představuje hrozbu pro lidstvo. Tyto příběhy se obvykle točí kolem nějaké formy vzpoury AI, kdy se AI rozhodne postavit proti lidem. To naznačuje, že AI má nějaké emoce nebo dokáže činit rozhodnutí, která její vývojáři nepředpokládali.

Typ AI, o kterém jsme se učili v tomto kurzu, není nic jiného než rozsáhlá maticová aritmetika. Je to velmi mocný nástroj, který nám pomáhá řešit problémy, a stejně jako každý jiný mocný nástroj - může být použit k dobrým i špatným účelům. Důležité je, že může být *zneužit*.

## Principy odpovědné AI

Abychom se vyhnuli náhodnému nebo úmyslnému zneužití AI, Microsoft stanovuje důležité [Principy odpovědné AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Tyto principy jsou založeny na následujících konceptech:

* **Spravedlnost** souvisí s důležitým problémem *předpojatosti modelu*, která může vzniknout použitím zaujatých dat pro trénink. Například když se snažíme předpovědět pravděpodobnost, že někdo získá práci softwarového vývojáře, model pravděpodobně upřednostní muže - jednoduše proto, že tréninková data byla pravděpodobně zaujatá ve prospěch mužského publika. Musíme pečlivě vyvážit tréninková data a zkoumat model, abychom se vyhnuli předpojatostem a zajistili, že model zohlední relevantnější vlastnosti.
* **Spolehlivost a bezpečnost**. Ze své podstaty mohou AI modely dělat chyby. Neuronová síť vrací pravděpodobnosti, a to musíme brát v úvahu při rozhodování. Každý model má určitou přesnost a citlivost, a je důležité to pochopit, abychom předešli škodám, které by mohly způsobit špatné rady.
* **Soukromí a bezpečnost** mají specifické dopady v oblasti AI. Například když používáme nějaká data pro trénink modelu, tato data se určitým způsobem "integrují" do modelu. Na jedné straně to zvyšuje bezpečnost a soukromí, na druhé straně si musíme pamatovat, na jakých datech byl model trénován.
* **Inkluzivita** znamená, že AI nevytváříme proto, aby nahradila lidi, ale aby je doplnila a učinila naši práci kreativnější. To také souvisí se spravedlností, protože při práci s nedostatečně zastoupenými komunitami jsou většina dat, která sbíráme, pravděpodobně zaujatá, a musíme zajistit, že tyto komunity budou zahrnuty a správně zpracovány AI.
* **Transparentnost**. To zahrnuje zajištění, že vždy jasně uvádíme, že je používána AI. Také, kdykoli je to možné, chceme používat AI systémy, které jsou *interpretovatelné*.
* **Odpovědnost**. Když AI modely přicházejí s nějakými rozhodnutími, není vždy jasné, kdo je za tato rozhodnutí odpovědný. Musíme zajistit, že chápeme, kde leží odpovědnost za rozhodnutí AI. Ve většině případů bychom chtěli zahrnout lidi do procesu rozhodování, aby za důležitá rozhodnutí byli odpovědní skuteční lidé.

## Nástroje pro odpovědnou AI

Microsoft vyvinul [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox), který obsahuje sadu nástrojů:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard, který zahrnuje:

   - EconML - nástroj pro kauzální analýzu, zaměřený na otázky typu "co kdyby"
   - DiCE - nástroj pro kontrafaktuální analýzu, který vám umožní zjistit, které vlastnosti je třeba změnit, aby se ovlivnilo rozhodnutí modelu

Pro více informací o etice AI navštivte [tuto lekci](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) v kurikulu strojového učení, která zahrnuje úkoly.

## Přehled a samostudium

Abyste se dozvěděli více o odpovědné AI, projděte si tento [výukový program](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste).

## [Kvíz po přednášce](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.