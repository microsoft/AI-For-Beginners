# အနက်ရှိုင်းသော Reinforcement Learning

Reinforcement learning (RL) သည် supervised learning နှင့် unsupervised learning အနက် machine learning ရဲ့ အခြေခံ paradigm တစ်ခုအဖြစ် သတ်မှတ်ထားသည်။ Supervised learning တွင် ရလဒ်များကို သိရှိထားသော dataset ကို အခြေခံပြီး လေ့လာရသလို RL တွင် **လုပ်ဆောင်ခြင်းမှတစ်ဆင့် လေ့လာခြင်း** ကို အခြေခံသည်။ ဥပမာအားဖြင့် ပထမဆုံး computer game ကို မြင်တွေ့သောအခါ ကျွန်ုပ်တို့သည် အစပျိုးက စတင်ကစားပြီး game ရဲ့ rule များကို မသိရှိဘဲဖြစ်စေ ကစားရင်း ကျွန်ုပ်တို့၏ ကျွမ်းကျင်မှုကို တိုးတက်စေသည်။

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/43)

RL ကို လုပ်ဆောင်ရန် ကျွန်ုပ်တို့အတွက် လိုအပ်သောအရာများမှာ -

* **Environment** သို့မဟုတ် **Simulator** - game ရဲ့ rule များကို သတ်မှတ်ပေးသောအရာ။ Simulator တွင် စမ်းသပ်မှုများကို လုပ်ဆောင်ပြီး ရလဒ်များကို ကြည့်ရှုနိုင်ရမည်။
* **Reward function** - စမ်းသပ်မှုရဲ့ အောင်မြင်မှုကို ဖော်ပြပေးသောအရာ။ ဥပမာအားဖြင့် computer game ကစားခြင်းကို လေ့လာနေစဉ် reward သည် ကျွန်ုပ်တို့ရဲ့ အဆုံးသတ် score ဖြစ်နိုင်သည်။

Reward function ကို အခြေခံပြီး ကျွန်ုပ်တို့၏ အပြုအမူကို ပြင်ဆင်ကောင်းမွန်စေပြီး နောက်တစ်ကြိမ်ကစားသောအခါ ပိုမိုကောင်းမွန်စေရန် လေ့လာနိုင်သည်။ RL နှင့် machine learning အခြားအမျိုးအစားများ၏ အဓိကကွာခြားချက်မှာ RL တွင် game ပြီးဆုံးသည်အထိ အနိုင်ရသို့မဟုတ် အရှုံးပေါ်မူတည်၍ မသိရှိနိုင်ခြင်းဖြစ်သည်။ ထို့ကြောင့် တစ်ခုချင်းစီသော move သည် ကောင်းမွန်သည်ဟု မဆိုနိုင်ဘဲ game ပြီးဆုံးသောအခါ reward ကိုသာ ရရှိသည်။

RL လုပ်ဆောင်စဉ် စမ်းသပ်မှုများစွာကို လုပ်ဆောင်ရသည်။ စမ်းသပ်မှုတစ်ခုစီတွင် **exploitation** (ယခင် strategy ကို လိုက်နာခြင်း) နှင့် **exploration** (state အသစ်များကို ရှာဖွေခြင်း) အကြား balance လုပ်ရန် လိုအပ်သည်။

## OpenAI Gym

