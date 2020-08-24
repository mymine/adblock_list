import sys
import os
import datetime

libdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'lib')
rawdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'raw')
outputdir = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
downpydir = os.path.join(os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'tools'), 'raw_download.py')
os.system('python3 %s' % downpydir)

rawdata = []
rawdata_plus = []
with open(os.path.join(libdir, 'metadata.txt'), 'r', encoding='UTF-8') as f:
    for line in f:
        temp = line.strip('\n')
        if temp.startswith('!') or temp.startswith('[') or temp.startswith('#') or len(temp) == 0:
            continue
        else:
            if not temp.startswith('?'):
                rawdata.append(temp)
            else:
                rawdata_plus.append(temp.strip('?'))


result = []
result_plus = []
data_lenth = len(rawdata)

for t in range(0, data_lenth):
    with open(os.path.join(rawdir, rawdata[t]), 'r', encoding='UTF-8') as f:
        for line in f:
            temp = line.strip('\n')
            if temp.startswith('!') or temp.startswith('[') or temp.startswith('#') or len(temp) == 0:
                continue
            else:
                result.append(temp)
                result_plus.append(temp)

# Plus 处理

data_lenth = len(rawdata_plus)
for t in range(0, data_lenth):
    with open(os.path.join(rawdir, rawdata_plus[t]), 'r', encoding='UTF-8') as f:
        for line in f:
            temp = line.strip('\n')
            if temp.startswith('!') or temp.startswith('[') or temp.startswith('#') or len(temp) == 0:
                continue
            else:
                result_plus.append(temp)

# 排序去重
result = list(set(result))
result.sort()
result_plus = list(set(result_plus))
result_plus.sort()

# 时间戳信息
time_now = datetime.datetime.now()
date_string = time_now.strftime('%Y%m%d%H')

# 文本输出

with open(os.path.join(outputdir, "adblock.txt"), "w", encoding='UTF-8') as f:
    f.write('[uniartisan\'s Adblock List]\n'+'! Version: ' +
            date_string+'\n'+'! Title:  uniartisan\'s Adblock List\n' +
            '! Expires: 1 days (update frequency)\n')
    lenth = len(result)
    f.write(
        '! URL = https://github.com/uniartisan/adblock_list\n! Lenth = ' + str(lenth)+'\n')
    for i in range(1, lenth):
        f.write(result[i]+'\n')

with open(os.path.join(outputdir, "adblock_plus.txt"), "w", encoding='UTF-8') as f:
    f.write('[uniartisan\'s Adblock List Plus]\n'+'! Version: ' +
            date_string+'\n'+'! Title:  uniartisan\'s Adblock List Plus\n' +
            '! Expires: 1 days (update frequency)\n')
    lenth_plus = len(result_plus)
    f.write('! URL = https://github.com/uniartisan/adblock_list\n! Lenth = ' +
            str(lenth_plus)+'\n')
    for i in range(1, lenth_plus):
        f.write(result_plus[i]+'\n')
