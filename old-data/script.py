import glob

path = './LeetCodePython/common/'
files = glob.glob(path + '*.py')

rd_path = './README.md'
f = open(rd_path, 'r', encoding='UTF-8')
lines = f.readlines()
f.close()

f = open(rd_path, 'w', encoding='UTF-8')
for line in lines:
    f.write(line)
    if line.find(':-:') != -1:
        break

for file in files:
    index = file.index('\\')
    filename = file[index+1:-3]
    index = filename.index('-')
    num = filename[:index]
    name = filename[index+1:]
    f.write('| ' + num + ' | [' + name + '](' + file + ') |\n')
    pass

f.close()
'''
wp_path = './WriteUp.md'
f = open(wp_path, 'r', encoding='UTF-8')
lines = f.readlines()
f.close()

f = open(wp_path, 'w', encoding='UTF-8')
for line in lines:
    f.write(line)
f.close()
'''
