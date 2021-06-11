---
layout: post
title: "Tensorflow学习笔记(一) 新的开始"
date: 2018-10-05 00:09:09 +0800
categories: technology
tags: tensorflow
img: "https://i.jpg.dog/img/7082a29eebab8ad6e6e82b2bfd14f3d1.jpg"
---
首先,人工智能是DSSQ,各种意义上的


## Preparation
### Tensorflow开发环境的部署
首先需要[Python3](https://www.python.org/)(最好能3.6.x,暂不支持3.7)),简单粗暴一点的话再写入系统的PATH,然后使用pip安装[tensorflow](https://www.tensorflow.org/install/)
```
pip3 install tensorflow
```
如果要用老黄的显卡的话,先要装CUDA,咱用的是 ~~CPU~~ [CUDA9.2](https://developer.nvidia.com/cuda-92-download-archive),下载完CUDA一直下一步安装什么都不用管
```
pip3 install tensorflow-gpu
```
没了,就这么简单
## Hello,World
```python
import tensorflow as tf     # 用脚想都知道要把tensorflow给import进来
greeting = tf.constant("Hello,World!")      # 创建一个tf常量
sess = tf.Session()     # 创建一个会话
print(sess.run(greeting))       # 运行这个会话并打印greeting的值
sess.close      # 关闭会话防止地球温室效应
```
打印结果
```
Hello,World
```
如果直接print(greeting)的话会输出greeting这个张量的信息
```python
Tensor("Const:0", shape=(), dtype=string)
```
所有要print出值的东西如果直接print那个变量的话,只会print出张量的信息而不是那个值
```python
tf.Variable()
tf.constant()
tf.placeholder()
```
都是这样.Variable就是变量constant就是常量,有点变成基础的人都能理解,placeholder是占位符,你可以先给他定着不去管他(应该).

tensorflow不完全是个机器学习框架但是大部分人都把它当机器学习框架,所以说如果你吃饱了撑得也可以把它当作什么四则运算的库之类的.
```python
num1 = tf.Variable(10)
num2 = tf.Variable(20)

num3 = tf.add(num1, num2)
num4 = tf.subtract(num1, num2)
num5 = tf.multiply(num1, num2)
num6 = tf.div(num1 ,num2)
```
建立一个会话
```python
sess = tf.Session()
sess.Close()
```
或者直接用with也行
```python
nmsl = tf.constant("NMSL")
with tf.Session() as sess:
    print(sess.run(nmsl))
```
要print出结果的话要这样玩
```python
print(sess.run(num1), sess.run(num2), sess.run(num3), sess.run(num4) ,sess.run(num5) ,sess.run(num6))
```
你也可以吃饱了没事干用tensorflow来算矩阵而不是用np
```python
ma1 = tf.constant([[1., 1.]])   # 一行两列的矩阵
ma2 = tf.constant([[1.], [1.]])   # 两行一列的矩阵
result = tf.matmul(ma1, ma2)
```
sess.run(result)如果不是2的话我把鼠标吃下去
