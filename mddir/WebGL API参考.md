## SuperMapWebGL API参考

![image-20191129090832261](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20191129090832261.png)

### Core库
---
#### Cartographic
	new Cesium.Cartographic(longitude, latitude, height)
	由经度、纬度、高度定义的空间位置。

| 方法名| 参数 | 返回值类型 | 作用  |
| ---- | ----  | ---- | ---- |
|   .clone   |   cartographic,result   |  Cartographic    |  复制实例    |
|   .equals   |   left,right   | Boolean     |  比较两张地图，值相等返回true，否则返回false |
|   .fromDegrees   |   longitude,latitude,height,result   |   Cartographic   |  根据以度为单位的经纬度数值创建Cartographic实例    |

#### HypsometricSetting
	new Cesium.HysometricSetting()
	分层设色类，该类主要用于定制三维模型渲染显示方案

#### Ellipsoid
	new Cesium.Ellpsoid(x,y,z)
#### ColorTable
	new Cesium.ColorTable()
	颜色表类
#### CesiumTerrainProvider
	new Cesium.CesiumTerrainProvider(options)
	提供地形切片，通过STK地形服务或者SuperMap iServer REST API
Example：
```
var  terrainProvider = new Cesium.CesiumTerrainProvider({
	                        url : ‘http://localhost:8090/Terrain’,
		                    requestWaterMask : true,
		                    requestVertexNormals : true,
		                    isSct : true
                     });
var viewer = new Cesium.Viewer(‘cesiumContainer’,{
                  terrainProvider : terrainProvider
             });
```
#### Cartesian3
	new Cesium.Cartesian3(x,y,z)
	三维笛卡尔坐标点。
#### CredentialType
	CredentialType()
	密钥类型

### DataSource
---
#### DataSource
	new Cesium.DataSource()
	定义数据源的接口，可将任意数据转换为EntityCollection供使用。此对象是用于文档目的的接口，不能直接实例化。
#### Entity
	new Cesium.Entity(options)
	实体实例类，它将多种可视化对象聚合到单个高级对象中。
### Fly
---
#### FlyManager
	new Cesium.FlyManager(options)
	飞行管理类，控制飞行的开始、暂停、停止以及站点事件等。
Example：
```
var routes = new Cesium.RouterCollection();
routes.fromFile('./test.fpf');
var fm = new Cesium.FlyManager({
	scene: scene,
	routes: routes
});

```
Members:
```
currentRoute: Route // 获取当前飞行路线
currentStopIndex: Number // 获取或者设置当前站点索引(指定从该站点开始飞行)
playRate: Number // 获取或者设置飞行路线的飞行速率
routes: RouteCollection // 获取或者设置当前路线集合对象
```
Methods
```
getAllRouteStops -> Array <RouteStop> // 获取当前飞行路线的所有站点
pause() // 暂停飞行
play() // 开始飞行
stop() // 停止飞行
viewToStop(stop) // 站点定位
```
#### StopPlayMode
	StopPlayMode()
	站点模式，包括普通模式和环绕飞行模式
Members：
```
Cesium.StopPlayMode.StopAround: String // 环绕飞行模式
cesium.StopPlayMpde.StopPause: String // 普通模式
```
#### RouteStop
	new Cesium.RouteStop(options)
	飞行站点对象类。飞行路线由多个飞行站点构成
Members：
```
duration: Number // 获取或设置当前站点到下一站点的飞行持续时间
heading: Number // 获取或者设置当前站点的相机heading角度
index: Number // 获取当前站点
point: Cartesian3 // 获取当前站点的位置
speed: Number // 获取或者设置当前站点的飞行速度
promise: object // 获取或者设置当前站点的promise，用于异步操作站点事件
```
Example：
```
flyManager.stopArrived.addEventListener(function(routeStop){
         audioEle.play();
         var defer = Cesium.when.defer();
         //播放音频的异步处理
         routeStop.promise = defer;
         audioEle.onended = function(){
              defer.resolve(true);
              routeStop.promise = undefined;
            };
          });
```
#### RouteCollection
	new Cesium.RouteCollection(entityCollection)
	飞行路线集合对象类
Example：
```
var routes = new Cesium.RouteCollection(entityCollection);
routes.fromFile('./test.fpf');
```
Members:
```
ready: Boolean // 获取路线集合是否准备就绪
routes: Array<Route> // 获取路线集合数组
```
Methods：
```
addRoute(route) // 添加路线对象
fromFile(url) // 异步加载记录飞行路线的fpf文本文件
```
#### Route
	new Cesium.Route(options, isStopVisible,routeName,speed,isAlongline,totalDuration)
	飞行路线对象类



