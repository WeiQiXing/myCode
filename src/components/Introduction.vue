<template>
  <div class='intro'>
    <p align="left">本项目是在学习了前端一段时间后,对前面学习的知识的总结与记录。
      <br>主要用到的技术有：
      <br><b>  ·HTML</b>
      <br><b>  ·CSS</b>
      <br><b>  ·JavaScript</b>
      <br><b>  ·Vue</b>
      <br><b>  ·Element-UI</b>
      <br><b>  ·Leaflet</b>
    </p>
    <el-button @click="show1 = !show1">详细简介</el-button>
    <transition name="el-zoom-in-center">
      <div class='markdown-body' v-show="show1"><md></md></div>
    </transition>
  </div>
</template>

<script>
import md from './docs/intro.md'

export default {
  name: 'Introduction',
  data: () => ({
    show1: false
  }),
  components: {md}
}
</script>
