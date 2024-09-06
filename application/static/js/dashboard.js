function logParams(data) {
    data = JSON.parse(data);
    var length = data.length;
    let pack_num = 0;
    let total_weight = 0;
    for (var i = 0; i < length; i++) {
        pack_num = data[i].params.length;
        for (let j = 0; j < pack_num; j++) {
            total_weight += data[i].params[j][1];
        }
        console.log("start: " + data[i].params[0][2]);
        console.log("end: " + data[i].params[pack_num - 1][2]);
        console.log("total weight: " + total_weight);
    }
}

function logHtml(data) {
    data = JSON.parse(data);
    var length = data.length;
    var html = "";
    for (var i = 0; i < length; i++) { 
        html += "<div class=\"div\">\
                    <img class=\"rectangle-3\" id=\"choose1" + i + "\" src=\"{{ url_for('static', filename='images/rectangle-46.svg') }}\" style=\"display: none;\" />\
                    <img class=\"rectangle-4\" id=\"choose2" + i + "\" src=\"{{ url_for('static', filename='images/rectangle-57.svg') }}\" style=\"display: none;\" />\
                    <img class=\"rectangle\" id=\"nor1" + i + "\" src=\"{{ url_for('static', filename='images/rectangle-47.svg') }}\" style=\"display: block;\" />\
                    <img class=\"rectangle\" id=\"nor2" + i + "\" src=\"{{ url_for('static', filename='images/rectangle-48.svg') }}\" style=\"display: block;\" />\
                    <div class=\"text-wrapper\">Phiên Cân</div>\
                    <div class=\"text-wrapper-2\">Tổng khối lượng</div>\
                    <div class=\"text-wrapper-3\" id=\"NO" + i + "\"></div>\
                    <div class=\"text-wrapper-4\" id=\"totalW" + i + "\"></div>\
                    <div class=\"text-wrapper-5\">Bắt đầu:</div>\
                    <div class=\"text-wrapper-6\" id=\"sTime" + i + "\"></div>\
                    <div class=\"text-wrapper-7\">25/07/2024</div>\
                    <div class=\"text-wrapper-8\" id=\"eTime" + i + "\"></div>\
                    <div class=\"text-wrapper-9\">Kết Thúc:</div>\
                    <div class=\"rectangle-2\"></div>\
                    <button class=\"select-bnt\">\
                        <div class=\"text-wrapper-10\">Chọn</div>\
                    </button>\
                </div>\
                <br />";
    }
    document.getElementById("dashLog").innerHTML = html;
}