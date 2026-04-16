# Duboko pojačano učenje

Pojačano učenje (RL) smatra se jednim od osnovnih paradigmi strojnog učenja, uz nadzirano učenje i nenadzirano učenje. Dok se u nadziranom učenju oslanjamo na skup podataka s poznatim ishodima, RL se temelji na **učenju kroz rad**. Na primjer, kada prvi put vidimo računalnu igru, počinjemo igrati, čak i bez poznavanja pravila, i ubrzo poboljšavamo svoje vještine samo kroz proces igranja i prilagođavanja ponašanja.

## [Kviz prije predavanja](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Za provođenje RL-a potrebni su nam:

* **Okruženje** ili **simulator** koji postavlja pravila igre. Trebali bismo moći provoditi eksperimente u simulatoru i promatrati rezultate.
* Neka **funkcija nagrade**, koja pokazuje koliko je naš eksperiment bio uspješan. U slučaju učenja igranja računalne igre, nagrada bi bila naš konačni rezultat.

Na temelju funkcije nagrade trebali bismo moći prilagoditi svoje ponašanje i poboljšati svoje vještine kako bismo sljedeći put igrali bolje. Glavna razlika između drugih vrsta strojnog učenja i RL-a je ta što u RL-u obično ne znamo hoćemo li pobijediti ili izgubiti dok ne završimo igru. Dakle, ne možemo reći je li određeni potez sam po sebi dobar ili ne - nagradu dobivamo tek na kraju igre.

Tijekom RL-a obično provodimo mnogo eksperimenata. Tijekom svakog eksperimenta moramo balansirati između praćenja optimalne strategije koju smo dosad naučili (**eksploatacija**) i istraživanja novih mogućih stanja (**eksploracija**).

## OpenAI Gym

