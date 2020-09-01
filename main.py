from flask import Flask

from api import handler


def create_app():
    # test_mode = not (os.getenv('TEST_MODE') is None)
    # globals.storage.init_app(test_mode)
    #
    #logger.info("starting service, test_mode={}, VERSION={}".format(test_mode, globals.VERSION))

    app = Flask(__name__)
    #if test_mode:
    app.debug = True

    app.register_blueprint(handler)

    return app


if __name__ == '__main__':
    create_app().run()

