import psycopg2
from urllib.parse import urlparse
from cinetify.config import DATABASE_URL


def database_connection():
    # parsed = urlparse(DATABASE_URL)
    # user = parsed.username
    # password = parsed.password
    # host = parsed.hostname
    # port = parsed.port
    # database = parsed.path.strip('/')
    user = 'postgres'
    password = 'perop1234'
    host = '10.200.1.237'
    port = '5432'
    database = 'postgres'

    connection = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
    connection.set_session(autocommit=True)

    return connection