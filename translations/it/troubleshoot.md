# Guida alla Risoluzione dei Problemi di AI-For-Beginners

Questa guida ti aiuta a risolvere i problemi comuni riscontrati durante l'utilizzo o il contributo al repository [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners). Ogni problema include contesto, sintomi, spiegazioni e soluzioni passo-passo.

---

## Indice

- [Problemi Generali](../..)
- [Problemi di Installazione](../..)
- [Problemi di Configurazione](../..)
- [Esecuzione dei Notebook](../..)
- [Problemi di Prestazioni](../..)
- [Problemi del Sito Web del Manuale](../..)
- [Problemi di Contributo](../..)
- [FAQ](../..)
- [Ottenere Aiuto](../..)

---

## Problemi Generali

### 1. Il Repository Non Si Clona Correttamente

**Contesto:** La clonazione ti permette di copiare il repository sul tuo computer.

**Sintomi:**
- Errore: `fatal: repository not found`
- Errore: `Permission denied (publickey)`

**Possibili Cause:**
- URL del repository errato
- Permessi insufficienti
- Chiavi SSH non configurate

**Soluzioni:**
1. **Controlla l'URL del repository.**  
   Usa l'URL HTTPS:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Passa a HTTPS se SSH fallisce.**  
   Se vedi `Permission denied (publickey)`, usa il link HTTPS sopra invece di SSH.
