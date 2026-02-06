# Primeri umetne inteligence za začetnike

Dobrodošli! Ta imenik vsebuje preproste, samostojne primere, ki vam bodo pomagali začeti z umetno inteligenco in strojno učenje. Vsak primer je zasnovan tako, da je prijazen začetnikom, z natančnimi komentarji in razlagami korak za korakom.

## 📚 Pregled primerov

| Primer | Opis | Težavnost | Predznanje |
|--------|------|-----------|------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Vaš prvi program umetne inteligence - preprosto prepoznavanje vzorcev | ⭐ Začetnik | Osnove Pythona |
| [Preprosta nevronska mreža](../../../examples/02-simple-neural-network.py) | Zgradite nevronsko mrežo iz nič | ⭐⭐ Začetnik+ | Python, osnovna matematika |
| [Razvrščevalnik slik](./03-image-classifier.ipynb) | Razvrščajte slike s predhodno naučenim modelom | ⭐⭐ Začetnik+ | Python, numpy |
| [Besedilni sentiment](../../../examples/04-text-sentiment.py) | Analizirajte sentiment besedila (pozitivno/negativno) | ⭐⭐ Začetnik+ | Python |

## 🚀 Začetek

### Predpogoji

Prepričajte se, da imate nameščen Python (priporočena različica 3.8 ali višja). Namestite potrebne pakete:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Ali uporabite conda okolje iz glavnega kurikuluma:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Zagon primerov

**Za Python skripte (.py datoteke):**
```bash
python 01-hello-ai-world.py
```

**Za Jupyter beležke (.ipynb datoteke):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Učni načrt

Priporočamo, da sledite primerom po vrsti:

1. **Začnite z "Hello AI World"** - Spoznajte osnove prepoznavanja vzorcev
2. **Zgradite preprosto nevronsko mrežo** - Razumite, kako delujejo nevronske mreže
3. **Preizkusite razvrščevalnik slik** - Oglejte si umetno inteligenco v akciji s pravimi slikami
4. **Analizirajte besedilni sentiment** - Raziščite obdelavo naravnega jezika

## 💡 Nasveti za začetnike

- **Pozorno preberite komentarje v kodi** - Razložijo, kaj počne vsaka vrstica
- **Eksperimentirajte!** - Poskusite spreminjati vrednosti in opazujte rezultate
- **Ne skrbite, če ne razumete vsega** - Učenje zahteva čas
- **Postavljajte vprašanja** - Uporabite [diskusijsko ploščo](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Naslednji koraki

Ko zaključite te primere, raziščite celoten kurikulum:
- [Uvod v umetno inteligenco](../lessons/1-Intro/README.md)
- [Nevronske mreže](../lessons/3-NeuralNetworks/README.md)
- [Računalniški vid](../lessons/4-ComputerVision/README.md)
- [Obdelava naravnega jezika](../lessons/5-NLP/README.md)

## 🤝 Prispevanje

So vam bili ti primeri v pomoč? Pomagajte nam jih izboljšati:
- Prijavite težave ali predlagajte izboljšave
- Dodajte več primerov za začetnike
- Izboljšajte dokumentacijo in komentarje

---

*Zapomnite si: Vsak strokovnjak je bil nekoč začetnik. Veselo učenje! 🎓*

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.