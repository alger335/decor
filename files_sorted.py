from datetime import datetime
import glob
import os

def debug(function):
    counter = {}

    def new_function(*args, **kwargs):
        date = datetime.now()
        print(f'[{date}] Вызвана функция {function.__name__}')
        print(f'с аргументами')
        print(f'{args}')
        print(f'{kwargs}')
        result = function(*args, **kwargs)
        print(f'Возвращенный результат {result}')
        function_called = counter.get(function.__name__, 0)
        if function_called == 0:
            counter[function.__name__] = 1
        else:
            counter[function.__name__] += 1

        print(f'Counter: {counter}')
        with open('log.txt', 'a', encoding='UTF-8') as w:
            w.write(f'[{date}] Вызвана функция {function.__name__},\
с аргументами {args}, {kwargs}. Возвращен результат {result}\n')
        return result
    return new_function



@debug #foo = replacer(foo)
def file_filter():
    names_list = []
    for name in glob.glob('*.txt'):
        names_list.append(os.path.join(name))
    return names_list

@debug
def len_file(names_list):
    names_len_list = []
    for name in names_list:
        with open(os.path.join(name), encoding='UTF-8') as f:
            file_len = [name, len(f.readlines())]
            names_len_list.append(file_len)
    names_len_list.sort(key=lambda k: k[1])
    return names_len_list

@debug
def write_file(names_len_list):
    for name in names_len_list:
        with open(os.path.join(name[0]), encoding='UTF-8') as f:
            text = f.readlines()
            with open('file.txt', 'a', encoding='UTF-8') as w:
                w.write(name[0])
                w.write(f"\n{str(name[1])}\n")
                w.writelines(f"{line}" for line in text)
                w.write('\n')
    return
