# AGENTS.md

## Преглед на проекта

AI for Beginners е обширна 12-седмична, 24-урочна учебна програма, която обхваща основите на изкуствения интелект. Този образователен репозиторий включва практически уроци с Jupyter Notebooks, тестове и практически лаборатории. Учебната програма обхваща:

- Символен ИИ с представяне на знания и експертни системи
- Невронни мрежи и дълбоко обучение с TensorFlow и PyTorch
- Техники и архитектури за компютърно зрение
- Обработка на естествен език (NLP), включително трансформъри и BERT
- Специализирани теми: Генетични алгоритми, Укрепващо обучение, Многоагентни системи
- Етика на ИИ и принципи за отговорен ИИ

**Ключови технологии:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (за приложението за тестове)

**Архитектура:** Образователен репозиторий със съдържание, организирано по теми, допълнен от приложение за тестове, базирано на Vue.js, и обширна поддръжка на много езици.

## Команди за настройка

### Основна среда за разработка (Python/Jupyter)

Учебната програма е проектирана да работи с Python и Jupyter Notebooks. Препоръчителният подход е използването на miniconda:

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

### Алтернатива: Използване на devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Настройка на приложението за тестове

Приложението за тестове е отделно Vue.js приложение, разположено в `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Работен процес за разработка

### Работа с Jupyter Notebooks

1. **Локална разработка:**
   - Активирайте conda средата: `conda activate ai4beg`
   - Стартирайте Jupyter: `jupyter notebook` или `jupyter lab`
   - Навигирайте до папките с уроци и отворете `.ipynb` файлове
   - Изпълнявайте клетките интерактивно, за да следвате уроците

2. **VS Code с разширение за Python:**
   - Отворете репозитория във VS Code
   - Инсталирайте разширението за Python
   - VS Code автоматично разпознава и използва conda средата
   - Отворете `.ipynb` файлове директно във VS Code

3. **Облачна разработка:**
   - **GitHub Codespaces:** Кликнете "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Използвайте значката Binder в README, за да стартирате в браузъра
   - Забележка: Binder има ограничени ресурси и някои ограничения за уеб достъп

### Поддръжка на GPU за напреднали уроци

По-късните уроци значително се възползват от ускорение с GPU:

- **Azure Data Science VM:** Използвайте NC-серия VM с поддръжка на GPU
- **Azure Machine Learning:** Използвайте функции за бележници с GPU изчисления
- **Google Colab:** Качвайте бележници индивидуално (има безплатна GPU поддръжка)

### Разработка на приложението за тестове

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Инструкции за тестване

Това е образователен репозиторий, фокусиран върху учебно съдържание, а не върху тестване на софтуер. Няма традиционен тестов пакет.

### Подходи за валидиране:

1. **Jupyter Notebooks:** Изпълнявайте клетките последователно, за да проверите дали примерите с код работят
2. **Тестване на приложението за тестове:** Ръчно тестване чрез сървър за разработка
3. **Валидиране на преводи:** Проверете преведеното съдържание в папката `translations/`
4. **Linting на приложението за тестове:** `npm run lint` в `etc/quiz-app/`

### Изпълнение на примери с код:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Стил на кода

### Стил на Python кода

- Стандартни Python конвенции за образователен код
- Ясен, четим код, който приоритизира ученето пред оптимизацията
- Коментари, обясняващи ключови концепции
- Съвместимост с Jupyter Notebook: клетките трябва да са самостоятелни, където е възможно
- Няма строги изисквания за linting за съдържанието на уроците

### JavaScript/Vue.js (Приложение за тестове)

- Конфигурация на ESLint в `etc/quiz-app/package.json`
- Стартирайте `npm run lint`, за да проверите и автоматично коригирате проблеми
- Конвенции за Vue 2.x
- Архитектура, базирана на компоненти

### Организация на файловете

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

## Създаване и разгръщане

### Jupyter съдържание

Не се изисква процес на създаване - Jupyter Notebooks се изпълняват директно.

### Приложение за тестове

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

### Сайт за документация

Репозиторият използва Docsify за документация:
- `index.html` служи като входна точка
- Не се изисква създаване - обслужва се директно чрез GitHub Pages
- Достъп на: https://microsoft.github.io/AI-For-Beginners/

## Насоки за принос

### Процес за Pull Request

1. **Формат на заглавието:** Ясни, описателни заглавия, описващи промяната
2. **Изискване за CLA:** Microsoft CLA трябва да бъде подписан (автоматична проверка)
3. **Насоки за съдържание:**
   - Поддържайте образователния фокус и подходящия за начинаещи стил
   - Тествайте всички примери с код в бележниците
   - Уверете се, че бележниците се изпълняват от край до край
   - Актуализирайте преводите, ако променяте съдържанието на английски
4. **Промени в приложението за тестове:** Стартирайте `npm run lint` преди да направите комит

### Приноси за преводи

- Преводите се автоматизират чрез GitHub Actions с помощта на co-op-translator
- Ръчните преводи се поставят в `translations/<language-code>/`
- Преводите за тестовете са в `etc/quiz-app/src/assets/translations/`
- Поддържани езици: 40+ езика (вижте README за пълния списък)

### Активни области за принос

Вижте `etc/CONTRIBUTING.md` за текущите нужди:
- Секции за дълбоко укрепващо обучение
- Подобрения в разпознаването на обекти
- Примери за разпознаване на именувани обекти
- Примери за обучение на персонализирани вграждания

## Конфигурация на средата

### Необходими зависимости

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

### Променливи на средата

Не се изискват специални променливи на средата за основна употреба.

За разгръщания в Azure (приложение за тестове):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (автоматично зададен от Azure)

## Отстраняване на грешки и проблеми

### Чести проблеми

**Проблем:** Създаването на conda среда се проваля
- **Решение:** Актуализирайте conda първо: `conda update conda -y`
- Уверете се, че имате достатъчно дисково пространство (препоръчително 50GB)

**Проблем:** Jupyter не намира ядрото
- **Решение:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Проблем:** GPU не се открива в бележниците
- **Решение:** 
  - Проверете инсталацията на CUDA: `nvidia-smi`
  - Проверете GPU в PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Проверете GPU в TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Проблем:** Приложението за тестове не стартира
- **Решение:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Проблем:** Binder изтича или блокира изтеглянията
- **Решение:** Използвайте GitHub Codespaces или локална настройка за по-добър достъп до ресурси

### Проблеми с паметта

Някои уроци изискват значителна RAM (препоръчително 8GB+):
- Използвайте облачни VM за уроци, изискващи много ресурси
- Затворете други приложения, когато обучавате модели
- Намалете размерите на партидите в бележниците, ако паметта не достига

## Допълнителни бележки

### За преподаватели

- Вижте `lessons/0-course-setup/for-teachers.md` за насоки за преподаване
- Уроците са самостоятелни и могат да се преподават последователно или индивидуално
- Прогнозно време: 12 седмици с 2 урока на седмица

### Облачни ресурси

- **Azure for Students:** Налични безплатни кредити за студенти
- **Microsoft Learn:** Допълнителни учебни пътеки, свързани в уроците
- **Binder:** Безплатен, но с ограничени ресурси и някои мрежови ограничения

### Опции за изпълнение на код

1. **Локално (Препоръчително):** Пълен контрол, най-добра производителност, поддръжка на GPU
2. **GitHub Codespaces:** Облачна VS Code среда, добра за бърз достъп
3. **Binder:** Jupyter в браузъра, безплатен, но ограничен
4. **Azure ML Notebooks:** Корпоративна опция с поддръжка на GPU
5. **Google Colab:** Качвайте бележници индивидуално, наличен безплатен GPU слой

### Работа с бележници

- Бележниците са проектирани да се изпълняват клетка по клетка за обучение
- Много бележници изтеглят набори от данни при първото изпълнение (може да отнеме време)
- Някои модели изискват GPU за разумно време за обучение
- Използват се предварително обучени модели, където е възможно, за да се намалят изчислителните изисквания

### Съображения за производителност

- По-късните уроци за компютърно зрение (CNN, GAN) се възползват от GPU
- Уроците за NLP трансформъри може да изискват значителна RAM
- Обучението от нулата е образователно, но отнема много време
- Примерите за трансферно обучение минимизират времето за обучение

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.