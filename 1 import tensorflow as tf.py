import tensorflow as tf

print("TensorFlow version:", tf.__version__)

mnist = tf.keras.datasets.mnist
#keras : sequental모델 이름. mnist: 데이터세트

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

