import speech_recognition as sr
import os
import time
import playsound
import csv
import shutil
import cv2
import glob

def readVideo(path_dir):
    file_list = os.listdir(path_dir)
    img_name = path_dir + '/' + file_list[0]
    capture = cv2.VideoCapture(img_name)

    if capture.isOpened():
        while True:
            ret, frame = capture.read()
            if ret:
                cv2.imshow(path_dir, frame)
                cv2.waitKey(25)
            else:
                break
            
    #while cv2.waitKey(25) < 0:
        #if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
            #capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

        #ret, frame = capture.read()
        #cv2.imshow("VideoFrame", frame)
    capture.release()
    cv2.destroyAllWindows()


r = sr.Recognizer()

with sr.Microphone() as source:

    print('Speak Anything : ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='ko-KR')
        path_dir = 'C:/Users/StudyK/eclipse-workspace/P0512/test/front/3001_6000/' + text
        print('You said : {}'.format(text))
        readVideo(path_dir)
        
    except:
        print('Sorry could not recognize your voice')
