import falcon
from cinetify.middleware.body_parser import JSONBodyParser
from cinetify.middleware.auth import AuthUser
from cinetify.utils.database import database_connection


db = database_connection()

middlewa = [JSONBodyParser(), AuthUser()]

api = falcon.API(middleware=middlewa)


from . import routes