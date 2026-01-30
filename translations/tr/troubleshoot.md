# AI-For-Beginners Sorun Giderme Kılavuzu

Bu kılavuz, [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) deposunu kullanırken veya katkıda bulunurken karşılaşılan yaygın sorunları çözmenize yardımcı olur. Her sorun için arka plan bilgisi, belirtiler, açıklamalar ve adım adım çözümler sunulmaktadır.

---

## İçindekiler

- [Genel Sorunlar](../..)
- [Kurulum Sorunları](../..)
- [Yapılandırma Sorunları](../..)
- [Notebook Çalıştırma](../..)
- [Performans Sorunları](../..)
- [Ders Kitabı Web Sitesi Sorunları](../..)
- [Katkı Sağlama Sorunları](../..)
- [SSS](../..)
- [Yardım Alma](../..)

---

## Genel Sorunlar

### 1. Depo Doğru Şekilde Klonlanamıyor

**Arka Plan:** Klonlama, depoyu bilgisayarınıza kopyalamanıza olanak tanır.

**Belirtiler:**
- Hata: `fatal: repository not found`
- Hata: `Permission denied (publickey)`

**Olası Nedenler:**
- Yanlış depo URL'si
- Yetersiz izinler
- SSH anahtarları yapılandırılmamış

**Çözümler:**
1. **Depo URL'sini kontrol edin.**  
   HTTPS URL'sini kullanın:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **SSH başarısız olursa HTTPS'e geçin.**  
   Eğer `Permission denied (publickey)` hatası alıyorsanız, SSH yerine yukarıdaki HTTPS bağlantısını kullanın.
