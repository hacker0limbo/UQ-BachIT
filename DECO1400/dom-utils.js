// var log = () => {
//     console.log.apply(console, arguments)
// }

var e = (selector) => {
    return document.querySelector(selector)
}

var es = (selector) => {
    return document.querySelectorAll(selector)
}

var appendHtml = (element, html) => {
	element.insertAdjacentHTML('beforeend', html)
}

var bindEvent = (element, eventName, callback) => {
    element.addEventListener(eventName, callback)
}

var addClass = (element, className) => {
    element.classList.add(className)
}

var removeClass = (element, className) => {
    element.classList.remove(className)
}

//
var removeSelfClass = function(className) {
    var selector = '.' + className
    var element = e(selector)
    element.classList.remove(className)
}

// 通过类名删除所有含有这个类的元素的类
var removeselfClassAll = function(className) {
    var selector = '.' + className
    var elements = document.querySelectorAll(selector)
    for (var i = 0; i < elements.length; i++) {
        var e = elements[i]
        e.classList.remove(className)
    }
}


var toggleClass = (element, className) => {
    if (element.classList.contains(className)) {
        removeClass(element, className)
    } else {
        addClass(element, className)
    }
}

var removeClassAll = (className) => {
    var selector = '.' + className
    var elements = document.querySelectorAll(selector)
    for (var i = 0; i < elements.length; i++) {
        var e = elements[i]
        e.classList.remove(className)
    }
}

var clearActive = (selector) => {
    var s = document.querySelector(selector)
    if (s != null) {
        s.classList.remove(selector)
    }
}

var bindAll = (selector, eventName, callback) => {
    var elements = document.querySelectorAll(selector)
    for(var i = 0; i < elements.length; i++) {
        var e = elements[i]
        bindEvent(e, eventName, callback)
    }
}

// find() could find all the children of element
var find = (element, selector) => {
    return element.querySelector(selector)
}


// animation
var tooglePlayAnimation = (element) => {
    if (count % 2 == 0) {
        element.style.webkitAnimationPlayState = "paused"
    } else {
        element.style.webkitAnimationPlayState = "running"
    }
    count++
}

// src
var getRelativeSrc = (element) => {
    var src = element.getAttribute("src")
    return src
}

var toogleSrc = (element, src1, src2) => {
    // use getAttribute to get the relative path
    var src = getRelativeSrc(element)
    if (src == src1) {
        element.src = src2
    } else {
        element.src = src1
    }
}
