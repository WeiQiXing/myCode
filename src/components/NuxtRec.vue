<template>
  <div class='nuxtrec'>
    <div class='markdown-body'><md></md></div>
  </div>
</template>

<script>
import md from './docs/Axios和Vuex及NuxtJS.md'

export default {
  name: 'Nuxtrec',
  data () {
    return {
      msg: 'Nuxtrec md file'
    }
  },
  components: {md}
}
</script>
