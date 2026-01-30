# AGENTS.md

## Proje Genel Bakış

AI for Beginners, Yapay Zeka temellerini kapsayan 12 haftalık, 24 derslik kapsamlı bir müfredattır. Bu eğitim deposu, Jupyter Notebooks, testler ve uygulamalı laboratuvarlar kullanarak pratik dersler içerir. Müfredat şunları kapsar:

- Bilgi Temsili ve Uzman Sistemleri ile Sembolik AI
- TensorFlow ve PyTorch ile Sinir Ağları ve Derin Öğrenme
- Bilgisayarlı Görü teknikleri ve mimarileri
- Doğal Dil İşleme (NLP), transformerlar ve BERT dahil
- Uzmanlaşmış konular: Genetik Algoritmalar, Pekiştirmeli Öğrenme, Çoklu Ajan Sistemleri
- AI Etiği ve Sorumlu AI ilkeleri

**Anahtar Teknolojiler:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (test uygulaması için)

**Mimari:** Konu alanlarına göre düzenlenmiş Jupyter Notebooks ile eğitim içeriği deposu, Vue.js tabanlı bir test uygulaması ve geniş çoklu dil desteği ile desteklenmiştir.

## Kurulum Komutları

### Birincil Geliştirme Ortamı (Python/Jupyter)

Müfredat, Python ve Jupyter Notebooks ile çalışacak şekilde tasarlanmıştır. Önerilen yöntem miniconda kullanmaktır:

```bash
# Clone the repository
git clone https://github.com/microsoft/ai-for-beginners
cd ai-for-beginners

# Create and activate conda environment
conda env create --name ai4beg --file environment.yml
conda activate ai4beg

# Start Jupyter Notebook
jupyter notebook
# OR
jupyter lab
```

### Alternatif: devcontainer kullanımı

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Test Uygulaması Kurulumu

Test uygulaması, `etc/quiz-app/` konumunda bulunan ayrı bir Vue.js uygulamasıdır:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Geliştirme İş Akışı

### Jupyter Notebooks ile Çalışma

1. **Yerel Geliştirme:**
   - Conda ortamını etkinleştirin: `conda activate ai4beg`
   - Jupyter'i başlatın: `jupyter notebook` veya `jupyter lab`
   - Ders klasörlerine gidin ve `.ipynb` dosyalarını açın
   - Dersleri takip etmek için hücreleri etkileşimli olarak çalıştırın

2. **VS Code ile Python Uzantısı:**
   - Depoyu VS Code'da açın
   - Python uzantısını yükleyin
   - VS Code, conda ortamını otomatik olarak algılar ve kullanır
   - `.ipynb` dosyalarını doğrudan VS Code'da açın

3. **Bulut Geliştirme:**
   - **GitHub Codespaces:** "Code" → "Codespaces" → "Create codespace on main" seçeneğine tıklayın
   - **Binder:** README'deki Binder rozetini kullanarak tarayıcıda başlatın
   - Not: Binder sınırlı kaynaklara sahiptir ve bazı web erişim kısıtlamaları vardır

### İleri Düzey Dersler için GPU Desteği

Sonraki dersler GPU hızlandırmasından önemli ölçüde faydalanır:

- **Azure Data Science VM:** GPU desteği olan NC serisi VM'leri kullanın
- **Azure Machine Learning:** GPU hesaplama özellikleriyle not defteri özelliklerini kullanın
- **Google Colab:** Not defterlerini tek tek yükleyin (ücretsiz GPU desteği vardır)

### Test Uygulaması Geliştirme

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Test Talimatları

Bu, yazılım testi yerine öğrenme içeriğine odaklanan bir eğitim deposudur. Geleneksel bir test paketi yoktur.

### Doğrulama Yaklaşımları:

