<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dbacf9b1915612981d76059678e563e5",
  "translation_date": "2025-08-25T20:58:44+00:00",
  "source_file": "lessons/6-Other/22-DeepRL/README.md",
  "language_code": "sw"
}
-->
# Kujifunza Kuimarisha kwa Kina

Kujifunza kuimarisha (RL) kunachukuliwa kama mojawapo ya mifumo ya msingi ya kujifunza kwa mashine, sambamba na kujifunza kwa kusimamiwa na kujifunza bila kusimamiwa. Wakati katika kujifunza kwa kusimamiwa tunategemea seti ya data yenye matokeo yanayojulikana, RL inategemea **kujifunza kwa kufanya**. Kwa mfano, tunapoona mchezo wa kompyuta kwa mara ya kwanza, tunaanza kucheza hata bila kujua sheria, na hivi karibuni tunaweza kuboresha ujuzi wetu kupitia mchakato wa kucheza na kurekebisha tabia zetu.

## [Jaribio la kabla ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

Ili kufanya RL, tunahitaji:

* **Mazingira** au **simulator** inayoweka sheria za mchezo. Tunapaswa kuwa na uwezo wa kuendesha majaribio kwenye simulator na kuchunguza matokeo.
* **Kazi ya Tuzo**, ambayo inaonyesha jinsi jaribio letu lilivyofanikiwa. Katika hali ya kujifunza kucheza mchezo wa kompyuta, tuzo inaweza kuwa alama yetu ya mwisho.

Kwa kuzingatia kazi ya tuzo, tunapaswa kuwa na uwezo wa kurekebisha tabia zetu na kuboresha ujuzi wetu, ili mara nyingine tunapocheza tufanye vizuri zaidi. Tofauti kuu kati ya aina nyingine za kujifunza kwa mashine na RL ni kwamba katika RL hatujui kama tumeshinda au tumeshindwa hadi mchezo umalizike. Kwa hivyo, hatuwezi kusema kama hatua fulani peke yake ni nzuri au la - tunapokea tuzo mwishoni mwa mchezo.

Wakati wa RL, mara nyingi tunafanya majaribio mengi. Katika kila jaribio, tunahitaji kusawazisha kati ya kufuata mkakati bora ambao tumeshajifunza (**kuchuma**) na kuchunguza hali mpya zinazowezekana (**kuchunguza**).

## OpenAI Gym

