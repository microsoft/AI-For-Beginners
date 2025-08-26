<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1c6b8c7c1778a35fc1139b7f2aecb7b3",
  "translation_date": "2025-08-25T20:59:56+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "sw"
}
-->
# Utangulizi wa Mitandao ya Neural

![Muhtasari wa maudhui ya Utangulizi wa Mitandao ya Neural katika mchoro](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.sw.png)

Kama tulivyojadili katika utangulizi, mojawapo ya njia za kufanikisha akili ni kufundisha **mfano wa kompyuta** au **ubongo wa bandia**. Tangu katikati ya karne ya 20, watafiti walijaribu mifano mbalimbali ya kihesabu, hadi miaka ya hivi karibuni ambapo mwelekeo huu ulithibitishwa kuwa na mafanikio makubwa. Mifano hii ya kihesabu ya ubongo inaitwa **mitandao ya neural**.

> Wakati mwingine mitandao ya neural huitwa *Mitandao ya Neural ya Bandia*, ANNs, ili kuonyesha kwamba tunazungumzia mifano, si mitandao halisi ya neurons.

## Kujifunza kwa Mashine

Mitandao ya Neural ni sehemu ya taaluma kubwa inayoitwa **Kujifunza kwa Mashine**, ambayo lengo lake ni kutumia data kufundisha mifano ya kompyuta inayoweza kutatua matatizo. Kujifunza kwa Mashine ni sehemu kubwa ya Akili Bandia, hata hivyo, hatutashughulikia ML ya kawaida katika mtaala huu.

> Tembelea mtaala wetu tofauti wa **[Kujifunza kwa Mashine kwa Kompyuta za Kuanza](http://github.com/microsoft/ml-for-beginners)** ili kujifunza zaidi kuhusu Kujifunza kwa Mashine ya kawaida.

Katika Kujifunza kwa Mashine, tunadhani kwamba tuna seti ya data ya mifano **X**, na thamani za matokeo zinazolingana **Y**. Mifano mara nyingi ni vekta za N-dimensional zinazojumuisha **vipengele**, na matokeo huitwa **lebo**.

Tutazingatia matatizo mawili ya kawaida ya kujifunza kwa mashine:

* **Uainishaji**, ambapo tunahitaji kuainisha kitu cha pembejeo katika darasa mbili au zaidi.
* **Urejeshaji**, ambapo tunahitaji kutabiri namba ya nambari kwa kila sampuli ya pembejeo.

> Wakati wa kuwakilisha pembejeo na matokeo kama tensors, seti ya data ya pembejeo ni matriki ya ukubwa M×N, ambapo M ni idadi ya sampuli na N ni idadi ya vipengele. Lebo za matokeo Y ni vekta ya ukubwa M.

Katika mtaala huu, tutazingatia tu mifano ya mitandao ya neural.

## Mfano wa Neuron

Kutoka kwa biolojia tunajua kwamba ubongo wetu unajumuisha seli za neural, kila moja ikiwa na "pembejeo" nyingi (axons), na matokeo (dendrite). Axons na dendrites zinaweza kusafirisha ishara za umeme, na miunganisho kati ya axons na dendrites inaweza kuonyesha viwango tofauti vya usafirishaji (inayodhibitiwa na neuromediators).

![Mfano wa Neuron](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.sw.jpg) | ![Mfano wa Neuron](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.sw.png)
----|----
Neuron Halisi *([Picha](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) kutoka Wikipedia)* | Neuron ya Bandia *(Picha na Mwandishi)*

Kwa hivyo, mfano rahisi wa kihesabu wa neuron una pembejeo kadhaa X<sub>1</sub>, ..., X<sub>N</sub> na matokeo Y, na mfululizo wa uzito W<sub>1</sub>, ..., W<sub>N</sub>. Matokeo yanahesabiwa kama:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

ambapo f ni **kazi ya uanzishaji** isiyo ya mstari.

> Mifano ya awali ya neuron ilielezewa katika karatasi ya kawaida [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) na Warren McCullock na Walter Pitts mwaka 1943. Donald Hebb katika kitabu chake "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" alipendekeza njia ambazo mitandao hiyo inaweza kufundishwa.

## Katika Sehemu Hii

Katika sehemu hii tutajifunza kuhusu:
* [Perceptron](03-Perceptron/README.md), mojawapo ya mifano ya awali ya mitandao ya neural kwa uainishaji wa darasa mbili
* [Mitandao ya Tabaka Nyingi](04-OwnFramework/README.md) na daftari lililoambatanishwa [jinsi ya kujenga mfumo wetu wenyewe](../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)
* [Mifumo ya Mitandao ya Neural](05-Frameworks/README.md), na daftari hizi: [PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) na [Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.