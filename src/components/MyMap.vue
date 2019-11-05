<template>
  <div class="mymap">
    <div id="mapdiv"></div>
  </div>
</template>

<script>
import * as L from 'leaflet'
/* eslint-disable */

export default {
  name: 'MyMap',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  mounted () {
    var map = L.map('mapdiv', {
      // 设置地图中心
      center: [30.2527, 120.0176],
      zoom: 13
    })
    // 加载地图
    L.tileLayer(
      'http://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
      {
        subdomains: ['1', '2', '3', '4'],
        attribution: 'GD'
      }
    ).addTo(map)
    // 添加标注,使用bindPopup()绑定信息到图形上，使用openPopup()显示出气泡
    var marker = L.marker([30.2527, 120.0176]).addTo(map)
    marker.bindPopup('<b>Hello world!</b><br>You are here').openPopup()
    // 弹出面板
    var popup = L.popup()
    // 添加点击地图事件,返回点击点的位置
    function onMapClick (e) {
      popup
        .setLatLng(e.latlng)
        .setContent('You clicked the map at' + e.latlng.toString())
        .openOn(map)
    }
    map.off('click', onMapClick)
    // 画多边形的函数
    var points = []
    var lines = new L.polyline([])
    var tempLines = new L.polyline([], {dashArray: 5})
    // 点击显示点击位置信息，并存入points中
    function onClick (e) {
      points.push([e.latlng.lat, e.latlng.lng])
      lines.addLatLng(e.latlng)
      map.addLayer(tempLines)
      map.addLayer(lines)
      map.addLayer(L.circle(e.latlng, {color: '#ff0000', fillColor: '#ff0000', fillOpacity: 1}))
      popup
        .setLatLng(e.latlng)
        .setContent('You clicked the map at' + e.latlng.toString())
        .openOn(map)
    }
    // 鼠标移动
    function onMove (e) {
      if (points.length > 0) {
        let ls = [points[points.length - 1], [e.latlng.lat, e.latlng.lng], points[0]]
        tempLines.setLatLng(ls)
      }
    }
    // 双击点击事件
    function onDoubleClick (e) {
      L.polygon(points).addTo(map)
      points = []
      lines.remove()
      tempLines.remove()
      lines = new L.polyline([])
    }
    map.on('click', onClick)
    map.on('dbclick', onDoubleClick)
    map.on('mousemove', onMove)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#mapdiv {
  width: 100%;
  height: 600px;
}
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
