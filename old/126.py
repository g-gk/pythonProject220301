# сама функция
def letter(name, data, email, place='Казань'):
    return f'To: {email}\n' \
           f'Здравствуйте, {name}!\n' \
           f'Были бы рады видеть вас на встрече начинающих программистов в {place}, ' \
           f'которая пройдет {data}.'


# вызываю функцию на имя моей подруги
print(letter('Аня', '07.08.22', 'kostinaanna2008@yandex.ru', 'Москва'))
print()
# а больше я никого не знаю, поэтому вызываю на свое имя
print(letter('Амира', '11.11.22', 'amirahaliullova@yandex.ru'))
