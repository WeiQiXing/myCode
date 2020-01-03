## Leaflet API
---
### Leaflet中常用地图服务类型
**OGC标准**
OGC全称Open Geospatial Consortium,是一个非盈利的、国际化的、自愿协商的标准化组织，它的主要目的就是制定与空间信息、基于位置服务相关的标准。
在GIS领域，OGC已经是一个比较官方的标准化机构了，它不但包括了ESRI、Google、Oracle等业界强势企业作为其成员，同时还和W3C、ISO、IEEE等协会或组织结成合作伙伴关系。
**OGC标准化服务**
Keyhole Markup Language：简称KML，是由Google旗下的Keyhole公司开发和维护的一种基于XML的标记语言，利用XML语法格式描述地理空间数据（如点、线、面、多边形和模型等），适合网络环境下的地理信息协作与共享。
Web Map Service：简称WMS，该标准定义了一些操作，这些操作允许用户在分布式的环境下通过HTTP对空间数据进行出图等操作。
Web Map Tile Service：简称WMTS，该标准定义了一些操作，这些操作允许用户访问切片地图。WMTS可能是OGC首个支持RESTful访问的服务标准。
Web Feature Service：简称WFS，该标准定义了一些操作，这些操作允许用户在分布式的环境下通过HTTP对空间数据进行查询、编辑等操作。
**非OGC标准化服务**
矢量地图：通常指代ArcGIS Server发布的Rest类型服务，该服务可以把矢量数据直接转换为web服务发布到互联网上，并可以完整保存数据的属性而无需额外增加属性服务。
矢量切片地图：是将矢量地图和栅格地图的特点结合起来，使得发布的数据服务既包含了矢量地图数据质量完好、属性信息完整的特点，又将栅格地图的切片原理结合起来，既将矢量数据利用某种算法（而不是真实的切断）以切片的形式在浏览器中表现出来，已达到快速访问的目的。
**Mapbox**是Leaflet的超集，是基于leaflet开发的地图引擎，其中mapbox-gl.js库支持浏览器WebGL渲染，可以展示仿真三维的数据表现。

### Leaflet的创建
通过对一个\<div>元素的DOM ID实例化一个地图对象，示例：
```
import * as L from 'leaflet'
var map = L.map('map', {
	// 设置中心点
	center: [30.25, 120.01],
	// 设置缩放
	zoom: 13
});
```
地图对象创建时可以添加选项，上述的center和zoom就是选项之一，其他选项：
| 选项 | 类型 | 默认 | 描述 |
| --- | --- | --- | --- |
| zoomControl | Boolean | true | 默认是否将缩放控件添加到地图 |
| closePopupOnClick | Boolean | true | 如果不希望用户单击地图时弹出窗口关闭，设false |
| trackResize | Boolean | true | 地图是否自动处理浏览器窗口大小调整以更新自身 |
| boxZoom | Boolean | true | 通过按住shift键同时拖动鼠标，地图是否可以缩放到指定的矩形区域中 |
| doubleClickZoom | Boolean/String | true | 按住shift键，是否可以通过双击地图来放大地图和通过双击来缩小地图 |
| dragging | Boolean | true | 地图是否可以通过鼠标/触摸拖动 |
| crs | CRS | L.CRS.EPSG3857 | 要使用的坐标参考系 |
| keyboard | Boolean | true | 使地图可聚焦，并允许用户使用键盘箭头和+/-键浏览地图 |
| scrollWheelZoom | Boolean | true | 使用鼠标滚轮是否可以缩放地图，如果通过center，则无论鼠标在何处，它都会缩放到视图的中心 |

