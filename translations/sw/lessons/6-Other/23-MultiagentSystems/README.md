<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ddf651d7681b4449f9d09ea3b17911e",
  "translation_date": "2025-08-25T20:58:00+00:00",
  "source_file": "lessons/6-Other/23-MultiagentSystems/README.md",
  "language_code": "sw"
}
-->
# Mfumo wa Wakala Wengi

Njia mojawapo ya kufanikisha akili ni mbinu inayoitwa **inayojitokeza** (au **synergetic**), ambayo inategemea ukweli kwamba tabia ya pamoja ya mawakala wengi rahisi inaweza kusababisha tabia ya jumla ya mfumo kuwa ngumu zaidi (au yenye akili). Kimsingi, hii inategemea kanuni za [Akili ya Pamoja](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentism](https://en.wikipedia.org/wiki/Global_brain) na [Cybernetics ya Mageuzi](https://en.wikipedia.org/wiki/Global_brain), ambazo zinasema kwamba mifumo ya kiwango cha juu hupata aina fulani ya thamani ya ziada inapounganishwa vizuri kutoka kwa mifumo ya kiwango cha chini (kanuni inayoitwa *mpito wa metasystem*).

## [Jaribio la Kabla ya Somo](https://ff-quizzes.netlify.app/en/ai/quiz/45)

Mwelekeo wa **Mfumo wa Wakala Wengi** ulianza kujitokeza katika AI miaka ya 1990 kama jibu la ukuaji wa mtandao na mifumo iliyosambazwa. Mojawapo ya vitabu vya kiada vya AI vya kawaida, [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), linaangazia mtazamo wa AI ya kawaida kutoka kwa mtazamo wa mifumo ya wakala wengi.

Kiini cha mbinu ya wakala wengi ni dhana ya **Wakala** - chombo kinachoishi katika **mazingira** fulani, ambacho kinaweza kutambua na kuchukua hatua juu yake. Hii ni tafsiri pana sana, na kunaweza kuwa na aina nyingi na uainishaji wa mawakala:

* Kwa uwezo wao wa kufikiri:
   - Mawakala **Wenye Majibu** mara nyingi huwa na tabia rahisi ya ombi-jibu.
   - Mawakala **Wenye Kufikiri** hutumia aina fulani ya kufikiri kimantiki na/au uwezo wa kupanga.
* Kwa mahali ambapo wakala huendesha msimbo wake:
   - Mawakala **Wenye Kudumu** hufanya kazi kwenye nodi maalum ya mtandao.
   - Mawakala **Wenye Kuhama** wanaweza kuhamisha msimbo wao kati ya nodi za mtandao.
* Kwa tabia yao:
   - Mawakala **Wenye Uzembe** hawana malengo maalum. Mawakala kama hao wanaweza kujibu vichocheo vya nje, lakini hawataanzisha vitendo vyovyote wenyewe.
   - Mawakala **Wenye Shughuli** wana malengo fulani wanayoyafuatilia.
   - Mawakala **Wenye Akili** wanahusisha upangaji na kufikiri kwa kina.

Mifumo ya wakala wengi kwa sasa inatumika katika programu kadhaa:

* Katika michezo, wahusika wengi wasio wachezaji hutumia aina fulani ya AI, na wanaweza kuchukuliwa kuwa mawakala wenye akili.
* Katika utengenezaji wa video, uundaji wa mandhari changamano za 3D zinazohusisha umati mara nyingi hufanywa kwa kutumia simulizi ya wakala wengi.
* Katika uundaji wa mifumo, mbinu ya wakala wengi hutumika kuiga tabia ya mfano changamano. Kwa mfano, mbinu ya wakala wengi imetumika kwa mafanikio kutabiri kuenea kwa ugonjwa wa COVID-19 duniani kote. Mbinu kama hiyo inaweza kutumika kuiga trafiki katika jiji, na kuona jinsi inavyoitikia mabadiliko ya sheria za trafiki.
* Katika mifumo changamano ya kiotomatiki, kila kifaa kinaweza kufanya kazi kama wakala huru, ambayo hufanya mfumo mzima kuwa si wa monolith na kuwa thabiti zaidi.

Hatutatumia muda mwingi kuchunguza kwa kina mifumo ya wakala wengi, lakini tutazingatia mfano mmoja wa **Uundaji wa Wakala Wengi**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) ni mazingira ya uundaji wa wakala wengi yanayotegemea toleo lililorekebishwa la lugha ya programu ya [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)). Lugha hii ilitengenezwa kwa ajili ya kufundisha dhana za programu kwa watoto, na inakuwezesha kudhibiti wakala anayeitwa **kobe**, ambaye anaweza kusonga, akiacha alama nyuma. Hii inaruhusu kuunda maumbo changamano ya kijiometri, ambayo ni njia ya kuona tabia ya wakala.

