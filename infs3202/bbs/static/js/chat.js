var socket;

var current_channel = ''

var change_channel = function (channel) {
    document.title = 'chatRoom - ' + channel;
    if (current_channel) {
        $("#id-div-channels-title").text(document.title);
    } else {
        $("#id-div-channels-title").text('chatRoom-Not joined');
    }
}

var clear_board = function () {
    $("#id_chat_area").val('');
}

$(document).ready(function () {
    console.log('ws://' + document.domain + ':' + location.port + '/chat')
    socket = io.connect('http://' + document.domain + ':' + location.port + '/chat');

    socket.on('connect', function () {
        console.log('connect');
        clear_board();
    });

    change_channel(current_channel)

    socket.on('status', function (data) {
        console.log('status')
        $('#id_chat_area').val($('#id_chat_area').val() + '<' + data.msg + '>\n');
        // $('#chat').scrollTop($('#chat')[0].scrollHeight);
    });
    socket.on('message', function (data) {
        console.log('message')
        $('#id_chat_area').val($('#id_chat_area').val() + data.msg + '\n');
        // $('#chat').scrollTop($('#chat')[0].scrollHeight);
    });

    $('#id-sendMsg').on('click', function(e) {
        if (!current_channel) {
                console.log("no current_channel:", current_channel);
                $('#text').val('');
                alert('Not joined any room yet')
                return;
            }
            text = $('#text').val();
            $('#text').val('');
            socket.emit('text', {
                msg: text,
                room: current_channel
            });
    })

    $('#text').keypress(function (e) {
        var code = e.keyCode || e.which;
        if (code == 13) {
            if (!current_channel) {
                console.log("no current_channel:", current_channel);
                $('#text').val('');
                alert('Not joined any room yet')
                return;
            }
            text = $('#text').val();
            $('#text').val('');
            socket.emit('text', {
                msg: text,
                room: current_channel
            });
        }
    });

    $('.rc-channel').on('click', function (e) {
        if (current_channel) {
            socket.emit('left', {}, function () {
                console.log("left room")
            });
        }
        // 加入房间
        current_channel = $(this).text();
        change_channel(current_channel);
        clear_board();
        socket.emit('joined', {
            msg: current_channel
        });
        $('#id_chat_area').empty();
    })
});
