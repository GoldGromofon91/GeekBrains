from function import get_list, create_file, create_folder, delete, copy, save_info,change_dir
import sys
from game import game
from game_reverse import game_reverse

try:
    command = sys.argv[1]
except IndexError:
    print('Введите команду, для помощи введите "help"')
else:
    # command_f = sys.argv[1],[2]
    if command == 'list':
        get_list()
    # elif command_f == 'list folder':
    #   choice = sys.argv[2]
    #  get_list(choice)
    # elif command_f == 'list file':
    #   choice = sys.argv[2]
    #  get_list(choice)
    elif command == 'game':
        game()
    elif command == 'reverse':
        game_reverse()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Введите имя файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Введите имя папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Введите имя файла или папки которую хотите удалить')
        else:
            delete(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Введите имя файла или имя нового файла')
        else:
            copy(name, new_name)
    elif command == 'change':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Введите имя директории')
        else:
            change_dir(name)
    elif command == 'help':
        print('Для просмотра файлов в директории введите "list", для выбора сортировки введите "folder"/"file"')
        print('Для создания файла введите "create_file"')
        print('Для создания папки введите "create_folder"')
        print('Для копирования файла введите "copy_(имя_файла)_(имя_нового_файла)"')
        print('Для копирования папик введите "copy_(имя_папки)_(имя_новой_папки)"')
        print('Для удаления файла или папки введите "delete_(имя_файла_или_папки)"')
        print('Для смены директории введите "change"')
        print('Для запуска игры №1 введите "game"')
        print('Для запуска игры №2 введите "reverse"')
