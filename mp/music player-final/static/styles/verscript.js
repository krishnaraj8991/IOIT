var socket;
$(document).ready(function () {
    // socket = io.connect('http://127.0.0.1:5000');
    // console.log(window.location.href);
    socket = io.connect(window.location.href);
    // sending a connect request to the server.

    // An event handler for a change of value 
    $('input.sync').on('input', function (event) {
        socket.emit('Slider value changed', {
            who: $(this).attr('id'),
            data: $(this).val()
        });
        return false;
    });

    socket.on('after connect', function (msg) {
        console.log('After connect', msg.list);
        document.getElementById('table').innerHTML = ''
        var cs = document.getElementById("current_song")
        cs.innerHTML = "" + msg.list[0].slice(0, -4);
        msg.list.forEach(add);
    });

    socket.on('update value', function (msg) {
        console.log('Slider value updated');
        $('#' + msg.who).val(msg.data);
    });
    socket.on('set max', function (msg) {
        console.log('new length =' + msg.length);
        // $('#' + msg.who).val(msg.data);
        document.getElementById("slider1").max = msg.length;
        // document.getElementById("slider1").val=0;
    });
});
var paly_pause = false
var que = []
index = 0
var limit = 0

function clicked() {
    console.log(paly_pause)
    // var socket = io.connect('http://127.0.0.1:5000');
    socket.emit('play_pause', "hi");
    paly_pause = !paly_pause

    let x = document.getElementById("play/pause");

    if (x.classList.contains("fa-play")) {

        x.classList.remove("fas", "fa-play", "sty");
        x.classList.add("fas", "fa-pause", "sty");
    } else if (x.classList.contains("fa-pause")) {
        x.classList.remove("fas", "fa-pause", "sty");
        x.classList.add("fas", "fa-play", "sty");
    }
}

/*function voll(){

    let y = document.getElementById("rell");
    let x = document.getElementById("voll");
    

    if(y.classList.contains("rel") && x.classList.contains("vol") )
    {
 
     x.classList.remove("rel");
     x.classList.add("relc");
     y.classList.remove("vol");
     y.classList.add("volc");
    }
    else if(x.classList.contains("relc") && x.classList.contains("volc"))
    {
        x.classList.remove("relc");
        x.classList.add("rel");
        y.classList.remove("volc");
        y.classList.add("vol");

    }
 return false;
}*/

function nextbt() {
    console.log('next' + index + ' ' + limit)
    if (index + 1 <= limit) {
        // var socket = io.connect('http://127.0.0.1:5000');
        socket.emit('next', "hi");
        var cs = document.getElementById("current_song")
        cs.innerHTML = que[index++].slice(0, -4);
    }
}

function add(data, index) {
    console.log('called')
    var table = document.getElementById("table");
    var row = table.insertRow(-1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell2.innerHTML = "<a href=\"javascript:list_clicked('" + data + "')\" id=\"foo\">" + data.slice(0, -4) + "</a>";
    data = data.slice(0, -4);
    // name=url_for('static', filename= data +".jpg");
    cell1.innerHTML = "<img  id='" + data + "'/>";
    document.getElementById(data).src = "static\\images\\" + data + ".jpg";
    // var fs = require('fs');
    // var files = fs.readdirSync('/songs');
    // console.log(files)
}


function list_clicked(data) {
    console.log(data);
    socket.emit('play track', {
        'data': data
    });
    que.push(data)
    limit++
    // var socket = io.connect('http://127.0.0.1:5000');
}

