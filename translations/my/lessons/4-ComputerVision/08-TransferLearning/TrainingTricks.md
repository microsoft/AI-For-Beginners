# အနက်ရှိုင်းသော သင်ကြားမှု လေ့ကျင့်မှု နည်းလမ်းများ

နယူးရယ်နက်ဝက်များ ပိုမိုနက်ရှိုင်းလာသည်နှင့်အမျှ၊ ၎င်းတို့ကို လေ့ကျင့်ခြင်းလုပ်ငန်းစဉ်သည် ပိုမိုခက်ခဲလာသည်။ အဓိကပြဿနာတစ်ခုမှာ [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) သို့မဟုတ် [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.) ဖြစ်သည်။ [ဒီပို့စ်](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) သည် ၎င်းပြဿနာများအပေါ် အကျဉ်းချုပ်ကောင်းတစ်ခုကို ပေးသည်။

နက်ရှိုင်းသော နက်ဝက်များကို ပိုမိုထိရောက်စွာ လေ့ကျင့်ရန်အတွက် အသုံးပြုနိုင်သော နည်းလမ်းအချို့ရှိသည်။

## တန်ဖိုးများကို သင့်တော်သော အကွာအဝေးတွင် ထိန်းသိမ်းခြင်း

ဂဏန်းတွက်ချက်မှုများကို ပိုမိုတည်ငြိမ်စေရန်၊ နယူးရယ်နက်ဝက်အတွင်းရှိ တန်ဖိုးများအားလုံးကို သင့်တော်သော အကွာအဝေး ([-1..1] သို့မဟုတ် [0..1]) တွင်ရှိစေရန် သေချာစေရန်လိုအပ်သည်။ ၎င်းသည် အလွန်တင်းကြပ်သော လိုအပ်ချက်မဟုတ်သော်လည်း၊ floating point တွက်ချက်မှုများ၏ သဘာဝသည် အရွယ်အစားကွာခြားမှုများကို တစ်ခုပေါင်းတစ်ခုဖြင့် တိကျစွာ စီမံနိုင်မည်မဟုတ်ပါ။ ဥပမာအားဖြင့် 10<sup>-10</sup> နှင့် 10<sup>10</sup> ကို ပေါင်းပါက၊ 10<sup>10</sup> ကိုရနိုင်ပြီး၊ သေးငယ်သောတန်ဖိုးသည် "အကြီးဆုံးတန်ဖိုး၏ အဆင့်" သို့ ပြောင်းလဲသွားပြီး mantissa ကို ဆုံးရှုံးနိုင်သည်။

Activation function များအများစုသည် [-1..1] အကွာအဝေးတွင် non-linear ဖြစ်ပြီး၊ ထို့ကြောင့် input data အားလုံးကို [-1..1] သို့မဟုတ် [0..1] အကွာအဝေးသို့ scale လုပ်ခြင်းသည် make sense ဖြစ်သည်။

## အစပိုင်း Weight Initialization

နက်ဝက် layer များကို ဖြတ်သွားပြီးနောက် တန်ဖိုးများကို အတူတူသော အကွာအဝေးတွင်ရှိစေရန် ကျွန်ုပ်တို့လိုချင်သည်။ ထို့ကြောင့် တန်ဖိုးများ၏ distribution ကို ထိန်းသိမ်းနိုင်ရန် weight များကို initialize လုပ်ခြင်းမှာ အရေးကြီးသည်။

Normal distribution **N(0,1)** သည် idea ကောင်းမဟုတ်ပါ၊ အကြောင်းမှာ *n* inputs ရှိပါက output ၏ standard deviation သည် *n* ဖြစ်ပြီး၊ တန်ဖိုးများသည် [0..1] အကွာအဝေးမှ ကျော်လွန်နိုင်သည်။

အောက်ပါ initialization များကို မကြာခဏ အသုံးပြုသည်-

 * Uniform distribution -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** သည် zero mean နှင့် standard deviation 1 ရှိသော inputs များအတွက် mean/standard deviation ကို ထိန်းသိမ်းနိုင်သည်
 * **N(0,√2/(n_in+n_out))** -- **Xavier initialization** (`glorot`) ဟုခေါ်သည်၊ ၎င်းသည် forward နှင့် backward propagation နှစ်ခုစလုံးတွင် signal များကို range အတွင်း ထိန်းသိမ်းနိုင်ရန် ကူညီသည်

