<template>
  <div class="appeal">
    <appealForm :id="id" :title="title"></appealForm>
  </div>
</template>

<script>
import AppealForm from "@/components/AppealForm.vue";

export default {
  name: "appeal",
  created: function() {
    this.id = this.$route.query.id;
    this.title=this.$route.query.title;

  },
  data: function() {
    return {
      title: "",
      id:""
    };
  },
  components: {
    AppealForm
  }
};
</script>
<style>
.appeal {
  text-align: center;
  width: 75%;
}
</style>

