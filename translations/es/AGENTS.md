# AGENTS.md

## Resumen del Proyecto

AI for Beginners es un plan de estudios completo de 12 semanas y 24 lecciones que cubre los fundamentos de la Inteligencia Artificial. Este repositorio educativo incluye lecciones prácticas utilizando Jupyter Notebooks, cuestionarios y laboratorios prácticos. El plan de estudios abarca:

- IA simbólica con Representación del Conocimiento y Sistemas Expertos
- Redes Neuronales y Aprendizaje Profundo con TensorFlow y PyTorch
- Técnicas y arquitecturas de Visión por Computadora
- Procesamiento de Lenguaje Natural (NLP), incluyendo transformers y BERT
- Temas especializados: Algoritmos Genéticos, Aprendizaje por Refuerzo, Sistemas Multiagente
- Ética en IA y principios de IA Responsable

**Tecnologías clave:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (para la aplicación de cuestionarios)

**Arquitectura:** Repositorio de contenido educativo con Jupyter Notebooks organizados por áreas temáticas, complementado con una aplicación de cuestionarios basada en Vue.js y soporte multilingüe extenso.

## Comandos de Configuración

### Entorno de Desarrollo Principal (Python/Jupyter)

El plan de estudios está diseñado para ejecutarse con Python y Jupyter Notebooks. El enfoque recomendado es usar miniconda:

```bash
# Clone the repository
git clone https://github.com/microsoft/ai-for-beginners
cd ai-for-beginners

# Create and activate conda environment
conda env create --name ai4beg --file environment.yml
conda activate ai4beg

# Start Jupyter Notebook
jupyter notebook
# OR
jupyter lab
```

### Alternativa: Usar devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Configuración de la Aplicación de Cuestionarios

La aplicación de cuestionarios es una aplicación separada de Vue.js ubicada en `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Flujo de Trabajo de Desarrollo

### Trabajando con Jupyter Notebooks

1. **Desarrollo Local:**
   - Activar el entorno conda: `conda activate ai4beg`
   - Iniciar Jupyter: `jupyter notebook` o `jupyter lab`
   - Navegar a las carpetas de lecciones y abrir archivos `.ipynb`
   - Ejecutar las celdas de manera interactiva para seguir las lecciones

2. **VS Code con Extensión de Python:**
   - Abrir el repositorio en VS Code
   - Instalar la extensión de Python
   - VS Code detecta automáticamente y utiliza el entorno conda
   - Abrir archivos `.ipynb` directamente en VS Code

3. **Desarrollo en la Nube:**
   - **GitHub Codespaces:** Haz clic en "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Usa el badge de Binder en el README para lanzarlo en el navegador
   - Nota: Binder tiene recursos limitados y algunas restricciones de acceso web

### Soporte de GPU para Lecciones Avanzadas

Las lecciones posteriores se benefician significativamente de la aceleración por GPU:

- **Azure Data Science VM:** Usar VMs de la serie NC con soporte de GPU
- **Azure Machine Learning:** Usar características de notebooks con computación GPU
- **Google Colab:** Subir notebooks individualmente (tiene soporte gratuito de GPU)

### Desarrollo de la Aplicación de Cuestionarios

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Instrucciones de Pruebas

Este es un repositorio educativo enfocado en contenido de aprendizaje más que en pruebas de software. No hay un conjunto de pruebas tradicional.

### Métodos de Validación:

1. **Jupyter Notebooks:** Ejecutar las celdas secuencialmente para verificar que los ejemplos de código funcionen
2. **Pruebas de la Aplicación de Cuestionarios:** Pruebas manuales a través del servidor de desarrollo
3. **Validación de Traducciones:** Revisar el contenido traducido en la carpeta `translations/`
4. **Linting de la Aplicación de Cuestionarios:** `npm run lint` en `etc/quiz-app/`

### Ejecución de Ejemplos de Código:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Estilo de Código

### Estilo de Código Python

- Convenciones estándar de Python para código educativo
- Código claro y legible que prioriza el aprendizaje sobre la optimización
- Comentarios explicando conceptos clave
- Compatible con Jupyter Notebook: las celdas deben ser autónomas siempre que sea posible
- No se requieren reglas estrictas de linting para el contenido de las lecciones

### JavaScript/Vue.js (Aplicación de Cuestionarios)

- Configuración de ESLint en `etc/quiz-app/package.json`
- Ejecutar `npm run lint` para verificar y corregir problemas automáticamente
- Convenciones de Vue 2.x
- Arquitectura basada en componentes

### Organización de Archivos

```
lessons/
  ├── 0-course-setup/          # Setup instructions
  ├── 1-Intro/                 # Introduction to AI
  ├── 2-Symbolic/              # Symbolic AI
  ├── 3-NeuralNetworks/        # Neural Networks basics
  ├── 4-ComputerVision/        # Computer Vision
  ├── 5-NLP/                   # Natural Language Processing
  ├── 6-Other/                 # Other AI techniques
  ├── 7-Ethics/                # AI Ethics
  └── X-Extras/                # Additional content

etc/
  ├── quiz-app/                # Vue.js quiz application
  └── quiz-src/                # Quiz source files

translations/                  # Multi-language translations
```

## Construcción y Despliegue

### Contenido de Jupyter

No se requiere proceso de construcción: los Jupyter Notebooks se ejecutan directamente.

### Aplicación de Cuestionarios

```bash
cd etc/quiz-app

