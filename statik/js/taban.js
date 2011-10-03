jQuery(function(){
    $('ul.sf-menu').supersubs({ 
        minWidth:    12,   // minimum width of sub-menus in em units 
        maxWidth:    27,   // maximum width of sub-menus in em units 
        extraWidth:  1     // extra width can ensure lines don't sometimes turn over 
                               // due to slight rounding differences and font-family 
        }).superfish({
        animation:   {opacity:'show',height:'show'},
		autoArrows:    false,         
   		dropShadows:   true 		
    });

    $('.banner').cycle({
	    fx: 'fade' 
    });

  	$("a.tek_resim").fancybox({
		'transitionIn'	:	'fade',
		'transitionOut'	:	'elastic',
		'speedIn'		:	600, 
		'speedOut'		:	200, 
		'overlayShow'	:	true
	});

    var degistir = function(){
        if($('#son_buton').css('backgroundColor')=="rgb(223, 1, 1)"||$('#son_buton').css('backgroundColor')=="rgb(223,1,1)"){
            $('#son_buton').animate({backgroundColor: "#000000"},{duration:700,complete:function(){degistir()}});
        } else {
            $('#son_buton').animate({backgroundColor: "#DF0101"},{duration:700,complete:function(){degistir()}});
        }
    };

    degistir();
});
