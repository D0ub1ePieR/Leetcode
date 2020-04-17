import glob
import os


def get_name(st):
    while st.find('-') != -1:
        name_index = st.find('-')
        st = st[name_index+1:]
    return st


def get_info(st):
    py_file_name = glob.glob(path + st + '/*.py')[0]
    py_file = open(py_file_name, 'r', encoding='utf-8')

    for j in range(5):
        line = py_file.readline()
        if j == 0:
            language = line[2:-1]
        if j == 1:
            level = line[2:-1]
        if j == 2:
            tag = line[2:-1]
        if j == 3:
            speed = line[-7:-1]
        if j == 4:
            memory = line[-7:-1]

    return language, level, tag, speed, memory


path = './solutions/'
file_name = './readme.md'

file = open(file_name, 'r', encoding='utf-8')
lines = file.readlines()
file.close()
start = lines.index('<start-tag>\n')
end = lines.index('<end-tag>\n')

dic = {}
for root, dirs, files in os.walk(path):
    for pack in dirs:
        index = pack.index('-')
        dic[int(pack[:index])] = pack

nums = sorted(dic)

file = open(file_name, 'w', encoding='utf-8')
for i in range(start+2):
    file.write(lines[i])
file.write('当前进度:  **' + str(len(nums)) + ' / -**\n')
file.write('| No. | 题目名称 | Language | 难度 | tag | 运行速度(超过) | 占用内存(超过) |\n')
file.write('| :-: | :-: | :-: | :-: | :-: | :-: | :-: |\n')

for num in nums:
    no = num
    name = get_name(dic[num])
    language, level, tag, speed, memory = get_info(dic[num])
    url = path + dic[num]
    file.write('| %s | [%s](%s) | %s | %s | %s | %s | %s |\n' % (str(no), name, url, language.replace('python', 'py'), level, tag, speed, memory))

for i in range(end-1, len(lines)):
    file.write(lines[i])
file.close()
