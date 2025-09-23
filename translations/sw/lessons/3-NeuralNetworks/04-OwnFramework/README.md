<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-25T21:00:11+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "sw"
}
-->
# Utangulizi wa Mitandao ya Neural. Multi-Layered Perceptron

Katika sehemu iliyopita, ulijifunza kuhusu mfano rahisi zaidi wa mtandao wa neural - perceptron ya tabaka moja, mfano wa uainishaji wa tabaka mbili wa mstari.

Katika sehemu hii tutapanua mfano huu kuwa mfumo wenye kubadilika zaidi, unaotuwezesha:

* kufanya **uainishaji wa tabaka nyingi** pamoja na tabaka mbili  
* kutatua **matatizo ya regression** pamoja na uainishaji  
* kutenganisha madarasa ambayo hayawezi kutenganishwa kwa mstari  

Pia tutaendeleza mfumo wetu wa modular kwa kutumia Python ambao utaturuhusu kujenga usanifu tofauti wa mitandao ya neural.

## [Jaribio la kabla ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Urasmishaji wa Kujifunza kwa Mashine

Tuanze kwa kurasmisha tatizo la Kujifunza kwa Mashine. Tuseme tuna seti ya mafunzo **X** yenye lebo **Y**, na tunahitaji kujenga mfano *f* ambao utatoa utabiri sahihi zaidi. Ubora wa utabiri hupimwa kwa kutumia **Kazi ya Hasara** ℒ. Kazi za hasara zifuatazo hutumika mara nyingi:

* Kwa tatizo la regression, ambapo tunahitaji kutabiri namba, tunaweza kutumia **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, au **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>  
* Kwa uainishaji, tunatumia **0-1 loss** (ambayo kimsingi ni sawa na **usahihi** wa mfano), au **logistic loss**.

Kwa perceptron ya tabaka moja, kazi *f* ilifafanuliwa kama kazi ya mstari *f(x)=wx+b* (hapa *w* ni matrix ya uzito, *x* ni vector ya vipengele vya ingizo, na *b* ni vector ya bias). Kwa usanifu tofauti wa mitandao ya neural, kazi hii inaweza kuchukua umbo tata zaidi.

> Katika hali ya uainishaji, mara nyingi ni muhimu kupata uwezekano wa madarasa husika kama matokeo ya mtandao. Ili kubadilisha namba za kawaida kuwa uwezekano (mfano, kuhalalisha matokeo), mara nyingi tunatumia kazi ya **softmax** σ, na kazi *f* inakuwa *f(x)=σ(wx+b)*

Katika ufafanuzi wa *f* hapo juu, *w* na *b* huitwa **vigezo** θ=⟨*w,b*⟩. Kwa kuzingatia seti ya data ⟨**X**,**Y**⟩, tunaweza kuhesabu kosa la jumla kwenye seti nzima ya data kama kazi ya vigezo θ.

> ✅ **Lengo la mafunzo ya mtandao wa neural ni kupunguza kosa kwa kubadilisha vigezo θ**

## Uboreshaji wa Gradient Descent

Kuna mbinu inayojulikana ya uboreshaji wa kazi inayoitwa **gradient descent**. Wazo ni kwamba tunaweza kuhesabu derivative (katika hali ya vipimo vingi huitwa **gradient**) ya kazi ya hasara kwa kuzingatia vigezo, na kubadilisha vigezo kwa njia ambayo kosa litapungua. Hii inaweza kurasmishwa kama ifuatavyo:

* Anzisha vigezo kwa thamani za nasibu w<sup>(0)</sup>, b<sup>(0)</sup>  
* Rudia hatua ifuatayo mara nyingi:  
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w  
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b  

Wakati wa mafunzo, hatua za uboreshaji zinapaswa kuhesabiwa kwa kuzingatia seti nzima ya data (kumbuka kuwa hasara huhesabiwa kama jumla kupitia sampuli zote za mafunzo). Hata hivyo, katika maisha halisi tunachukua sehemu ndogo za seti ya data zinazoitwa **minibatches**, na kuhesabu gradients kwa kuzingatia subset ya data. Kwa sababu subset huchukuliwa kwa nasibu kila wakati, mbinu hii huitwa **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons na Backpropagation

Mtandao wa tabaka moja, kama tulivyoona hapo juu, unaweza kuainisha madarasa yanayoweza kutenganishwa kwa mstari. Ili kujenga mfano tajiri zaidi, tunaweza kuchanganya tabaka kadhaa za mtandao. Kihisabati, hii itamaanisha kuwa kazi *f* itakuwa na umbo tata zaidi, na itahesabiwa kwa hatua kadhaa:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>  
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>  
* f = σ(z<sub>2</sub>)  

Hapa, α ni **kazi ya uanzishaji isiyo ya mstari**, σ ni kazi ya softmax, na vigezo θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algorithm ya gradient descent itabaki ile ile, lakini itakuwa ngumu zaidi kuhesabu gradients. Kwa kuzingatia kanuni ya mnyororo wa differentiation, tunaweza kuhesabu derivatives kama:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)  
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)  

> ✅ Kanuni ya mnyororo wa differentiation hutumika kuhesabu derivatives za kazi ya hasara kwa kuzingatia vigezo.

Kumbuka kuwa sehemu ya kushoto kabisa ya maelezo haya yote ni sawa, na hivyo tunaweza kuhesabu derivatives kwa ufanisi kuanzia kazi ya hasara na kurudi "nyuma" kupitia grafu ya kihesabu. Hivyo mbinu ya kufundisha perceptron ya tabaka nyingi huitwa **backpropagation**, au 'backprop'.

<img alt="compute graph" src="images/ComputeGraphGrad.png"/>

> TODO: rejea ya picha

> ✅ Tutashughulikia backprop kwa undani zaidi katika mfano wetu wa daftari.  

## Hitimisho

Katika somo hili, tumejenga maktaba yetu ya mtandao wa neural, na tumeitumia kwa kazi rahisi ya uainishaji wa vipimo viwili.

## 🚀 Changamoto

Katika daftari linaloambatana, utatekeleza mfumo wako wa kujenga na kufundisha perceptrons za tabaka nyingi. Utaweza kuona kwa undani jinsi mitandao ya neural ya kisasa inavyofanya kazi.

Endelea kwenye [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) daftari na uifanyie kazi.

## [Jaribio la baada ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Mapitio na Kujisomea

Backpropagation ni algorithm ya kawaida inayotumika katika AI na ML, inafaa kusomwa [kwa undani zaidi](https://wikipedia.org/wiki/Backpropagation)

## [Kazi ya Nyumbani](lab/README.md)

Katika maabara hii, unatakiwa kutumia mfumo uliounda katika somo hili kutatua uainishaji wa namba za mkono wa MNIST.

* [Maelekezo](lab/README.md)  
* [Daftari](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)  

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.