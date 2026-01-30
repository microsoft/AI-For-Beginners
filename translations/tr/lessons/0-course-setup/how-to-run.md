# Kodu Çalıştırma

Bu müfredat, çalıştırmak isteyebileceğiniz birçok yürütülebilir örnek ve laboratuvar içerir. Bunu yapmak için, bu müfredatın parçası olarak sağlanan Jupyter Not defterlerinde Python kodu çalıştırma yeteneğine ihtiyacınız vardır. Kodu çalıştırmak için birkaç seçeneğiniz vardır:

## Bilgisayarınızda Yerel Olarak Çalıştırma

Kodu bilgisayarınızda yerel olarak çalıştırmak için Python kurulumu gereklidir. Tavsiye edilenlerden biri **[miniconda](https://conda.io/en/latest/miniconda.html)** yüklemektir - bu, farklı Python **sanal ortamları** için `conda` paket yöneticisini destekleyen oldukça hafif bir kurulumdur.

Miniconda'yı yükledikten sonra, depoyu klonlayın ve bu ders için kullanılacak bir sanal ortam oluşturun:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code ile Python Eklentisi Kullanımı

Bu müfredat, en iyi şekilde [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) içindeki [Python Eklentisi](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) ile açıldığında kullanılır.

> **Not**: Depoyu klonlayıp VS Code’da dizini açtıktan sonra, Python eklentilerini yüklemenizi otomatik olarak önerecektir. Ayrıca yukarıda anlatıldığı gibi miniconda'yı da yüklemeniz gerekecektir.

> **Not**: VS Code, depoyu bir konteyner içinde yeniden açmanızı önerirse, yerel Python kurulumunu kullanmak için bunu reddetmelisiniz.

### Tarayıcıda Jupyter Kullanımı

Ayrıca kendi bilgisayarınızda tarayıcıdan Jupyter ortamı kullanabilirsiniz. Hem klasik Jupyter hem de JupyterHub, otomatik tamamlama, kod vurgulama gibi özelliklerle kullanışlı bir geliştirme ortamı sağlar.

Jupyter'ı yerel olarak başlatmak için ders dizinine gidin ve şunu yürütün:

```bash
jupyter notebook
```
 veya
```bash
jupyterhub
```
 Daha sonra herhangi bir `.ipynb` dosyasına gidip açabilir ve çalışmaya başlayabilirsiniz.

### Konteynerde Çalıştırma

Python kurulumu yapmak yerine, kodu bir konteynerde çalıştırmak bir alternatiftir. Depomuz, bu depo için nasıl bir konteyner oluşturulacağını gösteren özel bir `.devcontainer` klasörü sağlar ve VS Code, kodu bir konteynerde yeniden açma fırsatı sunar. Bunun için Docker kurulumu gerekir ve biraz daha karmaşıktır, bu yüzden daha deneyimli kullanıcılara tavsiye edilir.

## Bulutta Çalıştırma

Python'u yerel olarak kurmak istemiyorsanız ve bazı bulut kaynaklarına erişiminiz varsa - kodu bulutta çalıştırmak iyi bir alternatif olabilir. Bunu yapmanın birkaç yolu vardır:

* **[GitHub Codespaces](https://github.com/features/codespaces)** kullanmak, GitHub üzerinde sizin için oluşturulan, VS Code tarayıcı arayüzü ile erişilebilen sanal bir ortamdır. Eğer Codespaces erişiminiz varsa, depoda **Code** düğmesine tıklayabilir, bir codespace başlatabilir ve kısa sürede çalışmaya başlayabilirsiniz.
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** kullanmak. [Binder](https://mybinder.org), GitHub’daki bazı kodları denemeniz için bulutta ücretsiz hesaplama kaynakları sunar. Ana sayfada depoyu Binder'da açmak için bir düğme vardır - bu sizi hızla binder sitesine götürür, alt yapısında bir konteyner oluşturur ve sorunsuzca Jupyter web arayüzünü başlatır.

> **Not**: Kötüye kullanımı önlemek için, Binder bazı web kaynaklarına erişimi engellemiştir. Bu, modelleri ve/veya veri setlerini genel İnternetten çeken bazı kodların çalışmasını engelleyebilir. Bazı çözümler bulmanız gerekebilir. Ayrıca, Binder tarafından sağlanan hesaplama kaynakları oldukça temel seviyededir, bu nedenle eğitim özellikle daha karmaşık sonraki derslerde yavaş olacaktır.

## GPU ile Bulutta Çalıştırma

Bu müfredattaki bazı ileri dersler GPU desteğinden çok fayda sağlar. Örneğin model eğitimi aksi halde çok yavaş olabilir. Özellikle [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) veya kurumunuz aracılığıyla buluta erişiminiz varsa, takip edebileceğiniz birkaç seçenek vardır:

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) oluşturun ve Jupyter üzerinden bağlanın. Depoyu doğrudan bu makineye klonlayabilir ve öğrenmeye başlayabilirsiniz. NC-serisi VM’ler GPU desteğine sahiptir.

> **Not**: Azure for Students dahil bazı abonelikler kutudan çıktığı gibi GPU desteği sağlamaz. Ek GPU çekirdeği için teknik destek talebi yapmanız gerekebilir.

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) oluşturun ve oradaki Notebook özelliğini kullanın. [Bu video](https://azure-for-academics.github.io/quickstart/azureml-papers/) bir depoyu Azure ML dizinine nasıl klonlayacağınızı ve kullanmaya başlayacağınızı gösterir.

Ayrıca Google Colab kullanabilirsiniz; ücretsiz GPU desteğiyle gelir ve Jupyter Not defterlerini oraya yükleyip tek tek çalıştırabilirsiniz.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çeviri kullanımı sonucunda oluşabilecek herhangi bir yanlış anlama veya yorumlama için sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->