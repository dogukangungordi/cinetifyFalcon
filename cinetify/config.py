import os


TWO_WEEKS = 1209600

SECRET_KEY = os.getenv('SECRET_KEY', '123')
assert SECRET_KEY

TOKEN_EXPIRES = TWO_WEEKS

DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgres://10.200.1.237:5432/perop_test/'.format(os.getenv('perop1234', None)))
assert DATABASE_URL