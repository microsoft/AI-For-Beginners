<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-28T02:36:14+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "tl"
}
-->
# Panimula sa AI

![Buod ng Panimula sa AI na nilalaman sa isang doodle](../../../../translated_images/ai-intro.bf28d1ac4235881c096f0ffdb320ba4102940eafcca4e9d7a55a03914361f8f3.tl.png)

> Sketchnote ni [Tomomi Imura](https://twitter.com/girlie_mac)

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/1)

**Artificial Intelligence** ay isang kapanapanabik na disiplina ng agham na nag-aaral kung paano natin magagawang magpakita ng matalinong pag-uugali ang mga computer, halimbawa, gawin ang mga bagay na mahusay gawin ng mga tao.

Noong una, ang mga computer ay naimbento ni [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) upang gumana sa mga numero gamit ang isang malinaw na proseso - isang algorithm. Ang mga modernong computer, kahit na mas advanced kaysa sa orihinal na modelo noong ika-19 na siglo, ay sumusunod pa rin sa parehong ideya ng kontroladong pagkalkula. Kaya't posible na i-program ang isang computer upang gawin ang isang bagay kung alam natin ang eksaktong pagkakasunod-sunod ng mga hakbang na kailangan upang makamit ang layunin.

![Larawan ng isang tao](../../../../translated_images/dsh_age.d212a30d4e54fb5f68b94a624aad64bc086124bcbbec9561ae5bd5da661e22d8.tl.png)

