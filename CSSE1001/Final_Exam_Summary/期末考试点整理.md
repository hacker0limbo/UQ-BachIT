
# csse1001 期末考试知识点整理

该篇是我做`1001`考试卷整理出来的部分易错点, 有些知识点没有完全展开, 只是大概讲了讲, 原理还是需要自己谷歌, 毕竟应付考试为根本. 本篇文章仅供参考, 如有错误, 欢迎指出, 还请见谅!

## 优先级问题:
    
or < and < not


```python
a = False and False or True # True
b = True or False and False # True
print(a, b)
print(1 < 2 and not 2 > 3) # True
```

## 常考内置函数整理

### `split()`

`str.split(str="", num=string.count(str))`

- str: 分隔符, 默认为所有的空字符, 包括空格, `\n`, `\t`
- num: 分割次数

如果分割一个不存在的符号, 将该字符串转换为一个列表返回


```python
s = 'a bc]'
print(s.split(']')) # ['abc', '']
print(s.split('[]'))
```

### `find()`

`str.find(str, beg=0, end=len(string))`

- str 指定检索的字符串
- beg 开始检索的位置, 默认为 0
- end 结束检索的位置, 默认为字符串长度

从 beg 开始检索, 只要找到就返回该检索字符串的位置, 否则返回 -1


```python
s = 'abc d'
print(s.find(' '))
```

### `insert()`

`list.insert(index, obj)`

- index 要插入的对象所要插入的位置
- obj 要插入到列表中的对象

注意该方法无返回值(None), 如果`index`超出列表长度, 默认在最后插入


```python
l = [1, 2, 3]
print(l.insert(6, 4)) # None
print(l) # [1, 2, 3, 4]
```

### `join`

`str.join(sequence)`

sequence: 需要连接的元素序列, 常见形式为列表, 元组


```python
t = ('a', 'b', 'c')
print(':'.join(t)) # a:b:c
print(''.join(t)) # abc
```

## 返回值, 可变对象与不可变对象

1. 列表, 字典为可变对象, 元组为不可变对象. 字典的`key`只能是不可变对象, 因此列表无法作为`key`, 但是元组, 字符串, 数字都可以作为`key`
2. `list.append()`, `list.extend()`, 返回值均为`None`. `l.pop()`有返回值.
3. 列表为可变对象, 对于类似`.append()`, `+=` 均为在原本地址上操作, `l = l + []` 会这种生成一个新的地址, 例子如下


```python
l = [1, 2, 3]
l.append(4)
print(l, id(l)) # id 未变
l += [5]
print(l, id(l)) # id 未变

l = l + [6]
print(l, id(l)) # id 改变
```

## 指针赋值

`python`中一切都是指针, 同时可以由多个变量名指向同一个指针, 注意指针里保存的数据是否为可变变量, 通过一个变量名修改指针数据另一个变量名也会受到反馈


```python
a = 6
b = a
b = 7

print(a, b) # 6 7

x = [1, 2]
y = x
y.append(3)
print(x, y) # [1, 2, 3] [1, 2, 3]
```

## 全局变量和局部变量

- 函数内部任意地方有赋值, 这个地方为局部变量, 即使外面又重名变量也无关
- 如果函数内部没有赋值, 函数外面又赋值, 那么可以使用外面的变量, 即为全局变量
- 如果想要在函数内部修改全局变量需要使用 `global`


```python
x = 100

def f():
    x = 10

f()
print(x) # 100
```


```python
x = 100

def f():
    global x
    x = 10
    
f()
print(x) # 10
```


```python
x = 100

def f():
    x += 10
    
f() # 报错
```

## 字典 d.get() 和 d[k] = v 区别

`dict.get(key, default=None)`

- key: 字典中要查找的键
- default: 如果要查找的键的值不存在, 返回默认值, 默认为 None
    
与`d[k]`的区别为`d[k]`找不到会直接报错


```python
d = {
    1: 1,
    2: 2
}

a = d.get(1)
b = d.get(3, {})
c = d.get(4)
print(a, b, c) # 1, {}, None

print(d[4]) # 报错
```

## 列表推导

举例, 如`[(x + y) for x in [1, 2, 3] for y in [4, 5, 6] if (x + y) > 0]`


```python
l = [(x + y) for x in [1, 2, 3] for y in [4, 5, 6] if (x + y) > 0]
print(l)
```


```python
# 转换为如下循环结构:

l = []
for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        if x + y > 0:
            l.append(x+y)

print(l)
```

## 对象的布尔值

`Python`中所有对象可以使用`bool()`进行真值测试, 列出对象是`False`的对象

- None
- False
- 0, 0.0
- 空序列, 包括 `''`, `[]`, `()`
- 空字典 `{}`
- 自定义对象, 该对象的`__bool__`返回`False`或者`__len__`方法返回0

除了以上的情况外，所有的对象在`i`f或者`while`语句中的表现都为真

## 元组单元素写法

当元组里面的元素只有一个的时候需要加上逗号以区分, 否则会被认为是一个数字, 因为数字外面可以随意加括号

同时, 元组, 列表均可以相加, 对象是否可以相加取决于他们内部有没有`__add__`


```python
a = (1,) # 元组
b = (2) # 数字

print(a + (3, 4)) # (1, 3, 4)
print(a + b) # 报错, 不同类型无法相加
```

## 表达式计算

