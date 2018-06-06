class Ball extends Item {
    constructor(x, y, image) {
        super(100, 200, 'img/ball.png')
        this.speedX = 5
        this.speedY = 5
        this.fired = false
    }

    fire() {
        this.fired = true
    }
    move() {
        if (this.fired) {
            if (this.x < 0 || this.x + this.image.width > this.canvas.width) {
                this.speedX *= -1
            }
            if (this.y < 0 || this.y + this.image.height > this.canvas.height) {
                this.speedY *= -1
            }
            // move
            this.x += this.speedX
            this.y += this.speedY
        }
    }
    bound() {
        this.speedY *= -1
    }
}
