from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock

from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_API_key.json")
firebase_admin.initialize_app(cred)

class ChoreManagerApp(App):
    def build(self):
        return ChoreManagerInterface()
    
class ChoreManagerInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Defining what screen the app is on, and whether the current state is set or not
        self.currentState = "SignUp"
        self.currentStateSet = False
        self.checkCurrentState()

    #Making the screen output the correct items
    def checkCurrentState(self):
        if not self.currentStateSet:
            if self.currentState == "SignUp" :
                self.displaySignUp()
            if self.currentState == "SignIn":
                self.displaySignIn()
        self.currentStateSet = True

    #Button to respond to SignIn page button
    def ChangeToSignIn(self,button):
        self.currentState = "SignIn"
        self.currentStateSet = False
        self.clear_widgets()
        self.checkCurrentState()
    
    #Displaying the Sign Up Page
    def displaySignUp(self):
        self.spacing = 10
        btn1 = Button(text='Up', size_hint=(.7, 1))
        btn1.bind(on_press=self.ChangeToSignIn)
        btn2 = Button(text='Sign', size_hint=(.3, 1))
        self.add_widget(btn1)
        self.add_widget(btn2)

    #Displaying the Sign In Page
    def displaySignIn(self):
        btn1 = Button(text='Sign', size_hint=(.7, 1))
        btn2 = Button(text='In', size_hint=(.3, 1))
        self.add_widget(btn1)
        self.add_widget(btn2)

        store = firestore.client()
        usersRef = store.collection("users")

        for user in usersRef.get():
            self.add_widget(Label(text=str(user.to_dict())))

#=======================================================================================================

if __name__ == '__main__':
    ChoreManagerApp().run()