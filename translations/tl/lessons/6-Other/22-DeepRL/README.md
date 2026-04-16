# Deep Reinforcement Learning

Ang Reinforcement Learning (RL) ay isa sa mga pangunahing paradigms ng machine learning, katabi ng supervised learning at unsupervised learning. Habang sa supervised learning ay umaasa tayo sa dataset na may mga kilalang resulta, ang RL ay nakabatay sa **pagkatuto sa pamamagitan ng paggawa**. Halimbawa, kapag unang beses nating nakita ang isang computer game, nagsisimula tayong maglaro kahit hindi alam ang mga patakaran, at sa kalaunan ay napapabuti natin ang ating kakayahan sa pamamagitan ng paglalaro at pag-aadjust ng ating mga kilos.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Para magawa ang RL, kailangan natin ng:

* Isang **environment** o **simulator** na nagtatakda ng mga patakaran ng laro. Dapat nating magawa ang mga eksperimento sa simulator at obserbahan ang mga resulta.
* Isang **Reward function**, na nagpapakita kung gaano naging matagumpay ang ating eksperimento. Sa kaso ng pagkatuto na maglaro ng computer game, ang reward ay ang ating final score.

Batay sa reward function, dapat nating ma-adjust ang ating kilos at mapabuti ang ating kakayahan, upang sa susunod ay mas magaling tayong maglaro. Ang pangunahing pagkakaiba ng RL sa ibang uri ng machine learning ay sa RL, kadalasan hindi natin alam kung panalo o talo tayo hanggang matapos ang laro. Kaya, hindi natin masasabing ang isang partikular na galaw ay mabuti o hindi - makakatanggap lamang tayo ng reward sa dulo ng laro.

Sa RL, kadalasan ay gumagawa tayo ng maraming eksperimento. Sa bawat eksperimento, kailangan nating balansehin ang pagsunod sa optimal na strategy na natutunan natin sa ngayon (**exploitation**) at ang pag-explore ng mga bagong posibleng estado (**exploration**).

## OpenAI Gym

