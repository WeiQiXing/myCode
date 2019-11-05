

# HTML学习记录

## 1、HTML介绍

​	超文本标记语言（英语：HyperText Markup Language，简称：HTML）是一种用于创建网页的标准标记语言。

HTML不是一种编程语言，而是一种标记语言，html使用标记标签（markup tag）html使用标记标签来描述网页。

HTML标签通常被称为html标签（html tag）

​    标签是由尖括号包围的关键词，比如<html>

​    标签通常是成对出现的

​    标签中的第一个标签是开始标签，第二个标签是结束标签

## 2、HTML基础

```
<!DOCTYPE html> 声明为 HTML5 文档
<html> 元素是 HTML 页面的根元素
<head> 元素包含了文档的元（meta）数据，如 <meta charset="utf-8"> 定义网页编码格式为 utf-8。
<title> 元素描述了文档的标题
<meta> 标签提供了元数据，元数据也不显示在页面上，但会被浏览器解析。
<base> 标签描述了基本的链接地址/链接目标，该标签作为HTML文档中所有的链接标签的默认链接
<link> 标签定义了文档与外部资源之间的关系，通常用于链接到样式表
<style> 标签定义了HTML文档的样式文件引用地址，可以直接添加样式来渲染HTML文档
<body> 元素包含了可见的页面内容
<h1> 元素定义一个大标题
<p> 元素定义一个段落
<script>定义了客户端的脚本文件
<div> 元素是块级元素，它可用于组合其他HTML元素的容器，它没有特定的含义，常用于文档布局。
<span> 元素是内联元素，用作文本的容器，没有特定的含义，当与CSS一同使用时，<span>元素可用于为部分文本设置样式属性
<form>元素用于设置表单，表单元素是允许用户在表单中输入内容，比如：文本域(textarea)、下拉列表、单选框(radio-buttons)、复选框（checkboxes）等
<input type="text">标签来设定，用户要在表单中键入字母、数字等内容时，就会用到文本域。
<input type="password">标签来定义密码字段。
<input type="radio">标签定义了表单单选框选项
<input type="checkbox">定义了复选框，用户需要从若干给定的选择中选取一个或者若干选项。
<input type="submit">定义了提交按钮。
HTML5新标签中
<select>定义了下拉选项列表
<option>定义了下拉列表的选项
<fieldset>	定义了一组相关的表单元素，并使用外框包含起来
<legend>定义了 <fieldset> 元素的标题
<iframe src="URL"></iframe>该URL指向不同的网页，通过使用框架，可以在同一个浏览器窗口中显示不止一个页面。

```



```
<select>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="opel">Opel</option>
  <option value="audi">Audi</option>
</select>
```

### 2.1、HTML标题

HTML标题是通过<h1> - <h6>标签来定义的

标签数字越大，字体相应越小。

```
<h1>这个是标题</h1>
<h2>这个也是标题</h2>
```

<hr>标签在HTML页面创建水平线，用于分隔内容

### 2.2、HTML段落

HTML段落通过<p>定义

```
<p>这是段落</p>

<br>标签可以在不产生一个新段落的情况下进行换行。
```



### 2.3、HTML链接

HTML链接是通过标签<a>定义的,链接地址在属性href中设置

```
<a href="https://www.baidu.com">此为链接</a>
```

超链接可以是一个字，一个词，或者一组词，也可以是一幅图像，默认情况下，链接将以以下形式出现在浏览器中：

- 一个未访问过的链接显示为蓝色字体并带有下划线。
- 访问过的链接显示为紫色并带有下划线。
- 点击链接时，链接显示为红色并带有下划线。

target属性，可以定义被链接的文档在何处显示。

id属性，用于创建在一个html文档书签标记。

[HTML颜色名链接]:https://www.runoob.com/html/html-colornames.html



### 2.4、HTML图像与表格

HTML图像通过标签<img>来定义的,src是图片存储的路径，高度和宽度也可以设置，默认单位是像素。

```
<img src="/images/logo.png" width="258" height="39"/>
```

alt属性用来为图像定义一串预备的可替换文本，替换文本属性的值是用户定义的。

表格是由<table>标签来定义的，每个表格均有若干行（由<tr>标签定义），每行被分割为若干单元格(由<td>标签定义)。字母td指表格数据(table data)，即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线等。

