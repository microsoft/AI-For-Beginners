# Autoencoders

När vi tränar CNN:er är ett av problemen att vi behöver mycket märkt data. När det gäller bildklassificering behöver vi separera bilder i olika klasser, vilket är en manuell insats.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

Vi kan dock vilja använda rå (omärkt) data för att träna CNN-funktionsextraktorer, vilket kallas **självövervakad inlärning**. Istället för etiketter kommer vi att använda träningsbilder som både nätverksinmatning och utdata. Huvudidén med **autoencoder** är att vi kommer att ha ett **encoder-nätverk** som konverterar inmatad bild till ett visst **latent rum** (normalt är det bara en vektor av mindre storlek), och sedan **decoder-nätverket**, vars mål är att rekonstruera den ursprungliga bilden.

> ✅ En [autoencoder](https://wikipedia.org/wiki/Autoencoder) är "en typ av artificiellt neuralt nätverk som används för att lära sig effektiva kodningar av omärkt data."

Eftersom vi tränar en autoencoder för att fånga så mycket information som möjligt från den ursprungliga bilden för noggrann rekonstruktion, försöker nätverket hitta den bästa **inbäddningen** av inmatade bilder för att fånga betydelsen.

![AutoEncoder Diagram](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.sw.jpg)

> Bild från [Keras blog](https://blog.keras.io/building-autoencoders-in-keras.html)

## Scenarier för användning av Autoencoders

Även om rekonstruktion av ursprungliga bilder inte verkar användbart i sig, finns det några scenarier där autoencoders är särskilt användbara:

* **Minska dimensionen av bilder för visualisering** eller **träning av bildeinbäddningar**. Vanligtvis ger autoencoders bättre resultat än PCA, eftersom de tar hänsyn till den spatiala naturen hos bilder och hierarkiska funktioner.
* **Denoising**, dvs. ta bort brus från bilden. Eftersom brus bär med sig mycket oanvändbar information kan autoencodern inte passa in allt i det relativt lilla latenta rummet, och fångar därför endast den viktiga delen av bilden. När vi tränar avbrusare börjar vi med ursprungliga bilder och använder bilder med artificiellt tillagt brus som indata för autoencodern.
* **Super-upplösning**, öka bildens upplösning. Vi börjar med högupplösta bilder och använder bilder med lägre upplösning som autoencoder-inmatning.
* **Generativa modeller**. När vi har tränat autoencodern kan decoder-delen användas för att skapa nya objekt utifrån slumpmässiga latenta vektorer.

## Variational Autoencoders (VAE)

Traditionella autoencoders minskar dimensionen av indata på något sätt, genom att identifiera de viktiga funktionerna i inmatade bilder. Latenta vektorer ger dock ofta inte mycket mening. Med andra ord, med MNIST-datasetet som exempel, är det inte en lätt uppgift att ta reda på vilka siffror som motsvarar olika latenta vektorer, eftersom nära latenta vektorer inte nödvändigtvis motsvarar samma siffror.

Å andra sidan, för att träna *generativa* modeller är det bättre att ha en viss förståelse för det latenta rummet. Denna idé leder oss till **variational autoencoder** (VAE).

VAE är autoencodern som lär sig att förutsäga *statistisk fördelning* av de latenta parametrarna, så kallad **latent fördelning**. Till exempel kan vi vilja att latenta vektorer ska fördelas normalt med ett visst medelvärde z<sub>mean</sub> och standardavvikelse z<sub>sigma</sub> (både medelvärde och standardavvikelse är vektorer av viss dimension d). Encodern i VAE lär sig att förutsäga dessa parametrar, och sedan tar decodern en slumpmässig vektor från denna fördelning för att rekonstruera objektet.

Sammanfattningsvis:

 * Från inmatad vektor förutspår vi `z_mean` och `z_log_sigma` (istället för att förutsäga standardavvikelsen själv, förutspår vi dess logaritm)
 * Vi sampel en vektor `sample` från fördelningen N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * Decodern försöker avkoda den ursprungliga bilden med `sample` som inmatad vektor

 <img src="images/vae.png" width="50%">

> Bild från [denna blogginlägg](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) av Isaak Dykeman

Variational autoencoders använder en komplex förlustfunktion som består av två delar:

* **Rekonstruktionsförlust** är förlustfunktionen som visar hur nära en rekonstruerad bild är målet (det kan vara Mean Squared Error, eller MSE). Det är samma förlustfunktion som i vanliga autoencoders.
* **KL-förlust**, som säkerställer att de latenta variabelns fördelningar förblir nära normalfördelningen. Den baseras på begreppet [Kullback-Leibler divergence](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - en metrik för att uppskatta hur lika två statistiska fördelningar är.

En viktig fördel med VAEs är att de gör det möjligt för oss att generera nya bilder relativt enkelt, eftersom vi vet vilken fördelning vi ska sampela latenta vektorer från. Om vi till exempel tränar en VAE med 2D latent vektor på MNIST kan vi sedan variera komponenterna i den latenta vektorn för att få olika siffror:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Bild av [Dmitry Soshnikov](http://soshnikov.com)

Observera hur bilderna blandar sig med varandra, när vi börjar få latenta vektorer från olika delar av det latenta parameterrummet. Vi kan också visualisera detta rum i 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Bild av [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Övningar: Autoencoders

Lär dig mer om autoencoders i dessa motsvarande anteckningar:

* [Autoencoders i TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoencoders i PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Egenskaper hos Autoencoders

* **Dataspecifika** - de fungerar bara bra med den typ av bilder de har tränats på. Om vi till exempel tränar ett super-upplösningsnätverk på blommor kommer det inte att fungera bra på porträtt. Detta beror på att nätverket kan producera högupplösta bilder genom att ta fina detaljer från funktioner som lärts från träningsdatasetet.
* **Förlustiga** - den rekonstruerade bilden är inte densamma som den ursprungliga bilden. Förlustens natur definieras av *förlustfunktionen* som används under träning.
* Fungerar på **omärkt data**.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## Slutsats

I denna lektion lärde du dig om de olika typerna av autoencoders som finns tillgängliga för AI-forskaren. Du lärde dig hur man bygger dem och hur man använder dem för att rekonstruera bilder. Du lärde dig också om VAE och hur man använder den för att generera nya bilder.

## 🚀 Utmaning

I denna lektion lärde du dig om att använda autoencoders för bilder. Men de kan också användas för musik! Kolla in Magenta-projektets [MusicVAE](https://magenta.tensorflow.org/music-vae) projekt, som använder autoencoders för att lära sig rekonstruera musik. Gör några [experiment](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) med detta bibliotek för att se vad du kan skapa.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Granskning & Självstudie

För referens, läs mer om autoencoders i dessa resurser:

* [Bygga Autoencoders i Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blogginlägg om NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Förklarade Variational Autoencoders](https://kvfrans.com/variational-autoencoders-explained/)
* [Villkorliga Variational Autoencoders](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Uppgift

I slutet av [denna anteckning som använder TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb) hittar du en 'uppgift' - använd detta som din uppgift.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.