3. **SSH anahtarlarını yapılandırın (isteğe bağlı).**  
   SSH kullanmak istiyorsanız, [GitHub'ın SSH rehberini](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) takip edin.

---

## Kurulum Sorunları

### 2. Python Ortamı Sorunları

**Arka Plan:** Depo, Python ve çeşitli kütüphanelere dayanır.

**Belirtiler:**
- Hata: `ModuleNotFoundError: No module named '<package>'`
- Script veya notebook çalıştırırken ithalat hataları

**Olası Nedenler:**
- Bağımlılıklar yüklenmemiş
- Yanlış Python sürümü

**Çözümler:**
1. **Sanal bir ortam oluşturun.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Bağımlılıkları yükleyin.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Python sürümünü kontrol edin.**  
   Python 3.7 veya daha yeni bir sürüm kullanın.  
   ```bash
   python --version
   ```

### 3. Jupyter Yüklenmemiş

**Arka Plan:** Notebook'lar temel öğrenme kaynağıdır.

**Belirtiler:**
- Hata: `jupyter: command not found`
- Notebook'lar açılmıyor

**Olası Nedenler:**
- Jupyter yüklenmemiş

**Çözümler:**
1. **Jupyter Notebook'u yükleyin.**  
   ```bash
   pip install notebook
   ```
   veya, Anaconda kullanıyorsanız:
   ```bash
   conda install notebook
   ```
2. **Jupyter Notebook'u başlatın.**  
   ```bash
   jupyter notebook
   ```

### 4. Bağımlılık Sürüm Çakışmaları

**Arka Plan:** Paket sürümleri uyumsuz olduğunda projeler bozulabilir.

**Belirtiler:**
- Uyumsuz sürümlerle ilgili hata veya uyarılar

**Olası Nedenler:**
- Eski veya çakışan Python paketleri

**Çözümler:**
1. **Temiz bir ortamda yükleme yapın.**  
   Eski venv/conda ortamını silin ve yenisini oluşturun.
2. **Kesin sürümleri kullanın.**  
   Her zaman şu komutu çalıştırın:  
   ```bash
   pip install -r requirements.txt
   ```
   Eğer bu başarısız olursa, README'de açıklanan şekilde eksik paketleri manuel olarak yükleyin.

---

## Yapılandırma Sorunları

### 5. Ortam Değişkenleri Ayarlanmamış

**Arka Plan:** Bazı modüller anahtarlar, token'lar veya yapılandırma ayarları gerektirebilir.

**Belirtiler:**
- Hata: `KeyError` veya eksik yapılandırma ile ilgili uyarılar

**Olası Nedenler:**
- Gerekli ortam değişkenleri ayarlanmamış

**Çözümler:**
1. **`.env.example` veya benzer dosyaları kontrol edin.**
2. **Bir `.env` dosyası oluşturun ve gerekli değerleri doldurun.**
3. **Ortam değişkenlerini ayarladıktan sonra terminalinizi veya IDE'nizi yeniden başlatın.**

---

## Notebook Çalıştırma

### 6. Notebook Açılmıyor veya Çalışmıyor

**Arka Plan:** Jupyter notebook'ların doğru şekilde kurulması gerekir.

**Belirtiler:**
- Notebook başlatılamıyor
- Tarayıcı otomatik olarak açılmıyor

**Olası Nedenler:**
- Jupyter yüklenmemiş
- Tarayıcı yapılandırma sorunları

**Çözümler:**
1. **Jupyter'i yükleyin (yukarıdaki Kurulum Sorunları bölümüne bakın).**
2. **Notebook'ları manuel olarak açın.**
   - Terminaldeki URL'yi (örneğin, `http://localhost:8888/?token=...`) kopyalayıp tarayıcınıza yapıştırın.

### 7. Çekirdek Çöküyor veya Donuyor

**Arka Plan:** Notebook çekirdekleri kaynak sınırları veya kod hataları nedeniyle çökebilir.

**Belirtiler:**
- Çekirdek sürekli olarak çöküyor veya yeniden başlıyor
- Bellek yetersiz hataları

**Olası Nedenler:**
- Büyük veri setleri
- Uyumsuz kod veya paketler

**Çözümler:**
1. **Çekirdeği yeniden başlatın.**  
   Jupyter'deki "Restart Kernel" düğmesini kullanın.
2. **Bellek kullanımını kontrol edin.**  
   Kullanılmayan uygulamaları kapatın.
3. **Notebook'ları bulut platformlarında çalıştırın.**  
   [Google Colab](https://colab.research.google.com/) veya [Azure Notebooks](https://notebooks.azure.com/) kullanın.

---

## Performans Sorunları

### 8. Notebook'lar Yavaş Çalışıyor

**Arka Plan:** Bazı AI görevleri önemli miktarda bellek ve CPU gerektirir.

**Belirtiler:**
- Yavaş çalışma
- Dizüstü bilgisayar fanının yüksek sesle çalışması

**Olası Nedenler:**
- Büyük veri setleri veya modeller
- Sınırlı sistem kaynakları

**Çözümler:**
1. **Bir bulut platformu kullanın.**
   - Notebook'u Colab veya Azure Notebooks'a yükleyin.
2. **Veri seti boyutunu küçültün.**
   - Uygulama için örnek veri kullanın.
3. **Gereksiz programları kapatın.**
   - Sistem RAM'ini boşaltın.

---

## Ders Kitabı Web Sitesi Sorunları

### 9. Bölüm Yüklenmiyor

**Arka Plan:** Çevrimiçi ders kitabı, dersleri ve bölümleri görüntüler.

**Belirtiler:**
- Bir bölüm (örneğin, Transformers/BERT) eksik veya açılmıyor

**Bilinen Sorun:**  
- [Sorun #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. ders kitabı web sitesinde açılamıyor.” Dosya adı hatasından kaynaklanıyor (`READMEtransformers.md` yerine `README.md`).

**Çözümler:**
1. **Dosya adlandırma hatalarını kontrol edin.**  
   Eğer katkıda bulunuyorsanız, bölüm dosyalarının `README.md` olarak adlandırıldığından emin olun.
2. **Eksik dosyaları bildirin.**  
   Bölüm adı ve hata detaylarıyla bir GitHub sorunu açın.

---

## Katkı Sağlama Sorunları

### 10. PR Kabul Edilmiyor veya Yapılar Başarısız

**Arka Plan:** Katkılar testleri geçmeli ve yönergelere uygun olmalıdır.

**Belirtiler:**
- Pull request reddedildi
- CI/CD pipeline hataları

**Olası Nedenler:**
- Başarısız testler
- Kodlama standartlarına uyulmaması

**Çözümler:**
1. **Katkı yönergelerini okuyun.**
   - Depoya ait [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) dosyasını takip edin.
2. **Push yapmadan önce testleri yerel olarak çalıştırın.**
3. **Linting kurallarını veya biçimlendirme gereksinimlerini kontrol edin.**

---

## SSS

### Belirli modüller için nereden yardım alabilirim?
- Her modül genellikle kendi README dosyasına sahiptir. Kurulum ve kullanım ipuçları için oradan başlayın.

### Bir hata nasıl bildirilir veya özellik talep edilir?
- [GitHub Sorunu Açın](https://github.com/microsoft/AI-For-Beginners/issues/new) ve açık bir açıklama ile yeniden üretim adımlarını ekleyin.

### Sorunum listede yoksa yardım isteyebilir miyim?
- Evet! Önce mevcut sorunları arayın, eğer sorununuzu bulamazsanız yeni bir sorun oluşturun.

---

## Yardım Alma

- **Sorunları Kontrol Edin:** [GitHub Sorunları](https://github.com/microsoft/AI-For-Beginners/issues)
- **Sorular Sorun:** GitHub Discussions'ı kullanın veya bir sorun açın.
- **Topluluk:** Sohbet/forum seçenekleri için depo bağlantılarını inceleyin.

---

_Son Güncelleme: 2025-09-20_

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.