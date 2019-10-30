# JavaScript学习记录

## 1、JavaScript简介

JavaScript是一种轻量级的变成语言，可插入HTML页面的编程代码。同时，HTML中的脚本必须位于<script>与</script>标签之间，脚本可以被放置在HTML页面的<body>和<head>部分中。HTML文件中对脚本的数量没有限制。通常情况下，把函数放入<head>部分中，或者放在页面底部。

我们也可以把脚本保存到外部文件中。外部文件通常包含被多个网页使用的代码，外部JavaScript文件的文件扩展名是.js

如果使用外部文件，要在<script>标签的”scr"属性中设置该.js文件；

JavaScript是现代所有浏览器以及HTML5中的默认脚本语言。

一般来说，我们需要在某个事件发生时执行代码，比如当用户点击按钮时，如果我们把JavaScript代码放到函数中，就可以在事件发生时调用该函数。调用函数时要写全：“函数名+()”

## 2、JavaScript输出和语法

JavaScript没有任何打印或者输出的函数，但是可以通过不同的方式来输出数据：

- 使用window.alert()弹出警告框。
- 使用document.write()方法将内容写到HTML文档中。
- 使用innerHTML写入到HTML元素。
- 使用console.log()写入到浏览器的控制台。



在JS编程语言中，一般固定值称为字面量：

1.数字（Number）字面量可以是整数或者是小数，或者是科学计数（e）。

2.字符串（String）字面量可以使用单引号或者双引号。

3.表达式字面量用于计算。

4.数组（Array）字面量定义一个数组。

5.对象（Object）字面量定义一个对象。

6.函数（Function）字面量定义一个函数。

JavaScript数据类型：

值类型（基本类型）：字符串（String）、数字（Number）、布尔（Boolean）、对空（Null），未定义（Undefined）、Symbol。Symbol是ES6引入了新的原始数据类型，表示独一无二的值。

引用数据类型：对象（Object）、数组（Array）、函数（Function）。

动态类型，意味着相同变量可用作不同的类型。

对象由花括号分隔，在括号内部，对象的属性以名称和值对的形式（name:value）来定义，属性由逗号来分隔：

```
var person={firstname:"John",lastname:"Doe",id:5566};
对象属性寻址方式有两种：
name=person.lastname;
name=person["lastname"];


```



在JS编程语言中，变量用于存储数据值，JS使用关键字var来定义变量，使用等号来为变量赋值。未使用值来声明的变量，其值实际上是undefined。如果重新声明JS变量，该变量的值不会丢失。语句是通过分号分隔，注释使用双斜杠；JS对大小写是敏感的，它使用的是Unicode字符集，使用驼峰法的命名规则。

局部变量在函数开始执行时创建，函数执行完后局部变量会自动销毁。变量在函数外定义，即为全局变量。全局变量有全局作用域：网页中所有脚本和函数均可使用。如果变量在函数内没有声明（没有使用var关键字），该变量为全局变量。



 JavaScript 是脚本语言。浏览器会在读取代码时，逐行地执行脚本代码。而对于传统编程来说，会在执行前对所有代码进行编译。 

以下是JavaScript关键字：

| abstract | else       | instanceof | super        |
| -------- | ---------- | ---------- | ------------ |
| boolean  | enum       | int        | switch       |
| break    | export     | interface  | synchronized |
| byte     | extends    | let        | this         |
| case     | false      | long       | throw        |
| catch    | final      | native     | throws       |
| char     | finally    | new        | transient    |
| class    | float      | null       | true         |
| const    | for        | package    | try          |
| continue | function   | private    | typeof       |
| debugger | goto       | protected  | var          |
| default  | if         | public     | void         |
| delete   | implements | return     | volatile     |
| do       | import     | short      | while        |
| double   | in         | static     | with         |



## 3、JavaScript事件

当在HTML页面中使用JavaScript时，JavaScript可以触发这些事件。

常见的HTML事件：

| 事件        | 描述                         |
| :---------- | :--------------------------- |
| onchange    | HTML 元素改变                |
| onclick     | 用户点击 HTML 元素           |
| onmouseover | 用户在一个HTML元素上移动鼠标 |
| onmouseout  | 用户从一个HTML元素上移开鼠标 |
| onkeydown   | 用户按下键盘按键             |
| onload      | 浏览器已完成页面的加载       |

