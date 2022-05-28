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

    // var vip_link1 = $('.vclink1'); //封装“主页”点击链接，默认是主页，高亮显示的
    // vip_link1.addClass("nav-link active");
    // vip_link1.attr({ "data-toggle": "tab", "role": "tab", "aria-selected": "true" });
    // 以上和vip_link2合并

    var vip_link2 = $('.vclink'); //封装“日志”点击链接，默认是主页，这里无特殊效果，默认aria-selected为false
    vip_link2.addClass("nav-link"); //不加active ，没有特殊显示
    vip_link2.attr({ "data-toggle": "pill", "role": "tab", "aria-selected": "false" });

    var vip_tabPane = $('.vc_pane'); //封装跳转栏的class
    vip_tabPane.addClass("tab-pane fade");
    vip_tabPane.attr({ "role": "tabpanel" });

    var vip_navflex = $('.vc_flex');
    vip_navflex.addClass("nav flex-column nav-pills");
    vip_navflex.attr({ "role": "tablist", "aria-orientation": "vertical" });





    //判断浏览器的宽度
    var width = $(window).width()
    if (width > 768) {
        $(".g_rotation").css("height", "462px");

    } else {
        $(".g_rotation").css("height", "350px");
        $(".center_list>img").css({ "width": "250px", "margin-left": "8%" })
    }


    // 动态改变标签页中的样式
    var content = $(".mycontent")
    var show_content = '<div style="position:relative;height: 480px;" class="vc_pane show active">'
    content.prepend(show_content)
    $(".mycontent .show").attr("id", "one");
    $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 0;bottom:0;left: 0;padding: 5px;"><img src="image/imgwall-1.jpg" style="width: 100%;"></div>')

    $(".template li a").click(tabpage);

});


//表情
function setEmoji(tag, position) {
    if (position && typeof position != "string") {
        alert("position 需为字符串类型");
    }
    tag.emojioneArea({
        pickerPosition: position || 'top',
        // hidePickerOnBlur: false,
        events: {
            click: function(textarea) {
                textarea.attr({
                    "data-toggle": "collapse",
                    "data-target": "#vc_post"
                });
            }
        }
    });
}


// 获取input标签的图片路径
function getPath(id) {
    var filePath = URL.createObjectURL($('#' + id)[0].files[0]);
    return filePath; 
}