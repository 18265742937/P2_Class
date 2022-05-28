function Util(cvs, ctx, margin = 60) {
    return {
        aw: cvs.width - 2 * margin,
        ah: cvs.height - 2 * margin,
        ox: margin,
        oy: cvs.height - margin,
        fillColor: (color) => {
            ctx.fillStyle = color;
        },
        // circle:(radius, ox, oy) => {
        //     // 圆形
        //     const x = ox ? ox: cvs.width/2;
        //     const y = oy ? oy : cvs.height/2;
        //     const r = radius ? radius : 50;
        //     ctx.beginPath();
        //     ctx.arc(x, y, r, 0, 2 * Math.PI);
        //     ctx.closePath();
        //     ctx.fill();
        // },
        sectorRad: (d1, d2, radius, ox, oy) => {
            // 扇形 - 弧度
            const x = ox ? ox : cvs.width / 2;
            const y = oy ? oy : cvs.height / 2;
            const r = radius ? radius : 50;
            const deg1 = d1 ? d1 : 0;
            const deg2 = d2 ? d2 : 2 * Math.PI;
            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.arc(x, y, r, deg1, deg2);
            ctx.closePath();
            ctx.fill();
        },
        circle: (radius, ox, oy, d1, d2) => {
            const x = ox ? ox : cvs.width / 2;
            const y = oy ? oy : cvs.height / 2;
            const r = radius ? radius : 50;
            const deg1 = d1 ? Math.PI / 180 * d1 : 0;
            const deg2 = d2 ? Math.PI / 180 * d2 : 2 * Math.PI;
            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.arc(x, y, r, deg1, deg2);
            ctx.closePath();
            ctx.fill();
        },
        square: (px, py, width) => {
            const x = px ? px : cvs.width / 2;
            const y = py ? py : cvs.height / 2;
            const w = width ? width : 50;
            ctx.fillRect(x, y, w, w);
        },
        rect: (px, py, width, height) => {
            const x = px ? px : cvs.width / 2;
            const y = py ? py : cvs.height / 2;
            const w = width ? width : 150;
            const h = height ? height : 50;
            ctx.fillRect(x, y, w, h);
        },
        text: (tx, ty, text) => {
            ctx.fillText(text, tx, ty);
        },
        textAlign: (val) => {
            ctx.textAlign = val;
        },
        font: (size, type) => {
            if (size && type) {
                ctx.font = size + "px " + type;
            } else {
                ctx.font = size + "px sans-serif";
            }
        },
        getP: (e) => {
            var mousePosition = {};
            e = e || window.event;
            if (e.layerX || e.layerX == 0) {
                mousePosition.x = e.layerX;
                mousePosition.y = e.layerY;
            } else if (e.offsetX || e.offsetX == 0) {
                mousePosition.x = e.offsetX;
                mousePosition.y = e.offsetY;
            }
            return mousePosition;
        },
        line: function (x1, y1, x2, y2) {
            // 保存现场
            ctx.save();
            ctx.translate(0.5, 0.5);
            ctx.beginPath();
            ctx.moveTo(x1, y1);
            ctx.lineTo(x2, y2);
            ctx.stroke();
            ctx.closePath();
            ctx.translate(-0.5, -0.5);
            // 恢复现场
            ctx.restore();
        },
        lineStyle: (width, color) => {
            ctx.lineWidth = width;
            ctx.strokeStyle = color;
        },
        vcDrawX: function (data) {
            ctx.save();
            var ox = margin;
            var oy = cvs.height - margin;
            var cWidth = cvs.width - 2 * margin;
            var wth = Math.floor(cWidth / data.length);
            ctx.textAlign = "center";
            var pxs = data.map(function (el, i) {
                var x = ox + wth * (i + 1) - wth / 2;
                var y = oy + 20;
                ctx.fillText(el, x, y);
                return x;
            });
            var tx2 = cvs.width - margin;
            var ty2 = cvs.height - margin;
            this.line(ox, oy, tx2, ty2, "black");
            ctx.restore();
            return pxs;
        },
        vcDrawY: function (data, num) {
            ctx.save();
            var ox = margin;
            var oy = cvs.height - margin;
            var tx2 = cvs.width - margin;
            var cHeight = cvs.height - 2 * margin;

            BAR_MAXVALUE = data.reduce((v1, v2) => {
                return v1 > v2 ? v1 : v2;
            }) + 20;
            var step = Math.floor(BAR_MAXVALUE / num);
            ctx.strokeStyle = "#E0E0E0";
            for (var j = 0; j < num + 1; j++) {
                var markerText = step * j;
                var px = ox - 10;
                var py = oy - (cHeight / 10 * j);
                ctx.textAlign = "right";
                ctx.fillText(markerText, px, py + 6, 20);
                if (j > 0) {
                    this.line(ox, py, tx2, py);
                }
            }
            // var tx1 = margin;
            // var ty1 = margin;    
            // u.line(ox, oy, tx1, ty1, "black");            
            ctx.restore();
            return data.map((num) => {
                return num / BAR_MAXVALUE * this.ah;
            });
        },
        vcDotX: function (data, num = 5, anotation) {
            ctx.save();
            var ox = margin;
            var oy = cvs.height - margin;
            var tx2 = cvs.width - margin;
            var ty2 = cvs.height - margin;
            this.line(ox, oy, tx2, ty2, "black");
            var cWidth = cvs.width - 2 * margin;
            ctx.strokeStyle = "#E0E0E0";
            ctx.fillStyle = "#000";
            ctx.font = "13px Arial";
            var max = Math.max(...data);
            var min = Math.min(...data);
            var step = (max - min) / num;
            var unit = cWidth / num;
            for (var i = 0; i < num + 1; i++) {
                var text = (step * i + min).toFixed(1);
                var px = ox + unit * i; // 去掉间距
                var py = oy + 20;
                ctx.textAlign = "center";
                ctx.fillText(text, px, py);
                if (i > 0) {
                    this.line(px, oy, px, margin);
                }
            }
            ctx.fillText(anotation, ox + cWidth + 30, oy + 5);
            ctx.restore(); 
            return data.map((el) => {
                return (cvs.width - 2 * margin) / (max-min) * (el - min) + ox;
            });
        },
        vcDotY: function (data, num = 5, anotation) {
            ctx.save();
            var ox = margin;
            var oy = cvs.height - margin;
            var tx1 = margin;
            var ty1 = margin;
            this.line(ox, oy, tx1, ty1, "black");
            var cWidth = cvs.width - 2 * margin;
            var cHeight = cvs.height - 2 * margin;
            var max = Math.max(...data);
            var min = Math.min(...data);
            var step = (max - min) / num;
            var STEP_HEIGHT = cHeight / num;
            ctx.strokeStyle = "#E0E0E0";
            ctx.fillStyle = "#000";
            ctx.font = "13px Arial";
            for (var j = 0; j < num + 1; j++) {
                var text = (step * j + min).toFixed(1);
                var px = ox - 10;
                var py = oy - STEP_HEIGHT * j;
                ctx.textAlign = "right";
                ctx.fillText(text, px, py + 6);
                if (j > 0) {
                    this.line(ox, py, ox + cWidth, py);
                }
            }
            ctx.fillText(anotation, margin, margin - 10);
            ctx.restore();
            return data.map((el) => {
                return oy - (cvs.height - 2 * margin) / (max-min) * (el - min) ;
            });
        },
        isInPoint: function(x, y) {
           return ctx.isPointInPath(x, y);
        },
        onMouseMove: function (draw) {
            var timer = null;
            cvs.addEventListener("mousemove", function (e) {
                var p = u.getP();
                clearTimeout(timer);
                timer = setTimeout(function () {
                    draw(p);
                }, 20);
            });
        },
        clear: function () {
            ctx.clearRect(0, 0, cvs.width, cvs.height);
        }
    }
}