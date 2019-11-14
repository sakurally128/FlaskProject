DEBUG = True
# dialect+driver://username:password@host:port/database
HOST = '127.0.0.1'
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'app_demo'
PORT = '3306'
DRIVER = 'pymysql'
SQL = 'mysql'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(SQL,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False