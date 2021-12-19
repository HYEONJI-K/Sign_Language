import speech_recognition as sr
import os
import sys
import time
import playsound
import csv
import shutil
import cv2
import glob
import konlpy
from konlpy.tag import Komoran

path_dir = 'C:/Users/StudyK/eclipse-workspace/P0512/test/front/3001_6000/'

# 폴더 리스트 불러오기
f = open('C:/Users/StudyK/eclipse-workspace/P0605/test.txt', 'r', encoding='UTF8')
lines = f.readlines()
f.close()

dicpath = 'C:/Users/StudyK/eclipse-workspace/P0605/plus_text.txt'

noun_tag = []

for line in lines:
    # 줄바꿈 제거후, 리스트 생성
    noun_tag.append(line.rstrip())

def Noun(str_list):
    for i in str_list:
        c = 0
        komoran = Komoran(userdic=dicpath)
        temp = komoran.morphs(i)
        print(temp)
        if temp[c] in noun_tag:
            print("1. {}".format(temp))
            plus_dir = path_dir + temp[c]
            readVideo(plus_dir)
            c = c + 1
        else:
            state = ''.join(temp)
            print("2. {}".format(state))
            if state in noun_tag:
                plus_dir = path_dir + state
                readVideo(plus_dir)
                c = c + 1
            else:
                break
        
def readVideo(path_dir):
    file_list = os.listdir(path_dir)
    img_name = path_dir + '/' + file_list[0]
    print(file_list[0])
    capture = cv2.VideoCapture(img_name)

    if capture.isOpened():
        while True:
            ret, frame = capture.read()
            if ret:
                cv2.imshow(path_dir, frame)
                cv2.waitKey(10)
            else:
                break

    capture.release()
    cv2.destroyAllWindows()

    
r = sr.Recognizer()

# 띄어쓰기 나누기
str_list = []

# 형태소 분석 문장/단어 추출
temp = []

with sr.Microphone() as source:

    print('Speak Anything : ')
    audio = r.listen(source)
    
#    try:
    text = r.recognize_google(audio, language='ko-KR')
    print('{}'.format(text))
    komoran = Komoran()
    str_list = text.split(" ")
    Noun(str_list)
        
#    except:
#        print('Sorry could not recognize your voice')
