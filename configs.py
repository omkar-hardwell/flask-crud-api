"""Application configuration"""

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
    'username': 'username',
    'password': 'password',
    'host': 'host',
    'port': 3306,
    'database': 'database'
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
