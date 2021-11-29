

def setup_window_events(app):
    #-------------Window Drawing------------#
    @app.window.event
    def on_draw():
        app.window.clear()
        page = app.pages.current_page()
        page.camera.begin()
        page.drawer.draw()
        page.camera.end()
    #-----------Window Drawing End----------#