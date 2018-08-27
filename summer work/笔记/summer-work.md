# summer work
1. 做成绩登录系统，当判断成绩更新时，发送链接到邮箱中，点击链接，即可看到成绩页面
2. 学习python3的基础语法和了解并学MongoDB的语法，学习json基础语法，并了解flask框架，加深对css了解与认识
3. 首先进行把从教务处爬取得信息传到MongoDB中，其次获取科目数个数，当大于时，发送链接，到邮箱中
4. 在信息页面，加入了绩点，总绩点的信息。解决了字相互重合的问题
5. 现在存在的问题：
        
        *当其他人登录系统的时候，系统可以获取到登录人的邮箱，并进行发送
6. 对文件进行说明

   day3spider.py:爬取教务处的信息

   mail.py：进行发送邮件的设置

   info.html ：成绩信息页面

   score.html ：邮箱发送链接的页面
7. 对docker进行了解，在centos和Debian中都进行了安装，但是在创建自己的镜像的时候和创dockerhub账户的时候。
### *邮件通过QQ邮箱发送不出去
1. 需要一个安全的连接，例如SSL，因此接下来我们会使用SSL的方式去登录
2. 打开qq邮箱，点击设置--账户，找到 
POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务，开启IMAP/SMTP服务，然后根据要求使用手机发送到指定号码，获取授权码
3. 这个授权码就是你接下来登录要使用的密码，配置完成。即可成功发送邮件
        
        参考文件：Python3实现SMTP发送邮件详细教程
        https://blog.csdn.net/sunhuaqiang1/article/details/70833199
### *Python 数据循环越界问题
1. 比如你定义了一个长度为5的数组int[] a = new int[5];那么你用a[0]到a[4]都不会越界，当你的数组下标大于5时，就会数组越界

###  Python3 Flask在不同页面间传递参数
1. "AssertionError: View function mapping is overwriting an existing endpoint function"
        
        解决方案： 
        1.路由名相同或者函数名相同 
        2.自定义python装饰器时一定要使用@functools.wraps(func)修饰wrapper

### *完成图片展示
1. ![信息页面](raw.githubusercontent.com/MorlockZ/Dev-ops/master/day04-score%20system/完成图/3.png)
2. ![发送信息到邮箱中](raw.githubusercontent.com/MorlockZ/Dev-ops/master/day04-score%20system/完成图/2.png)
3. ![邮箱链接所示页面](raw.githubusercontent.com/MorlockZ/Dev-ops/master/day04-score%20system/完成图/1.png)

### *想法
在我想判断成绩更新时：最开始的想法是获取已知科目数，再传入MongoDB中，为最基本的参数。在判断刚数值更新的时候，触发邮件系统，并发送邮件。可是在我做的时候，发现并不适用。之后再网上查找资料发现可以判断文件的最后修改时间与创建时间是否在秒级别上一致，即为监测文件是否更新。但是不知道成绩在什么时候才能更新，所以还是按照原先得想法，来判断成绩更新。


<!-- TOC -->

- [summer work](#summer-work)
        - [*邮件通过QQ邮箱发送不出去](#邮件通过qq邮箱发送不出去)
        - [*Python 数据循环越界问题](#python-数据循环越界问题)
        - [Python3 Flask在不同页面间传递参数](#python3-flask在不同页面间传递参数)
        - [*完成图片展示](#完成图片展示)
        - [*想法](#想法)

<!-- /TOC -->