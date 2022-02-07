class User:
    def __init__(self,id,username):
        self.id = id 
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers +=1
        self.following +=1

user_1 = User('001','edem')
user_3 = User('003','Hans')
user_2 = User('002','Jack')
user_1.follow(user_2)
# user_2.follow(user_1)
user_3.follow(user_1)
print('User 1 Followers : ',user_1.followers)
print('User 1 Following : ',user_1.following )
print('User 2 Followers :', user_2.followers )
print('User 2 Following : ',user_2.following )
print('User 3 Following : ',user_3.followers )

