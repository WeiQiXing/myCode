# CSS学习记录

## 1、CSS简介

CSS指层叠样式表（Cascading Style Sheets），样式通常存储在样式表中，把样式添加到HTML4.0中，是为了解决内容与表现分离的问题。外部样式表可以极大地提高工作效率，通常存储在CSS文件中，多个样式定义可层叠为一个。

样式表定义如何显示HTML元素，就像HTML中字体标签和颜色属性所起的作用那样，样式通常保存在外部的.css文件中。



## 2、CSS语法

CSS规则由两个主要的部分构成：选择器，以及一条或多条声明。

```
p {color:red;text-align:center;}
```

选择器通常是你需要改变样式的HTML元素，每条声明由一个属性和一个值组成。属性（property）是你希望设置的样式属性（style attribute）。每个属性有一个值，属性和值被冒号分开。

```
CSS注释以“/*”开始，以“*/”结束。
```

**id选择器**可以为标有特定id的HTML元素指定特定的样式。

HTML元素以id属性来设置id选择器，CSS中id选择器以“#”来定义。

```
#para1
{
	text-align:center;
	color:red;
}
<p id="para1">hello</p>
```

**class选择器**用于描述一组元素的样式，class选择器有别于id选择器，class可以在多个元素中使用。class选择器在HTML中以class属性表示，在CSS中，类选择器以一个点“.”号显示。

```
.center
{
	text-align:center;
}

```



## 3、CSS样式表

### 3.1、外部样式表（External style sheet）

当样式需要应用于很多页面时，外部样式表将是理想的选择。在使用外部样式表的情况下，你可以通过改变一个文件来改变整个站点的外观。每个页面使用\<link>标签连接到样式表。\<link>标签在头部。

```
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>

```

浏览器会从文件mystyle.css文件中读到样式声明，并根据它来格式文档。

### 3.2、内部样式表（Internal style sheet）

当单个文档需要特殊的样式时。就应该使用内部样式表，可以使用\<style>标签在文档头部定义内部样式表：

```
<head>
<style>
hr {color:sienna;}
p {margin-left:20px;}
body {background-image:url("images/back40.gif");}
</style>
</head>

```



### 3.3、内联样式（Inline style）

由于要将表现和内容混杂在一起，内联样式会损失掉样式表的许多优势。当样式仅需要在一个元素上应用一次时，要使用内联样式，需要在相关的标签内使用样式（style）属性，Style属性可以包含任何CSS属性：

```
<p style="color:sienna;margin-left:20px">这是一个段落。</p>
```



## 4、CSS样式

### 4.1、CSS背景

CSS背景属性用于定义HTML元素的背景，定义背景效果：

- background-color 定义了元素的背景颜色
- background-image 描述了元素的背景图像
- background-repeat 设置定位与不平铺
- background-attachment  背景图像是否固定或者随着页面的其余部分滚动
- background-position 设置背景图像是否及如何重复

### 4.2、CSS文本格式

- color 设置文本颜色
- direction 设置文本方向
- letter-spacing 设置字符间距
- line-height 设置行高
- text-align 对齐元素中的文本
- text-indent 缩进元素中文本的首行
- text-shadow 设置文本阴影
- text-transform 控制元素中的字母
- text-decoration 用来设置或删除文本的修饰

### 4.3、CSS字体

- font 在一个声明中设置所有的字体属性
- font-family 指定文本的字体系列
- font-size 指定文本的字体大小
- font-style 指定文本的字体样式
- font-variant 以小型大号字体或者正常字体显示文本
- font-weight 指定字体的粗细

### 4.4、CSS链接

链接状态一共四个：

- a:link - 正常，为访问过的链接
- a:visited - 用户已访问过的链接
- a:hover - 当用户鼠标放在链接上时
- a:active - 链接被点击的那一刻

### 4.5、CSS列表

- list-style 简写属性，用于把所有用于列表的属性设置于一个声明中
- list-style-image 将图像设置为列表项标志
- list-style-position 设置列表中列表项标志的位置
- list-style-type 设置列表项标志的类型

### 4.6、CSS盒子模型

- Margin（外边距） - 清除边框外的区域，外边距是透明的
- Border（边框） - 围绕在内边距和内容外的边框
- Padding（内边距） - 清除内容周围的区域，内边距是透明的
- Content（内容） - 盒子的内容，显示文本和图像

