$(document).ready(function(){
    var form = $("#bilgiform")
    form.submit(function() {
        $("#submitbutton").attr('disabled', true);
        form.append("<img src='http://s.aucdn.net/resim/ajax-loader.gif' />")
    })
})
