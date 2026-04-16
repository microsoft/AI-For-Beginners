# Višeklasna klasifikacija s perceptronom

Laboratorijska vježba iz [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Zadatak

Koristeći kod koji smo razvili u ovoj lekciji za binarnu klasifikaciju rukom pisanih znamenki iz MNIST skupa podataka, kreirajte višeklasni klasifikator koji će moći prepoznati bilo koju znamenku. Izračunajte točnost klasifikacije na skupu za treniranje i testiranje te ispišite matricu zabune.

## Savjeti

1. Za svaku znamenku kreirajte skup podataka za binarnu klasifikaciju "ova znamenka naspram svih ostalih znamenki"
1. Trenirajte 10 različitih perceptrona za binarnu klasifikaciju (po jedan za svaku znamenku)
1. Definirajte funkciju koja će klasificirati ulaznu znamenku

> **Savjet**: Ako kombiniramo težine svih 10 perceptrona u jednu matricu, trebali bismo moći primijeniti svih 10 perceptrona na ulazne znamenke pomoću jedne matrične množenja. Najvjerojatnija znamenka može se zatim pronaći jednostavnim primjenom `argmax` operacije na izlazu.

## Početna bilježnica

Započnite laboratorijsku vježbu otvaranjem [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.