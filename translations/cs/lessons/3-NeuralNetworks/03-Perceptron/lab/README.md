# Více-třídní klasifikace s perceptronem

Laboratorní úkol z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úkol

Pomocí kódu, který jsme vyvinuli v této lekci pro binární klasifikaci ručně psaných číslic MNIST, vytvořte více-třídní klasifikátor, který bude schopen rozpoznat jakékoli číslo. Vypočítejte přesnost klasifikace na trénovacím a testovacím datasetu a zobrazte matici záměn.

## Tipy

1. Pro každé číslo vytvořte dataset pro binární klasifikátor „toto číslo vs. všechna ostatní čísla“
1. Natrénujte 10 různých perceptronů pro binární klasifikaci (jeden pro každé číslo)
1. Definujte funkci, která bude klasifikovat vstupní číslo

> **Tip**: Pokud zkombinujeme váhy všech 10 perceptronů do jedné matice, měli bychom být schopni aplikovat všech 10 perceptronů na vstupní čísla jedním maticovým násobením. Nejpravděpodobnější číslo pak můžeme najít jednoduše použitím operace `argmax` na výstupu.

## Výchozí notebook

Začněte laboratorní úkol otevřením [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.