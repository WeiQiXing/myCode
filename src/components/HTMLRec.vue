<template>
  <div class='htmlrec'>
    <div class='markdown-body'><md></md></div>
  </div>
</template>

<script>
import md from './docs/HTML学习记录.md'

export default {
  name: 'HTMLrec',
  data () {
    return {
      msg: 'HTMLrec md file'
    }
  },
  components: {md}
}
</script>
