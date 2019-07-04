const topicInput = document.querySelector('#input-topic-search')
const host = window.location.host

const awesomplete = new Awesomplete(topicInput, {
    minChars: 2,
    maxItems: 3,
    autoFirst: true,
})

const url = `http://${host}/api/topic/title/all`

fetch(url)
    .then((res) => {
        return res.json()
    })
    .then((result) => {
        awesomplete.list = result
    })