### Leaflet的事件(events)
图层事件
| 事件 | 数据 | 描述 |
| --- | --- | --- |
| baselayerchange | LayersControlEvent | 通过图层控件更改基本图层时触发 |
| layeradd | LayerEvent | 当新图层添加到地图时触发 |
| layerremove | LayerEvent | 从地图上删除某些图层时触发 |
地图状态变更事件
| 事件 | 数据 | 描述 |
| --- | --- | --- |
| zoomlevelschange | Event | 由于添加或删除图层而更改地图上的缩放级别数量时触发 |
| resize | ResizeEvent | 调整地图大小时触发 |
| unload | Event | 当使用remove方法销毁地图时触发 |
| zoom | Event | 在缩放级别的任何更改(包括缩放动画和动态动画)期间反复触发 |
| move | Event | 在地图的任何移动过程中反复触发，包括平移和飞行动画 |
| zoomend | Event | 更改任何动画后，地图更改时触发 |
| moveend | Event | 地图中心停止更改(例如，用户停止拖动地图)时触发 |
弹出事件、工具提示事件和定位事件
| 事件 | 数据 | 描述 |
| --- | --- | --- |
| popupopen | PopupEvent | 在地图中打开弹出窗口时触发 |
| popupclose | PopupEvent | 当地图中的弹出窗口关闭时触发 |
| autostart | Event | 打开弹出窗口时地图开始自动平移时触发 |
| tooltipopen | TooltipEvent | 在地图上打开工具提示时触发 |
| tooltipclose | TooltipEvent | 地图中的工具提示关闭时触发 |
| locationerror | ErrorEvent | 当地理位置(使用locate方法)失败时触发 |
| locationfound | LocationEvent | 当地理定位(使用locate方法)成功进行时触发 |
互动事件
| 事件 | 数据 | 描述 |
| --- | --- | --- |
| click | MouseEvent | 当用户点击地图时触发 |
| dbclick | MouseEvent | 当用户双击地图时触发 |
| mousedown | MouseEvent | 当用户在地图上按下鼠标按钮时触发 |
| mouseup | MouseEvent | 当用户释放地图上的鼠标按钮时触发 |
| mouseover | MouseEvent | 当鼠标进入地图时触发 |
| mouseout | MouseEvent | 当鼠标离开地图时触发 |
| mousemove | MouseEvent | 当鼠标移开地图上时触发 |
| keypress | KeyboardEvent | 当地图聚焦时用户按下键盘上的键时触发 |
| preclick | MouseEvent | 在地图上单击鼠标之前触发 |

### Leaflet的方法(Methods)
| 方法 | 返回值 | 描述 |
| --- | --- | --- |
| addControl(\<Control> control) | this | 将给定的控件添加到地图 |
| removeControl(\<Control> control) | this | 从地图上删除给定的控件 |
| addLayer(\<layer> layer) | this | 将给定图层添加到地图 |
| removeLayer(\<Layer> layer) | this | 从地图中删除给定的图层 |
| hasLayer(\<Layer> layer) | Boolean | 返回true当前是否将给定图层添加到地图中 |
| openPopup(\<Popup> popup) | this | 在关闭先前打开的窗口的同时打开指定的弹出窗口 |
| closePopup(\<Popup> popup) | this | 关闭先前用openPopup打开的弹出窗口 |
修改地图状态的方法
| 方法 | 返回值 | 描述 |
| --- | --- | --- |
| setView(\<LatLng> center,\<Number> zoom,\<Zoom/pan_options> options?) | this | 使用给定的动画选项设置地图视图(地理中心和缩放) |
| setZoom(\<Number> zoom,\<Zoom/pan_options> options?) | this | 设置地图的缩放比例 |
| ZoomIn(\<Number> delta?,\<Zoom opetions> options?) | this | 将地图的缩放比例增加到delta，同ZoomOut |
| panTo(\<LatLng> latlng, \<Pan options> options?) | this | 将地图平移到给定的中心 |
| stop() | this | 停止当前正在运行的panTo或flyTo动画 |
地理位置定位方法和其他方法
| 方法 | 返回值 | 描述 |
| --- | --- | --- |
| locate(\<Locate options> options?) | this | 尝试使用GeolocationAPI定位 |
| addHandler(\<String> name, \<Function> HandlerClass) | this | Handler给定地图的名称和构造函数，将其添加到地图中 |
| getPanes() | Object | 返回一个普通对象，该对象包含所有窗格的名称作为键，并包含所有窗格的值 |
| getCenter() | LatLng | 返回地图视图的地理中心 |
| getZoom() | Number | 返回地图视图的当前缩放级别 |
| getSize() | Point | 返回地图容器的当前大小(以像素为单位) |
| distance(\<LatLng> latlng1,\<LatLng> latlng2) | Number | 根据地图的CRS返回两个地理坐标之间的距离。默认距离以米为单位 |
| on(\<Object> eventMap) | this | 添加一组类型/侦听器对，例如{click: onClick} |
| off(\<Object> eventMap) | this | 删除一组类型/侦听器对 |
### Leaflet的属性
| 属性 | 类型 | 描述 |
| --- | --- | --- |
| boxZoom | Handler | 框(使用鼠标按住Shift键并拖动)缩放处理程序 |
| doubleClickZoom | Handler | 双击缩放处理程序 |
| dragging | Handler | 地图拖动处理程序 |
| keyboard | Handler | 键盘导航处理程序 |
| scroolWheelZoom | Handler | 滚轮缩放处理程序 |

