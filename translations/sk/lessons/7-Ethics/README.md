# Etická a zodpovedná AI

Tento kurz máte takmer dokončený a dúfam, že teraz už jasne vidíte, že AI je založená na množstve formálnych matematických metód, ktoré nám umožňujú nachádzať vzťahy v dátach a trénovať modely na replikáciu niektorých aspektov ľudského správania. V tomto bode histórie považujeme AI za veľmi mocný nástroj na extrakciu vzorcov z dát a ich aplikáciu na riešenie nových problémov.

## [Kvíz pred prednáškou](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Avšak v sci-fi často vidíme príbehy, kde AI predstavuje hrozbu pre ľudstvo. Zvyčajne sú tieto príbehy zamerané na nejaký druh vzbury AI, keď sa AI rozhodne postaviť proti ľuďom. To naznačuje, že AI má nejaké emócie alebo dokáže robiť rozhodnutia, ktoré jej vývojári nepredvídali.

Druh AI, o ktorom sme sa učili v tomto kurze, nie je nič iné ako veľká matica aritmetiky. Je to veľmi mocný nástroj, ktorý nám pomáha riešiť naše problémy, a ako každý iný mocný nástroj - môže byť použitý na dobré aj zlé účely. Dôležité je, že môže byť *zneužitý*.

## Princípy zodpovednej AI

Aby sme sa vyhli náhodnému alebo úmyselnému zneužitiu AI, Microsoft stanovuje dôležité [Princípy zodpovednej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Tieto princípy sú založené na nasledujúcich konceptoch:

* **Spravodlivosť** súvisí s dôležitým problémom *predsudkov modelu*, ktoré môžu vzniknúť použitím zaujatých dát na trénovanie. Napríklad, keď sa snažíme predpovedať pravdepodobnosť získania práce softvérového vývojára pre konkrétnu osobu, model pravdepodobne uprednostní mužov - jednoducho preto, že trénovacia dátová sada bola pravdepodobne zaujatá voči mužskému publiku. Musíme starostlivo vyvážiť trénovacie dáta a skúmať model, aby sme sa vyhli predsudkom a zabezpečili, že model zohľadňuje relevantnejšie vlastnosti.
* **Spoľahlivosť a bezpečnosť**. Zo svojej podstaty môžu AI modely robiť chyby. Neurónová sieť vracia pravdepodobnosti, a to musíme brať do úvahy pri rozhodovaní. Každý model má určitú presnosť a citlivosť, a musíme to pochopiť, aby sme predišli škodám, ktoré môžu spôsobiť nesprávne rady.
* **Súkromie a bezpečnosť** majú niektoré špecifické implikácie pre AI. Napríklad, keď používame nejaké dáta na trénovanie modelu, tieto dáta sa určitým spôsobom "integrujú" do modelu. Na jednej strane to zvyšuje bezpečnosť a súkromie, na druhej strane si musíme pamätať, na akých dátach bol model trénovaný.
* **Inkluzívnosť** znamená, že AI nestaviame na to, aby nahradila ľudí, ale aby ich doplnila a urobila našu prácu kreatívnejšou. Súvisí to aj so spravodlivosťou, pretože pri práci s nedostatočne zastúpenými komunitami sú väčšina dát, ktoré zbierame, pravdepodobne zaujaté, a musíme zabezpečiť, že tieto komunity sú zahrnuté a správne spracované AI.
* **Transparentnosť**. To zahŕňa zabezpečenie, že vždy jasne uvádzame, že používame AI. Tiež, kdekoľvek je to možné, chceme používať AI systémy, ktoré sú *interpretovateľné*.
* **Zodpovednosť**. Keď AI modely prichádzajú s nejakými rozhodnutiami, nie je vždy jasné, kto je za tieto rozhodnutia zodpovedný. Musíme zabezpečiť, že rozumieme, kde leží zodpovednosť za rozhodnutia AI. Vo väčšine prípadov by sme chceli zahrnúť ľudí do procesu prijímania dôležitých rozhodnutí, aby boli za ne zodpovední skutoční ľudia.

## Nástroje pre zodpovednú AI

Microsoft vyvinul [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox), ktorý obsahuje sadu nástrojov:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard, ktorý zahŕňa:

   - EconML - nástroj na kauzálnu analýzu, ktorý sa zameriava na otázky "čo ak"
   - DiCE - nástroj na kontrafaktuálnu analýzu, ktorý vám umožňuje vidieť, ktoré vlastnosti je potrebné zmeniť, aby sa ovplyvnilo rozhodnutie modelu

Pre viac informácií o etike AI navštívte [túto lekciu](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) v učebných osnovách strojového učenia, ktorá zahŕňa aj úlohy.

## Prehľad a samostatné štúdium

Absolvujte tento [učebný plán](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste), aby ste sa dozvedeli viac o zodpovednej AI.

## [Kvíz po prednáške](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.