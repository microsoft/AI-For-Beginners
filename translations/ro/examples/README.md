# Exemple de AI pentru Începători

Bun venit! Acest director conține exemple simple și independente pentru a te ajuta să începi cu AI și învățarea automată. Fiecare exemplu este conceput să fie prietenos pentru începători, cu comentarii detaliate și explicații pas cu pas.

## 📚 Prezentare Generală a Exemplului

| Exemplu | Descriere | Dificultate | Cerințe Prealabile |
|---------|-----------|-------------|--------------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Primul tău program AI - recunoaștere simplă de tipare | ⭐ Începător | Bazele Python |
| [Rețea Neurală Simplă](../../../examples/02-simple-neural-network.py) | Construiește o rețea neurală de la zero | ⭐⭐ Începător+ | Python, matematică de bază |
| [Clasificator de Imagini](./03-image-classifier.ipynb) | Clasifică imagini cu un model pre-antrenat | ⭐⭐ Începător+ | Python, numpy |
| [Sentiment Textual](../../../examples/04-text-sentiment.py) | Analizează sentimentul textului (pozitiv/negativ) | ⭐⭐ Începător+ | Python |

## 🚀 Începe

### Cerințe Prealabile

Asigură-te că ai instalat Python (recomandat 3.8 sau mai nou). Instalează pachetele necesare:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Sau folosește mediul conda din curriculumul principal:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Rularea Exemplului

**Pentru scripturi Python (.py):**
```bash
python 01-hello-ai-world.py
```

**Pentru notebook-uri Jupyter (.ipynb):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Calea de Învățare

Recomandăm să urmezi exemplele în ordine:

1. **Începe cu "Hello AI World"** - Învață bazele recunoașterii de tipare
2. **Construiește o Rețea Neurală Simplă** - Înțelege cum funcționează rețelele neurale
3. **Încearcă Clasificatorul de Imagini** - Vezi AI în acțiune cu imagini reale
4. **Analizează Sentimentul Textual** - Explorează procesarea limbajului natural

## 💡 Sfaturi pentru Începători

- **Citește cu atenție comentariile din cod** - Ele explică ce face fiecare linie
- **Experimentează!** - Încearcă să schimbi valori și vezi ce se întâmplă
- **Nu te îngrijora dacă nu înțelegi totul** - Învățarea necesită timp
- **Pune întrebări** - Folosește [forumul de discuții](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Următorii Pași

După ce finalizezi aceste exemple, explorează curriculumul complet:
- [Introducere în AI](../lessons/1-Intro/README.md)
- [Rețele Neurale](../lessons/3-NeuralNetworks/README.md)
- [Viziune Computațională](../lessons/4-ComputerVision/README.md)
- [Procesarea Limbajului Natural](../lessons/5-NLP/README.md)

## 🤝 Contribuie

Ai găsit aceste exemple utile? Ajută-ne să le îmbunătățim:
- Raportează probleme sau sugerează îmbunătățiri
- Adaugă mai multe exemple pentru începători
- Îmbunătățește documentația și comentariile

---

*Ține minte: Fiecare expert a fost odată un începător. Învățare plăcută! 🎓*

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.