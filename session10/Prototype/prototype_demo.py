"""
Specify the kinds of objects to create using a prototypical instance,
and create new objects by copying this prototype.
"""

import copy


class Prototype:
    """
    Example class to be copied.
    """
    pass

    def __init__(self):
        self.border_color = ""

    def green_clone(self):
        """last Object state will be copied"""
        green_obj = copy.deepcopy(self)
        green_obj.border_color = "green"
        green_obj.btn_color = "green"
        green_obj.red_btn = "green"
        return green_obj

    def clone(self):
        """last Object state will be copied"""
        return copy.deepcopy(self)

    def refresh(self):
        # reload data
        # show data
        print(self)


def main():
    html_page = Prototype()
    html_page.refresh()
    prototype_copy_green = html_page.green_clone()
    prototype_copy_red = html_page.red_clone()
    prototype_copy_red.refresh()


if __name__ == "__main__":
    main()