总元素的宽度=宽度+左填充+右填充+左边框+右边框+左边距+右边距

元素的总高度最终计算公式是这样的：

总元素的高度=高度+顶部填充+底部填充+上边框+下边框+上边距+下边距

### 4.7、CSS边框Border

| 属性                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| border                                                       | 简写属性，用于把针对四个边的属性设置在一个声明。             |
| border-style                                                 | 用于设置元素所有边框的样式，或者单独地为各边设置边框样式。   |
| border-width | 简写属性，用于为元素的所有边框设置宽度，或者单独地为各边边框设置宽度。 |
| border-color | 简写属性，设置元素的所有边框中可见部分的颜色，或为 4 个边分别设置颜色。 |
| border-bottom| 简写属性，用于把下边框的所有属性设置到一个声明中。           |
| border-bottom-color | 设置元素的下边框的颜色。                                     |
| border-bottom-style| 设置元素的下边框的样式。                                     |
| border-bottom-width| 设置元素的下边框的宽度。                                     |
| border-left | 简写属性，用于把左边框的所有属性设置到一个声明中。           |
| border-left-color| 设置元素的左边框的颜色。                                     |
| border-left-style| 设置元素的左边框的样式。                                     |
| border-left-width| 设置元素的左边框的宽度。                                     |
| border-right| 简写属性，用于把右边框的所有属性设置到一个声明中。           |
| border-right-color | 设置元素的右边框的颜色。                                     |
|border-right-style| 设置元素的右边框的样式。                                     |
| border-right-width | 设置元素的右边框的宽度。                                     |
| border-top| 简写属性，用于把上边框的所有属性设置到一个声明中。           |
| border-top-color | 设置元素的上边框的颜色。                                     |
| border-top-style| 设置元素的上边框的样式。                                     |
| border-top-width| 设置元素的上边框的宽度。                                     |

### 4.8、CSS外边距margin

