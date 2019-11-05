# Django框架学习(1)

标签（空格分隔）： Django

---

  刚刚了解了Flask框架后就开始进行Django框架的学习了。作为Web框架重量级选手之一，Django由纯Python编写，它采用了MVC的软件设计模式，也即模型M(Model),视图V(View)和控制器C(Controller)。

需要注意的是，Django和Python有对应的版本关系：
Django | Python
-------|--------
1.8|2.7,3.2,3.3,3.4,3.5
1.9,1.10|2.7,3.4,3.5
1.11|2.7,3.4,3.5,3.6
2.0|3.4,3.5,3.6,3.7
2.1,2.2|3.5,3.6,3.7

我使用的Pyhton版本是3.6，Django版本是2.2
具体的安装过程就不叙述了，我直接在pycharm里安装了。。

当然需要配置一下系统环境变量：
![系统环境变量](https://img-blog.csdnimg.cn/20190726132500802.png)
E:\software\Python\Anaconda\Scripts\
E:\software\Python\Anaconda\Lib\site-packages\django\bin
主要目的就是使用bin目录下的django-admin.py文件来创建工程


然后我们来实践一下吧
输入：django-admin startproject [yourSitename]


如果输入的是django-admin.py则运行失败，当然你要把py后缀的文件的打开方式都改为python.exe。

运行成功后，会在当前目录产生一个工程：
·
|--site1
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   ·-- wsgi.py
·-- manage.py

 - site1:工程的容器
 - manage.py:一个实用的命令行工具，可以使用各种方式于该Django工程进行交互
 - sit1/__init__.py:空文件，告诉python该目录是一个python包
 - site1/settings.py:该工程的配置
 - site1/urls.py:该工程的URL声明；一份由Django驱动的网站“目录”
 - 一个WSGI兼容的Web服务器的入口，以便运行工程

        注WSGI：Web Server Gateway Interface(Web服务器网关接口，WSGI)已经被用作Python Web应用程序开发的标准。
  
  