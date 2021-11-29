from Point import Point


def setup_mouse_events(app):
    #---------------Mouse Setup-------------#
    @app.window.event
    def on_mouse_press(x, y, button, modifiers):
        if button not in app.window.mouse_buttons:
            app.window.mouse_buttons.append(button)

    @app.window.event
    def on_mouse_release(x, y, button, modifiers):
        if button in app.window.mouse_buttons:
            app.window.mouse_buttons.remove(button)

    @app.window.event
    def on_mouse_motion(x, y, dx, dy):
        app.window.mouse_position = Point(x, y)

    @app.window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        app.window.mouse_position = Point(x, y)
    #-------------Mouse Setup End-----------#