import random
import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5

COIN_COUNT = 50

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.player_list = None

        self.player_sprite = None

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0
        self.player = Player()

        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2

        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = arcade.AnimatedTimeSprite(scale=0.5)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            coin.textures = []
            coin.textures.append(arcade.load_texture(":resources:images/items/gold_1.png"))
            coin.textures.append(arcade.load_texture(":resources:images/items/gold_2.png"))
            coin.textures.append(arcade.load_texture(":resources:images/items/gold_3.png"))
            coin.textures.append(arcade.load_texture(":resources:images/items/gold_4.png"))
            coin.textures.append(arcade.load_texture(":resources:images/items/gold_3.png"))
            coin.textures.append(arcade.load_texture(":resources:images/items/gold_2.png"))
            coin.scale = 2
            coin.cur_texture_index = random.randrange(len(coin.textures))

            self.coin_list.append(coin)

    def on_draw(self):

        arcade.start_render()

        self.coin_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


    def on_update(self, delta_time):

        self.coin_list.update()
        self.coin_list.update_animation()
        self.player_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)

        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


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


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

main()