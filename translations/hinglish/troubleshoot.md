# AI-For-Beginners Troubleshooting Guide

Yeh guide aapko [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) repository use karte waqt ya usme contribute karte waqt aane wali common problems solve karne mein madad karti hai. Har problem mein background, symptoms, explanation aur step-by-step solution diya gaya hai.

---

## Table of Contents

- [General Issues](../..)
- [Installation Issues](../..)
- [Configuration Issues](../..)
- [Notebooks chalana](../..)
- [Performance Issues](../..)
- [Textbook Website Issues](../..)
- [Contribution Issues](../..)
- [FAQ](../..)
- [Help kaise lein](../..)

---

## General Issues

### 1. Repository sahi se clone nahi ho rahi

**Background:** Cloning se aap repository ko apni machine par copy kar sakte hain.

**Symptoms:**
- Error: `fatal: repository not found`
- Error: `Permission denied (publickey)`

**Possible Causes:**
- Galat repository URL
- Permissions kam hain
- SSH keys configure nahi ki gayi hain

**Solutions:**
1. **Repository URL check karein.**  
   HTTPS URL use karein:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **SSH fail ho toh HTTPS par switch karein.**  
   Agar aapko `Permission denied (publickey)` dikhe, toh SSH ke bajay upar diya gaya HTTPS link use karein.
3. **SSH keys configure karein (optional).**  
   Agar aap SSH use karna chahte hain, toh [GitHub ki SSH guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) follow karein.

---

## Installation Issues

### 2. Python Environment Issues

**Background:** Repository Python aur kai libraries par depend karti hai.

**Symptoms:**
- Error: `ModuleNotFoundError: No module named '<package>'`
- Scripts ya notebooks chalate waqt import errors

**Possible Causes:**
- Dependencies install nahi ki gayi
- Python ka galat version

**Solutions:**
1. **Virtual environment set up karein.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Dependencies install karein.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Python version check karein.**  
   Python 3.7 ya usse naya version use karein.  
   ```bash
   python --version
   ```

### 3. Jupyter install nahi hai

**Background:** Notebooks ek main learning resource hain.

**Symptoms:**
- Error: `jupyter: command not found`
- Notebooks launch nahi ho rahi

**Possible Causes:**
- Jupyter install nahi hai

**Solutions:**
1. **Jupyter Notebook install karein.**  
   ```bash
   pip install notebook
   ```
   Ya, agar aap Anaconda use kar rahe hain:
   ```bash
   conda install notebook
   ```
2. **Jupyter Notebook start karein.**  
   ```bash
   jupyter notebook
   ```

### 4. Dependency Version Conflicts

**Background:** Package versions match na hone par projects toot sakte hain.

**Symptoms:**
- Incompatible versions ke baare mein errors ya warnings

**Possible Causes:**
- Purane ya conflicting Python packages

**Solutions:**
1. **Clean environment mein install karein.**  
   Purana venv/conda env hata dein aur naya banayein.
2. **Exact versions use karein.**  
   Hamesha yeh chalayein:
   ```bash
   pip install -r requirements.txt
   ```
   Agar yeh fail ho, toh README mein bataye gaye tareeke se missing packages manually install karein.

---

## Configuration Issues

### 5. Environment Variables set nahi hain

**Background:** Kuch modules ko keys, tokens ya config settings ki zaroorat ho sakti hai.

**Symptoms:**
- Error: `KeyError` ya missing configuration ke baare mein warnings

**Possible Causes:**
- Zaroori environment variables set nahi hain

**Solutions:**
1. **`.env.example` ya milti-julti files check karein.**
2. **Ek `.env` file banayein aur zaroori values bharein.**
3. **Environment variables set karne ke baad apna terminal ya IDE reload karein.**

---

## Notebooks chalana

### 6. Notebook khul ya chal nahi rahi

**Background:** Jupyter notebooks ko sahi setup ki zaroorat hoti hai.

**Symptoms:**
- Notebook launch nahi ho rahi
- Browser automatically nahi khul raha

**Possible Causes:**
- Jupyter install nahi hai
- Browser configuration issues

