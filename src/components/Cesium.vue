<template>
  <div class='ces'>
    <div id='toolbar' class='tool-bar'>
      <el-button type="button" plain id="distance">测距</el-button>
      <el-button type="button" plain id="area">侧面</el-button>
      <el-button type="button" plain id="height">测高</el-button>
      <el-button type="button" plain id="clear">清除</el-button>
    </div>
    <div id='cesrec'></div>
  </div>
</template>

<script>
// import * as Cesium from 'cesium/Source/Cesium'
// import buildModuleUrl from 'cesium/Source/Core/buildModuleUrl'
// import 'cesium/Source/Widgets/widgets.css'
import $ from 'jquery'

const Cesium = window.Cesium
export default {
  name: 'CesRec',
  data () {
    return {
      'msg': {}
    }
  },
  mounted () {
    var viewer = new Cesium.Viewer('cesrec')
    viewer.imageryLayers.addImageryProvider(new Cesium.BingMapsImageryProvider({
      url: 'https://dev.virtualearth.net',
      mapStyle: Cesium.BingMapsStyle.AERIAL
      // key: URL_CONFIG.BING_MAP_KEY URL_CONFIG文件可能没有添加进
    }))
    // 打开所发布三维服务下的所有图层
    var promise = viewer.scene.open('http://www.supermapol.com/realspace/services/3D-GuangZhou/rest/realspace')
    Cesium.when.all(promise, function (layers) {
      // 设置图层的阴影模式
      this.viewer.scene.camera.setView({
        // 将经度、纬度、高度的坐标转换为笛卡尔坐标
        destination: new Cesium.Cartesian3(-2323607.7945701713, 5386182.530303348, 2505814.811681112),
        orientation: {
          heading: 4.844795866469065,
          pitch: -0.58125995096984,
          roll: 1.2504663970958063e-11
        }
      })
    }, function (e) {
      if (viewer.cesiumWidget._showRenderLoopErrors) {
        var title = '加载SCP失败，请检查网络连接状态或者url地址是否正确？'
        viewer.cesiumWidget.showErrorPanel(title, undefined, e)
      }
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
  }
}
</script>

<style scoped>
#cesrec {
  width: 100%;
  height: 790px;
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
</style>
