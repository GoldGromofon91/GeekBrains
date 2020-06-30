import os
# имя операционной системы
print(os.name)
# посмотреть текущую директрию
print(os.getcwd())
#создаем новй путь
new_track = os.path.join(os.getcwd(), 'new_f')
# создаем папку по новому пути
os.mkdir(new_track)
