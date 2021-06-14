import subprocess
import locale

def info_str(string):
    for el in string:
        print('STRING ifno')
        print(f'String - {el}')
        print(f'Type - {type(el)}',end='\n')
        
def ascii_err():
    del_el=[]
    sbytes=['attribute','класс','функция','type']
    for el in sbytes:
        try:
            el = el.encode('ascii')
        except:
            del_el.append(el)
            continue
        finally:
            print(f'String - {el}')
            print(f'Type - {type(el)}',end='\n')
    print('Слова которые невозможно кодировать в байты\n',del_el)

def byte_info(byte_string=None):
    if byte_string:
        for el in byte_string:
            print('BYTES ifno')
            print(f'Bytes string - {el}')
            print(f'Type - {type(el)}')
    ascii_err()

def simple_decode(u_list):
    CODE_STANDART=['utf-8','ascii']
    choice = int(input(f'1.{CODE_STANDART[0]}\n2.{CODE_STANDART[1]} ')) - 1
    for el in u_list:
        print(f'Элемент-{el}')
        try:
            byte_str = el.encode(CODE_STANDART[choice])
        except:
            print('\tОшибка декодирования')
            byte_str = el.encode(CODE_STANDART[choice],'replace')
            continue
        finally:
            ret_str = byte_str.decode(CODE_STANDART[choice]) 
            print(f'Байты-{byte_str}\nДекодирвоание - {ret_str}')
        
def ping():
    args = ['ping', 'yandex.ru']
    subproc = subprocess.Popen(args, stdout=subprocess.PIPE)
    i=0
    for line in subproc.stdout:
        if i < 5:
            print(line)    
            line = line.decode('utf-8') 
            print(line)
            i += 1
        else:
            break

def open_s(file):
    with open(file) as f:
        print(f)
        for line in f:
            print(line, type(line))

def openUnic(file):
    coding = locale.getpreferredencoding()
    print(coding)
    with open(file, encoding=coding) as f:
        for el in f:
            print(el)

if __name__ == "__main__":
    #1.-2.
    info_str(['разработка','сокет','декоратор','\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430\u000a','\u0441\u043e\u043a\u0435\u0442\u000a','\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'])
    #3.
    byte_info([b'class', b'function', b'method'])
    byte_info()
    #4.
    simple_decode(['разработка','администрирование','protocol','standard'])
    #5.
    ping()
    #6.
    open_s("text.txt")
    #6.1
    openUnic('text.txt')