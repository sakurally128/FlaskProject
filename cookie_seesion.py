from flask import Flask
from flask import session
from datetime import timedelta
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

app.permanent_session_lifetime = timedelta(minutes=7)
session.permanent = True
'''
cookies：在Flask中操作cookie，是通过response对象来操作，可以在response返回之前，通过response.set_cookie来设置，这个方法有以下几个参数需要注意：

key：设置的cookie的key。
value：key对应的value。
max_age：改cookie的过期时间，如果不设置，则浏览器关闭后就会自动过期。
expires：过期时间，应该是一个datetime类型。
domain：该cookie在哪个域名中有效。一般设置子域名，比如cms.example.com。
path：该cookie在哪个路径下有效。
session：Flask中的session是通过from flask import session。然后添加值key和value进去即可。并且，Flask中的session机制是将session信息加密，然后存储在cookie中。专业术语叫做client side session。
'''
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
# 当我只设置了session.permanent = True时，可以看到浏览器中127.0.0.1中的session过期时间为31天。
#添加数据到session中
#操作session的时候，跟操作字典是一样的
#SECRET_KEY

@app.route('/')
def hello_world():
    session["username"] = "sakurally"
    return 'hello world'
@app.route('/get')
def get():
    return session.get('username')
@app.route('/delete/')
def delete():
    print(session.get("username"))
    session.pop("username")
    print(session.get("username"))
    return 'delete success'
@app.route('/clear/')
def clear():
    print(session.get("username"))
    session.clear()
    print(session.get("username"))
    return 'clear success'

# @app.route('/get')
# def get_session():
#     #可以直接使用session["username"],但是这样写，如果username不存在，则会抛出异常
#     print(session.get("username"))
#     return session.get("username")
if __name__ == '__main__':
    app.run()