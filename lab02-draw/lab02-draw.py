import arcade

arcade.open_window(800, 600, "Drawing Example")

# Cielo
arcade.set_background_color(arcade.color.DARK_BLUE)

################################################################################
def coche(x):
    #--Coche--#
    arcade.draw_triangle_filled(350+x,190,800,120,800,300,[255,255,0])

    arcade.draw_lrtb_rectangle_filled(50+x,400,225,130, arcade.color.RED)

    arcade.draw_arc_filled(410+x,190,50,55,arcade.color.ASH_GREY,90,270)

    arcade.draw_lrtb_rectangle_filled(50+x,300,300,150, arcade.color.RED)


    arcade.draw_arc_filled(125+x,127,100,110,arcade.color.DARK_RED,0,180)
    arcade.draw_arc_filled(320+x,127,100,110,arcade.color.DARK_RED,0,180)

    arcade.draw_lrtb_rectangle_filled(190+x,300,290,226, arcade.color.BLUE_BELL)
    arcade.draw_lrtb_rectangle_filled(70+x,180,290,226, arcade.color.BLUE_BELL)

    arcade.draw_circle_filled(125+x,137,37,arcade.color.BLACK)
    arcade.draw_circle_filled(125+x,137,20,arcade.color.ASH_GREY)
    arcade.draw_circle_filled(320+x,137,37,arcade.color.BLACK)
    arcade.draw_circle_filled(320+x,137,20,arcade.color.ASH_GREY)

################################################################################
def on_draw(tiempo):

    arcade.start_render()

    #--Suelo--#
    arcade.draw_lrtb_rectangle_filled(0,800,100,0, arcade.color.SLATE_GRAY)

    x_coche=1

    coche(x_coche)
    coche(0)
    x_coche+=50

################################################################################

def main():



    #Luna
    arcade.draw_circle_filled(800,600,180,arcade.color.WHITE_SMOKE)

    arcade.schedule(on_draw, 1 / 60)

    arcade.finish_render()
    arcade.run()

main()
