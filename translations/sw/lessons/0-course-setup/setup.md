# Komma igång med denna läroplan

## Är du student?

Börja med följande resurser:

* [Student Hub-sidan](https://docs.microsoft.com/learn/student-hub?WT.mc_id=academic-77998-cacaste) På denna sida hittar du nybörjarresurser, studentpaket och till och med sätt att få en gratis certifikatvoucher. Detta är en sida du vill bokmärka och kolla på då och då eftersom vi byter ut innehållet minst en gång i månaden.
* [Microsoft Student Learn-ambassadörer](https://studentambassadors.microsoft.com?WT.mc_id=academic-77998-cacaste) Gå med i en global gemenskap av studentambassadörer, detta kan vara din väg in i Microsoft.

**Studenter**, det finns flera sätt att använda läroplanen. Först och främst kan du bara läsa texten och titta på koden direkt på GitHub. Om du vill köra koden i någon av anteckningsböckerna - [läs våra instruktioner](./etc/how-to-run.md), och hitta mer råd om hur du gör det [i detta blogginlägg](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

> **Notera**: [Instruktioner om hur man kör koden i denna läroplan](/how-to-run.md)

## Självstudier

Men om du vill ta kursen som ett självstudieprojekt, föreslår vi att du forklar hela repot till ditt eget GitHub-konto och slutför övningarna på egen hand eller med en grupp:

* Börja med ett quiz före föreläsningen.
* Läs introduktionstexten för föreläsningen.
* Om föreläsningen har ytterligare anteckningsböcker, gå igenom dem, läs och kör koden. Om både TensorFlow- och PyTorch-anteckningsböcker tillhandahålls, kan du fokusera på en av dem - välj ditt favoritramverk.
* Anteckningsböcker innehåller ofta några av de utmaningar som kräver att du justerar koden lite för att experimentera.
* Ta quizet efter föreläsningen.
* Om det finns ett laboratorium kopplat till modulen - slutför uppgiften.
* Besök [Diskussionsforumet](https://github.com/microsoft/AI-For-Beginners/discussions) för att "lära ut högt".

> För vidare studier rekommenderar vi att följa dessa [Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-77998-cacaste) moduler och lärstigar.

**Lärare**, vi har [inkluderat några förslag](/for-teachers.md) på hur man använder denna läroplan.

---

## Pedagogik

Vi har valt två pedagogiska principer när vi byggde denna läroplan: att säkerställa att den är praktisk **projektbaserad** och att den inkluderar **frekventa quiz**.

Genom att säkerställa att innehållet är kopplat till projekt, görs processen mer engagerande för studenterna och retentionen av koncept kommer att öka. Dessutom sätter ett lågriskquiz före en lektion intentionen för studenten att lära sig ett ämne, medan ett andra quiz efter lektionen säkerställer ytterligare retention. Denna läroplan är utformad för att vara flexibel och rolig och kan tas helt eller delvis. Projekten börjar små och blir alltmer komplexa i slutet av den 12 veckor långa cykeln.

> **En notering om quiz**: Alla quiz finns [i denna app](https://red-field-0a6ddfd03.1.azurestaticapps.net/), med totalt 50 quiz av tre frågor vardera. De är länkade från lektionerna, men quiz-appen kan köras lokalt; följ instruktionerna i `etc/quiz-app`-mappen.

## Offline-åtkomst

Du kan köra denna dokumentation offline genom att använda [Docsify](https://docsify.js.org/#/). Forka detta repo, [installera Docsify](https://docsify.js.org/#/quickstart) på din lokala maskin, och skriv sedan `docsify serve` i `etc/docsify`-mappen i detta repo. Webbplatsen kommer att serveras på port 3000 på din localhost: `localhost:3000`. En pdf av läroplanen finns tillgänglig [på denna länk](../../../../../../etc/pdf/readme.pdf).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller inkonsekvenser. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller felaktiga tolkningar som uppstår till följd av användningen av denna översättning.