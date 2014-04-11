var generate_button = document.getElementById('generate');
var image_width = document.getElementById('width');
var image_height = document.getElementById('height');
BlobBuilder = window.MozBlobBuilder || window.WebKitBlobBuilder || window.BlobBuilder;


generate_button.addEventListener('click', function(){
    var _image_width = parseInt(image_width.value);
    var _image_height = parseInt(image_height.value);
    var url = 'http://blackmaas.com/image/generate?';
    var data = "width="+_image_width+"&height="+_image_height;
    window.open(url+data);
})

