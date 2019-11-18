## HTML

HTML（HyperText Markup Language）称为超文本标记语言，是一种标识性的语言。它包括一系列标签，通过这些标签可以将网络上的文档格式统一，使分散的Internet资源连接为一个逻辑整体。HTML文本是有HTML命令组成的描述性文本，HTML命令可以说明文字，图形、动画、声音、表格、链接等。

特点：

- 简易性： 超级文本标记语言版本升级采用超集方式，从而更加灵活方便。
- 可扩展性：超级文本标记语言的广泛应用带来了加强功能，增加标识符等要求，采用子类元素的方式，为系统扩展带来保证。
- 平台无关性： 可以在不同平台展示和使用。
- 通用性：HTML是网络的通用语言，一种简单、通用的全置标记语言。它允许网页制作人建立文本与图片相结合的复杂页面，这些页面可以被其他人在其他电脑或浏览器中浏览到。

## CSS

CSS（Cascading Style Sheets）称为层叠样式表，是一种用来表现HTML或者XML等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。CSS能够对网页中元素位置的排版进行像素级精确控制，支持几乎所有的字体字号样式，拥有对网页对象和模型样式编辑的能力。

特点：

- 丰富的样式定义： CSS提供了丰富的文档样式外观，以及设置文本和背景属性的能力；允许为任何元素创建边框，以及元素边框与元素内容间的距离；允许随意改变文本的大小写方式、修饰方式及其他页面效果。
- 易于使用和修改： CSS可以将样式定义在HTML元素的style属性中，也可以将其定义在HTML文档的header部分，也可以将样式声明在一个专门的CSS文件中，以供HTML页面引用。CSS样式表可以将所有的样式声明统一存放，进行统一管理。
- 多页面应用： CSS样式表单独存放在一个专门的文件中，可以在多个页面中使用相同的CSS样式表。
- 层叠： 层叠就是对一个元素多次设置同一个样式，这将使用最后一次设置的属性值，即対前面的样式进行重写。

## JavaScript

JavaScript是一种直译式脚本语言，是一种动态类型、弱类型、基于原型的语言，内置支持类型。其解释器被称为JavaScript引擎，为浏览器的一部分，广泛用于客户端的脚本语言。组成部分：1、ECMAScript，描述了该语言的语法和基本对象。2、文档对象模型（DOM）,描述处理网页内容的方法和接口。3、浏览器对象模型（BOM），描述与浏览器进行交互的方法和接口。

特点：

- 语言脚本：JavaScript是一种解释型的脚本语言，C、C++等语言先编译后执行，而JavaScript是在程序的运行过程中逐行进行解释。
- 基于对象：JavaScript是一种基于对象的脚本语言，它不仅可以创建对象，也能使用现有的对象。
- 简单： JavaScript语言中采用的是弱类型的变量类型，对使用的数据类型未做出严格的要求，是基于Java基本语句和控制的脚本语言，其设计简单紧凑。
- 动态性：JavaScript是一种采用事件驱动的脚本语言，它不需要经过web服务器就可以对用户的输入做出响应。在访问一个网页时，鼠标在网页中进行鼠标点击或上下移动、窗口移动等操作JavaScript都可以直接对这些时间给出相应的响应
- 跨平台性： JavaScript脚本语言不依赖于操作系统，仅需要浏览器的支持。

## ES6

全称ECMAScript6.0，是JavaScript的下一个版本标准，主要是为了解决ES5的先天不足，比如JavaScript里并没有类的概念。

- 新增关键字：let和const，let声明的变量只在let命令所在的代码块有效且只能声明一次。const声明一个只读的常量，一旦声明，常量的值就不能改变。

- 解构赋值： 这是一种针对数组或者对象进行模式匹配，然后对其中的变量进行赋值。解构的源，解构赋值表达式的右边部分，解构的目标，解构赋值表达式的左边部分。

- 原始数据类型Symbol：表示独一无二的值，最大的用法是用来定义对象的唯一属性名。

- Map与Set： Map对象保存键值对，任何值（对象或者原始值）都可以作为一个键或一个值。Set对象存储的值总是唯一的，可用于对象去重。

