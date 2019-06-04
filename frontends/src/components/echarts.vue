
<template>
  <div style="width:100%;margin: 0 auto;">
    <div id="myChart" :style="{width: '60%', height: '450px' , margin: '0 auto'}"></div>
  </div>
</template>

<script>
import "echarts-wordcloud";
import echarts from "echarts";
import { throws } from "assert";
import axios from "axios";

//var host="http://154.8.237.76:8000";
var host="";

export default {
  name: "excharts",
  //loadPath : this,
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      data1: [1, 2, 3]
    };
  },
  mounted() {
    this.drawLine();
  },
  methods: {
    drawLine() {
      // 基于准备好的dom，初始化echarts实例
      var that = this;
      var myChart = this.$echarts.init(document.getElementById("myChart"));
      var maskImage = new Image();
      myChart.on("click", function(params) {
        console.log(params.name);
        that.$router.push({
          path : "/Result",
          query : {
            model1 : 0,
            q:params.name,
            order : 0,
            page_size:10,
            page_num:1,
          }
      })
      });
      maskImage.src =
        "data:image/png;base64,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";

      // 绘制图表
      maskImage.onload = function() {
        axios
          .post(host+"/getkeyword")
          .then(res => {
            //console.log("res", res);
            this.data1 = res['data'];
            //console.log("data1", this.data1);
            //console.log("onload", this.data1),
              myChart.setOption({
                // titletitle: {
                //   text: "热点词汇", //标题
                //   x: "center",
                //   textStyle: {
                //     fontSize: 23
                //   }
                // },
                backgroundColor: "#fff",
                tooltip: {
                  show: false
                },
                series: [
                  {
                    name: "热点词汇",
                    type: "wordCloud",
                    gridSize: 1,
                    sizeRange: [15, 50],
                    rotationRange: [-45, 90],
                    maskImage: maskImage,
                    textStyle: {
                      normal: {
                        color: function() {
                          return (
                            "rgb(" +
                            Math.round(Math.random() * 255) +
                            ", " +
                            Math.round(Math.random() * 255) +
                            ", " +
                            Math.round(Math.random() * 255) +
                            ")"
                          );
                        }
                      }
                    },
                    left: "center",
                    top: "center",
                    right: null,
                    bottom: null,
                    data: this.data1,
                  }
                ]
              });
            // 为echarts对象加载数据

            myChart.setOption(option);
          })
          .catch(res => {
            console.log(res);
          });
      };
    }
  }
};
</script>

<style>
</style>
