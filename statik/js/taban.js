jQuery(function(){
  $('ul.sf-menu').superfish({
		autoArrows:    false,         
   		dropShadows:   false 		
    });

  $(".jcarousellite").jCarouselLite({  
		vertical: true,  
		visible: 2,  
		auto:2000,  
		speed:2000
    });  

  $('.banner').cycle({
		fx: 'fade' 
    });

});
