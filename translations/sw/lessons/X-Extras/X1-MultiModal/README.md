# Multi-Modal Nätverk

Efter framgången med transformer-modeller för att lösa NLP-uppgifter har samma eller liknande arkitekturer tillämpats på datorvisionsuppgifter. Det finns ett växande intresse för att bygga modeller som skulle *kombinera* visuella och naturliga språkkapaciteter. Ett av dessa försök gjordes av OpenAI, och det kallas CLIP och DALL.E.

## Kontrastiv Bild För-Träning (CLIP)

Huvudidén med CLIP är att kunna jämföra textpromptar med en bild och avgöra hur väl bilden motsvarar prompten.

![CLIP Arkitektur](../../../../../translated_images/clip-arch.b3dbf20b4e8ed8be1c38e2bc6100fd3cc257c33cda4692b301be91f791b13ea7.sw.png)

> *Bild från [detta blogginlägg](https://openai.com/blog/clip/)*

Modellen tränas på bilder som erhållits från Internet och deras bildtexter. För varje batch tar vi N par av (bild, text), och omvandlar dem till vissa vektorrepresentationer I
Du är tränad på data fram till oktober 2023. . Dessa representationer matchas sedan ihop. Förlustfunktionen definieras för att maximera kosinussimilariteten mellan vektorer som motsvarar ett par (t.ex. I och T), och minimera kosinussimilariteten mellan alla andra par. Det är anledningen till att denna metod kallas **kontrastiv**.

CLIP-modellen/biblioteket är tillgänglig från [OpenAI GitHub](https://github.com/openai/CLIP). Metoden beskrivs i [detta blogginlägg](https://openai.com/blog/clip/), och mer detaljerat i [detta papper](https://arxiv.org/pdf/2103.00020.pdf).

När denna modell är förtränad kan vi ge den en batch av bilder och en batch av textpromptar, och den kommer att returnera en tensor med sannolikheter. CLIP kan användas för flera uppgifter:

**Bildklassificering**

Anta att vi behöver klassificera bilder mellan, säg, katter, hundar och människor. I detta fall kan vi ge modellen en bild och en serie av textpromptar: "*en bild av en katt*", "*en bild av en hund*", "*en bild av en människa*". I den resulterande vektorn av 3 sannolikheter behöver vi bara välja indexet med det högsta värdet.

![CLIP för Bildklassificering](../../../../../translated_images/clip-class.3af42ef0b2b19369a633df5f20ddf4f5a01d6c8ffa181e9d3a0572c19f919f72.sw.png)

> *Bild från [detta blogginlägg](https://openai.com/blog/clip/)*

**Textbaserad Bildsökning**

Vi kan också göra motsatsen. Om vi har en samling bilder kan vi skicka denna samling till modellen, och en textprompt - detta kommer att ge oss den bild som är mest lik en given prompt.

## ✍️ Exempel: [Använda CLIP för Bildklassificering och Bildsökning](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

Öppna [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) anteckningen för att se CLIP i aktion.

## Bildgenerering med VQGAN+ CLIP

CLIP kan också användas för **bildgenerering** från en textprompt. För att göra detta behöver vi en **generator-modell** som kan generera bilder baserat på någon vektorinput. En av dessa modeller kallas [VQGAN](https://compvis.github.io/taming-transformers/) (Vektor-Quantized GAN).

De huvudsakliga idéerna med VQGAN som skiljer den från vanliga [GAN](../../4-ComputerVision/10-GANs/README.md) är följande:
* Använda en autoregressiv transformerarkitektur för att generera en sekvens av kontext-rika visuella delar som utgör bilden. Dessa visuella delar lärs i sin tur av [CNN](../../4-ComputerVision/07-ConvNets/README.md)
* Använda en sub-bilddiskriminator som upptäcker om delar av bilden är "äkta" eller "falska" (till skillnad från den "allt eller inget"-metoden i traditionella GAN).

Lär dig mer om VQGAN på [Taming Transformers](https://compvis.github.io/taming-transformers/) webbplats.

En av de viktiga skillnaderna mellan VQGAN och traditionella GAN är att den senare kan producera en anständig bild från vilken vektorinput som helst, medan VQGAN sannolikt kommer att producera en bild som inte skulle vara sammanhängande. Därför behöver vi ytterligare styra bildskapandeprocessen, och det kan göras med hjälp av CLIP. 

![VQGAN+CLIP Arkitektur](../../../../../translated_images/vqgan.5027fe05051dfa3101950cfa930303f66e6478b9bd273e83766731796e462d9b.sw.png)

För att generera en bild som motsvarar en textprompt börjar vi med en slumpmässig kodningsvektor som skickas genom VQGAN för att producera en bild. Sedan används CLIP för att producera en förlustfunktion som visar hur väl bilden motsvarar textprompten. Målet är då att minimera denna förlust, genom att använda backpropagation för att justera parametrarna för inputvektorn.

Ett fantastiskt bibliotek som implementerar VQGAN+CLIP är [Pixray](http://github.com/pixray/pixray)

![Bild producerad av Pixray](../../../../../translated_images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d09dc96de938b9f95bde8a7e1c721f48f286a7795bf16d56c7.sw.png) |  ![Bild producerad av Pixray](../../../../../translated_images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a439077e1c32cc8afdf714e634fe24dc78dc5aa45fd2f560b0ed5.sw.png) | ![Bild producerad av Pixray](../../../../../translated_images/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683b9d36a613b364deb7454760cd39205623fc1e3938fa133c0.sw.png)
----|----|----
Bild genererad från prompt *en närbild av en akvarellporträtt av en ung manlig lärare i litteratur med en bok* | Bild genererad från prompt *en närbild av en oljemålning av en ung kvinnlig lärare i datavetenskap med en dator* | Bild genererad från prompt *en närbild av en oljemålning av en gammal manlig matematiklärare framför en tavla*

> Bilder från **Artificial Teachers** samlingen av [Dmitry Soshnikov](http://soshnikov.com)

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E är en version av GPT-3 som tränats för att generera bilder från promptar. Den har tränats med 12 miljarder parametrar.

Till skillnad från CLIP tar DALL-E emot både text och bild som en enda ström av tokens för både bilder och text. Därför kan du generera bilder baserat på text från flera promptar.

### [DALL-E 2](https://openai.com/dall-e-2)
Den huvudsakliga skillnaden mellan DALL-E 1 och 2 är att den genererar mer realistiska bilder och konst.

Exempel på bildgenereringar med DALL-E:
![Bild producerad av Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.sw.png) |  ![Bild producerad av Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.sw.png) | ![Bild producerad av Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.sw.png)
----|----|----
Bild genererad från prompt *en närbild av en akvarellporträtt av en ung manlig lärare i litteratur med en bok* | Bild genererad från prompt *en närbild av en oljemålning av en ung kvinnlig lärare i datavetenskap med en dator* | Bild genererad från prompt *en närbild av en oljemålning av en gammal manlig matematiklärare framför en tavla*

## Referenser

* VQGAN Papper: [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP Papper: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller oegentligheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.