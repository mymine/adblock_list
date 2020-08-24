import sys
import os
import time

libdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'lib')
rawdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'raw')
    
down_data = []
with open(os.path.join(libdir, 'data_record.txt'), 'r', encoding='UTF-8') as f:
    for line in f:
        temp = line.strip('\n')
        down_data.append(temp)
down_lenth = len(down_data)
rawdata = []
with open(os.path.join(libdir, 'metadata.txt'), 'r', encoding='UTF-8') as f:
    for line in f:
        temp = line.strip('\n').strip('?')
        if temp.startswith('!') or temp.startswith('[') or temp.startswith('raw') or len(temp) == 0:
            continue
        else:
            rawdata.append(temp)
raw_lenth = len(rawdata)
for i in range(0, raw_lenth):
    os.system('rm %s' % (os.path.join(rawdir, rawdata[i])))
for i in range(0, down_lenth):
    os.system('wget -P %s %s' % (rawdir, down_data[i]))
