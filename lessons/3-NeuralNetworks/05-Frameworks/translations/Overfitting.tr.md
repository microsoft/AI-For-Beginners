# Aşırı Öğrenme

Aşırı öğrenme, makine öğrenmesinde son derece önemli bir kavramdır ve bunu doğru yapmak çok önemlidir!

Aşağıdaki 5 noktayı (aşağıdaki grafiklerde `x` ile temsil edilen) yaklaşıklama problemini göz önünde bulundurun:

![doğrusal](../../images/overfit1.jpg) | ![aşırı öğrenme](../../images/overfit2.jpg)
-------------------------|--------------------------
**Doğrusal model, 2 parametre** | **Doğrusal olmayan model, 7 parametre**
Eğitim hatası = 5.3 | Eğitim hatası = 0
Geçerleme hatası = 5.1 | Geçerleme hatası = 20

* Solda iyi bir düz doğru yaklaşımı görüyoruz. Parametre sayısı yeterli olduğundan, model nokta dağılımının arkasındaki fikri doğru alır.
* Sağdaki model çok güçlüdür. Sadece 5 noktamız ve modelin 7 parametresi olduğu için, kendisini tüm noktalardan geçecek şekilde ayarlayabilir ve hatayı 0 yapar. Ancak bu, modelin verinin arkasındaki doğru örüntüyü anlamasını engeller, dolayısıyla geçerleme hatası çok yüksektir.

Modelin zenginliği (parametre sayısı) ile eğitim örneklerinin sayısı arasında doğru bir denge kurmak çok önemlidir.

## Aşırı öğrenme neden olur?

  * Yeterli eğitim verisi yoktur.
  * Model çok güçlüdür.
  * Girdi verisinde çok fazla gürültü vardır.

## Aşırı öğrenme nasıl tespit edilir?

Yukarıdaki şekilden de görebileceğiniz gibi, aşırı öğrenme, çok düşük bir eğitim hatası ve yüksek bir geçerleme hatası ile tespit edilebilir. Normalde eğitim sırasında hem eğitim hem de geçerleme hatalarının azalmaya başladığını görürüz ve ardından bir noktada geçerleme hatası azalmayı durdurabilir ve yükselmeye başlayabilir. Bu, aşırı öğrenmenin bir işaretidir ve muhtemelen bu noktada eğitimi durdurmamız (veya en azından modelin anlık görüntüsünü almamız) gerektiğinin göstergesi olacaktır.

![aşırı öğrenme](../../images/Overfitting.png)

## Aşırı öğrenme nasıl önlenir?

Aşırı öğrenmenin meydana geldiğini görüyorsanız, aşağıdakilerden birini yapabilirsiniz:

 * Eğitim verisinin miktarını artırın
 * Modelin karmaşıklığını azaltın
 * [Hattan düşürme](../../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout) gibi bazı [düzenlileştirme teknikleri](../../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), ki daha sonra ele alacağız, kullanın.

## Aşırı öğrenme ve yanlılık-varyans ödünleşmesi

Aşırı öğrenme aslında istatistikte [yanlılık-varyans ödünleşmesi](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff) adı verilen daha genel bir sorundur. Modelimizde olası hata kaynaklarını göz önüne alırsak iki tür hata görebiliriz:

* **Yanlılık hataları**, algoritmamızın eğitim verileri arasındaki ilişkiyi doğru şekilde yakalayamamasından kaynaklanır. Modelimizin yeterince güçlü olmamasından (**eksik öğrenme**) kaynaklanabilir.
* **Varyans hataları**, modelin anlamlı ilişki yerine girdi verilerindeki gürültüyü yaklaşıklamasından (**aşırı öğrenme**) kaynaklanır.

Eğitim esnasında, yanlılık hatası azalır (modelimiz verilere yaklaşmayı öğrenirken) ve varyans hatası artar. Aşırı öğrenmeyi önlemek için eğitimi - manuel olarak (aşırı öğrenmeyi tespit ettiğimizde) veya otomatik olarak (düzenlileştirmeyi katarak) durdurmak önemlidir.

## Vargılar

Bu derste, en popüler iki YZ çerçevesi olan TensorFlow ve PyTorch için çeşitli API'ler arasındaki farkları öğrendiniz. Ayrıca, çok önemli bir konuyu da öğrendiniz, aşırı öğrenme.

## 🚀 Kendini Sınama

Ekli defterlerde alt kısımda 'görevler'i bulacaksınız; defterler üzerinden çalışın ve görevleri tamamlayın.

## [Ders sonrası sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/205)

## Gözden Geçirme ve Bireysel Çalışma

Aşağıdaki konularda biraz araştırma yapın:

- TensorFlow
- PyTorch
- Aşırı öğrenme

Kendinize şu soruları sorun:

- TensorFlow ve PyTorch arasındaki fark nedir?
- Aşırı öğrenme ile eksik öğrenme arasındaki fark nedir?

## [Ödev](../lab/README.md)

Bu laboratuvar çalışmasında, PyTorch veya TensorFlow kullanarak tek ve çok katmanlı tam bağlı ağları kullanarak iki tane sınıflandırma problemini çözmeniz isteniyor.

* [Talimatlar](../lab/README.md)
* [Not defteri](../lab/LabFrameworks.ipynb)
