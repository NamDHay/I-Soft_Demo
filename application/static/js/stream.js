document.addEventListener("DOMContentLoaded", function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('File', function (data) {
        console.log(data);
    });
});