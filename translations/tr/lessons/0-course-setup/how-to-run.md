# Kodu Çalıştırma Yöntemleri

Bu müfredat, çalıştırmak isteyeceğiniz birçok çalıştırılabilir örnek ve laboratuvar içermektedir. Bunu yapmak için, bu müfredatın bir parçası olarak sağlanan Jupyter Not Defterlerinde Python kodunu çalıştırabilme yeteneğine sahip olmanız gerekmektedir. Kodu çalıştırmak için birkaç seçeneğiniz var:

## Bilgisayarınızda Yerel Olarak Çalıştırma

Kodu bilgisayarınızda yerel olarak çalıştırmak için, bazı Python sürümlerinin kurulu olması gerekmektedir. Kişisel olarak **[miniconda](https://conda.io/en/latest/miniconda.html)** kurulumunu öneriyorum - bu, farklı Python **sanallaştırılmış ortamları** için `conda` paket yöneticisini destekleyen oldukça hafif bir kurulumdur.

Miniconda'yı kurduktan sonra, depoyu klonlamanız ve bu kurs için kullanılacak bir sanal ortam oluşturmanız gerekmektedir:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Python Uzantısıyla Visual Studio Code Kullanma

Müfredatı kullanmanın en iyi yolu, onu [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) içinde [Python Uzantısı](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) ile açmaktır.

> **Not**: Depoyu klonladıktan ve dizini VS Code'da açtıktan sonra, Python uzantılarını kurmanızı otomatik olarak önerecektir. Ayrıca yukarıda açıklandığı gibi miniconda'yı da kurmanız gerekecektir.

> **Not**: Eğer VS Code, depoyu konteynerde yeniden açmanızı önerirse, yerel Python kurulumunu kullanmak için bunu reddetmeniz gerekmektedir.

### Tarayıcıda Jupyter Kullanma

Ayrıca, kendi bilgisayarınızdaki tarayıcıdan Jupyter ortamını kullanabilirsiniz. Aslında, hem klasik Jupyter hem de Jupyter Hub, otomatik tamamlama, kod vurgulama vb. ile oldukça uygun bir geliştirme ortamı sunmaktadır.

Jupyter'i yerel olarak başlatmak için, kursun dizinine gidin ve şu komutu çalıştırın:

```bash
jupyter notebook
```
veya
```bash
jupyterhub
```
Daha sonra, bu repo için bir konteyner oluşturma talimatlarını veren herhangi bir `.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in container. Since our repository contains special `.devcontainer` klasörüne gidebilirsiniz; VS Code, kodu konteynerde yeniden açmanızı teklif edecektir. Bu, Docker kurulumu gerektirecek ve ayrıca daha karmaşık olacaktır, bu nedenle bunu daha deneyimli kullanıcılara öneriyoruz.

## Bulutta Çalıştırma

Eğer Python'u yerel olarak kurmak istemiyorsanız ve bazı bulut kaynaklarına erişiminiz varsa - bulutta kodu çalıştırmak iyi bir alternatif olacaktır. Bunu yapmanın birkaç yolu vardır:

* **[GitHub Codespaces](https://github.com/features/codespaces)** kullanarak, bu sizin için GitHub'da oluşturulmuş sanal bir ortamdır ve VS Code tarayıcı arayüzü üzerinden erişilebilir. Eğer Codespaces erişiminiz varsa, repo içinde **Code** butonuna tıklayarak bir codespace başlatabilir ve hızla çalışmaya başlayabilirsiniz.
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** kullanarak. [Binder](https://mybinder.org), sizin gibi insanların GitHub'da bazı kodları denemesi için sağlanan ücretsiz hesaplama kaynaklarıdır. Ana sayfada depoyu Binder'da açmak için bir buton bulunmaktadır - bu, sizi hızlı bir şekilde binder sitesine yönlendirecek ve arka planda gerekli konteyneri oluşturup Jupyter web arayüzünü sizin için başlatacaktır.

> **Not**: Suistimali önlemek için, Binder bazı web kaynaklarına erişimi engellemiştir. Bu, kamu internetinden model ve/veya veri setleri çeken bazı kodların çalışmasını engelleyebilir. Bazı çözümler bulmanız gerekebilir. Ayrıca, Binder tarafından sağlanan hesaplama kaynakları oldukça temel olduğu için, eğitim süreci yavaş olacaktır, özellikle daha karmaşık derslerde.

## Bulutta GPU ile Çalıştırma

Bu müfredattaki bazı sonraki dersler, GPU desteğinden büyük ölçüde yararlanacaktır, çünkü aksi takdirde eğitim acı verici derecede yavaş olacaktır. Özellikle [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) veya kurumunuz aracılığıyla buluta erişiminiz varsa, takip edebileceğiniz birkaç seçenek vardır:

* [Veri Bilimi Sanal Makinesi](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) oluşturun ve buna Jupyter üzerinden bağlanın. Daha sonra repoyu doğrudan makineye klonlayabilir ve öğrenmeye başlayabilirsiniz. NC serisi VM'ler GPU desteğine sahiptir.

> **Not**: Bazı abonelikler, Azure for Students dahil olmak üzere, kutudan çıktığı gibi GPU desteği sağlamaz. Ek GPU çekirdekleri talep etmeniz gerekebilir.

* [Azure Makine Öğrenimi Çalışma Alanı](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) oluşturun ve ardından orada Not Defteri özelliğini kullanın. [Bu video](https://azure-for-academics.github.io/quickstart/azureml-papers/) bir depoyu Azure ML not defterine nasıl klonlayacağınızı ve kullanmaya nasıl başlayacağınızı göstermektedir.

Ayrıca, bazı ücretsiz GPU desteği ile gelen Google Colab'ı da kullanabilirsiniz ve oraya Jupyter Not Defterlerini yükleyerek bunları tek tek çalıştırabilirsiniz.

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk konusunda çaba göstersek de, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen dikkate alınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucu ortaya çıkan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.