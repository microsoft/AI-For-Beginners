# Genetik Algoritmalar

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Genetik Algoritmalar** (GA), bir **evrimsel yaklaşım** temelinde yapay zeka (AI) için geliştirilmiş bir yöntemdir; burada bir popülasyonun evrim yöntemleri, belirli bir problem için optimal bir çözüm elde etmek amacıyla kullanılır. İlk olarak 1975 yılında [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) tarafından önerilmiştir.

Genetik Algoritmalar aşağıdaki fikirlere dayanır:

* Problemin geçerli çözümleri **genler** olarak temsil edilebilir
* **Çaprazlama** iki çözümü bir araya getirerek yeni bir geçerli çözüm elde etmemizi sağlar
* **Seçim**, bazı **uygunluk fonksiyonu** kullanarak daha optimal çözümleri seçmek için kullanılır
* **Mutasyonlar**, optimizasyonu istikrarsızlaştırmak ve yerel minimumdan çıkmamızı sağlamak için tanıtılır

Bir Genetik Algoritma uygulamak istiyorsanız, aşağıdakilere ihtiyacınız var:

* Problemin çözümlerini **genler** g∈Γ kullanarak kodlama yöntemini bulmak
* Genler kümesi Γ üzerinde **uygunluk fonksiyonu** fit: Γ→**R** tanımlamak. Daha küçük fonksiyon değerleri, daha iyi çözümlerle ilişkilidir.
* İki geni bir araya getirerek yeni bir geçerli çözüm elde etmek için **çaprazlama** mekanizmasını tanımlamak crossover: Γ<sup>2</sub>→Γ.
* **Mutasyon** mekanizmasını tanımlamak mutate: Γ→Γ.

Birçok durumda, çaprazlama ve mutasyon, genleri sayısal diziler veya bit vektörleri olarak manipüle etmek için oldukça basit algoritmalardır.

Genetik algoritmanın özel uygulaması duruma göre değişiklik gösterebilir, ancak genel yapı şu şekildedir:

1. Başlangıç popülasyonu G⊂Γ seçin
2. Bu adımda gerçekleştirilecek işlemlerden birini rastgele seçin: çaprazlama veya mutasyon
3. **Çaprazlama**:
   * Rastgele iki gen g<sub>1</sub>, g<sub>2</sub> ∈ G seçin
   * Çaprazlama g=crossover(g<sub>1</sub>,g<sub>2</sub>) hesaplayın
   * Eğer fit(g)<fit(g<sub>1</sub>) veya fit(g)<fit(g<sub>2</sub>) ise, popülasyondaki karşılık gelen geni g ile değiştirin.
4. **Mutasyon** - rastgele bir gen g∈G seçin ve onu mutate(g) ile değiştirin
5. Yeterince küçük bir fit değeri elde edene kadar veya adım sayısı sınırına ulaşana kadar 2. adımdan tekrarlayın.

## Tipik Görevler

Genetik Algoritmalar tarafından genellikle çözülen görevler şunlardır:

1. Program optimizasyonu
1. Optimal paketleme
1. Optimal kesme
1. Kapsamlı aramanın hızlandırılması

## ✍️ Alıştırmalar: Genetik Algoritmalar

Öğreniminizi aşağıdaki defterlerde devam ettirin:

Genetik Algoritmaların kullanımına dair iki örnek görmek için [bu deftere](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) gidin:

1. Hazine adaletli paylaşımı
1. 8 Kraliçe Problemi

## Sonuç

Genetik Algoritmalar, lojistik ve arama problemleri dahil birçok problemi çözmek için kullanılmaktadır. Bu alan, Psikoloji ve Bilgisayar Bilimi konularını birleştiren araştırmalardan ilham almıştır.

## 🚀 Meydan Okuma

"Genetik algoritmalar uygulaması kolaydır, ancak davranışlarını anlamak zordur." [kaynak](https://wikipedia.org/wiki/Genetic_algorithm) Bir Sudoku bulmacasını çözmek gibi bir genetik algoritma uygulaması bulmak için araştırma yapın ve nasıl çalıştığını bir taslak veya akış diyagramı olarak açıklayın.

## [Ders sonrası quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Gözden Geçirme & Kendi Kendine Çalışma

Bilgisayarların genetik algoritmalarla eğitilmiş sinir ağları kullanarak Super Mario oynamayı nasıl öğrenebileceği hakkında konuşan [bu harika videoyu](https://www.youtube.com/watch?v=qv6UVOQ0F44) izleyin. Bilgisayarların böyle oyunlar oynamayı öğrenmesi hakkında daha fazla bilgi edineceğiz [bir sonraki bölümde](../22-DeepRL/README.md).

## [Ödev: Diophantine Denklemi](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Amacınız, tam sayı kökleri olan **Diophantine denklemi** olarak bilinen bir denklemi çözmektir. Örneğin, a+2b+3c+4d=30 denklemini düşünün. Bu denklemi sağlayan tam sayı köklerini bulmanız gerekiyor.

*Bu ödev [bu yazıdan](https://habr.com/post/128704/) ilham alınmıştır.*

İpuçları:

1. Köklerin [0;30] aralığında olduğunu düşünebilirsiniz
1. Bir gen olarak, kök değerleri listesini kullanmayı düşünün

[Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) dosyasını başlangıç noktası olarak kullanın.

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen dikkate alınız. Belgenin orijinal hali, otorite kaynağı olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucu ortaya çıkan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.