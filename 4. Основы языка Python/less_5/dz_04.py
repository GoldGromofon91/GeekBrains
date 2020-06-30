rus_dict = {
    'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'
}


def add_list(file):
    l = []
    for line in file:
        l.append(line.split(' - '))
    return l


def fnc_sort(usr_tuple):
    sort = {tup[0]: int(tup[1]) for tup in usr_tuple}
    return sort


def result_rus(lang_dict):
    res_dict = {}
    for key, val in lang_dict.items():
        for key_rus, val_rus in rus_dict.items():
            if key == key_rus:
                res_dict[val_rus] = val
    return res_dict


with open('dz_04.txt') as f:
    file_list = add_list(f)
    print(file_list)
    lang = fnc_sort(file_list)
    print(lang)

# with open('dz_04_in.txt', 'w') as f:
#     rus = result_rus(lang)
#     for k,v in rus.items():
#         f.write(f'{k} - {v}\n')
