# Genetische Algoritmen

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetische Algoritmen** (GA) zijn gebaseerd op een **evolutionaire benadering** van AI, waarbij methoden van populatie-evolutie worden gebruikt om een optimale oplossing voor een bepaald probleem te vinden. Ze werden in 1975 voorgesteld door [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetische Algoritmen zijn gebaseerd op de volgende ideeën:

* Geldige oplossingen voor het probleem kunnen worden weergegeven als **genen**
* **Crossover** stelt ons in staat om twee oplossingen te combineren tot een nieuwe geldige oplossing
* **Selectie** wordt gebruikt om meer optimale oplossingen te kiezen met behulp van een **fitnessfunctie**
* **Mutaties** worden geïntroduceerd om de optimalisatie te verstoren en ons uit een lokaal minimum te halen

Als je een Genetisch Algoritme wilt implementeren, heb je het volgende nodig:

 * Een methode om de oplossingen van ons probleem te coderen met behulp van **genen** g&in;&Gamma;
 * Op de verzameling genen &Gamma; moeten we een **fitnessfunctie** definiëren fit: &Gamma;&rightarrow;**R**. Lagere functiewaarden komen overeen met betere oplossingen.
 * Een **crossover**-mechanisme definiëren om twee genen te combineren tot een nieuwe geldige oplossing crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Een **mutatie**-mechanisme definiëren mutate: &Gamma;&rightarrow;&Gamma;.

In veel gevallen zijn crossover en mutatie vrij eenvoudige algoritmen om genen te manipuleren als numerieke reeksen of bitvectoren.

De specifieke implementatie van een genetisch algoritme kan per geval verschillen, maar de algemene structuur is als volgt:

1. Selecteer een initiële populatie G&subset;&Gamma;
2. Selecteer willekeurig een van de operaties die in deze stap zullen worden uitgevoerd: crossover of mutatie
3. **Crossover**:
  * Selecteer willekeurig twee genen g<sub>1</sub>, g<sub>2</sub> &in; G
  * Bereken crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Als fit(g)<fit(g<sub>1</sub>) of fit(g)<fit(g<sub>2</sub>) - vervang het overeenkomstige gen in de populatie door g.
4. **Mutatie** - selecteer een willekeurig gen g&in;G en vervang het door mutate(g)
5. Herhaal vanaf stap 2, totdat we een voldoende kleine waarde van fit hebben bereikt, of totdat de limiet op het aantal stappen is bereikt.

## Typische Taken

Taken die typisch worden opgelost door Genetische Algoritmen zijn onder andere:

1. Optimalisatie van planningen
1. Optimale verpakkingen
1. Optimale snijpatronen
1. Versnellen van uitputtende zoekmethoden

## ✍️ Oefeningen: Genetische Algoritmen

Ga verder met leren in de volgende notebooks:

Ga naar [dit notebook](Genetic.ipynb) om twee voorbeelden te zien van het gebruik van Genetische Algoritmen:

1. Eerlijke verdeling van schatten
1. 8-Damesprobleem

## Conclusie

Genetische Algoritmen worden gebruikt om veel problemen op te lossen, waaronder logistieke en zoekproblemen. Het vakgebied is geïnspireerd door onderzoek dat onderwerpen in de psychologie en informatica combineerde.

## 🚀 Uitdaging

"Genetische algoritmen zijn eenvoudig te implementeren, maar hun gedrag is moeilijk te begrijpen." [bron](https://wikipedia.org/wiki/Genetic_algorithm) Doe wat onderzoek om een implementatie van een genetisch algoritme te vinden, zoals het oplossen van een Sudoku-puzzel, en leg uit hoe het werkt in de vorm van een schets of stroomdiagram.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Herziening & Zelfstudie

Bekijk [deze geweldige video](https://www.youtube.com/watch?v=qv6UVOQ0F44) waarin wordt uitgelegd hoe een computer kan leren Super Mario te spelen met behulp van neurale netwerken die zijn getraind door genetische algoritmen. We zullen meer leren over hoe computers leren om dit soort spellen te spelen [in de volgende sectie](../22-DeepRL/README.md).

## [Opdracht: Diofantische Vergelijking](Diophantine.ipynb)

Je doel is om de zogenaamde **Diofantische vergelijking** op te lossen - een vergelijking met gehele wortels. Overweeg bijvoorbeeld de vergelijking a+2b+3c+4d=30. Je moet de gehele wortels vinden die aan deze vergelijking voldoen.

*Deze opdracht is geïnspireerd door [dit artikel](https://habr.com/post/128704/).*

Hints:

1. Je kunt wortels beschouwen in het interval [0;30]
1. Gebruik als gen de lijst van wortelwaarden

Gebruik [Diophantine.ipynb](Diophantine.ipynb) als startpunt.

---

