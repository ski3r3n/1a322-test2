def on_button_pressed_a():
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        # # . # #
        # # . # #
        """)
    basic.clear_screen()
    basic.show_leds("""
        # . # . .
        # . # . #
        . # . # .
        . . . . #
        . . . # .
        """)
    basic.clear_screen()
    if randint(0, 2) == 0:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            # # . # #
            # # . # #
            """)
        basic.clear_screen()
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            """)
    elif randint(0, 1) == 0:
        basic.show_leds("""
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            . # # # .
            """)
        basic.clear_screen()
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            """)
    else:
        basic.show_leds("""
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            """)
        basic.clear_screen()
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        """)
    basic.clear_screen()
    basic.show_leds("""
        # . # . .
        # . # . #
        . # . # .
        . . . . #
        . . . # .
        """)
    basic.clear_screen()
    if randint(0, 2) == 0:
        basic.show_leds("""
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            """)
        basic.clear_screen()
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            """)
    elif randint(0, 1) == 0:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            # # . # #
            # # . # #
            """)
        basic.clear_screen()
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            """)
    else:
        basic.show_leds("""
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            . # # # .
            """)
        basic.clear_screen()
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . # # # .
        # # # # #
        # # # # #
        # # # # #
        . # # # .
        """)
    basic.clear_screen()
    basic.show_leds("""
        # . # . .
        # . # . #
        . # . # .
        . . . . #
        . . . # .
        """)
    basic.clear_screen()
    if randint(0, 2) == 0:
        basic.show_leds("""
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            . # # # .
            """)
        basic.clear_screen()
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            """)
    elif randint(0, 1) == 0:
        basic.show_leds("""
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            """)
        basic.clear_screen()
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            """)
    else:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            # # . # #
            # # . # #
            """)
        basic.clear_screen()
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_leds("""
        . # # # .
        # # # # #
        # # # # #
        # # # # #
        . # # # .
        """)
    basic.show_leds("""
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        """)
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        # # . # #
        # # . # #
        """)
    basic.show_leds("""
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        """)
    basic.show_leds("""
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        """)
    basic.show_leds("""
        . # # # .
        . . . . #
        # . . # .
        . . # . .
        . # # # #
        """)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
