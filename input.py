from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

all_expenses = []

class Input(Screen):
    def submit_expense(self):
        self.expense = self.expense_input.text
        print("Logged expense as " + self.expense +"\n")
        self.save_expense()
    def save_expense(self):
        all_expenses.append(float(self.expense))