事件可以用于处理表单验证，用户输入、用户行为及浏览器动作：

- 页面加载时触发事件
- 页面关闭时触发事件
- 用户点击按钮执行动作
- 验证用户输入内容的合法性

可以使用多种方法来执行JS事件代码：

- HTML事件属性可以直接执行JavaScript代码
- HTML事件属性可以调用JavaScript函数
- 为HTML元素指定自己的事件处理程序
- 阻止事件的发生

## 4、JavaScript字符串

字符串属性：

| 属性        | 描述                       |
| :---------- | :------------------------- |
| constructor | 返回创建字符串属性的函数   |
| length      | 返回字符串的长度           |
| prototype   | 允许您向对象添加属性和方法 |



字符串方法：

| 方法                | 描述                                                         |
| :------------------ | :----------------------------------------------------------- |
| charAt()            | 返回指定索引位置的字符                                       |
| charCodeAt()        | 返回指定索引位置字符的 Unicode 值                            |
| concat()            | 连接两个或多个字符串，返回连接后的字符串                     |
| fromCharCode()      | 将 Unicode 转换为字符串                                      |
| indexOf()           | 返回字符串中检索指定字符第一次出现的位置                     |
| lastIndexOf()       | 返回字符串中检索指定字符最后一次出现的位置                   |
| localeCompare()     | 用本地特定的顺序来比较两个字符串                             |
| match()             | 找到一个或多个正则表达式的匹配                               |
| replace()           | 替换与正则表达式匹配的子串                                   |
| search()            | 检索与正则表达式相匹配的值                                   |
| slice()             | 提取字符串的片断，并在新的字符串中返回被提取的部分           |
| split()             | 把字符串分割为子字符串数组                                   |
| substr()            | 从起始索引号提取字符串中指定数目的字符                       |
| substring()         | 提取字符串中两个指定的索引号之间的字符                       |
| toLocaleLowerCase() | 根据主机的语言环境把字符串转换为小写，只有几种语言（如土耳其语）具有地方特有的大小写映射 |
| toLocaleUpperCase() | 根据主机的语言环境把字符串转换为大写，只有几种语言（如土耳其语）具有地方特有的大小写映射 |
| toLowerCase()       | 把字符串转换为小写                                           |
| toString()          | 返回字符串对象值                                             |
| toUpperCase()       | 把字符串转换为大写                                           |
| trim()              | 移除字符串首尾空白                                           |
| valueOf()           | 返回某个字符串对象的原始值                                   |



null 和 undefined 的值相等，但类型不等：

typeof undefined       // undefined
typeof null         // object
null === undefined      // false
null == undefined      // true

在 JavaScript 中, **null** 用于对象, **undefined** 用于变量，属性和方法。

对象只有被定义才有可能为 null，否则为 undefined。

**1、定义**

-  （1）undefined：是所有没有赋值变量的默认值，自动赋值。
-  （2）null：主动释放一个变量引用的对象，表示一个变量不再指向任何对象地址。

**2、何时使用null?**

当使用完一个比较大的对象时，需要对其进行释放内存时，设置为 null。

**3、null 与 undefined 的异同点是什么呢？**

**共同点**：都是原始类型，保存在栈中变量本地。

不同点：

（1）undefined——表示变量声明过但并未赋过值。

它是所有未赋值变量默认值，例如：

```
var a;    // a 自动被赋值为 undefined
```

（2）null——表示一个变量将来可能指向一个对象。

一般用于主动释放指向对象的引用，例如：

```
var emps = ['ss','nn'];
emps = null;     // 释放指向数组的引用
```

4、延伸——垃圾回收站

它是专门释放对象内存的一个程序。

-  （1）在底层，后台伴随当前程序同时运行；引擎会定时自动调用垃圾回收期；
-  （2）总有一个对象不再被任何变量引用时，才释放。



## 5、JavaScript类型转换

Number()转换为数字，String()转换为字符串，Boolean()转化为布尔值。

数字转换为字符串：Number方法toString()，String()

布尔值转换为字符串：String(),Boolean方法toString()

字符串转换为数字：Number(),

布尔值转换为数字:Number(),

## 6、JavaScript正则表达式

