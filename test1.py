from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.textinput import TextInput

from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image


import firebase_admin
from firebase_admin import credentials

# cred = credentials.Certificate("firebase_API_key.json")
# firebase_admin.initialize_app(cred)


class ChoreManagerApp(App):
    def build(self):
        return ChoreManagerInterface()
    
class ChoreManagerInterface(BoxLayout):
    def __init__(self, **kwargs):
    
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Add a text input for entering chores
        self.task_input = TextInput(hint_text="Enter new chore")
        self.add_widget(self.task_input)
        
        # Add a button to submit new chores
        add_task_button = Button(text="Add Chore")
        add_task_button.bind(on_press=self.add_task)
        self.add_widget(add_task_button)
        
        # Create a ScrollView to hold the list of chores
        self.task_scrollview = ScrollView(size_hint=(1, 1))
        self.tasks_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.tasks_layout.bind(minimum_height=self.tasks_layout.setter('height'))  # Adjust height based on content
        self.task_scrollview.add_widget(self.tasks_layout)
        
        # Add the scrollable task list to the main layout
        self.add_widget(self.task_scrollview)
    
    def add_task(self, instance):
        # Get the text from the input field
        task_text = self.task_input.text.strip()
        
        # Only add if there's input text
        if task_text:
            # Add the task as a new label in the tasks layout
            task_label = Label(text=task_text, size_hint_y=None, height=40)
            self.tasks_layout.add_widget(task_label)
            
            # Clear the input field after adding the task
            self.task_input.text = ""

#=======================================================================================================

if __name__ == '__main__':
    ChoreManagerApp().run()