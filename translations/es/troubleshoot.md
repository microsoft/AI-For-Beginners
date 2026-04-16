# Guía de Solución de Problemas para AI-For-Beginners

Esta guía te ayuda a resolver problemas comunes al usar o contribuir al repositorio [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners). Cada problema incluye antecedentes, síntomas, explicaciones y soluciones paso a paso.

---

## Tabla de Contenidos

- [Problemas Generales](../..)
- [Problemas de Instalación](../..)
- [Problemas de Configuración](../..)
- [Ejecutar Notebooks](../..)
- [Problemas de Rendimiento](../..)
- [Problemas del Sitio Web del Libro](../..)
- [Problemas al Contribuir](../..)
- [Preguntas Frecuentes](../..)
- [Obtener Ayuda](../..)

---

## Problemas Generales

### 1. El repositorio no se clona correctamente

**Antecedentes:** Clonar permite copiar el repositorio a tu máquina.

**Síntomas:**
- Error: `fatal: repository not found`
- Error: `Permission denied (publickey)`

**Posibles Causas:**
- URL del repositorio incorrecta
- Permisos insuficientes
- Claves SSH no configuradas

**Soluciones:**
1. **Verifica la URL del repositorio.**  
   Usa la URL HTTPS:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Cambia a HTTPS si falla SSH.**  
   Si ves `Permission denied (publickey)`, usa el enlace HTTPS mencionado en lugar de SSH.
