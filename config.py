import os


# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

db_user = os.environ.get('aws_db_user')
db_pass = os.environ.get('aws_db_pass')
db_endpoint = os.environ.get('aws_db_endpoint')


SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_pass}@{db_endpoint}:3306/flaskfinance'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True