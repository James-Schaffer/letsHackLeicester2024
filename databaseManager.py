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

    def GetUserData(self, username, password):
        userRef = self.store.collection("users").where(filter=FieldFilter("username", "==", username))

        user = userRef.stream()

        # Check if the user exists
        user_found = False
        for user in user:
            user_found = True  # If we enter the loop, it means a user was found
            print(f"User found: {user.id}")
            # Optionally, you can access the user's data with user.to_dict()
            print(user.to_dict())
            tmp = user.id

        if not user_found:
            print("User does not exist.")
            return 404
        
        if user.to_dict()["password"] != password:
            print("Password incorrect")
            return 401

        return self.store.collection("users").document(tmp)
    
    def CreateNewUser(self, username, email, password):
        # Reference to the document with the userName as ID
        docRef = self.GetUserData(username, None)
        
        # Check if the document exists
        if docRef.get().exists:
            print("User already exists.")
            return

        # If it doesn't exist, create a new document
        userData = {
            "userName": username,
            "email"   : email,
            "passWord": password  # Encrypt passwords in production
        }
        docRef.set(userData)

        print(f"User created with auto-generated ID: {new_doc_ref[1].id}")
        print(f"User created with name: {username}")

