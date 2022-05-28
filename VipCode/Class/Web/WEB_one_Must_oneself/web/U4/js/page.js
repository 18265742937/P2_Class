function tabpage(event) {
    var tab_id = event.target.id
    if (tab_id == "num1") {
        $(".mycontent .show div").remove()
        $(".mycontent .show").attr("id", "one");
        $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 0;bottom:0;left: 0;padding: 5px;"><img src="image/imgwall-1.jpg" style="width: 100%;"></div>')
    }
    if (tab_id == "num2") {
        $(".mycontent .show div").remove()
        $(".mycontent .show").attr("id", "two");
        $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 50%;bottom:0;left: 0;padding: 5px;"><img src="image/imgwall-2.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 0;bottom:0;left: 50%;padding: 5px;"><img src="image/imgwall-3.jpg" style="width: 100%;"></div>')
    }
    if (tab_id == "num3") {
        $(".mycontent .show div").remove()
        $(".mycontent .show").attr("id", "three");
        $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 50%;bottom:0;left: 0;padding: 5px;"><img src="image/imgwall-2.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 1%;right: 0;bottom:0;left: 50%;padding: 5px;"><img src="image/imgwall-4.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 53%;right: 0;bottom:0;left: 50%;padding: 5px;"><img src="image/imgwall-6.jpg" style="width: 100%;"></div>')
    }
    if (tab_id == "num4") {
        $(".mycontent .show div").remove()
        $(".mycontent .show").attr("id", "fore");
        $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 50%;bottom:0;left: 0;padding: 5px;"><img src="image/imgwall-2.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 1%;right: 0;bottom:0;left: 50%;padding: 5px;"><img src="image/imgwall-4.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 52%;right: 25%;bottom:0;left: 50%;padding: 5px;"><img src="image/imgwall-5.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 52%;right: 0;bottom:0;left: 75%;padding: 5px;"><img src="image/imgwall-7.jpg" style="width: 100%;"></div>')
    }
    if (tab_id == "num5") {
        $(".mycontent .show div").remove()
        $(".mycontent .show").attr("id", "five");
        $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 50%;bottom:0;left: 0;padding: 5px;"><img src="image/imgwall-2.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 25%;bottom:0;left: 50%;padding: 5px;"><img src="image/imgwall-3.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 0;bottom:0;left: 75%;padding: 5px;"><img src="image/imgwall-5.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 52%;right: 25%;bottom:0;left: 50%;padding: 5px;"><img src="image/imgwall-7.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 52%;right: 0;bottom:0;left: 75%;padding: 5px;"><img src="image/imgwall-9.jpg" style="width: 100%;"></div>')
    }
    if (tab_id == "num6") {
        $(".mycontent .show div").remove()
        $(".mycontent .show").attr("id", "six");
        $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 75%;bottom:0;left: 0;padding: 5px;"><img src="image/imgwall-2.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 50%;bottom:0;left: 25%;padding: 5px;"><img src="image/imgwall-3.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 50%;right: 50%;bottom:0;left: 0;padding: 5px;"><img src="image/imgwall-6.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 0;right: 0;bottom:0;left: 50%;padding: 5px;"><img src="image/imgwall-8.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 48%;right: 25%;bottom:0;left: 50%;padding: 5px;"><img src="image/imgwall-9.jpg" style="width: 100%;"></div>')
        $(".mycontent .show").prepend('<div style="position: absolute;top: 48%;right: 0;bottom:0;left: 75%;padding: 5px;"><img src="image/imgwall-11.jpg" style="width: 100%;"></div>')
    }
}