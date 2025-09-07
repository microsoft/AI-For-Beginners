<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98c5222ff9556b55223fed2337145e18",
  "translation_date": "2025-08-26T07:13:25+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "it"
}
-->
*Immagine [da Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), di Longlivetheux - Opera propria, CC BY-SA 4.0*

Pertanto, il problema della **rappresentazione della conoscenza** consiste nel trovare un modo efficace per rappresentare la conoscenza all'interno di un computer sotto forma di dati, rendendola automaticamente utilizzabile. Questo può essere visto come uno spettro:

![Spettro della rappresentazione della conoscenza](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.it.png)

> Immagine di [Dmitry Soshnikov](http://soshnikov.com)

* A sinistra, ci sono tipi di rappresentazione della conoscenza molto semplici che possono essere utilizzati efficacemente dai computer. La più semplice è quella algoritmica, in cui la conoscenza è rappresentata da un programma informatico. Tuttavia, questo non è il modo migliore per rappresentare la conoscenza, poiché non è flessibile. La conoscenza nella nostra mente è spesso non algoritmica.
* A destra, ci sono rappresentazioni come il testo naturale. È la più potente, ma non può essere utilizzata per il ragionamento automatico.

> ✅ Pensa per un momento a come rappresenti la conoscenza nella tua mente e la converti in appunti. Esiste un formato particolare che funziona bene per te per favorire la memorizzazione?

## Classificazione delle rappresentazioni della conoscenza nei computer

Possiamo classificare i diversi metodi di rappresentazione della conoscenza nei computer nelle seguenti categorie:

* **Rappresentazioni a rete** si basano sul fatto che abbiamo una rete di concetti interrelati nella nostra mente. Possiamo provare a riprodurre le stesse reti come un grafo all'interno di un computer - una cosiddetta **rete semantica**.

1. **Triplette Oggetto-Attributo-Valore** o **coppie attributo-valore**. Poiché un grafo può essere rappresentato all'interno di un computer come un elenco di nodi e archi, possiamo rappresentare una rete semantica con un elenco di triplette, contenenti oggetti, attributi e valori. Ad esempio, costruiamo le seguenti triplette sui linguaggi di programmazione:

Oggetto | Attributo | Valore
--------|-----------|------
Python  | è         | Linguaggio non tipizzato
Python  | inventato-da | Guido van Rossum
Python  | sintassi-blocco | indentazione
Linguaggio non tipizzato | non ha | definizioni di tipo

> ✅ Pensa a come le triplette possono essere utilizzate per rappresentare altri tipi di conoscenza.

2. **Rappresentazioni gerarchiche** enfatizzano il fatto che spesso creiamo una gerarchia di oggetti nella nostra mente. Ad esempio, sappiamo che il canarino è un uccello, e tutti gli uccelli hanno le ali. Abbiamo anche un'idea di quale sia il colore di un canarino e della sua velocità di volo.

   - **Rappresentazione a frame** si basa sulla rappresentazione di ogni oggetto o classe di oggetti come un **frame** che contiene **slot**. Gli slot hanno possibili valori predefiniti, restrizioni di valore o procedure memorizzate che possono essere chiamate per ottenere il valore di uno slot. Tutti i frame formano una gerarchia simile a una gerarchia di oggetti nei linguaggi di programmazione orientati agli oggetti.
   - **Scenari** sono un tipo speciale di frame che rappresentano situazioni complesse che possono evolversi nel tempo.

**Python**

Slot | Valore | Valore predefinito | Intervallo |
-----|--------|--------------------|------------|
Nome | Python |                    |            |
È-Un | Linguaggio non tipizzato |            |            |
Caso Variabile |                    | CamelCase  |            |
Lunghezza Programma |              |            | 5-5000 righe |
Sintassi Blocco | Indentazione      |            |            |

3. **Rappresentazioni procedurali** si basano sulla rappresentazione della conoscenza tramite un elenco di azioni che possono essere eseguite quando si verifica una certa condizione.
   - Le regole di produzione sono dichiarazioni if-then che ci permettono di trarre conclusioni. Ad esempio, un medico può avere una regola che dice che **SE** un paziente ha febbre alta **O** un alto livello di proteina C-reattiva nel test del sangue **ALLORA** ha un'infiammazione. Una volta che incontriamo una delle condizioni, possiamo trarre una conclusione sull'infiammazione e poi usarla per ulteriori ragionamenti.
   - Gli algoritmi possono essere considerati un'altra forma di rappresentazione procedurale, anche se quasi mai vengono utilizzati direttamente nei sistemi basati sulla conoscenza.

4. **Logica** è stata originariamente proposta da Aristotele come un modo per rappresentare la conoscenza universale umana.
   - La logica predicativa come teoria matematica è troppo ricca per essere computabile, quindi normalmente viene utilizzato un sottoinsieme di essa, come le clausole di Horn utilizzate in Prolog.
   - La logica descrittiva è una famiglia di sistemi logici utilizzati per rappresentare e ragionare su gerarchie di oggetti e rappresentazioni distribuite della conoscenza come il *web semantico*.

## Sistemi esperti

Uno dei primi successi dell'IA simbolica sono stati i cosiddetti **sistemi esperti** - sistemi informatici progettati per agire come esperti in un dominio di problemi limitato. Si basavano su una **base di conoscenza** estratta da uno o più esperti umani e contenevano un **motore di inferenza** che eseguiva alcuni ragionamenti su di essa.

![Architettura umana](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.it.png) | ![Sistema basato sulla conoscenza](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.it.png)
---------------------------------------------|------------------------------------------------
Struttura semplificata del sistema neurale umano | Architettura di un sistema basato sulla conoscenza

I sistemi esperti sono costruiti come il sistema di ragionamento umano, che contiene **memoria a breve termine** e **memoria a lungo termine**. Allo stesso modo, nei sistemi basati sulla conoscenza distinguiamo i seguenti componenti:

* **Memoria del problema**: contiene la conoscenza sul problema attualmente in fase di risoluzione, ad esempio la temperatura o la pressione sanguigna di un paziente, se ha un'infiammazione o meno, ecc. Questa conoscenza è anche chiamata **conoscenza statica**, poiché contiene un'istantanea di ciò che sappiamo attualmente sul problema - il cosiddetto *stato del problema*.
* **Base di conoscenza**: rappresenta la conoscenza a lungo termine su un dominio di problemi. È estratta manualmente dagli esperti umani e non cambia da una consultazione all'altra. Poiché ci permette di navigare da uno stato del problema a un altro, è anche chiamata **conoscenza dinamica**.
* **Motore di inferenza**: orchestra l'intero processo di ricerca nello spazio dello stato del problema, ponendo domande all'utente quando necessario. È anche responsabile di trovare le regole giuste da applicare a ogni stato.

Come esempio, consideriamo il seguente sistema esperto per determinare un animale basandosi sulle sue caratteristiche fisiche:

![Albero AND-OR](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.it.png)

> Immagine di [Dmitry Soshnikov](http://soshnikov.com)

Questo diagramma è chiamato **albero AND-OR**, ed è una rappresentazione grafica di un insieme di regole di produzione. Disegnare un albero è utile all'inizio dell'estrazione della conoscenza dall'esperto. Per rappresentare la conoscenza all'interno del computer è più conveniente utilizzare regole:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Puoi notare che ogni condizione sul lato sinistro della regola e l'azione sono essenzialmente triplette Oggetto-Attributo-Valore (OAV). La **memoria di lavoro** contiene l'insieme di triplette OAV che corrispondono al problema attualmente in fase di risoluzione. Un **motore di regole** cerca regole per le quali una condizione è soddisfatta e le applica, aggiungendo un'altra tripletta alla memoria di lavoro.

> ✅ Scrivi il tuo albero AND-OR su un argomento che ti piace!

### Inferenza in avanti vs. inferenza all'indietro

Il processo descritto sopra è chiamato **inferenza in avanti**. Inizia con alcuni dati iniziali sul problema disponibili nella memoria di lavoro e poi esegue il seguente ciclo di ragionamento:

1. Se l'attributo target è presente nella memoria di lavoro - fermati e fornisci il risultato
2. Cerca tutte le regole la cui condizione è attualmente soddisfatta - ottieni il **set di conflitto** delle regole.
3. Esegui la **risoluzione del conflitto** - seleziona una regola che verrà eseguita in questo passaggio. Ci potrebbero essere diverse strategie di risoluzione del conflitto:
   - Seleziona la prima regola applicabile nella base di conoscenza
   - Seleziona una regola casuale
   - Seleziona una regola *più specifica*, cioè quella che soddisfa il maggior numero di condizioni nel "lato sinistro" (LHS)
4. Applica la regola selezionata e inserisci un nuovo pezzo di conoscenza nello stato del problema
5. Ripeti dal passo 1.

Tuttavia, in alcuni casi potremmo voler iniziare con una conoscenza vuota sul problema e porre domande che ci aiuteranno ad arrivare alla conclusione. Ad esempio, quando si effettua una diagnosi medica, di solito non eseguiamo tutte le analisi mediche in anticipo prima di iniziare a diagnosticare il paziente. Piuttosto, vogliamo eseguire analisi quando è necessario prendere una decisione.

Questo processo può essere modellato utilizzando **inferenza all'indietro**. È guidato dall'**obiettivo** - il valore dell'attributo che stiamo cercando di trovare:

1. Seleziona tutte le regole che possono fornire il valore di un obiettivo (cioè con l'obiettivo sul RHS ("lato destro")) - un set di conflitto
1. Se non ci sono regole per questo attributo, o c'è una regola che dice che dovremmo chiedere il valore all'utente - chiedilo, altrimenti:
1. Usa una strategia di risoluzione del conflitto per selezionare una regola che useremo come *ipotesi* - proveremo a dimostrarla
1. Ripeti ricorsivamente il processo per tutti gli attributi nel LHS della regola, cercando di dimostrarli come obiettivi
1. Se in qualsiasi momento il processo fallisce - usa un'altra regola al passo 3.

> ✅ In quali situazioni è più appropriata l'inferenza in avanti? E l'inferenza all'indietro?

### Implementazione dei sistemi esperti

I sistemi esperti possono essere implementati utilizzando diversi strumenti:

* Programmandoli direttamente in un linguaggio di programmazione di alto livello. Questa non è la scelta migliore, poiché il principale vantaggio di un sistema basato sulla conoscenza è che la conoscenza è separata dall'inferenza, e potenzialmente un esperto del dominio del problema dovrebbe essere in grado di scrivere regole senza comprendere i dettagli del processo di inferenza.
* Utilizzando un **guscio di sistemi esperti**, cioè un sistema progettato specificamente per essere popolato di conoscenza utilizzando un linguaggio di rappresentazione della conoscenza.

## ✍️ Esercizio: Inferenza sugli animali

Consulta [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) per un esempio di implementazione di un sistema esperto con inferenza in avanti e all'indietro.
> **Nota**: Questo esempio è piuttosto semplice e serve solo a dare un'idea di come appare un sistema esperto. Una volta che inizi a creare un sistema del genere, noterai un comportamento *intelligente* solo quando raggiungi un certo numero di regole, circa 200 o più. A un certo punto, le regole diventano troppo complesse per tenerle tutte a mente, e potresti iniziare a chiederti perché il sistema prenda determinate decisioni. Tuttavia, una caratteristica importante dei sistemi basati sulla conoscenza è che puoi sempre *spiegare* esattamente come è stata presa ciascuna decisione.
## Ontologie e il Web Semantico

Alla fine del XX secolo, è stata avviata un'iniziativa per utilizzare la rappresentazione della conoscenza al fine di annotare le risorse Internet, rendendo possibile trovare risorse che corrispondano a query molto specifiche. Questo movimento è stato chiamato **Web Semantico** e si basava su diversi concetti:

- Una rappresentazione della conoscenza speciale basata su **[logiche descrittive](https://en.wikipedia.org/wiki/Description_logic)** (DL). È simile alla rappresentazione della conoscenza a frame, poiché costruisce una gerarchia di oggetti con proprietà, ma ha una semantica logica formale e inferenza. Esiste un'intera famiglia di DL che bilanciano tra espressività e complessità algoritmica dell'inferenza.
- Una rappresentazione della conoscenza distribuita, in cui tutti i concetti sono rappresentati da un identificatore URI globale, rendendo possibile creare gerarchie di conoscenza che si estendono su Internet.
- Una famiglia di linguaggi basati su XML per la descrizione della conoscenza: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Un concetto fondamentale nel Web Semantico è quello di **Ontologia**. Si riferisce a una specifica esplicita di un dominio di problema utilizzando una rappresentazione formale della conoscenza. L'ontologia più semplice può essere solo una gerarchia di oggetti in un dominio di problema, ma le ontologie più complesse includeranno regole che possono essere utilizzate per l'inferenza.

Nel Web Semantico, tutte le rappresentazioni si basano su triplette. Ogni oggetto e ogni relazione sono identificati univocamente dall'URI. Ad esempio, se vogliamo affermare che questo Curriculum di AI è stato sviluppato da Dmitry Soshnikov il 1° gennaio 2022, ecco le triplette che possiamo utilizzare:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Qui `http://www.example.com/terms/creation-date` e `http://purl.org/dc/elements/1.1/creator` sono alcuni URI ben noti e universalmente accettati per esprimere i concetti di *creatore* e *data di creazione*.

In un caso più complesso, se vogliamo definire un elenco di creatori, possiamo utilizzare alcune strutture dati definite in RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagrammi sopra di [Dmitry Soshnikov](http://soshnikov.com)

Il progresso nella costruzione del Web Semantico è stato in qualche modo rallentato dal successo dei motori di ricerca e delle tecniche di elaborazione del linguaggio naturale, che consentono di estrarre dati strutturati dal testo. Tuttavia, in alcune aree ci sono ancora sforzi significativi per mantenere ontologie e basi di conoscenza. Alcuni progetti degni di nota:

* [WikiData](https://wikidata.org/) è una raccolta di basi di conoscenza leggibili dalle macchine associate a Wikipedia. La maggior parte dei dati è estratta dagli *InfoBox* di Wikipedia, pezzi di contenuto strutturato all'interno delle pagine di Wikipedia. Puoi [interrogare](https://query.wikidata.org/) WikiData in SPARQL, un linguaggio di query speciale per il Web Semantico. Ecco un esempio di query che mostra i colori degli occhi più popolari tra gli esseri umani:

```sparql
#defaultView:BubbleChart
SELECT ?eyeColorLabel (COUNT(?human) AS ?count)
WHERE
{
  ?human wdt:P31 wd:Q5.       # human instance-of homo sapiens
  ?human wdt:P1340 ?eyeColor. # human eye-color ?eyeColor
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?eyeColorLabel
```

* [DBpedia](https://www.dbpedia.org/) è un altro progetto simile a WikiData.

> ✅ Se vuoi sperimentare la costruzione delle tue ontologie o aprire quelle esistenti, c'è un ottimo editor visuale di ontologie chiamato [Protégé](https://protege.stanford.edu/). Scaricalo o usalo online.

<img src="images/protege.png" width="70%"/>

*Editor Web Protégé aperto con l'ontologia della Famiglia Romanov. Screenshot di Dmitry Soshnikov*

## ✍️ Esercizio: Un'Ontologia Familiare

Consulta [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) per un esempio di utilizzo delle tecniche del Web Semantico per ragionare sulle relazioni familiari. Prenderemo un albero genealogico rappresentato nel formato comune GEDCOM e un'ontologia delle relazioni familiari per costruire un grafo di tutte le relazioni familiari per un determinato insieme di individui.

## Microsoft Concept Graph

Nella maggior parte dei casi, le ontologie sono create con cura manualmente. Tuttavia, è anche possibile **estrarre** ontologie da dati non strutturati, ad esempio da testi in linguaggio naturale.

Un tentativo in tal senso è stato fatto da Microsoft Research, e ha portato al [Microsoft Concept Graph](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Si tratta di una vasta raccolta di entità raggruppate utilizzando la relazione di ereditarietà `is-a`. Consente di rispondere a domande come "Cos'è Microsoft?" - la risposta potrebbe essere qualcosa come "un'azienda con probabilità 0,87 e un marchio con probabilità 0,75".

Il grafo è disponibile sia come API REST che come un grande file di testo scaricabile che elenca tutte le coppie di entità.

## ✍️ Esercizio: Un Concept Graph

Prova il notebook [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) per vedere come possiamo utilizzare Microsoft Concept Graph per raggruppare articoli di notizie in diverse categorie.

## Conclusione

Oggi, l'AI è spesso considerata sinonimo di *Machine Learning* o *Reti Neurali*. Tuttavia, un essere umano dimostra anche un ragionamento esplicito, qualcosa che attualmente non viene gestito dalle reti neurali. Nei progetti del mondo reale, il ragionamento esplicito è ancora utilizzato per svolgere compiti che richiedono spiegazioni o la capacità di modificare il comportamento del sistema in modo controllato.

## 🚀 Sfida

Nel notebook sull'Ontologia Familiare associato a questa lezione, c'è l'opportunità di sperimentare altre relazioni familiari. Prova a scoprire nuove connessioni tra le persone nell'albero genealogico.

## [Quiz post-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/202)

## Revisione e Studio Autonomo

Fai una ricerca su Internet per scoprire aree in cui gli esseri umani hanno cercato di quantificare e codificare la conoscenza. Dai un'occhiata alla Tassonomia di Bloom e torna indietro nella storia per imparare come gli esseri umani hanno cercato di dare un senso al loro mondo. Esplora il lavoro di Linneo per creare una tassonomia degli organismi e osserva come Dmitri Mendeleev ha creato un modo per descrivere e raggruppare gli elementi chimici. Quali altri esempi interessanti riesci a trovare?

**Compito**: [Costruisci un'Ontologia](assignment.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.