import psycopg2
from faker import Faker

# Підключення до PostgreSQL
conn = psycopg2.connect(
    dbname="task_management",
    user="postgres",
    password="postgres_password",
    host="db",  # ім'я сервісу в docker-compose.yml
    port="5432",
)
cursor = conn.cursor()

# Ініціалізація Faker
fake = Faker()

# Заповнення таблиці users
for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cursor.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email)
    )

# Заповнення таблиці status
statuses = ["new", "in progress", "completed"]
for status in statuses:
    cursor.execute("INSERT INTO status (name) VALUES (%s)", (status,))

# Заповнення таблиці tasks
for _ in range(20):
    title = fake.sentence(nb_words=6)
    description = fake.paragraph()
    status_id = fake.random_int(min=1, max=3)
    user_id = fake.random_int(min=1, max=10)
    cursor.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
        (title, description, status_id, user_id),
    )

# Збереження змін та закриття з'єднання
conn.commit()
cursor.close()
conn.close()

print("Таблиці успішно заповнені!")