Isang mahusay na tool para sa RL ay ang [OpenAI Gym](https://gym.openai.com/) - isang **simulation environment**, na maaaring mag-simulate ng iba't ibang environment mula sa mga laro ng Atari, hanggang sa physics ng pole balancing. Isa ito sa mga pinakasikat na simulation environments para sa pag-train ng reinforcement learning algorithms, at pinapanatili ng [OpenAI](https://openai.com/).

> **Note**: Makikita mo ang lahat ng environment na available mula sa OpenAI Gym [dito](https://gym.openai.com/envs/#classic_control).

## CartPole Balancing

Marahil ay nakita na ninyo ang mga modernong balancing devices tulad ng *Segway* o *Gyroscooters*. Kaya nilang mag-balanse nang awtomatiko sa pamamagitan ng pag-adjust ng kanilang mga gulong batay sa signal mula sa accelerometer o gyroscope. Sa seksyong ito, matututo tayo kung paano lutasin ang isang katulad na problema - ang pag-balanse ng isang pole. Katulad ito ng sitwasyon kung saan ang isang circus performer ay kailangang mag-balanse ng pole sa kanyang kamay - ngunit ang pole balancing na ito ay nangyayari lamang sa 1D.

Ang isang pinasimpleng bersyon ng balancing ay kilala bilang **CartPole** problem. Sa mundo ng cartpole, mayroon tayong horizontal slider na maaaring gumalaw pakaliwa o pakanan, at ang layunin ay mag-balanse ng vertical pole sa ibabaw ng slider habang ito ay gumagalaw.

<img alt="a cartpole" src="../../../../../translated_images/tl/cartpole.f52a67f27e058170.webp" width="200"/>

Para gumawa at gumamit ng environment na ito, kailangan natin ng ilang linya ng Python code:

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
* `env.reset` nagsisimula ng bagong eksperimento
* `env.step` gumagawa ng simulation step. Tumanggap ito ng **action** mula sa **action space**, at nagbabalik ng **observation** (mula sa observation space), pati na rin ng reward at termination flag.

Sa halimbawa sa itaas, gumagawa tayo ng random action sa bawat hakbang, kaya't napakaikli ng buhay ng eksperimento:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Ang layunin ng RL algorithm ay mag-train ng modelo - ang tinatawag na **policy** &pi; - na magbabalik ng action bilang tugon sa isang ibinigay na estado. Maaari rin nating ituring ang policy bilang probabilistic, halimbawa, para sa anumang estado *s* at action *a*, magbabalik ito ng probability &pi;(*a*|*s*) na dapat nating gawin ang *a* sa estado *s*.

## Policy Gradients Algorithm

Ang pinaka-obvious na paraan upang mag-model ng policy ay sa pamamagitan ng paglikha ng neural network na kukuha ng mga estado bilang input, at magbabalik ng mga kaukulang action (o mas tamang sabihin, ang mga probability ng lahat ng action). Sa isang banda, magiging katulad ito ng normal na classification task, ngunit may malaking pagkakaiba - hindi natin alam nang maaga kung aling mga action ang dapat nating gawin sa bawat hakbang.

Ang ideya dito ay i-estimate ang mga probability na iyon. Gumagawa tayo ng vector ng **cumulative rewards** na nagpapakita ng kabuuang reward natin sa bawat hakbang ng eksperimento. Nag-aapply din tayo ng **reward discounting** sa pamamagitan ng pag-multiply ng mga naunang reward sa isang coefficient &gamma;=0.99, upang mabawasan ang papel ng mga naunang reward. Pagkatapos, pinapalakas natin ang mga hakbang sa landas ng eksperimento na nagbunga ng mas malaking reward.

> Matuto pa tungkol sa Policy Gradient algorithm at tingnan ito sa aksyon sa [example notebook](CartPole-RL-TF.ipynb).

## Actor-Critic Algorithm

Ang pinahusay na bersyon ng Policy Gradients approach ay tinatawag na **Actor-Critic**. Ang pangunahing ideya sa likod nito ay ang neural network ay itetrain upang magbalik ng dalawang bagay:

* Ang policy, na tumutukoy kung aling action ang gagawin. Ang bahaging ito ay tinatawag na **actor**
* Ang pagtatantiya ng kabuuang reward na maaari nating makuha sa estado na ito - ang bahaging ito ay tinatawag na **critic**.

Sa isang banda, ang arkitektura na ito ay kahawig ng [GAN](../../4-ComputerVision/10-GANs/README.md), kung saan mayroon tayong dalawang network na itinatrain laban sa isa't isa. Sa actor-critic model, ang actor ang nagmumungkahi ng action na kailangan nating gawin, at ang critic ang nagtatangkang maging kritikal at tantiyahin ang resulta. Gayunpaman, ang layunin natin ay itrain ang mga network na ito nang sabay.

Dahil alam natin ang parehong tunay na cumulative rewards at ang mga resulta na ibinalik ng critic sa panahon ng eksperimento, medyo madali ang pagbuo ng loss function na magpapaliit sa pagkakaiba sa pagitan nila. Magbibigay ito sa atin ng **critic loss**. Maaari nating i-compute ang **actor loss** gamit ang parehong approach tulad ng sa policy gradient algorithm.

Pagkatapos patakbuhin ang isa sa mga algorithm na ito, maaari nating asahan na ang CartPole natin ay mag-behave nang ganito:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Mga Ehersisyo: Policy Gradients at Actor-Critic RL

Ipagpatuloy ang iyong pag-aaral sa mga sumusunod na notebook:

* [RL sa TensorFlow](CartPole-RL-TF.ipynb)
* [RL sa PyTorch](CartPole-RL-PyTorch.ipynb)

## Iba Pang RL Tasks

Ang Reinforcement Learning ngayon ay isang mabilis na lumalaking larangan ng pananaliksik. Ilan sa mga kawili-wiling halimbawa ng reinforcement learning ay:

* Pagtuturo sa computer na maglaro ng **Atari Games**. Ang hamon sa problemang ito ay wala tayong simpleng estado na kinakatawan bilang vector, kundi isang screenshot - at kailangan nating gamitin ang CNN upang i-convert ang screen image sa feature vector, o upang kunin ang impormasyon ng reward. Ang mga laro ng Atari ay available sa Gym.
* Pagtuturo sa computer na maglaro ng mga board games, tulad ng Chess at Go. Kamakailan, ang mga state-of-the-art na programa tulad ng **Alpha Zero** ay itinrain mula sa simula ng dalawang agents na naglalaro laban sa isa't isa, at nagpapabuti sa bawat hakbang.
* Sa industriya, ginagamit ang RL upang lumikha ng mga control system mula sa simulation. Ang isang serbisyo na tinatawag na [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) ay partikular na idinisenyo para dito.

## Konklusyon

Natutunan na natin kung paano mag-train ng mga agents upang makamit ang magagandang resulta sa pamamagitan lamang ng pagbibigay sa kanila ng reward function na nagtatakda ng nais na estado ng laro, at sa pamamagitan ng pagbibigay sa kanila ng pagkakataon na matalinong mag-explore ng search space. Matagumpay nating sinubukan ang dalawang algorithm, at nakamit ang magandang resulta sa medyo maikling panahon. Gayunpaman, ito ay simula pa lamang ng iyong paglalakbay sa RL, at dapat mong isaalang-alang ang pagkuha ng hiwalay na kurso kung nais mong mas malalim na mag-aral.

## 🚀 Hamon

I-explore ang mga application na nakalista sa seksyong 'Iba Pang RL Tasks' at subukang i-implement ang isa!

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Review & Self Study

Matuto pa tungkol sa classical reinforcement learning sa aming [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Panoorin ang [napakagandang video na ito](https://www.youtube.com/watch?v=qv6UVOQ0F44) na nagpapakita kung paano natututo ang computer na maglaro ng Super Mario.

## Assignment: [Train a Mountain Car](lab/README.md)

Ang layunin mo sa assignment na ito ay mag-train ng ibang Gym environment - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

