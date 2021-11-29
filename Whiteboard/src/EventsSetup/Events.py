from .KeyboardEvents import setup_keyboard_events
from .MouseEvents import setup_mouse_events
from .TabletEvents import setup_tablet_events
from .WindowEvents import setup_window_events

def setup_events(app):
    setup_keyboard_events(app)
    setup_mouse_events(app)
    setup_tablet_events(app)
    setup_window_events(app)