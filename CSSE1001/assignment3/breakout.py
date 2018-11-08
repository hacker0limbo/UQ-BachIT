import tkinter as tk
from tkinter import messagebox


class Paddle:
    """
    A class to generate a paddle object in the canvas
    """
    def __init__(self, canvas):
        """
        Construct a new paddle in the shape of rectangle

        Parameters:
            canvas: The canvas to draw paddle
        """
        self._canvas = canvas
        self.x = 150
        self.y = 250
        self.w = 80
        self.h = 20
        self.speed = 30

        self.draw_image()

    def draw_image(self):
        """
        Draw paddle in the canvas
        """
        coords = (
            self.x,
            self.y,
            self.x + self.w,
            self.y + self.h,
        )
        self._img = self._canvas.create_rectangle(coords, fill='blue')

    def move_left(self):
        """
        Decrease paddle's x coord, and limit it inside canvas width
        """
        if self.x <= 0:
            self.x = self.speed
        self.x -= self.speed

    def move_right(self):
        """
        Decrease paddle's y coord, and limit it inside canvas height
        """
        if self.x + self.w >= self._canvas.WIDTH:
            self.x = self._canvas.WIDTH - self.w - self.speed
        self.x += self.speed

    def clear(self):
        """
        Delete paddle from canvas
        """
        self._canvas.delete(self._img)


class Ball:
    """
    A class to generate a ball object in the canvas
    """
    def __init__(self, canvas):
        """
        Construct a ball in the shape of circle

        Parameter:
            canvas: canvas to draw ball
        """
        self._canvas = canvas
        self.x = 170
        self.y = 220
        self.radius = 5
        self.w = 2*self.radius
        self.h = 2*self.radius
        self.speed_x = 10
        self.speed_y = 10

        self.fired = False
        self.draw_image()

    def fire(self):
        """
        Fire the ball to make ball move
        """
        self.fired = True

    def move(self):
        """
        Make keep moving and bouncing in the canvas
        """
        if self.fired:
            if self.x < 0 or self.x > self._canvas.WIDTH:
                self.speed_x *= -1
            if self.y < 0 or self.y > self._canvas.HEIGHT:
                self.speed_y *= -1

            self.x += self.speed_x
            self.y += self.speed_y

    def draw_image(self):
        """
        Draw ball image in the canvas
        """
        coords = (
            self.x,
            self.y,
            self.x + 2*self.radius,
            self.y + 2*self.radius,
        )
        self._img = self._canvas.create_oval(coords, fill="black", width=0)

    def clear(self):
        """
        Clear ball in the canvas
        """
        self._canvas.delete(self._img)

    def collide(self):
        """
        Determine if the ball collide with other object in the canvas

        Return:
            (bool) True if collide, False not collide
        """
        return len(self._canvas.find_overlapping(self.x, self.y, self.x+2*self.radius, self.y+2*self.radius)) > 0

    def bound(self):
        """
        Make ball bound when hit an object
        """
        self.speed_y *= -1

    def die(self):
        """
        Determine if the ball fall into the ground

        Return:
            (bool) True if ball hit canvas's ground, False is not
        """
        return self.y+2*self.radius >= self._canvas.HEIGHT


