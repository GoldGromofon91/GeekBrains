import sys, os

def create():
    for i in range(1,10):
        folder_name = f'dir_{i}'
        os.mkdir(folder_name)

def delete():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.rmdir(folder_name)

if __name__=="__main__":
    create()
    delete()