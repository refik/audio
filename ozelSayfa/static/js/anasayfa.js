jQuery(function(){
    $('#yeni_urunler').cycle({
        fx: 'scrollLeft',
        speed: 900,
        timeout: 5000,
        cleartype: true,
        cleartypeNoBg: true
    });

    $('#haberler').cycle({
        fx: 'fade',
        speed: 900,
        timeout: 5000,
        cleartype: true,
        cleartypeNoBg: true
    });
});
