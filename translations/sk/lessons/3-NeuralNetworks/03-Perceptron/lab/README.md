# Klasifikácia viacerých tried pomocou perceptronu

Laboratórna úloha z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úloha

Pomocou kódu, ktorý sme vyvinuli v tejto lekcii na binárnu klasifikáciu ručne písaných číslic MNIST, vytvorte klasifikátor viacerých tried, ktorý bude schopný rozpoznať akékoľvek číslo. Vypočítajte presnosť klasifikácie na tréningovej a testovacej množine a zobrazte maticu zámien.

## Tipy

1. Pre každé číslo vytvorte dataset pre binárny klasifikátor „toto číslo vs. všetky ostatné čísla“
1. Natrénujte 10 rôznych perceptronov na binárnu klasifikáciu (jeden pre každé číslo)
1. Definujte funkciu, ktorá bude klasifikovať vstupné číslo

> **Tip**: Ak skombinujeme váhy všetkých 10 perceptronov do jednej matice, mali by sme byť schopní aplikovať všetkých 10 perceptronov na vstupné čísla jedným násobením matíc. Najpravdepodobnejšie číslo potom môžeme nájsť jednoducho použitím operácie `argmax` na výstupe.

## Východiskový notebook

Začnite laboratórium otvorením [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.