'''
Mac和windows下数据库的安装：
    1.Mysql为例
    2.下载地址：https://dev.mysql.com/downloads/mysql/
    3.Mac上安装Mysql很简单，直接一顿一下步安装就好了
    4.设置初始化密码的命令是：
        mysqladmin -uroot password [password]
    5.windows:
        如果没有安装.net Framework4,就是在那个提示框中，找到url，下载下来，安装即可
        如果没有安装Microsoft Visual C++ X64，那么就需要谷歌或者百度下载这个
MySQL-python 中间件的介绍与安装：
    1.如果是在Unix系统上，直接进入虚拟环境，输入sudo pip install mysql-python
    2.如果是在windows系统上，python2的需要进入：http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python下载：MySQL_python‑1.2.5‑cp27‑none‑win_amd64.whl，
        然后在命令行中，进入到：MySQL_python‑1.2.5‑cp27‑none‑win_amd64.whl所在的目录，输入以下命令进行安装：pip install MySQL_python‑1.2.5‑cp27‑none‑win_amd64.whl
Flask-SQLAlchemy的介绍与安装：
    1.ORM：Object Relationship Mapping(模型关系映射)
    2.flask-sqlalchemy是一套ORM框架
    3.ORM的好处：可以让我们操作数据库跟操作对象是一样的，非常方便。因为一个表就抽象成一个类，一条数据就抽象成该类的一个对象
    4.安装flask-sqlalchemy：sudo pip install flask-sqlalchemy

Flask-SQLAlchemy的使用：
    1.初始化和设置数据库配置信息：
        使用flask_sqlalchemy中的SQLAlchemy进行初始化：
        from flask_sqlalchemy import SQLAlchemy
        app = Flask(__name__)
        db = SQLAlchemy(app)
    2.设置配置信息：在config.py文件中添加以下配置信息：
        HOST = '127.0.0.1'
        USERNAME = 'root'
        PASSWORD = '123456'
        DATABASE = 'app_demo'
        PORT = '3306'
        DRIVER = 'pymysql'
        SQL = 'mysql'
        SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(SQL,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    3.在
'''