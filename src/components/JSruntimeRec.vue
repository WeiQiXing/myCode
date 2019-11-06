<template>
  <div class='jsrunrec'>
    <div class='markdown-body'><md></md></div>
  </div>
</template>

<script>
import md from './docs/JS运行机制.md'

export default {
  name: 'JSrunrec',
  data () {
    return {
      msg: 'JSrunrec md file'
    }
  },
  components: {md}
}
</script>