RL အတွက် အကောင်းဆုံး tools တစ်ခုမှာ [OpenAI Gym](https://gym.openai.com/) ဖြစ်သည်။ ၎င်းသည် **simulation environment** တစ်ခုဖြစ်ပြီး Atari game များမှစ၍ pole balancing physics အထိ အမျိုးမျိုးသော environment များကို simulate လုပ်နိုင်သည်။ RL algorithm များကို လေ့ကျင့်ရန် အလွန်လူကြိုက်များသော simulation environment တစ်ခုဖြစ်ပြီး [OpenAI](https://openai.com/) မှ maintain လုပ်ထားသည်။

> **Note**: OpenAI Gym မှ environment များအားလုံးကို [ဒီမှာ](https://gym.openai.com/envs/#classic_control) ကြည့်ရှုနိုင်သည်။

## CartPole Balancing

Segway သို့မဟုတ် Gyroscooters ကဲ့သို့သော ခေတ်သစ် balancing device များကို မြင်ဖူးကြမယ်ထင်ပါတယ်။ ၎င်းများသည် accelerometer သို့မဟုတ် gyroscope မှ signal ကို အခြေခံပြီး wheel များကို ပြင်ဆင်ခြင်းဖြင့် အလိုအလျောက် balance လုပ်နိုင်သည်။ ဒီအပိုင်းမှာ ကျွန်ုပ်တို့ pole balancing ပြဿနာကို ဖြေရှင်းပုံကို လေ့လာပါမည်။ ၎င်းသည် circus performer တစ်ဦးက သူ့လက်ပေါ်တွင် pole ကို balance လုပ်ရသည့်အခြေအနေနှင့် ဆင်တူသည်။ သို့သော် ဒီ pole balancing သည် 1D တွင်သာ ဖြစ်ပေါ်သည်။

Balancing ရဲ့ simplified version ကို **CartPole** problem ဟု သိထားသည်။ CartPole world တွင် horizontal slider တစ်ခုရှိပြီး left သို့မဟုတ် right သို့ ရွှေ့နိုင်သည်။ ၎င်း slider ရဲ့ အပေါ်တွင် vertical pole ကို balance လုပ်ရန် ရည်ရွယ်ထားသည်။

<img alt="a cartpole" src="../../../../../translated_images/my/cartpole.f52a67f27e058170.webp" width="200"/>

ဒီ environment ကို ဖန်တီးပြီး အသုံးပြုရန် Python code အချို့လိုအပ်သည် -

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

Environment တစ်ခုစီကို အတိအကျ အတူတူ access လုပ်နိုင်သည် -
* `env.reset` သည် စမ်းသပ်မှုအသစ်ကို စတင်သည်။
* `env.step` သည် simulation step တစ်ခုကို လုပ်ဆောင်သည်။ ၎င်းသည် **action space** မှ **action** ကို လက်ခံပြီး **observation space** မှ **observation** ကို return ပြန်ပေးသည်။ ထို့အပြင် reward နှင့် termination flag ကိုလည်း return ပြန်ပေးသည်။

အထက်ပါဥပမာတွင် random action ကို တစ်ခုချင်းစီမှာ လုပ်ဆောင်သောကြောင့် စမ်းသပ်မှုရဲ့ အသက်ရှည်မှုသည် အလွန်တိုတောင်းသည် -

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

RL algorithm ရဲ့ ရည်ရွယ်ချက်မှာ model တစ်ခုကို လေ့ကျင့်ခြင်းဖြစ်သည် - ၎င်းကို **policy** &pi; ဟုခေါ်သည်။ Policy သည် state တစ်ခုအတွက် action ကို return ပြန်ပေးမည်။ Policy ကို probabilistic အနေနှင့်လည်း သတ်မှတ်နိုင်သည်။ ဥပမာအားဖြင့် state *s* နှင့် action *a* တစ်ခုအတွက် &pi;(*a*|*s*) သည် state *s* တွင် *a* ကို လုပ်ဆောင်သင့်ကြောင်း probability ကို return ပြန်ပေးမည်။

## Policy Gradients Algorithm

Policy ကို model လုပ်ရန် အလွယ်ဆုံးနည်းလမ်းမှာ state များကို input အဖြစ်ယူပြီး action များ (သို့မဟုတ် action များ၏ probability) ကို return ပြန်ပေးမည့် neural network တစ်ခုကို ဖန်တီးခြင်းဖြစ်သည်။ ၎င်းသည် classification task တစ်ခုနှင့် ဆင်တူသည်။ သို့သော် အဓိကကွာခြားချက်မှာ - ကျွန်ုပ်တို့သည် တစ်ခုချင်းစီသော step တွင် ဘယ် action ကို လုပ်ဆောင်သင့်ကြောင်းကို ကြိုတင်မသိရှိနိုင်ခြင်းဖြစ်သည်။

ဒီမှာ idea က probability များကို ခန့်မှန်းခြင်းဖြစ်သည်။ စမ်းသပ်မှုတစ်ခုစီတွင် **cumulative rewards** vector တစ်ခုကို ဖန်တီးပြီး အတိအကျ reward ကို ဖော်ပြသည်။ **reward discounting** ကိုလည်း အသုံးပြုပြီး &gamma;=0.99 coefficient ဖြင့် အစောပိုင်း reward များကို diminish လုပ်သည်။ ထို့နောက် reward များကို ပိုမိုရရှိစေသော step များကို reinforce လုပ်သည်။

> Policy Gradient algorithm ကို ပိုမိုလေ့လာပြီး ၎င်းကို လက်တွေ့အသုံးပြုပုံကို [example notebook](CartPole-RL-TF.ipynb) တွင် ကြည့်ရှုပါ။

## Actor-Critic Algorithm

Policy Gradients approach ရဲ့ တိုးတက်သော version ကို **Actor-Critic** ဟုခေါ်သည်။ ၎င်း၏ အဓိက idea က neural network ကို အောက်ပါအရာနှစ်ခုကို return ပြန်ပေးရန် လေ့ကျင့်ခြင်းဖြစ်သည် -

* Policy - ဘယ် action ကို လုပ်ဆောင်ရမည်ကို သတ်မှတ်ပေးသည်။ ဒီအပိုင်းကို **actor** ဟုခေါ်သည်။
* State တစ်ခုတွင် ရရှိနိုင်သော total reward ကို ခန့်မှန်းပေးသည်။ ဒီအပိုင်းကို **critic** ဟုခေါ်သည်။

ဒီ architecture သည် [GAN](../../4-ComputerVision/10-GANs/README.md) နှင့် ဆင်တူသည်။ GAN တွင် network နှစ်ခုကို တစ်ခုနှင့်တစ်ခု training လုပ်သည်။ Actor-Critic model တွင် actor သည် လုပ်ဆောင်ရန် action ကို propose လုပ်ပြီး critic သည် အရလွှာဖြစ်ပြီး ရလဒ်ကို ခန့်မှန်းသည်။ သို့သော် ကျွန်ုပ်တို့ရဲ့ ရည်ရွယ်ချက်မှာ network နှစ်ခုကို unison ဖြင့် training လုပ်ခြင်းဖြစ်သည်။

စမ်းသပ်မှုအတွင်း critic မှ return ပြန်ပေးသော result နှင့် အမှန်တကယ် cumulative rewards ကို သိရှိထားသောကြောင့် loss function တစ်ခုကို ဖန်တီးပြီး ၎င်းတို့အကြားကွာခြားမှုကို minimize လုပ်နိုင်သည်။ ၎င်းသည် **critic loss** ကို ပေးမည်။ **actor loss** ကို policy gradient algorithm တွင် အသုံးပြုသော နည်းလမ်းတူတူဖြင့် တွက်ချက်နိုင်သည်။

ဒီ algorithm များကို run လုပ်ပြီးနောက် ကျွန်ုပ်တို့ရဲ့ CartPole သည် အောက်ပါအတိုင်း လုပ်ဆောင်နိုင်မည်ဖြစ်သည် -

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ လေ့ကျင့်မှုများ: Policy Gradients နှင့် Actor-Critic RL

အောက်ပါ notebook များတွင် သင့်လေ့လာမှုကို ဆက်လက်လုပ်ဆောင်ပါ -

* [RL in TensorFlow](CartPole-RL-TF.ipynb)
* [RL in PyTorch](CartPole-RL-PyTorch.ipynb)

## အခြား RL Tasks

ယနေ့ခေတ်တွင် Reinforcement Learning သည် အလွန်မြန်ဆန်စွာ တိုးတက်နေသော သုတေသနနယ်ပယ်တစ်ခုဖြစ်သည်။ RL ရဲ့ စိတ်ဝင်စားဖွယ် ဥပမာများမှာ -

* **Atari Games** ကစားရန် computer ကို သင်ကြားခြင်း။ ဒီပြဿနာရဲ့ စိန်ခေါ်မှုမှာ simple state ကို vector အနေနှင့် မဖော်ပြနိုင်ဘဲ screenshot ကို အသုံးပြုရခြင်းဖြစ်သည်။ CNN ကို အသုံးပြု၍ screen image ကို feature vector သို့မဟုတ် reward information ကို extract လုပ်ရမည်။ Atari game များသည် Gym တွင် ရရှိနိုင်သည်။
* Chess နှင့် Go ကဲ့သို့သော board game များကို computer သင်ကြားခြင်း။ မကြာသေးမီက **Alpha Zero** ကဲ့သို့ state-of-the-art program များကို agent နှစ်ခုအပြန်အလှန် ကစားခြင်းဖြင့် အစမှ training လုပ်ခဲ့သည်။
* စက်မှုလုပ်ငန်းတွင် RL ကို simulation မှ control system များဖန်တီးရန် အသုံးပြုသည်။ [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) ဟုခေါ်သော service သည် အထူးသဖြင့် ဒီအတွက် ရည်ရွယ်ထားသည်။

## နိဂုံး

ကျွန်ုပ်တို့သည် game ရဲ့ ရည်မှန်းထားသော state ကို သတ်မှတ်ပေးသော reward function ကိုသာ ပေးပြီး intelligent search space ကို explore လုပ်ရန် agent များကို training လုပ်ပုံကို လေ့လာပြီး အောင်မြင်သောရလဒ်များရရှိခဲ့သည်။ Algorithm နှစ်ခုကို စမ်းသပ်ပြီး အချိန်တိုတောင်းအတွင်း ကောင်းမွန်သောရလဒ်ကို ရရှိခဲ့သည်။ သို့သော် RL ကို ပိုမိုနက်ရှိုင်းစွာ လေ့လာလိုပါက သီးခြားသင်တန်းတစ်ခုကို လေ့လာရန် သင့်လျော်သည်။

## 🚀 စိန်ခေါ်မှု

'Other RL Tasks' အပိုင်းတွင် ဖော်ပြထားသော application များကို explore လုပ်ပြီး တစ်ခုကို implement လုပ်ကြည့်ပါ။

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Review & Self Study

Classical reinforcement learning ကို ကျွန်ုပ်တို့ရဲ့ [Machine Learning for Beginners Curriculum](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md) တွင် ပိုမိုလေ့လာပါ။

Super Mario ကို computer သင်ကြားပုံကို ဖော်ပြထားသော [ဒီ video](https://www.youtube.com/watch?v=qv6UVOQ0F44) ကို ကြည့်ရှုပါ။

## Assignment: [Train a Mountain Car](lab/README.md)

ဒီ assignment တွင် သင့်ရည်ရွယ်ချက်မှာ Gym environment တစ်ခုဖြစ်သော [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/) ကို training လုပ်ရန်ဖြစ်သည်။

---

