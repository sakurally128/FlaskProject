'''
第一个Flask程序讲解：
1.第一次创建使用的时候，要添加flask的虚拟环境。添加虚拟环境的时候，一定要选择到python这个执行文件。
    比如：你的flask的虚拟环境的目录在/user/Virtualenv/flask-env/bin/python
2.flask程序代码的详细解释：
    #从flask这个框架中导入Flask这个类
    from flask import Flask

    #初始化一个Flask对象
    app = Flask（__name__）

    #@app.route('/')是一个装饰器，@开头，并且在函数的上面，说明是装饰器
    #这个装饰器的作用，是做一个url与视图函数的映射
    #127.0.0.1:5000/ ->去请求hello world这个函数，然后将结果返回给浏览器
    @app.route('/')
    def helloworld():
        return '我是第一个flask程序'
    #如果当前这个文件是作为入口程序运行，那么就执行app.run()
    if __name__ == '__main__':
        app.run()
    #启动一个应用服务器，来接收用户的请求
    #while True：
        listen（）
    app.run()
3.设置Debug模式
    1.在app.run()中传入一个关键字参数debug，app.run(debug=True)，就设置当前项目为debug模式
    2.debug模式的两大功能
        1)当程序出现问题的时候，可以在页面中看到错误信息和出错的位置
        2)只要修改了项目中的python文件，程序会自动加载，不需要手动重新启动服务
4.使用配置文件
    1.新建一个config.py文件
    2.在主app文件中导入这个文件，并且配置到app中，示例代码如下：
        import config
        app.config.from_object(config)
    3.还有许多的其他参数，都是放在这个配置文件中，比如：SECRET_KEY 和 SQLALCHEMY这些配置，都是在这个文件中。
5.url传参数：
    1.参数的作用：可以在相同的URL，但是指定不同的参数，来加载不同的数据
    2.在flask中如何使用参数：
        @app.route('/article/<id>')
        def article(id):
            return u'您请求的参数是：%s' %id
        参数需要放在两个尖括号中。
        视图函数中需要放和url中的参数同名的参数
6.反转URL：
    1.什么叫做反转URL：从视图函数到url的转换叫做反转URL
    2.反转URL的用处：
        在页面重定向的时候，会使用url反转
        在模板中，也会使用url反转
7.页面跳转和重定向
    1.用处：在用户访问一些需要登陆的页面的时候，如果用户没有登陆，那么可以让她重定向到登陆页面
    2.代码实现：
        from flask import redirect,url
        redirect(url_for('login'))
8.URL链接：使用url_for(视图函数名称)可以反转成url
9.加载静态文件：
   1.语法：url_for('static',filename = '路径')
   2.静态文件，flask会static文件夹中开始寻找，所以不需要再写static这个路径了。
   3.可以加载css文件，可以加载js文件，还有image文件。
    第一个：加载css文件<link rel="stylesheet" href="{{ url_for('static',filename='css/index.css') }}">
    第二个：加载js文件<script src="{{ url_for('static',filename='js/index.js') }}"></script>
    第三个：加载图片文件<img src="{{ url_for('static',filename='images/3.jpg') }}" alt="头像">

'''