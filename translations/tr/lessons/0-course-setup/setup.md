<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4c545eb30765a49469ced84cfb4379f",
  "translation_date": "2025-08-26T07:40:15+00:00",
  "source_file": "lessons/0-course-setup/setup.md",
  "language_code": "tr"
}
-->
# Bu Müfredata Başlarken

## Öğrenci misiniz?

Aşağıdaki kaynaklarla başlayabilirsiniz:

* [Öğrenci Merkezi sayfası](https://docs.microsoft.com/learn/student-hub?WT.mc_id=academic-77998-cacaste) Bu sayfada başlangıç kaynakları, Öğrenci paketleri ve hatta ücretsiz sertifika kuponu alma yollarını bulabilirsiniz. Bu sayfayı sık kullanılanlara ekleyip zaman zaman kontrol etmek isteyebilirsiniz, çünkü içeriği en az ayda bir değiştiriyoruz.
* [Microsoft Öğrenci Elçileri](https://studentambassadors.microsoft.com?WT.mc_id=academic-77998-cacaste) Küresel bir öğrenci elçileri topluluğuna katılın, bu sizin Microsoft'a açılan kapınız olabilir.

**Öğrenciler**, müfredatı kullanmanın birkaç yolu var. İlk olarak, metni okuyabilir ve kodu doğrudan GitHub'da inceleyebilirsiniz. Not defterlerindeki kodu çalıştırmak isterseniz - [talimatlarımızı okuyun](./etc/how-to-run.md) ve bunu nasıl yapacağınızla ilgili daha fazla tavsiyeyi [bu blog yazısında](https://soshnikov.com/education/how-to-execute-notebooks-from-github/) bulabilirsiniz.

> **Not**: [Bu müfredattaki kodu nasıl çalıştıracağınızla ilgili talimatlar](./how-to-run.md)

## Kendi Kendine Çalışma

Ancak, bu dersi kendi kendine çalışma projesi olarak almak isterseniz, tüm depoyu kendi GitHub hesabınıza çatallayıp alıştırmaları kendi başınıza veya bir grupla tamamlamanızı öneririz:

* Ders öncesi bir testle başlayın.
* Dersin giriş metnini okuyun.
* Eğer dersin ek not defterleri varsa, bunları okuyup kodu çalıştırarak inceleyin. Hem TensorFlow hem de PyTorch not defterleri sağlanmışsa, favori çerçevenizi seçip ona odaklanabilirsiniz.
* Not defterleri genellikle kodu biraz değiştirerek denemeler yapmanızı gerektiren bazı zorluklar içerir.
* Ders sonrası testi yapın.
* Modüle bağlı bir laboratuvar varsa - ödevi tamamlayın.
* [Tartışma panosunu](https://github.com/microsoft/AI-For-Beginners/discussions) ziyaret ederek "yüksek sesle öğrenin".

> Daha fazla çalışma için, bu [Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-77998-cacaste) modüllerini ve öğrenme yollarını takip etmenizi öneririz.

**Eğitmenler**, bu müfredatı nasıl kullanacağınızla ilgili [bazı öneriler ekledik](/for-teachers.md).

---

## Pedagoji

Bu müfredatı oluştururken iki pedagojik ilkeye bağlı kaldık: içeriğin **proje tabanlı** ve **sık sık testler içeren** bir yapıda olmasını sağlamak.

İçeriğin projelerle uyumlu olmasını sağlayarak, süreç öğrenciler için daha ilgi çekici hale gelir ve kavramların kalıcılığı artırılır. Ayrıca, ders öncesi düşük riskli bir test, öğrencinin bir konuyu öğrenmeye yönelik niyetini belirlerken, ders sonrası yapılan ikinci bir test daha fazla kalıcılığı sağlar. Bu müfredat esnek ve eğlenceli olacak şekilde tasarlandı ve tamamen veya kısmen alınabilir. Projeler küçük başlar ve 12 haftalık döngünün sonunda giderek daha karmaşık hale gelir.

> **Testler hakkında bir not**: Tüm testler [bu uygulamada](https://red-field-0a6ddfd03.1.azurestaticapps.net/) yer alır, toplamda üçer sorudan oluşan 50 test vardır. Derslerin içinden bağlantılıdır, ancak test uygulaması yerel olarak çalıştırılabilir; `etc/quiz-app` klasöründeki talimatları izleyin.

## Çevrimdışı erişim

Bu dokümantasyonu [Docsify](https://docsify.js.org/#/) kullanarak çevrimdışı çalıştırabilirsiniz. Bu depoyu çatallayın, [Docsify'i yükleyin](https://docsify.js.org/#/quickstart) yerel makinenize kurun ve ardından bu deponun kök klasöründe `docsify serve` yazın. Web sitesi localhost'unuzda 3000 portunda sunulacaktır: `localhost:3000`. Müfredatın bir PDF'sine [bu bağlantıdan](../../../../../../../../../etc/pdf/readme.pdf) ulaşabilirsiniz.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.