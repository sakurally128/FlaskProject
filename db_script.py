from flask_script import Manager
DBManager = Manager()

@DBManager.command
def init():
    print('数据初始化完成')
@DBManager.command
def migrate():
    print('数据迁移成功')