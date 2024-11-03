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
        self.clear_widgets()
        self.displaySignUp()

    # Method to change to the Sign In state
    def ChangeToSignIn(self, button):
        self.clear_widgets()
        self.displaySignIn()

    # Method to change to the Home Page
    def ChangeToHomePage(self,button):
        self.clear_widgets()
        self.DisplayHomeScreen()

    def ChangeToMakeHouse(self,button):
        self.clear_widgets()
        self.DisplayMakeHouse()
    
    def ChangeToSeeHouse(self,button):
        self.clear_widgets()
        self.DisplaySeeHouse()

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
        btn1.bind(on_press=lambda x: self.sign_in(name_input.text, password_input.text))  # Bind to signin logic
        center_layout.add_widget(btn1)

        self.add_widget(center_layout)  # Add the centered layout to the main layout
    
    # Displaying the Home Screen Page
    def DisplayHomeScreen(self):
        # Create a BoxLayout with vertical orientation
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Center the layout on the screen
        main_layout.size_hint = (None, None)
        main_layout.size = (800, 800)  # Set width and height of the button container
        main_layout.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Create the buttons with their properties and bindings
        btn1 = Button(text="Make House Chores", size=(700,300))
        btn1.bind(on_press=self.ChangeToMakeHouse)

        btn2 = Button(text="See a House Chores",size=(700,300))
        btn2.bind(on_press=self.ChangeToSeeHouse)

        # Add buttons to the layout
        main_layout.add_widget(btn1)
        main_layout.add_widget(btn2)

        # Add the layout to the main widget
        self.add_widget(main_layout)

    # Displaying the Make House Page
    def DisplayMakeHouse(self):
        # Create a BoxLayout with vertical orientation
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        # Collecting the house name from the user
        houseName_layout = BoxLayout(orientation="horizontal",padding=20,spacing=20)
        HouseName = Label()
        HouseName.text = "House Name : "
        HouseNameInput = TextInput()
        houseName_layout.add_widget(HouseName)
        houseName_layout.add_widget(HouseNameInput)
        # Area to add chores to the house
        addChore_layout = BoxLayout(orientation="horizontal",padding=20,spacing=20)
        self.AddChoreInput = TextInput() #Self so that this can be accessed in other functions
        AddChoreButton = Button(text="Add Chore")
        AddChoreButton.bind(on_press=self.addChore)
        addChore_layout.add_widget(self.AddChoreInput)
        addChore_layout.add_widget(AddChoreButton)
        # Area Below to display the chores
        # One chore is added each time the user clicks add chore
        self.chores_layout = BoxLayout(orientation="vertical",padding=20,spacing=20)
        # Make House Button
        MakeHouseButton = Button(text="Make House")
        # Adding all these items to the page
        self.add_widget(houseName_layout)
        self.add_widget(addChore_layout)
        self.add_widget(self.chores_layout)
        self.add_widget(MakeHouseButton)
    
    #Code used to add chore to chore layout
    def addChore(self,instance):
        # Get the text from the input field
        task_text = self.AddChoreInput.text.strip()
        
        # Only add if there's input text
        if task_text:
            # Add the task as a new label in the tasks layout
            task_label = Label(text=task_text, size_hint_y=None, height=40)
            self.chores_layout.add_widget(task_label)
            
            # Clear the input field after adding the task
            self.AddChoreInput.text = ""

    # Displaying the See House Page
    def DisplaySeeHouse(self):
        HouseName = Label()
        HouseName.text = "House Name"  # Get this value from the database
        AddFlatMates = Label()
        AddFlatMates.text = "Add Flat Mates : "
        FlatMateUserName = TextInput()
        AddFlatMateButton = Button(text="Add Flat Mate")
        TimetableText = Label()
        TimetableText.text = "Timetable"
        # This is where the timetable should be displayed
        EmptyText = Label()
        # Outputting the information to the screen
        self.add_widget(HouseName)
        self.add_widget(AddFlatMates)
        self.add_widget(FlatMateUserName)
        self.add_widget(AddFlatMateButton)
        self.add_widget(TimetableText)
        self.add_widget(EmptyText)

    #Making the Sign Up Logic for the page
    def sign_up(self,username,password):
        self.clear_widgets()
        self.DisplayHomeScreen()
    
    #Making the Sign In Logic for the page
    def sign_in(self,username,password):
        self.clear_widgets()
        self.DisplayHomeScreen()

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
