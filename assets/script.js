var say = document.getElementById("say")
var cla = document.getElementById("clea")
var don = document.getElementById("done")
var obj = document.getElementById("alert")
var til = document.getElementById("title")
var bdy = document.getElementById("content")
var box = document.getElementById("alertbox")
var hea = document.getElementById("postcontent")
var contain = document.getElementById("container")


var front = document.getElementById("font").value
var body = document.getElementById("buddy").value
var hbdy = document.getElementById("word").value
var title = document.getElementById("titty").value
var bgcolor = document.getElementById("bgcolor").value
var fontstyle = document.getElementById("fontstyle").value
var fontweight = document.getElementById("fontweight").value


function showPassword() {
    var x = document.getElementById("password2")
    var y = document.getElementById("password1")
    if (x.type == "password") {
        x.type = "text";
        y.type = "text";
    } else {
        x.type = "password";
        y.type = "password";
    }
}

function topComment() {
    var comment = document.getElementById("topComment")
    if (comment.style.display == "block") {
        comment.style.display = "none";
    } else {
        comment.style.display = "block";
    }
}

function postwide(m, d) {
    if (d == "d") {
        if (m.classList[1] == "maxnx") {
            m.classList.remove("maxnx")
            m.classList.add("autoo")
        } else if (m.classList[1] == "autoo") {
            m.classList.add("maxnx")
            m.classList.remove("autoo")
        }
    } else {
        if (m.classList[1] == "maxx") {
            m.classList.remove("maxx")
            m.classList.add("autoo")
        } else if (m.classList[1] == "autoo") {
            m.classList.add("maxx")
            m.classList.remove("autoo")
        }
    }
}

function scrolling(m) {
    var m = m.getElementsByClassName("postcontent")[0]
    var m = m.getElementsByClassName("content")[0]
    m.classList.remove("autoo")
    m.classList.add("maxx")
}

function menu(m) {
    var say = document.getElementsByClassName("menus")[0]
    if (say.style.display == "block") {
        say.style.display = "none";
        m.classList.remove("dark")
    } else {
        say.style.display = "block";
        m.classList.add("dark")
    }
}

function grow(me) {
    me.style.height = "5px"
    me.style.height = (me.scrollHeight) + "px"
    hbdy = me.value
}

function anmate() {
    for (let i = 1; i < 43; i++) {
        var colo = "color" + i
        var colou = "colour" + i
        var color = document.getElementsByClassName(colo)[0]
        color.classList.remove(colo)
        color.classList.add(colou)
    }
    alert("jc")
}

function post(me) {
    if (me == "home") {
        body = hbdy
    }
    alert(front)
    alert(body)
    alert(title)
    alert(bgcolor)
    alert(fontstyle)
    alert(fontweight)
    boxer("successfully post")
}

function draft() {
    alert(front)
    alert(body)
    alert(title)
    alert(bgcolor)
    alert(fontstyle)
    alert(fontweight)
    boxer("successfully saves as draft")
}

function funt() {
    for (let i = 1; i <= 43; i++) {
        var font = "font" + i
        var colo = "color" + i
        var color = document.getElementsByClassName(colo)[0]
        var fonts = document.getElementsByClassName(font)[0]
        fonts.style.fontFamily = fonts.innerHTML
        fonts.style.display = "block"
        color.classList.remove(colo)
    }
    fonts.style.display = "block"

}

function color() {
    for (let i = 1; i <= 43; i++) {
        var font = "font" + i
        var colo = "color" + i
        var colu = "colour"
        var color = document.getElementsByClassName(colu)[i - 1]
        var fonts = document.getElementsByClassName(font)[0]
        fonts.style.display = "none"
        color.classList.add(colo)
    }

}


function bold() {
    if (bdy.style.fontWeight == "bold") {
        bdy.style.fontWeight = "lighter"
        bdy.style.fontweight = "lighter"
    } else if (bdy.style.fontWeight == "lighter") {
        bdy.style.fontWeight = "normal"
        bdy.style.fontweight = "normal"
    } else {
        bdy.style.fontWeight = "bold"
        bdy.style.fontweight = "bold"
    }
}

function itall() {
    if (bdy.style.fontStyle !== "italic") {
        bdy.style.fontStyle = "italic"
    } else {
        bdy.style.fontStyle = "italic"
        bdy.style.fontStyle = "normal"
    }
}

function background(me) {
    clas = me.classList[3]
    bgcolor = clas
    claa = hea.classList[0]
    hea.classList.add(clas)
    hea.classList.remove(claa)
}

function boxer(a) {
    if (a == 2) {
        box.style.display = "none"
    } else if (a == null) {
        box.style.display = "block"
    } else {
        box.style.display = "block"
        obj.style.display = "none"
        cla.style.display = "none"
        don.style.display = "none"
        say.innerHTML = a
    }
}

function clos(a) {
    if (a == "studio") {
        boxer(2)
    } else {
        imageb.style.display = "none"
        for (let i = 1; i < 3; i++) {
            var c = "other" + i
            c = document.getElementById(c).style.display = "block"
        }
    }
}

function done() {
    if (box.value == "content") {
        bdy.innerHTML = obj.value
        bdy.value = obj.value
        body = obj.value
        box.style.display = "none"
        obj.value = null
        box.value = null
    } else {
        til.innerHTML = obj.value
        til.value = obj.value
        title = obj.value
        boxer(2)
        obj.value = null
        box.value = null
    }
}

function clea() {
    box.value = null
    obj.value = null
    obj.innerHTML = null
    obj.style.height = "40px"
}

function content() {
    boxer()
    say.innerHTML = "body of your post"
    obj.innerHTML = null
    if (typeof bdy.value !== 'undefined') {
        obj.value = bdy.value
    } else {
        obj.value = null
    }
    if (bdy.value == null) {
        obj.style.height = "40px"
    } else {
        obj.style.height = "140px"
    }
    box.value = "content"
}

function tile() {
    boxer()
    say.innerHTML = "title of your post"
    obj.innerHTML = null
    if (typeof til.value !== 'undefined') {
        obj.value = til.value
    } else {
        obj.value = null
    }
    if (til.value == null) {
        obj.style.height = "40px"
    } else {
        obj.style.height = "140px"
    }
    box.value = "title"
}

function imagebox(me) {
    for (let i = 1; i < 3; i++) {
        var c = "other" + i
        c = document.getElementById(c).style.display = "none"
    }
    var image = document.getElementById("imageb")
    var imageb = document.getElementById("imagebox")
    imageb.style.display = "block"
    image.src = me.src
}
const container = document.querySelector(".container");
const closeBtn = document.querySelector(".close");

closeBtn.addEventListener("click", () => {
    container.classList.add("show");
});
