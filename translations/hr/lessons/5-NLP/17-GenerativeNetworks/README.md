# Generativne mreže

## [Kviz prije predavanja](https://ff-quizzes.netlify.app/en/ai/quiz/33)

Rekurentne neuronske mreže (RNN) i njihove varijante s kontroliranim ćelijama, poput ćelija dugog kratkoročnog pamćenja (LSTM) i kontroliranih rekurentnih jedinica (GRU), omogućile su modeliranje jezika jer mogu naučiti redoslijed riječi i predvidjeti sljedeću riječ u nizu. To nam omogućuje korištenje RNN-a za **generativne zadatke**, poput generiranja običnog teksta, strojnog prevođenja, pa čak i opisivanja slika.

> ✅ Razmislite o svim situacijama u kojima ste imali koristi od generativnih zadataka, poput dovršavanja teksta dok tipkate. Istražite svoje omiljene aplikacije i provjerite koriste li RNN.

U arhitekturi RNN-a koju smo raspravili u prethodnoj jedinici, svaka RNN jedinica proizvodila je sljedeće skriveno stanje kao izlaz. Međutim, možemo dodati još jedan izlaz svakoj rekurentnoj jedinici, što bi nam omogućilo da generiramo **niz** (jednake duljine kao originalni niz). Osim toga, možemo koristiti RNN jedinice koje ne primaju ulaz na svakom koraku, već samo uzimaju početni vektor stanja i zatim proizvode niz izlaza.

To omogućuje različite neuronske arhitekture prikazane na slici ispod:

![Slika koja prikazuje uobičajene uzorke rekurentnih neuronskih mreža.](../../../../../translated_images/hr/unreasonable-effectiveness-of-rnn.541ead816778f42d.webp)

> Slika iz blog posta [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) autora [Andrej Karpaty](http://karpathy.github.io/)

* **Jedan-na-jedan** je tradicionalna neuronska mreža s jednim ulazom i jednim izlazom
* **Jedan-na-više** je generativna arhitektura koja prima jednu ulaznu vrijednost i generira niz izlaznih vrijednosti. Na primjer, ako želimo trenirati mrežu za **opisivanje slika** koja bi proizvela tekstualni opis slike, možemo sliku koristiti kao ulaz, proslijediti je kroz CNN kako bismo dobili skriveno stanje, a zatim koristiti rekurentni lanac za generiranje opisa riječ po riječ
* **Više-na-jedan** odgovara RNN arhitekturama koje smo opisali u prethodnoj jedinici, poput klasifikacije teksta
* **Više-na-više**, ili **niz-na-niz**, odgovara zadacima poput **strojnog prevođenja**, gdje prvo RNN prikuplja sve informacije iz ulaznog niza u skriveno stanje, a zatim drugi RNN lanac razvija ovo stanje u izlazni niz.

U ovoj jedinici fokusirat ćemo se na jednostavne generativne modele koji nam pomažu generirati tekst. Radi jednostavnosti, koristit ćemo tokenizaciju na razini znakova.

Trenirat ćemo ovaj RNN da generira tekst korak po korak. Na svakom koraku uzet ćemo niz znakova duljine `nchars` i tražiti od mreže da generira sljedeći izlazni znak za svaki ulazni znak:

![Slika koja prikazuje primjer generiranja riječi 'HELLO' pomoću RNN-a.](../../../../../translated_images/hr/rnn-generate.56c54afb52f9781d.webp)

Tijekom generiranja teksta (tijekom inferencije), počinjemo s nekim **poticajem**, koji se prosljeđuje kroz RNN ćelije kako bi se generiralo njegovo međustanje, a zatim iz tog stanja počinje generiranje. Generiramo jedan znak po jedan, prosljeđujemo stanje i generirani znak sljedećoj RNN ćeliji kako bismo generirali sljedeći znak, sve dok ne generiramo dovoljno znakova.

<img src="../../../../../translated_images/hr/rnn-generate-inf.5168dc65e0370eea.webp" width="60%"/>

> Slika autora

## ✍️ Vježbe: Generativne mreže

Nastavite učiti u sljedećim bilježnicama:

* [Generativne mreže s PyTorchom](GenerativePyTorch.ipynb)
* [Generativne mreže s TensorFlowom](GenerativeTF.ipynb)

## Mekano generiranje teksta i temperatura

Izlaz svake RNN ćelije je distribucija vjerojatnosti znakova. Ako uvijek uzmemo znak s najvećom vjerojatnošću kao sljedeći znak u generiranom tekstu, tekst često može postati "cikličan", ponavljajući iste sekvence znakova iznova i iznova, kao u ovom primjeru:

```
today of the second the company and a second the company ...
```

Međutim, ako pogledamo distribuciju vjerojatnosti za sljedeći znak, može se dogoditi da razlika između nekoliko najvećih vjerojatnosti nije velika, npr. jedan znak može imati vjerojatnost 0.2, a drugi 0.19, itd. Na primjer, kada tražimo sljedeći znak u nizu '*play*', sljedeći znak može jednako dobro biti razmak ili **e** (kao u riječi *player*).

To nas dovodi do zaključka da nije uvijek "pravedno" odabrati znak s najvećom vjerojatnošću, jer odabir drugog po redu također može dovesti do smislenog teksta. Mudrije je **uzorkovati** znakove iz distribucije vjerojatnosti koju daje izlaz mreže. Također možemo koristiti parametar **temperatura**, koji će izravnati distribuciju vjerojatnosti ako želimo dodati više slučajnosti, ili je učiniti strmijom ako želimo više se držati znakova s najvećom vjerojatnošću.

Istražite kako je ovo mekano generiranje teksta implementirano u bilježnicama povezanima gore.

## Zaključak

Iako generiranje teksta može biti korisno samo po sebi, glavne prednosti dolaze iz mogućnosti generiranja teksta pomoću RNN-a iz nekog početnog vektora značajki. Na primjer, generiranje teksta koristi se kao dio strojnog prevođenja (niz-na-niz, u ovom slučaju vektor stanja iz *enkodera* koristi se za generiranje ili *dekodiranje* prevedene poruke), ili generiranja tekstualnog opisa slike (u kojem slučaju vektor značajki dolazi iz CNN ekstraktora).

## 🚀 Izazov

Proučite neke lekcije na Microsoft Learn na ovu temu

* Generiranje teksta s [PyTorchom](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlowom](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Kviz nakon predavanja](https://ff-quizzes.netlify.app/en/ai/quiz/34)

## Pregled i samostalno učenje

Evo nekoliko članaka za proširenje vašeg znanja

* Različiti pristupi generiranju teksta s Markovim lancem, LSTM-om i GPT-2: [blog post](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Primjer generiranja teksta u [Keras dokumentaciji](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Zadatak](lab/README.md)

Vidjeli smo kako generirati tekst znak po znak. U laboratoriju ćete istražiti generiranje teksta na razini riječi.

---

