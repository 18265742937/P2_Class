!function(e){var t={};function n(o){if(t[o])return t[o].exports;var i=t[o]={i:o,l:!1,exports:{}};return e[o].call(i.exports,i,i.exports,n),i.l=!0,i.exports}n.m=e,n.c=t,n.d=function(e,t,o){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:o})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var o=Object.create(null);if(n.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var i in e)n.d(o,i,function(t){return e[t]}.bind(null,i));return o},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=1)}([function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.caculateWidth=function(e){var t;t=getComputedStyle?parseFloat(getComputedStyle(e,null).width):parseFloat(e.currentStyle.width);return t},t.eventListener=function(e,t,n,o){window.addEventListener?e.addEventListener(t,n,o):e.attachEvent("on"+t,n)},t.getClientHeight=function(){var e=0;if(document.body.clientHeight&&document.documentElement.clientHeight)var e=document.body.clientHeight<document.documentElement.clientHeight?document.body.clientHeight:document.documentElement.clientHeight;else var e=document.body.clientHeight>document.documentElement.clientHeight?document.body.clientHeight:document.documentElement.clientHeight;return e},t.objectInterface=function(e,t){if("[object Object]"===Object.prototype.toString.call(e)&&"[object Object]"===Object.prototype.toString.call(t)){var n="";if(Object.keys(t).forEach(function(o){var i=t[o];Object.prototype.toString.call(e[o])!=="[object "+i+"]"&&(n+=o+"-"+i+" ")}),n)throw new TypeError("the param of slide don't have correct-type-property: "+n);return!0}throw new TypeError("the param of objectInterface is not object")}},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=n(0),i=n(2),r=l(n(3)),a=l(n(4)),s=l(n(5));function l(e){return e&&e.__esModule?e:{default:e}}t.default=window.jsAnimate=function(){function e(e){return function(t,n){if(3!==arguments.length)if(1!==arguments.length||"[object Object]"!==Object.prototype.toString.call(arguments[0])){if(!Array.isArray(t))throw new Error(t+" is not array");if("[object Object]"!==Object.prototype.toString.call(n))throw new Error(n+" is not object");t.forEach(function(t){e(Object.assign({id:t},n))})}else e(arguments[0]);else e(arguments[0],arguments[1],arguments[2])}}return(0,o.eventListener)(window,"load",r.default),{show:i.show,hide:i.hide,returnTop:i.returnTop,slide:e(a.default),slick:e(s.default)}}()},function(e,t,n){"use strict";var o,i;Object.defineProperty(t,"__esModule",{value:!0}),t.show=function(e,t){if("string"!=typeof e)throw new TypeError("the id of hide is not string");if("number"!=typeof t)throw new TypeError("the time of hide is not number");if(node=document.getElementById(e),"1"===node.style.opacity)return;clearTimeout(o);var n=node.style.opacity||0,i=10,r=1/(1e3*t/i);n=parseFloat(n),node.style.display="block",function e(){node.style.opacity=n;n+=r;if(n<1)o=setTimeout(function(){e()},i);else if(n>=1)return void setTimeout(function(){node.style.opacity=1},i)}()},t.hide=function(e,t){if("string"!=typeof e)throw new TypeError("the id of hide is not string");if("number"!=typeof t)throw new TypeError("the time of hide is not number");if(node=document.getElementById(e),"0"===node.style.opacity)return;clearTimeout(o);var n=node.style.opacity||1,i=10,r=1/(1e3*t/i);n=parseFloat(n),function e(){node.style.opacity=n;n-=r;if(n>0)o=setTimeout(function(){e()},i);else if(n<=0)return void setTimeout(function(){node.style.opacity=0,node.style.display="none"},i)}()},t.returnTop=function(e){if("number"!=typeof e)throw new Error("the param of returnTop is not number");clearTimeout(i);var t=document.documentElement.scrollTop||window.pageYOffset||document.body.scrollTop||0;if(t>0){var n=10,o=t/(1e3*e/n);document.documentElement.scrollTop?r(document.documentElement,"scrollTop"):window.pageYOffset?r(window,"pageYOffset"):document.body.scrollTop&&r(document.body,"scrollTop")}function r(e,a){if(e[a]=t,(t-=o)>0)i=setTimeout(function(){r(e,a)},n);else if(t<=0)return void setTimeout(function(){e[a]=0},n)}}},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=function(){var e,t,n=[];e=document.getElementsByClassName("lazyfade"),t=(0,o.getClientHeight)();for(var i=0;i<e.length;i++){var r,a,s;e[i].classList.contains("zoomin")&&(e[i].style.opacity=0,e[i].style.transform="scale(0, 0)",e[i].style.webkitTransform="scale(0, 0)",s="zoomin",a=a||void 0),e[i].classList.contains("zoomin-r")&&(e[i].style.opacity=0,e[i].style.transform="scale(0, 0)",e[i].style.webkitTransform="scale(0, 0)",s="zoomin-r",a=!0),e[i].classList.contains("fadein-left")&&(e[i].style.opacity=0,e[i].style.transform+=" translate3d(-200px, 0, 0)",r="left",a=a||void 0),e[i].classList.contains("fadein-right")&&(e[i].style.opacity=0,e[i].style.transform+=" translate3d(200px, 0, 0)",r="right",a=a||void 0),e[i].classList.contains("fadein-top")&&(e[i].style.opacity=0,e[i].style.transform+=" translate3d(0, -200px, 0)",r="top",a=a||void 0),e[i].classList.contains("fadein-bottom")&&(e[i].style.opacity=0,e[i].style.transform+=" translate3d(0, 200px, 0)",r="bottom",a=a||void 0),e[i].classList.contains("fadein-left-r")&&(e[i].style.opacity=0,e[i].style.transform+=" translate3d(-200px, 0, 0)",r="left",a=!0),e[i].classList.contains("fadein-right-r")&&(e[i].style.opacity=0,e[i].style.transform+=" translate3d(200px, 0, 0)",r="right",a=!0),e[i].classList.contains("fadein-top-r")&&(e[i].style.opacity=0,e[i].style.transform+=" translate3d(0, -200px, 0)",r="top",a=!0),e[i].classList.contains("fadein-bottom-r")&&(e[i].style.opacity=0,e[i].style.transform+=" translate3d(0, 200px, 0)",r="bottom",a=!0),e[i].classList.contains("lazyfade-r")&&(e[i].style.opacity=0,r="fade",a=!0);var l,d,c={node:e[i],offsetTop:e[i].getBoundingClientRect().top,direction:r,zoom:s,hasFadeIn:void 0,hasFadeOut:!0,duration:{},reverse:a};if(l=e[i].getAttribute("duration")){var u,f,p=l.trim(),y=/^\{\s*(\w+)\s*:\s*(cubic-bezier\([^\)]+\)|[^\s][^,\}]*)/i,h=/^,\s*(\w+)\s*:\s*(cubic-bezier\([^\)]+\)|[^\s][^,\}]*)/i;for(y.test(p)&&(u=RegExp.$1,f=RegExp.$2.trim(),c.duration[u]=f,p=p.replace(y,""));h.test(p);)u=RegExp.$1,f=RegExp.$2.trim(),c.duration[u]=f,p=p.replace(h,"")}(d=e[i].getAttribute("transition-enter"))&&(c.transitionEnter=d,e[i].style.cssText+=";"+d),n.push(c),a=void 0,s=void 0}var m=function(){var e,o,i=/^(\d+)$/i;function r(e){var t,o=0;if(e.delay&&(o=e.delay),!e.delay&&e.duration&&e.duration.follow){var i=e.duration.follow,r="";if(!/^follow(.*)$/i.test(i))throw new Error("the attribute of element should be follow + ...");r=RegExp.$1,n.forEach(function(n,i){if(n.duration.target&&n.duration.target==="target"+r){if(t)throw new Error("redeclaration of target");if(t=i,n.delay)o=parseFloat(n.delay)+(parseFloat(n.duration.enter)||1e3);else if(o=s(n),e.duration.animation){var a=(parseFloat(getComputedStyle(e.node,null).getPropertyValue("animation-duration"))||0)+(parseFloat(getComputedStyle(e.node,null).getPropertyValue("animation-delay"))||0);o=parseFloat(o)+a}e.delay=o}else;}),o&&(e.node.style.transitionDelay=o+"ms")}if(e.duration&&e.duration.animation){var l;if(e.node.parentNode.getAttribute("sign"))l=e.node.parentNode;else{var d=e.node.parentNode;(l=document.createElement("div")).setAttribute("sign",!0),l.style.display="inline-block",l.style.opacity=e.node.style.opacity,l.style.transform=e.node.style.transform,l.style.transition=e.node.style.transition,o&&(l.style.transitionDelay=o+"ms"),e.node.style.opacity="",e.node.style.transform="",e.node.style.transition="",e.node.style.transitionDelay="",d.insertBefore(l,e.node),l.appendChild(e.node)}var c=e.duration.animation,u=c.split(" ");if(a(e.node,u),e.duration.type){var f=e.duration.type;switch(f){case"transition":e.node.offsetHeight;l.style.opacity=1,l.style.transform="scale(1, 1) translate3d(0, 0, 0)",l.style.webkitTransform="scale(1, 1) translate3d(0, 0, 0)",setTimeout(function(){e.node.className+=" "+c},o||s(e));break;case"animation":l.style.opacity=1;e.node.offsetHeight;e.node.className+=" "+c,setTimeout(function(){l.style.transform="scale(1, 1) translate3d(0, 0, 0)",l.style.webkitTransform="scale(1, 1) translate3d(0, 0, 0)",a(e.node,u)},o||s(e))}return}e.node.offsetHeight;return l.style.opacity=1,l.style.transform="scale(1, 1) translate3d(0, 0, 0)",l.style.webkitTransform="scale(1, 1) translate3d(0, 0, 0)",void(e.node.className+=" "+c)}e.node.offsetHeight;e.node.style.transform="scale(1, 1) translate3d(0, 0, 0)",e.node.style.webkitTransform="scale(1, 1) translate3d(0, 0, 0)",e.node.style.opacity=1}function a(e,t){t.forEach(function(t){e.classList.remove(t)})}function s(e){var t,n;return e.duration&&e.duration.enter&&i.test(e.duration.enter)?t=parseFloat(e.duration.enter):e.duration&&e.duration.enter&&(t=/^\d+\.?\d*\w$/g.test(e.duration.enter)?1e3*parseFloat(e.duration.enter):parseFloat(e.duration.enter)),e.duration&&e.duration.delay&&i.test(e.duration.delay)?n=parseFloat(e.duration.delay):e.duration&&e.duration.delay&&(n=/^\d+\.?\d*\w$/g.test(e.duration.delay)?1e3*parseFloat(e.duration.delay):parseFloat(e.duration.delay)),(t||1e3)+(n||0)}return n.forEach(function(t){if(t.node.style.transition||t.duration.enter||(t.node.style.transition="all 1s ease"),t.duration&&(t.duration.enter||t.duration.bezier||t.duration.delay)&&(t.duration.enter&&(e=i.test(t.duration.enter)?t.duration.enter+"ms":t.duration.enter,t.node.style.transition="all "+e+" ease"),t.duration.bezier&&(t.node.style.transitionTimingFunction=t.duration.bezier),t.duration.delay)){var n=t.duration.delay;n=n.trim(),i.test(n)?t.node.style.transitionDelay=RegExp.$1+"ms":t.node.style.transitionDelay=n}}),function(){n.forEach(function(e){if(!e.hasFadeIn)if(e.offsetTop=e.node.getBoundingClientRect().top,e.reverse){if(e.offsetTop<=t/10*9&&e.offsetTop>=t/8){if(!e.hasFadeOut)return;e.hasFadeIn=!0,e.hasFadeOut=!1;var n=s(e);r(e),setTimeout(function(){e.hasFadeIn=!1},n)}else if(e.offsetTop<t/8||e.offsetTop>t/10*9){if(e.hasFadeOut)return;e.hasFadeOut=!0,e.duration&&e.duration.leave&&(e.duration.leave=e.duration.leave.trim(),o=i.test(e.duration.leave)?e.duration.leave+"ms":e.duration.leave,e.node.style.transitionDuration=o),function(e,t,n){e.delay&&(e.node.style.transitionDelay=void 0+"ms");var o="",i="";switch(t){case"left":o=" translate3d(-200px, 0, 0)";break;case"right":o=" translate3d(200px, 0, 0)";break;case"top":o=" translate3d(0, -200px, 0)";break;case"bottom":o=" translate3d(0, 200px, 0)"}if(n)switch(n){case"zoomin-r":i="scale(0, 0)"}if(e.duration&&e.duration.animation){var r=e.duration.animation,l=r.split(" "),d=e.node.parentNode;if(!e.duration.type)return a(e.node,l),d.style.opacity=0,d.style.transform=i+o,e.node.offsetHeight,void(e.node.className+=" "+r);var c=e.duration.type;switch(c){case"transition":a(e.node,l),e.node.offsetHeight,e.node.className+=" "+r,setTimeout(function(){d.style.transform=i+o,d.style.opacity=0},s(e));break;case"animation":d.style.transform=i+o,setTimeout(function(){e.node.className+=" "+r,d.style.opacity=0},s(e))}}else e.node.style.transform=i+o,e.node.style.opacity=0}(e,e.direction,e.zoom)}}else if(e.offsetTop<=t&&e.offsetTop>=0)return e.hasFadeIn=!0,void r(e)})}}();(0,o.eventListener)(window,"scroll",m),(0,o.eventListener)(window,"scroll",function e(){window.removeEventListener("scroll",m);window.removeEventListener("scroll",e);setTimeout(function(){(0,o.eventListener)(window,"scroll",m),(0,o.eventListener)(window,"scroll",e)},20)}),m()};var o=n(0)},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=function(e,t,n){var i,r,a,s,l,d;(0,o.objectInterface)(e,{id:"String"}),i=document.getElementById(e.id),r=e.time||3,a=e.speed||.3,s=e.noArrow,l=e.noBottom,d=e.noAutoSlide,i.style.width="100%",i.style.position="relative",i.style.overflow="hidden";var c=i.children,u=c.length;if(1===u)return;var f,p,y,h,m,v=1,g=10,b=document.createDocumentFragment(),w=document.createElement("div");w.style.cssText="white-space:nowrap;overflow:hidden;",b.appendChild(w);var x=c[u-1].cloneNode(!0);x.style.display="inline-block",x.style.width="100%";var L=c[0].cloneNode(!0);L.style.display="inline-block",L.style.width="100%",w.appendChild(x);for(;f=c[0];)w.appendChild(f),f.style.display="inline-block",f.style.width="100%";if(w.appendChild(L),!l){var T=document.createElement("div");T.style.cssText="position:absolute;left:0;bottom:30px;width:100%;height:8px;text-align:center;";for(var E=0;E<u;E++){var k=document.createElement("span");k.style.cssText="display:inline-block;margin:0 12px;width:50px;height:100%;border-radius:20px;background:#fff;opacity:0.7;cursor:pointer;",T.appendChild(k)}(0,o.eventListener)(T,"click",function(e){if(m)return;var t,n=(e=e||window.event).target;if("SPAN"!==n.nodeName)return;p=getComputedStyle?parseFloat(getComputedStyle(i,null).width):parseFloat(i.currentStyle.width);for(var o=n.parentNode.children,r=0;r<o.length;r++)if(o[r]===n){t=r;break}if(v===++t)return;z(t),v=t}),w.appendChild(T)}if(!s){var C=document.createElement("span"),j=document.createElement("span");C.style.cssText="position:absolute;left:30px;top:50%;margin-top:-35px;width:60px;height:70px;line-height:70px;text-align:center;background:transparent;opacity:0;font-size:50px;color:#eee;transform:scaleY(2);cursor:pointer;transition:all 0.3s ease;",j.style.cssText="position:absolute;right:30px;top:50%;margin-top:-35px;width:60px;height:70px;line-height:70px;text-align:center;background:transparent;opacity:0;font-size:50px;color:#eee;transform:scaleY(2);cursor:pointer;transition:all 0.3s ease;",C.innerHTML="<",j.innerHTML=">",O(C,j),(0,o.eventListener)(i,"mouseover",function(){C.style.opacity=1,j.style.opacity=1}),(0,o.eventListener)(i,"mouseleave",function(){C.style.opacity=0,j.style.opacity=0}),(0,o.eventListener)(C,"mouseover",function(){C.style.backgroundColor="rgba(180, 180, 180, 0.1)"}),(0,o.eventListener)(C,"mouseleave",function(){C.style.backgroundColor="transparent"}),(0,o.eventListener)(j,"mouseover",function(){j.style.backgroundColor="rgba(180, 180, 180, 0.1)"}),(0,o.eventListener)(j,"mouseleave",function(){j.style.backgroundColor="transparent"}),(0,o.eventListener)(C,"click",function(e){e=e||window.event,S("left")}),(0,o.eventListener)(j,"click",function(e){e=e||window.event,S("right")}),w.appendChild(C),w.appendChild(j)}function F(){if(!d)return h=setInterval(function(){H()},1e3*r)}function O(e,t){if(!s){var n,r,a,l,d=(0,o.caculateWidth)(i);n=30/1903*d,r=60/1903*d,a=70/1903*d,l=50/1903*d,e.style.left=n+"px",e.style.marginTop=-a/2+"px",e.style.width=r+"px",e.style.height=a+"px",e.style.lineHeight=a+"px",e.style.fontSize=l+"px",t.style.right=n+"px",t.style.marginTop=-a/2+"px",t.style.width=r+"px",t.style.height=a+"px",t.style.lineHeight=a+"px",t.style.fontSize=l+"px"}}function S(e){if(!m)switch(m=!0,e){case"left":z(--v),t&&t(v);break;case"right":default:H()}}function H(){z(++v),n&&n(v)}function z(e){clearTimeout(y),e===u+1?v=1:0===e&&(v=u),I(e);var t=p*e,n=w.scrollLeft,o=Math.abs(t-n),i=o/(1e3*a/g);function r(e,n){y=setTimeout(function(){if(w.scrollLeft+=e,!n&&w.scrollLeft>t)r(e,n);else{if(!(n&&w.scrollLeft<t))return w.scrollLeft=t,w.scrollLeft=p*v,void(m=void 0);r(e,n)}},g)}t<n?r(-i):t>n&&r(i,!0)}function I(e){if(!l){e=(e=--e>u-1?0:e)<0?u-1:e;for(var t=0;t<T.children.length;t++)e===t?(T.children[t].style.backgroundColor="#25b8fd",T.children[t].style.opacity=1):(T.children[t].style.backgroundColor="#fff",T.children[t].style.opacity=.7)}}return(0,o.eventListener)(i,"mouseover",function(){clearInterval(h)}),(0,o.eventListener)(i,"mouseleave",function(){h=F()}),i.appendChild(b),I(v),(0,o.eventListener)(window,"load",function(){p=(0,o.caculateWidth)(i),w.scrollLeft=p}),(0,o.eventListener)(window,"resize",function(){p=(0,o.caculateWidth)(i),w.scrollLeft=p*v,O(C,j)}),F(),i};var o=n(0)},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=function(e){var t,n,i,r,a,s,l,d,c,u;(0,o.objectInterface)(e,{id:"String"}),t=document.getElementById(e.id),n=e.speed||.3,a=e.quick,s=e.row,l=e.imgScale,d=e.autoSlide,u=e.intervalTime||2e3,i=e.number||5,r=e.height||120;var f,p,y,h,m=10,v=0;t.style.cssText="position:relative;margin:0;padding:0 45px;overflow:hidden;height:"+r+"px;";var g=document.createDocumentFragment(),b=document.createElement("div");b.style.overflow="hidden",b.style.width="100%",b.style.height="100%",b.style.whiteSpace="noWrap";for(var w=document.createElement("ul"),x=t.children,L=x.length,T=0;T<L;T++){var E=document.createElement("li");E.appendChild(x[0]),w.appendChild(E)}if(w.style.cssText="margin:0;padding:0;display:inline-block;white-space:nowrap;height:100%;list-style:none;",L<=i)w.style.display="flex",w.style.flexFlow="row nowrap",w.style.justifyContent="center",w.style.alignItems="center";else{var k=w.cloneNode(!0),C=w.cloneNode(!0);b.appendChild(k),b.appendChild(w),b.appendChild(C)}b.appendChild(w);var j=document.createElement("span"),F=document.createElement("span");j.style.cssText="position:absolute;left:5px;top:50%;margin-top:-15px;width:30px;height:30px;line-height:30px;text-align:center;border-radius:50%;background:#eeeeee;transition:all 0.8s ease-out;cursor:pointer;color:rgb(70, 70, 70);",F.style.cssText="position:absolute;right:5px;top:50%;margin-top:-15px;width:30px;height:30px;line-height:30px;text-align:center;border-radius:50%;background:#eeeeee;transition:all 0.8s ease-out;cursor:pointer;color:rgb(70, 70, 70);";var O=document.createElement("span");O.innerHTML="<",O.style.cssText="display: inline-block;width: 100%;height: 100%;transform: scaleY(1.7);";var S,H,z=document.createElement("span");z.innerHTML=">",z.style.cssText="display: inline-block;width: 100%;height: 100%;transform: scaleY(1.7);",j.appendChild(O),F.appendChild(z),(0,o.eventListener)(j,"mouseover",function(){this.style.color="white",this.style.backgroundColor="#3057d8",this.style.boxShadow="0 0 4px 4px #bcc5f3"}),(0,o.eventListener)(j,"mouseleave",function(){this.style.color="rgb(70, 70, 70)",this.style.backgroundColor="#eeeeee",this.style.boxShadow=""}),(0,o.eventListener)(F,"mouseover",function(){this.style.color="white",this.style.backgroundColor="#3057d8",this.style.boxShadow="0 0 4px 4px #bcc5f3"}),(0,o.eventListener)(F,"mouseleave",function(){this.style.color="rgb(70, 70, 70)",this.style.backgroundColor="#eeeeee",this.style.boxShadow=""}),(0,o.eventListener)(j,"click",function(){L>i&&M("left")}),(0,o.eventListener)(F,"click",function(){L>i&&M("right")}),g.appendChild(b),g.appendChild(j),g.appendChild(F),t.appendChild(g),(0,o.eventListener)(window,"resize",function(){I(S=(0,o.caculateWidth)(b))}),S=(0,o.caculateWidth)(b),f=(H=S/i-20)/r,I(S),d&&(_(),(0,o.eventListener)(t,"mouseover",function(){clearInterval(c)}),(0,o.eventListener)(t,"mouseleave",function(){_()}));function I(e){r=(H=e/i-20)/f,t.style.height=r+"px";for(var n=0;n<b.children.length;n++)for(var a=b.children,d=0;d<a[n].children.length;d++){a[n].children[d].style.cssText="display:inline-block;margin:0 10px;vertical-align:top;width:"+H+"px;height:100%;text-align:center;background:#eeeeee;box-sizing:border-box;cursor:pointer;overflow:hidden;";var c=a[n].children[d].firstChild;c.style.display="flex",c.style.flexFlow=s&&"column"!==s?"row nowrap":"column nowrap",c.style.justifyContent="space-between",c.style.alignItems="center",c.style.height="100%";for(var u=0;u<c.children.length;u++)l&&"IMG"===c.children[u].nodeName&&((0,o.eventListener)(c.children[u],"mouseover",function(e){var t=(e=e||window.event).target;t.style.transform="scale(1.2, 1.2)"}),(0,o.eventListener)(c.children[u],"mouseleave",function(e){var t=(e=e||window.event).target;t.style.transform="scale(1, 1)"})),c.children[u].style.transition="all 0.4s ease-out",c.children[u].style.maxWidth="100%",c.children[u].style.flex="0 1 auto"}h=(0,o.caculateWidth)(w),L>i&&(b.scrollLeft=h+e/i*v)}function _(){c=setInterval(function(){L>i&&M("right")},u)}function M(e){if(!p)switch(p=!0,e){case"left":!function(){var e=-1;a?(v-=i,e*=i):v--;N(e)}();break;case"right":!function(){var e=1;a?(v+=i,e*=i):v++;N(e)}()}}function N(e){clearTimeout(y);var t=b.scrollLeft,o=t+S/i*e;o=o<1?0:o,a&&(v>=L?(v-=L,t=b.scrollLeft-=h):v<=-L&&(v+=L,t=b.scrollLeft+=h),o=h+S/i*v);var r=Math.abs(o-t),s=r/(1e3*n/m);function l(e,t){y=setTimeout(function(){if(b.scrollLeft+=e,!t&&b.scrollLeft>o)b.scrollLeft+e<0&&(e=0-b.scrollLeft),l(e,t);else{if(!(t&&b.scrollLeft<o))return b.scrollLeft=o,b.scrollLeft=o,a||Math.abs(v)!==L||(b.scrollLeft=h,v=0),void(p=void 0);b.scrollLeft+e>2*h&&(e=2*h-b.scrollLeft),l(e,t)}},m)}o<t?l(-s):o>t&&l(s,!0)}return t};var o=n(0)}]);