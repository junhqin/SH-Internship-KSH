var localhost = "http://127.0.0.1:8000/" // API路由地址
var chartDom = document.getElementById('g1');
var rand = Math.floor(Math.random() * 888);
var chartDom2 = document.getElementById('g2');
$(
    function () {
        avg_s();
        lan_fre();
        job_fre();
        g4();

    }
);
function avg_s() {
    var show;
    $.ajax({
      type: "GET",
      url: localhost + "app/avg_salary/?p=" + rand,
      dataType: "json",
      success: function (result) {
        console.log(result.data)
        show = result.data;
        // console.log(show);
        var myChart = echarts.init(chartDom);
        var option;
        const gaugeData = [
        {
            value: show['大专'][1].toFixed(2),
            name: '专科',
            title: {
            offsetCenter: ['0%', '-50%']
            },
            detail: {
            valueAnimation: true,
            offsetCenter: ['0%', '-40%']
            }
        },
        {
            value: show['本科'][1].toFixed(2),
            name: '本科',
            title: {
            offsetCenter: ['0%', '-20%']
            },
            detail: {
            valueAnimation: true,
            offsetCenter: ['0%', '-10%']
            }
        },
        {
            value: show['硕士'][1].toFixed(2),
            name: '硕士',
            title: {
            offsetCenter: ['0%', '10%']
            },
            detail: {
            valueAnimation: true,
            offsetCenter: ['0%', '20%']
            }
        },
        {
            value: show['total'][1].toFixed(2),
            name: '不限',
            title: {
            offsetCenter: ['0%', '40%']
            },
            detail: {
            valueAnimation: true,
            offsetCenter: ['0%', '50%']
            }
        }
        ];
        option = {
        series: [
            {
            type: 'gauge',
            startAngle: 90,
            endAngle: -270,
            max:300,
            pointer: {
                show: false
            },
            progress: {
                show: true,
                overlap: false,
                roundCap: true,
                clip: false,
                itemStyle: {
                borderWidth: 1,
                borderColor: '#464646'
                }
            },
            axisLine: {
                lineStyle: {
                width: 40
                }
            },
            splitLine: {
                show: false,
                distance: 1,
                length: 20
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                show: false,
                distance: 50
            },
            data: gaugeData,
            title: {
                fontSize: 14
            },
            detail: {
                width: 70,
                height: 24,
                fontSize: 14,
                color: 'inherit',
                borderColor: 'inherit',
                borderRadius: 30,
                borderWidth: 1,
                formatter: '{value}￥/天'
            },

            }
        ]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
        });
      }
    })
}
let timerId = setInterval(() => avg_s(), 10000);
let timerId2 = setInterval(() => lan_fre(), 5000);
let timerId3 = setInterval(() => job_fre(), 5000);
let timerId4 = setInterval(() => g4(), 5000);
let timerId5 = setInterval(() => SankeyChart(), 10000);
function lan_fre()
{
    $.ajax({
        type: "GET",
        url: localhost + "app/lan_fre/?p=" + rand,
        dataType: "json",
        success: function (result) {
            var myChart2 = echarts.init(chartDom2);
            var option;//分配的设置
            option = {
            title: {
                text: ''
            },
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b} : {c}'
            },
            toolbox: {
                feature: {
                dataView: { readOnly: false },
                restore: {},
                saveAsImage: {}
                }
            },
            legend: {
                data: ['Show', 'Click', 'Visit', 'Inquiry', 'Order']
            },
            series: [
                {
                name: 'Language',
                type: 'funnel',
                left: '10%',
                top: 60,
                bottom: 60,
                width: '80%',
                min: 0,
                max: 450,
                minSize: '0%',
                maxSize: '100%',
                sort: 'descending',
                gap: 2,
                label: {
                    show: true,
                    position: 'inside'
                },
                labelLine: {
                    length: 10,
                    lineStyle: {
                    width: 1,
                    type: 'solid'
                    }
                },
                itemStyle: {
                    borderColor: '#fff',
                    borderWidth: 1
                },
                emphasis: {
                    label: {
                    fontSize: 20
                    }
                },
                data : result.data

                }
                ]
            };
            myChart2.setOption(option);
            window.addEventListener("resize", function() {
                myChart2.resize();
            });
        },
    })
}

