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
    3.在主APP文件中，添加配置文件：
        app = Flask(__name__)
        app.config.from_object(config)
        db = SQLAlchemy(app)
    4.做测试，看有没有问题：
        db.create_all()
        如果没有报错，说明配置没有问题，如果有错误，可以根据错误进行修改
使用Flask-SQLAlchemy创建模型与表的映射：
    1.模型需要继承自db.Model,然后需要映射到表中的属性，必须写成db.Clumn的数据类型
    2.数据类型：
        db.Integer 代表整形
        db.String  代表Varchar，需要指定长度
        dB.Text    代表的是text
    3.其他参数：
        primary_key:代表的是将这个字段设置为主键
        autoincrement：代表的是这个主键为自增长的
        nullable：代表的是这个字段是否可以为空，默认可以为空，可以将这个值设置为Flase，在数据库中，这个值就不能为空了
    4.最后需要调用db.create_all来将这个模型真正的创建到数据库中
    
Flask-SQLAlchemy数据的增、删、该、查
    1.增：
        article1 = Article(title = 'aaa',content = 'bbb')
        db.session.add(article1)
        db.session.commit()
    2.查：
       #select * from article where article.title = 'aaa'
       article1 = Article.query.filter(Article.title == 'a').first()
       print("title:%s,content:%s" %(article1.title,article1.content))
    3.改：
       #1.先把你要更改的数据查找出来
       article1 = Article.query.filter(Article.title == 'aaa').first()
       #2.把这条数据，你需要修改的地方进行修改
       article1.title = "new title"
       #3.做事务的提交
       db.session.commit()
    4.删：
        #1.先把你要更改的数据查找出来
       article1 = Article.query.filter(Article.content == 'bbb').first()
       #2.把这条数据删除掉
       db.session.delete(article1)
       #3.做事务的提交
       db.session.commit()

Flask-SQLAlchemY外键及其关系：
    1.外键：
        class User(db.Model):
            __tablename__ = 'user'
            id = db.Column(db.Integer,primary_key=True,autoincrement=True)
            username = db.Column(db.String(100),nullable=False)

        class Article(db.Model):
            __tablename__ = 'article'
            id = db.Column(db.Integer, primary_key=True, autoincrement=True)
            title = db.Column(db.String(100),nullable=False)
            content = db.Column(db.Text,nullable=False)
            author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
            author = db.relationship("User",backref = db.backref("articles"))
            
    2.author = db.relationship("User",backref = db.backref("articles"))解释：
        给Article这个模型添加一个author属性，可以访问这篇文章的作者的数据，像访问普通模型一样
        backref是定义反向引用，可以通过User.articles访问这个模型所写的文章
        
    3.多对多
        多对多的关系，要通过一个中间表进行关联
        中间表，不能通过class的方式实现，只能通过db.Table的方式实现
        设置关联：tags = db.relationship("Tag",secondary = article_tag,backref = db.backref('articles'))需要使用一个关键字参数secondary = 中间表来进行关联
        
        访问和数据添加可以通过以下方式进行操作：
        添加数据：
        
    
'''