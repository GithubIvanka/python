"""
Внутри функции реализовать следующую логику:

Проверка на корректность e-mail отправителя и получателя.
Проверка на отправку самому себе.
Проверка на отправителя по умолчанию.
Пункты задачи:


Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".

Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"

Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."

В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
За один вызов функции выводится только одно из перечисленных уведомлений! Проверки перечислены по мере выполнения.
"""

def not_dog(string):
    for char in string:
        if char == '@':
            return False
    return True

def not_mail(string):
    if string[-3::] == ".ru" or string[-4::] == ".com" or string[-4::] == ".net":
        return False
    return True

def send_email(message, recipient, sender="university.help@gmail.com"):
    if not_dog(sender) or not_dog(recipient) or not_mail(sender) or not_mail(recipient):
        print(F"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(F"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(F"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')