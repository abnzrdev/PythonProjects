class User():
    def __init__(self, user_name, user_followers):
        self.user_name = user_name
        self.user_followers = user_followers

    def increase_followers(self, user_name):
        self.user_followers += 1

user1 = User("Abenezer", 10)
print(user1.user_followers)
user2 = User("Samuel", 20)
user1.increase_followers(user1.user_name)
print(user1.user_followers)
