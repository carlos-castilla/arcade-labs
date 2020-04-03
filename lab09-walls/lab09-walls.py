
import random
import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen "

VIEWPORT_MARGIN = 400

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.4)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        for x in range(200, 1650, 210):
            for y in range(0, 1000, 64):

                if random.randrange(5) > 0:
                    if random.randrange(5) > 0:
                        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                        wall.center_x = x
                        wall.center_y = y
                        self.wall_list.append(wall)
                    else:
                        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING + 0.5)
                        wall.center_x = x
                        wall.center_y = y
                        self.wall_list.append(wall)




        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        arcade.set_background_color(arcade.color.AMAZON)

        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):

        arcade.start_render()

        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        self.physics_engine.update()

        changed = False

        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

main()
