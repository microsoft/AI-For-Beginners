# AI-For-Beginners Troubleshooting Guide

This guide helps you resolve common issues encountered while using or contributing to the [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) repository. Each problem includes background, symptoms, explanations, and step-by-step solutions.

---

## Table of Contents

- [General Issues](#general-issues)
- [Installation Issues](#installation-issues)
- [Configuration Issues](#configuration-issues)
- [Running Notebooks](#running-notebooks)
- [Performance Problems](#performance-problems)
- [Textbook Website Problems](#textbook-website-problems)
- [Contributing Issues](#contributing-issues)
- [FAQ](#faq)
- [Getting Help](#getting-help)

---

## General Issues

### 1. Repository Not Cloning Properly

**Background:** Cloning allows you to copy the repository to your machine.

**Symptoms:**
- Error: `fatal: repository not found`
- Error: `Permission denied (publickey)`

**Possible Causes:**
- Incorrect repository URL
- Insufficient permissions
- SSH keys not configured

**Solutions:**
1. **Check the repository URL.**  
   Use the HTTPS URL:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Switch to HTTPS if SSH fails.**  
   If you see `Permission denied (publickey)`, use the HTTPS link above instead of SSH.
3. **Configure SSH keys (optional).**  
   If you want to use SSH, follow [GitHub's SSH guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Installation Issues

### 2. Python Environment Issues

**Background:** The repository relies on Python and various libraries.

**Symptoms:**
- Error: `ModuleNotFoundError: No module named '<package>'`
- Import errors when running scripts or notebooks

**Possible Causes:**
- Dependencies not installed
- Wrong Python version

**Solutions:**
1. **Set up a virtual environment.**  
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

### 3. Jupyter Not Installed

**Background:** Notebooks are a core learning resource.

**Symptoms:**
- Error: `jupyter: command not found`
- Notebooks fail to launch

**Possible Causes:**
- Jupyter not installed

**Solutions:**
1. **Install Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   or, if using Anaconda:
   ```bash
   conda install notebook
   ```
2. **Start Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Dependency Version Conflicts

**Background:** Projects can break if package versions are mismatched.

**Symptoms:**
- Errors or warnings about incompatible versions

**Possible Causes:**
- Old or conflicting Python packages

**Solutions:**
1. **Install in a clean environment.**  
   Delete old venv/conda env and create a new one.
2. **Use exact versions.**  
   Always run:
   ```bash
   pip install -r requirements.txt
   ```
   If this fails, manually install missing packages as described in README.

---

## Configuration Issues

### 5. Environment Variables Not Set

**Background:** Some modules may require keys, tokens, or config settings.

**Symptoms:**
- Error: `KeyError` or warnings about missing configuration

**Possible Causes:**
- Required environment variables not set

**Solutions:**
1. **Check for `.env.example` or similar files.**
2. **Create a `.env` file and fill in required values.**
3. **Reload your terminal or IDE after setting environment variables.**

---

## Running Notebooks

### 6. Notebook Will Not Open or Run

**Background:** Jupyter notebooks need proper setup.

**Symptoms:**
- Notebook fails to launch
- Browser not opening automatically

**Possible Causes:**
- Jupyter not installed
- Browser configuration issues

**Solutions:**
1. **Install Jupyter (see Installation Issues above).**
2. **Open notebooks manually.**
   - Copy the URL from terminal (e.g., `http://localhost:8888/?token=...`) and paste it into your browser.

### 7. Kernel Crashing or Freezing

**Background:** Notebook kernels can crash due to resource limits or code errors.

**Symptoms:**
- Kernel dies or restarts repeatedly
- Out-of-memory errors

**Possible Causes:**
- Large datasets
- Incompatible code or packages

**Solutions:**
1. **Restart the kernel.**  
   Use the "Restart Kernel" button in Jupyter.
2. **Check memory usage.**  
   Close unused applications.
3. **Run notebooks on cloud platforms.**  
   Use [Google Colab](https://colab.research.google.com/) or [Azure Notebooks](https://notebooks.azure.com/).

---

## Performance Problems

### 8. Notebooks Running Slowly

**Background:** Some AI tasks require significant memory and CPU.

**Symptoms:**
- Slow execution
- Laptop fan running loudly

**Possible Causes:**
- Large datasets or models
- Limited system resources

**Solutions:**
1. **Use a cloud platform.**
   - Upload notebook to Colab or Azure Notebooks.
2. **Reduce dataset size.**
   - Use sample data for practice.
3. **Close unnecessary programs.**
   - Free up system RAM.

---

## Textbook Website Problems

### 9. Chapter Not Loading

**Background:** The online textbook displays lessons and chapters.

**Symptoms:**
- A chapter (e.g., Transformers/BERT) is missing or not opening

**Known Issue:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. can't be opened on the textbook website.” Caused by a filename error (`READMEtransformers.md` instead of `README.md`).

**Solutions:**
1. **Check for file renaming errors.**  
   If you’re a contributor, ensure chapter files are named `README.md`.
2. **Report missing files.**  
   Open a GitHub issue with the chapter name and error details.

---

## Contributing Issues

### 10. PR Not Accepted or Builds Failing

**Background:** Contributions must pass tests and follow guidelines.

**Symptoms:**
- Pull request rejected
- CI/CD pipeline errors

**Possible Causes:**
- Failing tests
- Not following coding standards

**Solutions:**
1. **Read the contribution guidelines.**
   - Follow the repository’s [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md).
2. **Run tests locally before pushing.**
3. **Check for linting rules or formatting requirements.**

---

## FAQ

### Where can I find help for specific modules?
- Each module usually has its own README. Start there for setup and usage tips.

### How do I report a bug or request a feature?
- [Open a GitHub Issue](https://github.com/microsoft/AI-For-Beginners/issues/new) with a clear description and steps to reproduce.

### Can I ask for help if my problem isn’t listed?
- Yes! Search existing issues first, and if you don’t find your problem, create a new issue.

---

## Getting Help

- **Check Issues:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Ask Questions:** Use GitHub Discussions or open an issue.
- **Community:** See repository links for chat/forum options.

---

_Last Updated: 2025-09-20_
