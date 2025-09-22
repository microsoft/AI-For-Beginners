<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dbacf9b1915612981d76059678e563e5",
  "translation_date": "2025-08-28T02:27:39+00:00",
  "source_file": "lessons/6-Other/22-DeepRL/README.md",
  "language_code": "tl"
}
-->
# Deep Reinforcement Learning

Ang Reinforcement Learning (RL) ay itinuturing na isa sa mga pangunahing paradigma ng machine learning, kasabay ng supervised learning at unsupervised learning. Habang sa supervised learning ay umaasa tayo sa dataset na may kilalang resulta, ang RL ay nakabatay sa **pagkatuto sa pamamagitan ng paggawa**. Halimbawa, kapag unang beses nating nakita ang isang computer game, sinisimulan natin itong laruin kahit hindi alam ang mga patakaran, at kalaunan ay napapabuti natin ang ating kakayahan sa pamamagitan lamang ng paglalaro at pag-aadjust ng ating mga kilos.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Upang maisagawa ang RL, kailangan natin ng:

* Isang **environment** o **simulator** na nagtatakda ng mga patakaran ng laro. Dapat nating magawang magsagawa ng mga eksperimento sa simulator at obserbahan ang mga resulta.
* Isang **Reward function**, na nagpapakita kung gaano naging matagumpay ang ating eksperimento. Sa kaso ng pagkatuto sa paglalaro ng computer game, ang reward ay ang ating huling score.

Batay sa reward function, dapat nating magawang i-adjust ang ating kilos at pagbutihin ang ating kakayahan, upang sa susunod na paglalaro ay mas gumaling tayo. Ang pangunahing pagkakaiba ng RL sa ibang uri ng machine learning ay sa RL, karaniwan ay hindi natin alam kung tayo ay panalo o talo hangga't hindi natatapos ang laro. Kaya, hindi natin masasabi kung ang isang partikular na galaw ay mabuti o hindi - makakatanggap lamang tayo ng reward sa pagtatapos ng laro.

Sa RL, karaniwang nagsasagawa tayo ng maraming eksperimento. Sa bawat eksperimento, kailangan nating balansehin ang pagsunod sa pinakamainam na estratehiya na natutunan natin sa ngayon (**exploitation**) at ang paggalugad sa mga bagong posibleng estado (**exploration**).

## OpenAI Gym

