def not_dog(string):    # проверка на наличие символа '@'
    for char in string:
        if char == '@':
            return False
    return True

def not_mail(string):   # проверка на окончание ".ru", ".com", ".net"
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