3. **Configura le chiavi SSH (opzionale).**  
   Se vuoi usare SSH, segui la [guida SSH di GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Problemi di Installazione

### 2. Problemi con l'Ambiente Python

**Contesto:** Il repository si basa su Python e varie librerie.

**Sintomi:**
- Errore: `ModuleNotFoundError: No module named '<package>'`
- Errori di importazione durante l'esecuzione di script o notebook

**Possibili Cause:**
- Dipendenze non installate
- Versione di Python errata

**Soluzioni:**
1. **Configura un ambiente virtuale.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Installa le dipendenze.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Controlla la versione di Python.**  
   Usa Python 3.7 o successivo.  
   ```bash
   python --version
   ```

### 3. Jupyter Non Installato

**Contesto:** I notebook sono una risorsa fondamentale per l'apprendimento.

**Sintomi:**
- Errore: `jupyter: command not found`
- I notebook non si avviano

**Possibili Cause:**
- Jupyter non installato

**Soluzioni:**
1. **Installa Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   oppure, se usi Anaconda:
   ```bash
   conda install notebook
   ```
2. **Avvia Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Conflitti di Versione delle Dipendenze

**Contesto:** I progetti possono rompersi se le versioni dei pacchetti non sono compatibili.

**Sintomi:**
- Errori o avvisi su versioni incompatibili

**Possibili Cause:**
- Pacchetti Python vecchi o in conflitto

**Soluzioni:**
1. **Installa in un ambiente pulito.**  
   Elimina vecchi ambienti venv/conda e creane uno nuovo.
2. **Usa versioni esatte.**  
   Esegui sempre:
   ```bash
   pip install -r requirements.txt
   ```
   Se questo fallisce, installa manualmente i pacchetti mancanti come descritto nel README.

---

## Problemi di Configurazione

### 5. Variabili d'Ambiente Non Impostate

**Contesto:** Alcuni moduli potrebbero richiedere chiavi, token o impostazioni di configurazione.

**Sintomi:**
- Errore: `KeyError` o avvisi su configurazioni mancanti

**Possibili Cause:**
- Variabili d'ambiente richieste non impostate

**Soluzioni:**
1. **Controlla file come `.env.example` o simili.**
2. **Crea un file `.env` e inserisci i valori richiesti.**
3. **Ricarica il terminale o l'IDE dopo aver impostato le variabili d'ambiente.**

---

## Esecuzione dei Notebook

### 6. Il Notebook Non Si Apre o Non Si Esegue

**Contesto:** I notebook Jupyter necessitano di una configurazione corretta.

**Sintomi:**
- Il notebook non si avvia
- Il browser non si apre automaticamente

**Possibili Cause:**
- Jupyter non installato
- Problemi di configurazione del browser

**Soluzioni:**
1. **Installa Jupyter (vedi Problemi di Installazione sopra).**
2. **Apri i notebook manualmente.**
   - Copia l'URL dal terminale (es., `http://localhost:8888/?token=...`) e incollalo nel browser.

### 7. Kernel che Si Blocca o Si Riavvia

**Contesto:** I kernel dei notebook possono bloccarsi a causa di limiti di risorse o errori nel codice.

**Sintomi:**
- Il kernel si interrompe o si riavvia ripetutamente
- Errori di memoria insufficiente

**Possibili Cause:**
- Dataset grandi
- Codice o pacchetti incompatibili

**Soluzioni:**
1. **Riavvia il kernel.**  
   Usa il pulsante "Restart Kernel" in Jupyter.
2. **Controlla l'utilizzo della memoria.**  
   Chiudi applicazioni inutilizzate.
3. **Esegui i notebook su piattaforme cloud.**  
   Usa [Google Colab](https://colab.research.google.com/) o [Azure Notebooks](https://notebooks.azure.com/).

---

## Problemi di Prestazioni

### 8. Notebook Lenti

**Contesto:** Alcuni compiti di AI richiedono molta memoria e CPU.

**Sintomi:**
- Esecuzione lenta
- Ventola del laptop che gira rumorosamente

**Possibili Cause:**
- Dataset o modelli grandi
- Risorse di sistema limitate

**Soluzioni:**
1. **Usa una piattaforma cloud.**
   - Carica il notebook su Colab o Azure Notebooks.
2. **Riduci la dimensione del dataset.**
   - Usa dati di esempio per esercitarti.
3. **Chiudi programmi inutili.**
   - Libera RAM di sistema.

---

## Problemi del Sito Web del Manuale

### 9. Capitolo Non Caricato

**Contesto:** Il manuale online mostra lezioni e capitoli.

**Sintomi:**
- Un capitolo (es., Transformers/BERT) è mancante o non si apre

**Problema Conosciuto:**  
- [Problema #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. non si apre sul sito del manuale.” Causato da un errore nel nome del file (`READMEtransformers.md` invece di `README.md`).

**Soluzioni:**
1. **Controlla errori di rinominazione dei file.**  
   Se sei un collaboratore, assicurati che i file dei capitoli siano chiamati `README.md`.
2. **Segnala file mancanti.**  
   Apri un problema su GitHub con il nome del capitolo e i dettagli dell'errore.

---

## Problemi di Contributo

### 10. PR Non Accettata o Build Fallite

**Contesto:** I contributi devono superare i test e seguire le linee guida.

**Sintomi:**
- Pull request respinta
- Errori nella pipeline CI/CD

**Possibili Cause:**
- Test falliti
- Standard di codifica non rispettati

**Soluzioni:**
1. **Leggi le linee guida per i contributi.**
   - Segui il [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) del repository.
2. **Esegui i test localmente prima di inviare.**
3. **Controlla le regole di linting o i requisiti di formattazione.**

---

## FAQ

### Dove posso trovare aiuto per moduli specifici?
- Ogni modulo di solito ha un proprio README. Inizia da lì per suggerimenti su configurazione e utilizzo.

### Come posso segnalare un bug o richiedere una funzionalità?
- [Apri un problema su GitHub](https://github.com/microsoft/AI-For-Beginners/issues/new) con una descrizione chiara e i passaggi per riprodurre il problema.

### Posso chiedere aiuto se il mio problema non è elencato?
- Certo! Cerca prima tra i problemi esistenti e, se non trovi il tuo problema, crea un nuovo problema.

---

## Ottenere Aiuto

- **Controlla i Problemi:** [Problemi su GitHub](https://github.com/microsoft/AI-For-Beginners/issues)
- **Fai Domande:** Usa le Discussioni su GitHub o apri un problema.
- **Comunità:** Consulta i link del repository per opzioni di chat/forum.

---

_Ultimo Aggiornamento: 20 settembre 2025_

---

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.