class Block:
    """
    A class to generate a block object in the canvas
    """
    def __init__(self, canvas, x, y):
        """
        Construct a new block based on given x coord and y coord

        Parameters:
            canvas: canvas to draw block image
            x (int): x coord
            y (int): y coord
        """
        self._canvas = canvas
        self.x = x
        self.y = y
        self.w = 25
        self.h = 15
        self.alive = True

        self.draw_image()

    def draw_image(self):
        """
        Draw a new block in the canvas
        """
        coords = (
            self.x,
            self.y,
            self.x + self.w,
            self.y + self.h,
        )
        self._img = self._canvas.create_rectangle(coords, fill='yellow')

    def kill(self):
        """
        make block disappear in the canvas
        """
        self.alive = False

    def react_intersects(self, rect1, rect2):
        """
        Determine if two rectangles collide

        Parameters:
            rect1 (widget): the first canvas widget
            rect1 (widget): the second canvas widget
        """
        return (rect2.x + rect2.w >= rect1.x) \
               and (rect1.x + rect1.w >= rect2.x) \
               and (rect1.y <= rect2.y + rect2.h) \
               and (rect1.h + rect1.y >= rect2.y)

    def collide(self, o):
        """
        Return:
            (bool) whether another widget collide with this block
        """
        return (self.react_intersects(o, self) or self.react_intersects(self, o)) and self.alive

    def clear(self):
        """
        Clear block in the canvas
        """
        self._canvas.delete(self._img)


class Game(tk.Canvas):
    """
    A class to set a canvas for the game
    """
    WIDTH = 400
    HEIGHT = 300

    def __init__(self, master):
        """
        Construct a new game canvas

        Parameter:
            master (widget) master of the canvas
        """
        super().__init__(master, width=self.WIDTH, height=self.HEIGHT)
        self._master = master


class GameApp(tk.Frame):
    """
    A class to initialize the game App
    """
    BLOCKS_NUM = 5

    def __init__(self, master):
        """
        Construct a game app

        Parameter:
            master (widget) master of the Game
        """
        super().__init__(master)
        self._master = master
        self.game = Game(master)
        self.game.pack(expand=True, fill=tk.BOTH)
        self.ball = Ball(self.game)
        self.paddle = Paddle(self.game)

        self.blocks = []
        for index in range(self.BLOCKS_NUM):
            block = Block(self.game, (index+1)*60, 60)
            self.blocks.append(block)

        self.win = False
        self.lose = False

        self._master.bind('<Key>', self.callback)

        self.update_all()

    def check_end(self):
        """
        Check if the game is end, and do related action if the game is end

        Return:
            (bool) True means game is end, False is not
        """
        if self.win:
            self.win_message()
            return True
        elif self.lose:
            self.lose_message()
            return True
        return False

    def win_message(self):
        """
        Show the win message
        """
        messagebox.showinfo('victory', 'You Win!')

    def lose_message(self):
        """
        Show the lose message
        """
        messagebox.showwarning('Fail', 'You Lose..')

    def check_win_game(self):
        """
        Check if the user win the game
        """
        for block in self.blocks:
            if block.alive:
                return
        self.win = True

    def check_lose_game(self):
        """
        Check if the user lose the game
        """
        if self.ball.die():
            self.lose = True

    def callback(self, event):
        """
        Different actions will be performed when user press different keys

        Parameters:
            event: the event when user press a key
        """
        key = str(event.char)
        if key == 'a':
            self.paddle.move_left()
        if key == 'd':
            self.paddle.move_right()
        if key == 'f':
            self.ball.fire()

    def update_all(self):
        """
        Update all the information in the canvas, clear shapes and redraw the shapes again
        """
        # check game end
        self.check_win_game()
        self.check_lose_game()
        if self.check_end():
            return
        # check collide
        self.check_all()
        # clear
        self.clear_all()
        # draw
        self.draw_all()
        self._master.after(50, self.update_all)

    def check_all(self):
        """
        Check if the ball hit any block or paddle, and perform related actions
        """
        self.ball.move()
        if self.ball.collide():
            self.ball.bound()
        for block in self.blocks:
            if block.collide(self.ball):
                block.kill()

    def clear_all(self):
        """
        Clear all the shaped on the canvas
        """
        self.ball.clear()
        self.paddle.clear()
        for block in self.blocks:
            block.clear()

    def draw_all(self):
        """
        Redraw all the shape on the canvas
        """
        self.ball.draw_image()
        self.paddle.draw_image()
        for block in self.blocks:
            if block.alive:
                block.draw_image()
