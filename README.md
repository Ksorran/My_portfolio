# My_portfolio

Сайт на джанго, представляющий собой интерактивное портфолио.

## Описание

Данный сайт включает:
- Католог pet-проектов с подробным описанием;
- Мое резюме в интерактивном формате (с гиперссылками, на другие проекты/разделы сайта, подтверждающие скилы);
- Непосредственно сам сайт, который является достаточно большим и комплексным web-приложением, с достаточно широким
  функционалом (например полностью реализован процесс авторизации, в том числе через соцсети).

<details><summary><b>Скриншоты:</b></summary>
  
![Main_page](https://github.com/user-attachments/assets/46db04e5-4a8a-401b-978d-966f1b838f4e)

</details>

## Установка и запуск

### Зависимости

- Windows 11 (часть работ проводилась на Ubuntu, однако конечное тестирование проводилось только на Windows);
- Postgresql 16;
- Python 3.12;

### Установка

1. Скачать исходники из репозитория;
2. Установить зависимости (библиотеки) из файла `requirements.txt`:
   ```Python
   pip install -r requirements.txt
   ```
4. Переименовать env в `.env`;
5. Создать `.gitignore` (опционально);
6. Создать базу данных в PostgreSQL;
7. Прописать в `.env`:
   - DATABASE_NAME=имя вновь созданной БД в Postgresql,
   - DATABASE_USER=пользователь - владелец БД,
   - DATABASE_PASSWORD=пароль БД;
9. Произвести миграцию файлов (в терминале, находясь в корневой папке проекта):
     ```Shell
   python manage.py makemigrations
     ```
     ```Shell
   python manage.py migrate
     ```
11. Загрузить фикстуры:
    ```Shell
    python manage.py loaddata db.json
    ```

### Запуск

Для запуска сервера,
```Shell
python manage.py runserver
```

## Помощь

Обращаю внимание, что это демонстрационный вариант и в нем недоступна OAuth (авторизация через соцсети)
для её корректной работы в `.env` необходимо прописать SOCIAL_AUTH_GITHUB_SECRET и SOCIAL_AUTH_GITHUB_KEY.