### Scene
---
#### ScanEffectMode
	ScanEffectModel()
	扫描线效果模式，包括圆环状扫描模式和线状扫描模式
	Cesium.ScanEffectMode.CIRCLE 圆环状扫描模式
	Cesium.ScanEffectMode.LINE 线状扫描模式
#### DiscardColorTileImagePolicy
	new Cesium.DiscardColorTileImagePolicy()
	图片像素大于透明度所设置的值则不创建对该切片对应的纹理，并丢弃寻找可用父节点代替
Methods：
```
isReady() -> Boolean
shouldDiscardImage(image) -> Boolean
```
#### FieldLayer3D
	new Cesium.FieldLayer3D(context)
	场数据图层类，通过该图层加载场数据
Members：
```
fieldData: Array // 获取或者设置图层的场数据
layerBounds: Rectangle // 获取或者设置图层数据的X、Y方向范围
type: String // 获取该图层类型标识
visible: Boolean // 获取或设置图层的可见性
```
Methods：
```
destroy() -> undefined // 销毁对象并释放其webgl资源
```
#### ColorCorrection
	new Cesium.ColorCorrection()
	颜色校正类，此类用于场景图像的渲染后处理，可以调节图像的亮度、对比度、饱和度以及色调。
Members：
```
brightness: Number // 获取或设置图像的亮度
contrast: Number // 获取或设置图像的对比度
hue: Number // 获取或设置图像的色调
saturation: Number // 获取或设置图像的饱和度
show: Boolean // 获取或设置图像的颜色校正效果是否开启
```
#### DepthOfFieldEffect
	new Cesium.DepthOfFieldEffect()
	景深效果类，景深效果是模拟摄像机的光学成像效果，在聚焦的区域成像相对清晰，远离聚焦的区域成像逐渐模糊。景深效果画面镜头感更强，可以将观察者的注意力集中在聚焦的区域，而且大景深能塑造微距的模型效果。
Members：
```
Cesium.DepthOfFieldEffect.blurRadius: Number // 获取或设置焦外的模糊半径
Cesium.DepthOfFieldEffect.focalDistance: Number // 获取或设置相机的焦距
Cesium.DepthOfFieldEffect.focalRange: Number // 获取或设置完全聚焦的区域范围
Cesium.DepthOfFieldEffect.fStop: Number // 获取或设置相机镜头的光圈F值，值小景深浅
Cesium.DepthOfFieldEffect.show: Boolean // 获取或者设置是否开启景深效果
```
#### ScanEffect
	new Cesium.ScanEffect()
	扫描线效果类
Members：
```
Cesium.ScanEffect.centerPosition: Number // 获取或设置扫描线的中心点位置
Cesium.ScanEffect.color: Number // 获取或设置扫描线的颜色
Cesium.ScanEffect.lineMoveDirection: Number // 获取或设置线状扫描线的运行方向
Cesium.ScanEffect.lineWidth: Number // 获取或者设置线状扫描线的宽度
Cesium.ScanEffect.mode: Object // 获取或设置扫描线效果模式，包括圆环扫描模式和线状扫描模式
Cesium.ScanEffect.period: Number // 获取或设置扫描线的运行周期 
Cesium.ScanEffect.show: Boolean // 获取或设置是否开启扫描线效果
Cesium.ScanEffect.speed: Number // 获取或设置扫描线的运行速度
```
#### BloomEffect
	new Cesium.BloomEffect()
	泛光效果类
Members：
```
bloomIntensity： Number // 获取或设置泛光强度值
show: Boolean // 获取或设置是否开启泛光效果
threshold: Number // 获取或设置泛光亮度阈值
```
#### BingMapImageryProvider
	new Cesium.BingMapsImageryProvider(options)
	BingMap影像服务提供者
