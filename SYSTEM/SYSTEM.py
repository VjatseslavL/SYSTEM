"""Напишите программу имитирующую регистрацию и авторизацию пользователей в какой-либо системе.

До начала работы программы создайте 2 пустых списка(пароли и логины),
которые будут заполняться по мере регистрации новых пользователей.

Реализация регистрации и авторизации осуществичется при помощи функций.

В бесконечном цикле на каждом его ветке предлагайте пройти регистрацию, авторизироваться или закончить работу.

При выборе "авторизироваться":

разрешить это делать только пользователям из списка.
и если логин и пароль соответствуют значениям из списков
При выборе "регистрироваться" две возможности:

автоматическое создание пароля
самостоятельное"""

import random
import string

account = {}


def sign_up():
    try:
        while True:
            try:
                login = str(input("--> Введите имя: "))
                print("sam - создать свой пароль, generate - создать случайный пароль")
                select = str(input("--> Введите значение: "))

                if select == "sam":
                    password = str(input("--> Введите пароль: "))
                    password = list(password)

                    trdict = {"digits": False, "lowercase": False, "uppercase": False, "punc": False}

                    for i in password:
                        if i in string.digits:
                            trdict["digits"] = True

                        elif i in string.ascii_lowercase:
                            trdict["lowercase"] = True

                        elif i in string.ascii_uppercase:
                            trdict["uppercase"] = True

                        elif i in string.punctuation:
                            trdict["punc"] = True

                    if trdict == {"digits": True, "lowercase": True, "uppercase": True, "punc": True}:
                        pass
                    else:
                        return "Error!"

                    password = "".join(password)

                elif select == "generate":
                    str0 = ".,:;!_*-+()/#¤%&"
                    str1 = '0123456789'
                    str2 = 'qwertyuiopasdfghjklzxcvbnm'
                    str3 = str2.upper()
                    str4 = str0 + str1 + str2 + str3
                    ls = list(str4)
                    random.shuffle(ls)
                    # Извлекаем из списка 12 произвольных значений
                    password = ''.join([random.choice(ls) for x in range(12)])
                    # Пароль готов
                    print(password)

                print("--> exit - выход, next - дальше")
                select1 = str(input("--> Введите значение: "))

                xdict = {login: password}

                if select1 == "next":
                    pass
                elif select == "exit":
                    return "Вы вышли!"

                if len(account) == 0:
                    password = "".join(password)
                    account.update(xdict)
                    return f"---> Successful! {login, password}"

                listname = [i for i in account]

                if login in listname:
                    return "---> Такой пользователь уже есть! \n---> попробуйте ещё раз"
                else:
                    password = "".join(password)
                    account.update(xdict)
                    return f"---> Successful! {login, password}"
            except:
                pass
    except DeprecationWarning:
        pass


def sign_in():
    global login

    count = 0
    try:
        while True:
            login = str(input("--> Введите имя: "))
            password = str(input("--> Введите пароль: "))
            print("--> exit - выход, next - дальше")
            select = str(input("--> Введите значение: "))

            if select == "next":
                pass
            elif select == "exit":
                return "Вы вышли!"

            if login in account and account[login] == password:
                print("---> Successful!\n" + "---> Вы вошли в систему")
                return log()
            else:
                count += 1
                print(f"Try: {count}")

            if count == 10:
                return "Закончились попытки"

    except DeprecationWarning:
        pass


def log():
    while True:
        print("SYSTEM".center(16, "="))
        print("log out".center(16))
        print("exit".center(16))
        print(f"account: {login}")
        print("".center(16, "="))

        access = str(input("--> Ваш выбор: "))

        if access == "log out":
            return "Вы вышли из системы!"

        elif access == "exit":
            exit()

        elif access == "dict":
            print(account)


def computer():
    while True:
        print("SYSTEM".center(16, "="))
        print("sign_in".center(16))
        print("sign_up".center(16))
        print("exit".center(16))
        print("".center(16, "="))

        access = str(input("--> Ваш выбор: "))

        if access == "sign_in":
            print(sign_in())

        elif access == "sign_up":
            print(sign_up())

        elif access == "exit":
            exit()

        elif access == "dict":
            print(account)


if __name__ == '__main__':
    computer()
