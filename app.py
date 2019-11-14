from flask import Flask,render_template

app = Flask(__name__)
class Person(object):
    name = ''
    age = 0
class Student(Person):
    pass
books = [
    {
        "name":u"红楼梦",
        "author":u"曹雪芹",
        "price":"21.8"

    },
    {
        "name": u"西游记",
        "author": u"罗贯中",
        "price": "38.8"

    }
]


# @app.route('/')
# def index():
#     return render_template('index.html', avater ='https://profile.csdnimg.cn/4/3/F/1_milaoshu1020', books=books)

# @app.route('/login/')
# def login():
#     return render_template('login.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
