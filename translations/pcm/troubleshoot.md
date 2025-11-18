<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8d9c5a4a7c7798d699672a22cb7fea86",
  "translation_date": "2025-11-18T18:12:07+00:00",
  "source_file": "troubleshoot.md",
  "language_code": "pcm"
}
-->
# AI-For-Beginners Troubleshooting Guide

Dis guide go help you solve common wahala wey fit happen when you dey use or dey contribute to di [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) repository. Each problem get background, symptoms, explanation, and step-by-step solution.

---

## Table of Contents

- [General Wahala](../..)
- [Installation Wahala](../..)
- [Configuration Wahala](../..)
- [Running Notebooks](../..)
- [Performance Wahala](../..)
- [Textbook Website Wahala](../..)
- [Contributing Wahala](../..)
- [FAQ](../..)
- [How to Get Help](../..)

---

## General Wahala

### 1. Repository No Wan Clone Well

**Background:** Cloning na di way wey you go fit copy di repository enter your machine.

**Symptoms:**
- Error: `fatal: repository not found`
- Error: `Permission denied (publickey)`

**Possible Causes:**
- Di repository URL no correct
- You no get permission
- SSH keys no dey configured

**Solutions:**
1. **Check di repository URL.**  
   Use di HTTPS URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Switch to HTTPS if SSH no work.**  
   If you see `Permission denied (publickey)`, use di HTTPS link wey dey above instead of SSH.
3. **Configure SSH keys (optional).**  
   If you wan use SSH, follow [GitHub's SSH guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Installation Wahala

### 2. Python Environment Wahala

**Background:** Di repository dey depend on Python and some libraries.

**Symptoms:**
- Error: `ModuleNotFoundError: No module named '<package>'`
- Import errors when you dey run scripts or notebooks

**Possible Causes:**
- Dependencies no dey installed
- Wrong Python version

**Solutions:**
1. **Set up virtual environment.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Install dependencies.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Check Python version.**  
   Use Python 3.7 or newer.  
   ```bash
   python --version
   ```

### 3. Jupyter No Dey Installed

**Background:** Notebooks na di main learning resource.

**Symptoms:**
- Error: `jupyter: command not found`
- Notebooks no dey launch

**Possible Causes:**
- Jupyter no dey installed

**Solutions:**
1. **Install Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   or, if you dey use Anaconda:
   ```bash
   conda install notebook
   ```
2. **Start Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Dependency Version Wahala

**Background:** Projects fit break if package versions no match.

**Symptoms:**
- Errors or warnings about incompatible versions

**Possible Causes:**
- Old or conflicting Python packages

**Solutions:**
1. **Install for clean environment.**  
   Delete old venv/conda env and create new one.
2. **Use exact versions.**  
   Always run:
   ```bash
   pip install -r requirements.txt
   ```
   If e no work, manually install di missing packages as dem describe for README.

---

## Configuration Wahala

### 5. Environment Variables No Dey Set

**Background:** Some modules fit need keys, tokens, or config settings.

**Symptoms:**
- Error: `KeyError` or warnings about missing configuration

**Possible Causes:**
- Di environment variables wey dem need no dey set

**Solutions:**
1. **Check for `.env.example` or similar files.**
2. **Create `.env` file and put di values wey dem need.**
3. **Reload your terminal or IDE after you set di environment variables.**

---

## Running Notebooks

### 6. Notebook No Wan Open or Run

**Background:** Jupyter notebooks need proper setup.

**Symptoms:**
- Notebook no dey launch
- Browser no dey open automatically

**Possible Causes:**
- Jupyter no dey installed
- Browser configuration wahala

**Solutions:**
1. **Install Jupyter (check Installation Wahala above).**
2. **Open notebooks manually.**
   - Copy di URL from terminal (e.g., `http://localhost:8888/?token=...`) and paste am for your browser.

### 7. Kernel Dey Crash or Freeze

**Background:** Notebook kernels fit crash because of resource limits or code errors.

**Symptoms:**
- Kernel dey die or restart anyhow
- Out-of-memory errors

**Possible Causes:**
- Big datasets
- Code or packages wey no dey compatible

**Solutions:**
1. **Restart di kernel.**  
   Use di "Restart Kernel" button for Jupyter.
2. **Check memory usage.**  
   Close apps wey you no dey use.
3. **Run notebooks for cloud platforms.**  
   Use [Google Colab](https://colab.research.google.com/) or [Azure Notebooks](https://notebooks.azure.com/).

---

## Performance Wahala

### 8. Notebooks Dey Run Slow

**Background:** Some AI tasks dey need plenty memory and CPU.

**Symptoms:**
- Execution dey slow
- Laptop fan dey make noise

**Possible Causes:**
- Big datasets or models
- System resources no plenty

**Solutions:**
1. **Use cloud platform.**
   - Upload notebook go Colab or Azure Notebooks.
2. **Reduce dataset size.**
   - Use sample data for practice.
3. **Close programs wey you no need.**
   - Free up system RAM.

---

## Textbook Website Wahala

### 9. Chapter No Wan Load

**Background:** Di online textbook dey show lessons and chapters.

**Symptoms:**
- Chapter (e.g., Transformers/BERT) dey miss or no dey open

**Known Issue:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. no fit open for di textbook website.” E dey caused by filename error (`READMEtransformers.md` instead of `README.md`).

**Solutions:**
1. **Check for file renaming errors.**  
   If you be contributor, make sure say chapter files dey named `README.md`.
2. **Report missing files.**  
   Open GitHub issue with di chapter name and error details.

---

## Contributing Wahala

### 10. PR No Dey Accepted or Builds Dey Fail

**Background:** Contributions must pass tests and follow guidelines.

**Symptoms:**
- Pull request dey rejected
- CI/CD pipeline dey show errors

**Possible Causes:**
- Tests dey fail
- You no follow coding standards

**Solutions:**
1. **Read di contribution guidelines.**
   - Follow di repository’s [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md).
2. **Run tests locally before you push.**
3. **Check for linting rules or formatting requirements.**

---

## FAQ

### Where I fit find help for specific modules?
- Each module dey usually get im own README. Start from there for setup and usage tips.

### How I go report bug or request feature?
- [Open GitHub Issue](https://github.com/microsoft/AI-For-Beginners/issues/new) with clear description and steps to reproduce.

### I fit ask for help if my problem no dey listed?
- Yes! Search di existing issues first, and if you no see your problem, create new issue.

---

## How to Get Help

- **Check Issues:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Ask Questions:** Use GitHub Discussions or open issue.
- **Community:** Check repository links for chat/forum options.

---

_Last Updated: 2025-09-20_

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu don dey translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am accurate, abeg sabi say automatic translation fit get mistake or no correct well. Di original docu for im native language na di main correct source. For important information, e go beta make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->