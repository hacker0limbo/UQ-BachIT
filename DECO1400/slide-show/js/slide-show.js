/*
1. 写一个 div 有三个 img 标签
2. 只显示当前活动的 img 标签 display:none 但是添加一个 active 显示当前的
3. 加1个按钮, 点击的时候切换图片
 */

/*
要保证三个东西是一样的:
    1. slde 里面存储的active 数据
    2. active 在 img 里面的位置
    3. red 在 indicators 里面的位置
 */

// 测试函数, 测试3个index 是否保持一致
var test = function() {
    // slide 里面存储的
    var slide = e('.slide')
    var dataActive = slide.dataset.active

    // 显示图片的 active 所在图片的位置
    var activeImg = e('.active')
    var imgId = activeImg.id
    var imgLength = imgId.length
    var activedImgId = imgId[imgLength-1]

    // 显示小圆点 red 所在 indi 的位置
    var redIndi = e('.red')
    var redIndiId = redIndi.dataset.index

    console.log(`data-active里为${dataActive}, 图片为${activedImgId}, 圆点为${redIndiId}`);
}

// 更新 slide 里面的 data-active
var updateDataInSlide = function(index) {
    var slide = e('.slide')
    slide.dataset.active = String(index)
}

// 更新图片
var updateImg = function(index) {
    var imgId = '#id-img-' + String(index)
    var className = 'active'
    removeSelfClass(className)
    var img = e(imgId)
    img.classList.add(className)
}

// 更新小圆点
var updateIndi = function(index) {
    var indiId = '#id-indi-' + String(index)
    var colorName = 'red'
    removeSelfClass(colorName)
    var indi = e(indiId)
    indi.classList.add(colorName)
}

var update = function(index) {
    updateDataInSlide(index)
    updateIndi(index)
    updateImg(index)
}

var bindEventButtons = function() {
    // 给所有 button 都绑上事件
    var selector = 'button'
    bindAll(selector, 'click', function(event){

        var slide = e('.slide')

        var target = event.target
        // 得到图片总数和当前下标
        var numberOfImgs = Number(slide.dataset.imgs)
        var activeIndex = Number(slide.dataset.active)
        var imgIndex = 0

        if (target.classList.contains('slide-button-right')) {
            // 求出下一张图片的 index (用余数)
            imgIndex = (activeIndex + 1) % numberOfImgs
        }
        else if (target.classList.contains('slide-button-left')) {
            imgIndex = (activeIndex + 2) % numberOfImgs
        }

        update(imgIndex)
        test()
    })
}

var bindEventIndicator = function() {
    var selector = '.slide-indi'
    bindAll(selector, 'mouseover', function(event){
        var target = event.target
        // 小圆点的 id 要和图片的 id 对应, mouseover 的时候找到对应的 id就是图片的 id
        // 获取小圆点的 id
        var indicatorIndex = Number(target.dataset.index)

        update(indicatorIndex)
        // 测试函数
        test()
    })
}

var play = function() {
    var slide = e('.slide')
    var numberOfImgs = Number(slide.dataset.imgs)
    var activeIndex = Number(slide.dataset.active)
    var imgIndex = (activeIndex + 1) % numberOfImgs

    update(imgIndex)
}

var autoPlay = function() {
    var interval = 3000
    var timer = setInterval(function(){
        play()
        test()
    }, interval)
}

var __mian = function() {
    autoPlay()
    bindEventButtons()
    bindEventIndicator()
    test()
}
__mian()
