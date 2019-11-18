from flask import Flask,render_template
from models import User,Article,user_article
from exts import db
import settings
app = Flask(__name__)
app.config.from_object(settings)
# db = SQLAlchemy(app)
db.init_app(app)
# db.create_all()
@app.route('/login/')
def login():
    #增加
    # user1 = User(username=u'容祖儿' )
    # user2 = User(username=u'山猫')
    # db.session.add_all([user1, user2])
    # db.session.commit()
    # article1 = Article(title=u'白狐',content=u'我是一只修行千年的狐，千年修行千年孤独',author_id=user1.id)
    # article2 = Article(title=u'风花雪月',content=u'风是自息自生扰袖弄摆',author_id=user2.id)
    # db.session.add_all([article1,article2])
    # db.session.commit()
    #查询
    # result = Article.query.filter(Article.title == u'白狐').first()
    # print(result.id,result.title,result.content)

    return render_template('login.html')
if __name__ == '__main__':
    app.run()