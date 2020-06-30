import os, shutil
import datetime


def get_list(choice=None):
    result = os.listdir()
    if choice == 'folder':
        result = [f for f in result if os.path.isdir(f)]
    elif choice == 'file':
        result = [f for f in result if os.path.isfile(f)]
    return print(result)


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка с таким именем уже существует')


def delete(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Задайте другое имя')
    else:
        shutil.copy(name, new_name)


def save_info(massage):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {massage}'
    with open('info.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_dir(name):
    try:
        os.chdir(name)
    except FileNotFoundError:
        print('Папка с таким именем не существует. Создайте сначала папку!')
    else:
        print(f'Рабочая директория {os.getcwd()}')


if __name__ == '__main__':
    # create_folder('fol')
    # create_file('lll.txt')
    get_list('folder')
    get_list('file')
    get_list()