### Leaflet的记号(marker)
L.Marker用于在地图上显示可点击/拖动的图标，示例：
```
L.marker([30.25,120.01]).addTo(map);
```
| 方法 | 返回值 | 描述 |
| --- | --- | --- |
| toGeoJSON() | Object | 返回一个GeoJSON标记的表示形式 |
| getLatLng() | LatLng | 返回标记的当前地理位置 |
| setLatLng(\<LatLng> latlng) | this | 将标记位置更改为定点 |
| setIcon(\<Icon> icon) | this | 更改标记图标 |
| setOpacity(\<Number> opacity) | this | 更改标记的不透明度 |

### Leaflet的弹出(Popup)
用于在地图的某些位置打开弹出窗口，使用Map.openPopup打开弹出窗口，同时确保一次只打开一个弹出窗口，如果只想将弹出窗口绑定到标记单击，然后将其打开，则非常简单：
```
marker.bindPopup(popupContent).openPopup();
```
折线之类的路径叠加层也有一种bindPopup方法。这是在地图上打开弹出窗口的更复杂的方法：
```
var popup = L.popup()
	.setLatLng(latlng)
	.setContent('<p>Hello world!<br />This is a nice popup.</p>')
	.openOn(map);
```
### Leaflet的瓷砖图层(tileLayer)
用于在地图上加载和显示图块图层，示例：
```
L.tileLayer(url, {foo: 'bar'}).addTo(map);
```
url的形式：
```
'http://{s}.somedomain.com/blabla/{z}/{x}/{y}{r}.png'
```
{s}装置可用的子域中的一个，{z}-缩放级别，{x}以及{y}-瓷砖坐标，{r}可用于在网址中添加“@2x”以加载视图网膜图块。

### Leaflet的折线(PolyLine)
用于在地图上绘制折线叠加层的类，示例：
```
var latlngs = [
	[45.51, -122.68],
	[37.77, -122.43],
	[34.04, -118.2]
];
var polyline = L.polyLine(latlngs, {color: 'red'}).addTo(map);
map.fitBounds(polyline.getBounds());
```
### Leaflet的多边形(Polygon)
用于在地图上绘制多边形叠加层的类，示例：
```
var latlngs = [[37, -109.05],[41, -109.03],[41, -102.05],[37, -102.04]];
var polygon = L.polygon(latlngs, {color: 'red'}).addTo(map);
map.fitBounds(polygon.getBounds());
// 还可以传递由latlng组成的数组的数组，第一个数组代表外形，其他数组代表外形中的孔
var latlngs = [
  [[37, -109.05],[41, -109.03],[41, -102.05],[37, -102.04]], 
// outer ring
  [[37.29, -108.58],[40.71, -108.58],[40.71, -102.50],[37.29, -102.50]] // hole
];
```
### Leaflet的长方形(Rectangle)
用于在地图上绘制矩形叠加层的类，示例：
```
// define rectangle geographical bounds
var bounds = [[54.559322, -5.767822], [56.1210604, -3.021240]];
// create an orange rectangle
L.rectangle(bounds, {color: "#ff7800", weight: 1}).addTo(map);
// zoom the map to the rectangle bounds
map.fitBounds(bounds);
```
### Leaflet的圆(Circle)
用于在地图上绘制原型叠加层的类，示例：
```
L.circle([50.5,30.5],{radius: 200}).addTo(map);
```



## Three.js

