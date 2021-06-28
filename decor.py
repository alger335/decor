from datetime import datetime
import os

log_path = os.path.abspath('log')


def debug(log_path):
    def _debug(function):
        def new_function(*args, **kwargs):
            date = datetime.now()
            result = function(*args, **kwargs)
            with open(log_path, 'a', encoding='UTF-8') as w:
                w.write(f'[{date}] Вызвана функция {function.__name__},\
    с аргументами {args}, {kwargs}. Возвращен результат {result}\n')
            return result

        return new_function

    return _debug