|Name	|Type	|Description|
| --- | --- | --- |
|options	|Object	|对象具有以下属性:|
|Name	|Type	|Default Description|
|url	|String		|Bing Maps服务url。|
|key	|String		|optional应用程序所使用的key，可至官网https://www.bingmapsportal.com/ 申请。如果未提供key，将使用BingMapsApi.defaultKey；如果BingMapsApi.defaultKey也未定义，将写入消息提醒您创建申请。使用Bing Maps时，在没有创建单独key的情况下不能部署应用程序。|
|tileProtocol	|String		|optional加载瓦片时使用的协议，例如 'http:'或'https:'。默认情况下，使用与页面相同的协议加载|
|mapStyle	|BingMapsStyle	|BingMapsStyle.AERIAL	|optional服务类型。culture	String	''optional详细内容请参考http://msdn.microsoft.com/en-us/library/hh441729.aspx |
|ellipsoid	|Ellipsoid		|optional椭球体。未定义时默认使用WGS84椭球体。|
|tileDiscardPolicy	|TileDiscardPolicy		|optional决定切片是否无效及废弃的策略。未指定时默认使用DiscardMissingTileImagePolicy。|
|proxy	|Proxy		|optional请求的代理。此对象有一个getURL函数，如果需要，返回代理的URL。|
Example:
```
var bing = new Cesium.BingMapsImageryProvider({
    url : 'https://dev.virtualearth.net',
    key : 'get-yours-at-https://www.bingmapsportal.com/',
    mapStyle : Cesium.BingMapsStyle.AERIAL
});
```
#### Scene
	new Cesium.Scene(options)
	三维场景类，他是所有三维图形对象和状态的容器，通常不直接创建场景，而是由CesiumWidget隐式创建。
Members：
```
camera: Camera // 获取当前场景的相机对象
canvas: Element // 获取scene绑定的canvas元素
globe: Globe // 获取地球对象
id: String // 获取当前场景的id
imageryLayers: ImageryLayerCollection // 获取当前场景影像图层集合
layers: Layers // 获取当前场景的三维切片缓存图层集合
lightSource // 获取当前场景中的光源
mapProjection: MapProjection // 获取地图投影对象，用于2D或者Columbus View模式
mode: SceneMode // 获取当前场景的模式
terrainProvider: TerrainProvider // 获取或者设置当前场景的地形服务provider对象
```
Methods:
```
addFieldLayer(url) -> Promise // 根据url路径添加场数据图层，返回数据图层FieldLayer3D，异步创建图层对象
addLayerService(url,sceneName,layerName) // 添加场景图层服务
addLightSource(lightSource) ->Scene // 添加光源
addS3MGroupLayer(url,options,index) -> Promise // 添加S3M分组图层
addS3MTilesLayerByScp(url,options,index) -> Promise // 添加三维切片缓存图层
getHeight(lon,lat) ->Number // 根据经纬度坐标获取对应高度
getViewport(windowPosition) -> BoundingRectangle // 根据窗口坐标，获取当前场景视口
open(url) -> Promise // 打开iserver场景下服务的所有图层。
pick(windowPosition,width,height) -> Object // 场景拾取，返回在场景中该窗口位置对应的第一个图元对象，如果该位置没有任何物体则返回undefined。
```

#### MultiViewportMode
	多视口模式类
Members:
```
Cesium.MultiViewportMode.HORIZONTAL: Number // 水平跨越双视口模式
Cesium.MultiViewportMode.NONE: Number // 非多视口模式，即只有一个视口
Cesium.MultiViewportMode.QUAD: Number // 四视口模式
```
#### Scene
	new Cesium.Scene(options)
	三维场景类，它是所有三维图形对象和状态的容器，通常不直接创建对象，而是由CesiumWidget隐式创建。
Example：
```
var viewer = new Cesium.Viewer('Container');
var Scene = viewer.scene;
```
Members:
```
camera: Camera // 获取当前场景的相机对象
canvas: Element // 获取scene绑定的canvas元素
globe: Globe // 获取地球对象
id: String // 获取当前场景的id
layers: Layers // 获取当前场景的三维切片缓存图层集合
lightSource // 获取当前场景的光源
mapProjection: MapProjection // 获取地图投影对象，用于2D或者Columbus View模式
mode: SceneMode // 获取当前场景的模式
screenSpaceCameraController: ScreenSpaceCameraController // 获取当前场景的相机操作对象
terrainProvider: TerrainProvider // 获取或者设置当前场景的地形服务provider对象
terrainProviderChanged: Event // 获取当前场景地形服务provider改变事件
undergroundDepth: Number // 获取或者设置地下场景深度。默认1000米
undergroundMode: Boolean // 获取或者设置是否开启地下场景，默认值为false
```
Methods:
```
addFieldLayer(url) -> Promise // 根据url路径添加场数据图层
addLayerService(url,sceneName,layerName) // 添加场景图层服务
addLightSource(lightSource) -> Scene // 添加光源
addS3MGroupLayer(url,options,index) -> Promise // 添加S3M分组图层
addS3MTilesLayerByScp(url, options, index) -> Promise // 添加三维切片缓存图层
getHeight(lon,lat) -> Number // 根据经纬度坐标获取对应高度
getViewport(windowPosition) -> BoundingRectangle // 根据窗口坐标，获取当前场景视口
open(url) -> Promise // 打开iserver场景服务下的所有图层
pick(windowPosition,width,height) -> Object // 场景拾取，返回在场景中该窗口位置对应的第一个图元对象，如果该位置没有任何物体则返回undefined
pickPosition(windowPosition,result) -> Cartesian3 // 位置拾取，根据窗口坐标，从场景的深度缓冲区中拾取相应的位置，返回笛卡尔坐标需要支持深度纹理。
```
#### SuperMapImageryProvider
	new Cesium.SuperMapImageryProvider(options)
	提供影像切片，通过SuperMap iServer REST API
