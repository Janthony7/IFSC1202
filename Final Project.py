import re

class User:
    def __init__(self, UserName, Password):
        self.UserName = UserName
        self.Password = Password

class UserList:
    def __init__(self, filename):
        self.UserList = []
        self.filename = filename

    def ReadUserFile(self):
        with open(self.filename, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                self.UserList.append(User(username, password))
    
    def WriteUserFile(self):
        with open(self.filename, "w") as file:
            for user in self.UserList:
                file.write(f"{user.UserName}, {user.Password}\n")

    def DisplayUserList(self):
        print("Username        Password")
        print("--------------- ---------------")
        for user in self.UserList:
            print(f"{user.UserName:<15} {user.Password}")

    def FindUsername(self, username):
        for index, user in enumerate(self.UserList):
            if user.UserName == username:
                return index
        return -1
    
    def ChangePassword(self, username, password):
        index = self.FindUsername(username)
        if index != -1:
            self.UserList[index].Password = password
            print("Password Changed")
        else:
            print("Username Not Found")

    def AddUser(self, username, password):
        if self.FindUsername(username) == -1:
            self.UserList.append(User(username, password))
            print("User Added")
        else:
            print("Username Already Exists")

    def DeleteUser(self, username):
        index = self.FindUsername(username)
        if index != -1:
            del self.UserList[index]
            print("User Deleted")
        else:
            print("Username Not Found")

    def Strength(self, password):
        score = 0
        if len(password) >= 8:
            score += 1
        if re.search("[A-Z]", password):
            score += 1
        if re.search("[a-z]", password):
            score += 1
        if re.search("[0-9]", password):
            score += 1
        if re.search("[~!@#$%^&*()_+|-={}[]:;<>?/]", password):
            score += 1
        return score
    
def main():
    userList = UserList("Final Project Passwords.txt")
    userList.ReadUserFile()

    while True:
        print("\nMenu:")
        print("1) Add a New User")
        print("2) Delete an Existing User")
        print("3) Change Password on an Existing User")
        print("4) Display All Users")
        print("5) Save Changes to File")
        print("6) Quit")

        choice = input("Enter Selection: ")

        if choice == "1":
            username = input("Enter User ID: ")
            if userList.FindUsername(username) == -1:
                password = input("Enter Password: ")
                while userList.Strength(password) < 5:
                    print(f"This password is weak - {userList.Strength(password)}")
                    password = input("Enter a stronger Password: ")
                userList.AddUser(username, password)
            else:
                print("Username Already Exists")

        elif choice == "2":
            username = input("Enter User ID to Delete: ")
            userList.DeleteUser(username)  

        elif choice == "3":
            username = input("Enter User ID: ")
            if userList.FindUsername(username) != -1:
                password = input("Enter New Password: ")
                while userList.Strength(password) < 5:
                    print(f"This password is weak - {userList.Strength(password)}")
                    password = input("Enter a stronger Password: ")
                userList.ChangePassword(username, password)
            else:
                print("Username Not Found")

        elif choice == "4":
            userList.DisplayUserList()

        elif choice == "5":
            userList.WriteUserFile()
            print("Change Saved")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid Selection")

if __name__ == "__main__":
    main()



