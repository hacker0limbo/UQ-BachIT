# infs3202 期末整理

## L2

### WIS
What is Web information system:
- Web information system is an information system that uses Internet Web techologies to deliever information and services, to users or other information applications
- It is a software system whose main purpose is to publish and maintain data by using hypertext-based principles

WIS Architecture(分层架构模式)
- Traditional(one-tier) architecture
- Compoment-based(n-tier) architecture
- Service-oriented architecture

1. Traditional(one-tier) architecture: combined everything into a single program
Client-Server Architecture

2. Component-based N-Tier architecture
将功能划分为不同的层(Decompose functionalitie into layers)
    - Presentation Layer(表现层): layer sends content to browser(html, css, js)
    - Business Layer(业务层): implements business rules and process(实现业务逻辑)
    - Data Acess Layer(数据层): data management, store information in database
    
一般为 3-n tier 类似 mvc, 好处如下:
    - easy to maintain: each layer is independent
    - high performance: cache request
    - saclability(延伸性): application server can be deployed on many machines
    - security: users have no access to databse

### protocol

- HTTP(HyperText transfer protocol): the protocol used to transfer web pages through the internet
- TCP(Transmission Control Protocol, 传输控制协议): A reliable connection-oriented transport service that provides end-to-end reliablity
- UDP(User datagram Protocol, 用户数据报协议): conncetionless transport service
- IP(Internet Protocol Address, 互联网协议地址)
- FTP(File Transfer Protocol)


TCP/IP architectureal modal:
- Application layer(应用层): http, ftp
- Transport layer(传输层), end-to-end: tcp, udp
- Internet layer(网络层): ipv4, ipv6
- Link layer(链路层): mac

## L3&L4

### cookie
what is cookie:
- created by the server
- stored on user's computer
- used to identify a user
- sent to the server with a page request

php中设置cookie:
```php
// setcookie(name, value, expire, path, domain, secure);
// time()+3600 3600 seconds
// time()+3600*24 24 hours
<?php 
setcookie("admin", "a");

echo $_COOKIE["user"];
?>
<html><body>
```

### session
what is session:
- store information in variables to be used accrossmutiple pages
- session variable hold information about one single user, and are available to all pages in one application
- session information is stored in server side and will be deleted after the user has left the website(close the browser)

php 中使用 session
```php
session_start();
// 删除所有的 session 记录
session_destroy();
if (isset($_SESSION["views"])) {
    // 删除指定的 session
    unset($_SESSION['views']);
} else {
    $_SESSION["views"] = 1;
}
```

一个使用 session 完成登录的例子:

```php
/*
三个页面
1, loginform_session.php 包含了登录表单
2, login_session.php 设置 session
3, gallery.php 用户提交表单以后会前往的网页

*/

// loginform_session.php
<?php 
// 如果用户在登录状态下访问了该表单页面, 直接免登陆重定向到 gallery.php
session_start();
if (isset($_SESSION["username"] && isset($_SESSION["password"])) {
    header("Location: gallery.php");
}    
?>
<html>
...
<form metho="POST" action="login_session.php">
    ...
</form>
</html>

// login_session.php
<?php 
session_start();
$username = $_REQUEST["username"];
$password = $_REQUEST["password"];

if ($username == 'abc' && $password == 'efg') {
    // 登录成功, 识别了用户信息, 加入 session
    $_SESSION["username"] = "abc";
    $_SESSION["password"] = "efg";
    
    // 设置完毕, 前往页面
    header("Location: gallery.php");
} else {
    // 用户名密码错误, 返回登录页面
    header("Location: login_session.php");
}
?>

// gallery.php
如果用户直接访问了该页面, 需要做判断是否登录(因为登录了就说明添加了 session)
session_start();
// 如果没有设置 session, 说明没有登录, 重定向到登录页面
if (!isset($_SESSION["username"] || !isset($_SESSION["password"])) {
    header("Location: login_session.php");
}
<html>
...
</html>

```

Difference between session and cookie:
- cookie is stored in user's hard disk, session stored in server side
- a cookie can keep information in user's browser until deleted or expired, session will not be available once the browser is closed
- if set cookie, you dont have to log in next time, if you set session variable, you still have to log in next time you open your browser
- session is like tokens, for authentication
- sessions are more popular used, cookie could be blocked if user browser security is high


