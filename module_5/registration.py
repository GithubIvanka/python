class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, user_password):
        self.data[username] = user_password

class User:
    """
    Класс пользователя, содержащий атрибуты: логин и пароль.
    """
    def __init__(self, username, user_pass, password_confirm):
        self.username = username

        num_str = "0123456789"
        char_up = False
        num_confirm = False

        for char in user_pass:
            if not char_up and char == char.upper():
                char_up = True
            if not num_confirm and char in num_str:
                num_confirm = True
            if char_up and num_confirm:
                break

        if user_pass == password_confirm and char_up and num_confirm:
            self.user_pass = user_pass


if __name__ == "__main__":
    database = Database()

    while True:
        choice = input("Приветствую! Выберите действие: \n"
                       "1 - Вход\n"
                       "2 - Регистрация\n"
                       "3 - Выход\n")
        if choice == "1":
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Вход выполнен, {login}.")
                    break
                else:
                    print("Неверный пароль. ")
            else:
                print("Пользователь не найден.")
        elif choice == "2":
            user = User(input("Введите логин: "),
                password := input("Введите пароль: "),
                password2 := input("Повторите пароль: "))

            if password != password2:
                print("Пароли не совпадают, повторите попытку.")
                continue
            database.add_user(user.username, user.user_pass)
        elif choice == "3":
            break