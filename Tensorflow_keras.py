import tensorflow.keras as keras
import tensorflow as tf
import matplotlib.pyplot as plt
print(tf.__version__)
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
print(x_train[0])

print(y_train[0])
plt.imshow(x_train[0],cmap=plt.cm.binary)
plt.show()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)