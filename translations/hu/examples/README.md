# Kezdőbarát AI Példák

Üdvözlünk! Ez a könyvtár egyszerű, önálló példákat tartalmaz, amelyek segítenek az AI és a gépi tanulás alapjainak elsajátításában. Minden példa kezdőbarát, részletes megjegyzésekkel és lépésről lépésre történő magyarázatokkal.

## 📚 Példák Áttekintése

| Példa | Leírás | Nehézség | Előfeltételek |
|-------|--------|----------|---------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Az első AI programod - egyszerű mintafelismerés | ⭐ Kezdő | Python alapok |
| [Egyszerű Neurális Hálózat](../../../examples/02-simple-neural-network.py) | Neurális hálózat építése az alapoktól | ⭐⭐ Kezdő+ | Python, alap matematikai ismeretek |
| [Képosztályozó](./03-image-classifier.ipynb) | Képek osztályozása előre betanított modellel | ⭐⭐ Kezdő+ | Python, numpy |
| [Szöveg Hangulata](../../../examples/04-text-sentiment.py) | Szövegek hangulatának elemzése (pozitív/negatív) | ⭐⭐ Kezdő+ | Python |

## 🚀 Első Lépések

### Előfeltételek

Győződj meg róla, hogy a Python telepítve van (ajánlott verzió: 3.8 vagy újabb). Telepítsd a szükséges csomagokat:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Vagy használd a fő tananyag conda környezetét:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Példák Futattása

**Python szkriptekhez (.py fájlok):**
```bash
python 01-hello-ai-world.py
```

**Jupyter notebookokhoz (.ipynb fájlok):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Tanulási Útmutató

Javasoljuk, hogy a példákat sorrendben kövesd:

1. **Kezdd a "Hello AI World"-del** - Ismerd meg a mintafelismerés alapjait
2. **Építs egy Egyszerű Neurális Hálót** - Értsd meg, hogyan működnek a neurális hálók
3. **Próbáld ki a Képosztályozót** - Nézd meg az AI-t működés közben valódi képekkel
4. **Elemezd a Szöveg Hangulatát** - Fedezd fel a természetes nyelvfeldolgozást

## 💡 Tippek Kezdőknek

- **Olvasd el figyelmesen a kódban található megjegyzéseket** - Ezek elmagyarázzák, hogy mit csinál minden sor
- **Kísérletezz!** - Próbálj meg értékeket módosítani, és figyeld meg, mi történik
- **Ne aggódj, ha nem értesz mindent azonnal** - A tanulás időt vesz igénybe
- **Tegyél fel kérdéseket** - Használd a [Vita fórumot](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Következő Lépések

Miután befejezted ezeket a példákat, fedezd fel a teljes tananyagot:
- [Bevezetés az AI-ba](../lessons/1-Intro/README.md)
- [Neurális Hálók](../lessons/3-NeuralNetworks/README.md)
- [Számítógépes Látás](../lessons/4-ComputerVision/README.md)
- [Természetes Nyelvfeldolgozás](../lessons/5-NLP/README.md)

## 🤝 Közreműködés

Hasznosnak találtad ezeket a példákat? Segíts nekünk javítani rajtuk:
- Jelents hibákat vagy javasolj fejlesztéseket
- Adj hozzá további példákat kezdők számára
- Fejleszd a dokumentációt és a megjegyzéseket

---

*Ne feledd: Minden szakértő egyszer kezdő volt. Jó tanulást! 🎓*

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.