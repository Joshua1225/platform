
<template>

<div class="container" style="width:60%;margin: 0 auto;">

  <div id="myChart" :style="{width: '80%', height: '600px'}"></div>

</div>

</template>

<script>
import 'echarts-wordcloud';
import echarts from 'echarts';
import { throws } from 'assert';
export default {
  name: 'hello',
  //loadPath : this,
  data () {
    return { msg: 'Welcome to Your Vue.js App'
    }
  },
  mounted () {
    this.drawLine()
  },
  methods: {
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      var that = this
      var myChart = this.$echarts.init(document.getElementById('myChart'))
      var maskImage = new Image()
      myChart.on('click',function(params){
          console.log(params.name)
          that.$router.push('/Result')
      })
      maskImage.src = "data:image/png;base64,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"
      // 绘制图表

      maskImage.onload = function(){
        myChart.setOption( {
        title: {
            text: '热点词汇',//标题
            x: 'center',
            textStyle: {
                fontSize: 23
                
            }
        },
          backgroundColor:'#fff',
          tooltip: {
            show: false
          },
          series: [{
            name: '热点词汇',
            type: 'wordCloud',
            gridSize: 1,
            sizeRange: [10, 55],
            rotationRange: [ -45, 90],
            maskImage: maskImage,
            textStyle: {
              normal: {
                color: function() {
                  return 'rgb(' +
                      Math.round(Math.random() * 255) +
                      ', ' + Math.round(Math.random() * 255) +
                      ', ' + Math.round(Math.random() * 255) + ')'
                }
              }
            },
            left: 'center',
            top: 'center',
            right: null,
            bottom: null,
          data: [
              {
                name: 'Sam S Club',
                value: 10000,
                textStyle: {
                  normal: {
                    color: 'black'
                  },
                  emphasis: {
                    color: 'red'
                  }
                }
              },
              {
                name: 'Macys',
                value: 6181
              },
              {
                name: 'Amy Schumer',
                value: 4386
              },
              {
                name: 'Jurassic World',
                value: 4055
              },
              {
                name: 'Sam S Club',
                value: 10000,
            }, {
                name: 'Macys',
                value: 6181
            }, {
                name: 'Amy Schumer',
                value: 4386
            }, {
                name: 'Jurassic World',
                value: 4055
            }, {
                name: 'Charter Communications',
                value: 2467
            }, {
                name: 'Chick Fil A',
                value: 2244
            }, {
                name: 'Planet Fitness',
                value: 1898
            }, {
                name: 'Pitch Perfect',
                value: 1484
            }, {
                name: 'Express',
                value: 1112
            },{
                name: 'Home',
                value: 965
            }, {
                name: 'Johnny Depp',
                value: 847
            }, {
                name: 'Lena Dunham',
                value: 582
            }, {
                name: 'Lewis Hamilton',
                value: 555
            }, {
                name: 'KXAN',
                value: 550
            }, {
                name: 'Mary Ellen Mark',
                value: 462
            }, {
                name: 'Farrah Abraham',
                value: 366
            }, {
                name: 'Rita Ora',
                value: 360
            }, {
                name: 'Serena Williams',
                value: 282
            }, {
                name: 'NCAA baseball tournament',
                value: 273
            }, {
                name: 'Point' ,
                value: 273
            }, {
                name: 'Point Break',
                value: 265
            },
              {
                name: 'Charter Communications',
                value: 2467
              },
              {
                name: 'Sam S Club',
                value: 10000,
            }, {
                name: 'Macys',
                value: 6181
            }, {
                name: 'Amy Schumer',
                value: 4386
            }, {
                name: 'Jurassic World',
                value: 4055
            }, {
                name: 'Charter Communications',
                value: 2467
            }, {
                name: 'Chick Fil A',
                value: 2244
            }, {
                name: 'Planet Fitness',
                value: 1898
            }, {
                name: 'Pitch Perfect',
                value: 1484
            }, {
                name: 'Express',
                value: 1112
            }, {
                name: 'Home',
                value: 965
            }, {
                name: 'Johnny Depp',
                value: 847
            },{
                name: 'Macys',
                value: 6181
              },
              {
                name: 'Amy Schumer',
                value: 4386
              },
              {
                name: 'Jurassic World',
                value: 4055
              },
              {
                name: 'Sam S Club',
                value: 10000,
            }, {
                name: 'Macys',
                value: 6181
            }, {
                name: 'Amy Schumer',
                value: 4386
            }, {
                name: 'Jurassic World',
                value: 4055
            }, {
                name: 'Charter Communications',
                value: 2467
            }, {
                name: 'Chick Fil A',
                value: 2244
            }, {
                name: 'Planet Fitness',
                value: 1898
            }, {
                name: 'Pitch Perfect',
                value: 1484
            }, {
                name: 'Express',
                value: 1112
            }, {
                name: 'Home',
                value: 965
            }, {
                name: 'Johnny Depp',
                value: 847
            }, {
                name: 'Lena Dunham',
                value: 582
            }, {
                name: 'Lewis Hamilton',
                value: 555
            }, {
                name: 'KXAN',
                value: 550
            }, {
                name: 'Mary Ellen Mark',
                value: 462
            }, {
                name: 'Farrah Abraham',
                value: 366
            }, {
                name: 'Rita Ora',
                value: 360
            }, {
                name: 'Serena Williams',
                value: 282
            }, {
                name: 'NCAA baseball tournament',
                value: 273
            }, {
                name: 'Point' ,
                value: 273
            }, {
                name: 'Point Break',
                value: 265
            },
              {
                name: 'Charter Communications',
                value: 2467
              },
              {
                name: 'Sam S Club',
                value: 10000,
            }, {
                name: 'Macys',
                value: 6181
            }, {
                name: 'Amy Schumer',
                value: 4386
            }, {
                name: 'Jurassic World',
                value: 4055
            }, {
                name: 'Charter Communications',
                value: 2467
            }, {
                name: 'Chick Fil A',
                value: 2244
            }, {
                name: 'Planet Fitness',
                value: 1898
            }, {
                name: 'Pitch Perfect',
                value: 1484
            }, {
                name: 'Express',
                value: 1112
            }, {
                name: 'Home',
                value: 965
            }, {
                name: 'Johnny Depp',
                value: 847
            },
            {
                name: 'Macys',
                value: 6181
              },
              {
                name: 'Amy Schumer',
                value: 4386
              },
              {
                name: 'Jurassic World',
                value: 4055
              },
              {
                name: 'Sam S Club',
                value: 10000,
            }, {
                name: 'Macys',
                value: 6181
            }, {
                name: 'Amy Schumer',
                value: 4386
            }, {
                name: 'Jurassic World',
                value: 4055
            }, {
                name: 'Charter Communications',
                value: 2467
            }, {
                name: 'Chick Fil A',
                value: 2244
            }, {
                name: 'Planet Fitness',
                value: 1898
            }, {
                name: 'Pitch Perfect',
                value: 1484
            }, {
                name: 'Express',
                value: 1112
            }, {
                name: 'Home',
                value: 965
            }, {
                name: 'Johnny Depp',
                value: 847
            }, {
                name: 'Lena Dunham',
                value: 582
            }, {
                name: 'Lewis Hamilton',
                value: 555
            }, {
                name: 'KXAN',
                value: 550
            }, {
                name: 'Mary Ellen Mark',
                value: 462
            }, {
                name: 'Farrah Abraham',
                value: 366
            }, {
                name: 'Rita Ora',
                value: 360
            }, {
                name: 'Serena Williams',
                value: 282
            }, {
                name: 'NCAA baseball tournament',
                value: 273
            }, {
                name: 'Point' ,
                value: 273
            }, 
            {
                name: 'Home',
                value: 965
            }, {
                name: 'Johnny Depp',
                value: 847
            }, {
                name: 'Lena Dunham',
                value: 582
            }, {
                name: 'Lewis Hamilton',
                value: 555
            }, {
                name: 'KXAN',
                value: 550
            }, {
                name: 'Mary Ellen Mark',
                value: 462
            }, {
                name: 'Farrah Abraham',
                value: 366
            }, {
                name: 'Rita Ora',
                value: 360
            }, {
                name: 'Serena Williams',
                value: 282
            }, {
                name: 'NCAA baseball tournament',
                value: 273
            }, {
                name: 'Point' ,
                value: 273
            }, {
                name: 'Point Break',
                value: 265
            },
              {
                name: 'Charter Communications',
                value: 2467
              },
              {
                name: 'Sam S Club',
                value: 10000,
            }, {
                name: 'Macys',
                value: 6181
            }, {
                name: 'Amy Schumer',
                value: 4386
            }, {
                name: 'Jurassic World',
                value: 4055
            }, {
                name: 'Charter Communications',
                value: 2467
            }, {
                name: 'Chick Fil A',
                value: 2244
            }, {
                name: 'Planet Fitness',
                value: 1898
            }, {
                name: 'Pitch Perfect',
                value: 1484
            }, {
                name: 'Express',
                value: 1112
            }, {
                name: 'Home',
                value: 965
            }, {
                name: 'Johnny Depp',
                value: 847
            },{
                name: 'Macys',
                value: 6181
              },
              {
                name: 'Amy Schumer',
                value: 4386
              },
              {
                name: 'Jurassic World',
                value: 4055
              },
              {
                name: 'Sam S Club',
                value: 10000,
            }, {
                name: 'Macys',
                value: 6181
            }, {
                name: 'Amy Schumer',
                value: 4386
            }, {
                name: 'Jurassic World',
                value: 4055
            }, {
                name: 'Charter Communications',
                value: 2467
            }, {
                name: 'Chick Fil A',
                value: 2244
            }, {
                name: 'Planet Fitness',
                value: 1898
            }, {
                name: 'Pitch Perfect',
                value: 1484
            }, {
                name: 'Express',
                value: 1112
            }, {
                name: 'Home',
                value: 965
            }, {
                name: 'Johnny Depp',
                value: 847
            }, {
                name: 'Lena Dunham',
                value: 582
            }, {
                name: 'Lewis Hamilton',
                value: 555
            }, {
                name: 'KXAN',
                value: 550
            }, {
                name: 'Mary Ellen Mark',
                value: 462
            }, {
                name: 'Farrah Abraham',
                value: 366
            }, {
                name: 'Rita Ora',
                value: 360
            }, {
                name: 'Serena Williams',
                value: 282
            }, {
                name: 'NCAA baseball tournament',
                value: 273
            }, {
                name: 'Point' ,
                value: 273
            }, {
                name: 'Point Break',
                value: 265
            },
              {
                name: 'Charter Communications',
                value: 2467
              },
              {
                name: 'Sam S Club',
                value: 10000,
            }, {
                name: 'Macys',
                value: 6181
            }, {
                name: 'Amy Schumer',
                value: 4386
            }, {
                name: 'Jurassic World',
                value: 4055
            }, {
                name: 'Charter Communications',
                value: 2467
            }, {
                name: 'Chick Fil A',
                value: 2244
            }, {
                name: 'Planet Fitness',
                value: 1898
            }, {
                name: 'Pitch Perfect',
                value: 1484
            }, {
                name: 'Express',
                value: 1112
            }, {
                name: 'Home',
                value: 965
            }, {
                name: 'Johnny Depp',
                value: 847
            },
            {
                name: 'Macys',
                value: 6181
              },
              {
                name: 'Amy Schumer',
                value: 4386
              },
              {
                name: 'Jurassic World',
                value: 4055
              },
              {
                name: 'Sam S Club',
                value: 10000,
            }, {
                name: 'Macys',
                value: 6181
            }, {
                name: 'Amy Schumer',
                value: 4386
            }, {
                name: 'Jurassic World',
                value: 4055
            }, {
                name: 'Charter Communications',
                value: 2467
            }, {
                name: 'Chick Fil A',
                value: 2244
            }, {
                name: 'Planet Fitness',
                value: 1898
            }, {
                name: 'Pitch Perfect',
                value: 1484
            }, {
                name: 'Express',
                value: 1112
            }, {
                name: 'Home',
                value: 965
            }, {
                name: 'Johnny Depp',
                value: 847
            }, {
                name: 'Lena Dunham',
                value: 582
            }, {
                name: 'Lewis Hamilton',
                value: 555
            }, {
                name: 'KXAN',
                value: 550
            }, {
                name: 'Mary Ellen Mark',
                value: 462
            }, {
                name: 'Farrah Abraham',
                value: 366
            }, {
                name: 'Rita Ora',
                value: 360
            }, {
                name: 'Serena Williams',
                value: 282
            }, {
                name: 'NCAA baseball tournament',
                value: 273
            }, {
                name: 'Point' ,
                value: 273
            }, {
                name: 'Point Break',
                value: 265
            },
              {
                name: 'Charter Communications',
                value: 2467
              },
              {
                name: 'Sam S Club',
                value: 10000,
            }, {
                name: 'Macys',
                value: 6181
            }, {
                name: 'Amy Schumer',
                value: 4386
            }, {
                name: 'Jurassic World',
                value: 4055
            }, {
                name: 'Charter Communications',
                value: 2467
            }, {
                name: 'Chick Fil A',
                value: 2244
            }, {
                name: 'Planet Fitness',
                value: 1898
            }, {
                name: 'Pitch Perfect',
                value: 1484
            }, {
                name: 'Express',
                value: 1112
            }, {
                name: 'Home',
                value: 965
            }, {
                name: 'Johnny Depp',
                value: 847
            },
             {
                name: 'Lena Dunham',
                value: 582
            }, {
                name: 'Lewis Hamilton',
                value: 555
            }, {
                name: 'KXAN',
                value: 550
            }, {
                name: 'Mary Ellen Mark',
                value: 462
            }, {
                name: 'Farrah Abraham',
                value: 366
            }, {
                name: 'Rita Ora',
                value: 360
            }, {
                name: 'Serena Williams',
                value: 282
            }, {
                name: 'NCAA baseball tournament',
                value: 273
            }, {
                name: 'Point' ,
                value: 273
            }, {
                name: 'Point Break',
                value: 265
            },
              {
                name: 'Chick Fil A',
                value: 2244
              },
              {
                name: 'Planet Fitness',
                value: 1898
              },
              {
                name: 'Pitch Perfect',
                value: 1484
              },
              {
                name: 'Express',
                value: 1112
              },
              {
                name: 'Home',
                value: 965
              },
              {
                name: 'Johnny Depp',
                value: 847
              },
              {
                name: 'Lena Dunham',
                value: 582
              },
              {
                name: 'Lewis Hamilton',
                value: 555
              },
              {
                name: 'KXAN',
                value: 550
              },
              {
                name: 'Mary Ellen Mark',
                value: 462
              },
              {
                name: 'Farrah Abraham',
                value: 366
              },
              {
                name: 'Rita Ora',
                value: 360
              },
              {
                name: 'Serena Williams',
                value: 282
              },
              {
                name: 'NCAA baseball tournament',
                value: 273
              },
              {
                name: 'Point Break',
                value: 265
              }
            ]

        }]

      })
      // 为echarts对象加载数据

      myChart.setOption(option)

    }

  }
  }
}

</script>

<style>

 

</style>
