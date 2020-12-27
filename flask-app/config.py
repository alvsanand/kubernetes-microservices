from datetime import timedelta
import os

AUTH_HOST = os.getenv('AUTH_HOST', 'http://sinatra-app:5001')

MONGO_HOST = os.getenv('MONGO_HOST', 'mongo')
MONGO_PORT = int(os.getenv('MONGO_PORT', "27017"))
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'logger')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret-O^#E#mo4ru')

JWT_EXPIRATION_DELTA = timedelta(
    seconds=int(os.getenv('JWT_EXPIRATION_DELTA', "3000000")))
