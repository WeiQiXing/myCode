<template>
  <div class='jsrec'>
    <div class='markdown-body'><md></md></div>
  </div>
</template>

<script>
import md from './docs/JavaScript学习记录.md'

export default {
  name: 'JSrec',
  data () {
    return {
      msg: 'JSrec md file'
    }
  },
  components: {md}
}
</script>
