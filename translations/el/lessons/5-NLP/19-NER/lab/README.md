# NER

Εργαστηριακή Άσκηση από το [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Εργασία

Σε αυτό το εργαστήριο, πρέπει να εκπαιδεύσετε ένα μοντέλο αναγνώρισης οντοτήτων (NER) για ιατρικούς όρους.

## Το Σύνολο Δεδομένων

Για να εκπαιδεύσουμε ένα μοντέλο NER, χρειαζόμαστε ένα σωστά επισημασμένο σύνολο δεδομένων με ιατρικές οντότητες. Το [σύνολο δεδομένων BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) περιέχει επισημασμένες οντότητες ασθενειών και χημικών από περισσότερα από 1500 άρθρα. Μπορείτε να κατεβάσετε το σύνολο δεδομένων αφού εγγραφείτε στον ιστότοπό τους.

Το σύνολο δεδομένων BC5CDR μοιάζει κάπως έτσι:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Σε αυτό το σύνολο δεδομένων, υπάρχουν ο τίτλος και η περίληψη του άρθρου στις δύο πρώτες γραμμές, και στη συνέχεια εμφανίζονται οι μεμονωμένες οντότητες, με τις αρχικές και τελικές τους θέσεις μέσα στο μπλοκ τίτλου+περίληψης. Εκτός από τον τύπο της οντότητας, λαμβάνετε το αναγνωριστικό οντολογίας αυτής της οντότητας μέσα σε κάποια ιατρική οντολογία.

Θα χρειαστεί να γράψετε λίγο κώδικα Python για να μετατρέψετε αυτά τα δεδομένα σε μορφή BIO.

## Το Δίκτυο

Η πρώτη προσπάθεια για NER μπορεί να γίνει χρησιμοποιώντας ένα δίκτυο LSTM, όπως στο παράδειγμα που είδατε κατά τη διάρκεια του μαθήματος. Ωστόσο, στις εργασίες NLP, η [αρχιτεκτονική transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) και συγκεκριμένα τα [μοντέλα γλώσσας BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) δείχνουν πολύ καλύτερα αποτελέσματα. Τα προεκπαιδευμένα μοντέλα BERT κατανοούν τη γενική δομή μιας γλώσσας και μπορούν να προσαρμοστούν για συγκεκριμένες εργασίες με σχετικά μικρά σύνολα δεδομένων και χαμηλό υπολογιστικό κόστος.

Δεδομένου ότι σκοπεύουμε να εφαρμόσουμε το NER σε ιατρικό σενάριο, έχει νόημα να χρησιμοποιήσουμε ένα μοντέλο BERT εκπαιδευμένο σε ιατρικά κείμενα. Η Microsoft Research έχει κυκλοφορήσει ένα προεκπαιδευμένο μοντέλο που ονομάζεται [PubMedBERT][PubMedBERT] ([δημοσίευση][PubMedBERT-Pub]), το οποίο έχει προσαρμοστεί χρησιμοποιώντας κείμενα από το αποθετήριο [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Το *de facto* πρότυπο για την εκπαίδευση μοντέλων transformer είναι η βιβλιοθήκη [Hugging Face Transformers](https://huggingface.co/). Περιέχει επίσης ένα αποθετήριο με προεκπαιδευμένα μοντέλα που συντηρούνται από την κοινότητα, συμπεριλαμβανομένου του PubMedBERT. Για να φορτώσετε και να χρησιμοποιήσετε αυτό το μοντέλο, χρειάζεστε μόνο μερικές γραμμές κώδικα:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Αυτό μας δίνει το ίδιο το `model`, το οποίο είναι κατασκευασμένο για εργασία ταξινόμησης token χρησιμοποιώντας `classes` αριθμό κατηγοριών, καθώς και το αντικείμενο `tokenizer` που μπορεί να διασπάσει το κείμενο εισόδου σε tokens. Θα χρειαστεί να μετατρέψετε το σύνολο δεδομένων σε μορφή BIO, λαμβάνοντας υπόψη την τοκενιοποίηση του PubMedBERT. Μπορείτε να χρησιμοποιήσετε [αυτό το κομμάτι κώδικα Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) ως έμπνευση.

## Συμπέρασμα

Αυτή η εργασία είναι πολύ κοντά στην πραγματική εργασία που πιθανότατα θα έχετε αν θέλετε να αποκτήσετε περισσότερες γνώσεις από μεγάλα σύνολα κειμένων φυσικής γλώσσας. Στην περίπτωσή μας, μπορούμε να εφαρμόσουμε το εκπαιδευμένο μοντέλο μας στο [σύνολο δεδομένων άρθρων που σχετίζονται με τον COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) και να δούμε ποια συμπεράσματα μπορούμε να αντλήσουμε. [Αυτή η ανάρτηση στο blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) και [αυτό το άρθρο](https://www.mdpi.com/2504-2289/6/1/4) περιγράφουν την έρευνα που μπορεί να γίνει σε αυτό το σύνολο άρθρων χρησιμοποιώντας NER.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.