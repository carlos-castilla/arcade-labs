import arcade

screen_width = 800
screen_height = 600

class Ball:
    def __init__(self, pos_x, pos_y, radio, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radio, self.color)


class MyGame (arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height,title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        self.ball = Ball (50,50,15, arcade.color.ORANGE_RED)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.pos_x = x
        self.ball.pos_y = y



def main():
    window  = MyGame (640, 480, "Drawing Example")
    arcade.run()

main()