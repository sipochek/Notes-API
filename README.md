## Название проекта
Notes API.
## Описание проекта: 
Notes API создан для создания, изменения, удаления, просмотра заметок. Данные сохраняются в SQLite. Так же есть тесты.
## Стек: 
Python, FastAPI, SQLite, Pydantic, pytest.
## Установка
Откройте powershell и перейдите в папку проекта:

```powershell
git clone https://github.com/sipochek/Notes-API.git
cd Notes-API
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Установка зависимостей через Docker

1. Для начала перейдите в папку с проектом fast_api: командой cd ...(вместо ... ваше расположение проекта)
2. Затем в папке с проектом выполнить команду:
    ```powershell
    docker volume create notes-data
    ```
3. Здесь же комада:
    ```powershell
    docker compose up -d --build
    ```
4. Откройте [Swagger UI](http://127.0.0.1:8082/docs) или проверьте [GET /notes](http://127.0.0.1:8082/notes).

## Запуск

```powershell
python -m uvicorn main:app --reload
```
Документация API: http://127.0.0.1:8000/docs

## ТЕСТЫ
Запускайте из папки проекта: 
```powershell
python -m pytest -v
```
## Маршруты

| Метод | Адрес | Действие |
|---|---|---|
| GET | /notes | Список заметок с limit и offset |
| GET | /notes?search= | Получить заметку по названию title |
| GET | /notes/{note_id} | Получить заметку |
| POST | /notes | Создать заметку |
| PUT | /notes/{note_id} | Обновить заметку |
| DELETE | /notes/{note_id} | Удалить заметку |
