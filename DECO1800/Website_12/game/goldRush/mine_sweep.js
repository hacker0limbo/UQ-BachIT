// 我的库
var log = console.log.bind(console)

// querySelector() 函数返回的是一个元素节点, 未找到返回 null
var e = function(selector) {
    var element = document.querySelector(selector)
    if (element == null) {
        var s = `元素没找到，选择器 ${selector} 没有找到或者 js 没有放在 body 前面`
        alert(s)
    } else {
        return element
    }
}

// querySelectorAll() 返回的是一个数组, 所有匹配的元素节点
var es = function(selector) {
    var elements = document.querySelectorAll(selector)
    if (elements.length == 0) {
        var s = `元素没找到，选择器 ${selector} 没有找到或者 js 没有放在 body 前面`
        alert(s)
    } else {
        return elements
    }
}

// beforeend 插入元素内部的最后一个子节点之后。

var appendHtml = function(element, html) {
    element.insertAdjacentHTML('beforeend', html)
}

var bindEvent = function(element, eventName, callback) {
    element.addEventListener(eventName, callback)
}

// .classList以数组的形式返回一个元素的所有的类名, remove() 方法可以自动匹配
var removeClassAll = function(className) {
    var selector = '.' + className
    var elements = es(selector)
    for (var i = 0; i < elements.length; i++) {
        var e = elements[i]
        e.classList.remove(className)
    }
}

var bindAll = function(selector, eventName, callback) {
        var elements = es(selector)
        for (var i = 0; i < elements.length; i++) {
            var e = elements[i]
            bindEvent(e, eventName, callback)
        }
    }
    // find 函数可以查找 element 的所有子元素
var find = function(element, selector) {
    var e = element.querySelector(selector)
    if (e == null) {
        var s = `元素没找到，选择器 ${selector} 没有找到或者 js 没有放在 body 前面`
        alert(s)
    } else {
        return e
    }
}

var copySquare = function(square) {
    var a = []
    for (var i = 0; i < square.length; i++) {
        var s = square[i]
        var ss = s.slice(0)
        a.push(ss)
    }
    return a
}




// 创建扫雷数组
var plus = function(array, x, y) {
    if (x >= 0 && x < array.length && y >= 0 && y < array[0].length) {
        if (array[x][y] != 9) {
            array[x][y] += 1
        }
    }
}

var mark = function(array, x, y) {
    plus(array, x - 1, y - 1)
    plus(array, x - 1, y)
    plus(array, x - 1, y + 1)

    plus(array, x, y - 1)
    plus(array, x, y + 1)

    plus(array, x + 1, y - 1)
    plus(array, x + 1, y)
    plus(array, x + 1, y + 1)
}

var markedSquare = function(array) {
    var a = copySquare(array)
    for (var i = 0; i < a.length; i++) {
        for (var j = 0; j < a[i].length; j++) {
            if (a[i][j] == 9) {
                mark(a, i, j)
            }
        }
    }
    return a
}

var randomSquare00 = function(x, y) {
        var a = []
        for (var i = 0; i < x; i++) {
            a[i] = []
            for (var j = 0; j < y; j++) {
                a[i][j] = 0
            }
        }
        return a
    }
    // 随机布 n 个雷
var randomSquare09 = function(x, y, n) {
    var a = randomSquare00(x, y)

    var xlen = a.length
    var ylen = a[0].length
    for (var i = 0; i < n; i++) {
        var x = Math.floor(xlen * Math.random())
        var y = Math.floor(ylen * Math.random())
        if (a[x][y] == 9) {
            n++
        }
        a[x][y] = 9
    }
    return a
}

var number9 = function(array) {
    var n = 0
    for (var i = 0; i < array.length; i++) {
        for (var j = 0; j < array[i].length; j++) {
            if (array[i][j] == 9) {
                n++
            }
        }
    }
    return n
}

var markedSquare09 = function(a09) {
    // var a09 = randomSquare09(x, y, n)
    var s = markedSquare(a09)
    var n = number9(s)
    log('雷数', n)
    return s
}




// 创建点击事件
var selectTd = function(x, y) {
    var s = '_' + x + '_' + y
    var td = e(`#${s}`)
    return td
}

var getXY = function(td) {
    var id = td.id
    for (var i = 1; i < id.length; i++) {
        if (id[i] == '_') {
            var x = Number(id.slice(1, i))
            var y = Number(id.slice(i + 1))
        }
    }
    var a = [x, y]
    return a
}

var check = function(square, x, y) {
    if (x >= 0 && x < square.length && y >= 0 && y < square[0].length) {
        var n = square[x][y]
        var td = selectTd(x, y)
        var result1 = td.classList.contains('done')
        var result2 = td.classList.contains('mark')
        if (!result1 && !result2) {
            if (n == 0) {
                td.classList.add('done')
                checkRound(square, x, y)
            } else {
                td.classList.add('done')
                td.querySelector('span').classList.remove('hide')
            }
        }
    }
}

var checkRound = function(square, x, y) {
    check(square, x - 1, y - 1)
    check(square, x - 1, y)
    check(square, x - 1, y + 1)

    check(square, x, y - 1)
    check(square, x, y + 1)

    check(square, x + 1, y - 1)
    check(square, x + 1, y)
    check(square, x + 1, y + 1)
}


