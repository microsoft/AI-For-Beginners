<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-25T21:01:25+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "sw"
}
-->
# Utangulizi wa Mitandao ya Neural: Perceptron

## [Jaribio la kabla ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Moja ya majaribio ya kwanza ya kutekeleza kitu kinachofanana na mtandao wa neural wa kisasa yalifanywa na Frank Rosenblatt kutoka Maabara ya Anga ya Cornell mwaka 1957. Ilikuwa ni utekelezaji wa vifaa vilivyoitwa "Mark-1", iliyoundwa kutambua maumbo ya kijiometri rahisi, kama vile pembetatu, miraba na miduara.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Picha [kutoka Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Picha ya ingizo iliwakilishwa na safu ya seli za picha 20x20, hivyo mtandao wa neural ulikuwa na viingizo 400 na pato moja la binary. Mtandao rahisi ulikuwa na neuron moja, pia inayoitwa **kitengo cha mantiki ya kizingiti**. Uzito wa mtandao wa neural ulifanya kazi kama potentiometer ambazo zilihitaji kurekebishwa kwa mikono wakati wa awamu ya mafunzo.

> ✅ Potentiometer ni kifaa kinachoruhusu mtumiaji kurekebisha upinzani wa mzunguko.

> The New York Times iliandika kuhusu perceptron wakati huo: *kiinitete cha kompyuta ya kielektroniki ambayo [Jeshi la Wanamaji] linatarajia itaweza kutembea, kuzungumza, kuona, kuandika, kujizalisha yenyewe na kufahamu uwepo wake.*

## Mfano wa Perceptron

Tuseme tuna vipengele N katika mfano wetu, ambapo vector ya ingizo itakuwa vector ya ukubwa N. Perceptron ni mfano wa **uainishaji wa binary**, yaani inaweza kutofautisha kati ya madarasa mawili ya data ya ingizo. Tutadhani kwamba kwa kila vector ya ingizo x, pato la perceptron yetu litakuwa aidha +1 au -1, kulingana na darasa. Pato litahesabiwa kwa kutumia fomula:

y(x) = f(w<sup>T</sup>x)

ambapo f ni kazi ya uanzishaji wa hatua

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Mafunzo ya Perceptron

Ili kufundisha perceptron tunahitaji kupata vector ya uzito w ambayo inatofautisha kwa usahihi thamani nyingi, yaani inasababisha **kosa** dogo zaidi. Kosa hili E linafafanuliwa na **kigezo cha perceptron** kwa njia ifuatayo:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ambapo:

* jumla inachukuliwa kwa zile data za mafunzo i ambazo zinasababisha uainishaji usio sahihi
* x<sub>i</sub> ni data ya ingizo, na t<sub>i</sub> ni aidha -1 au +1 kwa mifano hasi na chanya ipasavyo.

Kigezo hiki kinachukuliwa kama kazi ya uzito w, na tunahitaji kukipunguza. Mara nyingi, njia inayoitwa **gradient descent** hutumika, ambapo tunaanza na uzito wa awali w<sup>(0)</sup>, na kisha kila hatua tunasasisha uzito kulingana na fomula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Hapa η ni kinachoitwa **kiwango cha kujifunza**, na ∇E(w) inaonyesha **gradienti** ya E. Baada ya kuhesabu gradienti, tunapata:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algorithimu katika Python inaonekana hivi:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Hitimisho

Katika somo hili, umejifunza kuhusu perceptron, ambayo ni mfano wa uainishaji wa binary, na jinsi ya kuifundisha kwa kutumia vector ya uzito.

## 🚀 Changamoto

Ikiwa ungependa kujaribu kujenga perceptron yako mwenyewe, jaribu [maabara hii kwenye Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) ambayo inatumia [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Jaribio la baada ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Mapitio na Kujisomea

Ili kuona jinsi tunavyoweza kutumia perceptron kutatua tatizo la mfano pamoja na matatizo ya maisha halisi, na kuendelea kujifunza - nenda kwenye daftari la [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb).

Hapa kuna [makala ya kuvutia kuhusu perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590
) pia.

## [Kazi ya Nyumbani](lab/README.md)

Katika somo hili, tumetekeleza perceptron kwa kazi ya uainishaji wa binary, na tumeitumia kutofautisha kati ya tarakimu mbili zilizoandikwa kwa mkono. Katika maabara hii, unaombwa kutatua tatizo la uainishaji wa tarakimu kikamilifu, yaani kubaini ni tarakimu gani inayowezekana zaidi kuendana na picha fulani.

* [Maelekezo](lab/README.md)
* [Daftari](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.