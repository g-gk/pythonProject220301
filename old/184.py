def check_password(password):
    def wrapper(func):
        """декоратор"""

        def wrap(*args, **kwargs):
            if input('пароль: ') != password:
                print('неверный пароль')
                return
            return func(*args, **kwargs)

        return wrap

    return wrapper
