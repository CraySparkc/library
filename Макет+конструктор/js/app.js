{
    // const request = new XMLHttpRequest();
    // const url = "mange.py";
    // request.open("POST", url, true);
    // request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    // request.send(dataJson);
}
if (window.matchMedia('(max-width: 1400px)').matches) {
    let canv = document.querySelector('#canvas')
    canv.setAttribute('width', 700)
    canv.setAttribute('height', 600)
}
if (window.matchMedia('(max-width: 768px)').matches) {
    let canv = document.querySelector('#canvas')
    canv.setAttribute('width', 500)
    canv.setAttribute('height', 500)
    document.querySelector('.wrapper').style.flexDirection = 'column';
    document.querySelector('.managePanel').style.flexDirection = 'row';
    document.querySelector('.managePanel').style.width = '500px';
    document.querySelector('.main-btns').style.flexDirection = 'row';
    document.querySelectorAll('.h2').forEach((item) => {
        item.style.display = 'none'
    })
    document.querySelector('.managePanel-plaseholder').style.display = 'none'
    document.querySelector('.tools').style.display = 'none'
}
let canvas = new fabric.Canvas('canvas');
let roomBtn = document.querySelector('.room-btn')
let textBtn = document.querySelector('.text-btn')
let wallBtn = document.querySelector('.wall-btn')
let stairsBtn = document.querySelector('.stairs-btn')
let plaseholder = document.querySelector('.managePanel-plaseholder')
roomBtn.addEventListener('click', () => {
    canvas.add(new fabric.Rect({
        left: 500,
        top: 100,
        opacity: 0.7,
        fill: '#fff',
        strokeWidth: 10, stroke: '#c2bebd',
        width: 200,
        height: 100,
    }))
})
wallBtn.addEventListener('click', () => {
    canvas.add(new fabric.Rect({
        left: 500,
        top: 100,
        fill: '#c2bebd',
        width: 10,
        height: 100,
    }))
})
textBtn.addEventListener('click', () => {
    let text = new fabric.IText(
        'ваш текст',
        {
            fontFamily: 'Montserrat',
            fontStyle: 'italic',
            opacity: 0.3,
            left: 100,
            width: 100,
            top: 100,
        })
    canvas.add(text)
})
stairsBtn.addEventListener('click', () => {
    fabric.Image.fromURL('./images/stairs.png', function (img) {
        canvas.add(img.set({ left: 100, top: 100 }).scale(0.2))
    })
})


document.querySelector('#dwld').addEventListener('click', () => {
    // console.log(canvas.getObjects())
    // canvas.getObjects()
    // let dataJson = JSON.stringify(canvas);
    let data = canvas.toSVG();
    function download(content, fileName, contentType) {
        var a = document.createElement("a");
        var file = new Blob([content], { type: contentType });
        a.href = URL.createObjectURL(file);
        a.download = fileName;
        a.click();
    }
    download(data, 'shem.svg', 'text/plain');
})
// var SendInfo= { SendInfo: [... your elements ...]};

//         $.ajax({
//             type: 'post',
//             url: 'Your-URI',
//             data: JSON.stringify(SendInfo),
//             contentType: "application/json; charset=utf-8",
//             traditional: true,
//             success: function (data) {
//                 ...
//             }
//         });

document.querySelector('#cdwld').addEventListener('click', () => {
    let dataJson = JSON.stringify(canvas);
    const request = new XMLHttpRequest();
    const url = "manage.py";
    const params = "id_product=" + dataJson;
    request.responseType = "json";
    request.open("POST", url, true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send(params);
})

