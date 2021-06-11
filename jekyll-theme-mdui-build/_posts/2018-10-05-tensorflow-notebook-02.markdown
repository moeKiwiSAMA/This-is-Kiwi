---
layout: post
title: "Tensorflow学习笔记(二) 利用梯度下降解决线性回归问题"
date: 2018-10-08 00:09:09 +0800
categories: technology
tags: tensorflow
img: "https://i.jpg.dog/img/43ffd87d244667422ca12ece5ab511d5.png"
---
说人话就是猜一次函数

## 安装需要使用到的库
```
pip3 install matplotlib numpy
```
然后打开IDE导入
```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

```
## 采集数据
### 生成数据
如果咱要猜一个线性函数 y = Wx + b ,那咱要给它喂数据吧,比如咱给它100个点
```python
points = []

for i in range(100):
    x1 = np.random.normal(0.0, 0.66)    # 生成 x
    y1 = 0.1 * x1 + 0.2 + np.random.normal(0.0, 0.04)   # 生成 y ,让 y = 0.1 * x + 0.2 + 噪声
    points.append([x1,y1])  # 把点给append到列表
```
把points这个列表里的遍历到x_data与y_data,让它们一一对应
```python
x_data = [v[0] for v in points]
y_data = [v[1] for v in points]
```
### 显示原始数据
```python
plt.plot(x_data, y_data, 'r*', label="Origional data")  # 用plt把点部署上去,用red色的*符号表示,并标注其为Origional data
plt.title("Liner Regression using Gradient Descent")    # 给plt起一个标题
plt.legend() # 标注
plt.show()   # 显示
```
## 建立模型
```python
W = tf.Variable(tf.random_uniform([1], -0.1, 1.0))  # 生成一个一维的张量W,这个变量的最小值为-0.1,最大值为1.0
b = tf.Variable(tf.zeros([1]))  # 创建一个全零的一维张量b
y = W * x_data + b # 定义这个线性函数模型

loss = tf.reduce_mean(tf.square(y-y_data))  # 计算lost(预期y-训练算出来的y)
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 使用梯度下降优化器来学习,里面的参数越小,学习越慢,但是好像会变精确
train = optimizer.minimize(loss)    # 用最小化loss的梯度下降优化器学习
```
## 建立会话
```python
sess = tf.Session() # 创建会话
```
## 训练过程
```python
sess.run(tf.global_variables_initializer())  # 初始化变量
for step in range(20):  # 20步打印一次结果
    sess.run(train)     # 训练
    print((step,sess.run(loss),sess.run(W),sess.run(b)))    # 20步打印一次结果

plt.plot(x_data, y_data, 'r*', label="Origional data")   # 用plt把点部署上去,用red色的*符号表示,并标注其为Origional data
plt.title("Liner Regression using Gradient Descent")    # 给plt起一个标题
plt.plot(x_data,sess.run(W) * x_data + sess.run(b),label="Fitted line") # 把训练出来的线标上去
plt.legend()    # 标注
plt.xlabel('x') # 把横轴标为x
plt.ylabel('y') # 把纵轴标为y
plt.show()      # 显示图
sess.close()    # 关闭会话
```
