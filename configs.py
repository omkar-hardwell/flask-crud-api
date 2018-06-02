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

# Database connection uri
DATABASE_URI = 'sqlite://'
if ENVIRONMENT == 'dev':
    DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
