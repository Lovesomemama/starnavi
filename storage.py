from auth_types import User
import errors


class Storage:

    def __init__(self):
        self.users = dict()
        self.posts = dict()

    def add_user(self, user):
        self.users[user.email] = user
        return True

    def get_profile(self, email):
        return self.users[email]

    def login(self, email, password):
        if email not in self.users.keys():
            return False
        elif self.users[email].password != password:
            return False
        else:
            return True

    def post_creation(self, email, post):
        self.users[email].posts.append(post)
        self.posts[email] = post

    def get_post(self, email):
        print(email)
        return self.posts[email]