3. **Configura claves SSH (opcional).**  
   Si prefieres usar SSH, sigue la [guía de SSH de GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Problemas de Instalación

### 2. Problemas con el entorno de Python

**Antecedentes:** El repositorio depende de Python y varias bibliotecas.

**Síntomas:**
- Error: `ModuleNotFoundError: No module named '<package>'`
- Errores de importación al ejecutar scripts o notebooks

**Posibles Causas:**
- Dependencias no instaladas
- Versión incorrecta de Python

**Soluciones:**
1. **Configura un entorno virtual.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Instala las dependencias.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Verifica la versión de Python.**  
   Usa Python 3.7 o más reciente.  
   ```bash
   python --version
   ```

### 3. Jupyter no está instalado

**Antecedentes:** Los notebooks son un recurso clave de aprendizaje.

**Síntomas:**
- Error: `jupyter: command not found`
- Los notebooks no se abren

**Posibles Causas:**
- Jupyter no está instalado

**Soluciones:**
1. **Instala Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   o, si usas Anaconda:
   ```bash
   conda install notebook
   ```
2. **Inicia Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Conflictos de versiones de dependencias

**Antecedentes:** Los proyectos pueden fallar si las versiones de los paquetes no coinciden.

**Síntomas:**
- Errores o advertencias sobre versiones incompatibles

**Posibles Causas:**
- Paquetes de Python antiguos o en conflicto

**Soluciones:**
1. **Instala en un entorno limpio.**  
   Elimina el entorno venv/conda antiguo y crea uno nuevo.
2. **Usa versiones exactas.**  
   Siempre ejecuta:
   ```bash
   pip install -r requirements.txt
   ```
   Si esto falla, instala manualmente los paquetes faltantes como se describe en el README.

---

## Problemas de Configuración

### 5. Variables de entorno no configuradas

**Antecedentes:** Algunos módulos pueden requerir claves, tokens o configuraciones.

**Síntomas:**
- Error: `KeyError` o advertencias sobre configuraciones faltantes

**Posibles Causas:**
- Variables de entorno requeridas no configuradas

**Soluciones:**
1. **Busca archivos como `.env.example` o similares.**
2. **Crea un archivo `.env` y completa los valores requeridos.**
3. **Recarga tu terminal o IDE después de configurar las variables de entorno.**

---

## Ejecutar Notebooks

### 6. El notebook no se abre o no se ejecuta

**Antecedentes:** Los notebooks de Jupyter necesitan una configuración adecuada.

**Síntomas:**
- El notebook no se lanza
- El navegador no se abre automáticamente

**Posibles Causas:**
- Jupyter no está instalado
- Problemas de configuración del navegador

**Soluciones:**
1. **Instala Jupyter (ver Problemas de Instalación arriba).**
2. **Abre los notebooks manualmente.**
   - Copia la URL desde el terminal (por ejemplo, `http://localhost:8888/?token=...`) y pégala en tu navegador.

### 7. El kernel se bloquea o se congela

**Antecedentes:** Los kernels de los notebooks pueden fallar debido a límites de recursos o errores de código.

**Síntomas:**
- El kernel muere o se reinicia repetidamente
- Errores de memoria insuficiente

**Posibles Causas:**
- Conjuntos de datos grandes
- Código o paquetes incompatibles

**Soluciones:**
1. **Reinicia el kernel.**  
   Usa el botón "Restart Kernel" en Jupyter.
2. **Verifica el uso de memoria.**  
   Cierra aplicaciones no utilizadas.
3. **Ejecuta los notebooks en plataformas en la nube.**  
   Usa [Google Colab](https://colab.research.google.com/) o [Azure Notebooks](https://notebooks.azure.com/).

---

## Problemas de Rendimiento

### 8. Los notebooks se ejecutan lentamente

**Antecedentes:** Algunas tareas de IA requieren mucha memoria y CPU.

**Síntomas:**
- Ejecución lenta
- El ventilador del portátil funciona a alta velocidad

**Posibles Causas:**
- Conjuntos de datos o modelos grandes
- Recursos limitados del sistema

**Soluciones:**
1. **Usa una plataforma en la nube.**
   - Sube el notebook a Colab o Azure Notebooks.
2. **Reduce el tamaño del conjunto de datos.**
   - Usa datos de muestra para practicar.
3. **Cierra programas innecesarios.**
   - Libera RAM del sistema.

---

## Problemas del Sitio Web del Libro

### 9. El capítulo no se carga

**Antecedentes:** El libro en línea muestra lecciones y capítulos.

**Síntomas:**
- Un capítulo (por ejemplo, Transformers/BERT) falta o no se abre

**Problema Conocido:**  
- [Problema #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. no se puede abrir en el sitio web del libro.” Causado por un error en el nombre del archivo (`READMEtransformers.md` en lugar de `README.md`).

**Soluciones:**
1. **Verifica errores en el renombrado de archivos.**  
   Si eres un contribuyente, asegúrate de que los archivos de los capítulos se llamen `README.md`.
2. **Reporta archivos faltantes.**  
   Abre un problema en GitHub con el nombre del capítulo y detalles del error.

---

## Problemas al Contribuir

### 10. PR no aceptado o fallos en las compilaciones

**Antecedentes:** Las contribuciones deben pasar pruebas y seguir las pautas.

**Síntomas:**
- Pull request rechazado
- Errores en la canalización CI/CD

**Posibles Causas:**
- Pruebas fallidas
- No seguir los estándares de codificación

**Soluciones:**
1. **Lee las pautas de contribución.**
   - Sigue el [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) del repositorio.
2. **Ejecuta pruebas localmente antes de hacer push.**
3. **Verifica reglas de linting o requisitos de formato.**

---

## Preguntas Frecuentes

### ¿Dónde puedo encontrar ayuda para módulos específicos?
- Cada módulo generalmente tiene su propio README. Comienza allí para obtener consejos de configuración y uso.

### ¿Cómo reporto un error o solicito una función?
- [Abre un problema en GitHub](https://github.com/microsoft/AI-For-Beginners/issues/new) con una descripción clara y pasos para reproducir.

### ¿Puedo pedir ayuda si mi problema no está listado?
- ¡Sí! Busca problemas existentes primero, y si no encuentras tu problema, crea uno nuevo.

---

## Obtener Ayuda

- **Revisa Problemas:** [Problemas en GitHub](https://github.com/microsoft/AI-For-Beginners/issues)
- **Haz Preguntas:** Usa las discusiones de GitHub o abre un problema.
- **Comunidad:** Consulta los enlaces del repositorio para opciones de chat/foro.

---

_Última Actualización: 20 de septiembre de 2025_

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.