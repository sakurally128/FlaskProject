from exts import db
user_article = db.Table(
    'user_article',
    db.Column('user_id',db.Integer,db.ForeignKey('user.id'),primary_key=True),
    db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key=True),
    db.relationship('article',sencondary="user_tag",backref = db.backref('article'))
)
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.Intege,nullable=False)
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    articles = db.relationship('User',backref = db.backref('articles'))