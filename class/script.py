class MyName:
    """Клас для роботи з іменами користувачів"""

    total_names = 0  # Class Variable: лічильник всіх створених об'єктів

    def __init__(self, name=None) -> None:
        """Ініціалізація класу"""
        if name is None:
            self.name = "Anonymous"
        else:
            # Перевірка: ім'я повинно містити лише літери
            if not name.isalpha():
                raise ValueError("Ім'я може містити лише літери!")
            self.name = name.capitalize()  # Перша літера завжди велика

        MyName.total_names += 1
        self.my_id = MyName.total_names

    @property
    def whoami(self) -> str:
        """Повертає рядок з ім'ям користувача"""
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Повертає email користувача"""
        return self.create_email()

    @property
    def full_name(self) -> str:
        """Нова властивість: User #id: name (email)"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def create_email(self, domain="itcollege.lviv.ua") -> str:
        """Повертає email користувача. Можна змінити домен після @"""
        return f"{self.name}@{domain}"

    def name_length(self) -> int:
        """Повертає кількість букв у імені"""
        return len(self.name)

    @classmethod
    def anonymous_user(cls):
        """Метод класу для створення анонімного користувача"""
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Статичний метод, який повертає текст привітання"""
        return f"You say: {message}"

    def save_to_file(self, filename="users.txt"):
        """Зберігає дані користувача у файл"""
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{self.full_name}\n")


# ------------------- Основний код -------------------

print("Розпочинаємо створювати обʼєкти!")

# Список імен
names = ("Oleksiy", "Bohdan", None)

# Створюємо об'єкти
all_names = {name: MyName(name) for name in names}

# Вивід інформації
for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email("example.com")}
This is static {type(MyName.say_hello)} with custom message:
{me.say_hello("Привіт! Мене звати Олексій 👋")}
Number of letters in name: {me.name_length()}
Full info: {me.full_name}
{"<*>"*20}""")
    
    # Зберегти в файл
    me.save_to_file()

# Порахувати кількість імен у списку names
num_names_in_list = len(names)
print(f"Кількість імен у списку names: {num_names_in_list}")
print(f"Кількість створених об'єктів: {MyName.total_names}")

