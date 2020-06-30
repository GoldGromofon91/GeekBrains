def add_list(file):
    l = []
    for line in file:
        l.append(line.split())
    return l


def fnc_sort(usr_tuple):
    sort = {tup[0]: int(tup[1]) for tup in usr_tuple}
    return sort


def res_sort(staff):
    sort = {k: v for k, v in staff.items() if v < 20000}
    return sort


def output(dict):
    for key, val in dict.items():
        print(key,val)


with open('dz_03.txt', 'r') as f:
    file_list = add_list(f)
    print(file_list)
    staff = fnc_sort(file_list)
    res_staff = res_sort(staff)
    print('Работники с ЗП менее 20000:')
    output(res_staff)