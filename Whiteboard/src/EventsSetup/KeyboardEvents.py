import pyglet


def setup_keyboard_events(app):
        #------------Keyboard Setup-------------#
    @app.window.event
    def on_key_press(symbol, modifiers):
        if symbol not in app.window.keys:
            app.window.keys.append(symbol)
        
        #Go to the next page
        if symbol == pyglet.window.key.E:
            app.pages.current_index += 1
            if app.pages.current_index >= app.pages.size():
                app.pages.Push() #Insert new page
            
            print("Number of pages: {0}".format(app.pages.size()))

        #Go to previous page
        elif symbol == pyglet.window.key.Q:
            if app.pages.current_index <= 0:
                return
            if app.pages.current_page().is_empty() and app.pages.current_index == app.pages.size() - 1:
                app.pages.Pop() #Remove the last page if it's empty

            app.pages.current_index -= 1
            print("Number of pages: {0}".format(app.pages.size()))
    
    @app.window.event
    def on_key_release(symbol, modifiers):
        if symbol in app.window.keys:
            app.window.keys.remove(symbol)
    #----------Keyboard Setup End-----------#