var EventUtil = {
    //添加事件处理函数
    addHandler: function(element, type, handler) {
        if (element.addEventListener) {
            element.addEventListener(type, handler, false);
        } else if (element.attachEvent) {
            element.attachEvent("on" + type, handler);
        } else {
            element["on" + type] = handler;
        }
    },

    //删除事件处理函数
    removeHandler: function(element, type, handler) {
        if (element.removeEventListener) {
            element.removeEventListener(type, handler, false);
        } else if (element.detachEvent) {
            element.detachEvent("on" + type, handler);
        } else {
            element["on" + type] = null;
        }
    },

    //获取事件
    getEvent: function(event) {
        return event ? event : window.event;
    },

    //获取事件目标
    getTarget: function(event) {
        return event.target || event.srcElement;
    },

    //取消默认行为
    preventDefault: function(event) {
        if (event.preventDefault) {
            event.preventDefault();
        } else {
            event.returnValue = false;
        }
    },

    //取消冒泡
    stopPropagation: function(event) {
        if (event.stopPropagation) {
            event.stopPropagation();
        } else {
            event.cancelBubble = true;
        }
    }
}

//类操作
function addClass(elem, classN) {
    if (elem.className == "") {
        elem.className = classN;
    } else if (elem.className.match(new RegExp("(\\s|^)" + classN + "(\\s|$)"))) {
        elem.className = elem.className;
    } else {
        elem.className += " " + classN;
    }
}

function removeClass(elem, classN) {
    if (elem.className.match(new RegExp("(\\s|^)" + classN + "(\\s|$)")))
        elem.className = elem.className.replace(new RegExp("(\\s|^)" + classN + "(\\s|$)"), " ");
}
var classArr = ["phoA", "phoB", "phoC", "phoD", "phoE", "phoF"];
var albumWrapper = document.querySelector('#wrapper');
var maskParent = document.querySelector(".background");
var nav = document.getElementsByTagName("nav")[0] //查看大图时，隐藏nav
var photos = document.querySelectorAll(".photos");

function turnToPhoto(i) {
    var degOld = albumWrapper.style.transform;
    var degNew;

    //利用字符串得到当前角度并转换为int型
    if (degOld == '') {
        degOld = 30 + '';
    } else {
        var begin = degOld.indexOf('rotateX(') + 8;
        var end = degOld.indexOf('deg', begin);
        degOld = degOld.substring(begin, end);
    }
    degOld = parseInt(degOld);

    //利用当前角度得到当前照片序号
    var indexNow = (degOld % 360 - 30) / 60;
    indexNow = indexNow < 0 ? indexNow + 6 : indexNow;

    //利用当前照片序号以及目标序号确定翻页的角度
    if (i < indexNow - 2) {
        if (indexNow == 4) {
            degNew = degOld + 60 * 2;
        } else if (indexNow == 5) {
            degNew = degOld + (i == 1 ? 2 * 60 : 60);
        }
    } else if (i > indexNow + 2) {
        if (indexNow == 1) {
            degNew = degOld - 60 * 2;
        } else if (indexNow == 0) {
            degNew = degOld - (i == 4 ? 2 * 60 : 60);
        }
    } else {
        degNew = degOld + (i - indexNow) * 60;
    }

    //翻页
    albumWrapper.style.transform = "rotateX(" + degNew + "deg)";
}

function showPhoto(i) {
    if (document.querySelector(".picMask")) {
        maskParent.removeChild(maskParent.querySelector(".picMask"));
        picMask = null;
        document.querySelector("." + classArr[i]).focus();
        return;
    }
    var picMask = document.createElement("div");
    picMask.className = "picMask";
    var pic = document.createElement("div");
    pic.className = "pic";
    pic.style.backgroundColor = "white";
    picMask.appendChild(pic);
    maskParent.appendChild(picMask);
    EventUtil.addHandler(picMask, "click", function(event) {
        maskParent.removeChild(picMask);
        picMask = null;
        document.querySelector("." + classArr[i]).focus();
    });
}

for (var i = 0; i < photos.length; i++) {
    photos[i].tabIndex = -1;
    (function(i) {
        EventUtil.addHandler(photos[i], 'focus', function(event) {
            turnToPhoto(i);
            photos[i].style.outline = "none";
            addClass(photos[i], "focus");
        });
        EventUtil.addHandler(photos[i], 'blur', function(event) {
            removeClass(photos[i], "focus");
        });
        EventUtil.addHandler(photos[i], 'keydown', function(event) {
            if (event.keyCode == 13) {
                showPhoto(i)
            }
            if (event.keyCode == 38) {
                //在蒙板时 去掉蒙板再转换相册
                if (document.querySelector(".picMask")) {
                    maskParent.removeChild(maskParent.querySelector(".picMask"));
                    picMask = null;
                    document.querySelector("." + classArr[i]).focus();
                }
                if (i - 1 < 0) {
                    photos[5].focus();
                } else {
                    photos[i - 1].focus();
                }
            }
            if (event.keyCode == 40) {
                //在蒙板时 去掉蒙板再转换相册
                if (document.querySelector(".picMask")) {
                    maskParent.removeChild(maskParent.querySelector(".picMask"));
                    picMask = null;
                    document.querySelector("." + classArr[i]).focus();
                }
                if (i + 1 > 5) {
                    photos[0].focus();
                } else {
                    photos[i + 1].focus();
                }
            }
        });
    })(i)
}
