from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock

from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import StringProperty

from databaseManager import DatabaseManager


class ChoreManagerApp(App):
    def build(self):
        return ChoreManagerInterface()
    
class ChoreManagerInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(LoginSignupMenu())

class LoginSignupMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        x = DatabaseManager()

        x.GetUserData("james", "12345")
    
    def LoadMenu(self, i):
        self.remove_widget(self.children[1])

        tmp = None

        if i==0: tmp = LoginInterface()
        
        if i==1: tmp = SignupInterface()

        self.add_widget(tmp, index=1)

class LoginInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def SubmitLoginDetails(self):
        return None
        userInfo = userManager.Login(self.children[0].children[0].children[2].text, self.children[0].children[0].children[1].text)

        if userInfo == -1:
            print("Failed login")
            return

        app= App.get_running_app()
        app.root.currentUser = [userInfo, self.children[0].children[0].children[1].text]
        app.root.LoadPage(1)

class SignupInterface(BoxLayout):
    signinFeedbackText = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def SubmitSignUpDetails(self):
        return None
        self.signinFeedbackText = ""
        if self.children[0].children[0].children[4].text == "":
            self.signinFeedbackText = "Username invalid"
            return

        if userManager.IsUsernameAvailable(self.children[0].children[0].children[4].text) == False:
            self.signinFeedbackText = "Username already taken"
            return

        if self.children[0].children[0].children[3].text == "":
            self.signinFeedbackText = "Password invalid"
            return
        
        if self.children[0].children[0].children[2].text != self.children[0].children[0].children[3].text:
            self.signinFeedbackText = "Passwords don't match"
            return
        
        if userManager.SignUp(self.children[0].children[0].children[4].text, self.children[0].children[0].children[3].text):
            self.parent.LoadMenu(0)
        
        self.signinFeedbackText = "Sign up failed, try again"

#=======================================================================================================

if __name__ == '__main__':
    ChoreManagerApp().run()