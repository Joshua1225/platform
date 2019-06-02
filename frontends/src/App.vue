<template>
  <div id="app">
    <div id="nav">
      <el-container>
        <el-header style="overflow: hidden">
          <top/>
        </el-header>
        <el-main>
          <router-view/>
        </el-main>
        <el-footer>
          <bottom/>
        </el-footer>
      </el-container>
    
    </div>
  </div>
</template>

<script>
import Bottom from '@/components/Bottom.vue'
import Top from '@/components/Top.vue'
export default {
  name:"app",
  components: {
    Bottom,Top
  }
}
</script>


<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
