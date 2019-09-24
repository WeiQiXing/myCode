# Django框架学习(2)

标签（空格分隔）： Django

---

经过几天的学习和摸索，我尝试在阿里云服务器ECS上搭建了一个自己的小网站，因为还没有购买域名，所以现在只能通过网络地址来找。

工程目录总结构
·
|--mysite
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- view.py
|   |-- testdb.py
|   ·-- wsgi.py
|--static
|   |-- css
|   |-- fonts
|   |-- img
|   |-- js
|--templates
|   |-- about.html
|   |-- index.html
|   |-- inner.html
|   |-- introduction.html
|   |-- contact.html
·-- manage.py

 - mysite:工程的容器
 - manage.py:一个实用的命令行工具，可以使用各种方式于该Django工程进行交互
 - mysite/__init__.py:空文件，告诉python该目录是一个python包
 - mysite/settings.py:该工程的配置
 - mysite/urls.py:该工程的URL声明；一份由Django驱动的网站“目录”
 - mysite/wsgi.py:一个WSGI兼容的Web服务器的入口，以便运行工程
 - mysite/view.py:视图文件,MVC中的V
 - mysite/testdb.py:用于测试数据库的，使用的是SQLite3数据库
 - static/文件下的是一些CSS、字体、图片以及JS的文件夹
 - templates/内的文件都是html模板



在本地编写好文件后可以通过WinSCP传输到服务器端，再通过putty连接服务器。

    cd mysite
    python3 manage.py runserver 0.0.0.0:8000


注：127.0.0.1是一个环回地址，不代表“本机”，0.0.0.0才是真正表示“本网络中的本机”，一般在服务器绑定端口的时候都选择绑定到0.0.0.0，这样可以通过多个IP地址访问，如果是127.0.0.1的话，其他的IP不能够访问服务。此外，localhost是一个域名，对应于127.0.0.1


用python3 manage.py runserver 0.0.0.0:8000命令运行django程序后，通过浏览器访问服务器网址的8000端口，出现访问错误，报错为 
Invalid HTTP_HOST header: ‘xxx.xx.xxx.xxx:8000’. You may need to add ‘xxx.xx’ to ALLOWED_HOSTS

解决办法： 
修改创建项目时生成的setting.py文件
将ALLOWED_HOSTS = []改为ALLOWED_HOSTS = ['*']

再次运行即可成功访问。


