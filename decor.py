from datetime import datetime

def debug(function):
    def new_function(*args, **kwargs):
        date = datetime.now()
        print(f'[{date}] Вызвана функция {function.__name__}')
        print(f'С аргументами')
        print(f'{args}')
        print(f'{kwargs}')
        result = function(*args, **kwargs)
        print(f'Возвращенный результат {result}')
        return result
    return new_function

@debug #foo = replacer(foo)
def foo(x):
    print('вызвана функция foo')
    print(x)
    return True

result = foo(3)
if result:
    print('Что-то сделать')

