## Python 基础语法
1. 行与缩进

python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
>缩进不一致，会导致运行错误
    
    IndentationError: unindent does not match any outer indentation level
2. 多行语句

Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠来实现多行语句.在 [], {}, 或 () 中的多行语句，不需要使用反斜杠。
>total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
3. 字符串(String)
    1. python中单引号和双引号使用完全相同。
    2. 使用三引号('''或""")可以指定一个多行字符串。
    3. 转义符：反斜线\
    4. 反斜杠可以用来转义，使用r可以让反斜杠不发生转义
            
            print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
            print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
    
            >hello
            runoob
            hello\nrunoob
    5. 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
    6. Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
    7. Python中的字符串不能改变。
    8. Python 没有单独的字符类型，一个字符就是长度为 1 的字符串.字符串的截取的语法格式如下：变量[头下标:尾下标]
           
            print(str[2:])    # 输出从第三个开始的后的所有字符
            print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
4. 多个语句构成代码组

像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束.
            
    if expression : 
5. print输出

需要注意的是：需要加括号

    1. 换行输出
            
            print( x )
            print( y )
            print('---------')
    2. 不换行输出
            
            print( x, end=" " )
            print( y, end=" " )
6. import 与 from...import

    1. 在 python 用 import 或者 from...import 来导入相应的模块。
    2. 将整个模块(somemodule)导入，格式为：
            
            import somemodule
    3. 从某个模块中导入某个函数,格式为： 
    
            from somemodule import somefunction
    4. 从某个模块中导入多个函数,格式为： 
            
            from somemodule import firstfunc, secondfunc, thirdfunc
    5. 将某个模块中的全部函数导入，格式为： 
            
            from somemodule import *

## Python 基础数据类型
1. List（列表）

列表是写在方括号 [] 之间、用逗号分隔开的元素列表
   
    1. 列表截取的语法格式如下：变量[头下标:尾下标]。
    2. 索引值以 0 为开始值，-1 为从末尾的开始位置。
    3. 注意：
        1. List写在方括号之间，元素用逗号隔开。
            
                a = [1, 2, 3, 4, 5, 6]
        2. list可以被索引和切片，和字符串一样。
        3. List可以使用+操作符进行拼接。
        4. List中的元素是可以改变的，字符串却不行。
注意：list[1:3] 其实输出的只有两个变量，即list中第二个元素到第三个元素，并不是第1 第2 第3三个元素。

2. Tuple（元组）

元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。字符串看作一种特殊的元组

    注意构造包含0或1个元素的元组的特殊语法规则。
        tup1 = ()    # 空元组
        tup2 = (20,) # 一个元素，需要在元素后添加逗号

注：string、list和tuple都属于sequence（序列）

3. Set（集合）

    1. 集合（set）是一个无序不重复元素的序列。
    2. 基本功能是进行成员关系测试和删除重复元素。
    3. 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

            创建格式：
            parame = {value01,value02,...}
            或者
            set(value)

4. Dictionary（字典）

    1. 字典（dictionary）是Python中另一个非常有用的内置数据类型。

    2. 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

    3. 字典是一种映射类型，字典用"{ }"标识
    
        它是一个无序的键(key) : 值(value)对集合。

    4. 键(key)必须使用不可变类型。在同一个字典中，键(key)必须是唯一的。

            dict = {}          #创建一个空字典
            dict['one'] = "1 "
            dict[2]     = "2 "
            tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}                       
            print (dict['one'])       # 输出键为 'one' 的值
            print (dict[2])           # 输出键为 2 的值
            print (tinydict)          # 输出完整的字典
            print (tinydict.keys())   # 输出所有键
            print (tinydict.values()) # 输出所有值

            1 
            2 
            {'name': 'runoob', 'site': 'www.runoob.com', 'code': 1}
            dict_keys(['name', 'site', 'code'])
            dict_values(['runoob', 'www.runoob.com', 1])
5. 





