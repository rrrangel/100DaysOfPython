class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Angel"
#
# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.name = "John"

user_3 = User("003", "Rob")

print(user_3.username, user_3.id, user_3.followers, user_3.following)

user_4 = User("004", "Lynn")

print(user_4.username, user_4.id, user_4.followers, user_4.following)

user_4.follow(user_3)
print(user_3.followers)
print(user_3.following)
print(user_4.followers)
print(user_4.following)
