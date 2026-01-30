# Como Executar o Código

Este currículo contém muitos exemplos executáveis e laboratórios que você vai querer executar. Para isso, você precisa da capacidade de executar código Python nos Jupyter Notebooks fornecidos como parte deste currículo. Você tem várias opções para executar o código:

## Executar localmente no seu computador

Para executar o código localmente no seu computador, é necessária uma instalação do Python. Uma recomendação é instalar o **[miniconda](https://conda.io/en/latest/miniconda.html)** - é uma instalação bastante leve que suporta o gerenciador de pacotes `conda` para diferentes **ambientes virtuais** Python.

Depois de instalar o miniconda, clone o repositório e crie um ambiente virtual para ser usado neste curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usando Visual Studio Code com Extensão Python

Este currículo é melhor utilizado ao abri-lo no [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Após clonar e abrir o diretório no VS Code, ele automaticamente sugerirá a instalação das extensões Python. Você também precisará instalar o miniconda conforme descrito acima.

> **Nota**: Se o VS Code sugerir reabrir o repositório em um contêiner, você deve recusar para usar a instalação local do Python.

### Usando Jupyter no Navegador

Você também pode usar um ambiente Jupyter pelo navegador em seu próprio computador. Tanto o Jupyter clássico quanto o JupyterHub fornecem um ambiente de desenvolvimento conveniente com auto-completar, realce de código, etc.

Para iniciar o Jupyter localmente, vá para o diretório do curso e execute:

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Depois você pode navegar para qualquer arquivo `.ipynb`, abri-lo e começar a trabalhar.

### Executando em contêiner

Uma alternativa à instalação do Python seria executar o código em um contêiner. Como nosso repositório fornece uma pasta especial `.devcontainer` que instrui como construir um contêiner para este repositório, o VS Code oferece a oportunidade de reabrir o código em um contêiner. Isso requer a instalação do Docker, e também seria mais complexo, então recomendamos isso para usuários mais experientes.

## Executando na Nuvem

Se você não quiser instalar o Python localmente e tiver acesso a alguns recursos na nuvem - uma boa alternativa seria executar o código na nuvem. Existem várias formas de fazer isso:

* Usando **[GitHub Codespaces](https://github.com/features/codespaces)**, que é um ambiente virtual criado para você no GitHub, acessível através da interface do navegador do VS Code. Se você tem acesso ao Codespaces, basta clicar no botão **Code** no repositório, iniciar um codespace e começar a trabalhar rapidamente.
* Usando **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) oferece recursos computacionais gratuitos na nuvem para pessoas como você testarem algum código no GitHub. Há um botão na página principal para abrir o repositório no Binder - isso deve levá-lo rapidamente ao site do binder, que construirá um contêiner subjacente e iniciará uma interface web Jupyter para você de forma transparente.

> **Nota**: Para evitar uso indevido, o Binder tem acesso a alguns recursos web bloqueado. Isso pode impedir o funcionamento de algum código que busca modelos e/ou conjuntos de dados na internet pública. Você pode precisar encontrar algumas soluções alternativas. Além disso, os recursos computacionais oferecidos pelo Binder são bastante básicos, então o treinamento será lento, especialmente em aulas mais complexas.

## Executando na Nuvem com GPU

Algumas das aulas posteriores deste currículo se beneficiariam muito do suporte a GPU. O treinamento de modelos, por exemplo, pode ser dolorosamente lento sem isso. Existem algumas opções que você pode seguir, especialmente se tiver acesso à nuvem pela [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ou pela sua instituição:

* Crie uma [Máquina Virtual de Ciência de Dados](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e conecte-se a ela via Jupyter. Você pode então clonar o repositório diretamente na máquina e começar a aprender. VMs da série NC têm suporte a GPU.

> **Nota**: Algumas assinaturas, incluindo Azure for Students, não oferecem suporte a GPU por padrão. Você pode precisar solicitar núcleos GPU adicionais por meio de um pedido de suporte técnico.

* Crie um [Workspace do Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e use o recurso Notebook nele. [Este vídeo](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra como clonar um repositório dentro do notebook Azure ML e começar a usar.

Você também pode usar o Google Colab, que oferece algum suporte gratuito a GPU, e fazer upload dos Jupyter Notebooks para executá-los um por um.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomendamos a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->