> Larawan ni [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Ang pagtukoy ng edad ng isang tao mula sa kanyang larawan ay isang gawain na hindi maaaring i-program nang malinaw, dahil hindi natin alam kung paano tayo nakakabuo ng numero sa ating isipan kapag ginagawa natin ito.

---

May mga gawain, gayunpaman, na hindi natin alam kung paano eksaktong lutasin. Halimbawa, ang pagtukoy ng edad ng isang tao mula sa kanyang larawan. Natutunan natin itong gawin dahil nakakita na tayo ng maraming halimbawa ng mga tao sa iba't ibang edad, ngunit hindi natin maipaliwanag nang malinaw kung paano natin ito ginagawa, o maiprograma ang computer upang gawin ito. Ito ang eksaktong uri ng gawain na interesado ang **Artificial Intelligence** (AI).

✅ Mag-isip ng ilang gawain na maaari mong ipasa sa isang computer na makikinabang mula sa AI. Isaalang-alang ang mga larangan ng pananalapi, medisina, at sining - paano nakikinabang ang mga larangang ito mula sa AI ngayon?

## Mahinang AI vs. Malakas na AI

Mahinang AI | Malakas na AI
---------------------------------------|-------------------------------------
Ang Mahinang AI ay tumutukoy sa mga sistema ng AI na idinisenyo at sinanay para sa isang tiyak na gawain o makitid na hanay ng mga gawain.|Ang Malakas na AI, o Artificial General Intelligence (AGI), ay tumutukoy sa mga sistema ng AI na may antas ng katalinuhan at pag-unawa na katulad ng tao.
Ang mga sistemang ito ay hindi pangkalahatang matalino; mahusay sila sa pagsasagawa ng isang paunang natukoy na gawain ngunit kulang sa tunay na pag-unawa o kamalayan.|Ang mga sistemang ito ay may kakayahang magsagawa ng anumang intelektwal na gawain na kayang gawin ng tao, umangkop sa iba't ibang larangan, at magkaroon ng anyo ng kamalayan o sariling kamalayan.
Mga halimbawa ng mahinang AI ay ang mga virtual assistant tulad ng Siri o Alexa, mga algorithm ng rekomendasyon na ginagamit ng mga streaming service, at mga chatbot na idinisenyo para sa mga tiyak na gawain sa serbisyo sa customer.|Ang pagkamit ng Malakas na AI ay isang pangmatagalang layunin ng pananaliksik sa AI at mangangailangan ng pagbuo ng mga sistemang AI na kayang mag-isip, matuto, umunawa, at umangkop sa malawak na hanay ng mga gawain at konteksto.
Ang Mahinang AI ay lubos na dalubhasa at walang kakayahang kognitibo na tulad ng tao o pangkalahatang kakayahan sa paglutas ng problema sa labas ng makitid nitong larangan.|Ang Malakas na AI ay kasalukuyang isang teoretikal na konsepto, at wala pang sistemang AI ang umabot sa antas na ito ng pangkalahatang katalinuhan.

Para sa karagdagang impormasyon, tingnan ang **[Artificial General Intelligence](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI).

## Ang Depinisyon ng Katalinuhan at ang Turing Test

Isa sa mga problema kapag pinag-uusapan ang terminong **[Katalinuhan](https://en.wikipedia.org/wiki/Intelligence)** ay ang kawalan ng malinaw na depinisyon nito. Maaaring sabihin na ang katalinuhan ay konektado sa **abstraktong pag-iisip**, o sa **sariling kamalayan**, ngunit hindi natin ito maipaliwanag nang maayos.

![Larawan ng isang Pusa](../../../../translated_images/photo-cat.8c8e8fb760ffe45725c5b9f6b0d954e9bf114475c01c55adf0303982851b7eae.tl.jpg)

> [Larawan](https://unsplash.com/photos/75715CVEJhI) ni [Amber Kipp](https://unsplash.com/@sadmax) mula sa Unsplash

Upang makita ang kalabuan ng terminong *katalinuhan*, subukang sagutin ang tanong: "Ang pusa ba ay matalino?". Iba't ibang tao ang may iba't ibang sagot sa tanong na ito, dahil walang pangkalahatang tinatanggap na pagsusulit upang patunayan kung totoo o hindi ang pahayag. At kung sa tingin mo ay mayroon - subukang ipasailalim ang iyong pusa sa isang IQ test...

✅ Mag-isip ng isang minuto kung paano mo tinutukoy ang katalinuhan. Ang uwak ba na kayang lutasin ang isang maze upang makakuha ng pagkain ay matalino? Ang bata ba ay matalino?

---

Kapag pinag-uusapan ang AGI, kailangan nating magkaroon ng paraan upang malaman kung nakalikha tayo ng tunay na matalinong sistema. Iminungkahi ni [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) ang isang paraan na tinatawag na **[Turing Test](https://en.wikipedia.org/wiki/Turing_test)**, na nagsisilbi ring depinisyon ng katalinuhan. Ang pagsusulit ay inihahambing ang isang sistema sa isang bagay na likas na matalino - isang tunay na tao, at dahil ang anumang awtomatikong paghahambing ay maaaring lampasan ng isang computer program, gumagamit tayo ng isang tao bilang tagapagtanong. Kaya, kung ang isang tao ay hindi makilala ang pagkakaiba sa pagitan ng isang tunay na tao at isang computer system sa text-based na diyalogo - ang sistema ay itinuturing na matalino.

> Ang isang chatbot na tinatawag na [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman), na binuo sa St. Petersburg, ay halos pumasa sa Turing test noong 2014 sa pamamagitan ng paggamit ng isang matalinong personalidad na trick. Inanunsyo nito na ito ay isang 13-taong gulang na batang Ukrainian, na nagpapaliwanag ng kakulangan sa kaalaman at ilang mga pagkakaiba sa teksto. Napaniwala ng bot ang 30% ng mga hukom na ito ay tao pagkatapos ng 5 minutong diyalogo, isang sukatan na pinaniniwalaan ni Turing na kayang lampasan ng isang makina pagsapit ng 2000. Gayunpaman, dapat maunawaan na hindi ito nangangahulugan na nakalikha tayo ng matalinong sistema, o na nalinlang ng computer system ang tagapagtanong - ang mga tagalikha ng bot ang tunay na nakalinlang!

✅ Nalinlang ka na ba ng isang chatbot na isipin na tao ang kausap mo? Paano ka nito napaniwala?

## Iba't Ibang Diskarte sa AI

Kung nais nating magpakilos ang isang computer na parang tao, kailangan nating i-modelo sa loob ng computer ang paraan ng ating pag-iisip. Dahil dito, kailangan nating subukang maunawaan kung ano ang nagpapatalino sa isang tao.

> Upang maiprograma ang katalinuhan sa isang makina, kailangan nating maunawaan kung paano gumagana ang ating sariling proseso ng paggawa ng desisyon. Kung magpapakilala ka sa sarili mo, mapapansin mo na may mga proseso na nangyayari nang hindi mo namamalayan – halimbawa, kaya nating makilala ang pusa mula sa aso nang hindi iniisip ito - habang ang iba naman ay nangangailangan ng pangangatwiran.

May dalawang posibleng diskarte sa problemang ito:

Diskarteng Top-down (Symbolic Reasoning) | Diskarteng Bottom-up (Neural Networks)
---------------------------------------|-------------------------------------
Ang diskarte ng top-down ay nagmomodelo sa paraan ng pangangatwiran ng isang tao upang lutasin ang isang problema. Kabilang dito ang pagkuha ng **kaalaman** mula sa isang tao, at pagre-representa nito sa isang anyong nababasa ng computer. Kailangan din nating bumuo ng paraan upang i-modelo ang **pangangatwiran** sa loob ng computer. | Ang diskarte ng bottom-up ay nagmomodelo sa istruktura ng utak ng tao, na binubuo ng napakaraming simpleng yunit na tinatawag na **neurons**. Ang bawat neuron ay kumikilos tulad ng isang weighted average ng mga input nito, at maaari nating sanayin ang isang network ng neurons upang lutasin ang mga kapaki-pakinabang na problema sa pamamagitan ng pagbibigay ng **training data**.

Mayroon ding iba pang posibleng diskarte sa katalinuhan:

* Ang **Emergent**, **Synergetic**, o **multi-agent approach** ay batay sa ideya na ang kumplikadong matalinong pag-uugali ay maaaring makuha mula sa interaksyon ng maraming simpleng ahente. Ayon sa [evolutionary cybernetics](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics), ang katalinuhan ay maaaring *lumitaw* mula sa mas simpleng, reaktibong pag-uugali sa proseso ng *metasystem transition*.

* Ang **Evolutionary approach**, o **genetic algorithm** ay isang proseso ng pag-optimize na batay sa mga prinsipyo ng ebolusyon.

Tatalakayin natin ang mga diskarteng ito sa mga susunod na bahagi ng kurso, ngunit sa ngayon ay magtutuon tayo sa dalawang pangunahing direksyon: top-down at bottom-up.

### Ang Diskarteng Top-Down

Sa isang **top-down approach**, sinusubukan nating i-modelo ang ating pangangatwiran. Dahil kaya nating sundan ang ating mga iniisip kapag tayo ay nangangatwiran, maaari nating subukang i-formalize ang prosesong ito at i-programa ito sa loob ng computer. Ito ay tinatawag na **symbolic reasoning**.

Ang mga tao ay may mga patakaran sa kanilang isipan na gumagabay sa kanilang mga proseso ng paggawa ng desisyon. Halimbawa, kapag ang isang doktor ay nag-diagnose ng pasyente, maaaring mapansin niya na ang tao ay may lagnat, kaya maaaring may impeksyon sa loob ng katawan. Sa pamamagitan ng paglalapat ng maraming hanay ng mga patakaran sa isang tiyak na problema, maaaring makabuo ang doktor ng pangwakas na diagnosis.

Ang diskarteng ito ay lubos na umaasa sa **representasyon ng kaalaman** at **pangangatwiran**. Ang pagkuha ng kaalaman mula sa isang dalubhasa ay maaaring ang pinakamahirap na bahagi, dahil sa maraming pagkakataon, hindi alam ng doktor kung bakit siya nagkakaroon ng partikular na diagnosis. Minsan, ang solusyon ay basta na lang lumalabas sa kanyang isipan nang walang malinaw na pag-iisip. Ang ilang mga gawain, tulad ng pagtukoy ng edad ng isang tao mula sa larawan, ay hindi maaaring mabawasan sa simpleng pagmamanipula ng kaalaman.

### Diskarteng Bottom-Up

Sa kabilang banda, maaari nating subukang i-modelo ang pinakasimpleng elemento sa ating utak – ang neuron. Maaari tayong bumuo ng tinatawag na **artificial neural network** sa loob ng computer, at pagkatapos ay subukang turuan ito na lutasin ang mga problema sa pamamagitan ng pagbibigay ng mga halimbawa. Ang prosesong ito ay katulad ng kung paano natututo ang isang bagong silang na sanggol tungkol sa kanyang kapaligiran sa pamamagitan ng pagmamasid.

✅ Mag-research ng kaunti kung paano natututo ang mga sanggol. Ano ang mga pangunahing elemento ng utak ng isang sanggol?

> | Paano naman ang ML?         |      |
> |--------------|-----------|
> | Ang bahagi ng Artificial Intelligence na batay sa pagkatuto ng computer upang lutasin ang isang problema batay sa ilang data ay tinatawag na **Machine Learning**. Hindi natin tatalakayin ang klasikong machine learning sa kursong ito - inirerekomenda namin sa iyo ang hiwalay na kurikulum na [Machine Learning for Beginners](http://aka.ms/ml-beginners). |   ![ML for Beginners](../../../../translated_images/ml-for-beginners.9e4fed176fd5817d7d1f7d358302515186579cbf09b2a6c5bd8092b345da7f22.tl.png)    |

## Maikling Kasaysayan ng AI

Ang Artificial Intelligence ay nagsimula bilang isang larangan noong kalagitnaan ng ika-20 siglo. Sa simula, ang symbolic reasoning ang nangingibabaw na diskarte, at nagbunga ito ng ilang mahahalagang tagumpay, tulad ng mga expert system – mga programang computer na kayang kumilos bilang eksperto sa ilang limitadong larangan ng problema. Gayunpaman, kalaunan ay naging malinaw na ang ganitong diskarte ay hindi madaling ma-scale. Ang pagkuha ng kaalaman mula sa isang eksperto, pagre-representa nito sa computer, at pagpapanatili ng kaalaman na ito ay napakahirap at masyadong magastos upang maging praktikal sa maraming kaso. Dahil dito, nagkaroon ng tinatawag na [AI Winter](https://en.wikipedia.org/wiki/AI_winter) noong 1970s.

> Larawan ni [Dmitry Soshnikov](http://soshnikov.com)

Habang lumilipas ang panahon, naging mas mura ang mga computing resources, at mas maraming data ang naging magagamit, kaya't ang mga diskarte sa neural network ay nagsimulang magpakita ng mahusay na pagganap sa pakikipagkumpitensya sa mga tao sa maraming larangan, tulad ng computer vision o pag-unawa sa pagsasalita. Sa nakaraang dekada, ang terminong Artificial Intelligence ay kadalasang ginagamit bilang kasingkahulugan ng Neural Networks, dahil karamihan sa mga tagumpay ng AI na naririnig natin ay batay dito.

Makikita natin kung paano nagbago ang mga diskarte, halimbawa, sa paggawa ng programang computer na naglalaro ng chess:

* Ang mga maagang programa sa chess ay batay sa paghahanap – sinusubukan ng programa na tantyahin ang mga posibleng galaw ng kalaban para sa isang tiyak na bilang ng mga susunod na galaw, at pinipili ang pinakamainam na galaw batay sa pinakamainam na posisyon na maaaring makamit sa ilang galaw. Nagresulta ito sa pagbuo ng tinatawag na [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) search algorithm.
* Ang mga estratehiya sa paghahanap ay mahusay sa dulo ng laro, kung saan ang espasyo ng paghahanap ay limitado sa maliit na bilang ng mga posibleng galaw. Gayunpaman, sa simula ng laro, ang espasyo ng paghahanap ay napakalaki, at maaaring mapabuti ang algorithm sa pamamagitan ng pag-aaral mula sa mga umiiral na laban sa pagitan ng mga manlalaro. Ang mga sumunod na eksperimento ay gumamit ng tinatawag na [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), kung saan ang programa ay naghahanap ng mga kaso sa knowledge base na halos katulad ng kasalukuyang posisyon sa laro.
* Ang mga modernong programa na nananalo laban sa mga manlalaro ng tao ay batay sa neural networks at [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning), kung saan natututo ang mga programa na maglaro sa pamamagitan lamang ng paglalaro ng mahabang panahon laban sa kanilang sarili at pag-aaral mula sa kanilang sariling mga pagkakamali – tulad ng ginagawa ng mga tao kapag natututo ng chess. Gayunpaman, ang isang programang computer ay maaaring maglaro ng mas maraming laro sa mas maikling panahon, kaya't mas mabilis itong natututo.

✅ Mag-research ng kaunti tungkol sa iba pang mga laro na nilaro ng AI.

Katulad nito, makikita natin kung paano nagbago ang diskarte sa paggawa ng mga "programang nagsasalita" (na maaaring pumasa sa Turing test):

* Ang mga maagang programa ng ganitong uri tulad ng [Eliza](https://en.wikipedia.org/wiki/ELIZA), ay batay sa napakasimpleng mga panuntunan sa gramatika at ang muling pagbabalangkas ng input na pangungusap sa isang tanong.
* Ang mga modernong assistant, tulad ng Cortana, Siri, o Google Assistant ay mga hybrid system na gumagamit ng Neural networks upang i-convert ang pagsasalita sa teksto at kilalanin ang ating layunin, at pagkatapos ay gumagamit ng ilang pangangatwiran o malinaw na mga algorithm upang isagawa ang mga kinakailangang aksyon.
* Sa hinaharap, maaari nating asahan ang isang kumpletong neural-based na modelo na kayang hawakan ang diyalogo nang mag-isa. Ang mga kamakailang neural networks tulad ng GPT at [Turing-NLG](https://turing.microsoft.com/) ay nagpapakita ng malaking tagumpay sa larangang ito.

> Larawan ni Dmitry Soshnikov, [larawan](https://unsplash.com/photos/r8LmVbUKgns) ni [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Kamakailang Pananaliksik sa AI

Ang malaking pag-usbong ng pananaliksik sa neural network ay nagsimula noong 2010, nang ang malalaking pampublikong dataset ay naging available. Isang malaking koleksyon ng mga larawan na tinatawag na [ImageNet](https://en.wikipedia.org/wiki/ImageNet), na naglalaman ng humigit-kumulang 14 milyong annotated na mga larawan, ang nagbigay-daan sa [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![ILSVRC Accuracy](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Larawan ni [Dmitry Soshnikov](http://soshnikov.com)

Noong 2012, unang ginamit ang [Convolutional Neural Networks](../4-ComputerVision/07-ConvNets/README.md) sa image classification, na nagresulta sa malaking pagbaba ng mga error sa classification (mula halos 30% hanggang 16.4%). Noong 2015, ang ResNet architecture mula sa Microsoft Research ay [nakamit ang human-level accuracy](https://doi.org/10.1109/ICCV.2015.123).

Simula noon, ang Neural Networks ay nagpakita ng napakagandang resulta sa maraming gawain:

---

Taon | Naabot ang Human Parity
-----|--------
2015 | [Image Classification](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Conversational Speech Recognition](https://arxiv.org/abs/1610.05256)
2018 | [Automatic Machine Translation](https://arxiv.org/abs/1803.05567) (Chinese-to-English)
2020 | [Image Captioning](https://arxiv.org/abs/2009.13682)

Sa nakalipas na ilang taon, nasaksihan natin ang malalaking tagumpay sa malalaking language models, tulad ng BERT at GPT-3. Nangyari ito dahil sa dami ng pangkalahatang text data na available, na nagbibigay-daan upang sanayin ang mga modelo na maunawaan ang istruktura at kahulugan ng mga teksto, i-pretrain ang mga ito sa pangkalahatang koleksyon ng teksto, at pagkatapos ay i-specialize ang mga modelo para sa mas tiyak na mga gawain. Matututo pa tayo tungkol sa [Natural Language Processing](../5-NLP/README.md) sa susunod na bahagi ng kursong ito.

## 🚀 Hamon

Maglibot sa internet upang tukuyin kung saan, sa iyong opinyon, ang AI ay pinaka-epektibong ginagamit. Ito ba ay sa isang Mapping app, o sa isang speech-to-text service, o sa isang video game? Saliksikin kung paano binuo ang sistema.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Review at Pag-aaral sa Sarili

Balikan ang kasaysayan ng AI at ML sa pamamagitan ng pagbabasa ng [araling ito](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Pumili ng isang elemento mula sa sketchnote sa itaas ng araling iyon o sa araling ito at saliksikin ito nang mas malalim upang maunawaan ang kontekstong kultural na nakaimpluwensya sa ebolusyon nito.

**Takdang-Aralin**: [Game Jam](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.