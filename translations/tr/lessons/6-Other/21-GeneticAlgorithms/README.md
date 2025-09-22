<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-26T07:31:34+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "tr"
}
-->
# Genetik Algoritmalar

## [Ders Öncesi Testi](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetik Algoritmalar** (GA), bir popülasyonun evrim yöntemlerini kullanarak verilen bir problem için en uygun çözümü elde etmeye dayanan bir **evrimsel yaklaşım** üzerine kuruludur. 1975 yılında [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) tarafından önerilmiştir.

Genetik Algoritmalar şu fikirlere dayanır:

* Problemin geçerli çözümleri **genler** olarak temsil edilebilir
* **Çaprazlama**, iki çözümü birleştirerek yeni bir geçerli çözüm elde etmemizi sağlar
* **Seçim**, bazı **uygunluk fonksiyonları** kullanılarak daha optimal çözümleri seçmek için kullanılır
* **Mutasyonlar**, optimizasyonu kararsız hale getirmek ve yerel minimumdan çıkmamızı sağlamak için tanıtılır

Bir Genetik Algoritma uygulamak istiyorsanız, şunlara ihtiyacınız var:

 * Problemin çözümlerini **genler** g∈Γ kullanarak kodlama yöntemini bulmak
 * Genler kümesi Γ üzerinde bir **uygunluk fonksiyonu** fit: Γ→**R** tanımlamak. Daha küçük fonksiyon değerleri daha iyi çözümlere karşılık gelir.
 * İki geni birleştirerek yeni bir geçerli çözüm elde etmek için bir **çaprazlama** mekanizması tanımlamak crossover: Γ<sup>2</sub>→Γ.
 * Bir **mutasyon** mekanizması tanımlamak mutate: Γ→Γ.

Birçok durumda, çaprazlama ve mutasyon, genleri sayısal diziler veya bit vektörleri olarak manipüle etmek için oldukça basit algoritmalardır.

Genetik algoritmanın belirli bir uygulaması durumdan duruma değişebilir, ancak genel yapı şu şekildedir:

1. Başlangıç popülasyonunu seçin G⊂Γ
2. Bu adımda gerçekleştirilecek işlemlerden birini rastgele seçin: çaprazlama veya mutasyon
3. **Çaprazlama**:
  * Rastgele iki gen seçin g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Çaprazlamayı hesaplayın g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Eğer fit(g)<fit(g<sub>1</sub>) veya fit(g)<fit(g<sub>2</sub>) ise - popülasyondaki ilgili geni g ile değiştirin.
4. **Mutasyon** - rastgele bir gen seçin g∈G ve bunu mutate(g) ile değiştirin
5. 2. adımdan itibaren tekrarlayın, uygunluk fonksiyonunun yeterince küçük bir değeri elde edilene kadar veya adım sayısı sınırına ulaşılana kadar.

## Tipik Görevler

Genetik Algoritmalarla genellikle çözülen görevler şunlardır:

1. Zamanlama optimizasyonu
1. Optimum yerleştirme
1. Optimum kesim
1. Tükenmeli aramayı hızlandırma

## ✍️ Alıştırmalar: Genetik Algoritmalar

Aşağıdaki not defterlerinde öğrenmeye devam edin:

[Bu not defterine](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) giderek Genetik Algoritmaların iki kullanım örneğini görebilirsiniz:

1. Hazine adil bölüşümü
1. 8 Vezir Problemi

## Sonuç

Genetik Algoritmalar, lojistik ve arama problemleri dahil olmak üzere birçok problemi çözmek için kullanılır. Bu alan, Psikoloji ve Bilgisayar Bilimi konularını birleştiren araştırmalardan ilham almıştır.

## 🚀 Meydan Okuma

"Genetik algoritmalar basit bir şekilde uygulanabilir, ancak davranışlarını anlamak zordur." [kaynak](https://wikipedia.org/wiki/Genetic_algorithm) Bir Sudoku bulmacasını çözmek gibi bir genetik algoritma uygulaması bulun ve bunun nasıl çalıştığını bir taslak veya akış diyagramı olarak açıklayın.

## [Ders Sonrası Testi](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Gözden Geçirme ve Kendi Kendine Çalışma

Genetik algoritmalarla eğitilmiş sinir ağlarını kullanarak bilgisayarların Super Mario oynamayı nasıl öğrenebileceğini anlatan [bu harika videoyu](https://www.youtube.com/watch?v=qv6UVOQ0F44) izleyin. Bilgisayarların bu tür oyunları oynamayı öğrenmesi hakkında daha fazla bilgi edineceğiz [bir sonraki bölümde](../22-DeepRL/README.md).

## [Ödev: Diofant Denklemi](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Amacınız, tam sayı kökleri olan **Diofant denklemini** çözmektir. Örneğin, a+2b+3c+4d=30 denklemini düşünün. Bu denklemi sağlayan tam sayı köklerini bulmanız gerekiyor.

*Bu ödev [bu gönderiden](https://habr.com/post/128704/) esinlenmiştir.*

İpuçları:

1. Köklerin [0;30] aralığında olduğunu düşünebilirsiniz
1. Gen olarak, kök değerlerinin listesini kullanmayı düşünebilirsiniz

Başlangıç noktası olarak [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) dosyasını kullanın.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.