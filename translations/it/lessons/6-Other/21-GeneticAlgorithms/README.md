<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-26T07:05:16+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "it"
}
-->
# Algoritmi Genetici

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/41)

Gli **Algoritmi Genetici** (GA) si basano su un **approccio evolutivo** all'IA, in cui vengono utilizzati metodi di evoluzione di una popolazione per ottenere una soluzione ottimale a un determinato problema. Furono proposti nel 1975 da [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Gli Algoritmi Genetici si basano sulle seguenti idee:

* Le soluzioni valide al problema possono essere rappresentate come **geni**
* Il **crossover** ci permette di combinare due soluzioni per ottenere una nuova soluzione valida
* La **selezione** viene utilizzata per scegliere soluzioni più ottimali usando una **funzione di fitness**
* Vengono introdotte **mutazioni** per destabilizzare l'ottimizzazione e uscire da un minimo locale

Per implementare un Algoritmo Genetico, è necessario:

 * Trovare un metodo per codificare le soluzioni del problema usando i **geni** g∈Γ
 * Sul set di geni Γ, è necessario definire una **funzione di fitness** fit: Γ→**R**. Valori più piccoli della funzione corrispondono a soluzioni migliori.
 * Definire un meccanismo di **crossover** per combinare due geni e ottenere una nuova soluzione valida crossover: Γ<sup>2</sub>→Γ.
 * Definire un meccanismo di **mutazione** mutate: Γ→Γ.

In molti casi, il crossover e la mutazione sono algoritmi piuttosto semplici per manipolare i geni come sequenze numeriche o vettori di bit.

L'implementazione specifica di un algoritmo genetico può variare da caso a caso, ma la struttura generale è la seguente:

1. Selezionare una popolazione iniziale G⊂Γ
2. Selezionare casualmente una delle operazioni da eseguire in questo passaggio: crossover o mutazione
3. **Crossover**:
  * Selezionare casualmente due geni g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Calcolare il crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Se fit(g)<fit(g<sub>1</sub>) o fit(g)<fit(g<sub>2</sub>) - sostituire il gene corrispondente nella popolazione con g.
4. **Mutazione** - selezionare un gene casuale g∈G e sostituirlo con mutate(g)
5. Ripetere dal passaggio 2, fino a ottenere un valore sufficientemente piccolo di fit, o fino a raggiungere il limite sul numero di passaggi.

## Compiti Tipici

I compiti tipicamente risolti dagli Algoritmi Genetici includono:

1. Ottimizzazione dei programmi
1. Imballaggio ottimale
1. Taglio ottimale
1. Accelerazione della ricerca esaustiva

## ✍️ Esercizi: Algoritmi Genetici

Continua il tuo apprendimento nei seguenti notebook:

Vai a [questo notebook](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) per vedere due esempi di utilizzo degli Algoritmi Genetici:

1. Divisione equa di un tesoro
1. Problema delle 8 Regine

## Conclusione

Gli Algoritmi Genetici vengono utilizzati per risolvere molti problemi, inclusi problemi di logistica e ricerca. Il campo è ispirato da ricerche che hanno unito argomenti di Psicologia e Informatica.

## 🚀 Sfida

"Gli algoritmi genetici sono semplici da implementare, ma il loro comportamento è difficile da comprendere." [fonte](https://wikipedia.org/wiki/Genetic_algorithm) Fai una ricerca per trovare un'implementazione di un algoritmo genetico, come la risoluzione di un puzzle di Sudoku, e spiega come funziona attraverso uno schema o un diagramma di flusso.

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Revisione e Studio Autonomo

Guarda [questo fantastico video](https://www.youtube.com/watch?v=qv6UVOQ0F44) che parla di come un computer possa imparare a giocare a Super Mario utilizzando reti neurali addestrate con algoritmi genetici. Impareremo di più su come i computer imparano a giocare a giochi simili [nella prossima sezione](../22-DeepRL/README.md).

## [Compito: Equazione Diofantea](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Il tuo obiettivo è risolvere la cosiddetta **equazione diofantea** - un'equazione con radici intere. Ad esempio, considera l'equazione a+2b+3c+4d=30. Devi trovare le radici intere che soddisfano questa equazione.

*Questo compito è ispirato da [questo post](https://habr.com/post/128704/).*

Suggerimenti:

1. Puoi considerare le radici nell'intervallo [0;30]
1. Come gene, considera di utilizzare l'elenco dei valori delle radici

Usa [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) come punto di partenza.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.