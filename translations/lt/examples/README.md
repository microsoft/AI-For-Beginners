# Pradedančiųjų AI pavyzdžiai

Sveiki! Šiame kataloge rasite paprastus, savarankiškus pavyzdžius, kurie padės jums pradėti dirbti su AI ir mašininio mokymosi technologijomis. Kiekvienas pavyzdys yra sukurtas taip, kad būtų draugiškas pradedantiesiems, su išsamiais komentarais ir žingsnis po žingsnio paaiškinimais.

## 📚 Pavyzdžių apžvalga

| Pavyzdys | Aprašymas | Sudėtingumas | Reikalavimai |
|----------|-----------|--------------|--------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Jūsų pirmoji AI programa – paprastas šablonų atpažinimas | ⭐ Pradedantysis | Python pagrindai |
| [Paprastas neuroninis tinklas](../../../examples/02-simple-neural-network.py) | Sukurkite neuroninį tinklą nuo nulio | ⭐⭐ Pradedantysis+ | Python, pagrindinė matematika |
| [Vaizdų klasifikatorius](./03-image-classifier.ipynb) | Klasifikuokite vaizdus naudodami iš anksto apmokytą modelį | ⭐⭐ Pradedantysis+ | Python, numpy |
| [Teksto sentimentas](../../../examples/04-text-sentiment.py) | Analizuokite teksto sentimentą (teigiamas/neigiamas) | ⭐⭐ Pradedantysis+ | Python |

## 🚀 Pradžia

### Reikalavimai

Įsitikinkite, kad turite įdiegtą Python (rekomenduojama 3.8 ar naujesnė versija). Įdiekite reikalingus paketus:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Arba naudokite conda aplinką iš pagrindinio mokymo plano:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Pavyzdžių paleidimas

**Python skriptams (.py failai):**
```bash
python 01-hello-ai-world.py
```

**Jupyter užrašinėms (.ipynb failai):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Mokymosi kelias

Rekomenduojame sekti pavyzdžius iš eilės:

1. **Pradėkite nuo "Hello AI World"** – Sužinokite šablonų atpažinimo pagrindus
2. **Sukurkite paprastą neuroninį tinklą** – Supraskite, kaip veikia neuroniniai tinklai
3. **Išbandykite vaizdų klasifikatorių** – Pamatykite AI veikimą su realiais vaizdais
4. **Analizuokite teksto sentimentą** – Tyrinėkite natūralios kalbos apdorojimą

## 💡 Patarimai pradedantiesiems

- **Atidžiai skaitykite kodo komentarus** – Jie paaiškina, ką daro kiekviena eilutė
- **Eksperimentuokite!** – Pabandykite keisti reikšmes ir stebėkite rezultatus
- **Nesijaudinkite, jei ne viską suprasite** – Mokymasis užtrunka
- **Užduokite klausimus** – Naudokitės [Diskusijų lenta](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Kiti žingsniai

Baigę šiuos pavyzdžius, tyrinėkite visą mokymo planą:
- [Įvadas į AI](../lessons/1-Intro/README.md)
- [Neuroniniai tinklai](../lessons/3-NeuralNetworks/README.md)
- [Kompiuterinis matymas](../lessons/4-ComputerVision/README.md)
- [Natūralios kalbos apdorojimas](../lessons/5-NLP/README.md)

## 🤝 Prisidėkite

Ar šie pavyzdžiai buvo naudingi? Padėkite mums juos patobulinti:
- Praneškite apie problemas arba siūlykite patobulinimus
- Pridėkite daugiau pavyzdžių pradedantiesiems
- Tobulinkite dokumentaciją ir komentarus

---

*Atminkite: Kiekvienas ekspertas kažkada buvo pradedantysis. Sėkmingo mokymosi! 🎓*

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius naudojant šį vertimą.