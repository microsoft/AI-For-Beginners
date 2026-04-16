# Yeni Başlayanlar İçin AI Örnekleri

Hoş geldiniz! Bu dizin, yapay zeka ve makine öğrenimine başlamak için basit, bağımsız örnekler içerir. Her örnek, ayrıntılı yorumlar ve adım adım açıklamalarla yeni başlayanlar için uygun şekilde tasarlanmıştır.

## 📚 Örneklerin Genel Görünümü

| Örnek | Açıklama | Zorluk | Ön Koşullar |
|-------|----------|--------|-------------|
| [Merhaba AI Dünyası](../../../examples/01-hello-ai-world.py) | İlk yapay zeka programınız - basit desen tanıma | ⭐ Başlangıç | Python temelleri |
| [Basit Sinir Ağı](../../../examples/02-simple-neural-network.py) | Sıfırdan bir sinir ağı oluşturun | ⭐⭐ Başlangıç+ | Python, temel matematik |
| [Görüntü Sınıflandırıcı](./03-image-classifier.ipynb) | Önceden eğitilmiş bir modelle görüntüleri sınıflandırın | ⭐⭐ Başlangıç+ | Python, numpy |
| [Metin Duygusu](../../../examples/04-text-sentiment.py) | Metin duygu analizini yapın (pozitif/negatif) | ⭐⭐ Başlangıç+ | Python |

## 🚀 Başlarken

### Ön Koşullar

Python'un yüklü olduğundan emin olun (3.8 veya daha yüksek sürüm önerilir). Gerekli paketleri yükleyin:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Ya da ana müfredattan conda ortamını kullanın:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Örnekleri Çalıştırma

**Python dosyaları (.py):**
```bash
python 01-hello-ai-world.py
```

**Jupyter defterleri (.ipynb):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Öğrenme Yolu

Örnekleri sırasıyla takip etmenizi öneririz:

1. **"Merhaba AI Dünyası" ile başlayın** - Desen tanımanın temellerini öğrenin
2. **Basit bir Sinir Ağı oluşturun** - Sinir ağlarının nasıl çalıştığını anlayın
3. **Görüntü Sınıflandırıcıyı deneyin** - Gerçek görüntülerle yapay zekayı görün
4. **Metin Duygusu Analizi yapın** - Doğal dil işleme dünyasını keşfedin

## 💡 Yeni Başlayanlar İçin İpuçları

- **Kod yorumlarını dikkatlice okuyun** - Her satırın ne yaptığını açıklar
- **Deneyin!** - Değerleri değiştirin ve sonuçları görün
- **Her şeyi anlamaya çalışmayın** - Öğrenmek zaman alır
- **Sorular sorun** - [Tartışma panosunu](https://github.com/microsoft/AI-For-Beginners/discussions) kullanın

## 🔗 Sonraki Adımlar

Bu örnekleri tamamladıktan sonra tam müfredatı keşfedin:
- [AI'ye Giriş](../lessons/1-Intro/README.md)
- [Sinir Ağları](../lessons/3-NeuralNetworks/README.md)
- [Bilgisayarlı Görü](../lessons/4-ComputerVision/README.md)
- [Doğal Dil İşleme](../lessons/5-NLP/README.md)

## 🤝 Katkıda Bulunma

Bu örnekleri faydalı buldunuz mu? Geliştirmemize yardımcı olun:
- Sorunları bildirin veya iyileştirme önerilerinde bulunun
- Yeni başlayanlar için daha fazla örnek ekleyin
- Belgeleri ve yorumları geliştirin

---

*Unutmayın: Her uzman bir zamanlar yeni başkandı. İyi öğrenmeler! 🎓*

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.