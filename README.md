# Интеграционное тестирование для AtomicBoard

Цель этого проекта покрыть интеграционными тестами веб-сервис AtomicBoard. 

Необходимо покрыть тестами основные сценарии использования сервиса:

* Загрузка с сервера и отображение списка актуальных задач
* Перетаскивание задачи из одного столбца в другой
* Редактирование существующей задачи
* Пометка задачи как решенной
* Создание новой задачи

Stage сервер с тестовыми данными доступен по адресу [atomicboard.devman.org](http://atomicboard.devman.org).

Перед каждым запуском тестов создаётся новый пользователь со стандартным набором "рыбных" данных. Для этих целей создана [специальная страница](http://atomicboard.devman.org/create_test_user/).

# Установка PhantomJS
Если у вас еще не установлен PhantomJS, то необходимо выполнить следующие шаги:

Шаг 1. Для начала нужно установить необходимые пакеты для работы PhantomJS.
```
sudo apt-get install build-essential chrpath libssl-dev libxft-dev libfreetype6-dev libfreetype6 libfontconfig1-dev libfontconfig1 -y
```
Шаг 2. Далее скачиваем PhantomJS.
```
sudo wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
```
Шаг 3. После скачивания необходимо распаковать архив.
```
sudo tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/
```
Шаг 4. В заключении необходимо создать символьную ссылку для PhantomJS.
```
sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/
```

# Запуск тестирования
Для того, чтобы запустить интеграционные тесты для AtomicBoard, необходимо ввести в консоли:
```
python3 test.py
```

# Цели проекта

Код написан в учебных целях. Обучающие курсы для веб-разработчиков - [DEVMAN.org](https://devman.org)
