import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def tensorflow_demo():
    '''
    TensorFlow的基本结构
    @return:
    '''
    # 原生python加法运算
    a = 2
    b = 5
    c = a + b
    print('普通加法运算的结果: %s' % c)
    # # TensorFlow实现加法运算（# 开启会话 tensorflow 2.0中已经取消了会话）
    # a_t = tf.constant(2)
    # b_t = tf.constant(5)
    # c_t = a_t + b_t
    # print('TensorFlow加法运算的结果:%s' % c_t)
    # 开启会话
    with tf.compat.v1.Session() as sess:
        a_t = tf.constant(2)
        b_t = tf.constant(5)
        c_t = a_t + b_t
        c_t_value = sess.run(c_t)
        print("c_t_value: %s" % c_t_value)






if __name__=='__main__':
    tensorflow_demo()
