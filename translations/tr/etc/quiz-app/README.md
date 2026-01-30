# Quizler

Bu quizler, https://aka.ms/ai-beginners adresindeki AI müfredatının ders öncesi ve sonrası quizleridir.

## Çevirilmiş bir quiz seti ekleme

Bir quiz çevirisi eklemek için, `assets/translations` klasörlerinde eşleşen quiz yapıları oluşturun. Orijinal quizler `assets/translations/en` klasöründe bulunur. Quizler, derslere göre birkaç gruba ayrılmıştır. Numaralandırmayı doğru quiz bölümüyle hizalamayı unutmayın. Bu müfredatta toplam 40 quiz bulunmaktadır ve numaralandırma 0'dan başlar.

Çevirileri düzenledikten sonra, çeviri klasöründeki `index.js` dosyasını düzenleyerek, `en` klasöründeki kurallara uygun şekilde tüm dosyaları içe aktarın.

`assets/translations` içindeki `index.js` dosyasını düzenleyerek yeni çevirilmiş dosyaları içe aktarın.

Son olarak, bu uygulamadaki `App.vue` dosyasındaki açılır menüyü düzenleyerek dilinizi ekleyin. Yerelleştirilmiş kısaltmayı dilinizin klasör adıyla eşleştirin.

Eğer varsa, çevirilmiş derslerdeki tüm quiz bağlantılarını düzenleyerek bu yerelleştirmeyi bir sorgu parametresi olarak ekleyin: Örneğin, `?loc=fr`.

## Proje kurulumu

```
npm install
```

### Geliştirme için derler ve sıcak yükleme yapar

```
npm run serve
```

### Üretim için derler ve küçültür

```
npm run build
```

### Dosyaları kontrol eder ve düzeltir

```
npm run lint
```

### Yapılandırmayı özelleştirme

[Configuration Reference](https://cli.vuejs.org/config/) adresine bakın.

Teşekkürler: Bu quiz uygulamasının orijinal versiyonu için teşekkürler: https://github.com/arpan45/simple-quiz-vue

## Azure'a Dağıtım

İşte başlamanıza yardımcı olacak adım adım bir rehber:

1. GitHub Deposunu Çatallayın  
Statik web uygulamanızın kodunun GitHub deponuzda olduğundan emin olun. Bu depoyu çatallayın.

2. Bir Azure Statik Web Uygulaması Oluşturun  
- Bir [Azure hesabı](http://azure.microsoft.com) oluşturun.  
- [Azure portalına](https://portal.azure.com) gidin.  
- “Bir kaynak oluştur”a tıklayın ve “Statik Web Uygulaması” arayın.  
- “Oluştur”a tıklayın.

3. Statik Web Uygulamasını Yapılandırın  
- Temel Bilgiler:  
  - Abonelik: Azure aboneliğinizi seçin.  
  - Kaynak Grubu: Yeni bir kaynak grubu oluşturun veya mevcut birini kullanın.  
  - Ad: Statik web uygulamanız için bir ad belirleyin.  
  - Bölge: Kullanıcılarınıza en yakın bölgeyi seçin.  

- #### Dağıtım Detayları:  
  - Kaynak: “GitHub”ı seçin.  
  - GitHub Hesabı: Azure’un GitHub hesabınıza erişmesine izin verin.  
  - Organizasyon: GitHub organizasyonunuzu seçin.  
  - Depo: Statik web uygulamanızı içeren depoyu seçin.  
  - Dal: Hangi daldan dağıtım yapacağınızı seçin.  

- #### Yapı Detayları:  
  - Yapı Ön Ayarları: Uygulamanızın oluşturulduğu çerçeveyi seçin (ör. React, Angular, Vue, vb.).  
  - Uygulama Konumu: Uygulama kodunuzu içeren klasörü belirtin (ör. kökteyse /).  
  - API Konumu: Eğer bir API’niz varsa, konumunu belirtin (isteğe bağlı).  
  - Çıktı Konumu: Yapı çıktısının oluşturulduğu klasörü belirtin (ör. build veya dist).  

4. Gözden Geçir ve Oluştur  
Ayarlarınızı gözden geçirin ve “Oluştur”a tıklayın. Azure, gerekli kaynakları ayarlayacak ve deponuzda bir GitHub Actions iş akışı oluşturacaktır.

5. GitHub Actions İş Akışı  
Azure, deponuzda otomatik olarak bir GitHub Actions iş akışı dosyası oluşturacaktır (.github/workflows/azure-static-web-apps-<name>.yml). Bu iş akışı, yapı ve dağıtım sürecini yönetecektir.

6. Dağıtımı İzleme  
GitHub deponuzdaki “Actions” sekmesine gidin.  
Bir iş akışının çalıştığını görmelisiniz. Bu iş akışı, statik web uygulamanızı Azure’a oluşturup dağıtacaktır.  
İş akışı tamamlandığında, uygulamanız sağlanan Azure URL’sinde canlı olacaktır.

### Örnek İş Akışı Dosyası

İşte GitHub Actions iş akışı dosyasının nasıl görünebileceğine dair bir örnek:  
name: Azure Static Web Apps CI/CD  
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "etc/quiz-app # App source code path"
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```

### Ek Kaynaklar  
- [Azure Statik Web Uygulamaları Dokümantasyonu](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Dokümantasyonu](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.