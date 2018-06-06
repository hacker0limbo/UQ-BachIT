var audio = e('.audio-player')
var playButton = e('#id-play-button')
var pauseButton = e('#id-pause-button')
var selector = '.audio-circle'
var preButton = e('#id-pre-button')
var nextButton = e('#id-next-button')
var source = e('source')


var checkPlaying = () => {
    var musicList = e('.music-list')
    var lists = musicList.children

    for (var eachList of lists) {
        var eachMusicText = eachList.innerHTML
        eachMusicText = eachMusicText.split(' ').join('-')
        var eachSrc = 'musics/' + String(eachMusicText) + '.mp3'
        if (eachList.classList.contains('playing')) {
            removeClass(eachList, 'playing')
        }
        if (eachSrc == getRelativeSrc(source)) {
            addClass(eachList, 'playing')
        }
    }
}

var checkButton = () => {
    removeClass(playButton, "button-hide")
    addClass(playButton, "button-hide")
    removeClass(pauseButton, "button-hide")
}

var autoPlay = () => {

    bindEvent(preButton, 'click', () => {
        checkButton()
        playAnimation()
        var index = parseInt(audio.dataset.index)
        var size = musics.length
        source.src = musics[(index + 2) % size]
        audio.src = musics[(index + 2) % size]
        audio.dataset.index = (index + 2) % size
        audio.autoplay = true
        audio.play()
        checkPlaying()
    })

    bindEvent(playButton, 'click', () => {
        toggleClass(playButton, "button-hide")
        toggleClass(pauseButton, "button-hide")
        playAnimation()
        audio.play()
        checkPlaying()
    })

    bindEvent(pauseButton, 'click', () => {
        toggleClass(pauseButton, "button-hide")
        toggleClass(playButton, "button-hide")
        stopAnimation()
        audio.pause()
        checkPlaying()
    })

    bindEvent(nextButton, 'click', () => {
        checkButton()
        playAnimation()
        var index = parseInt(audio.dataset.index)
        var size = musics.length
        source.src = musics[(index + 1) % size]
        audio.src = musics[(index + 1) % size]

        audio.dataset.index = (index + 1) % size
        audio.autoplay = true
        audio.play()
        checkPlaying()
    })

    bindAll(selector, 'click', (event) => {
        checkButton()
        playAnimation()
        var musicText = event.target.innerHTML
        musicText = musicText.split(' ').join('-')
        audio.src = 'musics/' + String(musicText) + '.mp3'
        source.src = 'musics/' + String(musicText) + '.mp3'
        audio.autoplay = true
        checkPlaying()
    })

    bindEvent(audio, 'ended', () => {
        var index = parseInt(audio.dataset.index)
        var size = musics.length
        audio.src = musics[(index + 1) % size]
        source.src = musics[(index + 1) % size]

        audio.dataset.index = (index + 1) % size
        audio.autoplay = true
    })
}


var playAnimation = () => {
    var animation = 'audio-spin'
    var block = e('.audio-block')
    // let it to play animation
    addClass(block, animation)
}

var stopAnimation = () => {
    var animation = 'audio-spin'
    var block = e('.audio-block')
    removeClass(block, animation)
}

var __main = () => {
    autoPlay()
}

__main()
