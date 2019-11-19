from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app_demo import app
from exts import db

manager = Manager(app)
migrate = Migrate(app,db)
#1.要使用flask_migrate,必须先绑定db
manager.add_command("db",MigrateCommand)

'''
python manage.py db init：这个命令不需要执行，因为已经初始化了迁移脚本的环境，这个命令只执行一次。

python manage.py db migrate：这个命令需要执行，因为模型改变了。

python manage.py db upgrade这个命令也需要执行，每次运行了migrate命令后，就记得要运行这个命令
'''

@manager.command
def runserver():
    print(u"服务器跑起来了！！！")
if __name__ == '__main__':
    manager.run()