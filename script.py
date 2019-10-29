import glob

path = './LeetCodePython/common/'
files = glob.glob(path + '*.py')
for file in files:
    pass

wp_path = './WriteUp.md'
f = open(wp_path, 'r', encoding='UTF-8')
lines = f.readlines()
f.close()

f = open(wp_path, 'w')
for line in lines:
    f.write(line)
f.close()
