<template>
  <div align="center">
    <el-card class="box-card" >
      <div slot="header" class="clearfix">
        <span style="float:left ;font-size:20px;width:75%">
          论女装
          <br>
          <div style="width:300px;float:left">
            <el-link type="info" style="float:left">王佳奇</el-link>
          </div>
        </span>
        <span style="float:right">
          <el-button type="warning" icon="el-icon-star-off" circle></el-button>
          <el-button type="info" round>认证</el-button>
        </span>
      </div>
      <div>摘要</div>
      <div class="text item">
        This website template has been designed by sc.chinaz.com for you, for free. You can replace all this text with your own text. Consectetur adipiscing elit. Nunc id lectus ante, adipiscing scelerisque odio. Nam non massa felis, ac consequat quam. Sed turpis nisl, convallis ut varius nec, vestibulum vel sapien. Donec euismod varius tellus, blandit egestas felis facilisis ut. Donec mattis purus at dui auctor nec volutpat purus ullamcorper. Phasellus sit amet magna vitae tellus mollis pharetra sed dictum metus. Nam ultrices mauris ut metus lacinia vitae suscipit augue molestie. Nulla facilisi. Fusce eget velit erat. Sed viverra, est vitae viverra convallis, nisi nulla venenatis mauris, vitae sagittis mauris ante in libero. Integer in augue nec arcu bibendum pulvinar vitae in velit. Quisque pretium venenatis sapien, non condimentum purus sodales mattis. In hac habitasse platea dictumst. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nunc a quam eu tellus congue ornare quis vel augue.
        Donec id sapien molestie ipsum blandit pellentesque. Cras molestie aliquet tellus ac interdum. Mauris ullamcorper porttitor justo, ultricies adipiscing massa dapibus non. Cras arcu justo, facilisis sit amet molestie eget, volutpat et urna. Integer diam odio, vestibulum vitae pharetra tempor, porttitor quis nunc. Duis vulputate ante sed enim pharetra facilisis lobortis urna mattis. Donec eu quam ante, vitae ornare neque. Praesent posuere orci nec lorem tempor elementum sed ornare odio. Aenean id interdum augue.
      </div>
      <el-divider></el-divider>
      <div class="clearfix">
        <span style="float:left">
          <p style="float:left;margin: 4px 0px">DOI：123545</p>
          <br>
          <p style="float:left;margin: 4px 0px">被引量：1111111</p>
        </span>
        <span style="float:right">
          <el-button type="success">下载</el-button>
        </span>
      </div>
    </el-card>
  </div>

</template>

<script>
export default {
  name: "paperinfo"
};
</script>


<style scoped>
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
  height:400px
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 80%;
}
</style>
