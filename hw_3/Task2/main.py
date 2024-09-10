import pymongo
from pymongo import MongoClient

# Підключення до MongoDB
client = MongoClient("mongodb://mongo_container:27017/")  # Підключення до контейнера MongoDB
db = client['cat_database']
collection = db['cats']

# CREATE
def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    result = collection.insert_one(cat)
    print(f"Кота додано з ID: {result.inserted_id}")

# READ
def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)

def find_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кота з іменем {name} не знайдено.")

# UPDATE
def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count > 0:
        print(f"Вік кота {name} оновлено до {new_age}.")
    else:
        print(f"Кота з іменем {name} не знайдено.")

def add_cat_feature(name, new_feature):
    result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    if result.matched_count > 0:
        print(f"Нову характеристику '{new_feature}' додано до кота {name}.")
    else:
        print(f"Кота з іменем {name} не знайдено.")

# DELETE
def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кота з іменем {name} видалено.")
    else:
        print(f"Кота з іменем {name} не знайдено.")

def delete_all_cats():
    result = collection.delete_many({})
    print(f"Видалено {result.deleted_count} записів.")

# Меню
def main():
    while True:
        print("\nВиберіть дію:")
        print("1. Додати кота")
        print("2. Вивести всіх котів")
        print("3. Знайти кота за ім'ям")
        print("4. Оновити вік кота")
        print("5. Додати нову характеристику коту")
        print("6. Видалити кота за ім'ям")
        print("7. Видалити всіх котів")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Введіть ім'я кота: ")
            age = int(input("Введіть вік кота: "))
            features = input("Введіть характеристики кота через кому: ").split(',')
            create_cat(name, age, features)

        elif choice == "2":
            read_all_cats()

        elif choice == "3":
            name = input("Введіть ім'я кота: ")
            find_cat_by_name(name)

        elif choice == "4":
            name = input("Введіть ім'я кота: ")
            new_age = int(input("Введіть новий вік кота: "))
            update_cat_age(name, new_age)

        elif choice == "5":
            name = input("Введіть ім'я кота: ")
            new_feature = input("Введіть нову характеристику: ")
            add_cat_feature(name, new_feature)

        elif choice == "6":
            name = input("Введіть ім'я кота: ")
            delete_cat_by_name(name)

        elif choice == "7":
            confirm = input("Ви впевнені, що хочете видалити всіх котів? (y/n): ")
            if confirm.lower() == 'y':
                delete_all_cats()

        elif choice == "0":
            print("Вихід...")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
