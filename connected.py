from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from datetime import datetime
from kivy.uix.dropdown import DropDown

class CDropDown(DropDown):
    pass

class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def getMonth(self):
        return datetime.now().strftime('%B')

    def getTotalSpent(self):
        return "$2398.00" #rewrite this later lol
#
# class CButton(Button):
#     def exp_or_collapse(self, box):
#         if box.height == self.height:
#             # expand
#             for child in box.children:
#                 child.height = 40
#                 child.opacity = 1
#         else:
#             # collapse
#             for child in box.children:
#                 if child != self:
#                     child.height = 0
#                     child.opacity = 0
