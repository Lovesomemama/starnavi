from flask import Blueprint, jsonify, request, abort

from globals import storage, VERSION
from auth_types import User, Post

handler = Blueprint("auth", __name__, url_prefix="/auth/v1")


@handler.route('/healthcheck', methods=["GET"])
def health_check():
    return jsonify(status="green", version=VERSION), 200


@handler.route('/signup', methods=['POST'])
def post_signup():
    if not request.json:
        abort(400)
    user = User.from_json(request.json)
    is_created = storage.add_user(user)

    return user.to_json(), 201 if is_created else 200


@handler.route('/login', methods=['GET'])
def post_login():
    email = request.json["email"]
    print(email)
    password = request.json["password"]
    is_logined = storage.login(email, password)
    res = "Welcome!" if is_logined else "Try again"

    return {"result": res}, 200


@handler.route('/post_creation', methods=['POST'])
def post_creation():
    post = Post.from_json(request.json)
    is_created = storage.post_creation(post.email, post)
    return post.to_json(), 201 if is_created else 200


@handler.route('/like/<string:email>', methods=['GET'])
def post_like(email):
    post = storage.get_post(email)
    post.likes += 1
    return post.to_json(), 200


@handler.route('/unlike/<string:email>', methods=['GET'])
def post_unlike(email):
    post = storage.get_post(email)
    post.likes -= 1
    return post.to_json(), 200





