import tensorflow as tf

import keras

from keras.models import load_model

model = load_model('C:/Users/StudyK/Desktop/handlan/mymodel.h5')


import cv2

import numpy as np


capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

hangul_list = ["giyeok","nieun","digeut","lieul","mieum","bieob","sioht","eiung","jieot","chieot","kiyeok","tigeut","pieup","hieut"]

red = (0,0,255) #빨간색

font_point = (370,100) #글자 위치


while True:

    ret, frame = capture.read()

    cv2.rectangle(frame,(220,140),(420,340),(0,255,0),2)

    subimg = frame[140:340 , 220:420]

    subimg = cv2.resize(subimg,dsize=(28,28),interpolation=cv2.INTER_AREA)

    subimg = (np.expand_dims(subimg,0))

    output = model.predict(subimg)

    for i in range(0,13):

        if output[0,i]:

            cv2.putText(frame,hangul_list[i],font_point,cv2.FONT_HERSHEY_COMPLEX,2,red)

    #cv2.imshow("roi", subimg)

    cv2.imshow("VideoFrame", frame)        

    if cv2.waitKey(30) > 0: break


capture.release()

cv2.destroyAllWindows()
