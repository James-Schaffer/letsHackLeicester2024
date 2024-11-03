import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

'''
store = firestore.client()
usersRef = store.collection("users")

for user in usersRef.get():
    self.add_widget(Label(text=str(user.to_dict()["username"])))
'''

class DatabaseManager:
    def __init__(self):
        self.cred = credentials.Certificate("firebase_API_key.json")
        firebase_admin.initialize_app(self.cred)
        self.store = firestore.client()

        self.username = None

    def UserfromUsername(self, username):
        userRef = self.store.collection("users").where(filter=FieldFilter("username", "==", username))
        
        user = userRef.stream()

        # Check if the user exists
        user_found = False
        for user in user:
            user_found = True  # If we enter the loop, it means a user was found
            print(f"User found: {user.id}")
            # Optionally, you can access the user's data with user.to_dict()
            print(user.to_dict())
            tmp = user

        if not user_found:
            print("User does not exist.")
            return 404
        
        return user
    
    def UserfromUserID(self, userID):
        userRef = self.store.collection("users").document(userID)
        
        user = userRef.get()

        # Check if the user exists
        if user.exists:
            print(f"User found: {user.id}")
            # Optionally, you can access the user's data with user.to_dict()
            print(user.to_dict())
        else:
            print("User does not exist.")
            return 404
        
        return user

    def GetUserData(self, userID=None, username=None):
        user = None
        if userID != None:
            user = self.UserfromUserID(userID)
        elif username != None:
            user = self.UserfromUsername(username)

        return user
    
    def LoginReq(self, username, password):
        user = self.GetUserData(username=username)

        if user == 404:
            return 404
        
        if user.to_dict()["password"] != password:
            print("Password incorrect")
            return 401
        
        self.username = username

        return user
    
    def CreateNewUser(self, username, email, password):
        # Check if user already exists
        docRef = self.GetUserData(username=username)

        print(docRef)
        
        # Check if the document exists
        if docRef != 404:
            print("User already exists.")
            return
        
        # If it doesn't exist, create a new document
        userData = {
            "username": username,
            "email"   : email,
            "password": password  # Encrypt passwords in production
        }
        
        try:
            new_doc_ref = self.store.collection("users").add(userData)

            print(f"User created with auto-generated ID: {new_doc_ref[1].id}")
            print(f"User created with name: {username}")
            return True
        except:
            return False
        
    def GetFlatData(self, flatID):
        flatRef = self.store.collection("flats").document(flatID)

        flat = flatRef.get()

        # Check if the user exists
        if not flat.exists:
            print("Flat does not exist.")
            return 404

        print(f"Flat found: {flat.id}")
        # Optionally, you can access the user's data with user.to_dict()
        print(flat.to_dict())

        return flat
        
    def CreateNewFlat(self, flatName, username):
        userRef = self.GetUserData(username=username)

        if userRef == 404 or userRef == 401:
            print("user does not exist or password incorrect")
            return None

        # If it doesn't exist, create a new document
        flatData = {
            "flatName": flatName
        }

        try:
            new_doc_ref = self.store.collection("flats").add(flatData)

            userFlatData = {
                "userID": userRef.id,
                "flatID": new_doc_ref[1].id
            }
        
            new_doc_ref = self.store.collection("userFlats").add(userFlatData)

            print(f"Flat created with auto-generated ID: {new_doc_ref[1].id}")
            return True
        except:
            return False

    def AddUserToFlat(self, flatID, usernameToAdd):
        user = self.GetUserData(username=usernameToAdd)

        if user == 404:
            print("user does not exist")
            return None

        userFlatData = {
            "userID": user.id,
            "flatID": flatID
        }
    
        self.store.collection("userFlats").add(userFlatData)

        print(f"{usernameToAdd} added to flat with ID: {flatID}")

    def GetUserFlatFromUsername(self, username):
        user = self.GetUserData(username=username)

        if user == 404:
            print("user does not exist")
            return None
        
        userFlatRef = self.store.collection("userFlats").where(filter=FieldFilter("userID", "==", user.id))
        
        userFlat = userFlatRef.stream()

        # Check if the user exists
        found = False
        tmp = []
        for userFlata in userFlat:
            found = True  # If we enter the loop, it means a user was found
            print(f"UserFlat found: {userFlata.id}")
            # Optionally, you can access the user's data with user.to_dict()
            print(userFlata.to_dict())
            tmp.append(userFlata)

        if not found:
            print("User is not in flat")
            return 404
        
        return tmp
    
    def GetTaskForUserFlat(self, username, flatID):
        userFlats = self.GetUserFlatFromUsername(username)

        if userFlats == 404:
            return None

        for userFlat in userFlats:
            if userFlat.id == flatID:
                continue
        
        userFlatTaskRef = self.store.collection("userFlatTasks").where(filter=FieldFilter("userFlatID", "==", userFlat.id))
        
        userFlatTask = userFlatTaskRef.stream()

        # Check if the user exists
        found = False
        tmp = []
        for userFlatTaska in userFlatTask:
            found = True  # If we enter the loop, it means a user was found
            print(f"UserFlat found: {userFlatTaska.id}")
            # Optionally, you can access the user's data with user.to_dict()
            print(userFlatTaska.to_dict())
            tmp.append(userFlatTaska)

        if not found:
            print("User is not in flat")
            return 404
        
        return tmp

    def AddTaskToUserFlat(self, userFlatID, taskID):
        from datetime import datetime
        userFlatRef = self.store.collection("userFlats").document(userFlatID)

        userFlat = userFlatRef.get()

        # Check if the user exists
        if not userFlat.exists:
            print("Flat does not exist.")
            return 404
        
        try:
            
            userFlatTaskData = {
                "userFlatID": userFlat.id,
                "taskID": taskID,
                "date": datetime.today().strftime('%d-%m-%Y'),
                "complete": False
            }
        
            new_doc_ref = self.store.collection("userFlatTasks").add(userFlatTaskData)

            print(f"userFlatTask created with auto-generated ID: {new_doc_ref[1].id}")
            return True
        except:
            return False

    def SetUserTaskComplete(self, userFlatTaskID):
        userFlatTaskRef = self.store.collection("userFlatTasks").document(userFlatTaskID)

        userFlatTask = userFlatTaskRef.get()

        # Check if the user exists
        if not userFlatTask.exists:
            print("Flat does not exist.")
            return 404
        
        userFlatTaskRef.set({"complete": True}, merge=True)