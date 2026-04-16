# Primjeri umjetne inteligencije za početnike

Dobrodošli! Ovaj direktorij sadrži jednostavne, samostalne primjere koji će vam pomoći da započnete s umjetnom inteligencijom i strojnim učenjem. Svaki primjer je osmišljen tako da bude prilagođen početnicima, uz detaljne komentare i objašnjenja korak po korak.

## 📚 Pregled primjera

| Primjer | Opis | Težina | Preduvjeti |
|---------|-------------|------------|---------------|
| [Pozdrav AI svijetu](../../../examples/01-hello-ai-world.py) | Vaš prvi AI program - jednostavno prepoznavanje uzoraka | ⭐ Početnik | Osnove Pythona |
| [Jednostavna neuronska mreža](../../../examples/02-simple-neural-network.py) | Izgradite neuronsku mrežu od nule | ⭐⭐ Početnik+ | Python, osnovna matematika |
| [Klasifikator slika](./03-image-classifier.ipynb) | Klasificirajte slike pomoću unaprijed treniranog modela | ⭐⭐ Početnik+ | Python, numpy |
| [Sentiment teksta](../../../examples/04-text-sentiment.py) | Analizirajte sentiment teksta (pozitivan/negativan) | ⭐⭐ Početnik+ | Python |

## 🚀 Početak rada

### Preduvjeti

Provjerite imate li instaliran Python (preporučuje se verzija 3.8 ili novija). Instalirajte potrebne pakete:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Ili koristite conda okruženje iz glavnog kurikuluma:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Pokretanje primjera

**Za Python skripte (.py datoteke):**
```bash
python 01-hello-ai-world.py
```

**Za Jupyter bilježnice (.ipynb datoteke):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Put učenja

Preporučujemo da slijedite primjere redoslijedom:

1. **Započnite s "Pozdrav AI svijetu"** - Naučite osnove prepoznavanja uzoraka
2. **Izgradite jednostavnu neuronsku mrežu** - Shvatite kako neuronske mreže funkcioniraju
3. **Isprobajte klasifikator slika** - Pogledajte AI u akciji s pravim slikama
4. **Analizirajte sentiment teksta** - Istražite obradu prirodnog jezika

## 💡 Savjeti za početnike

- **Pažljivo čitajte komentare u kodu** - Objašnjavaju što svaka linija radi
- **Eksperimentirajte!** - Pokušajte mijenjati vrijednosti i vidjeti što se događa
- **Ne brinite ako ne razumijete sve** - Učenje zahtijeva vrijeme
- **Postavljajte pitanja** - Koristite [diskusijsku ploču](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Sljedeći koraci

Nakon što završite ove primjere, istražite cijeli kurikulum:
- [Uvod u AI](../lessons/1-Intro/README.md)
- [Neuronske mreže](../lessons/3-NeuralNetworks/README.md)
- [Računalni vid](../lessons/4-ComputerVision/README.md)
- [Obrada prirodnog jezika](../lessons/5-NLP/README.md)

## 🤝 Doprinos

Jesu li vam ovi primjeri korisni? Pomozite nam da ih poboljšamo:
- Prijavite probleme ili predložite poboljšanja
- Dodajte više primjera za početnike
- Poboljšajte dokumentaciju i komentare

---

*Zapamtite: Svaki stručnjak je jednom bio početnik. Sretno u učenju! 🎓*

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.