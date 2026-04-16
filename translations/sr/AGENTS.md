# AGENTS.md

## Преглед пројекта

AI for Beginners је свеобухватан 12-недељни, 24-лекцијски курикулум који покрива основе вештачке интелигенције. Овај образовни репозиторијум укључује практичне лекције користећи Jupyter Notebooks, квизове и лабораторијске вежбе. Курикулум обухвата:

- Симболичку вештачку интелигенцију са представљањем знања и експертским системима
- Неуронске мреже и дубоко учење са TensorFlow и PyTorch
- Технике и архитектуре рачунарског вида
- Обраду природног језика (NLP), укључујући трансформере и BERT
- Специјализоване теме: генетски алгоритми, учење путем појачања, системи са више агената
- Етика вештачке интелигенције и принципи одговорне AI

**Кључне технологије:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (за апликацију квизова)

**Архитектура:** Репозиторијум образовног садржаја са Jupyter Notebooks организованим по тематским областима, допуњен апликацијом за квизове заснованом на Vue.js и обимном подршком за више језика.

## Команде за подешавање

### Примарно развојно окружење (Python/Jupyter)

Курикулум је дизајниран да ради са Python-ом и Jupyter Notebooks. Препоручени приступ је коришћење miniconda:

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

### Алтернатива: Коришћење devcontainer-а

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Подешавање апликације за квизове

