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
    <div class='markdown-body'><md></md></div>
  </div>
</template>

<script>
import md from './docs/Vue学习记录.md'

export default {
  name: 'Introduction',
  data () {
    return {
      msg: 'It is Intro HTML file'
    }
  },
  components: {md}
}
</script>
