# 코드 실행 방법

이 커리큘럼에는 실행 가능한 예제와 실습이 많이 포함되어 있습니다. 이를 실행하기 위해서는 이 커리큘럼의 일환으로 제공되는 Jupyter Notebooks에서 Python 코드를 실행할 수 있는 능력이 필요합니다. 코드를 실행하는 방법은 여러 가지가 있습니다.

## 컴퓨터에서 로컬로 실행하기

코드를 로컬 컴퓨터에서 실행하려면 Python의 어떤 버전이 설치되어 있어야 합니다. 개인적으로 **[miniconda](https://conda.io/en/latest/miniconda.html)** 설치를 추천합니다. 이는 다양한 Python **가상 환경**을 위한 `conda` 패키지 관리자를 지원하는 가벼운 설치입니다.

miniconda를 설치한 후, 리포지토리를 클론하고 이 과정에서 사용할 가상 환경을 생성해야 합니다:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Python 확장과 함께 Visual Studio Code 사용하기

커리큘럼을 사용하는 가장 좋은 방법은 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste)에서 [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)과 함께 여는 것입니다.

> **Note**: VS Code에서 디렉토리를 클론하고 열면 Python 확장 설치를 자동으로 제안합니다. 위에서 설명한 대로 miniconda도 설치해야 합니다.

> **Note**: VS Code에서 리포지토리를 컨테이너에서 다시 열라는 제안을 받으면, 로컬 Python 설치를 사용하기 위해 이를 거부해야 합니다.

### 브라우저에서 Jupyter 사용하기

브라우저에서 직접 Jupyter 환경을 사용할 수도 있습니다. 사실, 클래식 Jupyter와 Jupyter Hub 모두 자동 완성, 코드 하이라이팅 등으로 꽤 편리한 개발 환경을 제공합니다.

로컬에서 Jupyter를 시작하려면, 과정 디렉토리로 이동한 후 다음을 실행하세요:

```bash
jupyter notebook
```
또는
```bash
jupyterhub
```
그 후, `.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in container. Since our repository contains special `.devcontainer` 폴더로 이동하면 이 리포지토리를 위한 컨테이너를 빌드하는 방법이 안내됩니다. VS Code는 컨테이너에서 코드를 다시 열 것을 제안할 것입니다. 이 경우 Docker 설치가 필요하며, 더 복잡하므로 경험이 많은 사용자에게 추천합니다.

## 클라우드에서 실행하기

로컬에 Python을 설치하고 싶지 않거나 클라우드 리소스에 접근할 수 있다면, 클라우드에서 코드를 실행하는 것이 좋은 대안이 될 수 있습니다. 이를 수행할 수 있는 여러 방법이 있습니다:

* **[GitHub Codespaces](https://github.com/features/codespaces)**를 사용하기. GitHub에서 여러분을 위해 생성된 가상 환경으로, VS Code 브라우저 인터페이스를 통해 접근할 수 있습니다. Codespaces에 접근할 수 있다면, 리포지토리에서 **Code** 버튼을 클릭하고, 코드를 시작하여 금방 실행할 수 있습니다.
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**를 사용하기. [Binder](https://mybinder.org)는 GitHub에서 코드를 테스트할 수 있도록 제공되는 무료 컴퓨팅 리소스입니다. Binder에서 리포지토리를 열 수 있는 버튼이 홈페이지에 있으며, 이 버튼을 클릭하면 Binder 사이트로 빠르게 이동하여 기본 컨테이너를 빌드하고 Jupyter 웹 인터페이스를 원활하게 시작할 수 있습니다.

> **Note**: 오용을 방지하기 위해 Binder는 일부 웹 리소스에 대한 접근을 차단하고 있습니다. 이로 인해 공용 인터넷에서 모델 및/또는 데이터 세트를 가져오는 일부 코드가 작동하지 않을 수 있습니다. 우회 방법을 찾아야 할 수도 있습니다. 또한, Binder에서 제공하는 컴퓨팅 리소스는 기본적이므로, 특히 후반부의 더 복잡한 수업에서는 훈련 속도가 느릴 수 있습니다.

## GPU와 함께 클라우드에서 실행하기

이 커리큘럼의 일부 후반부 수업은 GPU 지원이 큰 도움이 될 것입니다. 그렇지 않으면 훈련 속도가 매우 느려질 것입니다. 특히 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste)나 귀하의 기관을 통해 클라우드에 접근할 수 있다면, 다음과 같은 몇 가지 옵션을 따라할 수 있습니다:

* [데이터 과학 가상 머신](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)을 생성하고 Jupyter를 통해 연결합니다. 그러면 리포지토리를 머신에 바로 클론하고 학습을 시작할 수 있습니다. NC 시리즈 VM은 GPU 지원을 제공합니다.

> **Note**: Azure for Students를 포함한 일부 구독은 기본적으로 GPU 지원을 제공하지 않습니다. 기술 지원 요청을 통해 추가 GPU 코어를 요청해야 할 수도 있습니다.

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)를 생성한 후, 그곳의 Notebook 기능을 사용합니다. [이 비디오](https://azure-for-academics.github.io/quickstart/azureml-papers/)는 Azure ML 노트북에 리포지토리를 클론하고 사용하는 방법을 보여줍니다.

또한 Google Colab을 사용할 수도 있으며, 여기에는 무료 GPU 지원이 제공되며 Jupyter Notebooks를 업로드하여 차례로 실행할 수 있습니다.

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 우리는 책임을 지지 않습니다.