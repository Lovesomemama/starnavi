import errors


class User:

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
        self.posts = []

    def to_json(self):
        return {
            "email": self.email,
            "name": self.name,
            "password": self.password,
            "posts": [post.to_json() for post in self.posts]
        }

    @staticmethod
    def from_json(json):
        try:
            email = json["email"]
            name = json["name"]
            password = json["password"]
        except ValueError as err:
            raise errors.InvalidJson("Value error : {0}".format(err))
        except KeyError as err:
            raise errors.InvalidJson("Key error : {0}".format(err))

        return User(email, name, password)


class Post:

    def __init__(self, email, info):
        self.email = email
        self.info = info
        self.likes = 0

    def to_json(self):
        return {
            "email": self.email,
            "likes": self.likes,
            "info": self.info
        }

    @staticmethod
    def from_json(json):
        try:
            email = json["email"]
            likes = 0
            info = json["info"]
        except ValueError as err:
            raise errors.InvalidJson("Value error : {0}".format(err))
        except KeyError as err:
            raise errors.InvalidJson("Key error : {0}".format(err))

        return Post(email, info)
