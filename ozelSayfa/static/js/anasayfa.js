jQuery(function(){
    $(".yeni_urunler").jCarouselLite({  
        vertical: false,  
        visible: 1,  
        auto:4000,  
        speed:2000  
    });  

    $("#haberler").css('height',231);

    var siyah = function(){
        $('#son_buton').animate(
            {backgroundColor: "#000000"},
            {duration: 400, 
            complete: mavi}
        );
    }

    var mavi = function(){
        $('#son_buton').animate(
            {backgroundColor: "#df0101"}, 
            {duration: 400,
            complete: siyah}
        );
    }

    mavi();
});
