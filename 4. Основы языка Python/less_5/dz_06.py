def fnc_sort(file_str):
    edit_list = []
    # print(file_str)
    for i in range(len(file_str.split())):
        # print(file_str.split())
        # print(i)
        lett = ''
        for el in file_str.split()[i]:
            # print(file_str.split()[i])
            # print(el)
            if el.isdigit():
                lett += el
                # print(lett)
            else:
                break
        if lett.isdigit():
            edit_list.append(int(lett))
            # print(edit_list)
    return sum(edit_list)


with open('dz_06.txt', 'r') as f:
    line = f.readlines()
print(line)
my_dict = {el.split(':')[0]: fnc_sort(el.split(':')[1]) for el in line}

print(my_dict)