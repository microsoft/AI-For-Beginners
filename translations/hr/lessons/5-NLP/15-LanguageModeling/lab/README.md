# Treniranje Skip-Gram modela

Laboratorijska vježba iz [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Zadatak

U ovoj vježbi izazivamo vas da trenirate Word2Vec model koristeći Skip-Gram tehniku. Trenirajte mrežu s ugradnjom (embedding) kako biste predvidjeli susjedne riječi unutar Skip-Gram prozora širine $N$ tokena. Možete koristiti [kod iz ove lekcije](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) i malo ga prilagoditi.

## Skup podataka

Slobodno koristite bilo koju knjigu. Mnogo besplatnih tekstova možete pronaći na [Project Gutenberg](https://www.gutenberg.org/), na primjer, ovdje je izravan link na [Alisine pustolovine u zemlji čudesa](https://www.gutenberg.org/files/11/11-0.txt)) Lewisa Carrolla. Ili, možete koristiti Shakespeareove drame, koje možete preuzeti koristeći sljedeći kod:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Istražujte!

Ako imate vremena i želite dublje istražiti temu, pokušajte istražiti nekoliko stvari:

* Kako veličina ugradnje (embedding) utječe na rezultate?
* Kako različiti stilovi teksta utječu na rezultat?
* Uzmite nekoliko vrlo različitih vrsta riječi i njihovih sinonima, dobijte njihove vektorske reprezentacije, primijenite PCA za smanjenje dimenzija na 2 i prikažite ih u 2D prostoru. Vidite li neke uzorke?

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.