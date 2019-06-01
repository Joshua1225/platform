// 下方状态栏
// 删除无用信息
//仅作为展示性质

<script src="https://cdn.staticfile.org/vue/2.4.2/vue.min.js"></script>
<script src="https://unpkg.com/element-ui/lib/index.js"></script>

<template>
    
  <div class = "outer" id = "main">
		<div class="div-a">
			<div class="question">{{ask}}</div>
			<div class="question">{{question1}}</div>
			<div class="question">{{question2}}</div>
			<div class="question">{{question3}}</div>
		</div>
		<div class="div-b">
				<el-row :gutter="10">1111111</el-row>
			<div class="contact">{{contactus}}</div>
			<div class="contact">{{contact1}}</div>
			<div class="contact">{{contact2}}</div>
			<div class="contact">{{contact3}}</div>
		</div>
	</div>
</template>

<script>
export default {
  name: 'bottom',
  props: {
    msg: String
  }
}

new Vue({
		el: "#main",
		data:{
			ask: "常见问题",
			question1: "如何充值积分",
			question2: "如何修改兴趣领域",
			question3: "如何申诉",
			contactus: "联系我们",
			contact1 : "1234567890",
			contact2 : "1234567890",
			contact3 : "1234567890",

		}
	})

</script>