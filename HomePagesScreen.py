from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class ChoreManagerApp(App):
    def build(self):
        return ChoreManagerInterface()


class ChoreManagerInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Defining what screen the app is on, and whether the current state is set or not
        self.currentState = "HomeScreen"
        self.currentStateSet = False
        self.checkCurrentState()

    # Making the screen output the correct items
    def checkCurrentState(self):
        if not self.currentStateSet:
            if self.currentState == "HomeScreen":
                self.DisplayHomeScreen()
            elif self.currentState == "MakeHouse":
                self.DisplayMakeHouse()
            elif self.currentState == "SeeHouse":
                self.DisplaySeeHouse()
        self.currentStateSet = True

    # Functions to change the currentState of the screen
    def ChangeToMakeHouse(self, button):
        self.currentState = "MakeHouse"
        self.currentStateSet = False
        self.clear_widgets()
        self.checkCurrentState()

    def ChangeToSeeHouse(self, button):
        self.currentState = "SeeHouse"
        self.currentStateSet = False
        self.clear_widgets()
        self.checkCurrentState()

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
        AddChoreInput = TextInput()
        AddChoreButton = Button(text="Add Chore")
        addChore_layout.add_widget(AddChoreInput)
        addChore_layout.add_widget(AddChoreButton)
        # Area Below to display the chores
        # One chore is added each time the user clicks add chore
        chores_layout = BoxLayout(orientation="vertical",padding=20,spacing=20)
        Chore1 = Label()
        Chore1.text = "Chore 1"
        Chore2 = Label()
        Chore2.text = "Chore 2"
        Chore3 = Label()
        Chore3.text = "Chore 3"
        Chore4 = Label()
        Chore4.text = "Chore 4"
        chores_layout.add_widget(Chore1)
        chores_layout.add_widget(Chore2)
        chores_layout.add_widget(Chore3)
        chores_layout.add_widget(Chore4)
        # Make House Button
        MakeHouseButton = Button(text="Make House")
        # Adding all these items to the page
        self.add_widget(houseName_layout)
        self.add_widget(addChore_layout)
        self.add_widget(chores_layout)
        self.add_widget(MakeHouseButton)

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


# =======================================================================================================

if __name__ == "__main__":
    ChoreManagerApp().run()
