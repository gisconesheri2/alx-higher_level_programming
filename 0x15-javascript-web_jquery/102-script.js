$(function () {

    $('INPUT#btn_translate').on('click', function() {
        const langCode = $('INPUT#language_code').val()
        
        const urlData = {}
        if(langCode===''){
            urlData = {'mode' : 'auto'};
        } else {
            urlData = {'lang' : langCode}
        }
        alert(urlData)
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            data : urlData,
            type : "GET",
            dataType: "json",
    }).done(function( translation) {
            $('DIV#hello').text(translation.hello)
        });
    });
});