class Block extends Item {
    constructor(x, y, image) {
        super(100, 100, 'img/block.png')
        this.alive = true
    }

    kill() {
        this.alive = false
    }
    collide(b) {
        return this.alive && (rectIntersects(this, b) || rectIntersects(b, this))
    }
}
