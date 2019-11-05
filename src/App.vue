<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <el-container style="height: 850px; width: 100%; boder: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238,241,246)">
        <el-menu :default-openeds="['1', '2', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <template solt="title">分组一</template>
              <el-menu-item index="1-1" @click="gotoHelloworld">Hello World</el-menu-item>
              <el-menu-item index="1-2">Introduction</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group>
              <template solt="title">分组二</template>
              <el-menu-item index="1-3">选项3</el-menu-item>
              <el-menu-item index="1-4">选项4</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-menu"></i>导航二</template>
            <el-menu-item-group>
              <template solt="title">分组一</template>
              <el-menu-item index="2-1" @click="gotoLeaflet">Leaflet</el-menu-item>
              <el-menu-item index="2-2" @click="gotoEUITest">ElementUITest</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title"><i class="el-icon-setting"></i>导航三</template>
            <el-menu-item-group>
              <template solt="title">分组一</template>
              <el-menu-item index="3-1">选项1</el-menu-item>
              <el-menu-item index="3-2">选项2</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-container style="height: 100%">
        <el-header style="text-align: right;font-size: 20px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>功能一</el-dropdown-item>
              <el-dropdown-item>功能二</el-dropdown-item>
              <el-dropdown-item>功能三</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>魏琦星</span>
        </el-header>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
<script>
export default {
  name: 'App',
  data () {
    return {
      msg: 'It is app'
    }
  },
  methods: {
    gotoHelloworld () {
      this.$router.push({path: '/hello'})
    },
    // 进入leaflet显示界面
    gotoLeaflet () {
      this.$router.push({path: '/map'})
    },
    // 进入element-ui显示界面
    gotoEUITest () {
      this.$router.push({path: '/test'})
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
}
  .el-aside {
    color: #333;
  }
</style>
