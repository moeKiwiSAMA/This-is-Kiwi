---
layout: post
title: "曝光：光圈值、快门与ISO"
date: 2020-02-20 11:43:00 +0800
categories: technology
tags: shoot
img: https://static.kiwi.cat/images/animals.jpg


---

简单地描述什么是曝光

<!-- Mathjax Support -->
<!-- 请允许js执行 -->

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

## 曝光

曝光能直接决定胶片或传感器的光量，通俗地，可以理解为照片在观感上的亮度。

相同环境下，曝光由`光圈值大小`、`快门（曝光时间）`、`ISO（感光度）`决定，且这三个因素都与照片曝光成正相关。

| 影响因素                   | 曝光变化 | 变化程度                    |
| -------------------------- | -------- | --------------------------- |
| 光圈值越大（f/后的值越小） | 曝光越强 | $$\log_{2}{n}$$             |
| 快门越慢（曝光时间越长）   | 曝光越强 | $$\log_{2}{n}$$             |
| ISO越大（感光度越大）      | 曝光越强 | $$\log_{2}{\frac{n}{100}}$$ |

但是，由于调整这三个参数中的任意一个值都会引发一些副作用，所以，当我们希望提升照片的曝光时，并`不应该单一地调整`其中任意因素。

## 光圈

光圈值越大，进光量越大，曝光越强。

光圈值（N=f/D）大小不是指物理上拿尺子量那个孔的口径大小，而是由镜头的焦距和光圈口径共同决定的（焦距/口径），一般以`f/D`来表示，例如f/1.8，f/4，由于D在分母的位置，D值越大，光圈值（N）越小，所以，`f/1.8`的光圈比`f/4` `大`得多。

<div style="margin:auto 0;text-align:center">
<img style="display: inline-block;width:80%" src="https://static.kiwi.cat/images/Lenses_with_different_apetures.jpg">
</div>



提升光圈所带来的影响不仅仅是提升曝光，同时还会带来景深的改变。

景深程度也就是背景虚化的程度，景深越浅，背景虚化程度越强烈，这种感觉能带来非常强烈的视觉冲击，大光圈的镜头也成为了许多摄影爱好者追随的梦想。

<div style="margin:auto 0;text-align:center">
<img style="display: inline-block;width:40%" src="https://static.kiwi.cat/images/TO-KILL-A%20Mockingbird-f1.8.jpg" alt="f/1.8">
<img style="display: inline-block;width:40%" src="https://static.kiwi.cat/images/TO-KILL-A%20Mockingbird-f9.jpg" alt="f/9">
</div>

可见f/1.8（左图）的背景虚化效果比f/9（右图）强烈许多。（已经调整其他参数使得曝光基本相同）

| 光圈值 | 数字上的分母 | 景深 | 背景虚化 |
| ------ | ------------ | ---- | -------- |
| 大     | 小           | 浅   | 强烈     |

## 快门速度

快门速度决定曝光时间，也就是传感器或胶片接触到光源的时间，以`秒`作为单位，通常我们见到的1/60，1/3000基本都是指曝光的时间。

胶卷相机的快门速度一般由物理的快门控制，而数码相机一般由`电子前帘`控制，当你打开了电子前帘快门时，物理的快门几乎是个装饰品，由于这一特性，索尼的A7M3也能做到静音拍摄。
当然你也可以手动关闭电子前帘。

<div style="margin:auto 0;text-align:center">
<img style="display: inline-block;width:40%" src="https://static.kiwi.cat/images/SteadyShot-Manual.png" alt="Sony SteadyShot Menu In Manual">
</div>

一般情况下，当我们想要控制曝光程度时，优先考虑的因素就是快门速度，但是快门速度也会带来副作用——拖影。

<div style="margin:auto 0;text-align:center">
<img style="display: inline-block;width:40%" src="https://static.kiwi.cat/images/UFO-1.5000.jpg" alt="f/1.8">
<img style="display: inline-block;width:40%" src="https://static.kiwi.cat/images/UFO-1.60.jpg" alt="f/9">
</div>

左：1/5000，右1/60  
很明显地可以看到，右侧图片出现了拖影。

## ISO

ISO表示感光度，代表了胶卷或传感器对光的敏感程度。一般我们所说的ISO100、ISO3200就表示感光度，在相同的快门速度与光圈大小之下，感光度`越高`，照片曝光`越强`。

<div style="margin:auto 0;text-align:center">
<img style="display: inline-block;width:40%" src="https://static.kiwi.cat/images/HIGH-ISO.jpg" alt="ISO 800">
<img style="display: inline-block;width:40%" src="https://static.kiwi.cat/images/LOW-ISO.jpg" alt="ISO 200">
</div>

左侧的照片是在ISO 800下拍摄<!--截图-->的，右侧的照片则为ISO 500。

`提升`ISO对整体曝光的`提升`是明显且直观的，不过，过高的ISO也会引发一些副作用——噪点明显增加。



<div style="margin:auto 0;text-align:center">
<img style="display: inline-block;width:40%" src="https://static.kiwi.cat/images/HIGH-ISO.jpg" alt="ISO 800">
<img style="display: inline-block;width:40%" src="https://static.kiwi.cat/images/BLOWUP-ISO.jpg" alt="ISO 32800">
</div>

左侧的照片是在ISO 800下拍摄<!--截图-->的，右侧的照片则为ISO 1280000，为了使右侧图片的曝光基本与左侧相同，拍摄时降低了一些快门速度，在右侧图片中能看到`明显的噪点`。

## 如何平衡这三个参数
