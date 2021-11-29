from Drawer import Drawer


class Page:
    def __init__(self):
        self.drawer = Drawer()

    def get_drawer(self):
        return self.drawer

    def draw(self):
        self.drawer.draw()
    
    def is_empty(self):
        if self.drawer.get_data() is not None:
            return len(self.drawer.get_data().vertices) == 0
        return True


class PageStack:
    def __init__(self):
        self.stack = [Page()]
        self.current_index = 0

    def Push(self):
        self.stack.append(Page())

    def Pop(self, index = None):
        if index is None:
            index = len(self.stack) - 1
        self.stack.pop(index)

    def get_current_page(self):
        return self.stack[self.current_index]
    
    def get_size(self):
        return len(self.stack)