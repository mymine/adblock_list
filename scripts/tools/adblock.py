import sys
import os
import datetime
from raw_download import *

libdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'lib')
rawdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'raw')
outputdir = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

success = False
while(success == False):
    success = download()

rawdata = []
rawdata_plus = []
rawdata_privacy = []
with open(os.path.join(libdir, 'metadata.txt'), 'r', encoding='UTF-8') as f:
    for line in f:
        temp = line.strip('\n')
        if temp.startswith('!') or temp.startswith('[') or temp.startswith('#') or len(temp) == 0:
            continue
        else:
            if temp.startswith('?'):
                rawdata_plus.append(temp.strip('?'))
            elif temp.startswith('&'):
                rawdata_privacy.append(temp.strip('&'))
            else:
                rawdata.append(temp)


result = []
result_plus = []
result_privacy = []
result_lite = []

# Baisc 处理
data_lenth = len(rawdata)
for t in range(0, data_lenth):
    with open(os.path.join(rawdir, rawdata[t]), 'r', encoding='UTF-8') as f:
        for line in f:
            temp = line.strip('\n')
            if temp.startswith('!') or temp.startswith('[') or len(temp) == 0:
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
            if temp.startswith('!') or temp.startswith('[') or len(temp) == 0:
                continue
            else:
                result_plus.append(temp)

# Privacy 处理
data_lenth = len(rawdata_privacy)
for t in range(0, data_lenth):
    with open(os.path.join(rawdir, rawdata_privacy[t]), 'r', encoding='UTF-8') as f:
        for line in f:
            temp = line.strip('\n')
            if temp.startswith('!') or temp.startswith('[') or len(temp) == 0:
                continue
            else:
                result_privacy.append(temp)

# 排序去重
result = list(set(result))
result.sort()
result_plus = list(set(result_plus))
result_plus.sort()
result_privacy = list(set(result_privacy))
result_privacy.sort()
result_lite = list(result_lite)
result_lite.sort()

# Lite 列表处理
# https://www.reddit.com/r/uBlockOrigin/comments/eylhw4/ignore_generic_cosmetic_filters_selected_or_not/
# ##.filter ###filter 会被忽略
lenth = len(result)
for t in range(0, lenth):
    if result[t].startswith('##.') or result[t].startswith('###'):
        continue
    else:
        result_lite.append(result[t])

# 时间戳信息
time_now = datetime.datetime.now()
date_string = time_now.strftime('%Y%m%d%H%S')

# 文本输出
with open(os.path.join(outputdir, "adblock.txt"), "w", encoding='UTF-8') as f:
    f.write('[uniartisan\'s Adblock List]\n'+'! Version: ' +
            date_string+'\n'+'! Title:  uniartisan\'s Adblock List\n' +
            '! Expires: 1 days (update frequency)\n')
    lenth = len(result)
    f.write(
        '! URL = https://github.com/uniartisan/adblock_list\n! Lenth = ' + str(lenth)+'\n')
    for i in range(0, lenth):
        f.write(result[i]+'\n')

with open(os.path.join(outputdir, "adblock_plus.txt"), "w", encoding='UTF-8') as f:
    f.write('[uniartisan\'s Adblock List Plus]\n'+'! Version: ' +
            date_string+'\n'+'! Title:  uniartisan\'s Adblock List Plus\n' +
            '! Expires: 1 days (update frequency)\n')
    lenth_plus = len(result_plus)
    f.write('! URL = https://github.com/uniartisan/adblock_list\n! Lenth = ' +
            str(lenth_plus)+'\n')
    for i in range(0, lenth_plus):
        f.write(result_plus[i]+'\n')

with open(os.path.join(outputdir, "adblock_privacy.txt"), "w", encoding='UTF-8') as f:
    f.write('[uniartisan\'s Privacy List]\n'+'! Version: ' +
            date_string+'\n'+'! Title:  uniartisan\'s Privacy List\n' +
            '! Expires: 1 days (update frequency)\n')
    lenth_privay = len(result_privacy)
    f.write('! URL = https://github.com/uniartisan/adblock_list\n! Lenth = ' +
            str(lenth_privay)+'\n')
    for i in range(0, lenth_privay):
        f.write(result_privacy[i]+'\n')

with open(os.path.join(outputdir, "adblock_lite.txt"), "w", encoding='UTF-8') as f:
    f.write('[uniartisan\'s Adblock List Lite]\n'+'! Version: ' +
            date_string+'\n'+'! Title:  uniartisan\'s Adblock List Lite\n' +
            '! Expires: 1 days (update frequency)\n')
    lenth = len(result_lite)
    f.write(
        '! URL = https://github.com/uniartisan/adblock_list\n! Lenth = ' + str(lenth)+'\n')
    for i in range(0, lenth):
        f.write(result_lite[i]+'\n')
