# Como Executar o Código

Este currículo contém muitos exemplos executáveis e laboratórios que vai querer executar. Para tal, é necessário ter a capacidade de executar código Python nos Jupyter Notebooks fornecidos como parte deste currículo. Tem várias opções para executar o código:

## Executar localmente no seu computador

Para executar o código localmente no seu computador, é necessária uma instalação de Python. Uma recomendação é instalar o **[miniconda](https://conda.io/en/latest/miniconda.html)** — é uma instalação relativamente leve que suporta o gestor de pacotes `conda` para diferentes **ambientes virtuais** de Python.

Depois de instalar o miniconda, clone o repositório e crie um ambiente virtual para usar neste curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Nota para Windows**: Se a criação do ambiente falhar ao instalar `gdk-pixbuf` com um `UnicodeDecodeError` que menciona o codec `gbk`, ative o modo UTF-8 do Python no seu terminal e tente novamente. Use a sintaxe para o terminal que está a utilizar:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Prompt de Comando (`cmd.exe`) ou Anaconda Prompt:**
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
> Se uma tentativa falhada deixou o ambiente `ai4beg` ativo, desative-o e remova esse ambiente antes de tentar novamente. Use `conda deactivate` primeiro quando um ambiente estiver ativo:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Usar o Visual Studio Code com a Extensão Python

Este currículo é melhor utilizado ao ser aberto no [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Assim que clonar e abrir a diretoria no VS Code, será sugerido automaticamente que instale as extensões de Python. Também terá de instalar o miniconda, conforme descrito acima.

> **Nota**: Se o VS Code lhe sugerir reabrir o repositório numa container, deve recusar para usar a instalação local do Python.

### Usar Jupyter no Navegador

Pode também usar um ambiente Jupyter a partir do navegador no seu próprio computador. Tanto o Jupyter clássico como o JupyterHub fornecem um ambiente de desenvolvimento conveniente com auto-completar, realce de código, etc.

Para iniciar o Jupyter localmente, vá para a diretoria do curso e execute:

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Pode depois navegar até a qualquer um dos ficheiros `.ipynb`, abri-los e começar a trabalhar.

### Executar numa container

Uma alternativa à instalação de Python seria executar o código numa container. Como o nosso repositório fornece uma pasta `.devcontainer` especial que indica como construir uma container para este repositório, o VS Code oferece a oportunidade de reabrir o código numa container. Isto requer a instalação do Docker e seria mais complexo, pelo que recomendamos isto a utilizadores mais experientes.

## Executar na Cloud

Se não quiser instalar o Python localmente e tiver acesso a alguns recursos cloud, uma boa alternativa seria executar o código na cloud. Existem várias formas de fazer isto:

* Usar **[GitHub Codespaces](https://github.com/features/codespaces)**, que é um ambiente virtual criado para si no GitHub, acessível através da interface do navegador do VS Code. Se tiver acesso ao Codespaces, pode simplesmente clicar no botão **Code** no repositório, iniciar um codespace e começar a funcionar num instante.
* Usar **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. O [Binder](https://mybinder.org) oferece recursos computacionais gratuitos na cloud para pessoas como você testarem código no GitHub. Existe um botão na página inicial para abrir o repositório no Binder — isto deverá levá-lo rapidamente para o site do Binder, que irá construir uma container subjacente e iniciar uma interface web do Jupyter para si, de forma fluída.

> **Nota**: Para prevenir abusos, o Binder tem acesso a alguns recursos web bloqueados. Isto pode impedir que algum código funcione, especialmente aquele que obtém modelos e/ou conjuntos de dados da internet pública. Pode ser necessário encontrar algumas soluções alternativas. Além disso, os recursos computacionais fornecidos pelo Binder são básicos, pelo que o treino será lento, especialmente em lições posteriores, mais complexas.

## Executar na Cloud com GPU

Algumas das lições mais avançadas deste currículo beneficiariam muito do suporte a GPU. O treino de modelos, por exemplo, pode ser dolorosamente lento de outra forma. Existem algumas opções que pode seguir, especialmente se tiver acesso à cloud através do [Azure para Estudantes](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ou através da sua instituição:

* Criar [Máquina Virtual de Ciência de Dados](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e ligar-se a ela via Jupyter. Pode clonar o repositório diretamente na máquina e começar a aprender. As VMs da série NC têm suporte a GPU.

> **Nota**: Algumas subscrições, incluindo o Azure para Estudantes, não fornecem suporte a GPU automaticamente. Pode precisar de pedir núcleos de GPU adicionais com um pedido ao suporte técnico.

* Criar um [Workspace Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e depois usar a funcionalidade de Notebooks aí. [Este vídeo](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra como clonar um repositório dentro do notebook Azure ML e começar a usá-lo.

Pode também usar o Google Colab, que oferece algum suporte gratuito a GPU, e carregar lá os Jupyter Notebooks para executá-los um a um.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->