1. **Jupyter Notebooks:** Kod örneklerinin çalıştığını doğrulamak için hücreleri sırasıyla çalıştırın
2. **Test Uygulaması Testi:** Geliştirme sunucusu üzerinden manuel test
3. **Çeviri Doğrulama:** `translations/` klasöründeki çevrilmiş içeriği kontrol edin
4. **Test Uygulaması Linting:** `npm run lint` komutunu `etc/quiz-app/` içinde çalıştırın

### Kod Örneklerini Çalıştırma:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Kod Stili

### Python Kod Stili

- Eğitim kodu için standart Python kuralları
- Öğrenmeyi optimizasyondan önceleyen açık, okunabilir kod
- Temel kavramları açıklayan yorumlar
- Jupyter Notebook dostu: hücreler mümkün olduğunca bağımsız olmalı
- Ders içeriği için katı linting gereksinimleri yok

### JavaScript/Vue.js (Test Uygulaması)

- `etc/quiz-app/package.json` içinde ESLint yapılandırması
- Sorunları kontrol etmek ve otomatik düzeltmek için `npm run lint` çalıştırın
- Vue 2.x kuralları
- Bileşen tabanlı mimari

### Dosya Organizasyonu

```
lessons/
  ├── 0-course-setup/          # Setup instructions
  ├── 1-Intro/                 # Introduction to AI
  ├── 2-Symbolic/              # Symbolic AI
  ├── 3-NeuralNetworks/        # Neural Networks basics
  ├── 4-ComputerVision/        # Computer Vision
  ├── 5-NLP/                   # Natural Language Processing
  ├── 6-Other/                 # Other AI techniques
  ├── 7-Ethics/                # AI Ethics
  └── X-Extras/                # Additional content

etc/
  ├── quiz-app/                # Vue.js quiz application
  └── quiz-src/                # Quiz source files

translations/                  # Multi-language translations
```

## Derleme ve Dağıtım

### Jupyter İçeriği

Derleme süreci gerekmez - Jupyter Notebooks doğrudan çalıştırılır.

### Test Uygulaması

```bash
cd etc/quiz-app

# Development
npm run serve

# Production build
npm run build  # Outputs to etc/quiz-app/dist/

# Deploy to Azure Static Web Apps
# Azure automatically creates GitHub Actions workflow
# See etc/quiz-app/README.md for detailed deployment instructions
```

### Dokümantasyon Sitesi

Depo, Docsify kullanarak belgeler sağlar:
- `index.html` giriş noktası olarak hizmet verir
- Derleme gerekmez - doğrudan GitHub Pages üzerinden sunulur
- Erişim: https://microsoft.github.io/AI-For-Beginners/

## Katkı Sağlama Kuralları

### Pull Request Süreci

1. **Başlık Formatı:** Değişikliği açıklayan açık, açıklayıcı başlıklar
2. **CLA Gerekliliği:** Microsoft CLA imzalanmış olmalı (otomatik kontrol)
3. **İçerik Kuralları:**
   - Eğitim odaklı ve başlangıç seviyesine uygun yaklaşımı koruyun
   - Not defterlerindeki tüm kod örneklerini test edin
   - Not defterlerinin baştan sona çalıştığından emin olun
   - İngilizce içeriği değiştiriyorsanız çevirileri güncelleyin
4. **Test Uygulaması Değişiklikleri:** Commit yapmadan önce `npm run lint` çalıştırın

### Çeviri Katkıları

