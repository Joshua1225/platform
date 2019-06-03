<style>
.message-style{
    float: left;
    font-size: 16px;
    height: 40px;
}

</style>

<template>
  <div>
    <el-row>
      <el-card shadow="always">
        <div class="message-style">您有{{messagenum}}条未读通知</div>
      </el-card>
    </el-row>
        <MessageList/>
    
  </div>
</template>

<script>
import MessageList from '@/components/MessageList.vue'
export default {
  name: "Message",
  components: {
    MessageList
  },
  data: function()
  {
    return {
        messagenum:100,
    }
  }
};
</script>
