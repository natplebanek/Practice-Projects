#Natalie Plebanek       Project 4       CSC 6003

#Music Collection Organizer

class Musimenu:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self, user):
    ##Add user: Allow users to create a New User object that
    ##can hold a music collection.
        if user in self.users:
            print(f"User '{user}' already exists.")
        else:
            self.users[user] = {"songs": {}}
            self.current_user = user
            print(f"User '{user}' added and set as current user.")

    def change_user(self, name):
    ##Change User: Allow users to select a different user
    ##or add a new user.
        if name in self.users:
            self.current_user = name
            print(f"Current user changed to '{name}'.")
        else:
            print(f"User '{name}' does not exist. Please add the user first.")

    def add_song2user(self, song, artist):
    ##Add a song: Prompt the user to enter the song title
    ##and artist, and add it to the music collection of
    ##that user.
        if self.current_user:
            if song in self.users[self.current_user]["songs"]:
                print(f"Song '{song}' by {artist} already exists in {self.current_user}'s library.")
            self.users[self.current_user]["songs"][song] = artist
            print(f"Added '{song}' by {artist} to {self.current_user}'s song library.")
        else:
            print("An error has occurred. Think about what you did to break the code.")

    def song_details(self, song):
    ##Retrieve song details: Prompt the user to enter a
    ##song title, and display the corresponding artist from
    ##the music collection of that user.
        if song in self.users[self.current_user]["songs"]:
            print(f"The artist for '{song}' is ", self.users[self.current_user]["songs"].get(song), ".")
        else:
            print("That song is not in this user's library.")

    def update_details(self, song, artist):
    ##Update song details: Prompt the user to enter a song
    ##title, and update the artist information in the music
    ##collection of that user.
        if song in self.users[self.current_user]["songs"]:
            self.users[self.current_user]["songs"][song] = artist
            print(f"The artist for '{song}' has been updated to {artist}")
        else:
            print("That song is not in this user's library.")

    def delete_song(self, song):
    ##Delete a song: Prompt the user to enter a song title,
    ##and remove the corresponding song from the music
    ##collection of that user.
        del self.users[self.current_user]["songs"][song]
        print(f"The song, '{song},' has been deleted from this collection.")
    
    def display_collection(self):
    ##Display all songs: Display all songs in the music
    ##collection of that user.
        songs = self.users[self.current_user]["songs"]
        if songs:
            print(f"Here is {self.current_user}'s music collection:")
            for song, artist in songs.items():
                  print(f"- {song} by {artist}")
        else:
            print(f"{self.current_user}'s song library is currently empty.")
        
print('''
~✧･ﾟ: *✧･ﾟ:* Welcome to MusiMenu! *:･ﾟ✧*:･ﾟ✧~

Please follow the prompts below to use. You will enter a
number that corresponds to each menu item in order to
access the modalities of that menu option.

For each user you add, we will organize the music you
would like to add directly to that user's profile.
''')

print('''
    ==== MusiMenu ====
     1) Add User
    ==================
''')

while True:
    try:
        menu_option = int(input("Menu Option: "))
        if menu_option == 1:
            break
        else:
            print("Please enter a 1. You gotta start this menu somehow (=.=)? .")
    except ValueError: 
            print("Invalid input. Please enter an integer.")

new_user = Musimenu()
username = input("Input new user's name: ")
new_user.add_user(username)

