# Questionários

Estes questionários são os questionários pré e pós-aula do currículo de IA em https://aka.ms/ai-beginners

## Adicionando um conjunto de questionários traduzidos

Adicione uma tradução de questionário criando estruturas de questionário correspondentes nas pastas `assets/translations`. Os questionários canônicos estão em `assets/translations/en`. Os questionários estão divididos em vários grupos por lição. Certifique-se de alinhar a numeração com a seção de questionário apropriada. Há um total de 40 questionários neste currículo, com a contagem começando em 0.

Após editar as traduções, edite o arquivo index.js na pasta de tradução para importar todos os arquivos seguindo as convenções em `en`.

Edite o arquivo `index.js` em `assets/translations` para importar os novos arquivos traduzidos.

Em seguida, edite o dropdown em `App.vue` neste aplicativo para adicionar seu idioma. Combine a abreviação localizada com o nome da pasta para o seu idioma.

Finalmente, edite todos os links dos questionários nas lições traduzidas, se existirem, para incluir esta localização como um parâmetro de consulta: `?loc=fr`, por exemplo.

## Configuração do projeto

```
npm install
```

### Compila e recarrega automaticamente para desenvolvimento

```
npm run serve
```

### Compila e minifica para produção

```
npm run build
```

### Lint e corrige arquivos

```
npm run lint
```

### Personalizar configuração

Veja [Referência de Configuração](https://cli.vuejs.org/config/).

Créditos: Agradecimentos à versão original deste aplicativo de questionário: https://github.com/arpan45/simple-quiz-vue

## Implantando no Azure

Aqui está um guia passo a passo para ajudá-lo a começar:

1. Faça um fork de um repositório GitHub
Certifique-se de que o código do seu aplicativo web estático está no seu repositório GitHub. Faça um fork deste repositório.

2. Crie um Azure Static Web App
- Crie uma [conta Azure](http://azure.microsoft.com)
- Vá para o [portal do Azure](https://portal.azure.com) 
- Clique em “Criar um recurso” e pesquise por “Static Web App”.
- Clique em “Criar”.

3. Configure o Static Web App
- Básicos: Assinatura: Selecione sua assinatura do Azure.
- Grupo de Recursos: Crie um novo grupo de recursos ou use um existente.
- Nome: Forneça um nome para seu aplicativo web estático.
- Região: Escolha a região mais próxima dos seus usuários.

- #### Detalhes da Implantação:
- Fonte: Selecione “GitHub”.
- Conta GitHub: Autorize o Azure a acessar sua conta GitHub.
- Organização: Selecione sua organização GitHub.
- Repositório: Escolha o repositório que contém seu aplicativo web estático.
- Branch: Selecione o branch do qual você deseja implantar.

- #### Detalhes da Compilação:
- Presets de Compilação: Escolha o framework com o qual seu aplicativo foi construído (por exemplo, React, Angular, Vue, etc.).
- Localização do App: Especifique a pasta que contém o código do seu aplicativo (por exemplo, / se estiver na raiz).
- Localização da API: Se você tiver uma API, especifique sua localização (opcional).
- Localização de Saída: Especifique a pasta onde a saída da compilação é gerada (por exemplo, build ou dist).

4. Revise e Crie
Revise suas configurações e clique em “Criar”. O Azure configurará os recursos necessários e criará um fluxo de trabalho do GitHub Actions em seu repositório.

5. Fluxo de Trabalho do GitHub Actions
O Azure criará automaticamente um arquivo de fluxo de trabalho do GitHub Actions em seu repositório (.github/workflows/azure-static-web-apps-<name>.yml). Este fluxo de trabalho gerenciará o processo de compilação e implantação.

6. Monitore a Implantação
Vá para a aba “Ações” em seu repositório GitHub.
Você deve ver um fluxo de trabalho em execução. Este fluxo de trabalho irá compilar e implantar seu aplicativo web estático no Azure.
Uma vez que o fluxo de trabalho seja concluído, seu aplicativo estará ativo na URL do Azure fornecida.

### Exemplo de Arquivo de Fluxo de Trabalho

Aqui está um exemplo de como o arquivo de fluxo de trabalho do GitHub Actions pode parecer:
name: Azure Static Web Apps CI/CD
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "etc/quiz-app # App source code path"
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```

### Recursos Adicionais
- [Documentação do Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [Documentação do GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

**Isenção de responsabilidade**:  
Este documento foi traduzido usando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.