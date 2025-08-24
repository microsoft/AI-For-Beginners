<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-24T21:37:43+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "ko"
}
-->
# 코드 실행 방법

이 커리큘럼에는 실행 가능한 예제와 실습이 많이 포함되어 있으며, 이를 실행해 보고 싶을 것입니다. 이를 위해서는 이 커리큘럼의 일부로 제공된 Jupyter Notebook에서 Python 코드를 실행할 수 있는 환경이 필요합니다. 코드를 실행하는 방법에는 여러 가지가 있습니다:

## 로컬 컴퓨터에서 실행

코드를 로컬 컴퓨터에서 실행하려면 Python의 어떤 버전이든 설치되어 있어야 합니다. 개인적으로는 **[miniconda](https://conda.io/en/latest/miniconda.html)**를 설치하는 것을 추천합니다. 이는 가벼운 설치 방식으로, 다양한 Python **가상 환경**을 지원하는 `conda` 패키지 관리자를 제공합니다.

miniconda를 설치한 후, 저장소를 클론하고 이 강좌에서 사용할 가상 환경을 생성해야 합니다:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Python 확장이 포함된 Visual Studio Code 사용

이 커리큘럼을 사용하는 가장 좋은 방법은 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste)와 [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)을 사용하여 여는 것입니다.

> **Note**: 저장소를 클론하고 VS Code에서 디렉토리를 열면, Python 확장을 설치하라는 제안이 자동으로 표시됩니다. 위에서 설명한 대로 miniconda도 설치해야 합니다.

> **Note**: VS Code가 저장소를 컨테이너에서 다시 열 것을 제안하면, 로컬 Python 설치를 사용하기 위해 이를 거부해야 합니다.

### 브라우저에서 Jupyter 사용

브라우저에서 바로 Jupyter 환경을 사용할 수도 있습니다. 실제로, 클래식 Jupyter와 Jupyter Hub는 자동 완성, 코드 하이라이팅 등 편리한 개발 환경을 제공합니다.

로컬에서 Jupyter를 시작하려면, 강좌 디렉토리로 이동하여 다음 명령을 실행하세요:

```bash
jupyter notebook
```  
또는  
```bash
jupyterhub
```  
그런 다음 `.ipynb` 파일 중 하나로 이동하여 열고 작업을 시작할 수 있습니다.

### 컨테이너에서 실행

Python을 설치하는 대신 컨테이너에서 코드를 실행하는 방법도 있습니다. 저장소에는 이 저장소를 위한 컨테이너를 빌드하는 방법을 지시하는 `.devcontainer` 폴더가 포함되어 있으므로, VS Code는 코드를 컨테이너에서 다시 열 것을 제안할 것입니다. 이를 위해 Docker 설치가 필요하며, 다소 복잡할 수 있으므로 더 숙련된 사용자에게 추천합니다.

## 클라우드에서 실행

Python을 로컬에 설치하고 싶지 않거나 클라우드 리소스에 접근할 수 있다면, 클라우드에서 코드를 실행하는 것도 좋은 대안입니다. 이를 실행하는 몇 가지 방법이 있습니다:

* **[GitHub Codespaces](https://github.com/features/codespaces)**를 사용하는 방법. 이는 GitHub에서 제공하는 가상 환경으로, VS Code 브라우저 인터페이스를 통해 접근할 수 있습니다. Codespaces에 접근할 수 있다면, 저장소의 **Code** 버튼을 클릭하고 Codespace를 시작하면 바로 실행할 수 있습니다.
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**를 사용하는 방법. [Binder](https://mybinder.org)는 GitHub에서 코드를 테스트하려는 사람들을 위해 제공되는 무료 클라우드 컴퓨팅 리소스입니다. 저장소의 첫 페이지에 Binder에서 저장소를 열 수 있는 버튼이 있으며, 이를 클릭하면 Binder 사이트로 이동하여 기본 컨테이너를 빌드하고 Jupyter 웹 인터페이스를 원활하게 시작할 수 있습니다.

> **Note**: 오용을 방지하기 위해 Binder는 일부 웹 리소스에 대한 접근을 차단합니다. 이는 모델이나 데이터를 공용 인터넷에서 가져오는 코드를 실행할 때 문제가 될 수 있습니다. 해결 방법을 찾아야 할 수도 있습니다. 또한, Binder에서 제공되는 컴퓨팅 리소스는 기본적이므로, 특히 더 복잡한 후반부 강의에서는 학습 속도가 느릴 수 있습니다.

## GPU를 활용한 클라우드 실행

이 커리큘럼의 후반부 강의 중 일부는 GPU 지원이 있으면 훨씬 더 효율적입니다. 그렇지 않으면 학습 속도가 매우 느릴 수 있습니다. 클라우드에 접근할 수 있는 경우, 특히 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste)나 기관을 통해 접근할 수 있다면, 다음 옵션을 고려할 수 있습니다:

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)을 생성하고 Jupyter를 통해 연결합니다. 그런 다음, 해당 머신에 저장소를 클론하고 학습을 시작할 수 있습니다. NC 시리즈 VM은 GPU를 지원합니다.

> **Note**: Azure for Students를 포함한 일부 구독은 기본적으로 GPU 지원을 제공하지 않습니다. 추가 GPU 코어를 요청하려면 기술 지원 요청이 필요할 수 있습니다.

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)를 생성한 후, Notebook 기능을 사용합니다. [이 비디오](https://azure-for-academics.github.io/quickstart/azureml-papers/)는 Azure ML 노트북에 저장소를 클론하고 사용하는 방법을 보여줍니다.

Google Colab도 사용할 수 있으며, 일부 무료 GPU 지원을 제공합니다. Jupyter Notebook을 업로드하여 하나씩 실행할 수 있습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.