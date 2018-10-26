var game = new Phaser.Game(800, 600, Phaser.CANVAS, 'convict-game', {
    preload: preload,
    create: create,
    update: update
});

function preload() {

    game.load.image('phaser', 'assets/ship.png');
    game.load.spritesheet('sea', 'assets/sea.png', 32, 32);

}

var sprite;
var group;
var cursors;
var left = 10;
var leftText;


function draw(name, index) {
    for (var j = 0; j < 10; j++) {
        var c = group.create(game.rnd.integerInRange(10, 700), game.rnd.integerInRange(0, 570), name, index);
        c.body.immovable = true;
    }
}


function create() {

    game.world.setBounds(0, 0, 500, 300);
    game.physics.startSystem(Phaser.Physics.ARCADE);

    game.stage.backgroundColor = '#b4eeb4';

    sprite = game.add.sprite(700, 0, 'phaser');

    game.physics.arcade.sortDirection = Phaser.Physics.Arcade.RIGHT_LEFT;

    game.physics.arcade.enable(sprite);

    group = game.add.physicsGroup(Phaser.Physics.ARCADE);

    // for (var i = 0; i < 50; i++) {
    //     var c = group.create(game.rnd.integerInRange(10, 700), game.rnd.integerInRange(0, 570), 'sea', game.rnd.integerInRange(0, 5));
    //     // c.name = 'veg' + i;
    //     c.body.immovable = true;
    // }

    // for (var j = 0; j < 10; j++) {
    //     //  Here we'll create some chillis which the player can pick-up. They are still part of the same Group.
    //     var c = group.create(game.rnd.integerInRange(10, 700), game.rnd.integerInRange(0, 570), 'sea', 6);
    //     c.body.immovable = true;
    // }

    for (var i = 0; i < 8; i++) {
        draw('sea', i)
    }

    game.camera.follow(sprite);

    cursors = game.input.keyboard.createCursorKeys();

    leftText = game.add.text(16, 16, 'island: 10', { fontSize: '28px', fill: '#000' })
}

function update() {

    game.physics.arcade.collide(sprite, group, collisionHandler, null, this);

    sprite.body.velocity.x = 0;
    sprite.body.velocity.y = 0;

    if (cursors.left.isDown) {
        sprite.body.velocity.x = -200;
    } else if (cursors.right.isDown) {
        sprite.body.velocity.x = 200;
    }

    if (cursors.up.isDown) {
        sprite.body.velocity.y = -200;
    } else if (cursors.down.isDown) {
        sprite.body.velocity.y = 200;
    }

}

function collisionHandler(player, veg) {

    //  If the player collides with the chillis then they get eaten :)
    //  The chilli frame ID is 17

    if (veg.frame === 6) {
        veg.kill();
        left--
        leftText.text = 'island: ' + left
    }

}