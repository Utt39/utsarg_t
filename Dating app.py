import emoji

class User:
    def __init__(self, name, video_url, emoji, location, city, birthday):
        self.name = name
        self.video_url = video_url
        self.emoji = emoji
        self.location = location
        self.city = city
        self.birthday = birthday

    def describe(self):
        description = emoji.emojize(f":{self.emoji}: {self.name}\nVideo: {self.video_url}\nLocation: {self.location}\nCity: {self.city}\nBirthday: {self.birthday}")
        return description


class DatingApp:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def match(self, user1, user2):
        # You could add some kind of video matching algorithm here,
        # but for this simple example, we'll just say they match if their names are the same
        if user1.name == user2.name:
            return emoji.emojize(":sparkling_heart: MATCH!\n" + user1.describe() + "\n" + user2.describe() + " :sparkling_heart:")
        else:
            return emoji.emojize(":broken_heart: No match. Better luck next time. :broken_heart:")

    def request_coffee_date(self, user1, user2):
        return emoji.emojize(f":coffee: {user1.name} has requested a coffee date with {user2.name}! :coffee:")

    def block_user(self, user1, user2):
        return emoji.emojize(f":no_entry_sign: {user1.name} has blocked {user2.name}. :no_entry_sign:")

    def report_user(self, user):
        return emoji.emojize(f":rotating_light: {user.name} has been reported. :rotating_light:")


# Create instances of the User class
tom = User("tom Doe", "https://www.lightboxlove.com/tom-doe-video", "woman", "100 meters", "New York", "01/01/2000")
john = User("john Doe", "https://www.lightboxlove.com/john-doe-video", "man", "500 feet", "Los Angeles", "02/02/2000")
liz = User("liz Smith", "https://www.lightboxlove.com/liz-smith-video", "woman", "1 mile", "Chicago", "03/03/2000")

# Create an instance of the DatingApp class
app = DatingApp()

# Add users to the dating app
app.add_user(tom)
app.add_user(john)
app.add_user(liz)

# Find a match between two users
print(app.match(tom, john))
print(app.match(tom, liz))

# Request a coffee date
print(app.request_coffee_date(tom, john))

# Block a user
print(app.block_user(tom, john))

# Report a user
print(app.report_user(john))

