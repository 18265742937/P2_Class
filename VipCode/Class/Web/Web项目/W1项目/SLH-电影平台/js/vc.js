$(function() {
    var vip_nav1 = $('.vipnav'); /** 导航栏  增加导航栏的class */
    vip_nav1.addClass("navbar navbar-expand-lg navbar-dark bg-dark fixed-top");

    // $('.myClass').addClass("navbar-brand"); /**导航栏第一个链接 */

    $('.vc_button').addClass("navbar-toggler"); /** 手机端的导航栏按钮 */
    var vip_navButton = $('.vc_button');
    vip_navButton.attr({ "data-toggle": "collapse", "aria-controls": "navbarNav", "aria-expanded": "false", "aria-label": "Toggle navigation" });
    var vc_icon = '<span class="navbar-toggler-icon"></span>'
    $(".vc_button").append(vc_icon) /*按钮图标 */

    $('.vc_hide').addClass("collapse navbar-collapse"); //隐藏导航栏

    $('.vipul').addClass("navbar-nav mr-auto"); //导航栏的ul列表

    var vip_dropdownId = $('.dropdown-toggle'); /**下拉菜单  简化下拉菜单*/
    vip_dropdownId.attr({ "role": "button", "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false" });



    var vip_tap = $('.vc_tab'); //封装ul的tap点击页面
    vip_tap.addClass("nav nav-tabs");
    vip_tap.attr({ "role": "tablist" });

    var vip_tapContent = $('.vc_content'); //封装分页栏的内容栏部分
    vip_tapContent.addClass("tab-content");
    vip_tapContent.attr({ "id": "myTabContent" });


    var vip_link2 = $('.vclink'); //封装“日志”点击链接，默认是主页，这里无特殊效果，默认aria-selected为false
    vip_link2.addClass("nav-link"); //不加active ，没有特殊显示
    vip_link2.attr({ "data-toggle": "pill", "role": "tab", "aria-selected": "false" });

    var vip_tabPane = $('.vc_pane'); //封装跳转栏的class
    vip_tabPane.addClass("tab-pane fade");
    vip_tabPane.attr({ "role": "tabpanel" });

    var vip_navflex = $('.vc_flex');
    vip_navflex.addClass("nav flex-column nav-pills");
    vip_navflex.attr({ "role": "tablist", "aria-orientation": "vertical" });

    var w = $(window).width();
    if (w < 800) {
        $("#slide").css("height", w / 2 + "px")
        $(".pic").css("height", w / 3 + "px")
    } else {
        $(".pic").css("height", "400px")
    }
});

function getStyle(obj) { //获取标签的top值
    if (obj.currentStyle) {
        return obj.currentStyle.top
    } else {
        return getComputedStyle(obj).top
    };
}



function getProper(num) {
    const width = ($(window).width() - 120) / num;
    return {
        imgWidth: width,
        imgGap: width + 40 / (num - 1)
    };
}








//图片抖动
// var aImg = $(".img_list img");
// var imgObj = getProper(aImg.length);
// for (i = 0; i < aImg.length; i++) {
//     aImg[i].style.width = imgObj.imgWidth + "px";
//     aImg[i].style.left = 40 + i * imgObj.imgGap + "px";
//     aImg[i].onmouseover = onmouse;
//     var pos = parseInt(getStyle(aImg[i]));
// }

// function onmouse(event) {
//     var on_img = event.target
//     var arr = [30, -30, 28, -28, 0];

//     var shake = setInterval(motion, 20); //每隔20毫秒执行一次抖动

//     function motion() {
//         if (arr.length > 0) {
//             on_img.style.top = pos + arr.shift() + "px";
//         } else {
//             clearInterval(shake);
//         }
//     }
// }

//渐变轮播
var pic = $('.pic img')
var index = pic.length - 2;
var length = pic.length;
var index2 = index + 1;

function transform() {
    if (index2 === length) {
        index2 = 0;
    }

    pic.eq(index2).fadeOut(2000);
    pic.eq(index).fadeIn(2000);
    if (index === 0) {
        index = pic.length - 1;
    } else {
        index--;
        index2 = index + 1;
    }
};
transform()
setInterval(transform, 3000);

//雪花特效
// ========class09========================================
// 完善上节课的雪花飘落效果（要求学生可以捋清楚逻辑并实现效果就可以了）
var snownum = setInterval(snowImg, 100);
var number = 1; //设置雪花的初始数量

function snowImg() {
    // 判断雪花的数量（限制雪花数量）
    if (number > 300) {
        clearInterval(snownum);
    }
    number++;
    // ========class09结束============================
    $(".snow").append('<img src="image/snow.png" class="snow_img">');     
    $(".snow_img").each(snow_random); 
}

function snow_random(index, element) { 
    var wid = $(window).width();
    // 获取浏览器的高度
    var hig = $(window).height(); //====class09================
    // 计算雪花随机的left值，控制雪花飘落的方向
    var float_left = Math.random() * wid * 2 - wid + "px"; //===class09===
    var snow_time = (Math.random() * 10 + 4) * 1000;
    $(element).animate({
        // 根据浏览器的高度飘落雪花
        top: hig + "px", //=======class09=====================
        left: float_left,
    }, snow_time);  
    // =====class09===========================================
    // 让雪花从随机位置落下
    var wid_left = Math.random() * wid + "px";       //计算随机的宽度
    // 根据雪花的左外边距做判断，修改雪花的随机位置      
    if ($(element).css("margin-left") == 1 + "px") {                
        $(element).css("margin-left", wid_left);                    
    }   
    // ====class09结束===================================              
}


// 轮播图
jsAnimate.slide({
    id: "slide", // 字符串类型，根元素id，该属性不可省略
    time: 3, // 数字类型，轮播时间，可省略，默认为3秒换一次图片
    speed: 0.2, // 数字类型，切换速度，可省略，默认为0.3秒图片切换完毕
}, LeftClick, RightClick)


var content_img = $(".text_content img");
var content_h = $(".text_content h1");
// console.log(content_img);
// console.log(content_h);


function LeftClick(index) {
    $(content_img).removeClass();
    $(content_h).removeClass();
    $(content_img[index]).addClass("slideRight");
    $(content_h[index]).addClass("slideRight");
}

function RightClick(index) {
    $(content_img).removeClass();
    $(content_img[index]).addClass("slideLeft");
    $(content_h).removeClass();
    $(content_h[index]).addClass("slideLeft");
}