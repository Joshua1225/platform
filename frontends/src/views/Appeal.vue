<template>
  <div>
    <appealForm :obj='obj'></appealForm>
  </div>
</template>

<script>
import AppealForm from "@/components/AppealForm.vue";

export default {
  name: "appeal",
  data: function() {
    return {
      obj: "father",
      type: "认证"
    };
  },
  components: {
    AppealForm
  }
};
</script>
