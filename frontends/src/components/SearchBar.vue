//搜索框+搜索按钮
//
<template>
    <div>
        <el-button @click="toResult">搜索</el-button>
    </div>
</template>

<script>

export default {
    name:'searchBar',
    methods:{
        toResult:function(){
            this.$router.push("/result")
        }
    }
}
</script>