while True:
    while (bool(new_user.users[new_user.current_user]["songs"]) == 0) and (len(new_user.users) == 1):
        print(f'''
    ==== MusiMenu ====
     ✧ User {new_user.current_user} ✧
     1) Add User
     3) Add a song
    ==================
    ''')

        while True:
            try:
                menu_option = int(input("Menu Option: "))
                if (menu_option == 1) or (menu_option == 3):
                    break
                else:
                    print("Please enter a 1 or a 3.")
            except ValueError: 
                print("Invalid input. Please enter an integer.")
        if menu_option == 1:
            username = input("Input new user's name: ")
            new_user.add_user(username)
        else:
            song_name = input("Enter the song title: ")
            artist_name = input("Name of the Artist: ")
            new_user.add_song2user(song_name, artist_name)

    while (bool(new_user.users[new_user.current_user]["songs"]) > 0) and (len(new_user.users) == 1):
        print(f'''
    ==== MusiMenu ====
     ✧ User {new_user.current_user} ✧
     1) Add User
     3) Add a song
     4) Retrieve song details
     5) Update song details
     6) Delete a song
     7) Display all songs
    ==================
    ''')

        while True:
            try:
                menu_option = int(input("Menu Option: "))
                if (1 <= menu_option < 2) or (2 < menu_option <= 7):
                    break
                else:
                    print("Please enter a number among the menu items above.")
            except ValueError: 
                print("Invalid input. Please enter an integer.")

        if menu_option == 1:
            username = input("Input new user's name: ")
            new_user.add_user(username)
        elif menu_option == 3:
            song_name = input("Enter the song title: ")
            artist_name = input("Name of the Artist: ")
            new_user.add_song2user(song_name, artist_name)
        elif menu_option == 4:
            song_name = input("What song would you like details on? ")
            new_user.song_details(song_name)
        elif menu_option == 5:
            song_name = input("What song would you like to update? ")
            artist_name = input("What would you like to update the artist name to? ")
            new_user.update_details(song_name, artist_name)
        elif menu_option == 6:
            song_name = input("What song would you like to delete from your collection? ")
            new_user.delete_song(song_name)
        else:
            new_user.display_collection()

    while (bool(new_user.users[new_user.current_user]["songs"]) == 0) and (len(new_user.users) > 1):
        print(f'''
    ==== MusiMenu ====
     ✧ User {new_user.current_user} ✧
     1) Add User
     2) Change User
     3) Add a song
    ==================
    ''')
        while True:
            try:
                menu_option = int(input("Menu Option: "))
                if 1 <= menu_option <= 3:
                    break
                else:
                    print("Please enter a number from the menu options above.")
            except ValueError: 
                print("Invalid input. Please enter an integer.")
        if menu_option == 1:
            username = input("Input new user's name: ")
            new_user.add_user(username)
        elif menu_option ==2:
            name = input("What user would you like to change to? ")
            new_user.change_user(name)
        else:
            song_name = input("Enter the song title: ")
            artist_name = input("Name of the Artist: ")
            new_user.add_song2user(song_name, artist_name)
        
    while (bool(new_user.users[new_user.current_user]["songs"]) > 0) and (len(new_user.users) > 1):
        print(f'''
    ==== MusiMenu ====
     ✧ User {new_user.current_user} ✧
     1) Add User
     2) Change User
     3) Add a song
     4) Retrieve song details
     5) Update song details
     6) Delete a song
     7) Display all songs
    ==================
    ''')

        while True:
            try:
                menu_option = int(input("Menu Option: "))
                if 1 <= menu_option <= 7:
                    break
                else:
                    print("Please enter a number among the menu items above.")
            except ValueError: 
                print("Invalid input. Please enter an integer.")

        if menu_option == 1:
            username = input("Input new user's name: ")
            new_user.add_user(username)
        elif menu_option ==2:
            name = input("What user would you like to change to? ")
            new_user.change_user(name)
        elif menu_option == 3:
            song_name = input("Enter the song title: ")
            artist_name = input("Name of the Artist: ")
            new_user.add_song2user(song_name, artist_name)
        elif menu_option == 4:
            song_name = input("What song would you like details on? ")
            new_user.song_details(song_name)
        elif menu_option == 5:
            song_name = input("What song would you like to update? ")
            artist_name = input("What would you like to update the artist name to? ")
            new_user.update_details(song_name, artist_name)
        elif menu_option == 6:
            song_name = input("What song would you like to delete from your collection? ")
            new_user.delete_song(song_name)
        else:
            new_user.display_collection()
        
            
            



            