- 浮点型 与 整型计算的表达式, 返回浮点型
- 字符串之间可以进行比较, 比较的是`s[0]`的`ASCII`码的大小, 可以使用`ord()`函数查到字母的码值, `a` < `b`


```python
print((4.4 + 6.6) // 2) # 5.0
print((2.0**3) % 3) # 2.0
print(ord('B')) # 66
```

## 切片

当第三个参数为 -1 的时候可以倒着切, 同时当索引超出切片长度的时候默认切到最后一个


```python
s = 'abcd'

print(s[2:0:-1]) # cb
print(s[-2:-6:-1]) # cba
```

## 参数传递

在`Python`中, 向函数中传递参数时遵循**"pass by assignment"**, 即在传递参数时，只是创建一个指向对象的引用，之后将这个引用赋值给函数参数中的形参, 例子如下


```python
def foo(n):
    n = 10 
    
x = 1
print(x) # 1

foo(x)
print(x) # 1
```

`x = 1`创建了一个引用, 该引用指向 1 这个对象, 然后该引用地址被保存到`x`变量里面. 传递给函数`foo`的时候, 又将这个引用传递给了`n`这个形参, 即此时`x = n => 1`. 在函数体内, 创建了一个新的引用 10, 将形参`n`指向了该新的引用, 因此执行完以后对`x`没有影响.

由于 1 是不可变变量, 如果传递的是可变变量, 可能造成对引用的修改, 如下:

这里`a`, `l`均指向了`[]`, 即`a = l = []`, 由于列表为可变对象, 对任何一个变量修改都直接修改引用


```python
def bar(a):
    a.append(1)
    
l = []
bar(l)
print(l) # [1]
```

当然也有可能出现传入可变对象不发生修改的情况, 如下:

在这种情况下尽管传递的是可变对象, 但是由于地址不同因此对原列表无影响.


```python
def f(a):
    print('before', id(a)) # 和 l 指向的地址一样
    a = a + [8]
    print('after', id(a)) # 地址修改了, 但此时 l 仍旧指向原地址
    
l = []
print('id l', id(l))
f(l)
print('l', l) # []
```

## 列表题目总结

### 2018.s1


```python
def f(l, a, b) :
    l.append(a)
    l = l + [b]
    return l

x = [5, 9]
x = f(x, 2, 1) + x

print(x) # [5, 9, 2, 1, 5, 9, 2]
```

解析:

1. `x = l = [5, 9]` (形参和 x 均指向同一个引用地址)
2. 执行`f(x, 2, 1)`:
    - `l.append(a)` => `l = x = [5, 9, 2]`
    - `l = l + [b]` => `l = [5, 9, 2, 1]`, `x = [5, 9, 2]` (形参指向新的地址, x 指向地址不变)
    - `f(x, 2, 1)`返回`[5, 9, 2, 1]`
3. `[5, 9, 2, 1]` + `[5, 9, 2]` = `[5, 9, 2, 1, 5, 9, 2]`为最后结果

### 2017.s2


```python
def g(p):
    z = p.pop(0)
    p.extend(z)
    return p

y = ['h', 'i', 'j']
g(y).extend(g(y[:]))

print(y) # ['i', 'j', 'h', 'j', 'h', 'i']
```

解析:
    
1. 执行`g(y)`, `y => ['i', 'j', 'h']`
2. 执行`.extend(g(y[:]))`
    - 先浅拷贝一份`y`, `y`地址不变, `y[:] =['i', 'j', 'h']`, 但是此时`y[:]`和`y`地址不同
    - `g(y[:])`, `g[:] => [j', 'h', 'i']`, `y`不变
3. 拼接`y`和`y[:]`, `['i', 'j', 'h'] + [j', 'h', 'i'] = ['i', 'j', 'h', 'j', 'h', 'i']`

### 2017.s2


```python
def f(x, y):
    y = y + [x]
    return y 

a = [2,1]
a = f(1,a) + 2*a

print(a) # [2, 1, 1, 2, 1, 2, 1]
```

解析:

1. `a = y => [2, 1]`
2. 执行`f(1, 2)`
    - `y => [2, 1, 1]`, `a` 不变, 仍旧指向`[2, 1]`
3. 执行`2*a`返回`[2, 1, 2, 1]`
4. 拼接结果

### 2015.s1


```python
y = [1, 2, 3, 4]
z = y + [y.pop(2)] + [y.pop(1)]

print(z)
```

解析:

1. 执行`y + [y.pop(2)]`:
    - 返回`[1, 2, 4, 3]`, 此时`y = [1, 2, 4]`
2. 执行`y.pop(1)`:
    - 返回 `2`, 此时`y = [1, 4]`
3. 将上面返回值相加, `[1, 2, 4, 3] + [2] = [1, 2, 4, 3, 2]`

## super() 和 self

- `super()`其实不代表父类, 代表的是当前类在`MRO`列表里面的下一个类, 多数情况下可以认为是父类
- `super()`其实在`python2.x`里面写作`super(cls, self)`, 可以使用他去调用父类的方法, 但是`self`还是指的是子类实例


```python
class X:
    def __init__(self):
        self.x = 10

    def f(self):
        return self.x


class Y(X):
    def __init__(self):
        self.x = 100

    def b(self):
        return super().f()

x = X()
y = Y()
print(y.b()) # => 100
```

这里的`super().f()`里面的`self`指代的是`y`, 同时, 这段代码等同于`self.f()`
