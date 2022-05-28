$(function() {
    var vip_nav1 = $('.vipnav'); /** 导航栏  增加导航栏的class */
    vip_nav1.addClass("navbar navbar-expand-lg");

    // $('.myClass').addClass("navbar-brand"); /**导航栏第一个链接 */

    $('.vc_button').addClass("navbar-toggler"); /** 手机端的导航栏按钮 */
    var vip_navButton = $('.vc_button');
    vip_navButton.attr({ "data-toggle": "collapse", "aria-controls": "navbarNav", "aria-expanded": "false", "aria-label": "Toggle navigation" });
    var vc_icon = '<span class="navbar-toggler-icon"></span>'
    $(".vc_button").append(vc_icon) /*按钮图标 */

    $('.vc_hide').addClass("collapse navbar-collapse"); //隐藏导航栏

    $('.vc_list').addClass("navbar-nav mr-auto"); //导航栏的ul列表

    var vip_dropdownId = $('#vc_id1'); /**下拉菜单  简化下拉菜单*/
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