const convictDataFromLocal = (name) => {
    warData = window.localStorage.getItem(name)
    data = JSON.parse(warData)
    console.log(data);
    return data
}

data = convictDataFromLocal('convict')

for (let i = 0; i < 3; i++) {
    let reocrd = data[i]
    let headline = reocrd['ConvictName']
    let info = reocrd['Sentencedetails']
    if (headline == '' || info == '') {
        continue
    }
    // console.log(imgSrc, info);
    container = e('#articles_container')
    console.log(container);

    const html = `
        <section class="article">
            <section class="headline">
                ${headline}
            </section>
            <img src='' class="image">
            <p>
                ${info}
            </p>
        </section>
    `

    container.insertAdjacentHTML('beforeend', html)
}