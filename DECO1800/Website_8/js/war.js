const warDataFromLocal = (name) => {
    warData = window.localStorage.getItem(name)
    data = JSON.parse(warData)
    return data
}

var insertData = () => {
    data = warDataFromLocal('war')
    console.log(data);

    newData = data.filter((elem) => {
        return elem['150_pixel'] && elem['title'] && elem['decsription']
    })

    var singlePages = document.querySelectorAll('.single-p')
    console.log(singlePages);

    for (var i = 0; i < singlePages.length; i++) {
        var singlePage = singlePages[i]
        var d = newData[i]
        var imgSrcSmall = d['150_pixel']
        var imgSrcLarge = d['1000_pixel']
        var title = d['title']
        var des = d['decsription']

        var html = `
            <div class="portrait">
                <a href="${imgSrcLarge}" 
                    class="strip" 
                    data-strip-caption="Soldier Portrait"
                    data-strip-group="mygroup">
                
                    <img src="${imgSrcSmall}">
                </a>
            </div>
            <div>
                <h3>Title:</h3>
                <p class="animated slideInDown">${title}</p>
            </div>
            <div>
                <h3>Decsription:</h3>
                <p class="animated zoomIn">${des}</p>
            </div>
    `
        singlePage.insertAdjacentHTML('beforeend', html)
    }
}


insertData()