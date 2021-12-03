import pyglet


def setup_window_events(app):
    #-------------Window Drawing------------#
    @app.window.event
    def on_draw():
        app.window.clear()

        r, g, b, a = app.window.background_color.get_rgba()
        pyglet.gl.glClearColor(r, g, b, a)

        app.draw()

        page = app.pages.current_page()
        page.camera.begin()

        page.drawer.draw()

        page.camera.end()
    #-----------Window Drawing End----------#