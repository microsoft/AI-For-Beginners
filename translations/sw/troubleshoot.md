# Mwongozo wa Kutatua Matatizo ya AI-For-Beginners

Mwongozo huu unakusaidia kutatua matatizo ya kawaida unayokutana nayo unapotumia au kuchangia kwenye [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) hifadhi. Kila tatizo lina maelezo ya msingi, dalili, maelezo, na hatua za kutatua.

---

## Jedwali la Maudhui

- [Masuala ya Jumla](../..)
- [Masuala ya Usakinishaji](../..)
- [Masuala ya Usanidi](../..)
- [Kuendesha Notebooks](../..)
- [Matatizo ya Utendaji](../..)
- [Matatizo ya Tovuti ya Kitabu](../..)
- [Masuala ya Kuchangia](../..)
- [Maswali Yanayoulizwa Mara kwa Mara (FAQ)](../..)
- [Kupata Msaada](../..)

---

## Masuala ya Jumla

### 1. Hifadhi Haikopi Kwa Usahihi

**Maelezo ya Msingi:** Kukopi hifadhi hukuruhusu kunakili hifadhi kwenye mashine yako.

**Dalili:**
- Kosa: `fatal: repository not found`
- Kosa: `Permission denied (publickey)`

**Sababu Zinawezekana:**
- URL ya hifadhi si sahihi
- Ruhusa hazitoshi
- Funguo za SSH hazijasakinishwa

**Suluhisho:**
1. **Hakikisha URL ya hifadhi.**  
   Tumia URL ya HTTPS:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Badilisha kwenda HTTPS ikiwa SSH inashindwa.**  
   Ikiwa unaona `Permission denied (publickey)`, tumia kiungo cha HTTPS badala ya SSH.
