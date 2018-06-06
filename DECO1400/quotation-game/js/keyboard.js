var allKeys = document.querySelectorAll('span');

const allQuotes = {
    a: a,
    b: b,
    c: c,
    d: d,
    e: e,
    f: f,
    g: g,
    h: h,
    i: i,
    j: j,
    k: k,
    l: l,
    m: m,
    n: n,
    o: o,
    p: p,
    q: q,
    r: r,
    s: s,
    t: t,
    w: w,
    y: y,
}

// functions
var toogleClass = (element, containedClass, class1, class2, method) => {
    var parentClassList = element.parentNode.classList
    if (parentClassList.contains(containedClass)) {
        parentClassList[method](class1)
    } else {
        parentClassList[method](class2)
    }
}

var palySound = () => {
    var audio = document.querySelector('audio')
    audio.play()
}

window.addEventListener('keydown', (event) => {
    var k = event.key
    var allQuotesArr = Object.keys(allQuotes)

    // play source
    palySound()

    // change style of keyboard
    for (var keySpan of allKeys) {
        var eachKey = keySpan.textContent
        if (k == eachKey.toLowerCase()) {
            toogleClass(keySpan, 'none-highlight', 'not-highlight', 'highlight', 'add')
        }
    }

    // show the quotes
    var quotes = document.querySelector('h1')
    for (var quote of allQuotesArr) {
        if (k == quote) {
            quotes.innerHTML = allQuotes[quote]
            quotes.classList.remove('animated')
            setTimeout(() => {
                quotes.classList.add('animated')
            }, 0)
        }
    }
})

window.addEventListener('keyup', (event) => {
    var k = event.key
    var allQuotesArr = Object.keys(allQuotes)

    for (var keySpan of allKeys) {
        var eachKey = keySpan.textContent
        if (k == eachKey.toLowerCase()) {
            toogleClass(keySpan, 'none-highlight', 'not-highlight', 'highlight', 'remove')
        }
    }
})