什么是three.js，简单来说可以理解成three+js，也就是使用JavaScript来写3D程序。Threejs比c++用更少的代码，而且更容易。更酷。可以通过[Threejs](https://github.com/mrdoob/three.js)下载代码。
### 源码目录结构
**Build目录**：包含两个文件，three.js 和three.min.js 。这是three.js最终被引用的文件。一个已经压缩，一个没有压缩的js文件。
**Docs目录**：这里是three.js的帮助文档，里面是各个函数的api，可惜并没有详细的解释。试图用这些文档来学会three.js是不可能的。
**Editor目录**：一个类似3D-max的简单编辑程序，它能创建一些三维物体。
**Examples目录**：一些很有趣的例子demo，可惜没有文档介绍。对图像学理解不深入的同学，学习成本非常高。
**Src目录**：源代码目录，里面是所有源代码。
**Test目录**：一些测试代码，基本没用。
**Utils目录**：存放一些脚本，python文件的工具目录。例如将3D-Max格式的模型转换为three.js特有的json模型。
**.gitignore文件**：git工具的过滤规则文件，没有用。
**CONTRIBUTING.md文件**：一个怎么报bug，怎么获得帮助的说明文档。
**LICENSE文件**：版权信息。
**README.md文件**：介绍three.js的一个文件，里面还包含了各个版本的更新内容列表。

### 引入Three.js示例
```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <style>canvas { width: 100%; height: 100% }</style>
</head>
<body>
    <script src="https://raw.github.com/mrdoob/three.js/master/build/three.js"></script>
</body>
</html>
```
### 三大组件
#### 场景scene
Threejs中场景只有一种，即THREE.Scene来表示，构建一个场景也很简单，只要new一个对象就行：
```
var scene = new THREE.Scene();
```
场景是所有物体的容器，如果要显示一个苹果，就要将苹果对象添加进场景中。
#### 相机camera
第二个组件是相机，相机决定了场景中哪个角度的景色会显示出来，相机就像人的眼睛一样，人站在不同位置，抬头或者低头就能看到不同的景色。
场景只有一种，但是相机却有很多种，不同的相机确定了成像的各个方面，通过设定参数可以使其产生不同的效果。
```
var camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
```
#### 渲染器renderer
最后一步就是设置渲染器，渲染器决定了渲染的结果应该画在页面的什么元素上面，并且以怎样的方式来绘制。
```
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
```
渲染器renderer的domElement元素表示渲染器中的画布，这里所有的渲染都是画在domElement上的，所以这里的appendChild表示将这个domElement挂接在body下面，这样渲染的结果就能够在页面中显示了。
接下来就是将物体添加到场景中：
```
var geometry = new THREE.CubeGeometry(1,1,1); 
var material = new THREE.MeshBasicMaterial({color: 0x00ff00});
var cube = new THREE.Mesh(geometry, material); 
scene.add(cube);
```
### 渲染
渲染需要使用渲染器，结合相机和场景来得到结果画面，实现这个功能的函数是renderer.render(scene,camera);
渲染函数的原型是：render(scene,camera,renderTarget,forceClear);
各个参数的意义是：
scene:定义的场景
camera:定义的相机
renderTarget:渲染的目标，默认渲染到定义的render变量中
forceClear:每次绘制之前都将画布的内容给清除，即使自动清除标志autoClear为false，也会清除。
### 循环渲染
渲染有两种方式，实时渲染和离线渲染。
```
function render() {
    cube.rotation.x += 0.1;
    cube.rotation.y += 0.1;
    renderer.render(scene, camera);
    requestAnimationFrame(render);
}
```
其中一个重要的函数是requestAnimationFrame，这个函数就是让浏览器去执行一次参数中的函数，这样通过上面render中调用requestAnimationFrame函数，requestAnimationFrame()函数又让render()再执行一次，就形成了我们通常所说的游戏循环了。
### 定义一个点
在三维空间中的某一个点可以用一个坐标点来表示，一个坐标点由x,y,z三个分量构成。在three.js中，点可以在右手坐标系中表示：空间几何中，点可以用一个向量来表示，在threejs中也可使用一个向量来表示的：
```
THREE.Vector3 = function(x,y,z){
this.x = x||0;
this.y = y||0;
this.z = z||0;
};
```

--- 
以下为超图基于Leaflet开发的API

--- 
**地图叠加**，**平面坐标系底图**
L.supermap.tiledMapLayer(url,options)
Example:
	L.supermap.tiledMapLayer(url).addTo(map);
Extends:
	L.TileLayer
Events:
	tilesetsinfoloaded	瓦片集信息设置完成后触发
	tileversionschanged	切片的版本切换和重绘成功之后触发。
Methods:
	getScale(zoom) -> {number} 根据缩放级别获取比例尺
	getScaleFromCoords(coords) -> {number} 根据行列号获取比例尺
	getTileUrl(coords) -> {string} 根据行列号获取瓦片地址
**自定义比例尺**
L.Proj.CRS(srsCode,options) 
Example:
```
var crs =L.Proj.CRS("EPSG:4326",{
		origin: [-180,90],
		scaleDenominators: [2000,1000,500,200,100,50,20,10],
	});
	var map=L.map('map',{
		crs:crs
	})
```
Extens:
	L.Class
Methods:
	scale(zoom) 通过缩放级别获取比例尺值
	zoom(scale) -> {number} 根据比例尺返回缩放级别
**地图信息**
L.supermap.mapService(url,options)
Example:
```
L.supermap.mapService(url)
  .getMapInfo(function(result){
  
  })
```
Extends:
	L.supermap.ServiceBase
Events:
	destroy 资源释放成功后触发
	initialized 构造函数构造成功后触发
Methods:
	destroy() 释放资源，将引用的资源属性置空
	getMapInfo(callback) 获取地图信息
	getTilesets(callback) 获取切片列表信息
**地图量算**，**量算参数类**
L.supermap.measureService(url,options)
Example:
```
L.supermap.measureService(url).measureDistance({
	geometry:xxx
},function(result){
})
```
Extends:
	L.supermap.ServiceBase
Events:
	destroy 资源释放成功后触发
	initialized 构造函数构造成功后触发
Methods：
```
L.supermap.measureService.measure(type,params,callback)
destroy() 释放资源，将引用的资源属性置空
measureArea(params,callback) 测面积
measureDistance(params,callback) 测距
```
SuperMap.MeasureParameters()
Members:
	distanceMode() 用来指定量算的方式按球面长度“Geodesic”或者平面长度“Planar”来计算。
Example:
```
var param=new SuperMap.MeasureParameters(getmetry,{distanceMode:'Planar'});
```
geometry object 要量算的几何对象
点类型可以是：
	SuperMap.Geometry.Point|L.Point|L.GeoJSON|ol.geom.Point|ol.format.GeoJSON
线类型可以是：
	SuperMap.Geometry.LineString|SuperMap.Geometry.LinearRing|L.Polyline|L.GeoJSON|ol.geom.LineString
面类型可以是：
	SuperMap.Geometry.Polygon|L.Polygon|L.GeoJSON|ol.geom.Polygon|ol.format.GeoJSON
**查询类**
L.supermap.featureService(url,options)
Example:
```
L.supermap.featureService(url)
	.getFeaturesByIDs(params,function(result){
	
	})
```
Extends
	L.supermap.ServiceBase
Events:
	destroy 资源释放成功后触发
	initialized 构造函数构造成功后触发
Methods：
	destroy() 释放资源，将引用的资源属性置空
	editFeatures(params,callback) 地物编辑服务
	getFeaturesByBounds(params,callback,resultFormat) 数据集bounds查询服务
	getFeaturesByBuffer(params,callback,resultFormat) 数据集buffer查询服务
	getFeaturesByGeometry(params,callback,resultFormat) 数据集几何查询服务类
	getFeaturesByIDs(params,callback,resultFormat) 数据集ID查询服务
	getFeaturesBySQL(params,callback,resultFormat) 数据集SQL查询服务
**空间分析服务类**
L.supermap.spatialAnalystService(url,options)
Example:
```
L.supermap.spatialAnalystService(url)
	.bufferAnalysis(params,function(result){
	
	})
```
Extends:
L.supermap.ServiceBase
Methods:
```
bufferAnalysis(params,callback,resultFormat) 缓冲区分析
densityAnalysis(params,callback,resultFormat) 点密度分析
generateSpatialData(params,callback,resultFormat) 动态分段分析
geometrybatchAnalysis(params,param,callback,resultFormat) 批量空间分析
geoRelationAnalysis(params,callback,reslutFormat) 空间关系分析
getAreaSolarRadiationResult(params, callback, resultFormat) 地区太阳辐射
interpolationAnalysis(params, callback, resultFormat) 插值分析
mathExpressionAnalysis(params, callback, resultFormat) 栅格代数运算
overlayAnalysis(params, callback, resultFormat) 叠加分析
routeCalculateMeasure(params, callback, resultFormat) 路由测量计算
routeLocate(params, callback, resultFormat) 路由定位
surfaceAnalysis(params, callback, resultFormat) 表面分析
terrainCurvatureCalculate(params, callback, resultFormat) 地形曲率计算
```

### Turf.js
Turfjs是一个用JavaScript编写的模块化的GIS引擎，根据GeoJSON数据处理执行地理空间任务，可以在服务器或在浏览器上运行，功能虽然不如geotools丰富，但在geojson格式数据处理上，绝对一流。
主要用于实现在网页端空间几何对象关系的计算，点、线、面之间包含、相交等一系统运算。
Turf是一个用于地理空间分析的库-大量的任务，例如计算面积和距离以及将点连接到多边形，使人们能够查看其数据中的图案或关系。空间分析在许多行业中使用：查找最近的咖啡店，计算旅行时间并显示公用事业使用情况的区域统计信息。它也是GIS的重要组成部分，其中许多问题都可以通过空间分析解决

### MapBox 
MapBox是移动和Web应用程序的地理信息数据平台，提供了丰富精美的在线地图及地图风格设计器；提供了位置搜索服务、导航服务及其API；提供了各种端的SDK，SDK开源免费。