## Batch Normalization

Weight initialization ကိုမှန်ကန်စွာ ပြုလုပ်ထားသည်ဖြစ်စေ၊ training အတွင်း weight များသည် အကြီးမားဆုံး သို့မဟုတ် အငယ်ဆုံးဖြစ်နိုင်ပြီး၊ signal များကို သင့်တော်သော range မှ ကျော်လွန်စေမည်။ Signal များကို ပြန်လည် သင့်တော်သော range သို့ ပြန်လည်ဆောင်ရွက်ရန် **normalization** နည်းလမ်းများကို အသုံးပြုနိုင်သည်။ Weight normalization, Layer Normalization စသည်တို့ရှိသော်လည်း၊ အများဆုံး အသုံးပြုသောနည်းလမ်းမှာ Batch Normalization ဖြစ်သည်။

**Batch normalization** ၏ အကြောင်းအရာမှာ minibatch အတွင်းရှိ တန်ဖိုးအားလုံးကို အခြေခံပြီး normalization (ဥပမာ mean ကိုနုတ်၍ standard deviation ဖြင့် ခွဲခြင်း) ပြုလုပ်ခြင်းဖြစ်သည်။ ၎င်းကို weight များကို အသုံးပြုပြီးနောက် activation function မတိုင်မီ normalization ပြုလုပ်သော network layer အဖြစ် အကောင်အထည်ဖော်ထားသည်။ ၎င်း၏ရလဒ်အနေဖြင့်၊ အမြင့်ဆုံး accuracy ရရှိနိုင်ခြင်းနှင့် training ပိုမိုမြန်ဆန်စေခြင်းကို တွေ့နိုင်သည်။

