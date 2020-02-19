---
layout: post
title: "记一次在Manjaro-KDE安装ibus-rime的经历"
date: 2018-09-19 10:24:49 +0800
categories: technology
tags: ibus rime manjaro kde archlinux
img: https://rime.im/images/home-title.svg
---
> 想必大部分Manjaro用户都是属于想要使用aur，想要使用一切Arch Linux拥有的东西但是又懒于安装Arch Linux的人群
但是如果要在安装输入法上折腾半个小时，那就感觉非常亏了。


## RIME中州韵输入法引擎
[RIME](https://rime.im/)真的是非常棒的一个东西了，应该是目前最优的一种选择。之前看见有人在Linux上使用[搜狗拼音输入法](https://pinyin.sogou.com/linux/?r=pinyin)，因为它安装起来非常方便，RIME的话也许会稍微复杂一点点。



## 我需要安裝哪些东西？
如果要安装[RIME](https://rime.im/)的话，一般有[两种选择](https://wiki.archlinux.org/index.php/Rime)，一种是[fcitx-rime](https://www.archlinux.org/packages/community/x86_64/fcitx-rime/)，还有一种是[ibus-rime](https://www.archlinux.org/packages/community/x86_64/ibus-rime/)，我在这里选择了[ibus](https://wiki.archlinux.org/index.php/IBus_(%E6%AD%A3%E9%AB%94%E4%B8%AD%E6%96%87))而不是过气[fcitx](https://wiki.archlinux.org/index.php/Fcitx_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))。

那么需要安装的当然就是[ibus-rime](https://www.archlinux.org/packages/community/x86_64/ibus-rime/)了。

首先你需要[yaourt](https://archlinux.fr/yaourt-en)或者[pacaur](https://aur.archlinux.org/packages/pacaur/)，
[pacaur](https://aur.archlinux.org/packages/pacaur/)的安装应该大部分人都会吧。
```bash
sudo pacman -S pacaur
```
然后再使用Aur安装[ibus-rime](https://www.archlinux.org/packages/community/x86_64/ibus-rime/)。
```bash
pacaur -S ibus-rime
```
由于还需要修改文本，所以我们需要安装一个文本编辑器，这里使用[vim](https://wiki.archlinux.org/index.php/vim)，安裝[vim](https://wiki.archlinux.org/index.php/vim)也应该是大部分都会的事。
```bash
sudo pacman -S vim
```

## 安装完成后需要干什么？
打开终端，输入
```bash
ibus-setup
```
选择输入法（input）>添加（Add）>汉语(Chinese)>Rime
这样就可以在[ibus](https://wiki.archlinux.org/index.php/IBus_(%E6%AD%A3%E9%AB%94%E4%B8%AD%E6%96%87))中添加[RIME](https://rime.im/)了，然后我们需要export三个变量  
GTK_IM_MOUDLE XMDIFIERS QT_IM_MOUDL  并且在开机的时候启动[ibus-rime](https://www.archlinux.org/packages/community/x86_64/ibus-rime/)。
我们使用[vim](https://wiki.archlinux.org/index.php/vim)来编辑~/.xprofile，也许这个文件会不存在，不要紧，直接干。
```bash
vim ~/.xprofile
```
然后在里面添加这些东西
```bash
export GTK_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT_IM_MODULE=ibus
ibus-daemon -x -d
```
ESC :x 保存退出 （[不会使用vim的人可以在这里速成](https://learnxinyminutes.com/docs/zh-cn/vim-cn/)）

注销账户重新登录以后就能正常使用[RIME](https://rime.im/)了

## 一些操作
默认切换到[RIME](https://rime.im/)按```Super + Space ```，也就是```Win + 空格```

在[RIME](https://rime.im/)內切换不同的输入法```Ctrl + ` ```
更多操作可以查阅官方[doc](https://rime.im/docs)
