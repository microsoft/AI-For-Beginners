<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-26T00:00:41+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "sk"
}
-->
# Klasifikácia viacerých tried pomocou perceptrónu

Laboratórna úloha z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úloha

Pomocou kódu, ktorý sme vyvinuli v tejto lekcii na binárnu klasifikáciu ručne písaných číslic MNIST, vytvorte klasifikátor viacerých tried, ktorý bude schopný rozpoznať akékoľvek číslo. Vypočítajte presnosť klasifikácie na tréningovej a testovacej množine a zobrazte maticu zámien.

## Tipy

1. Pre každú číslicu vytvorte dataset pre binárny klasifikátor „táto číslica vs. všetky ostatné číslice“.
1. Natrénujte 10 rôznych perceptrónov na binárnu klasifikáciu (jeden pre každú číslicu).
1. Definujte funkciu, ktorá bude klasifikovať vstupnú číslicu.

> **Tip**: Ak skombinujeme váhy všetkých 10 perceptrónov do jednej matice, mali by sme byť schopní aplikovať všetkých 10 perceptrónov na vstupné číslice jedným násobením matíc. Najpravdepodobnejšiu číslicu potom môžeme nájsť jednoduchým použitím operácie `argmax` na výstupe.

## Začiatočný notebook

Začnite úlohu otvorením [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb).

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.