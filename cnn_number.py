from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

import matplotlib.pyplot as plt

print(train_images[0])
print(train_labels[0])

image = train_images[0]
plt.imshow(image, cmap='gray')

train_images = train_images / 255.0
test_images = test_images / 255.0

train_labels = to_categorical(train_labels, 10)
test_labels = to_categorical(test_labels, 10)

print(train_images[0])
print(train_labels[0])

images = train_images[0]
plt.imshow(images, cmap='gray')

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, Flatten

model = Sequential([
  Input(shape=(28, 28)),
  Flatten(),
  Dense(128, activation='relu'),
  Dense(64, activation='relu'),
  Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
  loss='categorical_crossentropy',
  metrics=['accuracy']
)

model.fit(train_images, train_labels, epochs=10, batch_size=32,
validation_data=(test_images, test_labels))

test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(test_accuracy)

import cv2
import numpy as np
from google.colab import files
import matplotlib.pyplot as plt

uploaded = files.upload()
for filename in uploaded.keys():
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))
    img = img.astype('float32') / 255.0
    plt.imshow(img, cmap='gray')
    plt.title('Uploaded Image')
    plt.show()

    img = img.reshape(1, 28, 28)

    prediction = model.predict(img)
    predicted_digit = np.argmax(prediction)
    print(f"Predicted digit: {predicted_digit}")