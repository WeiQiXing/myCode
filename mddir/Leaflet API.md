## Leaflet API
---
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





