name = ''


def polite_input(question):
    # глобальная переменная name, которая отвечает за имя пользователя
    global name
    # если это первый вызов функции, то спрашиваем, как зовут пользователя
    if name == '':
        print('Как вас зовут?')
        # записываем в name имя
        name = input()
        # выводим вопрос
        print(f'{name}, {question}')
        # возвращаем ответ пользователя
        return input()
    else:
        # выводим вопрос
        print(f'{name}, {question}')
        # возвращаем ответ пользователя
        return input()
