<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-26T07:39:47+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "tr"
}
-->
# Kodu Çalıştırma Yöntemleri

Bu müfredat, çalıştırılabilir birçok örnek ve laboratuvar içermektedir ve bunları çalıştırmak isteyeceksiniz. Bunu yapmak için, bu müfredatın bir parçası olarak sağlanan Jupyter Notebooks'ta Python kodu çalıştırma yeteneğine ihtiyacınız var. Kodu çalıştırmak için birkaç seçeneğiniz var:

## Kendi Bilgisayarınızda Yerel Olarak Çalıştırma

Kodu kendi bilgisayarınızda yerel olarak çalıştırmak için bir Python sürümünün yüklü olması gerekir. Şahsen, **[miniconda](https://conda.io/en/latest/miniconda.html)** yüklemenizi öneririm - bu, farklı Python **sanal ortamlarını** destekleyen `conda` paket yöneticisini içeren oldukça hafif bir kurulumdur.

Miniconda'yı yükledikten sonra, bu kurs için kullanılacak bir sanal ortam oluşturmak ve depoyu klonlamak için şu adımları izleyin:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Python Uzantısı ile Visual Studio Code Kullanımı

Muhtemelen müfredatı kullanmanın en iyi yolu, [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) ile [Python Uzantısı](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) kullanarak açmaktır.

> **Not**: Depoyu klonlayıp VS Code'da açtığınızda, Python uzantılarını yüklemenizi otomatik olarak önerecektir. Yukarıda açıklandığı gibi miniconda'yı da yüklemeniz gerekecektir.

> **Not**: VS Code, depoyu bir konteyner içinde yeniden açmanızı önerirse, yerel Python kurulumunu kullanmak için bunu reddetmeniz gerekir.

### Tarayıcıda Jupyter Kullanımı

Jupyter ortamını kendi bilgisayarınızda tarayıcı üzerinden de kullanabilirsiniz. Aslında, hem klasik Jupyter hem de Jupyter Hub, otomatik tamamlama, kod vurgulama vb. özelliklerle oldukça kullanışlı bir geliştirme ortamı sunar.

Jupyter'i yerel olarak başlatmak için, kursun dizinine gidin ve şu komutları çalıştırın:

```bash
jupyter notebook
```  
veya  
```bash
jupyterhub
```  
Daha sonra herhangi bir `.ipynb` dosyasına gidip, açabilir ve çalışmaya başlayabilirsiniz.

### Konteynerde Çalıştırma

Python kurulumuna bir alternatif, kodu bir konteyner içinde çalıştırmaktır. Depomuz, bu depo için bir konteynerin nasıl oluşturulacağını açıklayan özel bir `.devcontainer` klasörü içerdiğinden, VS Code size kodu bir konteyner içinde yeniden açmayı teklif edecektir. Bu, Docker kurulumunu gerektirir ve daha karmaşık olabilir, bu nedenle bunu daha deneyimli kullanıcılara öneriyoruz.

## Bulutta Çalıştırma

Python'u yerel olarak kurmak istemiyorsanız ve bazı bulut kaynaklarına erişiminiz varsa, kodu bulutta çalıştırmak iyi bir alternatif olabilir. Bunu yapmanın birkaç yolu vardır:

* **[GitHub Codespaces](https://github.com/features/codespaces)** kullanarak. Bu, GitHub'da sizin için oluşturulan ve VS Code tarayıcı arayüzü üzerinden erişilebilen bir sanal ortamdır. Codespaces erişiminiz varsa, depodaki **Code** düğmesine tıklayıp bir codespace başlatabilir ve hemen çalışmaya başlayabilirsiniz.
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** kullanarak. [Binder](https://mybinder.org), GitHub'daki bazı kodları test etmek isteyen kişiler için bulutta ücretsiz hesaplama kaynakları sağlar. Ana sayfada depoyu Binder'da açmak için bir düğme vardır - bu, sizi hızla Binder sitesine yönlendirecek, temel konteyneri oluşturacak ve Jupyter web arayüzünü sorunsuz bir şekilde başlatacaktır.

> **Not**: Kötüye kullanımı önlemek için, Binder bazı web kaynaklarına erişimi engellemiştir. Bu, modelleri ve/veya veri setlerini genel internetten çeken bazı kodların çalışmasını engelleyebilir. Bazı alternatif çözümler bulmanız gerekebilir. Ayrıca, Binder tarafından sağlanan hesaplama kaynakları oldukça temel düzeydedir, bu nedenle özellikle daha karmaşık derslerde eğitim yavaş olacaktır.

## GPU ile Bulutta Çalıştırma

Bu müfredattaki bazı ileri düzey dersler, GPU desteğinden büyük ölçüde faydalanacaktır, çünkü aksi takdirde eğitim süreci oldukça yavaş olacaktır. Özellikle [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) veya kurumunuz aracılığıyla buluta erişiminiz varsa, aşağıdaki seçenekleri değerlendirebilirsiniz:

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) oluşturun ve Jupyter üzerinden bağlanın. Daha sonra depoyu doğrudan makineye klonlayabilir ve öğrenmeye başlayabilirsiniz. NC serisi sanal makineler GPU desteğine sahiptir.

> **Not**: Azure for Students dahil bazı abonelikler, GPU desteğini varsayılan olarak sağlamaz. Teknik destek talebiyle ek GPU çekirdekleri talep etmeniz gerekebilir.

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) oluşturun ve oradaki Notebook özelliğini kullanın. [Bu video](https://azure-for-academics.github.io/quickstart/azureml-papers/), bir depoyu Azure ML not defterine nasıl klonlayacağınızı ve kullanmaya başlayacağınızı gösterir.

Ayrıca, ücretsiz GPU desteği sunan Google Colab'i kullanabilir ve Jupyter Notebooks'u oraya yükleyerek tek tek çalıştırabilirsiniz.

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.