<template>
  <div class='ces' id="allContainer">
    <div id='toolbar' class='tool-bar'>
    <div class="cesium-search-control">
      <!-- 线路选择 -->
      <!-- <el-select value-key="id" size="small" v-model="form.line">
        <el-option v-for="(line) in lines" :key="line.id" :label="line.name" :value="line" />
      </el-select> -->
      <!-- 图层控制 -->
      <el-dropdown trigger="click">
        <el-button size="small">
          图层
          <i class="el-icon-arrow-down el-icon--right"></i>
        </el-button>
        <el-dropdown-menu slot="dropdown" class="cesium-layers">
          <el-tree
            :data="layers"
            show-checkbox
            default-expand-all
            node-key="code"
            ref="tree"
            highlight-current
            :props="layerProps"
            @check="layerChecked"
            @node-click="layerClick"
          ></el-tree>
        </el-dropdown-menu>
      </el-dropdown>
      <!-- 工具选择 -->
      <el-dropdown trigger="click" @command="toolSelect">
        <el-button size="small">
          工具
          <i class="el-icon-arrow-down el-icon--right"></i>
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item
            v-for="(tool, index) in tools"
            :key="index"
            :command="tool.name"
          >{{tool.name}}</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <!-- 车站定位 -->
      <el-dropdown trigger="click">
        <el-button size="small">
          车站定位
          <i class="el-icon-arrow-down el-icon--right"></i>
        </el-button>
        <el-dropdown-menu slot="dropdown" class="cesium-layers">
          <el-tree
            :data="stationlayers"
            show-checkbox
            default-expand-all
            node-key="code"
            ref="stationTree"
            highlight-current
            :props="stationLayerProps"
            @check="stationLayerChecked"
            @node-click="stationLayerClick"
          ></el-tree>
        </el-dropdown-menu>
      </el-dropdown>
      <!-- <el-button type="button" size="small" plain id="chooseView">绘制可视域</el-button>
      <el-button type="button" size="small" plain id="clearView">清除</el-button>
      <div id="wapper" style="display:none">
        <div id="login">
          <span class="close" aria-hidden="true">x</span>
          <form>
            <h1>属性编辑</h1>
            <p>
            <div>
              <label>方向(度)</label>
              <input type="range" id="direction" min="0" max="360" step="1.0" title="方向"
                data-bind="value: direction, valueUpdate: 'input'">
              <input type="text" size="5" data-bind="value: direction">
            </div>
            <div>
              <label>翻转(度)</label>
              <input type="range" id="pitch" min="-90" max="90" step="1.0" value="1" title="翻转"
                data-bind="value: pitch, valueUpdate: 'input'">
              <input type="text" size="5" data-bind="value: pitch">
            </div>
            <div>
              <label>距离(米)</label>
              <input type="range" id="distancem" min="1" max="500" step="1.0" value="1" title="距离"
                data-bind="value: distancem, valueUpdate: 'input'">
              <input type="text" size="5" data-bind="value: distancem">
            </div>
            <div>
              <label>水平视场角(度)</label>
              <input type="range" id="horizonalFov" min="1" max="120" step="1" value="1" title="水平视场角"
                data-bind="value: horizontalFov, valueUpdate: 'input'">
              <input type="text" size="5" data-bind="value: horizontalFov">
            </div>
            <div>
              <label>垂直视场角(度)</label>
              <input type="range" id="verticalFov" min="1" max="90" step="1.0" value="1" title="垂直视场角"
                data-bind="value: verticalFov, valueUpdate: 'input'">
              <input type="text" size="5" data-bind="value: verticalFov">
            </div>
            <p>
            <div class="square">
              <label>可见区域颜色</label><input class="colorPicker" data-bind="value: visibleAreaColor,valueUpdate: 'input'"
                id="colorPicker1"/>
            </div>
            <div class="square">
              <label>不可见区域颜色</label><input class="colorPicker"
                data-bind="value: invisibleAreaColor,valueUpdate: 'input'"
                id="colorPicker2"/>
            </div>
            <p><label>本例中观察者附加高度：1.8 米</label></p>
          </form>
        </div>
      </div> -->
    </div>
    <el-card
      class="cesium-measure-area"
      :body-style="{padding:'6px'}"
      v-show="toolShow==='measure'">
      <div slot="header" class="clearfix">
        <span>量算</span>
        <el-button size="small" class="is-circle cesium-tool-close" @click="toolShow=false">
          <i class="el-icon-close"></i>
        </el-button>
      </div>
      <el-button size="small" @click="measureSelect('distance')">测距</el-button>
      <el-button size="small" @click="measureSelect('area')">测面</el-button>
      <el-button size="small" @click="measureSelect('height')">测高</el-button>
      <el-button size="small" @click="measureSelect('clear')">清除</el-button>
    </el-card>
    <el-card class="cesium-measure-area" :body-style="{padding:'6px'}" v-show="toolShow==='fly'">
      <div slot="header" class="clearfix">
        <span>飞行漫游</span>
        <el-button size="small" class="is-circle cesium-tool-close" @click="toolShow=false">
          <i class="el-icon-close"></i>
        </el-button>
      </div>
      <el-button
        v-for="flyer in flyFiles"
        :key="flyer.id"
        class="text item"
        @click="fly(flyer.file)"
      >{{flyer.name }}</el-button>
    </el-card>
    <el-card
      class="cesium-measure-area"
      :body-style="{padding:'6px'}"
      v-show="toolShow==='transparency'">
      <div slot="header" class="clearfix">
        <span>透明度</span>
        <el-button size="small" class="is-circle cesium-tool-close" @click="toolShow=false">
          <i class="el-icon-close"></i>
        </el-button>
      </div>
      <div :style="{display:'flex',alignItems:'center'}">
        <span>倾斜摄影</span>
        <div :style="{display:'inline-block',width:'150px',marginLeft: '20px'}">
          <el-slider :show-tooltip="false" :max="1" :step="0.01" v-model="transparenc"></el-slider>
        </div>
      </div>
    </el-card>
    <div class="cesium-player-area" v-show="playerToolShow">
      <el-button @click="flyPlay">{{playStatus}}</el-button>
      <el-button @click="flyStop">停止</el-button>
      <el-button size="small" class="is-circle cesium-tool-close" @click="flyClose">
        <i class="el-icon-close"></i>
    </el-button>
    </div>
    </div>
    <div id="cesiumContainer" class="cesium-base"></div>
  </div>