### 文件
- $file = fopen("text.txt", "r")
- fgets($file)
- fclose("text.txt")
- fwrite("$file", "something")
- feof()
- file_exists()

上传文件

```html
<form action="upload_file.php" method="post" enctype="multipart/form-data">
    <label for="file">文件名：</label>
    <!-- 如果是多个文件上传的话需要加上 mutiple 属性, 并且 name 属性需要写成 array 的格式, 例如下面的 file[] -->
    <input type="file" name="file[]" id="file" multiple="multiple"><br>
    <input type="submit" name="submit" value="提交">
</form>
```

- $_FILE["file"]["name"] (如果是一个多文件就是一个数组)
- move_uploaded_file($_FILE["file"]["tmp_name"], $destionation)

### 邮件
```php
// 可以直接使用 mail() 函数发送邮件
<?php 
$to = "someone@example.com";
$subject = "Test mail";
$message = "Hello! Testing!";
$from = "someonelse@example.com";
$headers = "From:" . $from;
mail($to, $subject, $message, $headers);
echo "Mail Sent.";
?>

// 当然也可以使用在页面构建一个表单来发送
比如 $to = $_REQUEST["to"];
...
```

### 数据库
- DML: select, update, delete, insert into(增删改查)
- DDL: create databse, alter database, create table, alter table...

php 中操作数据库
```php
<?php
class MySQLDatabase {
    public $link = null;
    
    function connect($user, $password, $database) {
        $this->link = mysqli_connect('localhost', $user, $password);
        if ($this->link) {
            die("error");
        }
        // 选择数据库
        $db = mysqli_select_db($this->link, $database);
        if (!$db) {
            die ('Cannot use : ' . $database);
        }
        return $this->link;
    }
    
    function disconnect(){
        mysqli_close($this->link);
    }
}
?>
// 使用连接
include('connectMySQL.php');
$db = new MySQLDatabase();
$conn = $db->connect(“yourName”, “yourPassword”, “yourDatabase”);

// 插入数据
$query = "insert into studentRecord (studentName, ID) values ('John Smith',
'04123412')";
// db->$link 和 $conn 一样的
$result = mysqli_query($conn, $query); // 或者用 $db->link
if (!$result) {
    die(mysqli_error($db->link)); // useful for debugging
}

// 查找数据
$query = "select studentName, ID from studentRecord";
$result = mysqli_query($db->link,$query);
if ($result) {
    while ($row = mysqli_fetch_array($result)) {
        print "Name: {$row['studentName']} has ID: {$row['id']}";
    }
}
else {
    die(mysqli_error($db->link)); // useful for debugging
}

// 关闭数据库
$db->disconnect();
```

## L4

### xml
定义: eXtensible Markup Language 可扩展标记性语言
和 html 的区别是: html is about to displaying information, xml is about to describing information 
- html: diplay data
- xml: transport and store data

例子: 
```xml
<?xml version=“1.0” encoding="UTF-8"?>
<!-- my first XML doc -->
<courselist>
    <course level="medium">
        <lecturer>
            <firstname>H.</firstname>
            <lastname>Huang</lastname>
        </lecturer>
        <title>Web Information Systems</title>
        <code>INFS3202/INFS7202</code>
    </course>
</courselist>

<!-- 当然上面也可以写成下面这种, 推荐使用元素形式 -->
<course>
    <level>medium</level>
</course>
```

### JSON
定义: JavaScript Object Notation

- JSON.parse() 解析 json 字符串
- JSON.stringfy() 将对象转换为 json 字符串

### NOSQL

概念对应(sql: nosql):
- databse: databse
- tables: collections(一系列对象的集合)
- rows: documents(文档), 就是一个一个对象, 可以有 curd
- columns: fields(前面的 key)

### AJAX
定义: Asynchronous JavaScript And XML

创建一个 ajax:
```javascript
function loadXMLDoc() {
    var xmlhttp
    if (window.XMLHttpRequest) {
        // 查看是否支持
        xmlhttp = new XMLHttpRequest()
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("myDiv").innerHTML = xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET", "ajax_info.txt", true) // true 表示 async 异步
    xmlhttp.send()
}
```

## L7 Cloud computing
定义: A form of distributed computing that introduces models for remotely provided scalable and measured resources

