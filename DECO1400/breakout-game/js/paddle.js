class Paddle extends Item {
    constructor(x, y, image) {
        super(100, 230, 'img/paddle.png')
        this.speed = 10
    }

    move(x) {
        if (x < 0) {
            x = 0
        }
        if (x > this.canvas.width - this.image.width) {
            x = this.canvas.width - this.image.width
        }
        this.x = x
    }
    moveLeft() {
        this.move(this.x - this.speed)
    }
    moveRight() {
        this.move(this.x + this.speed)
    }
    collide(ball) {
        if (ball.y + ball.image.height > this.y) {
            if (ball.x > this.x && ball.x < this.x + this.image.width) {
                return true
            }
        }
        return false
    }
}