Odličan alat za RL je [OpenAI Gym](https://gym.openai.com/) - **simulacijsko okruženje** koje može simulirati mnoga različita okruženja, počevši od Atari igara do fizike balansiranja štapa. To je jedno od najpopularnijih simulacijskih okruženja za treniranje algoritama pojačanog učenja, a održava ga [OpenAI](https://openai.com/).

> **Napomena**: Sve dostupne okoline iz OpenAI Gym-a možete vidjeti [ovdje](https://gym.openai.com/envs/#classic_control).

## Balansiranje CartPole-a

Vjerojatno ste svi vidjeli moderne uređaje za balansiranje poput *Segwaya* ili *Gyroscootera*. Oni se automatski balansiraju prilagođavanjem svojih kotača na temelju signala iz akcelerometra ili žiroskopa. U ovom ćemo dijelu naučiti kako riješiti sličan problem - balansiranje štapa. To je slično situaciji kada cirkuski izvođač mora balansirati štap na svojoj ruci - ali ovo balansiranje štapa odvija se samo u 1D.

Pojednostavljena verzija balansiranja poznata je kao problem **CartPole**. U svijetu CartPole-a imamo horizontalni klizač koji se može kretati lijevo ili desno, a cilj je balansirati vertikalni štap na vrhu klizača dok se kreće.

<img alt="cartpole" src="../../../../../translated_images/hr/cartpole.f52a67f27e058170.webp" width="200"/>

Za stvaranje i korištenje ovog okruženja potrebno je nekoliko linija Python koda:

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

Svako okruženje može se pristupiti na isti način:
* `env.reset` započinje novi eksperiment
* `env.step` izvodi simulacijski korak. Prima **akciju** iz **prostora akcija** i vraća **promatranje** (iz prostora promatranja), kao i nagradu i zastavicu za završetak.

U gornjem primjeru izvodimo nasumičnu akciju u svakom koraku, zbog čega je trajanje eksperimenta vrlo kratko:

![cartpole bez balansiranja](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Cilj RL algoritma je trenirati model - tzv. **politiku** &pi; - koja će vratiti akciju kao odgovor na dano stanje. Politiku također možemo smatrati probabilističkom, npr. za bilo koje stanje *s* i akciju *a* vratit će vjerojatnost &pi;(*a*|*s*) da poduzmemo *a* u stanju *s*.

## Algoritam gradijenata politike

Najjednostavniji način za modeliranje politike je stvaranje neuronske mreže koja će uzimati stanja kao ulaz i vraćati odgovarajuće akcije (ili radije vjerojatnosti svih akcija). Na neki način, to bi bilo slično normalnom zadatku klasifikacije, s jednom velikom razlikom - unaprijed ne znamo koje akcije trebamo poduzeti u svakom koraku.

Ideja je ovdje procijeniti te vjerojatnosti. Gradimo vektor **kumulativnih nagrada** koji pokazuje našu ukupnu nagradu u svakom koraku eksperimenta. Također primjenjujemo **diskontiranje nagrada** množenjem ranijih nagrada s nekim koeficijentom &gamma;=0.99, kako bismo umanjili ulogu ranijih nagrada. Zatim pojačavamo one korake duž eksperimentalnog puta koji donose veće nagrade.

> Saznajte više o algoritmu gradijenata politike i pogledajte ga u akciji u [primjeru bilježnice](CartPole-RL-TF.ipynb).

## Algoritam Actor-Critic

Poboljšana verzija pristupa gradijenata politike naziva se **Actor-Critic**. Glavna ideja iza njega je da se neuronska mreža trenira da vraća dvije stvari:

* Politiku koja određuje koju akciju poduzeti. Ovaj dio se naziva **actor**.
* Procjenu ukupne nagrade koju možemo očekivati u ovom stanju - ovaj dio se naziva **critic**.

Na neki način, ova arhitektura podsjeća na [GAN](../../4-ComputerVision/10-GANs/README.md), gdje imamo dvije mreže koje se treniraju jedna protiv druge. U modelu actor-critic, actor predlaže akciju koju trebamo poduzeti, a critic pokušava biti kritičan i procijeniti rezultat. Međutim, naš cilj je trenirati te mreže ujedinjeno.

Budući da znamo i stvarne kumulativne nagrade i rezultate koje critic vraća tijekom eksperimenta, relativno je lako izgraditi funkciju gubitka koja će minimizirati razliku između njih. To nam daje **critic loss**. **Actor loss** možemo izračunati koristeći isti pristup kao u algoritmu gradijenata politike.

Nakon pokretanja jednog od tih algoritama, možemo očekivati da će naš CartPole izgledati ovako:

![balansirajući cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Vježbe: Gradijenti politike i Actor-Critic RL

Nastavite učiti u sljedećim bilježnicama:

* [RL u TensorFlowu](CartPole-RL-TF.ipynb)
* [RL u PyTorchu](CartPole-RL-PyTorch.ipynb)

## Ostali RL zadaci

Pojačano učenje danas je brzo rastuće područje istraživanja. Neki od zanimljivih primjera pojačanog učenja su:

* Podučavanje računala da igra **Atari igre**. Izazovni dio ovog problema je što nemamo jednostavno stanje predstavljeno kao vektor, već snimku zaslona - i moramo koristiti CNN za pretvaranje slike zaslona u vektor značajki ili za izdvajanje informacija o nagradi. Atari igre dostupne su u Gymu.
* Podučavanje računala da igra društvene igre, poput šaha i Goa. Nedavno su programi poput **Alpha Zero** postigli vrhunske rezultate trenirajući se od nule, gdje dva agenta igraju jedan protiv drugog i poboljšavaju se u svakom koraku.
* U industriji, RL se koristi za stvaranje sustava upravljanja iz simulacije. Usluga nazvana [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) posebno je dizajnirana za to.

## Zaključak

Sada smo naučili kako trenirati agente da postignu dobre rezultate samo pružanjem funkcije nagrade koja definira željeno stanje igre i omogućavanjem inteligentnog istraživanja prostora pretraživanja. Uspješno smo isprobali dva algoritma i postigli dobar rezultat u relativno kratkom vremenskom razdoblju. Međutim, ovo je tek početak vašeg putovanja u RL, i svakako biste trebali razmotriti pohađanje zasebnog tečaja ako želite dublje istražiti.

## 🚀 Izazov

Istražite primjene navedene u odjeljku 'Ostali RL zadaci' i pokušajte implementirati jednu!

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Pregled i samostalno učenje

Saznajte više o klasičnom pojačanom učenju u našem [kurikulumu za početnike u strojnome učenju](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Pogledajte [ovaj odličan video](https://www.youtube.com/watch?v=qv6UVOQ0F44) o tome kako računalo može naučiti igrati Super Mario.

## Zadatak: [Trenirajte Mountain Car](lab/README.md)

Vaš cilj tijekom ovog zadatka bit će trenirati drugačije Gym okruženje - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

