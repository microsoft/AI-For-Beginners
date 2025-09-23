<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98c5222ff9556b55223fed2337145e18",
  "translation_date": "2025-08-28T02:34:59+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "tl"
}
-->
*Image [mula sa Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), By Longlivetheux - Own work, CC BY-SA 4.0*

Kaya, ang problema ng **representasyon ng kaalaman** ay ang paghahanap ng epektibong paraan upang maipakita ang kaalaman sa loob ng isang computer sa anyo ng data, upang magamit ito nang awtomatiko. Ito ay maaaring makita bilang isang spectrum:

![Spectrum ng representasyon ng kaalaman](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.tl.png)

> Larawan ni [Dmitry Soshnikov](http://soshnikov.com)

* Sa kaliwa, mayroong napakasimpleng uri ng representasyon ng kaalaman na maaaring epektibong magamit ng mga computer. Ang pinakasimple ay algorithmic, kung saan ang kaalaman ay kinakatawan ng isang computer program. Gayunpaman, hindi ito ang pinakamahusay na paraan upang kumatawan sa kaalaman, dahil hindi ito flexible. Ang kaalaman sa ating isipan ay kadalasang hindi algorithmic.
* Sa kanan, may mga representasyon tulad ng natural na teksto. Ito ang pinakamakapangyarihan, ngunit hindi magagamit para sa awtomatikong pangangatwiran.

> ✅ Mag-isip ng isang minuto kung paano mo kinakatawan ang kaalaman sa iyong isipan at isinasalin ito sa mga tala. Mayroon bang partikular na format na epektibo para sa iyo upang makatulong sa pag-alala?

## Pag-uuri ng Representasyon ng Kaalaman sa Computer

Maaari nating uriin ang iba't ibang paraan ng representasyon ng kaalaman sa computer sa mga sumusunod na kategorya:

* **Network representations** ay batay sa katotohanan na mayroon tayong network ng magkakaugnay na konsepto sa loob ng ating isipan. Maaari nating subukang muling likhain ang parehong mga network bilang isang graph sa loob ng isang computer - ang tinatawag na **semantic network**.

1. **Object-Attribute-Value triplets** o **attribute-value pairs**. Dahil ang isang graph ay maaaring kumatawan sa loob ng isang computer bilang isang listahan ng mga nodes at edges, maaari nating kumatawan sa isang semantic network sa pamamagitan ng isang listahan ng mga triplets, na naglalaman ng mga object, attributes, at values. Halimbawa, bumuo tayo ng mga sumusunod na triplets tungkol sa mga programming language:

Object | Attribute | Value
-------|-----------|------
Python | ay | Untyped-Language
Python | imbento-ni | Guido van Rossum
Python | block-syntax | indentation
Untyped-Language | walang | type definitions

> ✅ Mag-isip kung paano magagamit ang mga triplets upang kumatawan sa iba pang uri ng kaalaman.

2. **Hierarchical representations** binibigyang-diin ang katotohanan na madalas tayong lumikha ng hierarchy ng mga object sa loob ng ating isipan. Halimbawa, alam natin na ang canary ay isang ibon, at lahat ng ibon ay may pakpak. Mayroon din tayong ideya kung anong kulay ang karaniwang canary, at kung ano ang bilis ng kanilang paglipad.

   - **Frame representation** ay batay sa representasyon ng bawat object o klase ng mga object bilang isang **frame** na naglalaman ng **slots**. Ang mga slots ay may posibleng default na mga halaga, mga limitasyon sa halaga, o mga nakaimbak na pamamaraan na maaaring tawagin upang makuha ang halaga ng isang slot. Ang lahat ng mga frame ay bumubuo ng isang hierarchy na katulad ng hierarchy ng object sa mga object-oriented programming language.
   - **Scenarios** ay espesyal na uri ng mga frame na kumakatawan sa mga kumplikadong sitwasyon na maaaring maganap sa paglipas ng panahon.

**Python**

Slot | Value | Default value | Interval |
-----|-------|---------------|----------|
Name | Python | | |
Is-A | Untyped-Language | | |
Variable Case | | CamelCase | |
Program Length | | | 5-5000 lines |
Block Syntax | Indent | | |

3. **Procedural representations** ay batay sa representasyon ng kaalaman sa pamamagitan ng isang listahan ng mga aksyon na maaaring isagawa kapag naganap ang isang tiyak na kondisyon.
   - Production rules ay mga if-then statements na nagpapahintulot sa atin na gumawa ng mga konklusyon. Halimbawa, ang isang doktor ay maaaring magkaroon ng panuntunan na nagsasabing **KUNG** ang isang pasyente ay may mataas na lagnat **O** mataas na antas ng C-reactive protein sa blood test **KUNG GAYON** siya ay may pamamaga. Kapag nakatagpo tayo ng isa sa mga kondisyon, maaari tayong gumawa ng konklusyon tungkol sa pamamaga, at pagkatapos ay gamitin ito sa karagdagang pangangatwiran.
   - Ang mga algorithm ay maaaring ituring na isa pang anyo ng procedural representation, bagaman halos hindi sila direktang ginagamit sa mga knowledge-based system.

4. **Logic** ay orihinal na iminungkahi ni Aristotle bilang isang paraan upang kumatawan sa unibersal na kaalaman ng tao.
   - Predicate Logic bilang isang mathematical theory ay masyadong mayaman upang maging computable, kaya't ang ilang subset nito ay karaniwang ginagamit, tulad ng Horn clauses na ginagamit sa Prolog.
   - Descriptive Logic ay isang pamilya ng mga logical systems na ginagamit upang kumatawan at mangatwiran tungkol sa mga hierarchy ng mga object na ipinamamahagi sa mga representasyon ng kaalaman tulad ng *semantic web*.

## Expert Systems

Isa sa mga maagang tagumpay ng symbolic AI ay ang tinatawag na **expert systems** - mga computer system na idinisenyo upang kumilos bilang isang eksperto sa ilang limitadong domain ng problema. Ang mga ito ay batay sa isang **knowledge base** na nakuha mula sa isa o higit pang mga eksperto sa tao, at naglalaman ng isang **inference engine** na gumagawa ng ilang pangangatwiran sa ibabaw nito.

![Arkitektura ng Tao](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.tl.png) | ![Knowledge-Based System](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.tl.png)
---------------------------------------------|------------------------------------------------
Pinadaling istruktura ng neural system ng tao | Arkitektura ng isang knowledge-based system

Ang mga expert systems ay binuo tulad ng sistema ng pangangatwiran ng tao, na naglalaman ng **short-term memory** at **long-term memory**. Katulad nito, sa mga knowledge-based systems, tinutukoy natin ang mga sumusunod na bahagi:

* **Problem memory**: naglalaman ng kaalaman tungkol sa problemang kasalukuyang nilulutas, halimbawa ang temperatura o presyon ng dugo ng isang pasyente, kung siya ay may pamamaga o wala, atbp. Ang kaalamang ito ay tinatawag ding **static knowledge**, dahil naglalaman ito ng snapshot ng kung ano ang kasalukuyang alam natin tungkol sa problema - ang tinatawag na *problem state*.
* **Knowledge base**: kumakatawan sa pangmatagalang kaalaman tungkol sa domain ng problema. Ito ay manu-manong nakuha mula sa mga eksperto sa tao, at hindi nagbabago mula sa konsultasyon hanggang sa konsultasyon. Dahil pinapayagan tayo nitong mag-navigate mula sa isang problem state patungo sa isa pa, ito ay tinatawag ding **dynamic knowledge**.
* **Inference engine**: nag-oorganisa ng buong proseso ng paghahanap sa problem state space, nagtatanong sa user kung kinakailangan. Ito rin ang responsable sa paghahanap ng tamang mga panuntunan na dapat ilapat sa bawat estado.

Bilang halimbawa, isaalang-alang natin ang sumusunod na expert system sa pagtukoy ng isang hayop batay sa mga pisikal na katangian nito:

![AND-OR Tree](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.tl.png)

> Larawan ni [Dmitry Soshnikov](http://soshnikov.com)

Ang diagram na ito ay tinatawag na **AND-OR tree**, at ito ay isang graphical na representasyon ng isang set ng production rules. Ang pagguhit ng puno ay kapaki-pakinabang sa simula ng pagkuha ng kaalaman mula sa eksperto. Upang kumatawan sa kaalaman sa loob ng computer, mas maginhawa ang paggamit ng mga panuntunan:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Mapapansin mo na ang bawat kondisyon sa kaliwang bahagi ng panuntunan at ang aksyon ay mahalagang object-attribute-value (OAV) triplets. Ang **working memory** ay naglalaman ng set ng OAV triplets na tumutugma sa problemang kasalukuyang nilulutas. Ang isang **rules engine** ay naghahanap ng mga panuntunan kung saan ang isang kondisyon ay nasiyahan at inilalapat ang mga ito, na nagdaragdag ng isa pang triplet sa working memory.

> ✅ Gumawa ng sarili mong AND-OR tree sa isang paksang gusto mo!

### Forward vs. Backward Inference

Ang prosesong inilarawan sa itaas ay tinatawag na **forward inference**. Nagsisimula ito sa ilang paunang data tungkol sa problema na magagamit sa working memory, at pagkatapos ay isinasagawa ang sumusunod na reasoning loop:

1. Kung ang target attribute ay naroroon sa working memory - huminto at ibigay ang resulta
2. Hanapin ang lahat ng mga panuntunan kung saan ang kondisyon ay kasalukuyang nasiyahan - makuha ang **conflict set** ng mga panuntunan.
3. Isagawa ang **conflict resolution** - pumili ng isang panuntunan na isasagawa sa hakbang na ito. Maaaring may iba't ibang conflict resolution strategies:
   - Piliin ang unang naaangkop na panuntunan sa knowledge base
   - Piliin ang random na panuntunan
   - Piliin ang *mas tiyak* na panuntunan, ibig sabihin, ang isa na tumutugon sa pinakamaraming kondisyon sa "left-hand-side" (LHS)
4. Ilapat ang napiling panuntunan at ipasok ang bagong piraso ng kaalaman sa problem state
5. Ulitin mula sa hakbang 1.

Gayunpaman, sa ilang mga kaso maaaring gusto nating magsimula sa walang kaalaman tungkol sa problema, at magtanong ng mga tanong na makakatulong sa atin na makarating sa konklusyon. Halimbawa, kapag gumagawa ng medikal na diagnosis, karaniwang hindi natin isinasagawa ang lahat ng medikal na pagsusuri nang maaga bago simulan ang pag-diagnose sa pasyente. Sa halip, gusto nating magsagawa ng pagsusuri kapag kailangan ng desisyon.

Ang prosesong ito ay maaaring i-modelo gamit ang **backward inference**. Ito ay hinihimok ng **goal** - ang halaga ng attribute na hinahanap natin:

1. Piliin ang lahat ng mga panuntunan na maaaring magbigay sa atin ng halaga ng isang goal (ibig sabihin, may goal sa RHS ("right-hand-side")) - isang conflict set
1. Kung walang mga panuntunan para sa attribute na ito, o mayroong panuntunan na nagsasabing dapat nating tanungin ang halaga mula sa user - tanungin ito, kung hindi:
1. Gumamit ng conflict resolution strategy upang pumili ng isang panuntunan na gagamitin bilang *hypothesis* - susubukan nating patunayan ito
1. Paulit-ulit na ulitin ang proseso para sa lahat ng mga attribute sa LHS ng panuntunan, sinusubukang patunayan ang mga ito bilang mga goal
1. Kung sa anumang punto ang proseso ay nabigo - gumamit ng ibang panuntunan sa hakbang 3.

> ✅ Sa anong mga sitwasyon mas angkop ang forward inference? Paano naman ang backward inference?

### Pagpapatupad ng Expert Systems

Ang mga expert systems ay maaaring ipatupad gamit ang iba't ibang mga tool:

* Pagprograma ng mga ito nang direkta sa ilang high-level programming language. Hindi ito ang pinakamahusay na ideya, dahil ang pangunahing bentahe ng isang knowledge-based system ay ang kaalaman ay hiwalay sa inference, at potensyal na ang isang eksperto sa domain ng problema ay dapat na makapagsulat ng mga panuntunan nang hindi nauunawaan ang mga detalye ng proseso ng inference.
* Paggamit ng **expert systems shell**, ibig sabihin, isang sistema na partikular na idinisenyo upang mapunan ng kaalaman gamit ang ilang knowledge representation language.

## ✍️ Ehersisyo: Animal Inference

Tingnan ang [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) para sa isang halimbawa ng pagpapatupad ng forward at backward inference expert system.
> **Tandaan**: Ang halimbawang ito ay medyo simple lamang, at nagbibigay lamang ng ideya kung paano ang hitsura ng isang ekspertong sistema. Kapag nagsimula kang lumikha ng ganitong sistema, mapapansin mo lamang ang ilang *matalinong* kilos mula rito kapag umabot ka na sa tiyak na bilang ng mga patakaran, mga 200 pataas. Sa isang punto, nagiging masyadong kumplikado ang mga patakaran upang maalala ang lahat ng mga ito, at sa puntong ito maaari mong simulan ang pag-iisip kung bakit gumagawa ng ilang mga desisyon ang sistema. Gayunpaman, ang mahalagang katangian ng mga sistemang nakabatay sa kaalaman ay palagi mong *maipapaliwanag* nang eksakto kung paano ginawa ang alinman sa mga desisyon.
## Ontolohiya at ang Semantic Web

Sa pagtatapos ng ika-20 siglo, nagkaroon ng inisyatibo na gamitin ang representasyon ng kaalaman upang maglagay ng anotasyon sa mga mapagkukunan sa Internet, upang mas madali itong mahanap batay sa napaka-espesipikong mga query. Ang kilusang ito ay tinawag na **Semantic Web**, at nakabatay ito sa ilang mga konsepto:

- Isang espesyal na representasyon ng kaalaman na nakabatay sa **[description logics](https://en.wikipedia.org/wiki/Description_logic)** (DL). Katulad ito ng frame knowledge representation, dahil bumubuo ito ng hierarchy ng mga bagay na may mga katangian, ngunit may pormal na lohikal na semantika at inference. Mayroong buong pamilya ng DLs na nagbabalanse sa pagitan ng pagiging mas detalyado at algorithmic complexity ng inference.
- Distributed na representasyon ng kaalaman, kung saan ang lahat ng konsepto ay kinakatawan ng isang global URI identifier, na nagbibigay-daan upang makabuo ng mga hierarchy ng kaalaman na sumasaklaw sa internet.
- Isang pamilya ng mga XML-based na wika para sa paglalarawan ng kaalaman: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Ang pangunahing konsepto sa Semantic Web ay ang konsepto ng **Ontology**. Tumutukoy ito sa isang malinaw na espesipikasyon ng isang problem domain gamit ang pormal na representasyon ng kaalaman. Ang pinakasimpleng ontolohiya ay maaaring isang hierarchy lamang ng mga bagay sa isang problem domain, ngunit ang mas kumplikadong ontolohiya ay may kasamang mga patakaran na maaaring gamitin para sa inference.

Sa Semantic Web, lahat ng representasyon ay nakabatay sa triplets. Ang bawat bagay at bawat relasyon ay natatanging kinikilala ng URI. Halimbawa, kung nais nating ipahayag ang katotohanan na ang AI Curriculum na ito ay binuo ni Dmitry Soshnikov noong Enero 1, 2022 - narito ang mga triplets na maaari nating gamitin:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Dito, ang `http://www.example.com/terms/creation-date` at `http://purl.org/dc/elements/1.1/creator` ay ilan sa mga kilala at pangkalahatang tinatanggap na URIs upang ipahayag ang mga konsepto ng *creator* at *creation date*.

Sa mas kumplikadong kaso, kung nais nating tukuyin ang isang listahan ng mga creator, maaari tayong gumamit ng ilang mga istruktura ng datos na tinukoy sa RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Ang mga diagram sa itaas ay mula kay [Dmitry Soshnikov](http://soshnikov.com)

Ang progreso ng pagbuo ng Semantic Web ay bahagyang bumagal dahil sa tagumpay ng mga search engine at mga teknolohiya ng natural language processing, na nagbibigay-daan sa pagkuha ng structured na datos mula sa teksto. Gayunpaman, sa ilang mga larangan, may mga makabuluhang pagsisikap pa rin upang mapanatili ang mga ontolohiya at mga knowledge base. Ilan sa mga proyektong dapat pansinin:

* [WikiData](https://wikidata.org/) ay isang koleksyon ng machine-readable na mga knowledge base na konektado sa Wikipedia. Karamihan sa datos ay minina mula sa Wikipedia *InfoBoxes*, mga piraso ng structured na nilalaman sa loob ng mga pahina ng Wikipedia. Maaari mong [i-query](https://query.wikidata.org/) ang WikiData gamit ang SPARQL, isang espesyal na query language para sa Semantic Web. Narito ang isang sample query na nagpapakita ng pinakasikat na kulay ng mata sa mga tao:

```sparql
#defaultView:BubbleChart
SELECT ?eyeColorLabel (COUNT(?human) AS ?count)
WHERE
{
  ?human wdt:P31 wd:Q5.       # human instance-of homo sapiens
  ?human wdt:P1340 ?eyeColor. # human eye-color ?eyeColor
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?eyeColorLabel
```

* [DBpedia](https://www.dbpedia.org/) ay isa pang proyekto na katulad ng WikiData.

> ✅ Kung nais mong mag-eksperimento sa pagbuo ng sarili mong ontolohiya, o pagbubukas ng mga umiiral na ontolohiya, mayroong mahusay na visual ontology editor na tinatawag na [Protégé](https://protege.stanford.edu/). I-download ito, o gamitin online.

<img src="images/protege.png" width="70%"/>

*Web Protégé editor na bukas gamit ang Romanov Family ontology. Screenshot ni Dmitry Soshnikov*

## ✍️ Ehersisyo: Isang Ontolohiya ng Pamilya

Tingnan ang [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) para sa isang halimbawa ng paggamit ng mga teknik ng Semantic Web upang magbigay ng lohikal na pagsusuri sa mga relasyon ng pamilya. Kukunin natin ang isang family tree na kinakatawan sa karaniwang GEDCOM format at isang ontolohiya ng mga relasyon ng pamilya upang bumuo ng graph ng lahat ng relasyon ng pamilya para sa isang ibinigay na hanay ng mga indibidwal.

## Microsoft Concept Graph

Sa karamihan ng mga kaso, ang mga ontolohiya ay maingat na nilikha nang manu-mano. Gayunpaman, posible rin na **minahin** ang mga ontolohiya mula sa unstructured na datos, halimbawa, mula sa mga natural language na teksto.

Isa sa mga ganitong pagsubok ay ginawa ng Microsoft Research, na nagresulta sa [Microsoft Concept Graph](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Ito ay isang malaking koleksyon ng mga entity na pinagsama-sama gamit ang `is-a` inheritance relationship. Pinapayagan nitong sagutin ang mga tanong tulad ng "Ano ang Microsoft?" - ang sagot ay maaaring "isang kumpanya na may posibilidad na 0.87, at isang brand na may posibilidad na 0.75".

Ang Graph ay magagamit bilang REST API, o bilang isang malaking downloadable na text file na naglilista ng lahat ng mga pares ng entity.

## ✍️ Ehersisyo: Isang Concept Graph

Subukan ang [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) notebook upang makita kung paano natin magagamit ang Microsoft Concept Graph upang i-grupo ang mga balita sa iba't ibang kategorya.

## Konklusyon

Sa kasalukuyan, ang AI ay madalas na itinuturing na kasingkahulugan ng *Machine Learning* o *Neural Networks*. Gayunpaman, ang tao ay nagpapakita rin ng malinaw na pangangatwiran, na isang bagay na hindi pa ganap na natutugunan ng neural networks. Sa mga tunay na proyekto, ang malinaw na pangangatwiran ay ginagamit pa rin upang magsagawa ng mga gawain na nangangailangan ng paliwanag, o kakayahang baguhin ang pag-uugali ng sistema sa isang kontroladong paraan.

## 🚀 Hamon

Sa Family Ontology notebook na kaugnay ng araling ito, may pagkakataon kang mag-eksperimento sa iba pang mga relasyon ng pamilya. Subukang tuklasin ang mga bagong koneksyon sa pagitan ng mga tao sa family tree.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/4)

## Review at Pag-aaral sa Sarili

Magsaliksik sa internet upang matuklasan ang mga larangan kung saan sinubukan ng tao na sukatin at i-codify ang kaalaman. Tingnan ang Bloom's Taxonomy, at balikan ang kasaysayan upang matutunan kung paano sinubukan ng tao na unawain ang kanilang mundo. Suriin ang gawain ni Linnaeus sa paglikha ng taxonomy ng mga organismo, at obserbahan kung paano nilikha ni Dmitri Mendeleev ang paraan upang maipaliwanag at ma-grupo ang mga elementong kemikal. Anong iba pang mga kawili-wiling halimbawa ang maaari mong makita?

**Takdang Aralin**: [Bumuo ng Ontolohiya](assignment.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.