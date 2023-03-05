---
categories:
- program
date: 2019-11-18 00:04:35
password: null
tags:
- git
- 截屏2020
- commit
- objects
- txt
title: git
---

> git 简介和使用

<!--more-->

## git 命令

- `git status (-s)`

  ```shell
  $ vim CONTRIBUTING.md 
  $ git status 
  On branch master 
  Changes to be committed:   
  		(use "git reset HEAD <file>..." to unstage)
      new file:   README     
      modified:   CONTRIBUTING.md
  Changes not staged for commit:   
  (use "git add <file>..." to update what will be committed)   
  (use "git checkout -- <file>..." to discard changes in working directory)
      modified:   CONTRIBUTING.md
  
  ```

- `git rm (--cached)`
- `git config --global alias.last 'log -1 HEAD'`



## git 分支

- 提交对象

  首次提交

  ![截屏2020-07-24 下午11.04.55](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2gnf7ccej31gg0rgn6i.jpg)

  以后的提交

  ![截屏2020-07-24 下午11.05.31](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2go0zfo9j31cc0g0ai4.jpg)

- Git 的分支，其实本质上仅仅是指向提交对象的可变指针。

-  **HEAD** 的特殊指针。在 Git 中，它是一个指针，指向当前所在的本地分支（译注：将 HEAD 想象为当前分支的别名）。

  ![截屏2020-07-24 下午11.19.33](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2h2mi8nrj31d20t278e.jpg)

### 合并

- fast-forward

  ![截屏2020-07-24 下午11.32.26](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2hg1iq2ej31f00mcwi3.jpg)

  ```shell
  $ git checkout master
  $ git merge hotfix 
  Updating f42c576..3a0874c
  Fast-forward 
  index.html | 2 ++ 
  1 file changed, 2 insertions(+)
  ```

  直接指针右移, 没有需要解决的冲突

- 分支之间的合并

![截屏2020-07-24 下午11.34.27](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2hi4e4pqj31dw0iugqd.jpg)

和之间将分支指针向前推进所不同的是，Git 将此次三方合并的结果做了一个新的快照并且自动创建一个新的提 交指向它。这个被称作一次合并提交，它的特别之处在于他有不止一个父提交。

![截屏2020-07-24 下午11.37.40](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2hlh6lc1j31c40ekjti.jpg)

### 解决冲突

如果你在两个不同的分支中，对**同一个文件的同一个部分**进行了不同的修 改，Git 就没法干净的合并它们。

![截屏2020-07-24 下午11.41.53](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2hpueb36j30q20cmqid.jpg)

![截屏2020-07-24 下午11.45.31](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2htn2dnqj306i04omxm.jpg)

在你解决了所有文件里的冲突之后，对每个文件使用 git add 命令来将其标记为冲突已解决。一旦暂存这 些原本有冲突的文件，Git 就会将它们标记为冲突已解决。

### 远程分支

- git clone

![截屏2020-07-24 下午11.56.55](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2i5i6y9yj31650u0tgx.jpg)

- git fetch

![截屏2020-07-24 下午11.57.54](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2i6jmqxmj315f0u07bt.jpg)

- git pull = git fetch + git merge

  ![截屏2020-07-25 上午1.55.11](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2lkjp3oqj31bk0s0wkh.jpg)

  git fetch, git merge

![截屏2020-07-25 上午1.55.46](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2ll5j1dhj31cw0km0xh.jpg)

​		git push

​		![截屏2020-07-25 上午1.56.21](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2lltvxjaj31aq0g4q7h.jpg)

​		

