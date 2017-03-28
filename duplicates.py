'''
- tests?
- readme.md
- commit ЧАЩЕ
- проверить с дупликатом и без

1 получить список файлов весь
2 цикл берем файл и сравниваем название с каждым в списке
3 если совпадает - проверяем размер
При совпадении сохранить?
!!! Не сравнивать файл с самим собой

Выводим: Название файла, размер и пути дубликатов

+++1) либо 2 цикла - берем файл, потом цикл по всем файлам
2) либо сначала сделать общий список файлов, потом по нему цикл - пути!!!! а не названия файлов

?
как быть с ситуацией, когда потом мы встретим дубликат?
Удалять из списка? 

'''

import os

# TODO # make sysargm
path = '/home/ildar/Projects/DevMan/'

# print(os.listdir(path))

# for file in os.listdir(path):
# 	print(file, os.path.getsize(file))

all_files = []

# create list with all files. Join for get full path
for root, dirs, files in os.walk(path):
	for file in files:
		all_files.append(os.path.join(root, file))

print(all_files)

for file in all_files:



# 		for item in files:
# 			if file == item:
# 				if os.path.getsize(file) == os.path.getsize(item):
# 					print("{} {}".format(os.path.join(root, file), os.path.getsize(file)))
# 					print("{} {}".format(os.path.join(root, item), os.path.getsize(item)))



# result



if __name__ == '__main__':
    pass
