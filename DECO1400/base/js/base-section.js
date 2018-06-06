
/*
**
section bottom
    animation - pig moving
 */
var pigImg = find(e('.pig-logo'), 'img')

pigImg.addEventListener('mouseenter', (event) => {
    var target = event.target
    target.style.webkitAnimationPlayState = "paused"
})

pigImg.addEventListener('mouseleave', (event) => {
    var target = event.target
    target.style.webkitAnimationPlayState = "running"
})

pigImg.addEventListener('animationiteration', (event) => {
    var moveLeftSrc = '../base/img/pig-walking.gif'
    var moveRightSrc = '../base/img/pig-walking-mirror.gif'
    var target = event.target

    toogleSrc(target, moveLeftSrc, moveRightSrc)
})