function job_fre()
{
    $.ajax({
      type: "GET",
      url: localhost + "app/job_fre/?p=" + rand,
      dataType: "json",
      success: function (result) {
        console.log(result.data)
        var chartDom3 = document.getElementById('g3');
        var myChart3 = echarts.init(chartDom3);
        var option;
        var jsonData = result.data;
        // console.log(jsonData);
        var dataAxis = Object.keys(jsonData);
        let data = Object.values(jsonData);

        let yMax = 400;
        let dataShadow = [];
        for (let i = 0; i < data.length; i++) {
            dataShadow.push(yMax);
        }
        option = {
        title: {
            text: '滚动进行缩放查看',
            subtext: 'Feature Sample: Gradient Color, Shadow, Click Zoom'
        },
        xAxis: {
            data: dataAxis,
            axisLabel: {
            inside: true,
            color: '#000'
            },
            axisTick: {
            show: false
            },
            axisLine: {
            show: false
            },
            z: 10
        },
        yAxis: {
            axisLine: {
            show: false
            },
            axisTick: {
            show: false
            },
            axisLabel: {
            color: '#999'
            }
        },
        dataZoom: [
            {
            type: 'inside'
            }
        ],
        series: [
            {
            type: 'bar',
            showBackground: true,
            itemStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: '#83bff6' },
                { offset: 0.5, color: '#188df0' },
                { offset: 1, color: '#188df0' }
                ])
            },
            emphasis: {
                itemStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    { offset: 0, color: '#2378f7' },
                    { offset: 0.7, color: '#2378f7' },
                    { offset: 1, color: '#83bff6' }
                ])
                }
            },
            data: data
            }
        ]
        };
        // Enable data zoom when user click bar.
        const zoomSize = 6;
        myChart3.on('click', function (params) {
        console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
        myChart3.dispatchAction({
            type: 'dataZoom',
            startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
            endValue:
            dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
        });
        });
        myChart3.setOption(option);
        window.addEventListener("resize", function() {
            myChart3.resize();
        });
      }

    })
}

function g4()
{
    $.ajax({
      type: "GET",
      url: localhost + "app/g4/?p=" + rand,
      dataType: "json",
        success:function (result)
        {
            jsonData = result.data;
            var chartDom4 = document.getElementById('g4');
            var myChart4 = echarts.init(chartDom4);
            var option;

            option = {
            tooltip: {
                trigger: 'item'
            },
            legend: {
                top: '5%',
                left: 'center'
            },
            series: [
                {
                name: '实习领域',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 10,
                    borderColor: '#fff',
                    borderWidth: 2
                },
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                    show: true,
                    fontSize: 40,
                    fontWeight: 'bold',
                    formatter:  function(param) {
                        // console.log(param.data);
                        return  param.data['name'] + " " + param.data['value'];
                    },
                    }
                },
                labelLine: {
                    show: false
                },
                data: jsonData
                }
            ]
            };
            myChart4.setOption(option);
            window.addEventListener("resize", function() {
                myChart4.resize();
            });
        }
    })
}

// 桑葚图
function SankeyChart()
{
    $.ajax({
    type: "GET",
    url: localhost + "app/sankey/",
    dataType: "json",
    success: function (result) {
        var options = result.data;
        var sankeyChart = echarts.init(document.getElementById('g6'));
        sankeyChart.setOption(options);
        window.addEventListener("resize", function() {
            sankeyChart.resize();
        });
    }
});
}

function renderChart(chart) {
    var chartHeight = chart.getHeight();
    $('.chart-container').height(chartHeight);
}


// 页面加载完成后调用 SankeyChart() 函数
$(document).ready(function() {
    SankeyChart();
});