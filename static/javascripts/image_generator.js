var generate_button = document.getElementById('generate');
var image_width = document.getElementById('width');
var image_height = document.getElementById('height');
BlobBuilder = window.MozBlobBuilder || window.WebKitBlobBuilder || window.BlobBuilder;


generate_button.addEventListener('click', function(){
    var _image_width = parseInt(image_width.value);
    var _image_height = parseInt(image_height.value);

    var data = "width="+_image_width+"&height="+_image_height;
    var xhr = new XMLHttpRequest();
    xhr.open('GET','/image/generate?'+data,true);
    xhr.responseType = 'blob';
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.onreadystatechange=function() {
        if (xhr.readyState==4 && xhr.status === 200) {
            var image_el = document.getElementById('generated-image');
            var url = window.URL.createObjectURL(xhr.response);
            window.open(url);
            window.URL.revokeObjectURL(url)
        }
    }
    xhr.send();

})

