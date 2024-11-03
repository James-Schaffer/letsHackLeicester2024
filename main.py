from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

from databaseManager import DatabaseManager

class ChoreManagerApp(App):
    def build(self):
        return ChoreManagerInterface()
    
class ChoreManagerInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Setting some base variables
        self.chores = []
        self.users = []
        # Set background color for the app
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

        self.DbM = DatabaseManager()

        # Create the buttons to switch states
        self.create_initial_buttons()

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def create_initial_buttons(self):
        # Set padding for the entire layout
        self.padding = [20, 50, 20, 20]  # left, top, right, bottom padding

        # Add the heading
        heading_label = Label(
            text='Welcome to Chore Manager',
            font_name="InriaSans-Bold.ttf",
            font_size='50sp',
            color=('#338b6b'),  
            size_hint=(1, None),
            height=50
        )
        self.add_widget(heading_label)  # Add heading to the main layout
        
        # Add a blank widget as a spacer
        spacer = Widget(size_hint=(1, None), height=35)  # Adjust height as needed for spacing
        self.add_widget(spacer)

        # Add the heading
        desc_label = Label(
            text='Make chores a team effort',
            font_name="InriaSans-Regular.ttf",
            font_size='25sp',
            color=(0.8, 0.8, 0.8, 1),  
            size_hint=(1, None),
            height=50
        )
        self.add_widget(desc_label)  # Add heading to the main layout

        # Add a blank widget as a spacer
        spacer = Widget(size_hint=(1, None), height=20)  # Adjust height as needed for spacing
        self.add_widget(spacer)

        # Create a horizontal layout for the buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=900, spacing=20)
        
        btn_sign_up = Button(
            text='Sign Up',
            size_hint=(.5, 1),
            font_name="InriaSans-Regular.ttf",
            background_color=(0.2, 0.8, 0.6, 1),  # Green background
            color=(1, 1, 1, 1),  # White text
            font_size='20sp'
        )
        btn_sign_up.bind(on_press=self.ChangeToSignUp)
        
        btn_sign_in = Button(
            text='Sign In',
            size_hint=(.5, 1),
            font_name="InriaSans-Regular.ttf",
            background_color=(0.2, 0.6, 0.8, 1),  # Blue background
            color=(1, 1, 1, 1),  # White text
            font_size='20sp'
        )
        btn_sign_in.bind(on_press=self.ChangeToSignIn)

        # Add the buttons to the button layout
        button_layout.add_widget(btn_sign_up)
        button_layout.add_widget(btn_sign_in)

        # Add the button layout to the main layout
        self.add_widget(button_layout)

    # Methond to change to initial page
    def ChangeToIntials(self,button):
        self.clear_widgets()
        self.create_initial_buttons()

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
        heading_label = Label(
            text='Sign Up',
            color=('#338b6b'), 
            font_name="InriaSans-Bold.ttf", 
            font_size='25sp', 
            size_hint=(1, None), 
            height=50)
        heading_label.bind(size=heading_label.setter('text_size'))  # Ensure text is wrapped
        center_layout.padding = [460, 20, 20, 500]  # Add padding around the layout
        center_layout.add_widget(heading_label)


        # Userame input
        name_input = TextInput(
            hint_text='Enter your username',
            font_name="InriaSans-Regular.ttf", 
            size_hint=(0.6, None), 
            height=50)
        center_layout.add_widget(name_input)

        # Password input
        password_input = TextInput(
            hint_text='Enter your password', 
            font_name="InriaSans-Regular.ttf",
            size_hint=(0.6, None), 
            height=50)
        center_layout.add_widget(password_input)

        # Button for Sign Up
        btn1 = Button(
            text='Sign Up', 
            font_name="InriaSans-Regular.ttf",
            background_color=('#338b6b'), 
            size_hint=(0.6, None), 
            height=60)  # Set size explicitly
        btn1.bind(on_press=lambda x: self.sign_up(name_input.text, password_input.text))  # Bind to sign-up logic
        center_layout.add_widget(btn1)

        self.add_widget(center_layout)  # Add the centered layout to the main layout
        
        # Create a horizontal layout for the buttons
        backBtn_layout = BoxLayout(orientation='horizontal', size_hint=(0.2, None), height=30, spacing=10)
       
        #Back button to display home screen
        back_btn=Button(text='Back')
        back_btn.bind(on_press=self.ChangeToIntials)

        backBtn_layout.add_widget(back_btn)

        # Add the button layout to the main layout
        self.add_widget(backBtn_layout)

    # Displaying the Sign In Page
    def displaySignIn(self):
        self.clear_widgets()  # Clear existing widgets
        self.spacing = 10

        # Create a layout to center the inputs and button
        center_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, None), height=300)
        center_layout.padding = [460, 20, 20, 500]  # Add padding around the layout

        # Add the heading
        heading_label = Label(
            text='Sign In', 
            color=('#338b6b'), 
            font_name="InriaSans-Bold.ttf",
            font_size='25sp', 
            size_hint=(1, None), 
            height=50)
        heading_label.bind(size=heading_label.setter('text_size'))  # Ensure text is wrapped
        center_layout.padding = [460, 20, 20, 500]  # Add padding around the layout
        center_layout.add_widget(heading_label)

        # Wrap username input
        name_input = TextInput(
            hint_text='Enter your username', 
            font_name="InriaSans-Bold.ttf",
            size_hint=(0.6, None), 
            height=50)
        center_layout.add_widget(name_input)

        # Wrap password input
        password_input = TextInput(
            hint_text='Enter your password', 
            font_name="InriaSans-Bold.ttf",
            size_hint=(0.6, None), 
            height=50)
        center_layout.add_widget(password_input)

        # Button for Sign Up
        btn1 = Button(text='Sign In', size_hint=(0.6, None), height=60)  # Set size explicitly
        btn1.bind(on_press=lambda x: self.sign_in(name_input.text, password_input.text))  # Bind to signin logic
        center_layout.add_widget(btn1)

        self.add_widget(center_layout)  # Add the centered layout to the main layout

        # Create a horizontal layout for the back buttons
        backBtn_layout = BoxLayout(orientation='horizontal', size_hint=(0.2, None), height=30, spacing=10)
        back_btn=Button(text='Back')
        back_btn.bind(on_press=self.ChangeToIntials)

        backBtn_layout.add_widget(back_btn)

        # Add the button layout to the main layout
        self.add_widget(backBtn_layout)
    
    # Displaying the Home Screen Page
    def DisplayHomeScreen(self):
        # Create a BoxLayout with vertical orientation
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=100)

        # Center the layout on the screen
        main_layout.size_hint = (None, None)
        main_layout.size = (800, 800)  # Set width and height of the button container
        main_layout.padding = [200, 40, 40, 200]

        # Create the buttons with their properties and bindings
        btn1 = Button(text="Make House Chores", font_size="60sp",size_hint=(None,None),size=(1200,300))
        btn1.bind(on_press=self.ChangeToMakeHouse)

        btn2 = Button(text="See House Chores",font_size="60sp",size_hint=(None,None),size=(1200,300))
        btn2.bind(on_press=self.ChangeToSeeHouse)

        # Add buttons to the layout
        main_layout.add_widget(btn1)
        main_layout.add_widget(btn2)

        # Add the layout to the main widget
        self.add_widget(main_layout)

        # Create a horizontal layout for the buttons
        logout_layout = BoxLayout(orientation='horizontal', size_hint=(0.2, None), height=30, spacing=10)
       
        #Back button to display home screen
        logout_btn=Button(text='Log Out')
        logout_btn.bind(on_press=self.ChangeToIntials)
        logout_layout.add_widget(logout_btn)
        self.add_widget(logout_layout)

    # Displaying the Make House Page
    def DisplayMakeHouse(self):
        # Main layout
        mainLayout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Collecting the house name from the user
        houseNameLayout = BoxLayout(orientation="horizontal", padding=10, spacing=10, size_hint=(1, None), height=80)
        houseNameLabel = Label(text="House Name:", size_hint=(0.3, 1), font_size=30, halign="right", valign="middle")
        houseNameLabel.bind(size=houseNameLabel.setter("text_size"))
        houseNameInput = TextInput(size_hint=(0.7, 1), font_size=30, multiline=False)
        houseNameLayout.add_widget(houseNameLabel)
        houseNameLayout.add_widget(houseNameInput)

        # Area to add chores
        addChoreLayout = BoxLayout(orientation="horizontal", padding=10, spacing=10, size_hint=(1, None), height=80)
        self.addChoreInput = TextInput(size_hint=(0.7, 1), font_size=30, multiline=False, hint_text="Enter a chore")
        addChoreButton = Button(text="Add Chore", size_hint=(0.3, 1), font_size=30)
        addChoreButton.bind(on_press=self.addChore)
        addChoreLayout.add_widget(self.addChoreInput)
        addChoreLayout.add_widget(addChoreButton)

        # Chores ScrollView for displaying added chores
        choresScrollView = ScrollView(size_hint=(1, 0.3))
        self.choresLayout = BoxLayout(orientation="vertical", padding=10, spacing=10, size_hint_y=None)
        self.choresLayout.bind(minimum_height=self.choresLayout.setter("height"))
        choresScrollView.add_widget(self.choresLayout)

        # Area to add users
        addUserLayout = BoxLayout(orientation="horizontal", padding=10, spacing=10, size_hint=(1, None), height=80)
        self.addUserInput = TextInput(size_hint=(0.7, 1), font_size=30, multiline=False, hint_text="Enter a user name")
        addUserButton = Button(text="Add User", size_hint=(0.3, 1), font_size=30)
        addUserButton.bind(on_press=self.addUser)
        addUserLayout.add_widget(self.addUserInput)
        addUserLayout.add_widget(addUserButton)

        # Users ScrollView for displaying added users
        usersScrollView = ScrollView(size_hint=(1, 0.3))
        self.usersLayout = BoxLayout(orientation="vertical", padding=10, spacing=10, size_hint_y=None)
        self.usersLayout.bind(minimum_height=self.usersLayout.setter("height"))
        usersScrollView.add_widget(self.usersLayout)

        # "Make House" button
        makeHouseButton = Button(text="Make House", size_hint=(1, None), height=80, font_size=30)
        makeHouseButton.bind(on_press= lambda x : self.MakeHouse(houseNameInput.text))

        # Back button
        backBtn = Button(text="Back", size_hint=(0.2, None), height=50, font_size=20)
        backBtn.bind(on_press=self.ChangeToHomePage)

        # Add all widgets to the main layout
        mainLayout.add_widget(houseNameLayout)
        mainLayout.add_widget(addChoreLayout)
        mainLayout.add_widget(choresScrollView)
        mainLayout.add_widget(addUserLayout)
        mainLayout.add_widget(usersScrollView)
        mainLayout.add_widget(makeHouseButton)
        mainLayout.add_widget(backBtn)
        self.add_widget(mainLayout)

    def addChore(self, instance):
        # Get the chore text from the input field
        chore_text = self.addChoreInput.text.strip()
        if chore_text:
            # Add the chore as a new label in the chores layout
            chore_label = Label(text=chore_text, size_hint_y=None, height=40, font_size=30)
            self.choresLayout.add_widget(chore_label)
            # Clear the input field after adding the chore
            self.addChoreInput.text = ""
            # Adding the chore to the chores array
            self.chores.append(chore_text)

    def addUser(self, instance):
        # Get the user name text from the input field
        user_text = self.addUserInput.text.strip()
        if user_text:
            # Add the user name as a new label in the users layout
            user_label = Label(text=user_text, size_hint_y=None, height=40, font_size=30)
            self.usersLayout.add_widget(user_label)
            # Clear the input field after adding the user
            self.addUserInput.text = ""
            self.users.append(user_text)

    #Function to Make a House, using the given information
    def MakeHouse(self,houseName):
        #Making the flat, using the username and flatName
        self.DbM.CreateNewFlat(houseName,self.DbM.username)
        #Opening up the flat in see house
        self.clear_widgets()
        self.DisplaySeeHouse()

    # Displaying the See House Page
    def DisplaySeeHouse(self):
        userFlatsRef = self.DbM.GetUserFlatFromUsername(self.DbM.username)[0].to_dict()
        flatRef = self.DbM.GetFlatData(userFlatsRef["flatID"])
        flatDictionary = flatRef.to_dict()
        flatName = flatDictionary["flatName"]


        HouseName = Label(text=flatName)
        #HouseName.text = "House Name : " + flatRef.to_dict()["flatName"] # Get this value from the database
        AddFlatMates = Label()
        AddFlatMates.text = "Add Flat Mates : "
        FlatMateUserName = TextInput()
        AddFlatMateButton = Button(text="Add Flat Mate")
        TimetableText = Label()
        TimetableText.text = "Timetable"
        # This is where the timetable should be displayed
        EmptyText = Label()

        # Create a horizontal layout for the back buttons
        backBtn_layout = BoxLayout(orientation='horizontal', size_hint=(0.2, None), height=30, spacing=10)
        back_btn=Button(text='Back')
        back_btn.bind(on_press=self.ChangeToHomePage)
        backBtn_layout.add_widget(back_btn)

        # Outputting the information to the screen
        self.add_widget(HouseName)
        self.add_widget(AddFlatMates)
        self.add_widget(FlatMateUserName)
        self.add_widget(AddFlatMateButton)
        self.add_widget(TimetableText)
        self.add_widget(EmptyText)
        self.add_widget(backBtn_layout)

    #Making the Sign Up Logic for the page
    def sign_up(self,username,password):
        if username == "" or password == "":
            return None

        self.DbM.CreateNewUser(username=username, password=password, email="foo@bar.com")

        self.clear_widgets()
        self.displaySignIn()
    
    #Making the Sign In Logic for the page
    def sign_in(self,username,password):
        ret = self.DbM.LoginReq(username, password)

        if ret == 401 or ret == 404:
            return None

        self.clear_widgets()
        self.DisplayHomeScreen()

        # store = firestore.client()
        # usersRef = store.collection("users")

#=======================================================================================================

if __name__ == '__main__':
    ChoreManagerApp().run()
