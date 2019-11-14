'''
get请求和post请求
    1.get请求：
        使用场景：如果只对服务器获取数据，并没有对服务器产生任何影响，那么这个时候使用get请求。
        传参：get请求传参是放在URL中，并且是通过？的形式来指定key和value的
    2.post请求：
        使用场景：如果要对服务器产生影响，那么使用post请求
        传参：post请求传参不是放在url中，是通过form data的形式发送给服务器的。

get和post请求获取参数
    1.get请求是通过flask.request.args来获取
    2.post请求是通过flask.request.form来获取
    3.post请求在模板中要注意几点：
        input标签中，要写name来表示这个value的key，方便后台获取。
        在写form表单的时候，要制定method = 'post' ,并且要指定action = '/login/'
    4.示例代码：
        <form action = "{{url_for('login')}}" method = "post">
            <table>
                <tbody>
                    <tr>
                        <td>用户名：</td>
                        <td><input type = 'text' placeholder = '请输入用户名' name = 'username'></td>
                    </tr>
                    <tr>
                        <td>密码：</td>
                        <td><input type = 'text' placeholder = '请输入密码' name = 'password'></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><input type = 'submit' value = '登陆'></td>
                    </tr>
                </tbody>
            </table>
        </form>


'''