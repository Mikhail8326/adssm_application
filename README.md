ASTEROID DEFENCE SATELLITE SWARM MODELING
ADDSM

ИНСТРУКЦИЯ ПО УСТАНОВКЕ

1) Желательно удалить с ПК интерпретатор Python если версия отличается от 3.10. Скачать Python 3.10 (https://www.python.org/downloads/release/python-31011/). Убедиться, что Python добавлен в системные переменные среды (из консоли вызывается Python и pip);
2) Установить poetry версии 1.2 (консоль: pip install poetry==1.2.0);
3) Установить PyCharm (https://www.jetbrains.com/ru-ru/pycharm/);
4) Установить GitHub Desktop (https://desktop.github.com/). Если нет аккаунта на github.com создать; 
5) Залогиниться в GitHub Desktop и клонировать публичный репозиторий с проектом в любую удобную папку (Clone a repository -> URL -> https://github.com/Mikhail8326/adssm_application.git);
6) Открыть проект в Pycharm. Открыть командную строку в корне проекта (можно через терминал Pycharm) и выполнить команду poetry install;
7) Дождаться окончания установки виртуальной среды. Выполнить команду poetry env info. Выбрать в настройках проекта интерпретатор python на тот, который указан в poetry env info;