3. **Sanidi funguo za SSH (hiari).**  
   Ikiwa unataka kutumia SSH, fuata [Mwongozo wa SSH wa GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Masuala ya Usakinishaji

### 2. Masuala ya Mazingira ya Python

**Maelezo ya Msingi:** Hifadhi inategemea Python na maktaba mbalimbali.

**Dalili:**
- Kosa: `ModuleNotFoundError: No module named '<package>'`
- Makosa ya uingizaji unapoendesha script au notebooks

**Sababu Zinawezekana:**
- Vitegemezi havijasakinishwa
- Toleo la Python si sahihi

**Suluhisho:**
1. **Sanidi mazingira ya kawaida.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Sakinisha vitegemezi.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Hakikisha toleo la Python.**  
   Tumia Python 3.7 au jipya zaidi.  
   ```bash
   python --version
   ```

### 3. Jupyter Haijasakinishwa

**Maelezo ya Msingi:** Notebooks ni rasilimali kuu ya kujifunza.

**Dalili:**
- Kosa: `jupyter: command not found`
- Notebooks zinashindwa kuzinduliwa

**Sababu Zinawezekana:**
- Jupyter haijasakinishwa

**Suluhisho:**
1. **Sakinisha Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   au, ikiwa unatumia Anaconda:
   ```bash
   conda install notebook
   ```
2. **Anzisha Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Migongano ya Toleo la Vitegemezi

**Maelezo ya Msingi:** Miradi inaweza kuvunjika ikiwa matoleo ya maktaba hayalingani.

**Dalili:**
- Makosa au maonyo kuhusu matoleo yasiyolingana

**Sababu Zinawezekana:**
- Maktaba za Python za zamani au zinazogongana

**Suluhisho:**
1. **Sakinisha katika mazingira safi.**  
   Futa venv/conda env ya zamani na unda mpya.
2. **Tumia matoleo sahihi.**  
   Daima endesha:
   ```bash
   pip install -r requirements.txt
   ```
   Ikiwa hii inashindwa, sakinisha maktaba zinazokosekana kwa mkono kama ilivyoelezwa kwenye README.

---

## Masuala ya Usanidi

### 5. Vigezo vya Mazingira Havijasetiwa

**Maelezo ya Msingi:** Baadhi ya moduli zinaweza kuhitaji funguo, tokeni, au mipangilio ya usanidi.

**Dalili:**
- Kosa: `KeyError` au maonyo kuhusu usanidi unaokosekana

**Sababu Zinawezekana:**
- Vigezo vya mazingira vinavyohitajika havijasetiwa

**Suluhisho:**
1. **Angalia faili kama `.env.example` au zinazofanana.**
2. **Unda faili `.env` na ujaze maadili yanayohitajika.**
3. **Pakia upya terminal au IDE yako baada ya kusanidi vigezo vya mazingira.**

---

## Kuendesha Notebooks

### 6. Notebook Haifunguki au Haifanyi Kazi

**Maelezo ya Msingi:** Notebooks za Jupyter zinahitaji usanidi sahihi.

**Dalili:**
- Notebook inashindwa kuzinduliwa
- Kivinjari hakifunguki kiotomatiki

**Sababu Zinawezekana:**
- Jupyter haijasakinishwa
- Masuala ya usanidi wa kivinjari

**Suluhisho:**
1. **Sakinisha Jupyter (angalia Masuala ya Usakinishaji hapo juu).**
2. **Fungua notebooks kwa mkono.**
   - Nakili URL kutoka terminal (mfano, `http://localhost:8888/?token=...`) na uiweke kwenye kivinjari chako.

### 7. Kernel Inazimika au Kuganda

**Maelezo ya Msingi:** Kernel za notebook zinaweza kuzimika kutokana na mipaka ya rasilimali au makosa ya msimbo.

**Dalili:**
- Kernel inakufa au kuanzishwa upya mara kwa mara
- Makosa ya kumbukumbu (out-of-memory)

**Sababu Zinawezekana:**
- Seti kubwa za data
- Msimbo au maktaba zisizolingana

**Suluhisho:**
1. **Anzisha upya kernel.**  
   Tumia kitufe cha "Restart Kernel" kwenye Jupyter.
2. **Angalia matumizi ya kumbukumbu.**  
   Funga programu zisizotumika.
3. **Endesha notebooks kwenye majukwaa ya wingu.**  
   Tumia [Google Colab](https://colab.research.google.com/) au [Azure Notebooks](https://notebooks.azure.com/).

---

## Matatizo ya Utendaji

### 8. Notebooks Zinachelewa Kuendesha

**Maelezo ya Msingi:** Baadhi ya kazi za AI zinahitaji kumbukumbu kubwa na CPU.

**Dalili:**
- Utekelezaji wa polepole
- Feni ya laptop inafanya kazi kwa sauti kubwa

**Sababu Zinawezekana:**
- Seti kubwa za data au mifano
- Rasilimali za mfumo zilizopunguzwa

**Suluhisho:**
1. **Tumia jukwaa la wingu.**
   - Pakia notebook kwenye Colab au Azure Notebooks.
2. **Punguza ukubwa wa seti ya data.**
   - Tumia data ya sampuli kwa mazoezi.
3. **Funga programu zisizohitajika.**
   - Ondoa RAM ya mfumo.

---

## Matatizo ya Tovuti ya Kitabu

### 9. Sura Haifunguki

**Maelezo ya Msingi:** Kitabu cha mtandaoni kinaonyesha masomo na sura.

**Dalili:**
- Sura (mfano, Transformers/BERT) haipo au haifunguki

**Tatizo Linalojulikana:**  
- [Tatizo #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. haifunguki kwenye tovuti ya kitabu.” Imesababishwa na kosa la jina la faili (`READMEtransformers.md` badala ya `README.md`).

**Suluhisho:**
1. **Angalia makosa ya kubadilisha jina la faili.**  
   Ikiwa wewe ni mchangiaji, hakikisha faili za sura zimepewa jina `README.md`.
2. **Ripoti faili zinazokosekana.**  
   Fungua tatizo la GitHub na jina la sura na maelezo ya kosa.

---

## Masuala ya Kuchangia

### 10. PR Haikubaliwi au Majengo Yanashindwa

**Maelezo ya Msingi:** Michango lazima ipite majaribio na kufuata miongozo.

**Dalili:**
- Ombi la kuvuta limekataliwa
- Makosa ya CI/CD pipeline

**Sababu Zinawezekana:**
- Majaribio yanashindwa
- Kutofuata viwango vya msimbo

**Suluhisho:**
1. **Soma miongozo ya kuchangia.**
   - Fuata [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) ya hifadhi.
2. **Endesha majaribio kwa ndani kabla ya kusukuma.**
3. **Angalia sheria za linting au mahitaji ya muundo.**

---

## FAQ

### Ninaweza kupata wapi msaada kwa moduli maalum?
- Kila moduli kwa kawaida ina README yake. Anza hapo kwa vidokezo vya usanidi na matumizi.

### Ninawezaje kuripoti hitilafu au kuomba kipengele?
- [Fungua Tatizo la GitHub](https://github.com/microsoft/AI-For-Beginners/issues/new) na maelezo wazi na hatua za kuzalisha.

### Je, ninaweza kuomba msaada ikiwa tatizo langu halipo kwenye orodha?
- Ndiyo! Tafuta masuala yaliyopo kwanza, na ikiwa huoni tatizo lako, unda tatizo jipya.

---

## Kupata Msaada

- **Angalia Masuala:** [Masuala ya GitHub](https://github.com/microsoft/AI-For-Beginners/issues)
- **Uliza Maswali:** Tumia Majadiliano ya GitHub au fungua tatizo.
- **Jamii:** Tazama viungo vya hifadhi kwa chaguo la mazungumzo/jukwaa.

---

_Ilisasishwa Mwisho: 2025-09-20_

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.