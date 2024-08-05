def send_email(message, recipient, sender = "university.help@gmail.com"):
    if not recipient.endswith(b) or not sender.endswith(b) or a not in recipient or a not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print('Невозможно отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
         print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif not  sender == 'university.help@gmail.com':
       print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!', f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')


a = ('@')
b = ('.com', '.ru', '.net')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')