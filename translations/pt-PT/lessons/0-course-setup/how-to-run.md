# Como Executar o Código

Este currículo contém muitos exemplos executáveis e laboratórios que você vai querer executar. Para isso, precisa da capacidade de executar código Python nos Jupyter Notebooks fornecidos como parte deste currículo. Tem várias opções para executar o código:

## Executar localmente no seu computador

Para executar o código localmente no seu computador, é necessário uma instalação de Python. Uma recomendação é instalar o **[miniconda](https://conda.io/en/latest/miniconda.html)** - é uma instalação relativamente leve que suporta o gestor de pacotes `conda` para diferentes **ambientes virtuais** Python.

Depois de instalar o miniconda, clone o repositório e crie um ambiente virtual a ser usado para este curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usar Visual Studio Code com a Extensão Python

Este currículo é melhor aproveitado quando aberto no [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Depois de clonar e abrir o diretório no VS Code, será sugerido automaticamente que instale extensões Python. Também terá de instalar o miniconda conforme descrito acima.

> **Nota**: Se o VS Code lhe sugerir reabrir o repositório num contentor, deve recusar para usar a instalação local do Python.

### Usar Jupyter no Navegador

Também pode usar um ambiente Jupyter a partir do navegador no seu próprio computador. Tanto o Jupyter clássico como o JupyterHub oferecem um ambiente de desenvolvimento conveniente com auto-completação, realce de código, etc.

Para iniciar o Jupyter localmente, vá para o diretório do curso e execute:

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Pode então navegar para qualquer um dos ficheiros `.ipynb`, abrir e começar a trabalhar.

### Executar em contentor

Uma alternativa à instalação do Python seria executar o código num contentor. Como o nosso repositório fornece uma pasta especial `.devcontainer` que indica como construir um contentor para este repositório, o VS Code oferece a oportunidade de reabrir o código num contentor. Isto irá requerer a instalação do Docker, e também será mais complexo, pelo que recomendamos isto para utilizadores mais experientes.

## Executar na Cloud

Se não pretende instalar Python localmente, e tem acesso a alguns recursos na cloud - uma boa alternativa seria executar o código na cloud. Existem várias formas de o fazer:

* Usar **[GitHub Codespaces](https://github.com/features/codespaces)**, que é um ambiente virtual criado para si no GitHub, acessível através de uma interface de navegador VS Code. Se tem acesso ao Codespaces, pode simplesmente clicar no botão **Code** no repositório, iniciar um codespace, e começar a correr em pouco tempo.
* Usar **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) oferece recursos computacionais gratuitos providenciados na cloud para pessoas como você testarem algum código no GitHub. Existe um botão na página inicial para abrir o repositório no Binder – isto deve levá-lo rapidamente ao site binder, que vai construir um contentor subjacente e iniciar uma interface web Jupyter para si de forma integrada.

> **Nota**: Para prevenir uso indevido, o Binder tem acesso a alguns recursos web bloqueados. Isto pode impedir que algum código funcione, especialmente o que descarrega modelos e/ou conjuntos de dados da Internet pública. Pode precisar de encontrar algumas soluções alternativas. Além disso, os recursos computacionais providenciados pelo Binder são bastante básicos, pelo que o treino será lento, especialmente nas lições mais avançadas e complexas.

## Executar na Cloud com GPU

Algumas das lições mais avançadas deste currículo beneficiariam muito do suporte a GPU. O treino de modelos, por exemplo, pode ser extremamente lento de outra forma. Existem algumas opções que pode seguir, especialmente se tiver acesso à cloud através do [Azure para Estudantes](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ou da sua instituição:

* Criar [Máquina Virtual para Ciência de Dados](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e ligar-se a ela através do Jupyter. Pode então clonar o repositório diretamente na máquina e começar a aprender. As máquinas virtuais NC-series têm suporte a GPU.

> **Nota**: Algumas subscrições, incluindo o Azure para Estudantes, não fornecem suporte a GPU por defeito. Pode precisar de pedir núcleos de GPU adicionais através de um pedido de suporte técnico.

* Criar um [Workspace Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e depois usar a funcionalidade Notebook aí. [Este vídeo](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra como clonar um repositório num notebook Azure ML e começar a usar.

Também pode usar o Google Colab, que vem com algum suporte GPU gratuito, e carregar Jupyter Notebooks lá para executá-los um a um.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->