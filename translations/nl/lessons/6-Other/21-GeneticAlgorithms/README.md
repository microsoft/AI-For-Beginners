<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-28T19:14:32+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "nl"
}
-->
# Genetische Algoritmen

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Genetische algoritmen** (GA) zijn gebaseerd op een **evolutionaire benadering** van AI, waarbij methoden van de evolutie van een populatie worden gebruikt om een optimale oplossing voor een gegeven probleem te vinden. Ze werden voorgesteld in 1975 door [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetische algoritmen zijn gebaseerd op de volgende ideeën:

* Geldige oplossingen voor het probleem kunnen worden weergegeven als **genen**
* **Crossover** stelt ons in staat om twee oplossingen te combineren om een nieuwe geldige oplossing te verkrijgen
* **Selectie** wordt gebruikt om meer optimale oplossingen te kiezen met behulp van een **fitnessfunctie**
* **Mutaties** worden geïntroduceerd om optimalisatie te destabiliseren en ons uit een lokaal minimum te halen

Als je een genetisch algoritme wilt implementeren, heb je het volgende nodig:

 * Een methode om de oplossingen van ons probleem te coderen met behulp van **genen** g∈Γ
 * Op de set van genen Γ moet je een **fitnessfunctie** definiëren fit: Γ→**R**. Kleinere functiewaarden komen overeen met betere oplossingen.
 * Een **crossover**-mechanisme definiëren om twee genen samen te combineren tot een nieuwe geldige oplossing crossover: Γ<sup>2</sub>→Γ.
 * Een **mutatie**-mechanisme definiëren mutate: Γ→Γ.

In veel gevallen zijn crossover en mutatie vrij eenvoudige algoritmen om genen te manipuleren als numerieke reeksen of bitvectoren.

De specifieke implementatie van een genetisch algoritme kan variëren van geval tot geval, maar de algemene structuur is als volgt:

1. Selecteer een initiële populatie G⊂Γ
2. Selecteer willekeurig een van de operaties die in deze stap zullen worden uitgevoerd: crossover of mutatie
3. **Crossover**:
  * Selecteer willekeurig twee genen g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Bereken crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Als fit(g)<fit(g<sub>1</sub>) of fit(g)<fit(g<sub>2</sub>) - vervang het overeenkomstige gen in de populatie door g.
4. **Mutatie** - selecteer een willekeurig gen g∈G en vervang het door mutate(g)
5. Herhaal vanaf stap 2, totdat we een voldoende kleine waarde van fit hebben bereikt, of totdat de limiet op het aantal stappen is bereikt.

## Typische Taken

Taken die typisch worden opgelost door genetische algoritmen zijn onder andere:

1. Optimalisatie van planningen
1. Optimaal inpakken
1. Optimaal snijden
1. Versnellen van uitputtend zoeken

## ✍️ Oefeningen: Genetische Algoritmen

Ga verder met leren in de volgende notebooks:

Ga naar [deze notebook](Genetic.ipynb) om twee voorbeelden te zien van het gebruik van genetische algoritmen:

1. Eerlijke verdeling van schatten
1. 8-damesprobleem

## Conclusie

Genetische algoritmen worden gebruikt om veel problemen op te lossen, waaronder logistieke en zoekproblemen. Het vakgebied is geïnspireerd door onderzoek dat onderwerpen uit de psychologie en informatica combineerde.

## 🚀 Uitdaging

"Genetische algoritmen zijn eenvoudig te implementeren, maar hun gedrag is moeilijk te begrijpen." [bron](https://wikipedia.org/wiki/Genetic_algorithm) Doe wat onderzoek om een implementatie van een genetisch algoritme te vinden, zoals het oplossen van een Sudoku-puzzel, en leg uit hoe het werkt in de vorm van een schets of stroomdiagram.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Review & Zelfstudie

Bekijk [deze geweldige video](https://www.youtube.com/watch?v=qv6UVOQ0F44) waarin wordt uitgelegd hoe een computer kan leren Super Mario te spelen met behulp van neurale netwerken die zijn getraind door genetische algoritmen. We zullen meer leren over hoe computers leren om dergelijke spellen te spelen [in de volgende sectie](../22-DeepRL/README.md).

## [Opdracht: Diophantine Vergelijking](Diophantine.ipynb)

Je doel is om de zogenaamde **Diophantine vergelijking** op te lossen - een vergelijking met gehele wortels. Bijvoorbeeld, beschouw de vergelijking a+2b+3c+4d=30. Je moet de gehele wortels vinden die aan deze vergelijking voldoen.

*Deze opdracht is geïnspireerd door [deze post](https://habr.com/post/128704/).*

Hints:

1. Je kunt wortels beschouwen in het interval [0;30]
1. Gebruik als gen de lijst met wortelwaarden

Gebruik [Diophantine.ipynb](Diophantine.ipynb) als startpunt.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.