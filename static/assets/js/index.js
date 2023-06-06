var localhost = "http://127.0.0.1:8000/" // API路由地址
var ul1 = document.getElementById("aa");
var ul2 = document.getElementById("aa1");
var ulbox = document.getElementById("box1");
var gd = document.getElementsByClassName('aa')
var ly = document.getElementById('ly')  //当前时间
var count = document.getElementById('count')//数据量
var cloud_count = document.getElementById('cloud_count')//数据量
var rand = Math.floor(Math.random() * 888);

window.onload = function (){
    // getroll();
}

setInterval(gxsj, 5000);
setInterval(getTime, 1000);



function getTime() {
    var myDate = new Date();
    var myYear = myDate.getFullYear(); //获取完整的年份(4位,1970-????)
    var myMonth = myDate.getMonth() + 1; //获取当前月份(0-11,0代表1月)
    var myToday = myDate.getDate(); //获取当前日(1-31)
    var myDay = myDate.getDay(); //获取当前星期X(0-6,0代表星期天)
    var myHour = myDate.getHours(); //获取当前小时数(0-23)
    var myMinute = myDate.getMinutes(); //获取当前分钟数(0-59)
    var mySecond = myDate.getSeconds(); //获取当前秒数(0-59)
    var week = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
    var nowTime;

    nowTime = myYear + '年' + fillZero(myMonth) + '月' + fillZero(myToday) + '日' + '  ' + fillZero(myHour) + ':' +
    fillZero(myMinute) + ':' + fillZero(mySecond) + '  ' + week[myDay] + '  ';
    $('#bjsj').html(nowTime);
};

function fillZero(str) {
    var realNum;
    if (str < 10) {
        realNum = '0' + str;
    } else {
        realNum = str;
    }
    return realNum;
}


$(
    function () {
        gxsj(ly);
    }
);

// 更新时间
function gxsj() {
    $.ajax({
      type: "GET",
      url: localhost + "app/update/?p=" + rand,
      dataType: "json",
      success: function (result) {
          var Time = result.data["数据获取时间"];

          ly.innerText = Time;
          $("#count").text(result.data["数据量"]);
          $("#cloud_count").text(result.data["词云数据量"]);
      }
    })
}
