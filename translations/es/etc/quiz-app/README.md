# Cuestionarios

Estos cuestionarios son los cuestionarios previos y posteriores a las lecciones del currículo de IA en https://aka.ms/ai-beginners

## Agregar un conjunto de cuestionarios traducidos

Agrega una traducción de cuestionarios creando estructuras de cuestionarios correspondientes en las carpetas `assets/translations`. Los cuestionarios originales están en `assets/translations/en`. Los cuestionarios están divididos en varios grupos por lección. Asegúrate de alinear la numeración con la sección de cuestionarios adecuada. Hay un total de 40 cuestionarios en este currículo, comenzando desde el número 0.

Después de editar las traducciones, edita el archivo index.js en la carpeta de traducción para importar todos los archivos siguiendo las convenciones en `en`.

Edita el archivo `index.js` en `assets/translations` para importar los nuevos archivos traducidos.

Luego, edita el menú desplegable en `App.vue` en esta aplicación para agregar tu idioma. Haz coincidir la abreviatura localizada con el nombre de la carpeta de tu idioma.

Finalmente, edita todos los enlaces de los cuestionarios en las lecciones traducidas, si existen, para incluir esta localización como un parámetro de consulta: `?loc=fr`, por ejemplo.

## Configuración del proyecto

```
npm install
```

### Compila y recarga automáticamente para desarrollo

```
npm run serve
```

### Compila y minimiza para producción

```
npm run build
```

### Revisa y corrige archivos

```
npm run lint
```

### Personalizar configuración

Consulta [Referencia de Configuración](https://cli.vuejs.org/config/).

Créditos: Gracias a la versión original de esta aplicación de cuestionarios: https://github.com/arpan45/simple-quiz-vue

## Desplegar en Azure

Aquí tienes una guía paso a paso para ayudarte a comenzar:

1. Haz un fork del repositorio de GitHub  
Asegúrate de que el código de tu aplicación web estática esté en tu repositorio de GitHub. Haz un fork de este repositorio.

2. Crea una aplicación web estática en Azure  
- Crea una [cuenta de Azure](http://azure.microsoft.com)  
- Ve al [portal de Azure](https://portal.azure.com)  
- Haz clic en “Crear un recurso” y busca “Aplicación Web Estática”.  
- Haz clic en “Crear”.  

3. Configura la aplicación web estática  
- Básicos: Suscripción: Selecciona tu suscripción de Azure.  
- Grupo de recursos: Crea un nuevo grupo de recursos o utiliza uno existente.  
- Nombre: Proporciona un nombre para tu aplicación web estática.  
- Región: Elige la región más cercana a tus usuarios.  

- #### Detalles de implementación:  
- Fuente: Selecciona “GitHub”.  
- Cuenta de GitHub: Autoriza a Azure para acceder a tu cuenta de GitHub.  
- Organización: Selecciona tu organización de GitHub.  
- Repositorio: Elige el repositorio que contiene tu aplicación web estática.  
- Rama: Selecciona la rama desde la que deseas desplegar.  

- #### Detalles de compilación:  
- Presets de compilación: Elige el framework con el que está construida tu aplicación (por ejemplo, React, Angular, Vue, etc.).  
- Ubicación de la aplicación: Especifica la carpeta que contiene el código de tu aplicación (por ejemplo, / si está en la raíz).  
- Ubicación de la API: Si tienes una API, especifica su ubicación (opcional).  
- Ubicación de salida: Especifica la carpeta donde se genera la salida de la compilación (por ejemplo, build o dist).  

4. Revisa y crea  
Revisa tu configuración y haz clic en “Crear”. Azure configurará los recursos necesarios y creará un archivo de flujo de trabajo de GitHub Actions en tu repositorio.  

5. Flujo de trabajo de GitHub Actions  
Azure creará automáticamente un archivo de flujo de trabajo de GitHub Actions en tu repositorio (.github/workflows/azure-static-web-apps-<nombre>.yml). Este flujo de trabajo manejará el proceso de compilación y despliegue.  

6. Monitorea el despliegue  
Ve a la pestaña “Actions” en tu repositorio de GitHub.  
Deberías ver un flujo de trabajo en ejecución. Este flujo de trabajo compilará y desplegará tu aplicación web estática en Azure.  
Una vez que el flujo de trabajo se complete, tu aplicación estará en vivo en la URL proporcionada por Azure.  

### Ejemplo de archivo de flujo de trabajo

Aquí tienes un ejemplo de cómo podría verse el archivo de flujo de trabajo de GitHub Actions:  
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

### Recursos adicionales  
- [Documentación de Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [Documentación de GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.