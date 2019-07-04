<?php
    $name = "fsdaf";
    echo "fdsaf {$name}";
?>

<?php
    // echo 语句可以进行插值, 可以输出多个字符串, 使用 , 进行分隔
    $a = 5;
    $names = array("a", "b");
    $myName = "myname";
    echo "aaa{$a}, {$names[0]}" . "hkfdsaf", "wtf";
    
    // strlen() 返回字符串的长度
    echo strlen($myName); // 6
?>

<?php 
    // var_dump 可以返回变量的数据类型和值
    var_dump($names);
?>

<?php 
    // 非关联数组
    $myNames = array("x", "y", 'z');
    
    // 遍历数组
    // 传统方法
    for ($i = 0; $i < count($myNames); $i++) {
        echo $myNames[$i];
    }
    // foreach 方法
    foreach ($myNames as $k => $v) {
        echo "{$k}: {$v}"; // 0: x, 1: y, 2: z
    }
    // 或者直接取值
    foreach ($myNames as $myName) {
        echo $myName; // x, y, z
    }
    
    // 关联数组
    $ages = array("a" => 10, "b" => 20, "c" => 30);
    $ages["d"] = 40;
    echo $ages["d"]; // 40
    // for each 遍历
    foreach ($ages as $name => $age) {
        echo "{$name}: {$age}";
    }
?>

<?php 
    // 函数
    function add($x, $y) {
        return $x + $y;
    }
    
    echo add(1, 2); // 3
?>

<?php 
    // 对象
    class Person {
        public $name;
        private $age;
        private $birthYear;
        
        function __construct($name, $age) {
            // 这里注意属性前面无 $ 符号
            $this -> name = $name;
            $this -> age = $age;
            $this -> setBirthYear();
        }
        
        public function speak($content) {
            echo $this -> birthYear;
            echo "{$this->name} said {$content}";
        }
        
        private function setBirthYear() {
            $this -> birthYear = 2019 - ($this -> age);
        }
    }
    
    $p1 = new Person("xiaoming", 60);
    $p1->speak("Hello");
    
    // 子类继承
    class Man extends Person {
        public $gender;
        
        function __construct() {
            // 调用父类构造方法
            parent::__construct($name, $age);
            $this -> gender = "male";
        }
    }
    
    $m1 = new Man();
    echo $m1 -> gender; // male
?>

<!-- 表单 -->
<form action="handle.php" method="post">
    name: <input type="text" name="username">
    age: <input type="text" name="age">
    <input type="submit" value="submit">
</form>

<?php 
    // GET 类似
    echo $_POST["username"];
    echo $_POST["age"];
?>


<!-- 文件上传 -->
<!-- 
<form> 标签的 enctype 属性规定了在提交表单时要使用哪种内容类型。
在表单需要二进制数据时，比如文件内容，请使用 "multipart/form-data 

<input> 标签的 type="file" 属性规定了应该把输入作为文件来处理。举例来说，当在浏览器中预览时，会看到输入框旁边有一个浏览按钮
-->
<form action="upload_file.php" method="post" enctype="multipart/form-data">
    <label for="file">文件名：</label>
    <input type="file" name="file" id="file"><br>
    <input type="submit" name="submit" value="提交">
</form>

<?php 
// $_FILES["file"]["name"] 上传文件的名称
// $_FILES["file"]["error"] 存储在服务器的文件的临时副本的名称
    if ($_FILES["file"]["error"] > 0) {
        echo "错误：" . $_FILES["file"]["error"] . "<br>";
    } else {
        echo "上传文件名: " . $_FILES["file"]["name"] . "<br>";
        echo "文件类型: " . $_FILES["file"]["type"] . "<br>";
        echo "文件大小: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
        echo "文件临时存储的位置: " . $_FILES["file"]["tmp_name"];
        
        // 判断当期目录下的 upload 目录是否存在该文件
        // 如果没有 upload 目录，你需要创建它，upload 目录权限为 777
        if (file_exists("upload/" . $_FILES["file"]["name"])) {
            echo $_FILES["file"]["name"] . " 文件已经存在。 ";
        } else {
            // 如果 upload 目录不存在该文件则将文件上传到 upload 目录下
            move_uploaded_file($_FILES["file"]["tmp_name"], "upload/" . $_FILES["file"]["name"]);
            echo "文件存储在: " . "upload/" . $_FILES["file"]["name"];
        }
    }
?>


<?php 
    // cookie 和 session
    // cookie 是一种服务器留在用户客户端上的小文件, 每当用户客户端浏览器请求服务器时, 该客户端都会发送 cookie
    setcookie("user", "abcd", time()+3600);
    // 启动 session
    session_start();
    $_SESSION['views'] = 1;
    // 可以用 isset 来查看是否设置了 cookie
    if (isset($_COOKIE["user"])) {
        echo $_COOKIE["user"];
    } else {
        echo "no";
    }
    
    // session 存于客户端的信息
    // 为每个访客创建一个唯一的 id (UID)，并基于这个 UID 来存储变量。UID 存储在 cookie 中，或者通过 URL 进行传导
?>
<!-- html 头部 -->
<!-- <html>... -->


<?php 
// 数据库
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";


// 面向对象
$conn = new mysqli($servername, $username, $password, $dbname);
// 面向过程
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
} 
 
$sql = "SELECT id, firstname, lastname FROM MyGuests";

// 这里如果是插入数据的话, $result 是 TRUE 表示插入成功
// 面向对象
$result = $conn->query($sql);
// 面向过程
$result = mysqli_query($conn, $sql);

if ($result->num_rows > 0) {
    // 输出数据
    while($row = mysqli_fetch_array($result)) {
        echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
    }
} else {
    die (mysqli_error($link));
}


?>

<!-- 文件 -->
<?php 
// 读一个文件
if (!file_exists("test.txt")) {
    exit("no file"); // 输出一段信息, 退出脚本
}
// 打开文件, 读模式
$file = fopen("test.txt", "r");
// feof 检查是否到了行尾
while (!feof($file)) {
    // fgets 可以逐行读取一个文件
    echo fgets($file) . "<br / >";
}
fclose($file);

// 写一个文件
$file = fopen("test.txt", "w");
// fwrite 会返回写入的字符串的数量, 这里为 8
echo fwrite($file, "content ");
?>
