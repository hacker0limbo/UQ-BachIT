const addNewBoard = () => {
    const url = `http://${host}/board/addjson`
    const newBoardBtn = document.querySelector('#id-newBoard')

    newBoardBtn.addEventListener('click', function(){
        const data = {
            title: document.querySelector('#message-text').value
        }
        fetch(url, {
            method: 'POST',
            body: JSON.stringify(data),
            headers: new Headers({
                'Content-Type': 'application/json'
            })
        }).then(res => res.json())
            .then(result => console.log('success'))
        window.location.reload()
    })
}

addNewBoard()