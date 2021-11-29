import copy

class Rectangle():
    colors = ('black', 'grey', 'red')

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        if color:
            self.color = color
        else:
            self.color = self.__class__.colors[0]
        self.__class__.colors = self.__class__.colors[1:]

    def click_left(self):
        # some common actions for all rectangle objects
        pass

    def click_right(self):
        # some common actions for all rectangle objects
        pass

    def clone(self, color=None, move_right=True, move_down=False):
        clone_object = copy.deepcopy(self)
        if color:
            clone_object.color = color
        if move_right:
            clone_object.x =+1
        if move_down:
            clone_object.y -=1
        return clone_object

    def clone_right(self):
        clone_object = copy.deepcopy(self)
        clone_object.x += 1
        clone_object.color = self.__class__.colors[0]
        self.__class__.colors = self.__class__.colors[1:]
        return clone_object


def show(obj):
    print(obj.x, obj.y, obj.color)

black = Rectangle(0, 2, 'black')
grey = black
grey.color = 'grey'

# ....

for rect in (black, grey, red):
    show(rect)