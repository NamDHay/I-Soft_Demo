document.addEventListener("DOMContentLoaded", function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('Data', function (data) {
        console.log("Data " + data);
    });
});