Cloud: A distinct IT environment that is designed for the purpose of remotely provisioning scalable and measureable IT resources

特点:
- On-demand usage: Cloud users has freedom to self-provision cloud's it recources, usage is automated once being configured
- Accessable: wiredly access
- mutiple users: serve different consumers
- flexiable: auto scale IT resources
- Mesured usage: keep track of usage and report billing and usage to users

### Cloud delivery(云计算提供模式)
- IaaS: infrastructure-as-a-server(基础设施即服务)
- paaS: platform-as-a-server(平台即服务)
- saaS: software-as-a-server(软件即服务)

IaaS: 
- 基本的 it 资源(infrastructure), hardware, network, operating system
- high level control
- initialized virtual machines
- users are system admins
- different CPU cores, ram 等等(自选)
e.g: Amazon EC2(AWS), Google Compute Engine(GCE), Microsoft Azure

PaaS:
- read to use environment(already deployed and configured IT resources)
- programming language environment, operating system, web server, database
- user dont need to worry about infrastructure
- user have to manage their own data
- low level contorl of it resources
e.g: Amazon Web services, Google app engine(GAE), Microsoft Azure

SaaS:
- shared cloud service product
- on-demand services
- accessible via a web browser
- be avilable for multiple users
- limited contorl
e.g: google docs/mail microsoft office 365

### Advantages & Limitations

Advantages:
- Low in cost(便宜)
- Improved performance(性能)
- Improved reliability(可靠)
- Universal access to data(访问权限)
- Device independent(独立)

Limitations
- Functions available might be limited
- Privacy issues
- Limitation of internet connection bandwidth

## L8 SOA

service oriented architecture

definition: a style of software design where services are provided to the other compoments by application components, through a communication protocol over a network

例子: socket+rpc, restful(http+json)

web service:
- A way to communicate(SOAP): 需要协议来约束如何访问 web 服务
- A way to descirbe services(WSDL, web service description language), 需要一种语言来描述你提供的 web 服务, e.g. xml
- A name and directory server(UDDI), 一个平台, 你可以发布你的 服务

现在更加常用的是使用 web api(aplicaiton programming interface)

api 优势: 
- 可以是所有任何语言描述, 比如 json, xml
- open source
- 支持协议更加多


## L9 mobile
两种方式: 
- Native: 使用原生方式, 比如 swift
- Hybrid: 使用 web 方式写 app, 在一个原生 app 里面开启一个 web 应用

Hybrid-Native: React Native
- 非 browse-based app, 无法做到写一次, 运行多个平台, 还是需要根据不同的平台修改一定的代码, 测试等
- 对于不同的平台, 会有不同的组件要求, 相应会投入更多的经历

Hybrid-Web: Ionic
- 写一次, 运行多个平台, 属于混合软件
- browse-baed app, 一次写, 多个平台都可以运行
- 但是性能会有问题


## L12 Security

### sql injection

定义: accepts user input and uses it as a part of sql statement to query a backend daabase

比如一个登陆页面有 username 和 password 需要填
如果在 username 里面填入: charles' -- 
那么 sql 代码为: 
```sql
SELECT * FROM user WHERE name=‘Charles’ -- ‘ AND passwd=‘ ’
```
即 -- 'AND passwd='' 全部被注释, 只匹配了 username, 免密码登陆


一些应对方法:
1. 使用 regular expression 过滤非法字符
2. 对参数进行验证, 是否符合类型等
3. 使用框架等

### Cross Site scripting(xss) 跨站脚本攻击
定义: attacker injects client-side script into the content, and viewd by other users

防范方法:
- 对于用户输入的东西进行检查
- 一些标签/属性检查
- 特殊字符串检查


### Broken authentication & session management
- 使用 https 而不是 http
- 数据库密码等存取进行加密处理
- 加盐(salt)
- RSA
- Digital Signature

### CSRF 跨站请求伪造

原理:
1. 登录受信任的网站 A, 并生成 Cookie
2. 在不登出 A 的情况下, 访问危险网站 B
B 网站在访问的时候可能会发送一些请求到 A 网站, 然后此时 cookie 还存在, 就冒用了你的信息进行了操作


其他的 attack: 
- Drive-by attack.
- Password attack.
