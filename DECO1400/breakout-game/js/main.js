var __main = function() {
    var game = Game(30)

    var paddle = new Paddle()
    var ball = new Ball()

    var blocks = []
    var leftBlocks = 3

    for (let i = 0; i < 3; i++) {
        let block = new Block()
        // set block's coordinate
        block.x = i * 100
        block.y = i * 30
        blocks.push(block)
    }

    var paused = false
    game.registerAction('a', () => {
        paddle.moveLeft()
    })
    game.registerAction('d', () => {
        paddle.moveRight()
    })
    game.registerAction('f', () => {
        ball.fire()
    })
    // press p to pause the game
    window.addEventListener('keydown', (event) => {
        if (event.key == 'p') {
            paused = !paused
        }
    })

    game.update = () => {
        if (paused) {
            return
        }
        ball.move()
        // decide ball collide with padlle
        if (paddle.collide(ball)) {
            console.log('ball collide with paddle');
            ball.bound()
        }
        // decide ball collide with block
        for (let i = 0; i < blocks.length; i++) {
            let block = blocks[i]
            if (leftBlocks == 0) {
                // pause game
                paused = !paused
                // show the ending
                showContent()
            }
            if (block.collide(ball)) {
                console.log('ball collide with block')
                // block disappear
                block.kill()
                // ball bound
                ball.bound()
                leftBlocks--
            }
        }
    }
    game.draw = () => {
        // draw
        game.drawImage(paddle)
        game.drawImage(ball)

        for (let i = 0; i < blocks.length; i++) {
            let block = blocks[i]
            if (block.alive) {
                game.drawImage(block)
            }
        }
    }

}
__main()