Zana nzuri kwa RL ni [OpenAI Gym](https://gym.openai.com/) - **mazingira ya simulizi**, ambayo yanaweza kuiga mazingira mengi tofauti kuanzia michezo ya Atari hadi fizikia ya kusawazisha nguzo. Ni mojawapo ya mazingira maarufu ya simulizi kwa mafunzo ya algorithimu za kujifunza kuimarisha, na inadumishwa na [OpenAI](https://openai.com/).

> **Note**: Unaweza kuona mazingira yote yanayopatikana kutoka OpenAI Gym [hapa](https://gym.openai.com/envs/#classic_control).

## Kusawazisha CartPole

Pengine nyote mmeona vifaa vya kisasa vya kusawazisha kama *Segway* au *Gyroscooters*. Vinaweza kusawazisha kiotomatiki kwa kurekebisha magurudumu yao kwa kujibu ishara kutoka kwa kipima kasi au gyroscope. Katika sehemu hii, tutajifunza jinsi ya kutatua tatizo kama hilo - kusawazisha nguzo. Ni sawa na hali ambapo mcheza sarakasi anahitaji kusawazisha nguzo kwenye mkono wake - lakini kusawazisha huku kunafanyika tu katika mwelekeo mmoja (1D).

Toleo rahisi la kusawazisha linajulikana kama tatizo la **CartPole**. Katika ulimwengu wa CartPole, tuna slider ya mlalo inayoweza kusogea kushoto au kulia, na lengo ni kusawazisha nguzo wima juu ya slider inaposogea.

<img alt="a cartpole" src="images/cartpole.png" width="200"/>

Ili kuunda na kutumia mazingira haya, tunahitaji mistari michache ya msimbo wa Python:

```python
import gym
env = gym.make("CartPole-v1")

env.reset()
done = False
total_reward = 0
while not done:
   env.render()
   action = env.action_space.sample()
   observaton, reward, done, info = env.step(action)
   total_reward += reward

print(f"Total reward: {total_reward}")
```

Kila mazingira yanaweza kufikiwa kwa njia ile ile:
* `env.reset` huanzisha jaribio jipya
* `env.step` hufanya hatua ya simulizi. Inapokea **kitendo** kutoka kwa **eneo la vitendo**, na kurudisha **uchunguzi** (kutoka eneo la uchunguzi), pamoja na tuzo na bendera ya kumaliza.

Katika mfano hapo juu tunafanya kitendo cha nasibu katika kila hatua, ndiyo maana maisha ya jaribio ni mafupi sana:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Lengo la algorithimu ya RL ni kufundisha mfano - unaoitwa **sera** π - ambayo itarudisha kitendo kwa kujibu hali fulani. Tunaweza pia kuzingatia sera kuwa ya uwezekano, yaani kwa hali yoyote *s* na kitendo *a* itarudisha uwezekano π(*a*|*s*) kwamba tunapaswa kuchukua *a* katika hali *s*.

## Algorithimu ya Policy Gradients

Njia ya wazi zaidi ya kuunda sera ni kwa kuunda mtandao wa neva ambao utachukua hali kama pembejeo, na kurudisha vitendo vinavyolingana (au badala yake uwezekano wa vitendo vyote). Kwa namna fulani, itakuwa sawa na kazi ya kawaida ya uainishaji, na tofauti kubwa - hatujui mapema ni vitendo gani tunavyopaswa kuchukua katika kila hatua.

Wazo hapa ni kukadiria uwezekano huo. Tunajenga vekta ya **tuzo zilizojumlishwa** ambayo inaonyesha tuzo yetu ya jumla katika kila hatua ya jaribio. Pia tunatumia **upunguzaji wa tuzo** kwa kuzidisha tuzo za awali na mgawo fulani γ=0.99, ili kupunguza umuhimu wa tuzo za awali. Kisha, tunaimarisha hatua hizo katika njia ya jaribio ambazo zinatoa tuzo kubwa zaidi.

> Jifunze zaidi kuhusu algorithimu ya Policy Gradient na uione ikifanya kazi katika [notebook ya mfano](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb).

## Algorithimu ya Actor-Critic

Toleo lililoboreshwa la mbinu ya Policy Gradients linaitwa **Actor-Critic**. Wazo kuu nyuma yake ni kwamba mtandao wa neva utafundishwa kurudisha mambo mawili:

* Sera, ambayo huamua ni kitendo gani cha kuchukua. Sehemu hii inaitwa **actor**.
* Makadirio ya tuzo ya jumla tunayoweza kutarajia kupata katika hali hii - sehemu hii inaitwa **critic**.

Kwa namna fulani, usanifu huu unafanana na [GAN](../../4-ComputerVision/10-GANs/README.md), ambapo tuna mitandao miwili inayofundishwa dhidi ya kila mmoja. Katika mfano wa actor-critic, actor inapendekeza kitendo tunachohitaji kuchukua, na critic inajaribu kuwa mkosoaji na kukadiria matokeo. Hata hivyo, lengo letu ni kufundisha mitandao hiyo kwa pamoja.

Kwa sababu tunajua tuzo za jumla halisi na matokeo yanayorudishwa na critic wakati wa jaribio, ni rahisi kujenga kazi ya hasara ambayo itapunguza tofauti kati yao. Hiyo itatupa **hasara ya critic**. Tunaweza kuhesabu **hasara ya actor** kwa kutumia mbinu ile ile kama katika algorithimu ya Policy Gradient.

Baada ya kuendesha mojawapo ya algorithimu hizi, tunaweza kutarajia CartPole yetu itende kama hii:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Mazoezi: Policy Gradients na Actor-Critic RL

Endelea kujifunza katika notebooks zifuatazo:

* [RL katika TensorFlow](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [RL katika PyTorch](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Majukumu Mengine ya RL

Kujifunza kuimarisha siku hizi ni uwanja unaokua kwa kasi wa utafiti. Baadhi ya mifano ya kuvutia ya kujifunza kuimarisha ni:

* Kufundisha kompyuta kucheza **Michezo ya Atari**. Sehemu ngumu katika tatizo hili ni kwamba hatuna hali rahisi inayowakilishwa kama vekta, bali picha ya skrini - na tunahitaji kutumia CNN kubadilisha picha hii ya skrini kuwa vekta ya vipengele, au kutoa taarifa za tuzo. Michezo ya Atari inapatikana kwenye Gym.
* Kufundisha kompyuta kucheza michezo ya bodi, kama vile Chess na Go. Hivi karibuni programu za hali ya juu kama **Alpha Zero** zilifundishwa kutoka mwanzo na mawakala wawili wakicheza dhidi ya kila mmoja, na kuboresha katika kila hatua.
* Katika viwanda, RL inatumika kuunda mifumo ya udhibiti kutoka kwa simulizi. Huduma inayoitwa [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) imeundwa mahsusi kwa ajili ya hilo.

## Hitimisho

Sasa tumejifunza jinsi ya kufundisha mawakala kufanikisha matokeo mazuri kwa kuwapa tu kazi ya tuzo inayofafanua hali inayotakiwa ya mchezo, na kwa kuwapa fursa ya kuchunguza kwa akili nafasi ya utafutaji. Tumefanikiwa kujaribu algorithimu mbili, na kufanikisha matokeo mazuri kwa muda mfupi. Hata hivyo, huu ni mwanzo tu wa safari yako katika RL, na unapaswa kuzingatia kuchukua kozi tofauti ikiwa unataka kuchimba zaidi.

## 🚀 Changamoto

Chunguza matumizi yaliyoorodheshwa katika sehemu ya 'Majukumu Mengine ya RL' na jaribu kutekeleza moja!

## [Jaribio la baada ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Mapitio na Kujisomea

Jifunze zaidi kuhusu kujifunza kuimarisha kwa njia ya kawaida katika [Mtaala wetu wa Kujifunza kwa Mashine kwa Kompyuta](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Tazama [video hii nzuri](https://www.youtube.com/watch?v=qv6UVOQ0F44) inayozungumzia jinsi kompyuta inavyoweza kujifunza kucheza Super Mario.

## Kazi: [Fundisha Gari la Mlima](lab/README.md)

Lengo lako wakati wa kazi hii litakuwa kufundisha mazingira tofauti ya Gym - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.