# Development
npm run serve

# Production build
npm run build  # Outputs to etc/quiz-app/dist/

# Deploy to Azure Static Web Apps
# Azure automatically creates GitHub Actions workflow
# See etc/quiz-app/README.md for detailed deployment instructions
```

### Sitio de Documentación

El repositorio utiliza Docsify para la documentación:
- `index.html` sirve como punto de entrada
- No se requiere construcción: se sirve directamente a través de GitHub Pages
- Acceso en: https://microsoft.github.io/AI-For-Beginners/

## Directrices para Contribuir

### Proceso de Pull Request

1. **Formato del Título:** Títulos claros y descriptivos que describan el cambio
2. **Requisito de CLA:** Se debe firmar el CLA de Microsoft (verificación automatizada)
3. **Directrices de Contenido:**
   - Mantener el enfoque educativo y accesible para principiantes
   - Probar todos los ejemplos de código en los notebooks
   - Asegurarse de que los notebooks se ejecuten de principio a fin
   - Actualizar traducciones si se modifica contenido en inglés
4. **Cambios en la Aplicación de Cuestionarios:** Ejecutar `npm run lint` antes de hacer commit

### Contribuciones de Traducción

- Las traducciones se automatizan mediante GitHub Actions usando co-op-translator
- Las traducciones manuales van en `translations/<language-code>/`
- Traducciones de cuestionarios en `etc/quiz-app/src/assets/translations/`
- Idiomas soportados: más de 40 idiomas (ver README para la lista completa)

### Áreas Activas de Contribución

Ver `etc/CONTRIBUTING.md` para necesidades actuales:
- Secciones de Aprendizaje por Refuerzo Profundo
- Mejoras en Detección de Objetos
- Ejemplos de Reconocimiento de Entidades Nombradas
- Muestras de entrenamiento de embeddings personalizados

## Configuración del Entorno

### Dependencias Requeridas

```bash
# Core Python packages (from requirements.txt)
tensorflow==2.17.0
torch (via conda)
torchvision (via conda)
keras==3.5.0
opencv (via conda)
scikit-learn
numpy==1.26
pandas==2.2.2
matplotlib==3.9
jupyter
```

### Variables de Entorno

No se requieren variables de entorno especiales para el uso básico.

Para despliegues en Azure (aplicación de cuestionarios):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (configurado automáticamente por Azure)

## Depuración y Resolución de Problemas

### Problemas Comunes

**Problema:** Falla la creación del entorno conda
- **Solución:** Actualizar conda primero: `conda update conda -y`
- Asegurarse de tener suficiente espacio en disco (se recomiendan 50GB)

**Problema:** Kernel de Jupyter no encontrado
- **Solución:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problema:** GPU no detectada en los notebooks
- **Solución:** 
  - Verificar instalación de CUDA: `nvidia-smi`
  - Comprobar GPU en PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Comprobar GPU en TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problema:** La aplicación de cuestionarios no inicia
- **Solución:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problema:** Binder se agota o bloquea descargas
- **Solución:** Usar GitHub Codespaces o configuración local para mejor acceso a recursos

### Problemas de Memoria

Algunas lecciones requieren una cantidad significativa de RAM (se recomiendan 8GB+):
- Usar VMs en la nube para lecciones que consumen muchos recursos
- Cerrar otras aplicaciones al entrenar modelos
- Reducir tamaños de lote en los notebooks si se agota la memoria

## Notas Adicionales

### Para Instructores del Curso

- Ver `lessons/0-course-setup/for-teachers.md` para orientación sobre enseñanza
- Las lecciones son autónomas y pueden enseñarse en secuencia o seleccionarse individualmente
- Tiempo estimado: 12 semanas con 2 lecciones por semana

### Recursos en la Nube

- **Azure for Students:** Créditos gratuitos disponibles para estudiantes
- **Microsoft Learn:** Rutas de aprendizaje complementarias enlazadas a lo largo del curso
- **Binder:** Gratuito pero con recursos limitados y algunas restricciones de red

### Opciones de Ejecución de Código

1. **Local (Recomendado):** Control total, mejor rendimiento, soporte GPU
2. **GitHub Codespaces:** VS Code basado en la nube, bueno para acceso rápido
3. **Binder:** Jupyter basado en navegador, gratuito pero limitado
4. **Azure ML Notebooks:** Opción empresarial con soporte GPU
5. **Google Colab:** Subir notebooks individualmente, disponible nivel gratuito de GPU

### Trabajando con Notebooks

- Los notebooks están diseñados para ejecutarse celda por celda para aprendizaje
- Muchos notebooks descargan conjuntos de datos en la primera ejecución (puede tomar tiempo)
- Algunos modelos requieren GPU para tiempos de entrenamiento razonables
- Se utilizan modelos preentrenados cuando es posible para reducir requisitos de cómputo

### Consideraciones de Rendimiento

- Las lecciones posteriores de visión por computadora (CNNs, GANs) se benefician de GPU
- Las lecciones de transformers en NLP pueden requerir una cantidad significativa de RAM
- Entrenar desde cero es educativo pero consume tiempo
- Los ejemplos de aprendizaje por transferencia minimizan el tiempo de entrenamiento

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.