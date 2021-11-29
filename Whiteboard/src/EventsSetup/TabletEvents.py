import pyglet


def setup_tablet_events(app):
    #--------------Tablet Input-------------#
    tablets = pyglet.input.get_tablets()

    if len(tablets) > 0:
        tablet = tablets[0]
        tablet = tablet.open(app.window)

        @tablet.event
        def on_motion(cursor, x, y, pressure, a, b):
            if pressure > 0:
                buttons = app.window.mouse_buttons

                from pyglet.window import mouse
                if mouse.LEFT not in buttons:
                    buttons.append(mouse.LEFT)
    #------------Tablet Input End-----------#