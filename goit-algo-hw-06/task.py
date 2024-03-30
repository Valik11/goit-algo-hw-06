from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value  # Ініціалізація поля зі значенням

    def __str__(self):
        return str(self.value)  # Повернення рядкового представлення поля

class Name(Field):
    pass  # Клас для зберігання імені, успадковує від Field

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Номер телефону повинен складатися з 10 цифр.")  # Перевірка на валідність номера телефону
        super().__init__(value)  # Виклик конструктора базового класу

class Record:
    def __init__(self, name):
        self.name = Name(name)  # Ініціалізація імені контакту
        self.phones = []  # Список телефонів контакту

    def add_phone(self, phone):
        self.phones.append(Phone(phone))  # Додавання нового телефону

    def remove_phone(self, phone):
        phone_to_remove = self.find_phone(phone)  # Пошук телефону для видалення
        if phone_to_remove:
            self.phones.remove(phone_to_remove)  # Видалення телефону

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.find_phone(old_phone)  # Пошук телефону для редагування
        if phone_to_edit:
            self.phones.remove(phone_to_edit)  # Видалення старого телефону
            self.phones.append(Phone(new_phone))  # Додавання нового телефону

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p  # Повернення знайденого телефону
        return None  # Якщо телефон не знайдено, повернення None

    def __str__(self):
        # Повернення рядкового представлення запису
        return f"Ім'я контакту: {self.name.value}, телефони: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record  # Додавання запису до адресної книги

    def find(self, name):
        return self.data.get(name)  # Пошук запису за іменем

    def delete(self, name):
        if name in self.data:
            del self.data[name]  # Видалення запису за іменем

# Приклад використання:
if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Ім'я контакту: John, телефони: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

