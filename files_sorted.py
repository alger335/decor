from decor import debug, log_path
import glob
import os


@debug(log_path=log_path)
def file_filter():
    names_list = []
    for name in glob.glob('*.txt'):
        names_list.append(os.path.join(name))
    return names_list


@debug(log_path=log_path)
def len_file(names_list):
    names_len_list = []
    for name in names_list:
        with open(os.path.join(name), encoding='UTF-8') as f:
            file_len = [name, len(f.readlines())]
            names_len_list.append(file_len)
    names_len_list.sort(key=lambda k: k[1])
    return names_len_list


@debug(log_path=log_path)
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
