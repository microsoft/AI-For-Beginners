# Příklady AI pro začátečníky

Vítejte! Tento adresář obsahuje jednoduché, samostatné příklady, které vám pomohou začít s AI a strojovým učením. Každý příklad je navržen tak, aby byl přívětivý pro začátečníky, s podrobnými komentáři a postupnými vysvětleními.

## 📚 Přehled příkladů

| Příklad | Popis | Obtížnost | Předpoklady |
|---------|-------|-----------|-------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Váš první AI program - jednoduché rozpoznávání vzorů | ⭐ Začátečník | Základy Pythonu |
| [Jednoduchá neuronová síť](../../../examples/02-simple-neural-network.py) | Vytvořte neuronovou síť od základu | ⭐⭐ Začátečník+ | Python, základní matematika |
| [Klasifikátor obrázků](./03-image-classifier.ipynb) | Klasifikujte obrázky pomocí předtrénovaného modelu | ⭐⭐ Začátečník+ | Python, numpy |
| [Textová sentimentální analýza](../../../examples/04-text-sentiment.py) | Analyzujte sentiment textu (pozitivní/negativní) | ⭐⭐ Začátečník+ | Python |

## 🚀 Začínáme

### Předpoklady

Ujistěte se, že máte nainstalovaný Python (doporučujeme verzi 3.8 nebo vyšší). Nainstalujte potřebné balíčky:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Nebo použijte conda prostředí z hlavního kurzu:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Spouštění příkladů

**Pro Python skripty (.py soubory):**
```bash
python 01-hello-ai-world.py
```

**Pro Jupyter notebooky (.ipynb soubory):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Učební cesta

Doporučujeme postupovat podle příkladů v tomto pořadí:

1. **Začněte s "Hello AI World"** - Naučte se základy rozpoznávání vzorů
2. **Vytvořte jednoduchou neuronovou síť** - Pochopte, jak fungují neuronové sítě
3. **Vyzkoušejte klasifikátor obrázků** - Podívejte se na AI v akci s reálnými obrázky
4. **Analyzujte sentiment textu** - Prozkoumejte zpracování přirozeného jazyka

## 💡 Tipy pro začátečníky

- **Pečlivě čtěte komentáře v kódu** - Vysvětlují, co každá řádka dělá
- **Experimentujte!** - Zkuste měnit hodnoty a sledujte, co se stane
- **Nedělejte si starosti, pokud všemu nerozumíte** - Učení vyžaduje čas
- **Ptejte se** - Použijte [diskusní fórum](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Další kroky

Po dokončení těchto příkladů prozkoumejte celý kurz:
- [Úvod do AI](../lessons/1-Intro/README.md)
- [Neuronové sítě](../lessons/3-NeuralNetworks/README.md)
- [Počítačové vidění](../lessons/4-ComputerVision/README.md)
- [Zpracování přirozeného jazyka](../lessons/5-NLP/README.md)

## 🤝 Přispívání

Pomohly vám tyto příklady? Pomozte nám je zlepšit:
- Nahlaste problémy nebo navrhněte vylepšení
- Přidejte další příklady pro začátečníky
- Zlepšete dokumentaci a komentáře

---

*Pamatujte: Každý expert byl kdysi začátečníkem. Přejeme vám příjemné učení! 🎓*

---

**Upozornění**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.