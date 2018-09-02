"""Application configuration"""
import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Api information
API_NAME = 'flask-crud-api'
BASE_PATH = '/v1'

# Swagger specification file path
SWAGGER_SPEC_PATH = 'spec/swagger.yaml'

# Application environment
'''
Development: dev
Testing: test
'''
ENVIRONMENT = 'dev'

# Database credentials
DB_CREDENTIALS = {
    'username': os.getenv('DB_USERNAME') or '{username}',
    'password': os.getenv('DB_PASSWORD') or '{password}',
    'host': os.getenv('DB_HOST') or '{host}',
    'port': os.getenv('DB_PORT') or 3306,
    'database': os.getenv('DB_NAME') or '{database}'
}

# Database connection uri
DATABASE_URI = 'sqlite://'
if ENVIRONMENT == 'dev':
    DATABASE_URI = \
        'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'.\
        format(
            username=DB_CREDENTIALS.get('username'),
            password=DB_CREDENTIALS.get('password'),
            host=DB_CREDENTIALS.get('host'),
            port=DB_CREDENTIALS.get('port'),
            database=DB_CREDENTIALS.get('database')
        )
