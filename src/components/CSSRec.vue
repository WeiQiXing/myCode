<template>
  <div class='cssrec'>
    <div class='markdown-body'><md></md></div>
  </div>
</template>

<script>
import md from './docs/CSS学习记录.md'

export default {
  name: 'CSSrec',
  data () {
    return {
      msg: 'CSSrec md file'
    }
  },
  components: {md}
}
</script>
