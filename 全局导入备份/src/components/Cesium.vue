<template>
  <div id='cesrec'>
  </div>
</template>

<script>
// import 'cesium/Source/Widgets/widgets.css'
// import Viewer from 'cesium/Source/Widgets/Viewer/Viewer'
// import buildModuleUrl from 'cesium/Source/Core/buildModuleUrl'
import * as Cesium from 'cesium/Cesium'
// 下面的样式很重要，否则控件就都会乱
import 'cesium/Widgets/widgets.css'

export default {
  name: 'CesRec',
  data () {
    return {
      'viewer': {}
    }
  },
  mounted: function () {
    // 设置静态资源目录
    // buildModuleUrl.setBaseUrl('../static/Cesium/')
    // 创建viewer实例
    this.viewer = new Cesium.Viewer('cesrec')
  }
}
</script>

<style scoped>
#cesrec {
  width: 100%;
  height: 100%;
  margin: 0;
  overflow: 0;
  padding: 0;
}
</style>
