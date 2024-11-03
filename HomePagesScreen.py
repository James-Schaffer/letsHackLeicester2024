from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


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
        # Main layout
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Collecting the house name from the user
        house_name_layout = BoxLayout(orientation="horizontal", padding=10, spacing=10, size_hint=(1, None), height=50)
        house_name_label = Label(text="House Name:", size_hint=(0.3, 1), font_size=18, halign="right", valign="middle")
        house_name_label.bind(size=house_name_label.setter("text_size"))
        house_name_input = TextInput(size_hint=(0.7, 1), font_size=18, multiline=False)
        house_name_layout.add_widget(house_name_label)
        house_name_layout.add_widget(house_name_input)

        # Area to add chores to the house
        add_chore_layout = BoxLayout(orientation="horizontal", padding=10, spacing=10, size_hint=(1, None), height=50)
        self.add_chore_input = TextInput(size_hint=(0.7, 1), font_size=18, multiline=False, hint_text="Enter a chore")
        add_chore_button = Button(text="Add Chore", size_hint=(0.3, 1), font_size=18)
        add_chore_button.bind(on_press=self.addChore)
        add_chore_layout.add_widget(self.add_chore_input)
        add_chore_layout.add_widget(add_chore_button)

        # Area to display the list of chores (using ScrollView for scrolling capability)
        scroll_view = ScrollView(size_hint=(1, 0.6))
        self.chores_layout = BoxLayout(orientation="vertical", padding=10, spacing=10, size_hint_y=None)
        self.chores_layout.bind(minimum_height=self.chores_layout.setter("height"))
        scroll_view.add_widget(self.chores_layout)

        # "Make House" button
        make_house_button = Button(text="Make House", size_hint=(1, None), height=50, font_size=18)
        
        # Adding all components to the main layout
        main_layout.add_widget(house_name_layout)
        main_layout.add_widget(add_chore_layout)
        main_layout.add_widget(scroll_view)
        main_layout.add_widget(make_house_button)

        return main_layout
    
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


# =======================================================================================================

if __name__ == "__main__":
    ChoreManagerApp().run()
