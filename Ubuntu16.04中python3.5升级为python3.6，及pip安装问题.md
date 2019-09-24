# Ubuntu16.04中python3.5升级为python3.6，及pip安装问题



---

最近在配置阿里云ECS服务器的时候，我想安装一些库，结果安装到matplotlib库时发现，python版本有点低，需要升到3.6，于是开始了升级。
首先需要输入如下四条命令：

    apt-get install software-properties-common
    add-apt-repository ppa:jonathonf/python-3.6
    apt-get update
    apt-get install python3.6

此时python3的版本还是3.5，我们需要改下软链接
使用which命令来查找python3的快捷键的路径


进入cd /usr/bin/，删除并创建新的软链接

    rm python3
    ln -s python3.6 python3
之后，在查看版本后就是3.6了。
安装好3.6版本后，第一件事情就是安装pip3了，
很简单的命令：

    apt-get install python3-pip

如果出现以下问题：
    from pip import main
    ImportError：cannot import name 'main'
就输入vi /usr/bin/pip3命令
将原来的：

    from pip import main
    if __name__ == '__main__':
        sys.exit(main())

改为如下：

    from pip import __main__
    if __name__ == '__main__':
        sys.exit(__main__._main())

若还出现这种问题：



就输入如下两条命令：

     wget https://bootstrap.pypa.io/get-pip.py  --no-check-certificate
     python3 get-pip.py


