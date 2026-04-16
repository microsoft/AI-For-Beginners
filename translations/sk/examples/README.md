# Príklady AI pre začiatočníkov

Vitajte! Tento adresár obsahuje jednoduché, samostatné príklady, ktoré vám pomôžu začať s AI a strojovým učením. Každý príklad je navrhnutý tak, aby bol priateľský pre začiatočníkov, s podrobnými komentármi a krok za krokom vysvetleniami.

## 📚 Prehľad príkladov

| Príklad | Popis | Obtiažnosť | Predpoklady |
|---------|-------------|------------|---------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Váš prvý AI program - jednoduché rozpoznávanie vzorov | ⭐ Začiatočník | Základy Pythonu |
| [Jednoduchá neurónová sieť](../../../examples/02-simple-neural-network.py) | Vytvorte neurónovú sieť od základov | ⭐⭐ Začiatočník+ | Python, základná matematika |
| [Klasifikátor obrázkov](./03-image-classifier.ipynb) | Klasifikujte obrázky pomocou predtrénovaného modelu | ⭐⭐ Začiatočník+ | Python, numpy |
| [Analýza sentimentu textu](../../../examples/04-text-sentiment.py) | Analyzujte sentiment textu (pozitívny/negatívny) | ⭐⭐ Začiatočník+ | Python |

## 🚀 Začíname

### Predpoklady

Uistite sa, že máte nainštalovaný Python (odporúča sa verzia 3.8 alebo vyššia). Nainštalujte potrebné balíčky:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Alebo použite conda prostredie z hlavného kurzu:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Spustenie príkladov

**Pre Python skripty (.py súbory):**
```bash
python 01-hello-ai-world.py
```

**Pre Jupyter notebooky (.ipynb súbory):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Učebná cesta

Odporúčame postupovať podľa príkladov v tomto poradí:

1. **Začnite s "Hello AI World"** - Naučte sa základy rozpoznávania vzorov
2. **Vytvorte jednoduchú neurónovú sieť** - Pochopte, ako fungujú neurónové siete
3. **Vyskúšajte klasifikátor obrázkov** - Pozrite sa na AI v akcii s reálnymi obrázkami
4. **Analyzujte sentiment textu** - Preskúmajte spracovanie prirodzeného jazyka

## 💡 Tipy pre začiatočníkov

- **Pozorne čítajte komentáre v kóde** - Vysvetľujú, čo robí každý riadok
- **Experimentujte!** - Skúste meniť hodnoty a sledujte, čo sa stane
- **Netrápte sa, ak všetkému nerozumiete** - Učenie si vyžaduje čas
- **Pýtajte sa otázky** - Použite [diskusné fórum](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Ďalšie kroky

Po dokončení týchto príkladov preskúmajte celý kurz:
- [Úvod do AI](../lessons/1-Intro/README.md)
- [Neurónové siete](../lessons/3-NeuralNetworks/README.md)
- [Počítačové videnie](../lessons/4-ComputerVision/README.md)
- [Spracovanie prirodzeného jazyka](../lessons/5-NLP/README.md)

## 🤝 Prispievanie

Považujete tieto príklady za užitočné? Pomôžte nám ich zlepšiť:
- Nahláste problémy alebo navrhnite vylepšenia
- Pridajte ďalšie príklady pre začiatočníkov
- Zlepšite dokumentáciu a komentáre

---

*Pamätajte: Každý odborník bol kedysi začiatočníkom. Šťastné učenie! 🎓*

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.