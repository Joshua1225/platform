<template>
    <div style="width:60%;margin: 0 auto;">
      <el-image style="width: 350px; height: 100px; margin-top: 70px" :src="url" fit="contain"></el-image>
      <el-input  style="margin-top:70px" v-model="input" placeholder="请输入搜索内容">
        <el-popover
            placement="left"
            width="100%"
            v-model="visible"
            slot="append">
            <div class="showsearch">包含全部检索词我的:<el-input v-model="input1" placeholder="包含全部检索词" ></el-input></div>
            <div class="showsearch">包含精确检索词:<el-input v-model="input2" placeholder="包含全部检索词" ></el-input></div>
            <div class="showsearch">包含至少一个检索词:<el-input v-model="input3" placeholder="包含全部检索词" ></el-input></div>
            <div class="showsearch">不包含检索词:<el-input v-model="input4" placeholder="包含全部检索词" ></el-input></div>
            <div class="showsearch">出现检索词的位置<el-input v-model="input5" placeholder="包含全部检索词" ></el-input></div>
            <div class="showsearch">作者<el-input v-model="input6" placeholder="包含全部检索词" ></el-input></div>
            <div class="showsearch">出版物:<el-input v-model="input7" placeholder="包含全部检索词" ></el-input></div>
            <div class="showsearch">发表时间<el-input v-model="input8" placeholder="包含全部检索词" ></el-input></div>
            <div class="showsearch">语言检索范围<el-input v-model="input9" placeholder="包含全部检索词" ></el-input></div>
            <div style="text-align: right; margin: 0">
                <el-button size="mini" type="text" @click="visible = false" style="margin-top:10px">取消</el-button>
                <el-button type="primary" size="mini" @click="visible = false">搜索</el-button>
            </div>
            <el-button slot="reference" icon="el-icon-arrow-down" style="margin:0 width='5%'"></el-button>
        </el-popover>
        <el-button slot="append" type="primary" icon="el-icon-search" @click="toSearch">搜索</el-button>
    </el-input>

    
    </div>
</template>
<script>
  export default {
    name: 'SearchBar',
    methods :{
       toSearch(){
         this.$router.push('/Result')
       }
     },
    data() {
      return {
        input :'',
        input1 :'',
        input2 :'',
        input3 :'',
        input4 :'',
        input5 :'',
        input6 :'',
        input7 :'',
        input8 :'',
        input9 :'',
        visible: false,
        url:require('@/assets/logo.jpg'),
      };
    }
  }
</script>

<style scoped>
.el-dropdown {
vertical-align: top;
}
.el-dropdown + .el-dropdown {
margin-left: 15px;
}
.el-icon-arrow-down {
font-size: 12px;
}
.showsearch {
width: 750px;
margin: 0 auto;
text-align:left;
}
</style>