[Batch normalization အကြောင်း](https://arxiv.org/pdf/1502.03167.pdf) [Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization) နှင့် [blog post](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) တို့တွင် ဖတ်ရှုနိုင်သည်။

## Dropout

**Dropout** သည် training အတွင်း random neurons တစ်ချို့ကို ဖယ်ရှားသည့် နည်းလမ်းတစ်ခုဖြစ်သည်။ ၎င်းကို layer အဖြစ် အကောင်အထည်ဖော်ထားပြီး၊ parameter တစ်ခု (typically 10%-50%) ဖြင့် neurons များကို ဖယ်ရှားသည်။ Training အတွင်း input vector ၏ random elements များကို zero လုပ်ပြီး၊ next layer သို့ ပို့သည်။

ဤနည်းလမ်းသည် ထူးဆန်းသော idea တစ်ခုဖြစ်သော်လည်း၊ MNIST digit classifier ကို training လုပ်သည့်အခါ Dropout ၏ အကျိုးသက်ရောက်မှုကို [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb) notebook တွင် တွေ့နိုင်သည်။ ၎င်းသည် training ကို မြန်ဆန်စေပြီး၊ training epoch အနည်းငယ်တွင် အမြင့်ဆုံး accuracy ရရှိစေသည်။

ဤအကျိုးသက်ရောက်မှုကို အောက်ပါနည်းလမ်းများဖြင့် ရှင်းလင်းနိုင်သည်-

 * ၎င်းကို model အတွက် random shocking factor အဖြစ် သတ်မှတ်နိုင်ပြီး၊ local minimum မှ optimization ကို ထွက်စေသည်
 * ၎င်းကို *implicit model averaging* အဖြစ် သတ်မှတ်နိုင်သည်၊ Dropout အတွင်း model အနည်းငယ်ကို training လုပ်နေသည်ဟု ဆိုနိုင်သည်

> *တချို့လူများက အရက်မူးနေသောသူသည် တစ်ခုခုကို သင်ယူရန်ကြိုးစားသောအခါ၊ နောက်နေ့မနက်တွင် အရက်မူးမနေသောသူထက် ပိုမိုမှတ်မိနိုင်သည်ဟု ဆိုကြသည်။ ဤအချက်ကို ကျွန်ုပ်တို့ကိုယ်တိုင် စမ်းသပ်မထားပါ။*

## Overfitting ကို ကာကွယ်ခြင်း

နက်ရှိုင်းသော သင်ကြားမှု၏ အရေးကြီးသော အပိုင်းတစ်ခုမှာ [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) ကို ကာကွယ်နိုင်ရန်ဖြစ်သည်။ အလွန်အစွမ်းထက်သော neural network model ကို အသုံးပြုရန် စိတ်လှုပ်ရှားစေသော်လည်း၊ model parameters အရေအတွက်နှင့် training samples အရေအတွက်ကို အချိုးကျစေရန် အမြဲလိုအပ်သည်။

> ကျွန်ုပ်တို့ [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) ၏ အကြောင်းအရာကို နားလည်ထားရန် သေချာပါစေ!

Overfitting ကို ကာကွယ်ရန် နည်းလမ်းအချို့မှာ-

 * Early stopping -- validation set အပေါ် error ကို ဆက်လက်ကြည့်ရှုပြီး၊ validation error တိုးလာသောအခါ training ကို ရပ်တန့်ခြင်း
 * Explicit Weight Decay / Regularization -- loss function အတွက် weight များ၏ absolute value များကို penalty ထည့်ခြင်း၊ model ကို မတည်ငြိမ်သောရလဒ်များရရှိခြင်းမှ ကာကွယ်သည်
 * Model Averaging -- model အများအပြားကို training လုပ်ပြီး၊ ရလဒ်ကို averaging လုပ်ခြင်း။ ၎င်းသည် variance ကို လျှော့ချရန် ကူညီသည်။
 * Dropout (Implicit Model Averaging)

## Optimizers / Training Algorithms

Training အတွက် အရေးကြီးသော အပိုင်းတစ်ခုမှာ training algorithm ကောင်းတစ်ခုကို ရွေးချယ်ခြင်းဖြစ်သည်။ **gradient descent** သည် reasonable choice ဖြစ်သော်လည်း၊ ၎င်းသည် တစ်ခါတစ်ရံ အလွန်နှေးကွေးနိုင်သည် သို့မဟုတ် အခြားပြဿနာများကို ဖြစ်စေနိုင်သည်။

နက်ရှိုင်းသော သင်ကြားမှုတွင် **Stochastic Gradient Descent** (SGD) ကို အသုံးပြုသည်၊ ၎င်းသည် training set မှ random minibatches ကို ရွေးချယ်ပြီး gradient descent ကို အကောင်အထည်ဖော်ခြင်းဖြစ်သည်။ Weight များကို အောက်ပါဖော်ပြထားသော formula ဖြင့် ပြင်ဆင်သည်-

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

**Momentum SGD** တွင်၊ ယခင်အဆင့်များမှ gradient တစ်စိတ်တစ်ပိုင်းကို ထိန်းသိမ်းထားသည်။ ၎င်းသည် inertia ဖြင့် တစ်နေရာမှ ရွေ့လျားနေသောအခါ၊ အခြားတစ်ဖက်မှ အလှည့်အပြောင်းတစ်ခုရရှိပါက၊ trajectory သည် ချက်ချင်းမပြောင်းလဲဘဲ၊ original movement ၏ တစ်စိတ်တစ်ပိုင်းကို ထိန်းသိမ်းထားသည်နှင့် ဆင်တူသည်။ ဤနေရာတွင် *speed* ကို ကိုယ်စားပြုသော vector v ကို ထည့်သွင်းသည်-

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

ဤနေရာတွင် parameter γ သည် inertia ကို အဘယ်လောက်ထိန်းသိမ်းမည်ကို ဖော်ပြသည်- γ=0 သည် classical SGD ကို ကိုယ်စားပြုသည်။ γ=1 သည် pure motion equation ဖြစ်သည်။

### Adam, Adagrad, စသည်တို့

Layer တစ်ခုစီတွင် signal များကို matrix W<sub>i</sub> ဖြင့် multiply လုပ်သောကြောင့် ||W<sub>i</sub>|| အပေါ်မူတည်၍ gradient သည် diminish ဖြစ်ပြီး 0 အနီးသို့ ရောက်နိုင်သည် သို့မဟုတ် အလွန်ကြီးမားနိုင်သည်။ ၎င်းသည် Exploding/Vanishing Gradients ပြဿနာ၏ အဓိကအကြောင်းရင်းဖြစ်သည်။

ဤပြဿနာကို ဖြေရှင်းရန် gradient ၏ direction ကိုသာ အသုံးပြုပြီး၊ absolute value ကို မထည့်သွင်းပါ-

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), where ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

