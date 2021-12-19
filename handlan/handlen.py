import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten

from keras.layers.convolutional import Conv2D

from keras.layers.convolutional import MaxPooling2D

from keras.preprocessing.image import ImageDataGenerator

from keras.preprocessing import image

import matplotlib.pyplot as plt

# 랜덤시드 고정시키기

np.random.seed(3)

train_datagen = ImageDataGenerator(rescale=1./255)


train_generator = train_datagen.flow_from_directory(

        'C:/Users/StudyK/Desktop/handlan/sign',

        target_size=(28, 28),

        batch_size=2,

        class_mode='categorical')


test_datagen = ImageDataGenerator(rescale=1./255)


test_generator = test_datagen.flow_from_directory(

        'C:/Users/StudyK/Desktop/handlan/test',

        target_size=(28, 28),

        batch_size=2,

        class_mode='categorical')

model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3),

                 activation='relu',

                 input_shape=(28,28,3)))

model.add(Conv2D(64, (3, 3), activation='relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(128, activation='relu'))

model.add(Dense(14, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit_generator(

        train_generator,

        steps_per_epoch=10,

        epochs=1000,

        validation_data=test_generator,

        validation_steps=10)

print("-- Evaluate --")

scores = model.evaluate_generator(test_generator, steps=5)

model.save('mymodel.h5')

print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

print("-- Predict --")

output = model.predict_generator(test_generator, steps=5)

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

print(test_generator.class_indices)

print(output)

print("-- Predict --")

img = image.load_img('C:/Users/StudyK/Desktop/handlan/test/ㄹ/1.png')

plt.imshow(img)

img = (np.expand_dims(img,0))

#output = model.predict_generator(test_generator)

output = model.predict(img)

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

print(test_generator.class_indices)

print(output)
