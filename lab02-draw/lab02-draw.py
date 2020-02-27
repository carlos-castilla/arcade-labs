import arcade

arcade.open_window(800, 600, "Drawing Example")

#Cielo
arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

arcade.start_render()


#--Suelo--#
arcade.draw_lrtb_rectangle_filled(0,800,100,0, arcade.color.SLATE_GRAY)

#--Coche--#
arcade.draw_triangle_filled(350,190,800,120,800,300,[255,255,0])

arcade.draw_lrtb_rectangle_filled(50,400,225,130, arcade.color.RED)

arcade.draw_arc_filled(410,190,50,55,arcade.color.BLACK,90,270)

arcade.draw_lrtb_rectangle_filled(50,300,300,150, arcade.color.RED)


arcade.draw_arc_filled(125,127,100,110,arcade.color.DARK_RED,0,180)
arcade.draw_arc_filled(320,127,100,110,arcade.color.DARK_RED,0,180)

arcade.draw_lrtb_rectangle_filled(190,300,290,226, arcade.color.BLUE_BELL)
arcade.draw_lrtb_rectangle_filled(70,180,290,226, arcade.color.BLUE_BELL)

arcade.draw_circle_filled(125,137,37,arcade.color.BLACK)
arcade.draw_circle_filled(125,137,20,arcade.color.ASH_GREY)
arcade.draw_circle_filled(320,137,37,arcade.color.BLACK)
arcade.draw_circle_filled(320,137,20,arcade.color.ASH_GREY)

#Luna
arcade.draw_circle_filled(800,600,180,arcade.color.WHITE_SMOKE)





arcade.finish_render()
arcade.run()
