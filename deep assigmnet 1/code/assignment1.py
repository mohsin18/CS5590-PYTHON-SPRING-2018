import time
import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# data reading
# built in function of tensor flow
MNIST = input_data.read_data_sets("/data/mnist", one_hot=True)
# Defining the parameters
learn = 0.01
batch = 128
n_ephs =10
#  creation of placeholders
# each label is one hot vector.
A = tf.placeholder(tf.float32, [batch, 784])
B = tf.placeholder(tf.float32, [batch, 10])
w = tf.Variable(tf.random_normal(shape=[784, 10], stddev=0.01), name="weights")
b = tf.Variable(tf.zeros([1, 10]), name="bias")
logits = tf.matmul(A, w) + b
entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=B)
loss = tf.reduce_mean(entropy) # computes mean over example
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learn).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    writer = tf.summary.FileWriter("./graphs/logistic", sess.graph)
    sess.run(init)
    n_batches = int(MNIST.train.num_examples/batch)
    for i in range(n_ephs):  #  n_ephs times training
        for _ in range(n_batches):
            A_batch, B_batch = MNIST.train.next_batch(batch)
            sess.run([optimizer, loss], feed_dict={A: A_batch, B: B_batch})
    n_batches = int(MNIST.test.num_examples / batch)
    total_correct_preds = 0
    for i in range(n_batches):
        X_batch, Y_batch = MNIST.test.next_batch(batch)
        _, loss_batch, logits_batch = sess.run([optimizer, loss, logits],feed_dict={A: A_batch, B: B_batch})
        preds = tf.nn.softmax(logits_batch)
        correct_preds = tf.equal(tf.argmax(preds, 1), tf.argmax(B_batch, 1))
        accuracy = tf.reduce_sum(tf.cast(correct_preds, tf.float32))
        total_correct_preds += sess.run(accuracy)
    print ("Accuracy {0}".format(total_correct_preds/MNIST.test.num_examples))
