<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-28T15:33:46+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "da"
}
-->
> Billede af [Dmitry Soshnikov](http://soshnikov.com)

Med tiden er computerressourcer blevet billigere, og der er kommet mere data til rådighed, hvilket har gjort, at neurale netværk har vist stor ydeevne i at konkurrere med mennesker på mange områder, såsom computer vision og talegenkendelse. I det seneste årti er begrebet kunstig intelligens ofte blevet brugt som synonym for neurale netværk, da de fleste af de AI-succeser, vi hører om, er baseret på dem.

Vi kan observere, hvordan tilgangen har ændret sig, for eksempel i udviklingen af et skakspillende computerprogram:

* Tidlige skakprogrammer var baseret på søgning – et program forsøgte eksplicit at estimere mulige træk fra en modstander for et givet antal fremtidige træk og valgte det optimale træk baseret på den bedste position, der kunne opnås inden for få træk. Dette førte til udviklingen af den såkaldte [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) søgealgoritme.
* Søgestrategier fungerer godt mod slutningen af spillet, hvor søgeområdet er begrænset af et lille antal mulige træk. Men i begyndelsen af spillet er søgeområdet enormt, og algoritmen kan forbedres ved at lære fra eksisterende kampe mellem menneskelige spillere. Efterfølgende eksperimenter anvendte den såkaldte [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), hvor programmet søgte efter tilfælde i vidensbasen, der minder meget om den aktuelle position i spillet.
* Moderne programmer, der vinder over menneskelige spillere, er baseret på neurale netværk og [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning), hvor programmerne lærer at spille udelukkende ved at spille mod sig selv i lang tid og lære af deres egne fejl – meget ligesom mennesker gør, når de lærer at spille skak. Dog kan et computerprogram spille mange flere spil på meget kortere tid og dermed lære langt hurtigere.

✅ Undersøg andre spil, som AI har spillet.

På samme måde kan vi se, hvordan tilgangen til at skabe "talende programmer" (der måske kan bestå Turing-testen) har ændret sig:

* Tidlige programmer af denne type, såsom [Eliza](https://en.wikipedia.org/wiki/ELIZA), var baseret på meget simple grammatiske regler og omformulering af input-sætningen til et spørgsmål.
* Moderne assistenter som Cortana, Siri eller Google Assistant er alle hybride systemer, der bruger neurale netværk til at konvertere tale til tekst og genkende vores intentioner, og derefter anvender en form for ræsonnement eller eksplicitte algoritmer til at udføre de ønskede handlinger.
* I fremtiden kan vi forvente en komplet neuralbaseret model, der selv kan håndtere dialog. De seneste GPT- og [Turing-NLG](https://turing.microsoft.com/) familier af neurale netværk viser stor succes på dette område.

> Billede af Dmitry Soshnikov, [foto](https://unsplash.com/photos/r8LmVbUKgns) af [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Nyere AI-forskning

Den enorme vækst i forskning inden for neurale netværk begyndte omkring 2010, da store offentlige datasæt blev tilgængelige. En stor samling af billeder kaldet [ImageNet](https://en.wikipedia.org/wiki/ImageNet), som indeholder omkring 14 millioner annoterede billeder, gav anledning til [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![ILSVRC Nøjagtighed](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Billede af [Dmitry Soshnikov](http://soshnikov.com)

I 2012 blev [Convolutional Neural Networks](../4-ComputerVision/07-ConvNets/README.md) først brugt til billedklassifikation, hvilket førte til et markant fald i klassifikationsfejl (fra næsten 30% til 16,4%). I 2015 opnåede ResNet-arkitekturen fra Microsoft Research [menneskelignende nøjagtighed](https://doi.org/10.1109/ICCV.2015.123).

Siden da har neurale netværk vist sig at være meget succesfulde i mange opgaver:

---

År | Menneskelig paritet opnået
-----|--------
2015 | [Billedklassifikation](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Samtale-baseret talegenkendelse](https://arxiv.org/abs/1610.05256)
2018 | [Automatisk maskinoversættelse](https://arxiv.org/abs/1803.05567) (Kinesisk-til-Engelsk)
2020 | [Billedtekstning](https://arxiv.org/abs/2009.13682)

I løbet af de seneste år har vi været vidne til enorme succeser med store sprogmodeller som BERT og GPT-3. Dette skete primært på grund af, at der findes en stor mængde generel tekstdata, som gør det muligt at træne modeller til at fange strukturen og betydningen af tekster, fortræne dem på generelle tekstsamlinger og derefter specialisere disse modeller til mere specifikke opgaver. Vi vil lære mere om [Natural Language Processing](../5-NLP/README.md) senere i dette kursus.

## 🚀 Udfordring

Tag en tur på internettet for at afgøre, hvor du mener, AI bliver brugt mest effektivt. Er det i en kortlægningsapp, en tale-til-tekst-tjeneste eller et videospil? Undersøg, hvordan systemet blev bygget.

## [Quiz efter forelæsning](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Gennemgang & Selvstudie

Gennemgå AI's og ML's historie ved at læse [denne lektion](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Tag et element fra sketchnoten øverst i den lektion eller denne og undersøg det mere i dybden for at forstå den kulturelle kontekst, der har informeret dets udvikling.

**Opgave**: [Game Jam](assignment.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.