<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-26T00:00:32+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "cs"
}
-->
# Více-třídní klasifikace s perceptronem

Laboratorní úloha z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úkol

Pomocí kódu, který jsme vyvinuli v této lekci pro binární klasifikaci ručně psaných číslic MNIST, vytvořte více-třídní klasifikátor, který bude schopen rozpoznat jakékoli číslo. Vypočítejte přesnost klasifikace na trénovacím a testovacím datasetu a zobrazte matici záměn.

## Tipy

1. Pro každou číslici vytvořte dataset pro binární klasifikátor "tato číslice vs. všechny ostatní číslice"
1. Natrénujte 10 různých perceptronů pro binární klasifikaci (jeden pro každou číslici)
1. Definujte funkci, která bude klasifikovat vstupní číslici

> **Tip**: Pokud zkombinujeme váhy všech 10 perceptronů do jedné matice, měli bychom být schopni aplikovat všech 10 perceptronů na vstupní číslice pomocí jedné maticové násobení. Nejpravděpodobnější číslici pak lze najít jednoduše použitím operace `argmax` na výstupu.

## Výchozí notebook

Začněte laboratorní úlohu otevřením [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.