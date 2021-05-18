import os
import shutil
import csv

def createFolder(directory):
    if not os.path.isdir(directory):
           os.makedirs(directory)
    else:
        print ('Error: Creating directory. ' +  directory)

f = open('C:/Users/StudyK/eclipse-workspace/P0512/KETI-2017-SL-Annotation-v2_1.CSV', 'r', encoding = 'cp949')
data = csv.reader(f)

fname = []
mean = []
i = 0
j = 0

source = 'C:/Users/StudyK/eclipse-workspace/P0512/test/3001_6000'

for row in data:
    mean.append(row[-1])
    fname.append(row[0])
    path = 'C:/Users/StudyK/eclipse-workspace/P0512/test/3001_6000/' + mean[i]
    createFolder(path)
    files = os.listdir(source)
    i = i + 1
    fn = 'C:/Users/StudyK/eclipse-workspace/P0512/test/3001_6000/' + fname[j]
    pn = path + '/' + fname[j]
    shutil.copy(fn, pn)
    j = j + 1
f.close()
