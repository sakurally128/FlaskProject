# 常用软件
## 网络抓包工具
1. fiddler
    > windows平台,http协议分析,修改请求/响应
    1. bpu 请求前断点
    2. bpafter 获取响应之后断点
    3. AutoReponder 修改响应 
    
2. wireshark
    > 网络协议分析
3. tcpdump
    > linux 命令行工具,可以导出使用wireshark分析
4. anyproxy
    > 基于nodejs,跨平台,可扩展

## 弱网测试
1. clumsy 可模拟网络延迟、丢包、重发、篡改、乱序

## 内网穿透
1. 花生壳 收费
2. 基于ssh端口转发 临时使用
    ```bash
    ssh -N -R 9999:127.0.0.1:31112 ops1
    ```

3. ngrok 开源软件,go语言开发，需要在服务器安装。客户端使用简单

# DEBUG
1. xdebug php扩展
    ```
    export XDEBUG_CONFIG="remote_enable=1 remote_mode=req remote_port=9001 remote_host=10.0.75.1"
    ```
2. 通过ssh使php能连接远程不对外访问的数据库
    ```
    ssh -N -L 23306:172.18.128.245:3306 ops1
    ```
## 联调
1. 通过日志获取到请求参数重新请求
2. 前端开发人员复制请求curl发给后端同学，后端同学在Postman重新请求

# 日志记录
1. 日志记录关键数据，比如if条件判断时记录相关参数
    ```
    $taskStarted = $task->status === TaskStatus::STARTED;
    if ($taskStarted) {
        Log::info('task status ' . $task->status, ['task_id' => $taskId]);
    }
    ```
2. context 带上业务id，比如订单相关需要记录订单id
    ```
    Log::warning('order status ' . ORDER_STATUS, ['out_trade_no' => $outTradeNo]);
    ```

## 单元测试
1. 编写单元测试保障基础功能的正确性
2. 保证测试粒度足够小。单测粒度至多是类级别，一般是方法级别
3. 和数据库相关的单元测试，使用自动回滚机制
    ```php
    use DatabaseTransactions;

    private $connectionsToTransact = ['mysql-user'];
    ```

# 代码规范
* 注释
    * 使用DocBlock注释
    ```
    * 方法
        * 方法介绍
        * 限定方法参数类型和返回类型
        * 使用异常中断方法执行，不要根据返回类型/值判断，注释声明抛出异常类型和异常说明
        * 创建方法的同事姓名以及时间。
        * 修改方法的同事姓名以及时间与修改的内容。
        * 参数注释：类型、名称、参数说明。
        * 参数与其他注释之间要有空行。
        * 参数示例：如果参数当中有复杂的参数。可以在参数下方给出示例以增强说明。
        * 返回值。需要给出返回的类型。
    * 变量
        * 针对申明的变量进行介绍
    * 类
        * 针对整个类的介绍
    * 常量
        * 针对常量的介绍
        * 数据库字段类型可以枚举的使用类常量 const
        ```php
        final class BuyAuthType 
        {
            const WEIXIN = 0;
            const MOBILE = 1;
        }

        if ($buyAuthType === BuyAuthType::MOBILE) {}
        ```
    * 代码
        * 对请求参数进行验证
        * 不得使用 超过2层的条件判断或循环处理
        * if中判断过长使用变量分解加强可阅读性/封装成方法
        ```php
        function canBuy() 
        {
            // 商品是否在售
            $canBuy = $goods->status() === GoodsStatus::SALE;
            // 限制购买次数
            $canBuy = $canBuy && Goods::limitBuy();

            return $canBuy; 
        }
        ```
        * 级联调用使用data_get防止因数据导致异常
        ```php
        // $addressStatus = $user.order.address.status;
        $addressStatus = data_get($user, 'order.address.status', DEFAULT_VALUE);
        ```
        * 多余的注释必须删除，其中多余表示的是对于代码阅读无关紧要、代码的注释等。
        * 字符控制
            * 单个文件不超过1500行
            * 单个方法不超过80行
        * 命名规范
            * 变量/方法命名用单词或单词缩写
            * 变量多个单词统一用驼峰
            * 方法多个单词统一用驼峰
            * 更新方法使用 update 前缀
            * 删除方法使用 remove 或者 delete 前缀
            * 插入方法使用 save 或者 insert 前缀
            * 获取单个数据方法使用 get 前缀
            * 获取多个数据方法使用 list 前缀
            * 统计方法使用 count 前缀
            * 判断方法使用 is 前缀

# 数据库
1. 表达是与否概念的字段，必须使用 is_xxx 的方式命名，数据类型是 unsigned tinyint
（ 1 表示是，0 表示否）。
2. 软删除字段使用is_del 1表示删除,0未删除
3. 表名、字段名必须使用小写字母或数字，禁止出现数字开头，禁止两个下划线中间只
出现数字。数据库字段名的修改代价很大，因为无法进行预发布/灰度，所以字段名称需要慎重考虑
4. 表名不使用复数
5. 禁用保留字做为表名/字段名
6. 唯一索引名为 uk_字段名/unique_key_字段名；普通索引名则为 idx_字段名
7. 不使用float、double类型
8. 存储用户数据表如果需要使用text字段，独立出来一张表，用主键来对应，避免影响其它字段索引效率。
9. 业务上具有唯一特性的字段，即使是多个字段的组合，也必须建成唯一索引，避免脏数据的产生
10. 多表join查询 join列字段类型需要一致
11. 在varchar 字段上建立索引时，必须指定索引长度，没必要对全字段建立索引，根据实际文本区分度决定索引长度即可
12. 利用覆盖索引来进行查询操作，避免回表
13. 在代码中写分页查询逻辑时，若 count 为 0 应直接返回，避免执行后面的分页语句
14. 不使用字符串拼接 SQL 访问数据库，防止 SQL 注入

# 项目结构
1. web/controller 层：主要是对访问控制进行转发，各类基本参数校验，针对request、response、session、cookie等跟http协议有关，或者不复用的业务简单处理等。
2. Service 层：相对业务的具体实现,Service层跟通信协议无关。不使用web相关对象
3. Manager/Middle 层：通用业务处理层，对第三方平台的封装，统一的异常、缓存处理
4. Model/DAO 层：数据访问