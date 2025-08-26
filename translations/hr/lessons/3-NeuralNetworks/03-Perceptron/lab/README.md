<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-26T00:01:13+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "hr"
}
-->
# Višeklasna klasifikacija s perceptronom

Laboratorijska vježba iz [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Zadatak

Koristeći kod koji smo razvili u ovoj lekciji za binarnu klasifikaciju MNIST rukom pisanih znamenki, kreirajte višeklasni klasifikator koji će moći prepoznati bilo koju znamenku. Izračunajte točnost klasifikacije na skupu za treniranje i testiranje te ispišite matricu konfuzije.

## Savjeti

1. Za svaku znamenku kreirajte skup podataka za binarnu klasifikaciju "ova znamenka naspram svih ostalih znamenki"
1. Trenirajte 10 različitih perceptrona za binarnu klasifikaciju (jedan za svaku znamenku)
1. Definirajte funkciju koja će klasificirati ulaznu znamenku

> **Savjet**: Ako kombiniramo težine svih 10 perceptrona u jednu matricu, trebali bismo moći primijeniti svih 10 perceptrona na ulazne znamenke jednom matričnom množenjem. Najvjerojatnija znamenka može se zatim pronaći jednostavno primjenom `argmax` operacije na izlaz.

## Početna bilježnica

Započnite laboratorijsku vježbu otvaranjem [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.