# Träna Mountain Car för att Fly

Laborationsuppgift från [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Uppgift

Ditt mål är att träna RL-agenten att kontrollera [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/) i OpenAI-miljön. Du är tränad på data fram till oktober 2023.

## Miljön

Mountain Car-miljön består av en bil som är fast i en dal. Ditt mål är att hoppa ut ur dalen och nå flaggan. De åtgärder du kan utföra är att accelerera åt vänster, åt höger eller göra ingenting. Du kan observera bilens position längs x-axeln och hastigheten.

## Starta Anteckningsbok

Börja labben genom att öppna [MountainCar.ipynb](../../../../../../lessons/6-Other/22-DeepRL/lab/MountainCar.ipynb)

## Sammanfattning

Du bör lära dig under denna labb att anpassa RL-algoritmer till en ny miljö ofta är ganska enkelt, eftersom OpenAI Gym har samma gränssnitt för alla miljöer, och algoritmerna i sig beror inte i stor utsträckning på miljöns natur. Du kan till och med omstrukturera Python-koden på ett sådant sätt att du kan skicka vilken miljö som helst till RL-algoritmen som en parameter.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi tar inget ansvar för missförstånd eller felaktiga tolkningar som uppstår från användningen av denna översättning.