- Reflect与Proxy： Proxy可以对目标对象的读取、函数调用等操作进行拦截，然后进行操作处理。它不直接操作对象，而是像代理模式，通过对象的代理对象进行操作，在进行操作时，可以添加一些需要的额外操作。Reflect可以用于获取目标对象的行为，与Object类似，但是更易读，为操作对象提供了一种更优雅的方式。

- 箭头函数： 基本语法

  ```
  参数 => 函数体
  var f = v => v;
  // 等价于
  var f = function(a){
  	return a;
  }
  f(1); //1
  ```

- 迭代器Iterator： 迭代器是一个统一的接口，它的主要作用是使各种数据结构可被便捷的访问，通过一个键为Symbol.iterator的方法实现，迭代器是用于遍历数据结构元素的指针，可以迭代的值：Array,String,Map,Set,Dom元素。

- Promise对象：是一种异步编程的解决方案，从语法上说，Promise是一个对象，从它可以获取异步操作的消息。
  Promise异步操作有三种状态：pending(进行中)，fulfilled（已成功）和rejected（已失败）。除了异步操作的结果，任何其他操作都无法改变这个状态。Promise对象只有：从pending变为fulfilled和从pending变为rejected的状态改变。只要出于fulfilled和rejected，状态就不会再变了，即resolved（已定型）。
  then方法接收两个函数作为参数，第一个参数是Promise执行成功时的回调，第二个参数是Promise执行失败时的回调，两个函数只有一个会被调用。在JavaScript事件队列的当前运行完成之前，回调函数永远不会被调用。then方法可以多次调用。

- Generator函数：ES6新引入了Generator函数，可以通过yield关键字，把函数的执行流挂起，为改变执行流程提供了可能，从而为异步编程提供解决方法。
  Generator有两个区分于普通函数的部分：1、在function后面，函数名之前有个*；2、函数内部有yield表达式。yield * 表达式表示yield返回一个遍历器对象，用于Generator函数内部，调用另一个Generator函数。

- async函数：语法

  ```
  async function name([param[,param[,...param]]]) { statements }
  // name:函数名称
  // param： 要传递给函数的参数的名称
  // statements： 函数体语句
  ```

  async函数返回一个Promise对象，可以使用then方法添加回调函数。

  ```
  async function helloAsync(){
  	return "helloAsync";
  }
  console.log(helloAsync()) // Promise { <resolved>: "helloAsync"}
  helloAsync().then(v => {
  	console.log(v);
  })
  ```

  async函数中可能会有await表达式，async函数执行时，如果遇到await就会先暂停执行，等到触发的异步操作完成后，恢复async函数的执行并返回解析值。await只能在async function内部使用。

  ```
  function testAwait(){
     return new Promise((resolve) => {
         setTimeout(function(){
            console.log("testAwait");
            resolve();
         }, 1000);
     });
  }
   
  async function helloAsync(){
     await testAwait();
     console.log("helloAsync");
   }
  helloAsync();
  // testAwait
  // helloAsync
  ```


## Git

Linux的创始者Linus花了2周时间开发了Git，并将Git应用于Linux源码管理，随后Git迅速成为了最流行的分布式版本控制系统。

分布式：

- 版本库在本地
- 版本控制流程：1、工作  2、提交新版本到本地库
- 安全性高
- 对网络没有依赖
- 不需要版本控制服务器
- 多人协作，共享远端版本库

集中式：

- 版本库在服务器中
- 版本控制流程：1、服务器端取得最新版本 2、工作 3、把工作提交给服务器
- 对网络有依赖
- 服务器不能宕机

Git优势之一：分支管理，分支可以在本地及远端随意创建，分支的创建、删除都是轻量级的，切换分支对Git而言仅仅是移动一下指针，只要不把分支push到远端，分支就是本地的。

在工作目录修改、添加或删除文件后，通过使用git add命令添加到暂存区，然后通过 git commit命令提交到本地库。

## Leaflet

Leaflet是一个为建设移动设备友好的互动地图而开发的现代的、开源的JavaScript库。它可以加载多种类型的地图服务，例如矢量地图、影像地图、矢量切片地图以及多种格式的点、线、面类型的数据，并且可以通过统计分析将分析结果展示在地图上。

[Leaflet官网]: https://leafletjs.com

   



