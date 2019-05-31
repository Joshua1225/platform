<template>
  <div id="app">
    <div id="nav">
      <el-container>
        <el-header>
          <head/>
        </el-header>
        <el-main>
          <router-view/>
        </el-main>

        <el-footer>
          <footer/>
        </el-footer>
      </el-container>
    
    </div>
  </div>
</template>



<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
