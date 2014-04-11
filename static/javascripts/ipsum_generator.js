var generate_button = document.getElementById('generate');
var targetTextArea = document.getElementById('generated-text');
var includeEnochianCheck = document.getElementById('includeEnochian');
var enochianWeight = document.getElementById('enochianWeight');

generate_button.addEventListener('click', function(){
    var _nParagraphs = parseInt(document.getElementById('paragraphCount').value);
    var _sentenceVariance = parseInt(document.getElementById('sentenceLength').value);
    var _includeEnochian = document.getElementById('includeEnochian').checked;
    var _enochianWeight = parseInt(document.getElementById('enochianWeight').value);

    var data = "p="+_nParagraphs+"&sentence_variance="+_sentenceVariance+"&include_enochian="+_includeEnochian+"&enochian_weight="+_enochianWeight;
    var xhr = new XMLHttpRequest();
    xhr.open('GET','/ipsum/generate?'+data,true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.onreadystatechange=function() {
        if (xhr.readyState==4 && xhr.status==200){
            targetTextArea.innerHTML=JSON.parse(xhr.responseText)['text'];
        }
    }
    xhr.send();

    // targetTextArea.innerHTML = _generatedText;
})

includeEnochianCheck.addEventListener('click', function(){
    var _style;
    if(includeEnochianCheck.checked){
       _style='block'; 
    }
    else{
        _style='none';
    }
    enochianWeight.style.display = _style;
    enochianWeight.previousElementSibling.style.display = _style;
})
