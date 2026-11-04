# Como Executar o Código

Este currículo contém muitos exemplos executáveis e laboratórios que você vai querer rodar. Para isso, você precisa da capacidade de executar código Python em Jupyter Notebooks fornecidos como parte deste currículo. Você tem várias opções para executar o código:

## Executar localmente no seu computador

Para executar o código localmente no seu computador, é necessária uma instalação do Python. Uma recomendação é instalar o **[miniconda](https://conda.io/en/latest/miniconda.html)** - é uma instalação bastante leve que suporta o gerenciador de pacotes `conda` para diferentes **ambientes virtuais** Python.

Depois de instalar o miniconda, clone o repositório e crie um ambiente virtual a ser usado para este curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Nota para Windows**: Se a criação do ambiente falhar ao instalar `gdk-pixbuf` com um `UnicodeDecodeError` que menciona o codec `gbk`, habilite o modo UTF-8 do Python no seu terminal e tente novamente. Use a sintaxe para o terminal que você está utilizando:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Prompt de Comando (`cmd.exe`) ou Prompt Anaconda:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, incluindo Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Se uma tentativa falhada deixou o ambiente `ai4beg` para trás, desative-o e remova esse ambiente antes de tentar novamente. Use `conda deactivate` primeiro quando um ambiente estiver ativo:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Usando Visual Studio Code com a Extensão Python

Este currículo é melhor utilizado ao abrir no [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Assim que você clonar e abrir o diretório no VS Code, ele sugerirá automaticamente que você instale extensões Python. Você também precisará instalar o miniconda conforme descrito acima.

> **Nota**: Se o VS Code sugerir que você reabra o repositório em um container, você deve recusar isso para usar a instalação local do Python.

### Usando Jupyter no Navegador

Você também pode usar um ambiente Jupyter no navegador no seu próprio computador. Tanto o Jupyter clássico quanto o JupyterHub oferecem um ambiente de desenvolvimento conveniente com auto-completar, realce de código, etc.

Para iniciar o Jupyter localmente, vá para o diretório do curso e execute:

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Você então pode navegar até qualquer um dos arquivos `.ipynb`, abri-los e começar a trabalhar.

### Executando em container

Uma alternativa à instalação do Python seria executar o código em um container. Como nosso repositório fornece uma pasta `.devcontainer` especial que instrui como construir um container para este repo, o VS Code oferece a oportunidade de reabrir o código em um container. Isso exigirá a instalação do Docker e também seria mais complexo, portanto recomendamos essa opção para usuários mais experientes.

## Executando na Nuvem

Se você não quiser instalar o Python localmente, e tiver acesso a alguns recursos de nuvem - uma boa alternativa seria executar o código na nuvem. Existem várias formas de fazer isso:

* Usando **[GitHub Codespaces](https://github.com/features/codespaces)**, que é um ambiente virtual criado para você no GitHub, acessível através de uma interface do navegador do VS Code. Se você tiver acesso ao Codespaces, basta clicar no botão **Code** no repositório, iniciar um codespace e começar a rodar em pouco tempo.
* Usando **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) oferece recursos computacionais gratuitos fornecidos na nuvem para pessoas como você testarem código no GitHub. Há um botão na página inicial para abrir o repositório no Binder - isso deve levá-lo rapidamente ao site do binder, que construirá um container subjacente e iniciará uma interface web do Jupyter para você de forma transparente.

> **Nota**: Para evitar uso indevido, o Binder tem acesso bloqueado a alguns recursos web. Isso pode impedir que parte do código funcione, especialmente código que busca modelos e/ou conjuntos de dados na Internet pública. Você pode precisar encontrar algumas soluções alternativas. Além disso, os recursos computacionais fornecidos pelo Binder são bastante básicos, então o treinamento será lento, especialmente nas lições mais avançadas e complexas.

## Executando na Nuvem com GPU

Algumas das lições finais deste currículo se beneficiariam bastante do suporte a GPU. O treinamento de modelos, por exemplo, pode ser dolorosamente lento caso contrário. Existem algumas opções que você pode seguir, especialmente se tiver acesso à nuvem através do [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), ou através da sua instituição:

* Crie uma [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e conecte-se a ela através do Jupyter. Você pode então clonar o repositório diretamente na máquina e começar a aprender. VMs da série NC têm suporte a GPU.

> **Nota**: Algumas assinaturas, incluindo Azure for Students, não fornecem suporte a GPU por padrão. Você pode precisar solicitar cores adicionais de GPU com um pedido de suporte técnico.

* Crie um [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e então use o recurso de Notebook lá. [Este vídeo](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra como clonar um repositório em um notebook do Azure ML e começar a usá-lo.

Você também pode usar o Google Colab, que já vem com algum suporte gratuito a GPU, e carregar os Jupyter Notebooks lá para executá-los um a um.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->