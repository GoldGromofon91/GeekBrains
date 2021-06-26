import csv
import re


def get_data():
    main_list = []
    search_list = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_list.append(search_list)
    file_data = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    for file in file_data:
        with open(file, encoding='cp1251') as f:
            string = f.read()
            prod = re.findall(search_list[0] + r".{1,}", string)[0].split('  ')[-1].strip()
            name = re.findall(search_list[1] + r".{1,}", string)[0].split('  ')[-1].strip()
            code = re.findall(search_list[2] + r".{1,}", string)[0].split('  ')[-1].strip()
            type = re.findall(search_list[3] + r".{1,}", string)[0].split('  ')[-1].strip()

            os_prod_list.append(prod)
            os_name_list.append(name)
            os_code_list.append(code)
            os_type_list.append(type)

    main_list.append(os_prod_list)
    main_list.append(os_name_list)
    main_list.append(os_code_list)
    main_list.append(os_type_list)

    return (main_list)


def write_to_csv(file):
    list_to_write = get_data()
    with open(file, 'w') as f:
        f_writer = csv.writer(f)
        for row in list_to_write:
            f_writer.writerow(row)

    # with open(file) as f:
    #     f_n_reader = csv.reader(f)
    #     f_n_headers = next(f_n_reader)
    #     print('Headers: ', f_n_headers)
    #     for row in f_n_reader:
    #         print(row)


if __name__ == "__main__":
    write_to_csv('result.csv')