正则表达式是由一个字符序列形成的搜索模式，当你在文本中搜索数据时，你可用搜索模式来描述你要查询的内容。正则表达式可以是一个简单的字符，也可以是一个更复杂的模式，可用于所有文本搜索和文本替换的操作。

```
/正则表达式主体/修饰符（可选）
```

通过字符串方法：search()和replace();search()方法用于检索字符串中指定的子字符串，或检索与正则表达式相匹配的字符串，并返回子串的起始位置。replace()方法用于在字符串中用一些字符替换另一些字符，或替换一个与正则表达式匹配的子串。

| 表达式 | 描述                       |
| :----- | :------------------------- |
| [abc]  | 查找方括号之间的任何字符。 |
| [0-9]  | 查找任何从 0 至 9 的数字。 |
| (x\|y) | 查找任何以 \| 分隔的选项。 |

| 量词 | 描述                                  |
| :--- | :------------------------------------ |
| n+   | 匹配任何包含至少一个 *n* 的字符串。   |
| n*   | 匹配任何包含零个或多个 *n* 的字符串。 |
| n?   | 匹配任何包含零个或一个 *n* 的字符串。 |

## 7、JavaScript Cookie

Cookie用于存储web页面的用户信息，cookie是一些数据，存储于你电脑上的文本文件中，当web服务器向浏览器发送web页面时，在链接关闭后，服务端不会记录用户的信息。cookie的作用就是用于解决“如何记录客户端的用户信息”：1、当用户访问web页面时，他的名字可以记录在cookie中。2、在用户下一次访问该页面时，可以在cookie中读取用户访问记录。cookie以名/值对形式存储



## 8、AJAX

AJAX=Asynchronous JavaScript and XML（异步JavaScript和XML）,这是一种使用现有标准的新方法，最大的优点是在不重新加载整个页面的情况下，可以与服务器交换数据并更新部分网页内容。



![1571885611524](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1571885611524.png)

AJAX是基于现有的Internet标准，并联合使用它们：

- XMLHttpRequest对象（异步的与服务器交换数据）
- JavaScript/DOM（信息显示/交互）
- CSS（给数据定义样式）
- XML（作为转换数据的格式）



创建XMLHttpRequest对象，用于在后台与服务器交换数据。

```
variable=new XMLHttpRequest();
下面是老版本的IE浏览器使用ActiveX对象
variable=new ActiveXObject("Microsoft.XMLHTTP");

```

向服务器发送请求。

```
xmlhttp.open("GET","ajax_info.txt",true);
xmlhttp.send();
```

| 方法                         | 描述                                                         |
| :--------------------------- | :----------------------------------------------------------- |
| open(*method*,*url*,*async*) | 规定请求的类型、URL 以及是否异步处理请求。*method*：请求的类型；GET 或 POST*url*：文件在服务器上的位置*async*：true（异步）或 false（同步） |
| send(*string*)               | 将请求发送到服务器。*string*：仅用于 POST 请求               |

与POST相比，GET更简单也更快，并且在大部分情况下都能用，然而在以下情况中，使用POST请求：

- 无法使用缓存文件（更新服务器上的文件或数据库）
- 向服务器发送大量数据（POST没有数据量限制）
- 发送包含未知字符的用户输入时，POST比GET更加稳定可靠

服务器响应

如果想要获得来自服务器的响应，请使用XMLHttpRequest对象的responseText或responseXML属性。

| 属性         | 描述                       |
| :----------- | :------------------------- |
| responseText | 获得字符串形式的响应数据。 |
| responseXML  | 获得 XML 形式的响应数据。  |

onreadystatechange事件

当请求被发送到服务器时，我们需要执行一些基于响应的任务。

每当readyState改变时，就会触发onreadystatechange事件。readyState属性存有XMLHttpRequest的状态信息。

| 属性               | 描述                                                         |
| :----------------- | :----------------------------------------------------------- |
| onreadystatechange | 存储函数（或函数名），每当 readyState 属性改变时，就会调用该函数。 |
| readyState         | 存有 XMLHttpRequest 的状态。从 0 到 4 发生变化。0: 请求未初始化1: 服务器连接已建立2: 请求已接收3: 请求处理中4: 请求已完成，且响应已就绪 |
| status             | 200: "OK" 404: 未找到页面                                    |















