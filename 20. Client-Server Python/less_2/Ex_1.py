import csv
import re

def get_data():
    
    data=['info_1.txt','info_2.txt','info_3.txt']
    correct_data = []
    correct_title = ['LENOVO','ACER','DELL']
    os_prod_list,os_name_list, os_code_list, os_type_list = [],[],[],[]

    for idx,el in enumerate(data):
        file=''
        with open (el,'rb') as f_obj:
            for line in f_obj:
                line_bytes = line.decode('utf-8','replace')
                file += line_bytes
                prod = re.search(r'^[\S]{12,}\s[\S]{7}:', line_bytes)
                os = re.search(r'^[\S]{8}\s[\S]{2}:', line_bytes)
                if prod:
                    arr = line_bytes.strip().split()
                    for el in arr:
                        if el in correct_title:
                            os_prod_list.append(el)
                if os:
                    arr = line_bytes.strip().split(':')
                    print(arr)
                    for el in arr:
                        print(el.strip())
                        el_s = re.match(r"^[A-Z]*\s[A-Z]*\s\d+\s",el.strip())
                        print(el_s.group(0))
                        continue
        correct_data.insert(idx,file)
        continue


    print(os_prod_list)
    print(os_name_list)

if __name__ == "__main__":
    get_data()