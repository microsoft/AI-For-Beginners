# Guia de Solução de Problemas do AI-For-Beginners

Este guia ajuda você a resolver problemas comuns encontrados ao usar ou contribuir para o repositório [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners). Cada problema inclui contexto, sintomas, explicações e soluções passo a passo.

---

## Índice

- [Problemas Gerais](../..)
- [Problemas de Instalação](../..)
- [Problemas de Configuração](../..)
- [Execução de Notebooks](../..)
- [Problemas de Desempenho](../..)
- [Problemas no Site do Livro Didático](../..)
- [Problemas de Contribuição](../..)
- [FAQ](../..)
- [Obtendo Ajuda](../..)

---

## Problemas Gerais

### 1. Repositório Não Clona Corretamente

**Contexto:** Clonar permite copiar o repositório para sua máquina.

**Sintomas:**
- Erro: `fatal: repository not found`
- Erro: `Permission denied (publickey)`

**Possíveis Causas:**
- URL do repositório incorreta
- Permissões insuficientes
- Chaves SSH não configuradas

**Soluções:**
1. **Verifique a URL do repositório.**  
   Use a URL HTTPS:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Troque para HTTPS se o SSH falhar.**  
   Se você vir `Permission denied (publickey)`, use o link HTTPS acima em vez de SSH.
3. **Configure chaves SSH (opcional).**  
   Se quiser usar SSH, siga o [guia de SSH do GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Problemas de Instalação

### 2. Problemas com o Ambiente Python

**Contexto:** O repositório depende do Python e de várias bibliotecas.

**Sintomas:**
- Erro: `ModuleNotFoundError: No module named '<package>'`
- Erros de importação ao executar scripts ou notebooks

**Possíveis Causas:**
- Dependências não instaladas
- Versão errada do Python

**Soluções:**
1. **Configure um ambiente virtual.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Instale as dependências.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Verifique a versão do Python.**  
   Use Python 3.7 ou mais recente.  
   ```bash
   python --version
   ```

### 3. Jupyter Não Instalado

**Contexto:** Notebooks são um recurso essencial de aprendizado.

**Sintomas:**
- Erro: `jupyter: command not found`
- Notebooks não iniciam

**Possíveis Causas:**
- Jupyter não instalado

**Soluções:**
1. **Instale o Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   ou, se estiver usando Anaconda:
   ```bash
   conda install notebook
   ```
2. **Inicie o Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Conflitos de Versão de Dependências

**Contexto:** Projetos podem falhar se as versões dos pacotes forem incompatíveis.

**Sintomas:**
- Erros ou avisos sobre versões incompatíveis

**Possíveis Causas:**
- Pacotes Python antigos ou conflitantes

**Soluções:**
1. **Instale em um ambiente limpo.**  
   Exclua o venv/env do conda antigo e crie um novo.
2. **Use versões exatas.**  
   Sempre execute:  
   ```bash
   pip install -r requirements.txt
   ```
   Se isso falhar, instale manualmente os pacotes ausentes conforme descrito no README.

---

## Problemas de Configuração

### 5. Variáveis de Ambiente Não Configuradas

**Contexto:** Alguns módulos podem exigir chaves, tokens ou configurações.

**Sintomas:**
- Erro: `KeyError` ou avisos sobre configurações ausentes

**Possíveis Causas:**
- Variáveis de ambiente necessárias não configuradas

**Soluções:**
1. **Verifique arquivos como `.env.example` ou similares.**
2. **Crie um arquivo `.env` e preencha os valores necessários.**
3. **Recarregue seu terminal ou IDE após configurar as variáveis de ambiente.**

---

## Execução de Notebooks

### 6. Notebook Não Abre ou Não Executa

**Contexto:** Notebooks Jupyter precisam de configuração adequada.

**Sintomas:**
- Notebook não inicia
- Navegador não abre automaticamente

**Possíveis Causas:**
- Jupyter não instalado
- Problemas de configuração do navegador

**Soluções:**
1. **Instale o Jupyter (veja Problemas de Instalação acima).**
2. **Abra os notebooks manualmente.**
   - Copie a URL do terminal (ex.: `http://localhost:8888/?token=...`) e cole no navegador.

### 7. Kernel Travando ou Congelando

**Contexto:** Kernels de notebooks podem travar devido a limites de recursos ou erros de código.

**Sintomas:**
- Kernel morre ou reinicia repetidamente
- Erros de falta de memória

**Possíveis Causas:**
- Conjuntos de dados grandes
- Código ou pacotes incompatíveis

**Soluções:**
1. **Reinicie o kernel.**  
   Use o botão "Restart Kernel" no Jupyter.
2. **Verifique o uso de memória.**  
   Feche aplicativos não utilizados.
3. **Execute notebooks em plataformas na nuvem.**  
   Use [Google Colab](https://colab.research.google.com/) ou [Azure Notebooks](https://notebooks.azure.com/).

---

## Problemas de Desempenho

### 8. Notebooks Executando Lentamente

**Contexto:** Algumas tarefas de IA exigem muita memória e CPU.

**Sintomas:**
- Execução lenta
- Ventoinha do laptop funcionando intensamente

**Possíveis Causas:**
- Conjuntos de dados ou modelos grandes
- Recursos limitados do sistema

**Soluções:**
1. **Use uma plataforma na nuvem.**
   - Faça upload do notebook para Colab ou Azure Notebooks.
2. **Reduza o tamanho do conjunto de dados.**
   - Use dados de amostra para prática.
3. **Feche programas desnecessários.**
   - Libere RAM do sistema.

---

## Problemas no Site do Livro Didático

### 9. Capítulo Não Carrega

**Contexto:** O livro didático online exibe lições e capítulos.

**Sintomas:**
- Um capítulo (ex.: Transformers/BERT) está ausente ou não abre

**Problema Conhecido:**  
- [Issue #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. não pode ser aberto no site do livro didático.” Causado por um erro no nome do arquivo (`READMEtransformers.md` em vez de `README.md`).

**Soluções:**
1. **Verifique erros de renomeação de arquivos.**  
   Se você for um colaborador, certifique-se de que os arquivos dos capítulos estejam nomeados como `README.md`.
2. **Relate arquivos ausentes.**  
   Abra um problema no GitHub com o nome do capítulo e detalhes do erro.

---

## Problemas de Contribuição

### 10. PR Não Aceito ou Builds Falhando

**Contexto:** Contribuições devem passar por testes e seguir diretrizes.

**Sintomas:**
- Pull request rejeitado
- Erros na pipeline de CI/CD

**Possíveis Causas:**
- Testes falhando
- Não seguir padrões de codificação

**Soluções:**
1. **Leia as diretrizes de contribuição.**
   - Siga o [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) do repositório.
2. **Execute testes localmente antes de enviar.**
3. **Verifique regras de linting ou requisitos de formatação.**

---

## FAQ

### Onde posso encontrar ajuda para módulos específicos?
- Cada módulo geralmente tem seu próprio README. Comece por lá para dicas de configuração e uso.

### Como posso relatar um bug ou solicitar um recurso?
- [Abra um problema no GitHub](https://github.com/microsoft/AI-For-Beginners/issues/new) com uma descrição clara e etapas para reproduzir.

### Posso pedir ajuda se meu problema não estiver listado?
- Sim! Pesquise problemas existentes primeiro e, se não encontrar seu problema, crie um novo.

---

## Obtendo Ajuda

- **Verifique Problemas:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Faça Perguntas:** Use as Discussões do GitHub ou abra um problema.
- **Comunidade:** Veja os links do repositório para opções de chat/fórum.

---

_Última Atualização: 20/09/2025_

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante estar ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.