- rebase

  与 git merge 不同, 其实，还有一种方法：你可以提取在 C4 中引入的补丁和修改，然后在 C3 的基础上再应用一次。在 Git 中，这种 操作就叫做 变基。**你可以使用 rebase 命令将提交到某一分支上的所有修改都移至另一分支上，就好像“重新 播放”一样。**

  它的原理是首先找到这两个分支（即当前分支 experiment、变基操作的目标基底分支 master）的最近共同祖 先 C2，然后对比当前分支相对于该祖先的历次提交，提取相应的修改并存为临时文件，然后将当前分支指向目 标基底 C3, 最后以此将之前另存为临时文件的修改依序应用。

  ![截屏2020-07-25 上午1.07.41](https://tva1.sinaimg.cn/large/007S8ZIlly1gh2k75saijj31ds0e0jtx.jpg)

  变基使得提交历史更加整洁

## git 工具

- git show SHA-1 

## git 内部原理

### git 基础

**工作区**

电脑里能看到的目录

**版本库**

.git

其中包含了 **stage/index** 暂存区, 即 git add 操作

![截屏2020-07-31 下午3.29.01](https://tva1.sinaimg.cn/large/007S8ZIlly1gha6tcriipj30rg0duaf6.jpg)



### git 数据库

**.git 文件**

```
$ ls -F1
HEAD
config*
description
hooks/
info/
objects/
refs/
```

description gitweb 程序使用, 无需关心

config 配置

info 包含一个全局性排除文件

hooks 包含客户端或服务端的钩子脚本

objects 存储所有数据内容

refs 存储指向数据(分支)的提交对象的指针

HEAD 只是目前被检出的分支

index 保存暂存区信息

**objects**

### 数据对象

- git init 用于创建一个空的git仓库，或重置一个已存在的git仓库

- git hash-object git底层命令，用于向Git数据库中写入数据

  ```shell
  $ echo "version 1" | git hash-object -w --stdin
   83baae61804e65cc73a7201a7252750c76066a30
  $ find .git/objects/ -type f
  .git/objects/83/baae61804e65cc73a7201a7252750c76066a30
  ```

  ```shell
  $ echo "version 1" > file.txt
  $ git hash-object -w file.txt
  83baae61804e65cc73a7201a7252750c76066a30
  ```

  

- git cat-file git底层命令，用于查看Git数据库中数据

  ```shell
   $ git cat-file -p 83baa
   version 1
  ```

- 问题: 

  第一，无法记录文件名的变化；

  第二，无法记录文件夹的变化；

  第三，记忆每一个版本对应的hash值无聊且乏味且不可能；

  第四，无法得知文件的变更时序；

  第五，缺少对每一次版本变化的说明。

### 树对象

Git利用树对象（tree object）解决文件名保存的问题，树对象也能够将多个文件组织在一起。

- git update-index git底层命令，用于创建暂存区
- git ls-files --stage git底层命令，用于查看暂存区内容
- git write-tree git底层命令，用于将暂存区内容写入一个树对象

前两个命令都是对暂存区操作, 第三个则会在 objects 里创建一个树对象

```shell
$ find .git/objects -type f
.git/objects/1f/7a7a472abf3dd9643fd615f6da379c4acb3e3a
.git/objects/83/baae61804e65cc73a7201a7252750c76066a30
$ git update-index --add file.txt
$ find .git/objects/ -type f
.git/objects/1f/7a7a472abf3dd9643fd615f6da379c4acb3e3a
.git/objects/83/baae61804e65cc73a7201a7252750c76066a30
$ git write-tree
391a4e90ba882dbc9ea93855103f6b1fa6791cf6
$ find .git/objects/ -type f
.git/objects/39/1a4e90ba882dbc9ea93855103f6b1fa6791cf6
.git/objects/1f/7a7a472abf3dd9643fd615f6da379c4acb3e3a
.git/objects/83/baae61804e65cc73a7201a7252750c76066a30
```

查看内容

```shell
$ git cat-file -t 391a4e # -t 类型
tree
$ git cat-file -p 391a4e # -p 内容
100644 blob 83baa...    file.txt  
```

### commit 对象

commit对象能够帮你记录什么时间，由什么人，因为什么原因提交了一个新的版本，这个新的版本的父版本又是谁。

- git commit-tree git 底层命令, 用来创建提交对象

```shell
$ git write-tree
cb0fbcc484a3376b3e70958a05be0299e57ab495

$ git commit-tree cb0fbcc -m "first commit"
7020a97c0e792f340e00e1bb8edcbafcc4dfb60f

$ git cat-file 7020a97
tree cb0fbcc484a3376b3e70958a05be0299e57ab495
author john <john@163.com> 1537961478 +0800
committer john <john@163.com> 1537961478 +0800

first commit
```



## git 工作原理

![img](https://pic2.zhimg.com/80/v2-3bc9d5f2c49a713c776e69676d7d56c5_1440w.jpg)

Workspace：工作区
Index / Stage：暂存区
Repository：仓库区（或本地仓库）
Remote：远程仓库



## 初次使用 git

```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

git config 一个用来配置 git 的工具

--global 默认全局, 如果要针对特定 git 仓库修改, 不要使用 global



1.git 回退

```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")
```



你可以发现，Git会告诉你，`git checkout -- file`可以丢弃工作区的修改：

```
$ git checkout -- readme.txt
```

总之，就是让这个文件回到最近一次`git commit`或`git add`时的状态。

2. Git同样告诉我们，用命令`git reset HEAD <file>`可以把暂存区的修改撤销掉（unstage），重新放回工作区：

```
$ git reset HEAD readme.txt
Unstaged changes after reset:
M	readme.txt
```

3. -u参数：关联本地分支和远程分支

4. git merge $branch_name 如果有冲突要手动解决(一般是两个分支有不同的提交内容)

5. git branch -d $branch_name 删除分支

6. git rm --cached $doc_name    删除文件（会影响到远程

7. git branch --set-upstream-to=origin/$name

8. git branch -vv     查看本地分支和远程分支的对应关系

9. git pull <远程主机名> <远程分支名>:<本地分支名>

10. fatal: refusing to merge unrelated histories

    --allow-unrelated-histories

11. CRLF和LF

    [参考网站](https://blog.csdn.net/ccfxue/article/details/52625806)

    crlf：carriage return line feed回车换行

    lf：line feed 换行

    reason：

    When you view changes in a file, Git handles line endings in its own way.Since you're collaborating on projects with Git and GitHub, Git mightproduce unexpected results if, for example, you're working on a Windows machine,and your collaborator has made a change in OS X.

    CRLF->Windows-style

    LF->Unix Style

    CR->Mac Style

    CRLF表示句尾使用回车换行两个字符(即我们常在Windows编程时使用"\r\n"换行)

    LF表示表示句尾，只使用换行.

    CR表示只使用回车.

# 