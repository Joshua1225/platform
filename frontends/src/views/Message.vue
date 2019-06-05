<style>
.message-style {
  float: left;
  font-size: 16px;
  height: 40px;
}
</style>

<template>
  <div style="padding:10px">
      <el-card
        shadow="always"
        body-style="{padding-top : 5px ; text-align : left ; font-size : 13px ;}"
      >您有{{messagenum}}条未读通知</el-card>
  
    <MessageList :message="message" />
  </div>
</template>

<script>
import MessageList from "@/components/MessageList.vue";
export default {
  name: "Message",
  props:{
    message:[]
  },
  components: {
    MessageList
  },
  data: function() {
    return {
      messagenum: this.message.length
    };
  }
};
</script>
