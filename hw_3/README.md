# Проект: Основи комп'ютерних систем та їхні елементи

## Структура бази даних

### Task 1: PostgreSQL

- **База даних:** `task_management`
- **Таблиці:**
  - `users`
    - `id`: SERIAL PRIMARY KEY
    - `fullname`: VARCHAR(100) NOT NULL
    - `email`: VARCHAR(100) UNIQUE NOT NULL
  - `status`
    - `id`: SERIAL PRIMARY KEY
    - `name`: VARCHAR(50) UNIQUE NOT NULL
  - `tasks`
    - `id`: SERIAL PRIMARY KEY
    - `title`: VARCHAR(100) NOT NULL
    - `description`: TEXT
    - `status_id`: INTEGER REFERENCES `status(id)`
    - `user_id`: INTEGER REFERENCES `users(id)` ON DELETE CASCADE

### Task 2: MongoDB

- **База даних:** `cat_database`
- **Колекція:**
  - `cats`
    - `_id`: ObjectId
    - `name`: Ім'я кота (string)
    - `age`: Вік кота (int)
    - `features`: Список характеристик кота (array)

## Як запустити

### Task 1: PostgreSQL з Docker

1. Склонуйте репозиторій:
    ```bash
    git clone https://your-repository-url
    ```

2. Перейдіть у директорію `Task1`:
    ```bash
    cd Task1
    ```

3. Запустіть Docker-контейнери:
    ```bash
    docker-compose up --build
    ```

4. Після запуску база даних `task_management` буде створена, і ви зможете підключитися до неї за допомогою будь-якого клієнта, такого як `DBeaver` або `psql`.

5. Виконайте SQL-запити через будь-який клієнт для перевірки функціоналу CRUD:
    - Отримання завдань користувача.
    - Оновлення статусу завдань.
    - Додавання нових завдань.

### Task 2: MongoDB з Docker

1. Перейдіть у директорію `Task2`:
    ```bash
    cd Task2
    ```

2. Запустіть Docker-контейнери:
    ```bash
    docker-compose up --build
    ```

3. Після запуску MongoDB буде готовий до використання.

4. Виконайте Python скрипт для роботи з базою даних MongoDB:
    ```bash
    docker-compose exec python_app python3 /app/main.py
    ```

5. У меню виберіть одну з опцій:
    - Додати кота.
    - Вивести всіх котів.
    - Знайти кота за ім'ям.
    - Оновити вік кота.
    - Додати нову характеристику коту.
    - Видалити кота за ім'ям.
    - Видалити всіх котів.

## Ліцензія

Цей проект ліцензовано під ліцензією MIT.
