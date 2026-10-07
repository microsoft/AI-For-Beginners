# Code Kaise Chalayein

Is curriculum mein bahut saare executable examples aur labs hain jinhe aap chalana chahenge. Iske liye, aapke paas is curriculum ke part ke roop mein diye gaye Jupyter notebooks mein Python code execute karne ki ability honi chahiye. Code chalane ke liye aapke paas kai options hain:

## Apne Computer Par Locally Chalayein

Apne computer par code chalane ke liye, Python installation zaroori hai. Ek suggestion hai **[miniconda](https://conda.io/en/latest/miniconda.html)** install karna - yeh ek lightweight installation hai jo alag-alag Python **virtual environments** ke liye `conda` package manager support karta hai.

miniconda install karne ke baad, repository clone kijiye aur is course ke liye use hone wala virtual environment banaiye:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code Ke Saath Python Extension Use Karna

Is curriculum ko use karne ka sabse accha tareeka hai ki aap ise [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) mein [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) ke saath kholein.

> **Note**: Jaise hi aap directory ko clone karke VS Code mein kholte hain, woh aapko automatically Python extension install karne ka suggestion dega. Aapko upar bataye anusar miniconda bhi install karna hoga.

> **Note**: Agar VS Code aapko repository ko container mein dobara kholne ka suggestion de, toh local Python installation use karne ke liye aapko ise decline kar dena chahiye.

### Browser Mein Jupyter Use Karna

Aap apne computer par browser se bhi Jupyter environment use kar sakte hain. Classic Jupyter aur JupyterHub dono ek convenient development environment dete hain jisme auto-completion, code highlighting, etc. shamil hain.

Jupyter ko locally start karne ke liye, course ki directory mein jaiye, aur yeh execute kijiye:

```bash
jupyter notebook
```
 ya
```bash
jupyterhub
```
 Iske baad aap kisi bhi `.ipynb` file par navigate kar sakte hain, unhe khol sakte hain aur kaam shuru kar sakte hain.

### Container Mein Chalana

Python installation ka ek alternative container mein code chalana ho sakta hai. Kyunki hamari repository mein ek special `.devcontainer` folder hai jo batata hai ki is repo ke liye container kaise banana hai, VS Code aapko code ko container mein dobara kholne ka mauka deta hai. Iske liye Docker installation chahiye hoga, aur yeh zyada complex hoga, isliye hum ise zyada experienced users ke liye recommend karte hain.

## Cloud Mein Chalana

Agar aap Python locally install nahi karna chahte, aur aapke paas kuch cloud resources ka access hai - toh code ko cloud mein chalana ek accha option hoga. Aap yeh kai tareeke se kar sakte hain:

* **[GitHub Codespaces](https://github.com/features/codespaces)** use karna, jo aapke liye GitHub par banaya gaya ek virtual environment hai, jise VS Code browser interface ke through access kiya ja sakta hai. Agar aapke paas Codespaces ka access hai, toh aap bas repo mein **Code** button par click karein, ek codespace start karein, aur turant kaam shuru kar dein.
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** use karna. [Binder](https://mybinder.org) cloud mein free computing resources deta hai taaki aap GitHub par maujood kuch code ko test kar sakein. Front page par ek button hai jo repository ko Binder mein kholta hai - isse aap turant Binder site par pahunch jayenge, jo underlying container banakar aapke liye seamlessly Jupyter web interface start kar dega.

> **Note**: Abuse rokne ke liye, Binder mein kuch web resources ka access block hai. Isse kuch code kaam nahi karega, jo public Internet se models aur/ya datasets fetch karta hai. Aapko kuch workarounds dhoondhne pad sakte hain. Saath hi, Binder jo compute resources deta hai woh kaafi basic hain, isliye training slow hogi, khaaskar baad ke zyada complex lessons mein.

## GPU Ke Saath Cloud Mein Chalana

Is curriculum ke kuch baad ke lessons GPU support se bahut fayda uthayenge. Jaise, model training warna bahut slow ho sakti hai. Aap kuch options apna sakte hain, khaaskar agar aapke paas cloud ka access hai, chahe [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ke through ho, ya apne institution ke through:

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) banaiye aur Jupyter ke through us se connect kijiye. Aap machine par repo clone kar sakte hain, aur learning shuru kar sakte hain. NC-series VMs mein GPU support hota hai.

> **Note**: Kuch subscriptions, jinme Azure for Students shamil hai, box se hi GPU support nahi dete. Aapko technical support request ke saath extra GPU cores request karne pad sakte hain.

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) banaiye aur wahan notebook feature use kijiye. [Yeh video](https://azure-for-academics.github.io/quickstart/azureml-papers/) dikhata hai ki Azure ML notebook mein repo clone karke use karna kaise shuru karein.

Aap Google Colab bhi use kar sakte hain, jisme kuch free GPU support milta hai, aur wahan Jupyter notebooks upload karke unhe ek-ek karke execute kar sakte hain.

---

<!-- HINGLISH NOTE START -->
**Note**:
Yeh document Hindi translation ko Hinglish (Roman script) mein convert karke banaya gaya hai, taaki padhna aur samajhna aasaan ho.
Isme kuch galtiyan ya anuvaad ki kamiyan ho sakti hain. Sabse sahi jaankari ke liye original English document ko hi authoritative source maanein.
<!-- HINGLISH NOTE END -->