Isang mahusay na kasangkapan para sa RL ay ang [OpenAI Gym](https://gym.openai.com/) - isang **simulation environment**, na maaaring magsimulate ng maraming iba't ibang environment mula sa mga laro ng Atari hanggang sa pisika ng pole balancing. Isa ito sa mga pinakapopular na simulation environment para sa pagsasanay ng reinforcement learning algorithms, at pinapanatili ito ng [OpenAI](https://openai.com/).

> **Note**: Makikita mo ang lahat ng environment na available mula sa OpenAI Gym [dito](https://gym.openai.com/envs/#classic_control).

## CartPole Balancing

Marahil ay nakita na ninyo ang mga modernong balancing device tulad ng *Segway* o *Gyroscooters*. Ang mga ito ay kayang awtomatikong magbalanse sa pamamagitan ng pag-adjust ng kanilang mga gulong batay sa signal mula sa accelerometer o gyroscope. Sa seksyong ito, matututuhan natin kung paano lutasin ang isang katulad na problema - ang pagbabalanse ng isang poste. Katulad ito ng sitwasyon kung saan ang isang circus performer ay kailangang magbalanse ng poste sa kanyang kamay - ngunit ang pagbabalanseng ito ay nangyayari lamang sa 1D.

Ang isang pinasimpleng bersyon ng pagbabalanse ay kilala bilang **CartPole** problem. Sa mundo ng cartpole, mayroon tayong isang horizontal slider na maaaring gumalaw pakaliwa o pakanan, at ang layunin ay magbalanse ng isang vertical na poste sa ibabaw ng slider habang ito ay gumagalaw.

<img alt="a cartpole" src="images/cartpole.png" width="200"/>

Upang likhain at gamitin ang environment na ito, kailangan natin ng ilang linya ng Python code:

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

Ang bawat environment ay maaaring ma-access sa parehong paraan:
* `env.reset` ay nagsisimula ng bagong eksperimento
* `env.step` ay nagsasagawa ng isang simulation step. Tumanggap ito ng isang **action** mula sa **action space**, at nagbabalik ng isang **observation** (mula sa observation space), pati na rin ang reward at termination flag.

Sa halimbawa sa itaas, gumagawa tayo ng random na aksyon sa bawat hakbang, kaya't napakaikli ng buhay ng eksperimento:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Ang layunin ng isang RL algorithm ay sanayin ang isang modelo - ang tinatawag na **policy** π - na magbabalik ng aksyon bilang tugon sa isang partikular na estado. Maaari rin nating ituring ang policy bilang probabilistic, halimbawa, para sa anumang estado *s* at aksyon *a*, ibabalik nito ang probabilidad π(*a*|*s*) na dapat nating gawin ang *a* sa estado *s*.

## Policy Gradients Algorithm

Ang pinaka-obvious na paraan upang i-modelo ang isang policy ay sa pamamagitan ng paglikha ng isang neural network na tatanggap ng mga estado bilang input, at magbabalik ng mga kaukulang aksyon (o mas tamang sabihin, ang mga probabilidad ng lahat ng aksyon). Sa isang banda, magiging katulad ito ng isang normal na classification task, ngunit may malaking pagkakaiba - hindi natin alam nang maaga kung aling mga aksyon ang dapat nating gawin sa bawat hakbang.

Ang ideya dito ay i-estimate ang mga probabilidad na iyon. Gumagawa tayo ng isang vector ng **cumulative rewards** na nagpapakita ng kabuuang reward natin sa bawat hakbang ng eksperimento. Nag-aapply din tayo ng **reward discounting** sa pamamagitan ng pag-multiply ng mga naunang reward sa isang coefficient γ=0.99, upang mabawasan ang epekto ng mga naunang reward. Pagkatapos, pinapalakas natin ang mga hakbang sa landas ng eksperimento na nagdudulot ng mas malalaking reward.

> Alamin ang higit pa tungkol sa Policy Gradient algorithm at tingnan ito sa aksyon sa [example notebook](CartPole-RL-TF.ipynb).

## Actor-Critic Algorithm

Ang isang pinahusay na bersyon ng Policy Gradients approach ay tinatawag na **Actor-Critic**. Ang pangunahing ideya nito ay ang neural network ay sinasanay upang magbalik ng dalawang bagay:

* Ang policy, na tumutukoy kung aling aksyon ang dapat gawin. Ang bahaging ito ay tinatawag na **actor**.
* Ang pagtatantiya ng kabuuang reward na maaari nating asahan sa estado na iyon - ang bahaging ito ay tinatawag na **critic**.

Sa isang banda, ang arkitekturang ito ay kahawig ng isang [GAN](../../4-ComputerVision/10-GANs/README.md), kung saan mayroon tayong dalawang network na sinasanay laban sa isa't isa. Sa actor-critic model, ang actor ang nagmumungkahi ng aksyon na kailangan nating gawin, at ang critic ang sumusubok maging kritikal at tinatantiya ang resulta. Gayunpaman, ang layunin natin ay sanayin ang mga network na ito nang sabay.

Dahil alam natin ang parehong tunay na cumulative rewards at ang mga resulta na ibinabalik ng critic sa panahon ng eksperimento, medyo madali ang pagbuo ng loss function na magpapaliit sa pagkakaiba sa pagitan ng mga ito. Ito ang magbibigay sa atin ng **critic loss**. Maaari nating kalkulahin ang **actor loss** gamit ang parehong paraan tulad ng sa policy gradient algorithm.

Pagkatapos patakbuhin ang isa sa mga algorithm na ito, maaari nating asahan na ang ating CartPole ay magpapakita ng ganitong kilos:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Mga Ehersisyo: Policy Gradients at Actor-Critic RL

Ipagpatuloy ang iyong pag-aaral sa mga sumusunod na notebook:

* [RL sa TensorFlow](CartPole-RL-TF.ipynb)
* [RL sa PyTorch](CartPole-RL-PyTorch.ipynb)

## Iba Pang RL Tasks

Ang Reinforcement Learning sa kasalukuyan ay isang mabilis na lumalaking larangan ng pananaliksik. Ilan sa mga kawili-wiling halimbawa ng reinforcement learning ay:

* Pagtuturo sa isang computer na maglaro ng **Atari Games**. Ang hamon sa problemang ito ay wala tayong simpleng estado na kinakatawan bilang isang vector, kundi isang screenshot - at kailangan nating gumamit ng CNN upang i-convert ang screen image na ito sa isang feature vector, o upang kunin ang reward information. Ang mga laro ng Atari ay available sa Gym.
* Pagtuturo sa isang computer na maglaro ng mga board game, tulad ng Chess at Go. Kamakailan, ang mga state-of-the-art na programa tulad ng **Alpha Zero** ay sinanay mula sa simula sa pamamagitan ng dalawang agent na naglalaro laban sa isa't isa, at patuloy na gumagaling sa bawat hakbang.
* Sa industriya, ginagamit ang RL upang lumikha ng mga control system mula sa simulation. Ang isang serbisyo na tinatawag na [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) ay partikular na idinisenyo para dito.

## Konklusyon

Natutuhan na natin ngayon kung paano sanayin ang mga agent upang makamit ang magagandang resulta sa pamamagitan lamang ng pagbibigay sa kanila ng reward function na nagtatakda ng nais na estado ng laro, at pagbibigay sa kanila ng pagkakataong matalinong galugarin ang search space. Matagumpay nating nasubukan ang dalawang algorithm, at nakamit ang magandang resulta sa isang medyo maikling panahon. Gayunpaman, ito ay simula pa lamang ng iyong paglalakbay sa RL, at dapat mong isaalang-alang ang pagkuha ng hiwalay na kurso kung nais mong mas malalim na tuklasin ito.

## 🚀 Hamon

Galugarin ang mga aplikasyon na nakalista sa seksyong 'Iba Pang RL Tasks' at subukang ipatupad ang isa!

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Review at Pag-aaral sa Sarili

Alamin ang higit pa tungkol sa klasikong reinforcement learning sa aming [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Panoorin ang [napakagandang video na ito](https://www.youtube.com/watch?v=qv6UVOQ0F44) na nagpapakita kung paano natututo ang isang computer na maglaro ng Super Mario.

## Takdang-Aralin: [Sanayin ang Mountain Car](lab/README.md)

Ang iyong layunin sa takdang-araling ito ay sanayin ang isang ibang Gym environment - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.