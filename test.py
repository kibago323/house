from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivy.uix.gridlayout import GridLayout

Window.size = (300, 500)

main_helper = """
#:import NoTransition kivy.uix.screenmanager.NoTransition

ScreenManager:
    transition: NoTransition()
    LoginScreen:
    MainScreen:
    InputScreen:
    BuyList:
    SettingScreen:

<CustButton@Button>:
    font_size: 32

<CalcGridLayout>:
    id: calculator
    display: entry
    rows: 6
    padding: 10
    spacing: 10



    # Where input is displayed
    BoxLayout:
        TextInput:
            id: entry
            font_size: 32
            multiline: False

    # When buttons are pressed update the entry
    BoxLayout:
        spacing: 10
        CustButton:
            text: "7"
            on_press: entry.text += self.text
        CustButton:
            text: "8"
            on_press: entry.text += self.text
        CustButton:
            text: "9"
            on_press: entry.text += self.text
        CustButton:
            text: "+"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "4"
            on_press: entry.text += self.text
        CustButton:
            text: "5"
            on_press: entry.text += self.text
        CustButton:
            text: "6"
            on_press: entry.text += self.text
        CustButton:
            text: "-"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "1"
            on_press: entry.text += self.text
        CustButton:
            text: "2"
            on_press: entry.text += self.text
        CustButton:
            text: "3"
            on_press: entry.text += self.text
        CustButton:
            text: "*"
            on_press: entry.text += self.text

    # When equals is pressed pass text in the entry
    # to the calculate function
    BoxLayout:
        spacing: 10
        CustButton:
            text: "AC"
            on_press: entry.text = ""
        CustButton:
            text: "0"
            on_press: entry.text += self.text
        CustButton:
            text: "="
            on_press: calculator.calculate(entry.text)
        CustButton:
            text: "/"
            on_press: entry.text += self.text

<LoginScreen>:
    name: 'login_screen'
    canvas.before:

        Rectangle:
            source: 'logo.jpg'
            pos: (50, 375)
            size: (200, 150)

        Rectangle:
            source: 'Avatar_morgan.png'
            pos: (50, 330)
            size: (100, 100)

        Rectangle:
            source: 'Avatar_bella.png'
            pos: (150, 330)
            size: (100, 100)

        Rectangle:
            source: 'Avatar_kaise.png'
            pos: (90, 190)
            size: (100, 100)

        Rectangle:
            source: 'Avatar_bella.png'
            pos: (190, 190)
            size: (100, 100)

        Color:
            rgba: 55/255, 102/255, 76/255, 0.3
        Rectangle:
            pos: self.pos
            size: self.size


    BoxLayout:
        id: login_layout
        orientation: 'vertical'
        padding: [10,50,10,50]
        spacing: 10
        pos: (0, -40)

        BoxLayout:
            orientation: 'vertical'

            MDLabel:
                text: 'Login'
                font_size: 18
                halign: 'left'
                text_size: root.width-20, 20

            TextInput:
                id: login
                size_hint: (1, .7)
                multiline:False
                font_size: 28

        BoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: 'Password'
                halign: 'left'
                font_size: 18
                text_size: root.width-20, 20

            TextInput:
                size_hint: (1, .7)
                id: password
                multiline:False
                password:True
                font_size: 28

        Button:
            text: 'Login'
            font_size: 24
            size: (300, 50)
            on_press: app.change_to_main()



<MainScreen>:
    name: 'main_screen'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            left_action_items: [["menu", lambda x: app.change_to_settings()]]
            canvas:
                Rectangle:
                    source: 'logo.jpg'
                    pos: ((85, self.pos[1]-20))
                    size: (150, 100)

        MDLabel:
            text: 'MAIN'
            halign: 'center'

        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["calculator", lambda x: app.change_to_input()], ["account-cash", lambda x: app.change_to_buylist()]]
                mode: 'end'
                type: 'bottom'
                elevation: -5
                on_action_button: app.navigation_draw()
                icon: 'icon.png'

<InputScreen>:
    name: 'input_screen'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            left_action_items: [["menu", lambda x: app.change_to_settings()]]
            canvas:
                Rectangle:
                    source: 'logo.jpg'
                    pos: ((85, self.pos[1]-20))
                    size: (150, 100)

        CalcGridLayout:

        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["calculator", lambda x: app.change_to_input()], ["account-cash", lambda x: app.change_to_buylist()]]
                mode: 'end'
                type: 'bottom'
                elevation: -5
                on_action_button: app.change_to_main()
                icon: 'icon.png'

<BuyList>:
    name: 'buylist'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            left_action_items: [["menu", lambda x: app.change_to_settings()]]
            canvas:
                Rectangle:
                    source: 'logo.jpg'
                    pos: ((85, self.pos[1]-20))
                    size: (150, 100)
        MDLabel:
            text: "BUYLIST"
            halign: 'center'

        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["calculator", lambda x: app.change_to_input()], ["account-cash", lambda x: app.change_to_buylist()]]
                mode: 'end'
                type: 'bottom'
                elevation: -5
                on_action_button: app.change_to_main()
                icon: 'icon.png'


<SettingScreen>:
    name: 'setting_screen'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            left_action_items: [["menu", lambda x: app.change_to_settings()]]
            canvas:
                Rectangle:
                    source: 'logo.jpg'
                    pos: ((85, self.pos[1]-20))
                    size: (150, 100)
        MDLabel:
            text: "SETTINGS"
            halign: 'center'

        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["calculator", lambda x: app.change_to_input()], ["account-cash", lambda x: app.change_to_buylist()]]
                mode: 'end'
                type: 'bottom'
                elevation: -5
                on_action_button: app.change_to_main()
                icon: 'icon.png'

"""

class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class InputScreen(Screen):
    pass

class BuyList(Screen):
    pass

class SettingScreen(Screen):
    pass

class CalcGridLayout(GridLayout):
    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class DemoApp(MDApp):

    username = StringProperty(None)
    password = StringProperty(None)


    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.sm = Builder.load_string(main_helper)
        self.sm.current = "login_screen"
        return self.sm


    def navigation_draw(self):
        print("Navigation")

    def change_to_input(self):
        self.sm.current = "input_screen"

    def change_to_main(self):
        self.sm.current = "main_screen"

    def change_to_buylist(self):
        self.sm.current = "buylist"

    def change_to_settings(self):
        self.sm.current = "setting_screen"

if __name__ == '__main__':
    DemoApp().run()
