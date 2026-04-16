# Etik ve Sorumlu Yapay Zeka

Bu kursu neredeyse tamamladınız ve umarım şu ana kadar yapay zekanın, verilerdeki ilişkileri bulmamıza ve insan davranışının bazı yönlerini taklit eden modelleri eğitmemize olanak tanıyan bir dizi resmi matematiksel yönteme dayandığını açıkça görüyorsunuzdur. Tarihin bu noktasında, yapay zekayı verilerden desenler çıkarmak ve bu desenleri yeni problemleri çözmek için uygulamak adına çok güçlü bir araç olarak görüyoruz.

## [Ders Öncesi Test](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Ancak, bilim kurgu hikayelerinde genellikle yapay zekanın insanlık için bir tehlike oluşturduğu senaryolarla karşılaşırız. Bu hikayeler genellikle bir tür yapay zeka isyanı etrafında döner; yapay zekanın insanlara karşı çıkmaya karar verdiği durumlar. Bu, yapay zekanın bir tür duyguya sahip olduğunu veya geliştiricileri tarafından öngörülemeyen kararlar alabildiğini ima eder.

Bu kursta öğrendiğimiz yapay zeka türü, büyük matris aritmetiğinden başka bir şey değildir. Problemlerimizi çözmemize yardımcı olan çok güçlü bir araçtır ve diğer güçlü araçlar gibi - hem iyi hem de kötü amaçlar için kullanılabilir. Önemli olan, bu aracın *yanlış kullanılabileceğidir*.

## Sorumlu Yapay Zeka İlkeleri

Yapay zekanın kazara veya kasıtlı olarak yanlış kullanılmasını önlemek için Microsoft, önemli [Sorumlu Yapay Zeka İlkeleri](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste) belirlemiştir. Bu ilkelerin temelini oluşturan kavramlar şunlardır:

* **Adalet**, *model önyargıları* gibi önemli bir problemle ilgilidir. Bu önyargılar, eğitim için önyargılı verilerin kullanılmasıyla ortaya çıkabilir. Örneğin, bir kişinin yazılım geliştirici işine girme olasılığını tahmin etmeye çalıştığımızda, modelin erkeklere daha fazla öncelik verme olasılığı yüksektir - çünkü eğitim veri seti muhtemelen erkeklere yönelik bir önyargıya sahipti. Eğitim verilerini dikkatlice dengelemeli, modeli incelemeli ve önyargıları önlemek için daha alakalı özellikleri dikkate aldığından emin olmalıyız.
* **Güvenilirlik ve Güvenlik**. Yapay zeka modelleri doğası gereği hata yapabilir. Bir sinir ağı olasılıkları döndürür ve karar verirken bunu dikkate almamız gerekir. Her modelin belirli bir hassasiyeti ve hatırlama oranı vardır ve yanlış tavsiyelerin neden olabileceği zararı önlemek için bunu anlamamız gerekir.
* **Gizlilik ve Güvenlik**, yapay zekaya özgü bazı sonuçlara sahiptir. Örneğin, bir modeli eğitmek için bazı verileri kullandığımızda, bu veriler bir şekilde modelin içine "entegre" olur. Bir yandan bu güvenlik ve gizliliği artırır, diğer yandan modelin hangi verilerle eğitildiğini hatırlamamız gerekir.
* **Kapsayıcılık**, yapay zekayı insanları değiştirmek için değil, insanları desteklemek ve işimizi daha yaratıcı hale getirmek için inşa ettiğimiz anlamına gelir. Bu aynı zamanda adaletle de ilgilidir, çünkü az temsil edilen topluluklarla çalışırken topladığımız veri setlerinin çoğu muhtemelen önyargılı olacaktır ve bu toplulukların yapay zeka tarafından doğru bir şekilde ele alındığından emin olmamız gerekir.
* **Şeffaflık**. Bu, yapay zekanın kullanıldığını her zaman açıkça belirttiğimizden emin olmayı içerir. Ayrıca, mümkün olduğunda, *yorumlanabilir* yapay zeka sistemleri kullanmak isteriz.
* **Hesap Verebilirlik**. Yapay zeka modelleri bazı kararlar verdiğinde, bu kararların sorumluluğunun kimde olduğu her zaman net değildir. Yapay zeka kararlarının sorumluluğunun nerede olduğunu anladığımızdan emin olmamız gerekir. Çoğu durumda, önemli kararlar alınırken insanları sürece dahil etmek isteriz, böylece gerçek insanlar sorumlu tutulabilir.

## Sorumlu Yapay Zeka Araçları

Microsoft, bir dizi araç içeren [Sorumlu Yapay Zeka Araç Kutusu](https://github.com/microsoft/responsible-ai-toolbox) geliştirmiştir:

* Yorumlanabilirlik Panosu (InterpretML)
* Adalet Panosu (FairLearn)
* Hata Analizi Panosu
* Sorumlu Yapay Zeka Panosu, şunları içerir:

   - EconML - Nedensel Analiz için bir araç, "ne olurdu" sorularına odaklanır
   - DiCE - Karşıt Analiz için bir araç, modelin kararını etkilemek için hangi özelliklerin değiştirilmesi gerektiğini görmenizi sağlar

Yapay Zeka Etiği hakkında daha fazla bilgi için, ödevler içeren Makine Öğrenimi Müfredatındaki [bu derse](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) göz atabilirsiniz.

## Gözden Geçirme ve Kendi Kendine Çalışma

Sorumlu yapay zeka hakkında daha fazla bilgi edinmek için bu [Öğrenme Yolunu](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) tamamlayın.

## [Ders Sonrası Test](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.