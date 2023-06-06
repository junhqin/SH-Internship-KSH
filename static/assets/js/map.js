$(
    function () {
        render_map();
    }
);

function render_map() {
    console.log(points)
    var map = new BMap.Map(document.querySelector(".container1"));
    var point = new BMap.Point(121.409809, 31.228032);
    map.centerAndZoom(point, 15);
    map.enableScrollWheelZoom();
    if (!isSupportCanvas()) {
        alert('热力图目前只支持有canvas支持的浏览器,您所使用的浏览器不能使用热力图功能~')
    }
    heatmapOverlay = new BMapLib.HeatmapOverlay({"radius": 20});
    map.addOverlay(heatmapOverlay);
    var heatmapData = [];

    for (var i = 0; i < points.length; i++) {
        var point = points[i][0];
        var lng = point[3];
        var lat = point[4];
        var url = point[5];
        heatmapData.push({lng: lng, lat: lat, count: 400});
    }
    console.log(heatmapData);
    heatmapOverlay.setDataSet({data: heatmapData, max: 800});
    function setGradient() {
        var gradient = {};
        var colors = document.querySelectorAll("input[type='color']");
        colors = [].slice.call(colors, 0);
        colors.forEach(function (ele) {
            gradient[ele.getAttribute("data-key")] = ele.value;
        });
        heatmapOverlay.setOptions({"gradient": gradient});
    }

    function isSupportCanvas() {
        var elem = document.createElement('canvas');
        return !!(elem.getContext && elem.getContext('2d'));
    }
    //华师大校园点
    var fixedPoint = new BMap.Point(121.409809, 31.228032);
    // 创建一个自定义标注覆盖物
    function CustomOverlay(point) {
      this._point = point;
    }
    // 继承覆盖物类的初始化方法
    CustomOverlay.prototype = new BMap.Overlay();
    CustomOverlay.prototype.initialize = function (map) {
      this._map = map;
      var div = document.createElement("div");
      div.className = "icofont icofont-home";
       div.style.color = "#587187"; // 设置图标的颜色
      div.style.fontSize = "50px"; // 设置图标的大小
      div.style.width = 0; // 设置覆盖物的宽度
      div.style.height = 0; // 设置覆盖物的高度
      div.style.position = "absolute";
      div.style.zIndex = BMap.Overlay.getZIndex(this._point.lat);

      this._div = div;
      map.getPanes().markerPane.appendChild(div);
      return div;
    };
    CustomOverlay.prototype.draw = function () {
      var position = this._map.pointToOverlayPixel(this._point);
      var iconSize = 50; // 图标的尺寸
      this._div.style.left = position.x - iconSize / 2 + "px"; // 将图标在 x 轴方向上居中
      this._div.style.top = position.y - iconSize / 2 + "px"; // 将图标在 y 轴方向上居中
    };

    // 创建自定义标注覆盖物对象
    var customOverlay = new CustomOverlay(fixedPoint);

    // 将自定义标注添加到地图上
    map.addOverlay(customOverlay);
    //遍历列表中的每个点，创建直线对象，并添加到地图中
    var lines = [];
    var markers = [];
    for (var i = 0; i < points.length; i++) {
        var point = points[i][0];
        var lng = point[3];
        // console.log(point[3]);
        var lat = point[4];
        var bmapPoint = new BMap.Point(lng, lat);
        var line = new BMap.Polyline([fixedPoint, bmapPoint], {
            strokeColor: "#00b3ff",
            strokeWeight: 2,
            strokeOpacity: 1
        });
        lines.push(line);
        map.addOverlay(line);
        //在每个点上添加一个突出的点
        var marker = new BMap.Marker(bmapPoint);

        map.addOverlay(marker);
        //在每个点上添加一个点击事件，弹出一个信息窗口
        marker.addEventListener("click", function (e) {
            //获取当前点击的点的索引
            var index = e.target.index;
            //获取当前点击的点的信息
            var info = points[index];
            console.log(info[0])
            //创建一个信息窗口的内容
            var content = "<h4>职位名称：<a href='" + info[0][5] + "'>" + info[0][1] + "</a></h4>" +
                "<p>公司名称：" + info[0][0] + "</p>" +
                "<p>地址：" + info[0][2] + "</p>";
            //创建一个信息窗口对象
            var infoWindow = new BMap.InfoWindow(content, {enableCloseOnClick: true});
            //在当前点击的点上打开信息窗口
            e.target.openInfoWindow(infoWindow);
        });
        //给每个点添加一个自定义属性，用于存储索引
        marker.index = i;
        markers.push(marker);
    }

    //获取两个按钮元素
    var heatmapButton = document.getElementById("heatmap");
    var polylineButton = document.getElementById("polyline");
    var lineButton = document.getElementById("line");
    var resetButton = document.getElementById("reset");
    //给热力图按钮添加一个点击事件，显示热力图，隐藏直线图和点
    heatmapButton.addEventListener("click", function () {
        heatmapOverlay.show();
        // map.removeOverlay(polylineOverlay);
        for (var i = 0; i < lines.length; i++) {
            lines[i].hide();
        }

        for (var i = 0; i < markers.length; i++) {
            map.removeOverlay(markers[i]);
        }
    });

    lineButton.addEventListener('click',function()
        {
            heatmapOverlay.hide();
            for (var i = 0; i < lines.length; i++) {
                lines[i].hide();
            }
        }
        )
    resetButton.addEventListener('click',function() {
            var point = new BMap.Point(121.409809, 31.228032);
            map.centerAndZoom(point, 15);
        }
    )

    //给直线图按钮添加一个点击事件，显示直线图，隐藏热力图
    polylineButton.addEventListener("click", function () {
        heatmapOverlay.hide();
        for (var i = 0; i < lines.length; i++) {
            lines[i].show();
        }
        for (var i = 0; i < markers.length; i++) {
            map.addOverlay(markers[i]);
        }
    });
        // 监听窗口大小变化事件
    window.addEventListener("resize", function () {
      map.setZoom(map.getZoom());
      var center = map.getCenter();
      map.setCenter(center);
    });

}