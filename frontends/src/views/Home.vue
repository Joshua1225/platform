<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <AppealMessagea/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/AppealMessage.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
  }
}
</script>
