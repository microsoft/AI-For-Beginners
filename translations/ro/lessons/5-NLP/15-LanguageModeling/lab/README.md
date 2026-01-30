# Antrenarea modelului Skip-Gram

Temă de laborator din [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Sarcina

În acest laborator, te provocăm să antrenezi un model Word2Vec folosind tehnica Skip-Gram. Antrenează o rețea cu embedding pentru a prezice cuvintele vecine într-o fereastră Skip-Gram de $N$ token-uri. Poți folosi [codul din această lecție](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) și să-l modifici ușor.

## Setul de date

Poți folosi orice carte. Găsești o mulțime de texte gratuite pe [Project Gutenberg](https://www.gutenberg.org/), de exemplu, iată un link direct către [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) de Lewis Carroll. Sau, poți folosi piesele lui Shakespeare, pe care le poți obține folosind următorul cod:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Explorează!

Dacă ai timp și vrei să aprofundezi subiectul, încearcă să explorezi câteva aspecte:

* Cum influențează dimensiunea embedding-ului rezultatele?
* Cum influențează diferitele stiluri de text rezultatele?
* Ia câteva tipuri foarte diferite de cuvinte și sinonimele lor, obține reprezentările lor vectoriale, aplică PCA pentru a reduce dimensiunile la 2 și plotează-le în spațiul 2D. Observi vreun tipar?

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.