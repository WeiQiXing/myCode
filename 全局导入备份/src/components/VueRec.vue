<template>
  <div class='vuerec'>
    <div class='markdown-body'><md></md></div>
  </div>
</template>

<script>
import md from './docs/Vue学习记录.md'

export default {
  name: 'Vuerec',
  data () {
    return {
      msg: 'Vuerec md file'
    }
  },
  components: {md}
}
</script>