var insertRest = function(n) {
    var span = e('#id-li-rest')
    span.innerHTML = n
}
var insertTime = function(t) {
    var span = e('#id-li-time')
    span.innerHTML = t
}

var time = function() {
    var t = 0
    timeId = setInterval(function() {
        t++
        insertTime(t)
    }, 1000);
}


var click0 = function(square, td) {
    var a = getXY(td)
    var x = a[0]
    var y = a[1]
    td.classList.add('done')
    checkRound(square, x, y)
}
var click9 = function(td) {
    var tds = es('td')
    for (var i = 0; i < tds.length; i++) {
        if (tds[i].querySelector('span').innerHTML == 9) {
            tds[i].classList.add('nine')
        }
    }
    clearInterval(timeId)
    var table = e('table')
    table.classList.add('ban')
    alert('You Lose')
}
var clickElse = function(td) {
    td.classList.add('done')
    td.querySelector('span').classList.remove('hide')
}

var finish = function(n) {
    var tds = es('td')
    var m = 0
    var right = 0
    for (var i = 0; i < tds.length; i++) {
        var td = tds[i]
        if (!td.classList.contains('done')) {
            m++
        }
        if (td.classList.contains('mark')) {
            right++
        }
    }
    log('总雷数', n, '余雷数', n - right, '剩余未点击数', m)
    if (n == m) {
        clearInterval(timeId)
        var table = e('table')
        table.classList.add('ban')
        var t = document.querySelector('#id-li-time').innerHTML
        alert(`You win , takes ${t} seconds`)
    }
}

var judgeClick = function(m, square, td) {
    if (m == 9) {
        click9(td)
            // alert('扫雷失败')
    } else if (m == 0) {
        click0(square, td)
        log('click0')
    } else {
        clickElse(td)
        log('clickElse')
    }
}

var firstClickIs9 = function(a09, td, n) {
    var s = copySquare(a09)
    var a = getXY(td)
    var x = a[0]
    var y = a[1]
    for (var i = 0; i < s.length; i++) {
        for (var j = 0; j < s[i].length; j++) {
            if (s[i][j] != 9) {
                s[i][j] = 9
                break
            }
        }
        break
    }
    s[x][y] = 0
    var square = markedSquare09(s)
    insertTable(square, n)
    var td = selectTd(x, y)
    td.classList.add('done')
    td.querySelector('span').classList.remove('hide')
    if (td.querySelector('span').innerHTML == 0) {
        click0(square, td)
    }
}


var bindClick = function(square, n, a09) {
    bindAll('td', 'click', function() {
        var tds = es('td')
            // 获得被点数 num
        var num = 0
        for (var i = 0; i < tds.length; i++) {
            if (tds[i].classList.contains('done')) {
                num++
            }
        }
        if (num == 0) {
            time()
        }
        var td = event.target
        var m = td.querySelector('span').innerHTML
        if (num == 0 && m == 9) {
            firstClickIs9(a09, td, n)
        } else {
            if (!td.classList.contains('mark')) {
                judgeClick(m, square, td)
            }
            finish(n)
        }
    })
}

// 右击事件
var bindContextmenu = function(n) {
    bindAll('td', 'contextmenu', function() {
        event.preventDefault()
        var td = event.target
        if (!td.classList.contains('done'))
            td.classList.toggle('mark')

        var tds = es('td')
        var right = 0
        for (var i = 0; i < tds.length; i++) {
            var td = tds[i]
            if (td.classList.contains('mark')) {
                right++
            }
        }
        insertRest(n - right)
        log('总雷数', n, '余雷数', n - right)
    })
}



// 创建网页元素
var createTd = function(a, n) {
    var td = ''
    for (var i = 0; i < a.length; i++) {
        if (a[i] == 0) {
            td += `<td id="_${n}_${i}"><span class="zero hide">${a[i]}</span></td>`
        } else {
            td += `<td id="_${n}_${i}"><span class="hide">${a[i]}</span></td>`
        }
    }
    return td
}

var createTr = function(a, i) {
    var tds = createTd(a, i)
    var tr = `<tr>${tds}</tr>`
    return tr
}

var insertTable = function(square, n, a09) {
    var table = e('table')
    table.innerHTML = ''
    for (var i = 0; i < square.length; i++) {
        var tr = createTr(square[i], i)
        appendHtml(table, tr)
    }
    bindClick(square, n, a09)
    bindContextmenu(n)
    log('insertTable square', square)
}

var createTable = function(x, y, n) {
    insertRest(n)
    var a09 = randomSquare09(x, y, n)
    var square = markedSquare09(a09)
    insertTable(square, n, a09)
}


var selectLevel = function() {
    bindAll('.level', 'click', function() {
        if (typeof timeId != 'undefined') {
            clearInterval(timeId)
        }
        insertTime(0)
        var button = event.target
        var table = e('table')
        var id = button.id
        if (id == 'id-button-low') {
            table.innerHTML = ''
            table.classList.remove('ban')
            createTable(9, 9, 10)
        } else if (id == 'id-button-middle') {
            table.innerHTML = ''
            table.classList.remove('ban')
            createTable(16, 16, 40)
        } else {
            table.innerHTML = ''
            table.classList.remove('ban')
            createTable(16, 30, 99)
        }
    })
}




var __main = function() {
    // createTable(16, 30, 99)
    selectLevel()
    createTable(9, 9, 10)
}

__main()