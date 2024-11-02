from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock

import firebase_admin
from firebase_admin import credentials, firestore

class ChoreManagerApp(App):
    def build(self):
        return ChoreManagerInterface()
    
class ChoreManagerInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Start with an empty layout
        self.currentState = "None"
        self.currentStateSet = False

        # Create the buttons to switch states
        self.create_initial_buttons()

    def create_initial_buttons(self):
        
        # Add the heading
        heading_label = Label(text='Welcome to Chore Manager', font_size='25sp', size_hint=(1, None), height=50)
        self.add_widget(heading_label)  # Add heading to the main layout

        # Create a horizontal layout for the buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=60, spacing=10)

        btn_sign_up = Button(text='Sign Up', size_hint=(.5, 1))
        btn_sign_up.bind(on_press=self.ChangeToSignUp)
        
        btn_sign_in = Button(text='Sign In', size_hint=(.5, 1))
        btn_sign_in.bind(on_press=self.ChangeToSignIn)

        # Add the buttons to the button layout
        button_layout.add_widget(btn_sign_up)
        button_layout.add_widget(btn_sign_in)

        # Add the button layout to the main layout
        self.add_widget(button_layout)

    # Method to change to the Sign Up state
    def ChangeToSignUp(self, button):
        self.currentState = "SignUp"
        self.currentStateSet = False
        self.clear_widgets()
        self.displaySignUp()

    # Method to change to the Sign In state
    def ChangeToSignIn(self, button):
        self.currentState = "SignIn"
        self.currentStateSet = False
        self.clear_widgets()
        self.displaySignIn()

    # Displaying the Sign Up Page
    def displaySignUp(self):
        self.clear_widgets()  # Clear existing widgets
        self.spacing = 10

        # Create a layout to center the inputs and button
        center_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, None), height=300)
        center_layout.padding = [460, 20, 20, 500]  # Add padding around the layout

        # Add the heading
        heading_label = Label(text='Sign Up', font_size='25sp', size_hint=(1, None), height=50)
        heading_label.bind(size=heading_label.setter('text_size'))  # Ensure text is wrapped
        center_layout.padding = [460, 20, 20, 500]  # Add padding around the layout
        center_layout.add_widget(heading_label)


        # Userame input
        name_input = TextInput(hint_text='Enter your username', size_hint=(0.6, None), height=50)
        center_layout.add_widget(name_input)

        # Password input
        password_input = TextInput(hint_text='Enter your password', size_hint=(0.6, None), height=50)
        center_layout.add_widget(password_input)

        # Button for Sign Up
        btn1 = Button(text='Sign Up', size_hint=(0.6, None), height=60)  # Set size explicitly
        btn1.bind(on_press=lambda x: self.sign_up(name_input.text, password_input.text))  # Bind to sign-up logic
        center_layout.add_widget(btn1)

        self.add_widget(center_layout)  # Add the centered layout to the main layout


    # Displaying the Sign In Page
    def displaySignIn(self):
        self.clear_widgets()  # Clear existing widgets
        self.spacing = 10

        # Create a layout to center the inputs and button
        center_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, None), height=300)
        center_layout.padding = [460, 20, 20, 500]  # Add padding around the layout

        # Add the heading
        heading_label = Label(text='Sign In', font_size='25sp', size_hint=(1, None), height=50)
        heading_label.bind(size=heading_label.setter('text_size'))  # Ensure text is wrapped
        center_layout.padding = [460, 20, 20, 500]  # Add padding around the layout
        center_layout.add_widget(heading_label)

        # Wrap username input
        name_input = TextInput(hint_text='Enter your username', size_hint=(0.6, None), height=50)
        center_layout.add_widget(name_input)

        # Wrap password input
        password_input = TextInput(hint_text='Enter your password', size_hint=(0.6, None), height=50)
        center_layout.add_widget(password_input)

        # Button for Sign Up
        btn1 = Button(text='Sign In', size_hint=(0.6, None), height=60)  # Set size explicitly
        btn1.bind(on_press=lambda x: self.sign_up(name_input.text, password_input.text))  # Bind to sign-up logic
        center_layout.add_widget(btn1)

        self.add_widget(center_layout)  # Add the centered layout to the main layout

        # store = firestore.client()
        # usersRef = store.collection("users")

        # for user in usersRef.get():
        #     self.add_widget(Label(text=str(user.to_dict())))

    def sign_in(self, email, password):
        # Logic for signing in the user
        print(f"Email: {email}, Password: {password}")

#=======================================================================================================

if __name__ == '__main__':
    ChoreManagerApp().run()
