# Multi-klasse klassifikation med Perceptron

Lab-opgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Opgave

Ved hjælp af den kode, vi har udviklet i denne lektion til binær klassifikation af MNIST håndskrevne cifre, skal du oprette en multi-klasse klassifikator, der kan genkende ethvert ciffer. Beregn klassifikationsnøjagtigheden på trænings- og testdatasættet, og udskriv forvirringsmatricen.

## Tips

1. For hvert ciffer skal du oprette et datasæt til binær klassifikation af "dette ciffer vs. alle andre cifre"
1. Træn 10 forskellige perceptroner til binær klassifikation (én for hvert ciffer)
1. Definér en funktion, der kan klassificere et inputciffer

> **Tip**: Hvis vi kombinerer vægtene fra alle 10 perceptroner i én matrix, bør vi kunne anvende alle 10 perceptroner på inputcifrene ved én matrixmultiplikation. Det mest sandsynlige ciffer kan derefter findes ved blot at anvende `argmax`-operationen på outputtet.

## Startnotebook

Start labben ved at åbne [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.