```
<table border="1">
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```

<th>标签来定义表格的表头，大多数浏览器把表头显示为粗体居中的文本。

### 2.5、HTML元素

- HTML元素以开始标签起始
- HTML元素以结束标签终止
- 元素的内容是开始标签和结束标签之间的内容
- 大多数HTML元素可拥有属性
- 空元素在开始标签中进行关闭
- HTML元素可以嵌套

### 2.6、HTML属性

- HTML元素可以设置属性
- 属性可以在元素中添加附加信息
- 属性一般描述于开始标签
- 属性总是以名称/值对的形式出现，比如：name="value"
- 属性值应该始终被包括在引号内，双引号是最常用的，可以使用单引号
- 适用大多数HTML元素的属性：

| 属性  | 描述                                   |
| ----- | -------------------------------------- |
| class | 为html元素定义一个或多个类名           |
| id    | 定义元素的唯一id                       |
| style | 规定了元素的行内样式（inline style）   |
| title | 描述了元素的额外信息（作为工具条使用） |

### 2.7、HTML列表

HTML列表分为无序列表、有序列表和自定义列表。

无序列表是一个项目的列表。此列项目使用粗体圆点进行标记,使用<ul>标签

```
<ul>
<li>Coffee</li>
<li>Milk</li>
</ul>
```

有序列表也是一列项目，列表项目使用数字进行标记。有序列表始于<ol>标签，每个列表项始于<li>标签。

列表项使用数字来标记。

```
<ol>
<li>Coffee</li>
<li>Milk</li>
</ol>
```

自定义列表不仅仅是一列项目，而是项目及其注释的组合。

自定义列表以<dl>标签开始，每个自定义列表项以<dt>开始，每个自定义列表项的定义以<dd>开始。

```
<dl>
<dt>Coffee</dt>
<dd>- black hot drink</dd>
<dt>Milk</dt>
<dd>- white cold drink</dd>
</dl>
```



### 2.8、HTML常用标签

| 标签     | 描述         |
| -------- | ------------ |
| <b>      | 定义粗体文本 |
| <em>     | 定义着重文字 |
| <i>      | 定义斜体字   |
| <small>  | 定义小号字   |
| <strong> | 定义加重语气 |
| <sub>    | 定义下标字   |
| <sup>    | 定义上标字   |
| <ins>    | 定义插入字   |
| <del>    | 定义删除字   |

| 标签   | 描述               |
| ------ | ------------------ |
| <code> | 定义计算机代码     |
| <kbd>  | 定义键盘码         |
| <samp> | 定义计算机代码样本 |
| <var>  | 定义变量           |
| <pre>  | 定义预格式         |

| 显示结果 | 描述   | 实体名称 | 实体编号 |
| -------- | ------ | -------- | -------- |
|          | 空格   | &nbsp；  | &#160；  |
| <        | 小于号 | &lt；    | &#60；   |
| >        | 大于号 | &gt；    | &#62；   |
| &        | 和号   | &amp；   | &#38；   |
| "        | 引号   | &quot；  | &#34；   |
| '        | 撇号   | &apos；  | &#39；   |



## 3、HTML5改进

- 新元素，可以向HTML添加新的元素，并为该元素定义样式；
- 新属性
- 完全支持CSS3
- Video和Audio
- 2D/3D制图
- 本地存储
- 本地SQL数据
- Web应用

### 3.1、HTML5标签

```
<canvas> 标签通过脚本（通常是 JavaScript）来绘制图形（比如图表和其他图像）。
<canvas> 标签只是图形容器，您必须使用脚本来绘制图形。
<caption> 标签定义表格的标题。
<caption> 标签必须直接放置到 <table> 标签之后。
您只能对每个表格定义一个标题。


```

```
var x=document.getElementById("demo");
function getLocation()
{
    if (navigator.geolocation)
    {
        navigator.geolocation.getCurrentPosition(showPosition);
    }
    else
    {
        x.innerHTML="该浏览器不支持获取地理位置。";
    }
}

function showPosition(position)
{
    x.innerHTML="纬度: " + position.coords.latitude + 
    "<br>经度: " + position.coords.longitude;    
}

```

```
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
您的浏览器不支持Video标签。
</video>

<audio controls>
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
您的浏览器不支持 audio 元素。
</audio>

```

