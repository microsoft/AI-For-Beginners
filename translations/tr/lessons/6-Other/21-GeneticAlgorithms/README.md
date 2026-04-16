# Genetik Algoritmalar

## [Ders Öncesi Testi](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetik Algoritmalar** (GA), bir problemin optimal çözümünü elde etmek için bir popülasyonun evrim yöntemlerini kullanan **evrimsel bir yaklaşım**a dayalıdır. 1975 yılında [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) tarafından önerilmiştir.

Genetik Algoritmalar şu fikirlere dayanır:

* Problemin geçerli çözümleri **genler** olarak temsil edilebilir
* **Çaprazlama**, iki çözümü birleştirerek yeni bir geçerli çözüm elde etmemizi sağlar
* **Seçim**, bazı **uygunluk fonksiyonları** kullanılarak daha optimal çözümleri seçmek için kullanılır
* **Mutasyonlar**, optimizasyonu istikrarsızlaştırmak ve yerel minimumdan çıkmamızı sağlamak için eklenir

Bir Genetik Algoritma uygulamak istiyorsanız, aşağıdakilere ihtiyacınız var:

 * Problemin çözümlerini **genler** g&in;&Gamma; kullanarak kodlama yöntemini bulmak
 * Genler kümesi &Gamma; üzerinde **uygunluk fonksiyonu** fit: &Gamma;&rightarrow;**R** tanımlamak. Daha küçük fonksiyon değerleri daha iyi çözümlere karşılık gelir.
 * İki geni birleştirerek yeni bir geçerli çözüm elde etmek için **çaprazlama** mekanizmasını tanımlamak crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * **Mutasyon** mekanizmasını tanımlamak mutate: &Gamma;&rightarrow;&Gamma;.

Çoğu durumda, çaprazlama ve mutasyon, genleri sayısal diziler veya bit vektörleri olarak manipüle eden oldukça basit algoritmalardır.

Genetik algoritmanın belirli bir uygulaması durumdan duruma değişebilir, ancak genel yapı şu şekildedir:

1. Başlangıç popülasyonunu seç G&subset;&Gamma;
2. Bu adımda gerçekleştirilecek işlemlerden birini rastgele seç: çaprazlama veya mutasyon
3. **Çaprazlama**:
  * Rastgele iki gen seç g<sub>1</sub>, g<sub>2</sub> &in; G
  * Çaprazlama hesapla g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Eğer fit(g)<fit(g<sub>1</sub>) veya fit(g)<fit(g<sub>2</sub>) ise - popülasyondaki ilgili geni g ile değiştir.
4. **Mutasyon** - rastgele bir gen seç g&in;G ve onu mutate(g) ile değiştir
5. fit değerinin yeterince küçük bir değere ulaşmasına veya adım sayısı sınırına ulaşılana kadar 2. adımdan itibaren tekrarla.

## Tipik Görevler

Genetik Algoritmalar ile genellikle çözülen görevler şunlardır:

1. Takvim optimizasyonu
1. Optimal yerleştirme
1. Optimal kesim
1. Kapsamlı aramayı hızlandırma

## ✍️ Alıştırmalar: Genetik Algoritmalar

Aşağıdaki not defterlerinde öğrenmeye devam edin:

Genetik Algoritmaların kullanımına dair iki örneği görmek için [bu not defterine](Genetic.ipynb) gidin:

1. Hazineyi adil bölme
1. 8 Kraliçe Problemi

## Sonuç

Genetik Algoritmalar, lojistik ve arama problemleri dahil birçok problemi çözmek için kullanılır. Bu alan, Psikoloji ve Bilgisayar Bilimi konularını birleştiren araştırmalardan ilham almıştır.

## 🚀 Meydan Okuma

"Genetik algoritmaların uygulanması basittir, ancak davranışlarını anlamak zordur." [kaynak](https://wikipedia.org/wiki/Genetic_algorithm) Sudoku bulmacası çözmek gibi bir genetik algoritma uygulaması bulun ve nasıl çalıştığını bir taslak veya akış diyagramı olarak açıklayın.

## [Ders Sonrası Testi](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Gözden Geçirme ve Kendi Kendine Çalışma

Genetik algoritmalarla eğitilmiş sinir ağlarını kullanarak bilgisayarların Super Mario oynamayı nasıl öğrenebileceğini anlatan [bu harika videoyu](https://www.youtube.com/watch?v=qv6UVOQ0F44) izleyin. Bilgisayarların bu tür oyunları oynamayı öğrenmesi hakkında daha fazla bilgi edineceğiz [bir sonraki bölümde](../22-DeepRL/README.md).

## [Ödev: Diofant Denklemi](Diophantine.ipynb)

Amacınız, tam sayı kökleri olan **Diofant denklemini** çözmek. Örneğin, a+2b+3c+4d=30 denklemini düşünün. Bu denklemi sağlayan tam sayı köklerini bulmanız gerekiyor.

*Bu ödev [bu gönderiden](https://habr.com/post/128704/) ilham alınmıştır.*

İpuçları:

1. Köklerin [0;30] aralığında olduğunu düşünebilirsiniz
1. Gen olarak kök değerlerinin listesini kullanmayı düşünün

Başlangıç noktası olarak [Diophantine.ipynb](Diophantine.ipynb) dosyasını kullanın.

---

