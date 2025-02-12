# Quizler

Bu quizler, https://aka.ms/ai-beginners adresindeki AI müfredatı için ders öncesi ve sonrası quizlerdir.

## Çevirisi yapılmış bir quiz seti ekleme

Eşleşen quiz yapıları oluşturarak bir quiz çevirisi ekleyin `assets/translations` klasörlerinde. Temel quizler `assets/translations/en` içinde bulunmaktadır. Quizler, derslere göre birkaç gruba ayrılmıştır. Numara sıralamasını doğru quiz bölümüne göre ayarladığınızdan emin olun. Bu müfredatta toplam 40 quiz bulunmaktadır ve sayım 0'dan başlamaktadır.

Çevirileri düzenledikten sonra, çeviri klasöründeki index.js dosyasını `en` içindeki kurallara göre tüm dosyaları içerecek şekilde düzenleyin.

Yeni çevrilmiş dosyaları içermek için `assets/translations` içindeki `index.js` dosyasını düzenleyin.

Ardından, bu uygulamadaki `App.vue` bölümündeki açılır menüyü düzenleyerek dilinizi ekleyin. Yerelleştirilmiş kısaltmayı diliniz için klasör adıyla eşleştirin.

Son olarak, çevrilen derslerdeki tüm quiz bağlantılarını, varsa, bu yerelleştirmeyi bir sorgu parametresi olarak ekleyecek şekilde düzenleyin: örneğin `?loc=fr`.

## Proje kurulumu

```
npm install
```

### Geliştirme için derler ve sıcak yeniden yükler

```
npm run serve
```

### Üretim için derler ve küçültür

```
npm run build
```

### Dosyaları denetler ve düzeltir

```
npm run lint
```

### Yapılandırmayı özelleştirin

[Configuration Reference](https://cli.vuejs.org/config/) sayfasına bakın.

Krediler: Bu quiz uygulamasının orijinal sürümüne teşekkürler: https://github.com/arpan45/simple-quiz-vue

## Azure'a Dağıtım

Başlamak için adım adım bir kılavuz:

1. GitHub Deposu Oluşturun
Statik web uygulamanızın kodunun GitHub deponuzda olduğundan emin olun. Bu depoyu fork edin.

2. Azure Statik Web Uygulaması Oluşturun
- Bir [Azure hesabı](http://azure.microsoft.com) oluşturun.
- [Azure portalına](https://portal.azure.com) gidin.
- "Bir kaynak oluştur" seçeneğine tıklayın ve "Statik Web Uygulaması" araması yapın.
- "Oluştur" seçeneğine tıklayın.

3. Statik Web Uygulamasını Yapılandırın
- Temel Bilgiler: Abonelik: Azure aboneliğinizi seçin.
- Kaynak Grubu: Yeni bir kaynak grubu oluşturun veya mevcut birini kullanın.
- İsim: Statik web uygulamanız için bir isim verin.
- Bölge: Kullanıcılarınıza en yakın bölgeyi seçin.

- #### Dağıtım Detayları:
- Kaynak: "GitHub" seçeneğini seçin.
- GitHub Hesabı: Azure'un GitHub hesabınıza erişim izni vermesini onaylayın.
- Organizasyon: GitHub organizasyonunuzu seçin.
- Depo: Statik web uygulamanızı içeren depoyu seçin.
- Dal: Dağıtım yapmak istediğiniz dalı seçin.

- #### Derleme Detayları:
- Derleme Ön Ayarları: Uygulamanızın inşa edildiği çerçeveyi seçin (örn., React, Angular, Vue, vb.).
- Uygulama Konumu: Uygulama kodunuzu içeren klasörü belirtin (örn., kökse /).
- API Konumu: Bir API'niz varsa, konumunu belirtin (isteğe bağlı).
- Çıktı Konumu: Derleme çıktısının oluşturulacağı klasörü belirtin (örn., build veya dist).

4. Gözden Geçirin ve Oluşturun
Ayarlarınızı gözden geçirin ve "Oluştur" seçeneğine tıklayın. Azure gerekli kaynakları kuracak ve deponuzda bir GitHub Actions iş akışı oluşturacaktır.

5. GitHub Actions İş Akışı
Azure, deponuzda otomatik olarak bir GitHub Actions iş akışı dosyası oluşturacaktır (.github/workflows/azure-static-web-apps-<name>.yml). Bu iş akışı, derleme ve dağıtım sürecini yönetecektir.

6. Dağıtımı İzleyin
GitHub deponuzdaki "Actions" sekmesine gidin.
Bir iş akışının çalıştığını görmelisiniz. Bu iş akışı, statik web uygulamanızı Azure'a derleyip dağıtacaktır.
İş akışı tamamlandığında, uygulamanız sağlanan Azure URL'sinde canlı olacaktır.

### Örnek İş Akışı Dosyası

GitHub Actions iş akışı dosyasının nasıl görünebileceğine dair bir örnek:
name: Azure Statik Web Uygulamaları CI/CD
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
- [Azure Statik Web Uygulamaları Belgeleri](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [GitHub Actions Belgeleri](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

**Açıklama**:  
Bu belge, makine tabanlı AI çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otorite kaynağı olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucunda ortaya çıkan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.