<!-- TOC -->

- [Docker](#docker)
    - [Docker的应用场景](#docker的应用场景)
    - [Docker 架构](#docker-架构)
    - [CentOS Docker  安装过程](#centos-docker--安装过程)
    - [docker Debian 安装过程](#docker-debian-安装过程)
    - [理解镜像(images)和容器(containers)](#理解镜像images和容器containers)
        - [搜索&运行whalesay镜像](#搜索运行whalesay镜像)
    - [控制Docker服务：](#控制docker服务)
    - [docker 常见命令](#docker-常见命令)
    - [构建自己的镜像](#构建自己的镜像)
    - [上传镜像到dockerhub](#上传镜像到dockerhub)
        - [linux](#linux)

<!-- /TOC -->


#  Docker
Docker 是一个开源的应用容器引擎。Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

##  Docker的应用场景
1. Web 应用的自动化打包和发布。
2. 自动化测试和持续集成、发布。
3. 在服务型环境中部署和调整数据库或其他的后台应用。
4. 从头编译或者扩展现有的OpenShift或Cloud Foundry平台来搭建自己的PaaS环境

## Docker 架构
1. Docker 使用客户端-服务器 (C/S) 架构模式，使用远程API来管理和创建Docker容器。
2. Docker 容器通过 Docker 镜像来创建。
3. 容器与镜像的关系类似于面向对象编程中的对象与类

## CentOS Docker  安装过程
1. 检查CentOS版本，Docker 要求 CentOS 系统的内核版本高于 3.10。uname -r 命令查看你当前的内核版本。
2. Docker有两个版本：Docker CE 和 Docker EE。其中Docker EE为企业版，需收费
3. 安装Docker CE 正式开始：
    
    1. yum install docker-ce 安装docker
    2. docker来测试一下HelloWorld，通过输入docker pull hello-world来拉取hello-world镜像
    3. 输入docker images 查找仓库，确定仓库拉取到了HelloWorld的镜像，接下来我们来运行一下，通过输入docker run hello-world
        >
            Hello from Docker!
            This message shows that your installation appears to be working correctly.

            To generate this message, Docker took the following steps:
            1. The Docker client contacted the Docker daemon.
            2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
                (amd64)
            3. The Docker daemon created a new container from that image which runs the
                executable that produces the output you are currently reading.
            4. The Docker daemon streamed that output to the Docker client, which sent it
                to your terminal.

            To try something more ambitious, you can run an Ubuntu container with:
            $ docker run -it ubuntu bash

            Share images, automate workflows, and more with a free Docker ID:
            https://hub.docker.com/

            For more examples and ideas, visit:
            https://docs.docker.com/engine/userguide/
        出现上面所示的内容则说明hello-world运行成功

## docker Debian 安装过程
1. 设置Docker存储库：安装在软件包下面以使“ apt ”获得https方法的支持。

        sudo apt-get update
        sudo apt-get install -y apt-transport-https ca-certificates wget software-properties-common

2. 鉴于国内网络问题，强烈建议使用国内源，官方源请在注释中查看。为了确认所下载软件包的合法性，需要添加软件源的 GPG 密钥。

        $ curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/debian/gpg | sudo apt-key add -


        # 官方源
        # $ curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
3. 通过在终端中运行以下命令将官方Docker存储库添加到系统。

        echo“deb [arch = amd64https://download.docker.com/linux/debian $（lsb_release -cs）stable”| sudo tee -a /etc/apt/sources.list.d/docker.list
        将这段代码注释（#）掉
4. 更新apt数据库。

        sudo apt-get update

5. 配置镜像加速器 
        
通过修改daemon配置文件/etc/docker/daemon.json（没有时新建该文件）来使用加速器：

        
    {
        "registry-mirrors": ["https://registry.docker-cn.com"]
    }
    该代码必须符合json的格式
然后之后重新启动服务。

    systemctl daemon-reload
    systemctl restart docker
检查加速器是否生效配置加速器之后，如果拉取镜像仍然十分缓慢，请手动检查加速器配置是否生效，在命令行执行 docker info，如果从结果中看到了如下内容，说明配置成功。

    Registry Mirrors:
    https://registry.docker-cn.com/

6. 安装docker-ce

    question1：现在没有可用的软件包vim，但是它被其它的软件包引用了&gcc命令无法使用。解决方法需要换源，在更新vim。参考文件：https://blog.csdn.net/gsh_hello_world/article/details/70227852

    question2：没有可用的软件包 docker-ce，但是它被其它的软件包引用了。这可能意味着这个缺失的软件包可能已被废弃，或者只能在其他发布源中找到。 
   
    解决方法：用阿里云或者DaoCloud 的安装脚本，来安装docker-ce

        curl -sSL https://get.daocloud.io/docker | sh
7. 在测试docker 是否安装成功
    
    docker run hello-word


## 理解镜像(images)和容器(containers)
1. 镜像的功能基于它是如何构建的, 一个镜像可以运行一个简单的 独立的命令, 然后退出. 这就是hello-world所做的事情.
2. 镜像是运行在容器中的, 和硬件无关. 只要一个镜像可以在一个容器中运行,那么把这个镜像分享出来,可以在任何一个Docker容器中运行. 镜像可以通过个人的需要定制不同的镜像。一个人Ubuntu镜像中安装一个mysql, 另外一个人在Ubuntu镜像中安装了Apache, 这就是两个镜像, 不同的人根据不同的需要下载不同的镜像. 然后把镜像运行在自己电脑的容器中即可


### 搜索&运行whalesay镜像
1. 输入命令docker run docker/whalesay cowsay boo然后回车
终端所示即为下面的样子
>    _____ 
    < boo >
    ----- 
        \
        \
        \     
                        ##        .            
                ## ## ##       ==            
            ## ## ## ##      ===            
        /""""""""""""""""___/ ===        
    ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~   
        \______ o          __/            
            \    \        __/             
            \____\______/   

>第一次再运行镜像时, Docker命令会在本地查找是否存在这个镜像. 如果镜像不存在, Docker会从Docker Hub中下载这个镜像
2. docker images并按回车. 这个命令会列出你本地系统中的所有镜像
   再运行一个镜像在容器中时, Docker下载这个镜像到你的计算机中, 这个本地的镜像复制会节省你到时间. Docker只会在镜像在Docker Hub上发生变化时才会再次下载. 
## 控制Docker服务：
1. 要启动Docker，请运行：

    sudo systemctl start docker
2. 要停止Docker服务，请运行：

    sudo systemctl stop docker
3. 要重新启动Docker服务，请运行：

    sudo systemctl restart docker
4. 要检查Docker服务的状态，请运行：

    sudo systemctl status docker
5. 要使Docker服务在系统引导时自动启动，请运行：

    sudo systemctl enable docker
## docker 常见命令
1. 进入容器：

    docker exec -it 镜像ID /bin/bash
2. 退出容器：

    exist
3. 查看正在运行的镜像容器

    docker ps
4. 在后台运行镜像

    docker run -d 镜像ID
5. 停掉镜像

    docker stop 镜像ID
6. 设置容器对应的端口

    docker run -d -p 主机端口:容器端口 镜像ID
注：-d为设置该镜像在后台运行 -p小写p，为设置对应的端口映射关系，如果是大写的P，则不需要设置对应的端口映射关系，docker随机获取主机的端口和容器端口进行映射（docker run -d -P 镜像ID） 
7. 查看端口使用情况：

    netstat -na|grep 端口号
8. 删除镜像
    
    docker rmi -f 镜像ID
注：-f的作用是强制删除该镜像

## 构建自己的镜像
在这边出现了很大的问题：
1. 参考苏金鹏写的dockerfile的信息，进行尝试修改，安装还在进行，没有创建完成自己的镜像。
## 上传镜像到dockerhub
1. 在dockerhub官网上注册账户
2. 在进行关联进行即可
参考网页：https://www.cnblogs.com/wherein/p/6862911.html


###  linux
1. apt-key 参数 
   操作指令：APT密钥操作指令。
        
        apt-key list #列出已保存在系统中key。 
        apt-key add keyname #把下载的key添加到本地trusted数据库中。
        apt-key del keyname #从本地trusted数据库删除key。 
        apt-key update #更新本地trusted数据库，删除过期没用的key。

