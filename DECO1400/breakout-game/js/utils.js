var log = console.log.bind(console)

// selector
var e = (selector) => document.querySelector(selector);

// load a image
const imageFromPath = (path) => {
    var img = new Image()
    img.src = path
    return img
}

// rectangles overlap
const rectIntersects = (a, b) => {
    var ah = a.image.height
    var aw = a.image.width
    if (b.y > a.y && b.y < a.y + ah) {
        if (b.x > a.x && b.x < a.x + aw) {
            return true
        }
    }
    return false
}