Katika NetLogo, tunaweza kuunda kobe wengi kwa kutumia amri ya `create-turtles`. Tunaweza kisha kuamuru kobe wote kufanya vitendo fulani (katika mfano hapa chini - kusonga mbele kwa pointi 10):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Bila shaka, si jambo la kuvutia wakati kobe wote wanafanya jambo lile lile, kwa hivyo tunaweza `ask` vikundi vya kobe, kwa mfano wale walio karibu na eneo fulani. Tunaweza pia kuunda kobe wa *aina* tofauti kwa kutumia amri ya `breed [cats cat]`. Hapa `cat` ni jina la aina, na tunahitaji kutaja neno la umoja na wingi, kwa sababu amri tofauti hutumia aina tofauti kwa uwazi.

> ✅ Hatutajifunza lugha ya NetLogo yenyewe - unaweza kutembelea rasilimali bora ya [Kamusi ya Kielekezi ya Kuanza ya NetLogo](https://ccl.northwestern.edu/netlogo/bind/) ikiwa una nia ya kujifunza zaidi.

Unaweza [kupakua](https://ccl.northwestern.edu/netlogo/download.shtml) na kusakinisha NetLogo ili kuijaribu.

### Maktaba ya Miundo

Jambo zuri kuhusu NetLogo ni kwamba ina maktaba ya miundo inayofanya kazi ambayo unaweza kuijaribu. Nenda kwa **Faili → Maktaba ya Miundo**, na una kategoria nyingi za miundo za kuchagua.

<img alt="Maktaba ya Miundo ya NetLogo" src="images/NetLogo-ModelLib.png" width="60%"/>

> Picha ya skrini ya maktaba ya miundo na Dmitry Soshnikov

Unaweza kufungua mojawapo ya miundo, kwa mfano **Biolojia → Flocking**.

### Kanuni Kuu

Baada ya kufungua mfano, unapelekwa kwenye skrini kuu ya NetLogo. Hapa kuna mfano wa mfano unaoelezea idadi ya mbwa mwitu na kondoo, ikizingatiwa rasilimali finyu (nyasi).

![Skrini Kuu ya NetLogo](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.sw.png)

> Picha ya skrini na Dmitry Soshnikov

Kwenye skrini hii, unaweza kuona:

* Sehemu ya **Kiolesura** ambayo ina:
  - Uwanja mkuu, ambapo mawakala wote wanaishi
  - Vidhibiti tofauti: vifungo, slaidi, n.k.
  - Grafu unazoweza kutumia kuonyesha vigezo vya simulizi
* Kichupo cha **Msimbo** ambacho kina mhariri, ambapo unaweza kuandika programu ya NetLogo

Katika hali nyingi, kiolesura kitakuwa na kifungo cha **Setup**, ambacho huanzisha hali ya simulizi, na kifungo cha **Go** kinachoanzisha utekelezaji. Hizi hushughulikiwa na vishughulikiaji vinavyolingana katika msimbo unaoonekana kama huu:

```
to go [
...
]
```

Ulimwengu wa NetLogo unajumuisha vitu vifuatavyo:

* **Mawakala** (kobe) ambao wanaweza kusonga kwenye uwanja na kufanya jambo fulani. Unawaamuru mawakala kwa kutumia sintaksia ya `ask turtles [...]`, na msimbo kwenye mabano unatekelezwa na mawakala wote katika *hali ya kobe*.
* **Sehemu** ni maeneo ya mraba ya uwanja, ambapo mawakala wanaishi. Unaweza kurejelea mawakala wote kwenye sehemu moja, au unaweza kubadilisha rangi za sehemu na mali nyingine. Unaweza pia `ask patches` kufanya jambo fulani.
* **Mwangalizi** ni wakala wa kipekee anayesimamia ulimwengu. Vishughulikiaji vyote vya vifungo hutekelezwa katika *hali ya mwangalizi*.

> ✅ Uzuri wa mazingira ya wakala wengi ni kwamba msimbo unaoendeshwa katika hali ya kobe au hali ya sehemu unatekelezwa kwa wakati mmoja na mawakala wote kwa sambamba. Kwa hivyo, kwa kuandika msimbo kidogo na kupanga tabia ya wakala mmoja, unaweza kuunda tabia changamano ya mfumo wa simulizi kwa ujumla.

### Flocking

Kama mfano wa tabia ya wakala wengi, hebu tuzingatie **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**. Flocking ni muundo changamano unaofanana sana na jinsi makundi ya ndege huruka. Ukiwaangalia wakiruka unaweza kufikiria kwamba wanafuata aina fulani ya algoriti ya pamoja, au kwamba wanamiliki aina fulani ya *akili ya pamoja*. Hata hivyo, tabia hii changamano hutokea wakati kila wakala mmoja (katika kesi hii, *ndege*) anapoangalia mawakala wengine kwa umbali mfupi kutoka kwake, na kufuata sheria tatu rahisi:

* **Ulinganifu** - inajielekeza kuelekea mwelekeo wa wastani wa mawakala wa jirani.
* **Ushirikiano** - inajaribu kuelekea nafasi ya wastani ya majirani (*mvuto wa masafa marefu*).
* **Kutengana** - inapokaribia sana ndege wengine, inajaribu kujiondoa (*kushinikiza kwa masafa mafupi*).

Unaweza kuendesha mfano wa flocking na kuangalia tabia. Unaweza pia kurekebisha vigezo, kama vile *kiwango cha kutengana*, au *masafa ya kuona*, ambayo yanafafanua jinsi kila ndege anavyoweza kuona mbali. Kumbuka kwamba ukipunguza masafa ya kuona hadi 0, ndege wote wanakuwa vipofu, na flocking inakoma. Ukipunguza kutengana hadi 0, ndege wote hukusanyika katika mstari ulionyooka.

> ✅ Badilisha hadi kichupo cha **Msimbo** na uone mahali ambapo sheria tatu za flocking (ulinganifu, ushirikiano na kutengana) zinatekelezwa katika msimbo. Kumbuka jinsi tunavyorejelea tu mawakala walio katika upeo wa macho.

### Miundo Mingine ya Kuona

Kuna miundo mingine ya kuvutia ambayo unaweza kuijaribu:

* **Sanaa → Fireworks** inaonyesha jinsi fataki inaweza kuchukuliwa kuwa tabia ya pamoja ya mito ya moto ya kibinafsi.
* **Sayansi ya Jamii → Traffic Basic** na **Sayansi ya Jamii → Traffic Grid** zinaonyesha mfano wa trafiki ya jiji katika Gridi ya 1D na 2D yenye au bila taa za trafiki. Kila gari katika simulizi hufuata sheria zifuatazo:
   - Ikiwa nafasi mbele yake iko wazi - ongeza kasi (hadi kasi fulani ya juu).
   - Ikiwa linaona kikwazo mbele - punguza kasi (na unaweza kurekebisha jinsi dereva anavyoweza kuona mbali).
* **Sayansi ya Jamii → Party** inaonyesha jinsi watu wanavyokusanyika pamoja wakati wa sherehe ya vinywaji. Unaweza kupata mchanganyiko wa vigezo vinavyopelekea ongezeko la haraka la furaha ya kikundi.

Kama unavyoona kutoka kwa mifano hii, simulizi za wakala wengi zinaweza kuwa njia muhimu ya kuelewa tabia ya mfumo changamano unaojumuisha watu binafsi wanaofuata mantiki sawa au inayofanana. Pia inaweza kutumika kudhibiti mawakala wa kawaida, kama [NPCs](https://en.wikipedia.org/wiki/NPC) katika michezo ya kompyuta, au mawakala katika ulimwengu wa 3D uliotengenezwa.

## Mawakala Wenye Kufikiri

Mawakala waliotajwa hapo juu ni rahisi sana, wakijibu mabadiliko katika mazingira kwa kutumia aina fulani ya algoriti. Kwa hivyo wao ni **mawakala wenye majibu**. Hata hivyo, wakati mwingine mawakala wanaweza kufikiri na kupanga vitendo vyao, ambapo wanaitwa **wenye kufikiri**.

Mfano wa kawaida ungekuwa wakala wa kibinafsi anayepokea maagizo kutoka kwa binadamu ya kuweka nafasi ya ziara ya likizo. Fikiria kwamba kuna mawakala wengi wanaoishi kwenye mtandao, ambao wanaweza kumsaidia. Inapaswa kisha kuwasiliana na mawakala wengine kuona ni safari gani zinapatikana, bei za hoteli kwa tarehe tofauti, na kujaribu kujadiliana bei bora. Mpango wa likizo unapokamilika na kuthibitishwa na mmiliki, inaweza kuendelea na uhifadhi.

Ili kufanya hivyo, mawakala wanahitaji **kuwasiliana**. Kwa mawasiliano yenye mafanikio wanahitaji:

* Baadhi ya **lugha za kawaida za kubadilishana maarifa**, kama [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) na [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Lugha hizi zimetengenezwa kulingana na [nadharia ya Matendo ya Hotuba](https://en.wikipedia.org/wiki/Speech_act).
* Lugha hizo zinapaswa pia kujumuisha baadhi ya **taratibu za mazungumzo**, kulingana na aina tofauti za **mnada**.
* **Ontolojia ya kawaida** ya kutumia, ili waweze kurejelea dhana zile zile wakijua maana yake.
* Njia ya **kugundua** kile mawakala tofauti wanaweza kufanya, pia kulingana na aina fulani ya ontolojia.

Mawakala wenye kufikiri ni changamano zaidi kuliko wenye majibu, kwa sababu hawajibu tu mabadiliko katika mazingira, wanapaswa pia kuwa na uwezo wa *kuanzisha* vitendo. Mojawapo ya usanifu uliopendekezwa kwa mawakala wenye kufikiri ni wakala wa Imani-Tamaa-Nia (BDI):

* **Imani** huunda seti ya maarifa kuhusu mazingira ya wakala. Inaweza kuwa na muundo kama msingi wa maarifa au seti ya sheria ambazo wakala anaweza kutumia kwa hali maalum katika mazingira.
* **Tamaa** hufafanua kile wakala anataka kufanya, yaani malengo yake. Kwa mfano, lengo la wakala msaidizi wa kibinafsi hapo juu ni kuweka nafasi ya ziara, na lengo la wakala wa hoteli ni kuongeza faida.
* **Nia** ni vitendo maalum ambavyo wakala anapanga kufanikisha malengo yake. Vitendo mara nyingi hubadilisha mazingira na kusababisha mawasiliano na mawakala wengine.

Kuna majukwaa kadhaa yanayopatikana kwa ajili ya kujenga mifumo ya wakala wengi, kama [JADE](https://jade.tilab.com/). [Karatasi hii](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) ina mapitio ya majukwaa ya wakala wengi, pamoja na historia fupi ya mifumo ya wakala wengi na hali zake tofauti za matumizi.

## Hitimisho

Mifumo ya Wakala Wengi inaweza kuchukua aina tofauti sana na kutumika katika programu nyingi tofauti. 
Yote huwa na mwelekeo wa tabia rahisi ya wakala mmoja, na kufanikisha tabia changamano ya mfumo mzima kutokana na **athari ya synergetic**.

## 🚀 Changamoto

Chukua somo hili katika ulimwengu halisi na jaribu kufikiria mfumo wa wakala wengi ambao unaweza kutatua tatizo. Kwa mfano, mfumo wa wakala wengi ungehitaji kufanya nini ili kuboresha njia ya basi la shule? Unaweza kufanya kazi vipi katika mkate?

## [Jaribio la Baada ya Somo](https://ff-quizzes.netlify.app/en/ai/quiz/46)

## Mapitio na Kujifunza Binafsi

Pitia matumizi ya aina hii ya mfumo katika sekta. Chagua uwanja kama utengenezaji au sekta ya michezo ya video na gundua jinsi mifumo ya wakala wengi inaweza kutumika kutatua matatizo ya kipekee.

## [Kazi ya NetLogo](assignment.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.