### 3.2、HTML5元素

```
<section> 标签定义文档中的节（section、区段）。比如章节、页眉、页脚或文档中的其他部分
<article> 标签定义独立的内容。.
<nav> 标签定义导航链接的部分。
<nav> 元素用于定义页面的导航链接部分区域，但是，不是所有的链接都需要包含在 <nav> 元素中!
<aside> 标签定义页面主区域内容之外的内容（比如侧边栏）。
aside 标签的内容应与主区域的内容相关.
<header>元素描述了文档的头部区域
<header>元素主要用于定义内容的介绍展示区域.
在页面中你可以使用多个<header> 元素.
<footer> 元素描述了文档的底部区域.
<footer> 元素应该包含它的包含元素
一个页脚通常包含文档的作者，著作权信息，链接的使用条款，联系信息等
<figure>标签规定独立的流内容（图像、图表、照片、代码等等）。
<figure> 元素的内容应该与主内容相关，但如果被删除，则不应对文档流产生影响。
<figcaption> 标签定义 <figure> 元素的标题.
<figcaption>元素应该被置于 "figure" 元素的第一个或最后一个子元素的位置。

```

### 3.3、HTML5应用程序缓存

HTML5 引入了应用程序缓存，这意味着 web 应用可进行缓存，并可在没有因特网连接时进行访问。

应用程序缓存为应用带来三个优势：

1. 离线浏览 - 用户可在应用离线时使用它们
2. 速度 - 已缓存资源加载得更快
3. 减少服务器负载 - 浏览器将只从服务器下载更新过或更改过的资源。

 如需启用应用程序缓存，请在文档的<html> 标签中包含 manifest 属性： 

```
<!DOCTYPE HTML>
<html manifest="demo.appcache">
...
</html>
```

每个指定了 manifest 的页面在用户对其访问时都会被缓存。如果未指定 manifest 属性，则页面不会被缓存（除非在 manifest 文件中直接指定了该页面）。manifest 文件的建议的文件扩展名是：".appcache"。请注意，manifest 文件需要配置正确的 MIME-type，即 "text/cache-manifest"。必须在 web 服务器上进行配置。

manifest 文件是简单的文本文件，它告知浏览器被缓存的内容（以及不缓存的内容）。manifest 文件可分为三个部分：

- *CACHE MANIFEST* - 在此标题下列出的文件将在首次下载后进行缓存
- *NETWORK* - 在此标题下列出的文件需要与服务器的连接，且不会被缓存
- *FALLBACK* - 在此标题下列出的文件规定当页面无法访问时的回退页面（比如 404 页面）

### 3.4、HTML5WebSQL数据库

以下是规范中定义的三个核心方法：

1. **openDatabase**：这个方法使用现有的数据库或者新建的数据库创建一个数据库对象。

   openDatabase() 方法对应的五个参数说明：

   1. 数据库名称
   2. 版本号
   3. 描述文本
   4. 数据库大小
   5. 创建回调

2. **transaction**：这个方法让我们能够控制一个事务，以及基于这种情况执行提交或者回滚。

3. **executeSql**：这个方法用于执行实际的 SQL 查询。

### 3.5、HTML5Web存储

早些时候,本地存储使用的是 cookie。但是Web 存储需要更加的安全与快速. 这些数据不会被保存在服务器上，但是这些数据只用于用户请求网站数据上.它也可以存储大量的数据，而不影响网站的性能。数据以 键/值 对存在, web网页的数据只允许该网页访问使用

客户端存储数据的两个对象为：

- localStorage - 用于长久保存整个网站的数据，保存的数据没有过期时间，直到手动去除。
- sessionStorage - 用于临时保存同一窗口(或标签页)的数据，在关闭窗口或标签页之后将会删除这些数据

不管是 localStorage，还是 sessionStorage，可使用的API都相同，常用的有如下几个（以localStorage为例）：

- 保存数据：localStorage.setItem(key,value);
- 读取数据：localStorage.getItem(key);
- 删除单个数据：localStorage.removeItem(key);
- 删除所有数据：localStorage.clear();
- 得到某个索引的key：localStorage.key(index);

**提示:** 键/值对通常以字符串存储，你可以按自己的需要转换该格式。