**Solutions:**
1. **Jupyter install karein (upar Installation Issues dekhein).**
2. **Notebook ko manually kholein.**
   - Terminal se URL copy karein (jaise, `http://localhost:8888/?token=...`) aur use apne browser mein paste karein.

### 7. Kernel crash ya freeze ho raha hai

**Background:** Notebook kernels resource limits ya code errors ki wajah se crash ho sakte hain.

**Symptoms:**
- Kernel baar-baar die ya restart hota hai
- Out-of-memory errors

**Possible Causes:**
- Bade datasets
- Incompatible code ya packages

**Solutions:**
1. **Kernel restart karein.**  
   Jupyter mein "Restart Kernel" button use karein.
2. **Memory usage check karein.**  
   Zaroori na hone wali applications band karein.
3. **Notebooks ko cloud platform par chalayein.**  
   [Google Colab](https://colab.research.google.com/) ya [Azure Notebooks](https://notebooks.azure.com/) use karein.

---

## Performance Issues

### 8. Notebooks slow chal rahi hain

**Background:** Kuch AI tasks ko kaafi memory aur CPU ki zaroorat hoti hai.

**Symptoms:**
- Slow execution
- Laptop ka fan tez chal raha hai

**Possible Causes:**
- Bade datasets ya models
- Limited system resources

**Solutions:**
1. **Cloud platform use karein.**
   - Notebooks ko Colab ya Azure Notebooks par upload karein.
2. **Dataset ka size kam karein.**
   - Practice ke liye sample data use karein.
3. **Zaroori na hone wale programs band karein.**
   - System RAM free karein.

---

## Textbook Website Issues

### 9. Chapter load nahi ho raha

**Background:** Online textbook lessons aur chapters display karti hai.

**Symptoms:**
- Koi chapter (jaise, Transformers/BERT) missing hai ya khul nahi raha

**Known Issue:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. textbook website par nahi khul raha.” Iski wajah file name ki galti hai (`README.md` ke bajay `READMEtransformers.md`).

**Solutions:**
1. **File naming errors check karein.**  
   Agar aap contributor hain, toh dhyan rakhein ki chapter files ka naam `README.md` ho.
2. **Missing files report karein.**  
   Chapter ke naam aur error ki details ke saath ek GitHub issue kholein.

---

## Contribution Issues

### 10. PR accept nahi ho raha ya builds fail ho rahe hain

**Background:** Contributions ko tests pass karne chahiye aur guidelines follow karni chahiye.

**Symptoms:**
- Pull request reject ho gaya
- CI/CD pipeline errors

**Possible Causes:**
- Tests fail ho rahe hain
- Coding standards follow nahi kiye gaye

**Solutions:**
1. **Contribution guidelines padhein.**
   - Repository ki [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) follow karein.
2. **Push karne se pehle tests locally chalayein.**
3. **Linting rules ya formatting requirements check karein.**

---

## FAQ

### Specific modules ke liye madad kahan mil sakti hai?
- Har module ka aam taur par apna README hota hai. Setup aur usage tips ke liye wahin se shuru karein.

### Bug report ya feature request kaise karein?
- Clear description aur reproduce karne ke steps ke saath [GitHub Issue kholein](https://github.com/microsoft/AI-For-Beginners/issues/new).

### Agar meri problem list mein nahi hai toh kya main madad maang sakta hoon?
- Haan! Pehle existing issues search karein, aur agar aapko apni problem nahi milti, toh ek naya issue banayein.

---

## Help kaise lein

- **Issues check karein:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Sawaal poochein:** GitHub Discussions use karein ya ek issue kholein.
- **Community:** Chat/forum options ke liye repository ke links dekhein.

---

_Last updated: 2025-09-20_

---

<!-- HINGLISH NOTE START -->
**Note**:
Yeh document Hindi translation ko Hinglish (Roman script) mein convert karke banaya gaya hai, taaki padhna aur samajhna aasaan ho.
Isme kuch galtiyan ya anuvaad ki kamiyan ho sakti hain. Sabse sahi jaankari ke liye original English document ko hi authoritative source maanein.
<!-- HINGLISH NOTE END -->