</template>

<script>
/* eslint-disable */
import $ from 'jquery'
import Bubble from './js/Bubble.js'
// import './js/spectrum.js'
// import './js/slider.js'
const Cesium = window.Cesium
export default {
  name: 'CesRec',
  data () {
    return {
      token: '113662e12bb999694e90e48f474e2f7f',
      scene: null,
      viewer: null,
      toolShow: false,
      playerToolShow: false,
      lines: [],
      tools: [
        {
          name: '量算',
          id: 1
        },
        {
          name: '飞行漫游',
          id: 2
        },
        {
          name: '透明度',
          id: 3
        }
      ],
      transparenc: 1,
      layers: [
        {
          name: '三维模型',
          code: '1',
          children: [
            {
              name: '倾斜摄影',
              code: '1-1',
              layer: []
            }
          ]
        },
        {
          name: '地图底图',
          code: '2',
          children: [
            {
              name: '影像',
              code: '2-1',
              layer: []
            },
            {
              name: '注记',
              code: '2-2',
              layer: []
            }
          ]
        },
        {
          name: '路线图例',
          code: '3',
          children: [
            {
              name: '1号线区间',
              code: '3-1',
              layer: []
            },
            {
              name: '1号线车站',
              code: '3-2',
              layer: []
            },
            {
              name: '1号线保护区',
              code: '3-3',
              layer: []
            },
            {
              name: '2号线区间',
              code: '3-4',
              layer: []
            },
            {
              name: '2号线车站',
              code: '3-5',
              layer: []
            },
            {
              name: '2号线保护区',
              code: '3-6',
              layer: []
            }
          ]
        }
      ],
      stationlayers: [],
      flyFiles: [
        {
          name: '1号线',
          file: 'static/line/1-fly.fpf',
          id: 1
        },
        {
          name: '2号线',
          file: 'static/line/2-fly.fpf',
          id: 2
        }
      ],
      playStatus: '播放',
      flyManager: null,
      layerProps: {
        children: 'children',
        label: 'name'
      },
      stationLayerProps: {
        children: 'children',
        label: 'name'
      },
      form: {
        line: null
      },
      handlerDis: null,
      handlerArea: null,
      handlerHeight: null
    };
  },
  computed: {},
  watch: {
    transparenc(value) {
      this.layers[0].children[0].layer.forEach(layer => {
        layer.style3D.fillForeColor.alpha = value;
      });
    }
  },
  methods: {
    addLayerToTree(layerIndex, childrenIndex, layer, checked) {
      this.layers[layerIndex].children[childrenIndex].layer = layer;
      this.$refs.tree.setChecked(
        this.layers[layerIndex].children[childrenIndex].code,
        checked
      );
    },
    layerChecked(current, all) {
      console.log(current, all);
      const checked = all.checkedKeys.some(code => code === current.code);

      if (current.code[0] === '1') {
        //倾斜摄影
        if (current.children) {
          current.children.forEach(layerNode => {
            layerNode.layer.forEach(layer => {
              layer.visible = checked;
            });
          });
        } else {
          current.layer.forEach(layer => {
            layer.visible = checked;
          });
        }
      } else if (current.code[0] === '2') {
        //底图
        if (current.children) {
          current.children.forEach(layerNode => {
            layerNode.layer.forEach(layer => {
              layer.show = checked;
            });
          });
        } else {
          current.layer.forEach(layer => {
            layer.show = checked;
          });
        }
      } else if (current.code[0] === '3') {
        //路线图例
        if (current.children) {
          current.children.forEach(layerNode => {
            layerNode.layer.forEach(layer => {
              layer.visible = checked;
            });
          });
        } else {
          current.layer.forEach(layer => {
            layer.visible = checked;
          });
        }
      }
    },
    stationLayerChecked(current, all) {
      const checked = all.checkedKeys.some(code => code === current.code);
      if (current.children) {
        current.children.forEach(layerNode => {
          layerNode.layer.forEach(layer => {
            layer.show = checked;
          });
          layerNode.bubble.visibility(checked);
        });
      } else {
        current.layer.forEach(layer => {
          layer.show = checked;
        });
        current.bubble.visibility(checked);
      }
    },
    layerClick(current, currentNode) {
      console.log(current, currentNode);
      if (currentNode.isLeaf) {
        this.viewer.flyTo(current.layer[0]);
      }
    },
    stationLayerClick(current, currentNode) {
      console.log(current, currentNode);
      if (currentNode.isLeaf) {
        this.viewer.flyTo(current.layer[0]);
      }
    },
    toolSelect(toolName) {
      switch (toolName) {
        case '量算':
          this.toolShow = 'measure';
          break;
        case '飞行漫游':
          this.toolShow = 'fly';
          break;
        case '透明度':
          this.toolShow = 'transparency';
          break;
        default:
          break;
      }
    },
    fly(fpfUrl) {
      this.flyStop();
      this.flyManager = null;
      this.playerToolShow = true;
      var Cesium = window.Cesium;
      var viewer = this.viewer;
      var scene = viewer.scene;
      var routes = new Cesium.RouteCollection(viewer.entities);
      //添加fpf飞行文件，fpf由SuperMap iDesktop生成
      routes.fromFile(fpfUrl);
      //初始化飞行管理
      var flyManager = new Cesium.FlyManager({
        scene: scene,
        routes: routes
      });

      flyManager.readyPromise.then(() => {
        console.log(flyManager);
        // 飞行路线就绪
        var currentRoute = flyManager.currentRoute;
        currentRoute.isLineVisible = false;
        currentRoute.isStopVisible = false;
        this.flyManager = flyManager;
        this.playStatus = '播放';
        this.flyPlay();
      });
    },
    flyPlay() {
      if (this.playStatus === '播放') {
        this.flyManager && this.flyManager.play();
        this.playStatus = '暂停';
      } else {
        this.flyManager && this.flyManager.pause();
        this.playStatus = '播放';
      }
    },
    flyStop() {
      this.flyManager && this.flyManager.stop();
      this.playStatus = '播放';
    },
    flyClose() {
      this.flyManager && this.flyManager.stop();
      this.playerToolShow = false;
    },
    measureSelect(type) {
      this.deactiveAll();
      switch (type) {
        case 'distance':
          this.handlerDis && this.handlerDis.activate();
          break;
        case 'area':
          this.handlerArea && this.handlerArea.activate();
          break;
        case 'height':
          this.handlerHeight && this.handlerHeight.activate();
          break;
        case 'clear':
          this.clearAll();
          break;
      }
    },
    deactiveAll() {
      this.handlerDis && this.handlerDis.deactivate();
      this.handlerArea && this.handlerArea.deactivate();
      this.handlerHeight && this.handlerHeight.deactivate();
    },
    clearAll() {
      this.handlerDis && this.handlerDis.clear();
      this.handlerArea && this.handlerArea.clear();
      this.handlerHeight && this.handlerHeight.clear();
    }
  },
  mounted () {
    var that = this
    this.viewer = new Cesium.Viewer('cesiumContainer')
    var viewer = this.viewer
    viewer._element.removeChild(viewer.bottomContainer)
    viewer.infoBox.destroy()
    var scene = viewer.scene
    var widget = viewer.cesiumWidget
    var imageryLayers = viewer.imageryLayers
    // 服务器
    var workspace = 'http://115.231.108.140:8090/iserver/services/3D-nc1125/rest/realspace'
    try {
      imageryLayers.removeAll(true)
      this.layers[1].children[0].layer.push(
        imageryLayers.addImageryProvider(
          new Cesium.TiandituImageryProvider({
            credit: new Cesium.Credit('天地图全球影像服务'),
            url:"http://[subdomain].tianditu.com/img_w/wmts?tk=0a65163e2ebdf5a37abb7f49274b85df"
        })
      )
      )
      this.layers[1].children[1].layer.push(
        imageryLayers.addImageryProvider(
          new Cesium.TiandituImageryProvider({
            mapStyle: Cesium.TiandituMapsStyle.CIA_C,
            url:"http://[subdomain].tianditu.com/img_w/wmts?tk=0a65163e2ebdf5a37abb7f49274b85df"
          })
        )
      )
      // imageryLayers.addImageryProvider(new Cesium.BingMapsImageryProvider({
      //     key: 'AqgBIfrBG50dl7Ykc9nANoj5UJnIxg5YyEZu-UE7sY_sHoZT1db1jGZAalBsU73w',
      //     url: '//dev.virtualearth.net'
      // }))
      this.$refs.tree.setChecked('2-1', true)
      this.$refs.tree.setChecked('2-2', true)
      Cesium.loadJson(workspace + '/scenes.json').then(scenes => {
        var sname = scenes[0].name
        Cesium.loadJson(workspace + '/scenes/' + sname + '.json').then(jsonData => {
          var cameraPosition = jsonData.camera
          var tilt = Cesium.Math.toRadians(cameraPosition.tilt - 90)
          scene.addS3MTilesLayerByScp(
            workspace + '/datas/Config2/config',
            {name: '倾斜摄影'}
          ).then((layer) => {
            layer.clearMemoryImmediately = false
            that.addLayerToTree(0, 0, [layer], true)
            scene.camera.flyTo({
              destination: new Cesium.Cartesian3.fromDegrees(
                cameraPosition.longitude,
                cameraPosition.latitude,
                cameraPosition.altitude
              ),
              orientation: {
                heading: Cesium.Math.toRadians(360.0),
                pitch: tilt,
                roll: 0
              },
              duration: 5
            })
            scene.addS3MTilesLayerByScp(
              workspace + '/datas/不用polyline_2号线保护区@nc1125/config',
              { name: '2号保护区' }
            ).then((layer) => {
              layer.style3D.fillForeColor = Cesium.Color.RED
              that.addLayerToTree(2, 5, [layer], true);
            })
            scene.addS3MTilesLayerByScp(
              workspace + '/datas/区间_2号线@nc1125/config',
              { name: '2号线区间' }
            ).then((layer) => {
              that.addLayerToTree(2, 3, [layer], true);
            })
            scene.addS3MTilesLayerByScp(
              workspace + '/datas/车站_2号线@nc1125/config',
              { name: '2号线车站' }
            ).then((layer) => {
              that.addLayerToTree(2, 4, [layer], true);
            })
            scene.addS3MTilesLayerByScp(
              workspace + '/datas/不用polyline_1号线保护区@nc1125/config',
              { name: '1号线保护区' }
            ).then((layer) => {
              layer.style3D.fillForeColor = Cesium.Color.RED
              that.addLayerToTree(2, 2, [layer], true);
            })
            scene.addS3MTilesLayerByScp(
              workspace + '/datas/区间_1号线@nc1125/config',
              { name: '1号线区间' }
            ).then((layer) => {
              that.addLayerToTree(2, 0, [layer], true);
            })
            scene.addS3MTilesLayerByScp(
              workspace + '/datas/车站_1号线@nc1125/config',
              { name: '1号线车站' }
            ).then((layer) => {
              that.addLayerToTree(2, 1, [layer], true);
            })
            Cesium.loadJson('static\\line\\1-location.geojson').then(stations => {
              that.stationlayers.push({
                name: '一号线',
                code: '1',
                children: []
              })
              stations.features.forEach((station, index) => {
                const position = new Cesium.Cartesian3.fromDegrees(
                  station.geometry.coordinates[0],
                  station.geometry.coordinates[1],
                  240
                )
                const point = new Cesium.Entity({
                  name: station.properties.sta_name,
                  positon: position,
                  point: {
                    color: Cesium.Color.WHITE,
                    pixelSize: 15
                  }
                })
                viewer.entities.add(point)
                var statLabelSpan = `<span id="1号线-${station.properties.sta_name}" class="cesium-stat-btn">${station.properties.sta_name}</span>`
                window.$('#allContainer').append(statLabelSpan)
                var statBubble = new Bubble(
                  scene,
                  '1号线-' + station.properties.sta_name
                );
                statBubble.showAt(position);
                that.stationlayers[0].children.push({
                  name: station.properties.sta_name,
                  code: `1-${index}`,
                  layer: [point],
                  bubble: statBubble
                });
                that.$nextTick(function() {
                  that.$refs.stationTree.setChecked(`1-${index}`, true);
                });
              })
            })
            Cesium.loadJson('static\\line\\2-location.geojson').then(stations => {
              that.stationlayers.push({
                name: '二号线',
                code: '2',
                children: []
              })
              stations.features.forEach((station, index) => {
                const position = new Cesium.Cartesian3.fromDegrees(
                  station.geometry.coordinates[0],
                  station.geometry.coordinates[1],
                  240
                )
                const point = new Cesium.Entity({
                  name: station.properties.sta_name,
                  positon: position,
                  point: {
                    color: Cesium.Color.WHITE,
                    pixelSize: 15
                  }
                })
                viewer.entities.add(point)
                var statLabelSpan = `<span id="二号线-${station.properties.sta_name}" class="cesium-stat-btn">${station.properties.sta_name}</span>`
                window.$('#allContainer').append(statLabelSpan)
                var statBubble = new Bubble(
                  scene,
                  '二号线-' + station.properties.sta_name
                );
                statBubble.showAt(position);
                that.stationlayers[1].children.push({
                  name: station.properties.sta_name,
                  code: `2-${index}`,
                  layer: [point],
                  bubble: statBubble
                });
                that.$nextTick(function() {
                  that.$refs.stationTree.setChecked(`2-${index}`, true);
                });
              })
            })
            //初始化测量距离
            that.handlerDis = new Cesium.MeasureHandler(
              viewer,
              Cesium.MeasureMode.Distance
            );
            //注册测距功能事件
            that.handlerDis.measureEvt.addEventListener(function(result) {
              var dis = Number(result.distance);
              var distance =
                dis > 1000
                  ? (dis / 1000).toFixed(2) + 'km'
                  : dis.toFixed(2) + 'm';
              that.handlerDis.disLabel.text = '距离:' + distance;
            });

            //初始化测量面积
            that.handlerArea = new Cesium.MeasureHandler(
              viewer,
              Cesium.MeasureMode.Area
            );
            that.handlerArea.measureEvt.addEventListener(function(result) {
              var mj = Number(result.area);
              var area = mj > 1000000
                  ? (mj / 1000000).toFixed(2) + 'km²'
                  : mj.toFixed(2) + '㎡';
              that.handlerArea.areaLabel.text = '面积:' + area;
            });

            //初始化测量高度
            that.handlerHeight = new Cesium.MeasureHandler(
              viewer,
              Cesium.MeasureMode.DVH
            );
            that.handlerHeight.measureEvt.addEventListener(function (result) {
              var distance =
                result.distance > 1000
                  ? (result.distance / 1000).toFixed(2) + 'km'
                  : result.distance + 'm';
              var vHeight =
                result.verticalHeight > 1000
                  ? (result.verticalHeight / 1000).toFixed(2) + 'km'
                  : result.verticalHeight + 'm';
              var hDistance =
                result.horizontalDistance > 1000
                  ? (result.horizontalDistance / 1000).toFixed(2) + 'km'
                  : result.horizontalDistance + 'm';
              that.handlerHeight.disLabel.text = '空间距离:' + distance;
              that.handlerHeight.vLabel.text = '垂直高度:' + vHeight;
              that.handlerHeight.hLabel.text = '水平距离:' + hDistance;
            });
            if (!scene.pickPositionSupported) {
              alert('不支持深度纹理,无法拾取位置！');
            }
          })
        })
      })
      // // 绘制可视域
      // var viewPosition;
      // scene.viewFlag = true;
      // var pointHandler = new Cesium.DrawHandler(viewer, Cesium.DrawMode.Point);
      // // 创建可视域分析对象
      // var viewshed3D = new Cesium.ViewShed3D(scene);
      // var colorStr1 = viewshed3D.visibleAreaColor.toCssColorString();
      // var colorStr2 = viewshed3D.hiddenAreaColor.toCssColorString();
      // // $('#colorPicker1').spectrum({
      // //   color: colorStr1,
      // //   showPalette: true,
      // //   showAlpha: true,
      // //   localStorageKey: "spectrum.demo"
      // // })
      // // $('#colorPicker2').spectrum({
      // //   color: colorStr2,
      // //   showPalette: true,
      // //   showAlpha: true,
      // //   localStorageKey: "spectrum.demo"
      // // })
      // $('.close').click(function () {
      //   $('#wrapper').hide();
      // })
      // var widget = viewer.cesiumWidget;
      // var viewModel = {
      //   direction: 1.0,
      //   pitch: 1.0,
      //   distancem: 1.0,
      //   verticalFov: 1.0,
      //   horizontalFov: 1.0,
      //   visibleAreaColor: '#ffffffff',
      //   invisibleAreaColor: '#ffffffff'
      // }
      // Cesium.knockout.track(viewModel);
      // var toolbar = document.getElementById('wapper');
      // Cesium.knockout.applyBindings(viewModel, toolbar);
      // Cesium.knockout.getObservable(viewModel, 'direction').subscribe(
      //   function (newValue) {
      //     viewshed3D.direction = parseFloat(newValue);
      //   }
      // )
      // Cesium.knockout.getObservable(viewModel, 'pitch').subscribe(
      //   function (newValue) {
      //     viewshed3D.pitch = parseFloat(newValue);
      //   }
      // )
      // Cesium.knockout.getObservable(viewModel, 'distancem').subscribe(
      //   function (newValue) {
      //     viewshed3D.distancem = parseFloat(newValue);
      //   }
      // )
      // Cesium.knockout.getObservable(viewModel, 'verticalFov').subscribe(
      //   function (newValue) {
      //     viewshed3D.horizontalFov = parseFloat(newValue);
      //   }
      // )
      // Cesium.knockout.getObservable(viewModel, 'visibleAreaColor').subscribe(
      //   function (newValue) {
      //     var color = Cesium.Color.fromCssColorString(newValue);
      //     viewshed3D.visibleAreaColor = color;
      //   }
      // )
      // // Cesium.knockout.getObservable(viewModel, 'hiddenAreaColor').subscribe(
      // //   function (newValue) {
      // //     var color = Cesium.Color.fromCssColorString(newValue);
      // //     viewshed3D.hiddenAreaColor = color;
      // //   }
      // // )
      // var handler = new Cesium.ScreenSpaceEventHandler(scene.canvas);
      // handler.setInputAction(function (e) {
      //   if (!scene.viewFlag) {
      //     var position = e.endPosition;
      //     var last = scene.pickPosition(position);
      //     var distance = Cesium.Cartesian3.distance(viewPosition, last);
      //     if (distance > 0) {
      //       var cartographic = Cesium.Cartographic.fromCartesian(last);
      //       var longitude = Cesium.Math.toDegrees(cartographic.longitude);
      //       var latitude = Cesium.Math.toDegrees(cartographic.latitude);
      //       var height = cartographic.height;
      //       viewshed3D.setDistDirByPoint([longitude, latitude, height]);
      //     }
      //   }
      // }, Cesium.ScreenSpaceEventType.MOUSE_MOVE);
      // handler.setInputAction(function (e) {
      //   scene.viewFlag = true;
      //   $('#wapper').show();
      //   viewModel.direction = viewshed3D.direction;
      //   viewModel.pitch = viewshed3D.pitch;
      //   viewModel.distancem = viewshed3D.distance;
      //   viewModel.horizontalFov = viewshed3D.horizontalFov;
      //   viewModel.verticalFov = viewshed3D.verticalFov;
      // }, Cesium.ScreenSpaceEventType.RIGHT_CLICK);
      // document.getElementById('chooseView').onclick = function () {
      //   if (pointHandler.active) {
      //     return;
      //   }
      //   viewer.entities.removeAll();
      //   viewshed3D.distance = 0.1;
      //   scene.viewFlag = true;
      //   pointHandler.activate();
      // }
      // pointHandler.drawEvt.addEventListener(function (result) {
      //   var point = result.object;
      //   var position = point.position;
      //   viewPosition = position;
      //   var cartographic = Cesium.Cartographic.fromCartesian(position);
      //   var longitude = Cesium.Math.toDegrees(cartographic.longitude);
      //   var latitude = Cesium.Math.toDegrees(cartographic.latitude);
      //   var height = cartographic.height + 1.8;
      //   point.position = Cesium.Cartesian3.fromDegrees(longitude, latitude, height);
      //   if (scene.viewFlag) {
      //     viewshed3D.viewPosition = [longitude, latitude, height];
      //     viewshed3D.build();
      //     scene.viewFlag = false;
      //   }
      // })
      // $('#clearView').on('click', function () {
      //   $('#wapper').hide();
      //   viewer.entities.removeAll();
      //   viewshed3D.distance = 0.1;
      //   scene.viewFlag = true;
      // })
      /*
      viewer.scene.undergroundMode = true
      viewer.scene.screenSpaceCameraController.minimumZoomDistance = -1000
      viewer.scene.terrainProvider.isCreateSkirt = false
      var viewModel = {
        overGroundAlpha: 1
      }
      Cesium.knockout.track(viewModel)
      var toobar = document.getElementById('toolbar')
      Cesium.knockout.applyBindings(viewModel, toobar)
      Cesium.knockout.getObservable(viewModel, 'overGroundAlpha').subscribe(
        function (newValue) {
          overGroundLayer.style3D.fillForeColor.alpha = parseFloat(newValue)
        }
      )
            $('#excavation').on('click', function () { // 绘制开挖区域
        var handlerPolygon = new Cesium.DrawHandler(viewer, Cesium.DrawMode.Polygon)
        handlerPolygon.activeEvt.addEventListener(function (isActive) {
          if (isActive === true) {
            viewer.enableCursorStyle = false
            viewer._element.style.cursor = ''
            $('.ces').removeClass('drawCur').addClass('drawCur')
          } else {
            viewer.enableCursorStyle = true
            $('.ces').removeClass('drawCur')
          }
        })
        handlerPolygon.movingEvt.addEventListener(function (windowPosition) {
        })
        handlerPolygon.drawEvt.addEventListener(function (result) {
          handlerPolygon.polygon.show = false
          handlerPolygon.polyline.show = false
          var polygon = result.object
          var positions = polygon.positions
          var flatPoints = []
          for (var i = 0, j = positions.length; i < j; i++) { // 获取经纬度和高度
            var position = positions[i]
            var cartographic = Cesium.Cartographic.fromCartesian(position)
            var lon = Cesium.Math.toDegrees(cartographic.longitude)
            var lat = Cesium.Math.toDegrees(cartographic.latitude)
            var height = cartographic.height
            flatPoints.push(lon)
            flatPoints.push(lat)
            flatPoints.push(height)
          }
          overGroundLayer.addExcavationRegion({ // 设置倾斜开挖参数
            position: flatPoints,
            name: 'excavation_' + Math.random()
          })
          handlerPolygon.deactivate()
        })
        handlerPolygon.activate()
      })
      // 空间模式
      var clampMode = 0
      var handlerDis, handlerArea, handlerHeight
      handlerDis = new Cesium.MeasureHandler(viewer, Cesium.MeasureMode.Distance, clampMode)
      handlerDis.measureEvt.addEventListener(function (result) {
        let dis = Number(result.distance)
        let distance = dis > 1000 ? (dis / 1000).toFixed(2) + 'km' : dis.toFixed(2) + 'm'
        handlerDis.disLabel.text = '距离：' + distance
      })
      handlerArea = new Cesium.MeasureHandler(viewer, Cesium.MeasureMode.Area, clampMode)
      handlerArea.measureEvt.addEventListener(function (result) {
        var mj = Number(result.area)
        var area = mj > 1000000 ? (mj / 1000000).toFixed(2) + 'km²' : mj.toFixed(2) + '㎡'
        handlerArea.areaLabel.text = '面积:' + area
      })
      handlerHeight = new Cesium.MeasureHandler(viewer, Cesium.MeasureMode.DVH)
      handlerHeight.measureEvt.addEventListener(function (result) {
        var distance = result.distance > 1000 ? (result.distance / 1000).toFixed(2) + 'km' : result.distance + 'm'
        var vHeight = result.verticalHeight > 1000 ? (result.verticalHeight / 1000).toFixed(2) + 'km' : result.verticalHeight + 'm'
        var hDistance = result.horizontalDistance > 1000 ? (result.horizontalDistance / 1000).toFixed(2) + 'km' : result.horizontalDistance + 'm'
        handlerHeight.disLabel.text = '空间距离:' + distance
        handlerHeight.vLabel.text = '垂直高度:' + vHeight
        handlerHeight.hLabel.text = '水平距离:' + hDistance
      })
      $('#distance').click(function () {
        deactiveAll()
        handlerDis && handlerDis.activate()
      })
      $('#area').click(function () {
        deactiveAll()
        handlerArea && handlerArea.activate()
      })
      $('#height').click(function () {
        deactiveAll()
        handlerHeight && handlerHeight.activate()
      })
      $('#clear').click(function () {
        clearAll()
      })
      function clearAll () {
        handlerDis && handlerDis.clear()
        handlerArea && handlerArea.clear()
        handlerHeight && handlerHeight.clear()
      }
      function deactiveAll () {
        handlerDis && handlerDis.deactivate()
        handlerArea && handlerArea.deactivate()
        handlerHeight && handlerHeight.deactivate()
      }
      // 键盘控制
      var scene = viewer.scene
      var canvas = viewer.canvas
      canvas.setAttribute('tabindex', '0')
      canvas.onclock = function () {
        canvas.focus()
      }
      var ellipsoid = scene.globe.ellipsoid
      var flags = {
        looking: false,
        moveForward: false,
        moveBackward: false,
        moveUp: false,
        moveDown: false,
        moveLeft: false,
        moveRight: false
      }
      // 判断按键值
      function getFlagForKeyCode (keyCode) {
        switch (keyCode) {
          case 'W'.charCodeAt(0):
            return 'moveForward'
          case 'S'.charCodeAt(0):
            return 'moveBackward'
          case 'Q'.charCodeAt(0):
            return 'moveUp'
          case 'E'.charCodeAt(0):
            return 'moveDown'
          case 'D'.charCodeAt(0):
            return 'moveRight'
          case 'A'.charCodeAt(0):
            return 'moveLeft'
          default:
            return undefined
        }
      }
      document.addEventListener('keydown', function (e) {
        var flagName = getFlagForKeyCode(e.keyCode)
        if (typeof flagName !== 'undefined') {
          flags[flagName] = true
        }
      }, false)
      document.addEventListener('keyup', function (e) {
        var flagName = getFlagForKeyCode(e.keyCode)
        if (typeof flagName !== 'undefined') {
          flags[flagName] = false
        }
      }, false)
      viewer.clock.onTick.addEventListener(function (clock) {
        let camera = viewer.camera
        var cameraHeight = ellipsoid.cartesianToCartographic(camera.position).height
        var moveRate = cameraHeight / 100.0
        if (flags.moveForward) {
          camera.moveForward(moveRate)
        }
        if (flags.moveBackward) {
          camera.moveBackward(moveRate)
        }
        if (flags.moveUp) {
          camera.moveUp(moveRate)
        }
        if (flags.moveDown) {
          camera.moveDown(moveRate)
        }
        if (flags.moveLeft) {
          camera.moveLeft(moveRate)
        }
        if (flags.moveRight) {
          camera.moveRight(moveRate)
        }
      })
      */
    } catch (e) {
      if (widget._showRenderLoopErrors) {
        var title = '渲染时发生错误，已停止渲染。'
        widget.showErrorPanel(title, undefined, e)
      }
    }
  }
}
</script>

<style scoped>
#cesiumContainer {
  width: 100%;
  min-height: 850px;
  height: auto;
  margin: 0;
  overflow: hidden;
  padding: 0;
}
.tool-bar {
  background-color: rgba(38, 38, 38, 0.75);
  padding: 20px 20px 10px 20px;
  color: #ffffff;
  border: 1px solid #526f82;
  position: absolute;
  left: 250px;
  top: 100px;
  z-index: 10000;
}
.cesium-layers {
  min-width: 150px;
  max-height: 600px;
  overflow-y: auto;
}
</style>
