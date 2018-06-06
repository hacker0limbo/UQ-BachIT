class Item {
    constructor(x, y, image) {
        var canvas = document.querySelector('#id-canvas')
        var context = canvas.getContext('2d')

        this.canvas = canvas
        this.context = context
        this.image = imageFromPath(image)
        this.x = x
        this.y = y
        this.w = image.width
        this.h = image.height
    }
}
