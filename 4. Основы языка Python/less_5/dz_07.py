import json


def firm_edit(file_list):
    firm_list = []
    for i in file_line:
        firm_list.append([i.split()[0], int(i.split()[-2]) - int(i.split()[-1])])
    return firm_list


with open('dz_07.txt', 'r') as f:
    file_line = f.readlines()
firms = firm_edit(file_line)
profit = [i[1] for i in firms if i[1] > 0]
firm_dict = [{firms[i][0]: firms[i][1] for i in range(len(firms))}, {'avarage': round(sum(profit) / len(profit), 2)}]

with open('dz_07.json', 'w', encoding='utf-8') as f:
    firm_json = json.dump(firm_dict, f)

with open('dz_07.json', 'r', encoding='utf-8') as file:
    firma = json.load(file)
print(firma)
