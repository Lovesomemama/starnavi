import os

from storage import Storage


storage = Storage()

VERSION = "1.0"

if not os.getenv('TEST_MODE'):
    VERSION += ".{}".format(os.getenv("VERSION_TAG"))
