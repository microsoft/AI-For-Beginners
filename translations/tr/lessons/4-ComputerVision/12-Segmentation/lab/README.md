# İnsan Vücudu Segmentasyonu

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) için laboratuvar ödevi.

## Görev

Video prodüksiyonunda, örneğin hava durumu tahminlerinde, bir insan görüntüsünü kameradan kesip başka bir görüntünün üzerine yerleştirmemiz sıkça gerekmektedir. Bu genellikle, bir insanın tek renkli bir arka plan önünde çekildiği ve ardından bu arka planın kaldırıldığı **chroma key** teknikleri kullanılarak yapılır. Bu laboratuvar çalışmasında, insan siluetini kesmek için bir sinir ağı modeli eğiteceğiz.

## Veri Seti

Kaggle'dan [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) veri setini kullanacağız. Veri setini Kaggle'dan manuel olarak indirin.

## Not Defterini Açma

Laboratuvara [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb) dosyasını açarak başlayın.

## Önemli Nokta

Vücut segmentasyonu, insanların görüntüleriyle yapabileceğimiz yaygın görevlerden sadece biridir. Diğer önemli görevler arasında **iskelet tespiti** ve **poz tespiti** bulunur. Bu görevlerin nasıl uygulanabileceğini görmek için [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) kütüphanesine göz atın.

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen dikkate alınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucunda ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.