const warDataFromLocal = (name) => {
    warData = window.localStorage.getItem(name)
    data = JSON.parse(warData)
    console.log(data);
    return data
}

data = warDataFromLocal('war')

for (let i = 0; i < 7; i++) {
    let reocrd = data[i]
    let imgSrc = reocrd['150_pixel']
    let info = reocrd['decsription']
    if (imgSrc == '' || info == '') {
        continue
    }
    console.log(imgSrc, info);
    container = e('#articles_container')
    console.log(container);

    const html = `
        <section class="article">
            <section class="headline">
                Headline
            </section>
            <img src=${imgSrc} class="image">
            <p>
                ${info}
            </p>
        </section>
    `

    container.insertAdjacentHTML('beforeend', html)
}