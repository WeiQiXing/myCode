## ECharts
---
	ECharts,一个纯Javascript的图表库，可以流畅的运行在PC和移动设备上
### 简介
ECharts，缩写来自 Enterprise Charts，商业级数据图表，是百度的一个开源的数据可视化工具，一个纯 Javascript 的图表库，能够在 PC 端和移动设备上流畅运行，兼容当前绝大部分浏览器（IE6/7/8/9/10/11，chrome，firefox，Safari等），底层依赖轻量级的 Canvas 库 ZRender，ECharts 提供直观，生动，可交互，可高度个性化定制的数据可视化图表。创新的拖拽重计算、数据视图、值域漫游等特性大大增强了用户体验，赋予了用户对数据进行挖掘、整合的能力。
[Echarts官网](https://echarts.apache.org/zh/index.html)


### 特点
1. ECharts 属于开源软件，并且我们提供了非常炫酷的图形界面，特色是地图，另外还提供了柱状图、折线图、饼图、气泡图及四象限图等；
2. ECharts 使用简单，在官网中为我们封装了 JS，只要会引用就会得到完美的展示效果；
3. ECharts 种类多，ECharts 实现简单，各类图形都有，如常规的折线图、柱状图、散点图、饼图，用于统计的盒形图，用于地理数据可视化的地图、热力图，用于关系数据可视化的关系图、treemap、旭日图；相应的模板，还有丰富的 API 及文档说明，非常详细；
4. ECharts 兼容性好，基于HTML5，有着良好的动画渲染效果。
5. 多种数据格式无需转换直接使用，支持直接传入包括二维表，key-value等多种格式的数据源。
6. 通过增量渲染技术，配合各种细致的优化，可以展现千万级的数据量，并且在这个数据量级依然能够进行流畅的缩放平移等交互。
7. 通过GL实现更多更强大绚丽的三维可视化。
### 使用方法
首先设置一个DOM容器，然后通过echarts.init()方法和setOption方法生成图形，示例：
```
<body>
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div id="main" style="width: 600px;height:400px;"></div>
    <script type="text/javascript">
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));

        // 指定图表的配置项和数据
        var option = {
            title: {
                text: 'ECharts 入门示例'
            },
            tooltip: {},
            legend: {
                data:['销量']
            },
            xAxis: {
                data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
            },
            yAxis: {},
            series: [{
                name: '销量',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
    </script>
</body>
```
### 自定义构建Echarts
1. 完全版：echarts/dist/echarts.js，体积最大，包含所有的图表和组件，所包含内容参见：echarts/echarts.all.js。
2. 常用版：echarts/dist/echarts.common.js，体积适中，包含常见的图表和组件，所包含内容参见：echarts/echarts.common.js。
3. 精简版：echarts/dist/echarts.simple.js，体积较小，仅包含最常用的图表和组件，所包含内容参见：echarts/echarts.simple.js。

### 个性化图表的样式
```
myChart.setOption({
    series : [
        {
            name: '访问来源',
            type: 'pie',
            radius: '55%',
            data:[
                {value:235, name:'视频广告'},
                {value:274, name:'联盟广告'},
                {value:310, name:'邮件营销'},
                {value:335, name:'直接访问'},
                {value:400, name:'搜索引擎'}
            ]
        }
    ]
})
```
这里的data属性值不像入门教程里那样每一项都是单个数值，而一个包含name和value属性的对象，ECharts中的数据项都是既可以只设成数值，也可以设成一个包含有名称、该数据图形的样式配置、标签配置的对象。
饼图也支持通过设置roseType显示成南丁格尔图，通过半径表示数据的大小：
```
roseType: 'angle'
```
### ECharts中的样式简介
#### 颜色主题Theme
最简单的更改全局样式的方式，是直接采用颜色主题（Theme），可以选择“Theme”，直接看到采用主题的效果。ECharts4除了默认主题外，新内置了两套主题，分别为‘light’和‘dark’，使用方法：
```
var chart = echarts.init(dom, 'light');
var chart = echarts.init(dom, 'dark');
```
#### 调色板
调色板，可以在option中设置，它给定了一组颜色，图形、系列会自动从其中选择颜色。可以设置全局的调色盘，也可以设置系列自己专属的调色盘。
```
option = {
    // 全局调色盘。
    color: ['#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3'],

    series: [{
        type: 'bar',
        // 此系列自己的调色盘。
        color: ['#dd6b66','#759aa0','#e69d87','#8dc1a9','#ea7e53','#eedd78','#73a373','#73b9bc','#7289ab', '#91ca8c','#f49f42'],
        ...
    }, {
        type: 'pie',
        // 此系列自己的调色盘。
        color: ['#37A2DA', '#32C5E9', '#67E0E3', '#9FE6B8', '#FFDB5C','#ff9f7f', '#fb7293', '#E062AE', '#E690D1', '#e7bcf3', '#9d96f5', '#8378EA', '#96BFFF'],
        ...
    }]
}
```
#### 直接的样式设置itemStyle，lineStyle，areaStyle，label
直接的样式设置是比较常用设置方式。纵观ECharts的option中，很多地方可以设置itemStyle，lineStyle，areaStyle，label等等。这些地方可以直接设置图形元素的颜色、线宽、点的大小、标签的文字、标签的样式等。
#### 高亮的样式：emphasis
在鼠标悬浮到图形元素上时，一般会出现高亮的样式。默认情况下，高亮的样式是根据普通样式自动生成的。但是高亮的样式也可以自己定义，主要是通过emphasis属性定制。emphasis中的结构和普通样式的结构相同，例如：
```
option = {
    series: {
        type: 'scatter',

        // 普通样式。
        itemStyle: {
            // 点的颜色。
            color: 'red'
        },
        label: {
            show: true,
            // 标签的文字。
            formatter: 'This is a normal label.'
        },

        // 高亮样式。
        emphasis: {
            itemStyle: {
                // 高亮时点的颜色。
                color: 'blue'
            },
            label: {
                show: true,
                // 高亮时标签的文字。
                formatter: 'This is a emphasis label.'
            }
        }
    }
}
```
### 异步数据加载和更新
ECharts实现异步数据的更新非常简单，在图表初始化后不管任何时候只要通过jQuery等工具异步获取数据后通过setOption填入数据和配置项就行了。
```
var myChart = echarts.init(document.getElementById('main'));
$.get('data.json').done(function (data) {
	myChart.setOption({
		title: {
			text: '异步数据加载示例'
		},
		tooltip: {},
		legend: {
			data:['销量']
		},
		xAxis: {
			data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
		},
		yAxis: {},
		series: [{
			name: '销量'，
			type: 'bar',
			data: [5,20,36,10,10,20]
		}]
	});
});
```
ECharts 中在更新数据的时候需要通过name属性对应到相应的系列，上面示例中如果name不存在也可以根据系列的顺序正常更新，但是更多时候推荐更新数据的时候加上系列的name数据。
如果数据加载时间较长，一个空的坐标轴放在画布上也会让用户觉得是不是产生 bug 了，因此需要一个 loading 的动画来提示用户数据正在加载。
ECharts 默认有提供了一个简单的加载动画。只需要调用 showLoading 方法显示。数据加载完成后再调用 hideLoading 方法隐藏加载动画。
```
myChart.showLoading();
$.get('data.json').done(function (data) {
    myChart.hideLoading();
    myChart.setOption(...);
});
```
ECharts 由数据驱动，数据的改变驱动图表展现的改变，因此动态数据的实现也变得异常简单。
所有数据的更新都通过 setOption实现，你只需要定时获取数据，setOption 填入数据，而不用考虑数据到底产生了那些变化，ECharts 会找到两组数据之间的差异然后通过合适的动画去表现数据的变化。

### 使用dataset管理数据
ECharts4开始支持了dataset组件用于单独的数据集声明，从而数据可以单独管理被多个组件复用，并且可以基于数据指定数据到视觉的映射。示例：
```
option = {
    legend: {},
    tooltip: {},
    dataset: {
        // 提供一份数据。
        source: [
            ['product', '2015', '2016', '2017'],
            ['Matcha Latte', 43.3, 85.8, 93.7],
            ['Milk Tea', 83.1, 73.4, 55.1],
            ['Cheese Cocoa', 86.4, 65.2, 82.5],
            ['Walnut Brownie', 72.4, 53.9, 39.1]
        ]
    },
    // 声明一个 X 轴，类目轴（category）。默认情况下，类目轴对应到 dataset 第一列。
    xAxis: {type: 'category'},
    // 声明一个 Y 轴，数值轴。
    yAxis: {},
    // 声明多个 bar 系列，默认情况下，每个系列会自动对应到 dataset 的每一列。
    series: [
        {type: 'bar'},
        {type: 'bar'},
        {type: 'bar'}
    ]
}
```
我们制作数据可视化图表的逻辑是这样的：基于数据，在配置项中指定如何映射到图形。
概略而言，可以进行这些映射：
指定 dataset 的列（column）还是行（row）映射为图形系列（series）。这件事可以使用 series.seriesLayoutBy 属性来配置。默认是按照列（column）来映射。
指定维度映射的规则：如何从 dataset 的维度（一个“维度”的意思是一行/列）映射到坐标轴（如 X、Y 轴）、提示框（tooltip）、标签（label）、图形元素大小颜色等（visualMap）。这件事可以使用 series.encode 属性，以及 visualMap 组件（如果有需要映射颜色大小等视觉维度的话）来配置。上面的例子中，没有给出这种映射配置，那么 ECharts 就按最常见的理解进行默认映射：X 坐标轴声明为类目轴，默认情况下会自动对应到 dataset.source 中的第一列；三个柱图系列，一一对应到 dataset.source 中后面每一列。
按行还是按列做映射

有了数据表之后，使用者可以灵活得配置：数据如何对应到轴和图形系列。
用户可以使用 seriesLayoutBy 配置项，改变图表对于行列的理解。seriesLayoutBy 可取值：
- 'column': 默认值。系列被安放到 dataset 的列上面。
- 'row': 系列被安放到 dataset 的行上面
#### 维度（dimension）
介绍 encode 之前，首先要介绍“维度（dimension）”的概念。
常用图表所描述的数据大部分是“二维表”结构，上述的例子中，我们都使用二维数组来容纳二维表。现在，当我们把系列（series）对应到“列”的时候，那么每一列就称为一个“维度（dimension）”，而每一行称为数据项（item）。反之，如果我们把系列（series）对应到表行，那么每一行就是“维度（dimension）”，每一列就是数据项（item）。
维度可以有单独的名字，便于在图表中显示。维度名（dimension name）可以在定义在 dataset 的第一行（或者第一列）。例如上面的例子中，'score'、'amount'、'product' 就是维度名。从第二行开始，才是正式的数据。dataset.source 中第一行（列）到底包含不包含维度名，ECharts 默认会自动探测。当然也可以设置 dataset.sourceHeader: true 显示声明第一行（列）就是维度，或者 dataset.sourceHeader: false 表明第一行（列）开始就直接是数据。
#### 数据到图形的映射（encode）
```
var option = {
    dataset: {
        source: [
            ['score', 'amount', 'product'],
            [89.3, 58212, 'Matcha Latte'],
            [57.1, 78254, 'Milk Tea'],
            [74.4, 41032, 'Cheese Cocoa'],
            [50.1, 12755, 'Cheese Brownie'],
            [89.7, 20145, 'Matcha Cocoa'],
            [68.1, 79146, 'Tea'],
            [19.6, 91852, 'Orange Juice'],
            [10.6, 101852, 'Lemon Juice'],
            [32.7, 20112, 'Walnut Brownie']
        ]
    },
    xAxis: {},
    yAxis: {type: 'category'},
    series: [
        {
            type: 'bar',
            encode: {
                // 将 "amount" 列映射到 X 轴。
                x: 'amount',
                // 将 "product" 列映射到 Y 轴。
                y: 'product'
            }
        }
    ]
};
```
默认的映射
指的一提的是，ECharts 针对最常见直角坐标系中的图表（折线图、柱状图、散点图、K线图等）、饼图、漏斗图，给出了简单的默认的映射，从而不需要配置 encode 也可以出现图表（一旦给出了 encode，那么就不会采用默认映射）。默认的映射规则不易做得复杂，基本规则大体是：
- 在坐标系中（如直角坐标系、极坐标系等）
- 如果有类目轴（axis.type 为 'category'），则将第一列（行）映射到这个轴上，后续每一列（行）对应一个系列。
- 如果没有类目轴，假如坐标系有两个轴（例如直角坐标系的 X Y 轴），则每两列对应一个系列，这两列分别映射到这两个轴上。
- 如果没有坐标系（如饼图）
- 取第一列（行）为名字，第二列（行）为数值（如果只有一列，则取第一列为数值）。

默认的规则不能满足要求时，就可以自己来配置 encode，也并不复杂。
### 在图表中加入交互组件
除了图表外ECharts中，提供了很多交互组件，例如：
图里组件 legend、标题组件 title、视觉映射组件 visualMap、数据区域缩放组件 dataZoom、时间线组件 timeline
#### dataZoom组件
『概览数据整体，按需关注数据细节』是数据可视化的基本交互需求。dataZoom 组件能够在直角坐标系（grid）、极坐标系（polar）中实现这一功能。
dataZoom 组件是对 数轴（axis） 进行『数据窗口缩放』『数据窗口平移』操作。
可以通过 dataZoom.xAxisIndex 或 dataZoom.yAxisIndex 来指定 dataZoom 控制哪个或哪些数轴。
dataZoom 组件可同时存在多个，起到共同控制的作用。控制同一个数轴的组件，会自动联动。下面例子中会详细说明。
dataZoom 的运行原理是通过『数据过滤』来达到『数据窗口缩放』的效果。
数据过滤模式的设置不同，效果也不同，参见：dataZoom.filterMode。
dataZoom 的数据窗口范围的设置，目前支持两种形式：
百分比形式：参见 dataZoom.start 和 dataZoom.end。
绝对数值形式：参见 dataZoom.startValue 和 dataZoom.endValue。
```
option = {
    xAxis: {
        type: 'value'
    },
    yAxis: {
        type: 'value'
    },
    dataZoom: [
        {   // 这个dataZoom组件，默认控制x轴。
            type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
            start: 10,      // 左边在 10% 的位置。
            end: 60         // 右边在 60% 的位置。
        }
    ],
    series: [
        {
            type: 'scatter', // 这是个『散点图』
            itemStyle: {
                opacity: 0.8
            },
            symbolSize: function (val) {
                return val[2] * 40;
            },
            data: [["14.616","7.241","0.896"],["3.958","5.701","0.955"],["2.768","8.971","0.669"],["9.051","9.710","0.171"],["14.046","4.182","0.536"],["12.295","1.429","0.962"],["4.417","8.167","0.113"],["0.492","4.771","0.785"],["7.632","2.605","0.645"],["14.242","5.042","0.368"]]
        }
    ]
}
```
### 数据的视觉映射
数据可视化是 数据 到 视觉元素 的映射过程（这个过程也可称为视觉编码，视觉元素也可称为视觉通道）。
ECharts 的每种图表本身就内置了这种映射过程，比如折线图把数据映射到『线』，柱状图把数据映射到『长度』。一些更复杂的图表，如 graph、事件河流图、treemap 也都会做出他们内置的映射。
此外，ECharts 还提供了 visualMap 组件 来提供通用的视觉映射。visualMap 组件中可以使用的视觉元素有：
图形类别（symbol）、图形大小（symbolSize）
颜色（color）、透明度（opacity）、颜色透明度（colorAlpha）、
颜色明暗度（colorLightness）、颜色饱和度（colorSaturation）、色调（colorHue）
### ECharts中的事件和行为
在ECharts的图表中用户的操作将会触发相应的事件。开发者可以监听这些事件，然后通过回调函数做相应的处理，比如跳转到一个地址，或者弹出对话框，或者做数据下钻等等。
ECharts3中绑定事件跟2一样都是通过on方法，但是事件名称比2更加简单，在ECharts3中，事件名称对应DOM事件名称，均为小写的字符串，如下。是一个绑定点击操作的示例：
```
myChart.on('click', function(params) {
	console.log(params.name);
})
```
在ECharts中事件分为两种类型，一种是用户鼠标操作点击，或者hover图表的图形时触发的事件，还有一种是用户在使用可以交互的组件后触发的行为事件，例如在切换图例开关时触发的‘legendselectchanged’事件，数据区域缩放时触发的‘datazoom’事件等等。
#### 鼠标事件的处理
ECharts支持常规的鼠标事件类型，包括
‘click’，‘dbclick’，‘mousedown’，‘mousemove’，‘mouseup’，‘mouseover’，‘mouseout’，‘globalout’，‘contextmenu’事件。示例：
```
// 基于准备好的dom，初始化ECharts实例
var myChart = echarts.init(document.getElementById('main'));

// 指定图表的配置项和数据
var option = {
    xAxis: {
        data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
};
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
// 处理点击事件并且跳转到相应的百度搜索页面
myChart.on('click', function (params) {
    window.open('https://www.baidu.com/s?wd=' + encodeURIComponent(params.name));
});
```
使用 query 只对指定的组件的图形元素的触发回调：
```
chart.on(evenName,query,handler);
query可为string或者Object
```