Апликација за квизове је засебна Vue.js апликација која се налази у `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Радни ток развоја

### Рад са Jupyter Notebooks

1. **Локални развој:**
   - Активирајте conda окружење: `conda activate ai4beg`
   - Покрените Jupyter: `jupyter notebook` или `jupyter lab`
   - Навигирајте до фасцикли са лекцијама и отворите `.ipynb` датотеке
   - Интерактивно покрените ћелије да бисте пратили лекције

2. **VS Code са Python екстензијом:**
   - Отворите репозиторијум у VS Code
   - Инсталирајте Python екстензију
   - VS Code аутоматски детектује и користи conda окружење
   - Отворите `.ipynb` датотеке директно у VS Code

3. **Развој у облаку:**
   - **GitHub Codespaces:** Кликните на "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Користите Binder значку на README-у за покретање у прегледачу
   - Напомена: Binder има ограничене ресурсе и неке рестрикције у приступу вебу

### Подршка за GPU за напредне лекције

Касније лекције значајно користе GPU акцелерацију:

- **Azure Data Science VM:** Користите NC-серије VM-ова са GPU подршком
- **Azure Machine Learning:** Користите функције нотебука са GPU рачунарством
- **Google Colab:** Отпремите нотебуке појединачно (има бесплатну GPU подршку)

### Развој апликације за квизове

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Упутства за тестирање

Ово је образовни репозиторијум фокусиран на садржај за учење, а не на тестирање софтвера. Не постоји традиционални тестни пакет.

### Приступи за валидацију:

1. **Jupyter Notebooks:** Покрените ћелије секвенцијално да бисте проверили да ли примери кода раде
2. **Тестирање апликације за квизове:** Ручно тестирање преко развојног сервера
3. **Валидација превода:** Проверите преведени садржај у фасцикли `translations/`
4. **Linting апликације за квизове:** `npm run lint` у `etc/quiz-app/`

### Покретање примера кода:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Стил кода

### Стил Python кода

- Стандардне Python конвенције за образовни код
- Јасан, читљив код који приоритет даје учењу уместо оптимизацији
- Коментари који објашњавају кључне концепте
- Прилагођено за Jupyter Notebook: ћелије треба да буду самосталне где је могуће
- Нема строгих захтева за linting за садржај лекција

### JavaScript/Vue.js (Апликација за квизове)

- ESLint конфигурација у `etc/quiz-app/package.json`
- Покрените `npm run lint` за проверу и аутоматско исправљање проблема
- Vue 2.x конвенције
- Архитектура заснована на компонентама

### Организација датотека

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

## Изградња и распоређивање

### Jupyter садржај

Није потребан процес изградње - Jupyter Notebooks се директно извршавају.

### Апликација за квизове

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

### Сајт документације

Репозиторијум користи Docsify за документацију:
- `index.html` служи као улазна тачка
- Није потребна изградња - директно се сервира преко GitHub Pages
- Приступ на: https://microsoft.github.io/AI-For-Beginners/

## Упутства за допринос

### Процес Pull Request-а

1. **Формат наслова:** Јасни, описни наслови који описују промену
2. **Захтев за CLA:** Microsoft CLA мора бити потписан (аутоматска провера)
3. **Смернице за садржај:**
   - Одржавајте образовни фокус и приступ прилагођен почетницима
   - Тестирајте све примере кода у нотебуцима
   - Осигурајте да нотебуци раде од почетка до краја
   - Ажурирајте преводе ако мењате садржај на енглеском
4. **Промене у апликацији за квизове:** Покрените `npm run lint` пре комитовања

### Доприноси у преводу

- Преводи се аутоматски обављају преко GitHub Actions користећи co-op-translator
- Ручни преводи иду у `translations/<language-code>/`
- Преводи квизова у `etc/quiz-app/src/assets/translations/`
- Подржани језици: 40+ језика (погледајте README за комплетну листу)

### Активне области доприноса

Погледајте `etc/CONTRIBUTING.md` за тренутне потребе:
- Секције дубоког учења путем појачања
- Побољшања у детекцији објеката
- Примери препознавања именованих ентитета
- Узорци за обуку прилагођених уградњи

## Конфигурација окружења

### Потребне зависности

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

### Променљиве окружења

Нису потребне посебне променљиве окружења за основну употребу.

За Azure распоређивања (апликација за квизове):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (аутоматски постављен од стране Azure-а)

## Отклањање грешака и решавање проблема

### Уобичајени проблеми

**Проблем:** Креирање conda окружења не успева
- **Решење:** Прво ажурирајте conda: `conda update conda -y`
- Осигурајте довољно простора на диску (препоручено 50GB)

**Проблем:** Jupyter kernel није пронађен
- **Решење:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Проблем:** GPU није детектован у нотебуцима
- **Решење:** 
  - Проверите CUDA инсталацију: `nvidia-smi`
  - Проверите PyTorch GPU: `python -c "import torch; print(torch.cuda.is_available())"`
  - Проверите TensorFlow GPU: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Проблем:** Апликација за квизове се не покреће
- **Решење:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Проблем:** Binder истекне или блокира преузимања
- **Решење:** Користите GitHub Codespaces или локално подешавање за бољи приступ ресурсима

### Проблеми са меморијом

Неке лекције захтевају значајну RAM меморију (препоручено 8GB+):
- Користите cloud VM-ове за лекције које захтевају више ресурса
- Затворите друге апликације приликом тренирања модела
- Смањите величину batch-а у нотебуцима ако понестане меморије

## Додатне напомене

### За инструкторе курса

- Погледајте `lessons/0-course-setup/for-teachers.md` за упутства за предавање
- Лекције су самосталне и могу се предавати редом или бирати појединачно
- Процењено време: 12 недеља са 2 лекције недељно

### Ресурси у облаку

- **Azure for Students:** Бесплатни кредити доступни студентима
- **Microsoft Learn:** Допунски путеви учења повезани кроз курс
- **Binder:** Бесплатан, али са ограниченим ресурсима и неким мрежним ограничењима

### Опције за извршавање кода

1. **Локално (препоручено):** Потпуна контрола, најбоље перформансе, GPU подршка
2. **GitHub Codespaces:** Cloud-базирани VS Code, добар за брз приступ
3. **Binder:** Jupyter у прегледачу, бесплатан али ограничен
4. **Azure ML Notebooks:** Ентерпрајз опција са GPU подршком
5. **Google Colab:** Отпремите нотебуке појединачно, доступан бесплатан GPU ниво

### Рад са нотебуцима

- Нотебуци су дизајнирани да се извршавају ћелија по ћелија ради учења
- Многи нотебуци преузимају скупове података при првом покретању (може потрајати)
- Неки модели захтевају GPU за разумно време тренирања
- Претходно обучени модели се користе где је могуће ради смањења потреба за рачунарством

### Перформансе

- Касније лекције рачунарског вида (CNN, GAN) користе GPU
- NLP лекције са трансформерима могу захтевати значајну RAM меморију
- Тренирање од почетка је образовно, али захтева време
- Примери трансфер учења минимизирају време тренирања

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.