```
var provider = new Cesium.SuperMapImageryProvider({url: URL_CONFIG.ZF_IMG});
var layer = viewer.imageryLayers.addImageryProvider(provider);
// Members
readyPromise: Promise // 获取该服务的请求状态的promise
```
#### TiandituImageryProvider
	new Cesium.TiandituImageryProvider(options)
	天地图影像服务提供者类
Example：
```
var laberImagery = new Cesium.TiandituImageryProvider({
	mapStyle: Cesium.TiandituMapsStyle.CIA_C // 天地图全球中文注记服务
});
```
Members:
```
credit: String // 获取服务的描述信息
errorEvent: String // 错误事件
mapStyle: String // 获取服务类型
tileHeight: Number // 获取瓦片高度
url: String // 获取服务的url
```
#### Camera
	new Cesium.Camera(scene)
	相机类，它由位置、方向和视锥体(viewing frustum)由6个(上、下、左、右、近、远)平面限定，每个平面可由Cartesian4对象表示，其中x,y和z分量定义垂直于平面的单位向量，w分量是平面距原点/相机位置的距离。
Examples:
```
var camera = new Cesium.Camera(scene);
camera.position = new Cesium.Cartesian3();
camera.direction = Cesium.Cartesian3.negate(Cesium.Cartesian3.UNIT_Z, new Cesium.Cartesian3());
camera.up = Cesium.Cartesian3.clone(Cesium.Cartesian3.UNIT_Y);
camera.frustum.fov = Cesium.Math.PI_OVER_THREE;
camera.frustum.near = 1.0;
camera.frustum.far = 2.0;
```


#### Layers
	new Cesium.Layers()
	图层集合类，该类用于对场景中的所有图层进行管理
Members: layerQueue: Array // 获取图层列表
Methods:
```
add(layer) // 向图层集合添加一个图层
find(name) -> Layer // 根据图层名称查找图层对象
findByIndex(index) -> Layer // 根据指定索引查找图层对象
getSelectedLayers() -> S3MTilesLayer // 获取当前点击选中的S3M图层
pickFeatures(winpos,scene) // 查找特征要素信息
releaseSelection() // 释放被选择的图层对象
removeAll(destroy) // 删除图层集合中的所有图层对象
setSelectedLayer(layer) // 设置当前点击选中的S3M图层
```

---
#### Viewer
new Cesium.Viewer(container, options)
Viewer是用于构建应用程序的基础部件，它将所有标准的Cesium部件组合成一个可重复使用的包。
Example：
```
//初始化viewer部件
var viewer = new Cesium.Viewer('cesiumContainer', {
    //使用 STK World Terrain
    terrainProvider : new Cesium.CesiumTerrainProvider({
        url : 'https://assets.agi.com/stk-terrain/world'
    }),
    //使用OpenStreetMaps
    imageryProvider : Cesium.createOpenStreetMapImageryProvider({
        url : 'https://a.tile.openstreetmap.org/'
    }),
});

//添加基础拖放功能
viewer.extend(Cesium.viewerDragDropMixin);

//处理删除文件时遇到错误，显示弹出式警告。
viewer.dropError.addEventListener(function(dropHandler, name, error) {
    console.log(error);
    window.alert(error);
});
```
Members：
	animation：Animation 获取动画部件
	baseLayerPicker：BaseLayerPicker 获取基础图层拾取器对象
	bottomContainer： Element 获取窗口底部包含CreditDisplay及其他潜在信息的DOM对象。
	camera：Camera 获取相机对象
	canvas： Canvas 获取画布对象
	cesiumWidget：CesiumWidget 获取CesiumWidget对象
	clock： Clock 获取时钟对象
	container：Element 获取父容器
	scene：Scene 获取场景对象
	timeLine：Timeline 获取时间轴部件
Methods：
	destroy() 释放对象占用的资源。
	extend(mixin,options) 使用提供的mixin来扩展基础viewer功能
    flyTo(target,options)->Promise 相机飞向指定的实体、实体集或数据源。
    forceResize() 强制重调，使得部件重新考虑包括部件大小、credit放置等布局。
    render() 渲染场景


























