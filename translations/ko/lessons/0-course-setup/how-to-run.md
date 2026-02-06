# 코드 실행 방법

이 커리큘럼에는 실행할 수 있는 많은 예제와 실습이 포함되어 있습니다. 이를 실행하려면 이 커리큘럼의 일부로 제공되는 Jupyter 노트북에서 Python 코드를 실행할 수 있어야 합니다. 코드를 실행하는 몇 가지 방법이 있습니다:

## 컴퓨터에서 로컬로 실행

컴퓨터에서 코드를 로컬로 실행하려면 Python 설치가 필요합니다. 한 가지 권장 방법은 **[miniconda](https://conda.io/en/latest/miniconda.html)**를 설치하는 것입니다. 이는 비교적 가벼운 설치로, 다양한 Python **가상 환경**을 위한 `conda` 패키지 관리자를 지원합니다.

miniconda를 설치한 후, 저장소를 복제하고 이 과정에 사용할 가상 환경을 만드십시오:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Python 확장 기능과 함께 Visual Studio Code 사용

이 커리큘럼은 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste)에서 [Python 확장 기능](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)과 함께 열었을 때 가장 잘 사용됩니다.

> **참고**: 저장소를 복제하고 VS Code에서 디렉터리를 열면 자동으로 Python 확장 기능 설치를 제안합니다. 위에서 설명한 대로 miniconda도 설치해야 합니다.

> **참고**: VS Code에서 저장소를 컨테이너에서 다시 열도록 제안하면, 로컬 Python 설치를 사용하려면 이를 거부해야 합니다.

### 브라우저에서 Jupyter 사용

브라우저에서 컴퓨터의 Jupyter 환경도 사용할 수 있습니다. 고전적인 Jupyter와 JupyterHub 모두 자동 완성, 코드 강조 등 편리한 개발 환경을 제공합니다.

로컬로 Jupyter를 시작하려면, 과정 디렉터리로 이동하여 다음을 실행하세요:

```bash
jupyter notebook
```
또는
```bash
jupyterhub
```
그런 다음 `.ipynb` 파일 중 아무거나 찾아 열어 작업을 시작할 수 있습니다.

### 컨테이너에서 실행

Python 설치에 대한 대안으로 컨테이너에서 코드를 실행할 수 있습니다. 저장소는 이 저장소용 컨테이너 빌드 방법을 안내하는 특별한 `.devcontainer` 폴더를 제공하므로, VS Code는 코드를 컨테이너에서 다시 열 기회를 제공합니다. 이 방법은 Docker 설치가 필요하며 좀 더 복잡하므로, 숙련된 사용자에게 권장합니다.

## 클라우드에서 실행

로컬에 Python을 설치하고 싶지 않고, 클라우드 자원에 접근할 수 있다면 클라우드에서 코드를 실행하는 좋은 대안이 있습니다. 다음과 같은 방법들이 있습니다:

* **[GitHub Codespaces](https://github.com/features/codespaces)** 사용하기: GitHub에서 가상 환경을 만들어 VS Code 브라우저 인터페이스를 통해 접근할 수 있습니다. Codespaces에 접근 권한이 있으면 저장소의 **Code** 버튼을 클릭해 codespace를 시작하고 빠르게 실행할 수 있습니다.
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** 사용하기: [Binder](https://mybinder.org)는 GitHub상의 코드를 테스트할 수 있도록 클라우드에서 무료 컴퓨팅 자원을 제공합니다. 저장소 첫 페이지에 Binder에서 저장소를 열 수 있는 버튼이 있어, 이를 클릭하면 기저 컨테이너가 빌드되고 Jupyter 웹 인터페이스가 원활하게 시작됩니다.

> **참고**: 오용 방지를 위해 Binder에서는 일부 웹 자원 접근이 차단됩니다. 이로 인해 공개 인터넷에서 모델이나 데이터셋을 가져오는 일부 코드가 작동하지 않을 수 있습니다. 일부 우회 방법을 찾아야 할 수 있습니다. 또한 Binder에서 제공하는 컴퓨팅 자원은 초보 수준이므로, 특히 나중에 복잡한 수업에서는 훈련 속도가 느립니다.

## GPU가 포함된 클라우드에서 실행

이 커리큘럼의 후반 수업 중 일부는 GPU 지원이 크게 도움이 됩니다. 예를 들어 모델 훈련은 그렇지 않으면 매우 느릴 수 있습니다. 특히 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 또는 기관을 통해 클라우드에 접근할 수 있다면 다음 옵션들을 고려할 수 있습니다:

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) 생성 후 Jupyter로 연결하기. 그 후 저장소를 머신에 복제하고 학습을 시작할 수 있습니다. NC 시리즈 VM에는 GPU 지원이 포함되어 있습니다.

> **참고**: Azure for Students를 포함한 일부 구독은 기본적으로 GPU를 지원하지 않습니다. 추가 GPU 코어 요청을 기술 지원에 해야 할 수 있습니다.

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) 생성 후 노트북 기능 사용. [이 영상](https://azure-for-academics.github.io/quickstart/azureml-papers/)은 Azure ML 노트북에 저장소를 복제하고 사용하는 방법을 보여줍니다.

또한 일부 무료 GPU 지원이 포함된 Google Colab을 사용할 수도 있으며, Jupyter 노트북을 업로드해 차례대로 실행할 수 있습니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 이용하여 번역되었습니다. 정확성을 위해 최선을 다했지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 공식적인 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->