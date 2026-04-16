# İnsan Vücudu Segmentasyonu

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) kapsamında bir laboratuvar ödevi.

## Görev

Video prodüksiyonunda, örneğin hava durumu sunumlarında, genellikle bir insan görüntüsünü kameradan kesip başka bir görüntünün üzerine yerleştirmemiz gerekir. Bu genellikle, bir insanın tek renkli bir arka plan önünde çekildiği ve ardından bu arka planın kaldırıldığı **chroma key** teknikleri kullanılarak yapılır. Bu laboratuvarda, bir insan siluetini kesmek için bir sinir ağı modeli eğiteceğiz.

## Veri Seti

Kaggle'dan [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) veri setini kullanacağız. Veri setini Kaggle'dan manuel olarak indirin.

## Başlangıç Not Defteri

Laboratuvara [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb) dosyasını açarak başlayın.

## Çıkarım

Vücut segmentasyonu, insan görüntüleriyle yapabileceğimiz yaygın görevlerden sadece biridir. Diğer önemli görevler arasında **iskelet tespiti** ve **poz tespiti** bulunur. Bu görevlerin nasıl uygulanabileceğini görmek için [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) kütüphanesine göz atın.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.