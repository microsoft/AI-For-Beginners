<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-24T09:08:08+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "pt"
}
-->
# Como Executar o Código

Este currículo contém muitos exemplos executáveis e laboratórios que você provavelmente vai querer executar. Para isso, é necessário ter a capacidade de executar código Python em Jupyter Notebooks fornecidos como parte deste currículo. Existem várias opções para executar o código:

## Executar localmente no seu computador

Para executar o código localmente no seu computador, será necessário ter alguma versão do Python instalada. Recomendo pessoalmente instalar o **[miniconda](https://conda.io/en/latest/miniconda.html)** - é uma instalação leve que suporta o gestor de pacotes `conda` para diferentes **ambientes virtuais** Python.

Depois de instalar o miniconda, será necessário clonar o repositório e criar um ambiente virtual para ser usado neste curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usar o Visual Studio Code com a Extensão Python

Provavelmente, a melhor forma de usar o currículo é abri-lo no [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Assim que clonar e abrir o diretório no VS Code, ele sugerirá automaticamente a instalação das extensões Python. Também será necessário instalar o miniconda, conforme descrito acima.

> **Nota**: Se o VS Code sugerir reabrir o repositório num container, deve recusar para usar a instalação local do Python.

### Usar o Jupyter no Navegador

Também pode usar o ambiente Jupyter diretamente no navegador no seu próprio computador. Na verdade, tanto o Jupyter clássico quanto o Jupyter Hub oferecem um ambiente de desenvolvimento bastante conveniente com auto-completação, realce de código, etc.

Para iniciar o Jupyter localmente, vá até o diretório do curso e execute:

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Depois, pode navegar até qualquer um dos ficheiros `.ipynb`, abri-los e começar a trabalhar.

### Executar num container

Uma alternativa à instalação do Python seria executar o código num container. Como o nosso repositório contém uma pasta especial `.devcontainer` que instrui como construir um container para este repositório, o VS Code oferecerá a opção de reabrir o código num container. Isto exigirá a instalação do Docker e será mais complexo, por isso recomendamos esta opção para utilizadores mais experientes.

## Executar na Nuvem

Se não quiser instalar o Python localmente e tiver acesso a alguns recursos na nuvem, uma boa alternativa seria executar o código na nuvem. Existem várias formas de fazer isso:

* Usar o **[GitHub Codespaces](https://github.com/features/codespaces)**, que é um ambiente virtual criado para si no GitHub, acessível através da interface do navegador do VS Code. Se tiver acesso ao Codespaces, basta clicar no botão **Code** no repositório, iniciar um codespace e começar a trabalhar rapidamente.
* Usar o **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. O [Binder](https://mybinder.org) oferece recursos computacionais gratuitos na nuvem para pessoas como você testarem algum código no GitHub. Há um botão na página inicial para abrir o repositório no Binder - isso deve levá-lo rapidamente ao site do Binder, que construirá o container subjacente e iniciará a interface web do Jupyter para si de forma transparente.

> **Nota**: Para evitar uso indevido, o Binder tem acesso a alguns recursos web bloqueados. Isso pode impedir que algum código funcione, especialmente se ele buscar modelos e/ou conjuntos de dados da Internet pública. Pode ser necessário encontrar algumas alternativas. Além disso, os recursos computacionais fornecidos pelo Binder são bastante básicos, então o treino será lento, especialmente nas lições mais complexas.

## Executar na Nuvem com GPU

Algumas das lições mais avançadas deste currículo beneficiariam muito do suporte a GPU, pois, caso contrário, o treino será extremamente lento. Existem algumas opções que pode seguir, especialmente se tiver acesso à nuvem, seja através do [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ou da sua instituição:

* Criar uma [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e conectá-la através do Jupyter. Pode então clonar o repositório diretamente na máquina e começar a aprender. As VMs da série NC têm suporte a GPU.

> **Nota**: Algumas subscrições, incluindo o Azure for Students, não fornecem suporte a GPU por padrão. Pode ser necessário solicitar núcleos de GPU adicionais através de um pedido de suporte técnico.

* Criar um [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e usar a funcionalidade de Notebooks lá. [Este vídeo](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra como clonar um repositório para o notebook do Azure ML e começar a utilizá-lo.

Também pode usar o Google Colab, que oferece algum suporte gratuito a GPU, e carregar os Jupyter Notebooks lá para executá-los um por um.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.