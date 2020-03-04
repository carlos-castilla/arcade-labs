import arcade

arcade.open_window(800, 600, "Drawing Example")

# Cielo
arcade.set_background_color(arcade.color.DARK_BLUE)

def iniciar():
    arcade.draw_triangle_filled(350 , 190, 800, 120, 800, 300, [255, 255, 0])

    arcade.draw_lrtb_rectangle_filled(50, 400, 225, 130, arcade.color.RED)

    arcade.draw_arc_filled(410, 190, 50, 55, arcade.color.ASH_GREY, 90, 270)

    arcade.draw_lrtb_rectangle_filled(50 , 300 , 300, 150, arcade.color.RED)

    arcade.draw_arc_filled(125 , 127, 100, 110, arcade.color.DARK_RED, 0, 180)
    arcade.draw_arc_filled(320 , 127, 100, 110, arcade.color.DARK_RED, 0, 180)

    arcade.draw_lrtb_rectangle_filled(190 , 300 , 290, 226, arcade.color.BLUE_BELL)
    arcade.draw_lrtb_rectangle_filled(70, 180 , 290, 226, arcade.color.BLUE_BELL)

    arcade.draw_circle_filled(125 , 137, 37, arcade.color.BLACK)
    arcade.draw_circle_filled(125 , 137, 20, arcade.color.ASH_GREY)
    arcade.draw_circle_filled(320 , 137, 37, arcade.color.BLACK)
    arcade.draw_circle_filled(320 , 137, 20, arcade.color.ASH_GREY)

################################################################################
def coche(x):
    #--Coche--#
    arcade.draw_triangle_filled(350+x,190,800+x,120,800+x,300,[255,255,0])

    arcade.draw_lrtb_rectangle_filled(50+x,400+x,225,130, arcade.color.RED)

    arcade.draw_arc_filled(410+x,190,50,55,arcade.color.ASH_GREY,90,270)

    arcade.draw_lrtb_rectangle_filled(50+x,300+x,300,150, arcade.color.RED)


    arcade.draw_arc_filled(125+x,127,100,110,arcade.color.DARK_RED,0,180)
    arcade.draw_arc_filled(320+x,127,100,110,arcade.color.DARK_RED,0,180)

    arcade.draw_lrtb_rectangle_filled(190+x,300+x,290,226, arcade.color.BLUE_BELL)
    arcade.draw_lrtb_rectangle_filled(70+x,180+x,290,226, arcade.color.BLUE_BELL)

    arcade.draw_circle_filled(125+x,137,37,arcade.color.BLACK)
    arcade.draw_circle_filled(125+x,137,20,arcade.color.ASH_GREY)
    arcade.draw_circle_filled(320+x,137,37,arcade.color.BLACK)
    arcade.draw_circle_filled(320+x,137,20,arcade.color.ASH_GREY)

################################################################################
def luna(x):

    #Luna
    arcade.draw_circle_filled(800-x,600,180,arcade.color.WHITE_SMOKE)


def iniciarluna():
    arcade.draw_circle_filled(980,600,180,arcade.color.WHITE_SMOKE)


################################################################################
def on_draw(delta_time):

    arcade.start_render()

    #--Suelo--#
    arcade.draw_lrtb_rectangle_filled(0,800,100,0, arcade.color.SLATE_GRAY)


    luna(on_draw.luna_x)
<<<<<<< HEAD
    on_draw.luna_x +=5

    coche(on_draw.coche_x)
    on_draw.coche_x += 10

    if on_draw.coche_x>800:
        iniciar()
        on_draw.coche_x=-820

    if on_draw.luna_x>880:
        iniciarluna()
        on_draw.luna_x=-300
=======
    on_draw.luna_x +=1

    coche(on_draw.coche_x)
    on_draw.coche_x += 1

    if on_draw.coche_x>800:
        iniciar()
        on_draw.coche_x=1







>>>>>>> 63e6b196c565f60e5f5ee286491906eaf39ad9b4

on_draw.coche_x=1
on_draw.luna_x=1


################################################################################

def main():

    arcade.schedule(on_draw, 1 / 60)

    arcade.finish_render()
    arcade.run()

main()
