---
categories:
- null
date: 2022-06-28 19:22:05
tags:
- ctrl
- echo
- bin
- var
- path
title: ShellScript
---

> mac terminal 快捷键
>
> 1、将光标移动到行首：ctrl + a
>
> 2、将光标移动到行尾：ctrl + e
>
> 3、清除屏幕：       ctrl + l
>
> 4、搜索以前使用命令：ctrl + r
>
> 5、清除当前行：     ctrl + u
>
> 6、清除至当前行尾：  ctrl + k
>
> 7、单词为单位移动：option + 方向键

<!--more-->

# vim

## vim config

~/.vimrc

## 基本指令

i, a 插入

hjkl 左上下右

o 新增下一行 O 新增上一行

gg 第一行 G 最后一行

yy 复制当前行 yw 复制单词 p 粘贴 3p 粘贴三次

dd 删除当前行

. 重复前次操作

u 撤销前次操作

ctrl r 恢复前次操作

dw 删除单词 cw 改变单词

w 下个单词首部, e 下个单词尾部, b 上个单词首部

/ 搜索

:%s/old/new/g 全局替换

ci+括号 删除括号里的内容

ctrl u 向上翻页

ctrl d 向下翻页

f 查找

ctrl v 可视化块 d 删除

shift v 可视化行

# 文件

- ~/.bashrc: 提示文本, 颜色
- ~/.bash_history: 保存运行过的命令

# 概述

- ; 分隔命令

- 在Bash中，每一个变量的值都是字符串

  查看 QQ 进程的环境变量

  ```shell
   ps -p 8617 -wwwE # QQ
    PID TTY           TIME CMD
   8617 ??       243:33.14 /Applications/QQ.app/Contents/MacOS/QQ USER=akunda __CFBundleIdentifier=com.tencent.qq COMMAND_MODE=unix2003 LOGNAME=akunda PATH=/usr/bin:/bin:/usr/sbin:/sbin SSH_AUTH_SOCK=/private/tmp/com.apple.launchd.Anke8CUOPJ/Listeners SHELL=/bin/zsh HOME=/Users/akunda __CF_USER_TEXT_ENCODING=0x1F5:0x19:0x34 TMPDIR=/var/folders/7_/pnngkwkj0fj188s18w3rvx3w0000gn/T/ XPC_SERVICE_NAME=application.com.tencent.qq.115283210.115284637 XPC_FLAGS=1
  ```

  变量赋值

  ```shell
  var="value  ?" # 不要加空格!
  echo $var
  echo ${var}
  echo "we have a ${var}"
  echo "we have a $var"
  length=${#var} # 得到变量长度
  ```

  环境变量是未在当前进程中定义，而从父进程中继承而来的变量
  export命令用来设置环境变量。至此之后，从当前shell脚本执行的任何应用程序都会继承 这个变量。

  ```shell
  echo $PATH
  # $PATH /usr/local/apache-maven-3.6.3/bin
  export PATH="$PATH:/home/user/bin"
  
  PATH="$PATH:/home/user/bin"
  export PATH
  ```

  超级用户 UID=0

- echo
  ```shell
  echo "welcome\!"
  echo 'welcome!'
  echo welcome!
  
  printf  "%-5s %-10s %-4.2f\n" 1 Sarath 80.3456 
  
  echo -e "1\t2\t3" 
  #123
  
  ```

- 



































