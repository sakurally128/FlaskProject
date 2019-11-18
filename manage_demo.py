from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app_demo import app
from exts import db

manager = Manager(app)
migrate = Migrate(app,db)
#1.要使用flask_migrate,必须先绑定db
manager.add_command("db",MigrateCommand)

@manager.command
def runserver():
    print(u"服务器跑起来了！！！")
if __name__ == '__main__':
    manager.run()