| 属性                                                         | 描述                                       |
| :----------------------------------------------------------- | :----------------------------------------- |
| [margin](https://www.runoob.com/cssref/pr-margin.html)       | 简写属性。在一个声明中设置所有外边距属性。 |
| [margin-bottom](https://www.runoob.com/cssref/pr-margin-bottom.html) | 设置元素的下外边距。                       |
| [margin-left](https://www.runoob.com/cssref/pr-margin-left.html) | 设置元素的左外边距。                       |
| [margin-right](https://www.runoob.com/cssref/pr-margin-right.html) | 设置元素的右外边距。                       |
| [margin-top](https://www.runoob.com/cssref/pr-margin-top.html) | 设置元素的上外边距。                       |

### 4.9、CSS填充Padding

| 属性                                                         | 说明                                       |
| :----------------------------------------------------------- | :----------------------------------------- |
| [padding](https://www.runoob.com/cssref/pr-padding.html)     | 使用简写属性设置在一个声明中的所有填充属性 |
| [padding-bottom](https://www.runoob.com/cssref/pr-padding-bottom.html) | 设置元素的底部填充                         |
| [padding-left](https://www.runoob.com/cssref/pr-padding-left.html) | 设置元素的左部填充                         |
| [padding-right](https://www.runoob.com/cssref/pr-padding-right.html) | 设置元素的右部填充                         |
| [padding-top](https://www.runoob.com/cssref/pr-padding-top.html) | 设置元素的顶部填充                         |

### 4.10、嵌套选择器

- **p{ }**: 为所有 **p** 元素指定一个样式。
- **.marked{ }**: 为所有 **class="marked"** 的元素指定一个样式。
- **.marked p{ }**: 为所有 **class="marked"** 元素内的 **p** 元素指定一个样式。
- **p.marked{ }**: 为所有 **class="marked"** 的 **p** 元素指定一个样式。





### 4.11、CSS常见属性

display属性：设置一个元素如何显示

visibility属性：设置一个元素应可见还是隐藏

position属性：指定了元素的定位类型

overflow属性：用于控制内容溢出元素框时显示的方式

float属性：会使元素向左或向右移动，其周围的元素也会重新排列。可用于制作水平导航栏



### 4.12、CSS组合选择符

- 后代选择器（以空格分隔） 用于选取某元素的后代元素
- 子元素选择器（以大于号分隔） 只能选择作为某元素子元素的元素
- 相邻兄弟选择器（以加号分隔） 可选择紧接在另一元素后的元素，且两者有相同的元素
- 普通兄弟选择器（以破折号分隔） 选取所有指定元素之后的相邻兄弟元素



### 4.13、CSS元素相关特性

**块级元素(block)特性：**

- 总是独占一行，表现为另起一行开始，而且其后的元素也必须另起一行显示;
- 宽度(width)、高度(height)、内边距(padding)和外边距(margin)都可控制;

**内联元素(inline)特性：**

- 和相邻的内联元素在同一行;
- 宽度(width)、高度(height)、内边距的top/bottom(padding-top/padding-bottom)和外边距的top/bottom(margin-top/margin-bottom)都不可改变，就是里面文字或图片的大小;

**块级元素主要有：**

-  address , blockquote , center , dir , div , dl , fieldset , form , h1 , h2 , h3 , h4 , h5 , h6 , hr , isindex , menu , noframes , noscript , ol , p , pre , table , ul , li

**内联元素主要有：**

- a , abbr , acronym , b , bdo , big , br , cite , code , dfn , em , font , i , img , input , kbd , label , q , s , samp , select , small , span , strike , strong , sub , sup ,textarea , tt , u , var

**可变元素(根据上下文关系确定该元素是块元素还是内联元素)：**

- applet ,button ,del ,iframe , ins ,map ,object , script

**CSS中块级、内联元素的应用：**

利用CSS我们可以摆脱上面表格里HTML标签归类的限制，自由地在不同标签/元素上应用我们需要的属性。

主要用的CSS样式有以下三个：

- display:block -- 显示为块级元素
- display:inline -- 显示为内联元素
- display:inline-block -- 显示为内联块元素，表现为同行显示并可修改宽高内外边距等属性



### 4.14、CSS网页布局

网页布局有很多种方式，一般分为以下几个部分：头部区域、菜单导航区域、内容区域、底部区域

头部区域位于整个网页的顶部，一般用于设置网页的标题或者网页的logo

菜单导航区域包含了一些链接，可以引导用户浏览其他页面

内容区域一般有三种形式：

- 1列，一般用于移动端
- 2列，一般用于平板设备
- 3列，一般用于PC桌面设备



### 4.15、CSS制作下拉菜单

```
<style>
/* 下拉按钮样式 */
.dropbtn {
    background-color: #4CAF50;
    color: white;
    padding: 16px;
    font-size: 16px;
    border: none;
    cursor: pointer;
}

/* 容器 <div> - 需要定位下拉内容 */
.dropdown {
    position: relative;
    display: inline-block;
}

/* 下拉内容 (默认隐藏) */
.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
}

/* 下拉菜单的链接 */
.dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

/* 鼠标移上去后修改下拉菜单链接颜色 */
.dropdown-content a:hover {background-color: #f1f1f1}

/* 在鼠标移上去后显示下拉菜单 */
.dropdown:hover .dropdown-content {
    display: block;
}

/* 当下拉内容显示后修改下拉按钮的背景颜色 */
.dropdown:hover .dropbtn {
    background-color: #3e8e41;
}
</style>

<div class="dropdown">
  <button class="dropbtn">下拉菜单</button>
  <div class="dropdown-content">
    <a href="#">菜鸟教程 1</a>
    <a href="#">菜鸟教程 2</a>
    <a href="#">菜鸟教程 3</a>
  </div>
</div>

```

### 4.16、CSS制作提示工具

```
<style>
/* Tooltip 容器 */
.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black; /* 悬停元素上显示点线 */
}
 
/* Tooltip 文本 */
.tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: black;
    color: #fff;
    text-align: center;
    padding: 5px 0;
    border-radius: 6px;
 
    /* 定位 */
    position: absolute;
    z-index: 1;
}
 
/* 鼠标移动上去后显示提示框 */
.tooltip:hover .tooltiptext {
    visibility: visible;
}
</style>
 
<div class="tooltip">鼠标移动到这
  <span class="tooltiptext">提示文本</span>
</div>
```