ဤ algorithm ကို **Adagrad** ဟုခေါ်သည်။ အခြား algorithm များဖြစ်သော **RMSProp**, **Adam** သည်လည်း အတူတူသော idea ကို အသုံးပြုသည်။

> **Adam** သည် အများသော application များအတွက် အလွန်ထိရောက်သော algorithm ဖြစ်သည်ဟု သတ်မှတ်ထားပြီး၊ သုံးစွဲရန် မသေချာပါက Adam ကို အသုံးပြုပါ။

### Gradient clipping

Gradient clipping သည် အထက်ဖော်ပြထားသော idea ၏ extension ဖြစ်သည်။ ||∇ℒ|| ≤ θ ဖြစ်ပါက၊ weight optimization တွင် original gradient ကို အသုံးပြုသည်။ ||∇ℒ|| > θ ဖြစ်ပါက gradient ကို norm ဖြင့် ခွဲသည်။ ဤနေရာတွင် θ သည် parameter ဖြစ်ပြီး၊ အများဆုံးကိစ္စများတွင် θ=1 သို့မဟုတ် θ=10 ကို အသုံးပြုနိုင်သည်။

### Learning rate decay

Training အောင်မြင်မှုသည် learning rate parameter η အပေါ် မူတည်သည်။ η တန်ဖိုးကြီးများသည် training ပိုမိုမြန်ဆန်စေသည်ဟု သတ်မှတ်နိုင်ပြီး၊ training အစပိုင်းတွင် ၎င်းကို အသုံးပြုလိုသည်။ ထို့နောက် η တန်ဖိုးငယ်များသည် network ကို fine-tune လုပ်ရန် ကူညီသည်။ ထို့ကြောင့် training အတွင်း η ကို လျော့ချလိုသည်။

ဤလုပ်ငန်းစဉ်ကို training epoch တစ်ခုစီပြီးနောက် η ကို (ဥပမာ 0.98) multiplier ဖြင့် လျော့ချခြင်း သို့မဟုတ် **learning rate schedule** ကို အသုံးပြုခြင်းဖြင့် ပြုလုပ်နိုင်သည်။

## နက်ဝက် Architecture များ

သင့်ပြဿနာအတွက် နက်ဝက် architecture ကို ရွေးချယ်ခြင်းသည် ခက်ခဲနိုင်သည်။ သာမန်အားဖြင့်၊ သင့် task (သို့မဟုတ် ဆင်တူသော task) အတွက် အောင်မြင်မှုရရှိထားသော architecture ကို ရွေးချယ်လေ့ရှိသည်။ [ဒီအကျဉ်းချုပ်](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) သည် computer vision အတွက် neural network architecture များကို ဖော်ပြထားသည်။

> သင့် training samples အရေအတွက်အတွက် အတော်လေးအစွမ်းထက်သော architecture ကို ရွေးချယ်ရန် အရေးကြီးသည်။ အလွန်အစွမ်းထက်သော model ကို ရွေးချယ်ခြင်းသည် [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) ဖြစ်စေနိုင်သည်။

အခြားနည်းလမ်းက self-adjusting ဖြစ်သော architecture ကို အသုံးပြုခြင်းဖြစ်သည်။ **ResNet** architecture နှင့် **Inception** တစ်ချို့သည် self-adjusting ဖြစ်သည်။ [Computer vision architecture များအကြောင်း](../07-ConvNets/CNN_Architectures.md) တွင် ပိုမိုသိရှိနိုင်သည်။

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။