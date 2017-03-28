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

'''

import os

# TODO # make sysargm
path = '/home/ildar/Projects/DevMan/'

# print(os.listdir(path))

# for file in os.listdir(path):
# 	print(file, os.path.getsize(file))


for root, dirs, files in os.walk(path):
	print("\nroot: ", root)
	print("dirs: ", dirs)
	print("files: ", files)
	# for file in files:
	# 	for item in files:
	# 		if file == item:
	# 			if os.path.getsize(file) == os.path.getsize(item):
	# 				print("{} {}".format(os.path.join(root, file), os.path.getsize(file)))
	# 				print("{} {}".format(os.path.join(root, item), os.path.getsize(item)))



# result



if __name__ == '__main__':
    pass