- Çeviriler, GitHub Actions aracılığıyla co-op-translator kullanılarak otomatikleştirilir
- Manuel çeviriler `translations/<language-code>/` içine gider
- Test çevirileri `etc/quiz-app/src/assets/translations/` içine gider
- Desteklenen diller: 40+ dil (tam liste için README'ye bakın)

### Aktif Katkı Alanları

Mevcut ihtiyaçlar için `etc/CONTRIBUTING.md` dosyasına bakın:
- Derin Pekiştirmeli Öğrenme bölümleri
- Nesne Algılama iyileştirmeleri
- Adlandırılmış Varlık Tanıma örnekleri
- Özel gömme eğitimi örnekleri

## Ortam Yapılandırması

### Gerekli Bağımlılıklar

```bash
# Core Python packages (from requirements.txt)
tensorflow==2.17.0
torch (via conda)
torchvision (via conda)
keras==3.5.0
opencv (via conda)
scikit-learn
numpy==1.26
pandas==2.2.2
matplotlib==3.9
jupyter
```

### Ortam Değişkenleri

Temel kullanım için özel ortam değişkenleri gerekmez.

Azure dağıtımları (test uygulaması) için:
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (Azure tarafından otomatik olarak ayarlanır)

## Hata Ayıklama ve Sorun Giderme

### Yaygın Sorunlar

**Sorun:** Conda ortamı oluşturma başarısız
- **Çözüm:** Önce conda'yı güncelleyin: `conda update conda -y`
- Yeterli disk alanı olduğundan emin olun (50GB önerilir)

**Sorun:** Jupyter çekirdeği bulunamadı
- **Çözüm:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Sorun:** Not defterlerinde GPU algılanmıyor
- **Çözüm:** 
  - CUDA kurulumunu doğrulayın: `nvidia-smi`
  - PyTorch GPU kontrolü: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow GPU kontrolü: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Sorun:** Test uygulaması başlamıyor
- **Çözüm:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Sorun:** Binder zaman aşımına uğruyor veya indirmeleri engelliyor
- **Çözüm:** Daha iyi kaynak erişimi için GitHub Codespaces veya yerel kurulum kullanın

### Bellek Sorunları

Bazı dersler önemli miktarda RAM gerektirir (8GB+ önerilir):
- Kaynak yoğun dersler için bulut VM'leri kullanın
- Modelleri eğitirken diğer uygulamaları kapatın
- Bellek tükeniyorsa not defterlerinde toplu işlem boyutlarını azaltın

## Ek Notlar

### Kurs Eğitmenleri İçin

- Öğretim rehberi için `lessons/0-course-setup/for-teachers.md` dosyasına bakın
- Dersler bağımsızdır ve sırayla veya tek tek seçilerek öğretilebilir
- Tahmini süre: Haftada 2 dersle 12 hafta

### Bulut Kaynakları

- **Azure for Students:** Öğrenciler için ücretsiz krediler mevcut
- **Microsoft Learn:** Müfredat boyunca bağlantılı ek öğrenme yolları
- **Binder:** Ücretsiz ancak sınırlı kaynaklar ve bazı ağ kısıtlamaları

### Kod Çalıştırma Seçenekleri

1. **Yerel (Önerilen):** Tam kontrol, en iyi performans, GPU desteği
2. **GitHub Codespaces:** Bulut tabanlı VS Code, hızlı erişim için iyi
3. **Binder:** Tarayıcı tabanlı Jupyter, ücretsiz ancak sınırlı
4. **Azure ML Notebooks:** GPU desteği ile kurumsal seçenek
5. **Google Colab:** Not defterlerini tek tek yükleyin, ücretsiz GPU katmanı mevcut

### Not Defterleri ile Çalışma

- Not defterleri öğrenme için hücre hücre çalıştırılacak şekilde tasarlanmıştır
- Birçok not defteri ilk çalıştırmada veri setlerini indirir (zaman alabilir)
- Bazı modeller makul eğitim süreleri için GPU gerektirir
- Hesaplama gereksinimlerini azaltmak için önceden eğitilmiş modeller kullanılır

### Performans Düşünceleri

- Bilgisayarlı görme derslerinin (CNN'ler, GAN'lar) GPU'dan faydası büyük
- NLP transformer dersleri önemli miktarda RAM gerektirebilir
- Sıfırdan eğitim öğretici ancak zaman alıcıdır
- Transfer öğrenme örnekleri eğitim süresini minimize eder

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.