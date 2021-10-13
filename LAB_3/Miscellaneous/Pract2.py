# Basic Program of TensorFlow.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066

import tensorflow as tf

if __name__ == '__main__':
    node1 = tf.constant(3, dtype=tf.int32)
    node2 = tf.constant(5, dtype=tf.int32)
    node3 = tf.add(node1, node2)