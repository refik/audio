var search_isim_mesaj;
var search_dosya;
var search_durum;
var search_daire;
var search_tutar;
var search_tarih;
var search_sehir;
var sort_table;


//testQuery smart return to remember who hid the element (to chain filter)
function smart_return(search, value, row, uid){
    var hiders = row.attr('data-hiders') ? row.attr('data-hiders') : '';
	var selector = uid ? search.selector + uid : search.selector;
    var is_hider = hiders.indexOf(selector) != -1 ? true : false;
    var same = hiders == selector ? true : false;
    if(value){
        if(hiders.length){
            if(!same){
                value = false;
            }
            if(is_hider){
                hiders = hiders.replace(selector,'');
                row.attr('data-hiders', hiders);
            }
        }
    } else {
        if(!is_hider){
            row.attr('data-hiders', hiders + selector);
        }
    }
    return value;
}

//Text testQuery with chain support and '||' based
function text_test(query, txt, _row){
    var check_first = query[0];
    if(check_first == '-'){
        return smart_return(this, true, $(_row));
    }
    for (var i = 0; i < query.length; i += 1) {
        if (txt.indexOf(query[i]) != -1) {
            return smart_return(this, true, $(_row));
        }
    }
    return smart_return(this, false, $(_row))
}

//Combined boolean and number testQuery for quicksearch
function number_bool_test(query, txt, _row) {  
    var to_return;
    query = query[0];
    if(query == 'true' || query == 'false' || query == '-'){
        if(query == 'true' && txt != 'x'){
            to_return = true;
        } else if(query == 'false' && txt == 'x'){
            to_return = true;
        } else if(query == '-'){
            to_return = true;
        } else {
            to_return = false;
        }
        return smart_return(this, to_return, $(_row));
    }

    var operation = query[0];
    var compare = Number(query.replace(query[0],''));
    var value = Number(txt.replace(/,/g,''));
    if(value != '-'){
        if(operation == '<' && value < compare){
            to_return = true;
        } else if(operation == '>' && value > compare){
            to_return = true;
        } else {
            to_return = false;
        }
    } else {
        to_return = true;
    }
    return smart_return(this, to_return, $(_row), operation);
}   

//Boolean testQuery for quicksearch 
function bool_test(query, txt, _row) {
    var to_return;
    query = query[0];
    if(query != '-'){
        if(query == 'true' && txt != 'x'){
            to_return = true;
        } else if(query == 'false' && txt == 'x'){
            to_return = true;
        } else {
            to_return = false;
        }
    }
    else{
        to_return = true;
    }
    return smart_return(this, to_return, $(_row));
}

//Default search options for quicksearch
var def_search_opts = {
    onAfter: function(){update_sum();update_stripe();}, 
    hide: function(){$(this).prop('class','hide')}, 
    show: function(){$(this).prop('class','')},
    loader: 'img.loading',
    bind: 'keyup change',
    delay: 500
}

//Flashes a given row
function blink(row_pk){
    var row = $('tr[data-pk="' + row_pk + '"]');
    if(row.length){
        var current = $('tr[data-pk="' + row_pk + '"]').css('background-color');
        row.css('background-color', '#82ff82');
        row.animate({'background-color': current}, 1500, function(){ 
            row.css('background-color', '#82ff82');
            row.animate({'background-color':current}, 1500);
        });
    }
}

//Scrolls to a given row
function attention(row_pk){
    var row = $('tr[data-pk="' + row_pk + '"]');
    if(row.length){
        $('html, body').animate({
            scrollTop: row.offset().top - 110
        }, 500);
        blink(row_pk);
    }
}

//Loading animation for a given element
function loading(element){
    element.children().each(function(){$(this).css('opacity',0.2);});
    element.prepend('<img alt="yukleniyor" id="loading" src="http://s.aucdn.net/resim/ajax-loader.gif" />');
}

var sum = function(items) {
    var result = 0;
	if(items.length){
    	items.each(function() {
        	result += Number($(this).html().replace(/,/g,''));
    	});
	}
    return result
};

function number_with_commas(num) {
    return num.toString().replace(/\B(?=(?:\d{3})+(?!\d))/g, ",");
}

//Updating statistics for visible table values
function update_sum() {
    $('#sum-tutar').html('Tutar: ' + number_with_commas(sum($('.tutar').not('tr.hide .tutar'))) + ' TL');
    $('#sum-daire').html('Daire: ' + number_with_commas(sum($('.daire').not('tr.hide .daire'))));
    $('#sum-sayi').html('Sayi: ' + ($('#main tr').not('tr.hide').length - 1));
}

//Zebra stripes for the form
function update_stripe() {
    $('#main tbody tr').css('background-color', '#ffffff');
    $('#main tr').not($('tr.hide')).filter(':odd').css('background-color', '#f5f5f5');
}   

function get_form(form, offer_pk){
    var result = null;
    $.ajax({
                url: '/teklif/form/',
                data: {form_type: form, pk: offer_pk},
                type: 'get',
                dataType: 'html',
                async: false,
                success: function(data) { result = data; }
            });
    return result
}

//function position_pop(old_height){
//    var popover = $('.popover');
//    var current_height = popover.height();
//    var current_top = parseInt(popover.css('top'));
//    var height_dif = current_height - old_height;
//    var new_top = current_top - height_dif
//    popover.css('top', new_top);
//}

//Updating an existing row with newest values
function update_row(pk){
    $('tr[data-pk="' + pk + '"]').load('/teklif/yenile/' + pk + '/ th, td', function(){
        update_sum(); 
        // Wont be necessary will use '$.on'
        //init_interaction($(this));
        update_last_action($(this));
        blink(pk);
    });
}

//Initializing an ajax form
function init_form(type){
    //var pop_height = $('.popover').height();
    var pk;

    // This is how django gets it
    $.datepicker.regional['tr'].dateFormat = 'dd/mm/yy'

    $('form .datepicker').datepicker($.datepicker.regional['tr']);
    $('form').ajaxForm({data: { form_type: type}, beforeSubmit: function(arr, $form, options){
        loading($('.content p'));
        $.each(arr,function(i,v){
            if (v.name == 'teklif') pk = v.value
        });
    }, success: function(data){
        if(data == ''){
            update_row(pk);
            $('.close').click();
        } else {
            $('.content p').html(data);
            init_form(type);
            //position_pop(pop_height); 
        }
    }});
}

//Durum dialogs form update for choosing an action
function update_form(pk){
    var form_to_get = $('.content select option:selected').val();
    if(form_to_get){
        $('.content p form').remove();
        $('.content p').append(get_form(form_to_get, pk));
        init_form(form_to_get);
    }
}

function show_alert() {
    var current_count = Number($('#new-count').html())
    $('.alert-message').show('slow')
    $('#new-count').html(current_count + 1);
}

//Sorting function to figure out the latest offer
var ascending = function(first, last){ return $(first).data('pk') - $(last).data('pk') }

//Loop for requesting new offers from server
//function get_new_loop(){
//    var latest = $('tbody tr, #new-stack tr').sort(ascending).filter(':last');
//    $.get('/teklif/yeni/' + latest.data('pk') + '/', function(data){
//        if (data) {
//            $('#new-stack').prepend(data)
//            show_alert();
//        }
//        setTimeout(function(){get_new_loop();}, 20000);
//    })
//}

//Appending new offers to dom
//function unleash(){
//    var new_rows = $('#new-stack').html();
//    $('#search').val('').change();
//    $('.alert-message').hide('slow');
//    $('tbody').prepend(new_rows);
//    update_stripe();
//    update_sum();
//    $('#new-stack').html('');
//    $('#new-count').html(0);
//    $(new_rows).each(function(){
//        pk = $(this).data('pk')
//        update_row(pk);
//    });
//}

//Saving filters selected value to dom
function update_filter(on_dom, current, search_item){
    var select = $(current).children(':selected');
    var name = on_dom.split(' ')[0].replace('#search-', '');
	var type = on_dom.split(' ')[1].replace(/select.|select/g, '');
	var className = name + '-' + type;
	if (type=='') var info = name
	if (type=='exists') var info = name
	if (type=='bigger') var info = name + ' buyuk'
	if (type=='smaller') var info = name + ' kucuk'
    var indicator = '<li class="indicator ' + className + '"><span>' + info + ': ' + select.html() + '</span> <span class="divider">/</span></li>'
    $(on_dom + ' option:selected').removeAttr('selected');
    $(on_dom + ' option[value="' + select.val() + '"]').attr('selected','selected');
    search_item.search(select.val());
    $('.dropdown:last').removeClass('open');    
    $('.close').click();
    $('#filter-indicator').find('.' + className).remove()
	if(select.val()!='-') $('#filter-indicator').append(indicator).show('slow')
    if(!$('.indicator').length) $('#filter-indicator').hide('slow')
}

//Preparing special title for closing popovers
function get_title(element) {
    return  $(element).data('original-title') + '<span class="close" onclick="' + 
            '$(this).parents(\u0027.popover\u0027).' + 
            'fadeOut(\u0027fast\u0027, function(){$(this).remove();})">x</span>'
}

//Shortcut function for delayed hovering
//function hover_after(element, time, execute){
//    element.hover(function(){
//        $.data(this, 'timer', setTimeout($.proxy(execute, this), time));
//    }, function(){
//        clearTimeout($.data(this, 'timer'));
//    });
//}

//Coloring offers based on last actin. Green is good, red is bad
function adjust_urgency_color(element){
    hour = element.html()
    if(hour >= 100){
        red = 255;
        green = hour > 200 ? 130 : Math.floor(390 - (hour * 1.35));
        blue = green;
    } else {
        red = hour < 1 ? 130 : Math.floor(130 + (hour * 1.25));
        green = 255;
        blue = red;
    }
    element.parents('td').css('background-color', 'rgb(' + red + ',' + green + ',' + blue + ')');
}

//Converting last action of elements from date format to ordinal
//SO that javascript can order them
function update_last_action(elements){
    var now = new Date().getTime();
    elements.find('.last-action').each(function(){
        date_string = $(this).html();
        date_args = date_string.split('-');
        var date = new Date(); 
        date.setFullYear(Number(date_args[0]), Number(date_args[1]) - 1, Number(date_args[2]));
        date.setHours(Number(date_args[3]));
        action = date.getTime();
        difference = now - action;
        dif_hour = difference > 0 ? Math.floor(difference / 3600000) : 0;
        $(this).html(dif_hour);
        adjust_urgency_color($(this));
    })
}

function init_interaction(){
    //Twipsy initializations
    $('#main').on('mouseenter mouseleave', '.static', function(e){
        var $element = $(this)
        if(e.type == 'mouseenter'){
            $element.data('timer', setTimeout(function(){
                $element.twipsy({html: true, placement: 'below', trigger:'live'}).twipsy('show');
            }, 500))
        } else {
            clearTimeout($element.data('timer'))
            setTimeout(function(){
                $element.twipsy('hide')
                $element.removeData('twipsy')
            }, 500)
        }
    })
    $('#main').on('mouseenter mouseleave', '.dynamic', function(e){
        var $element = $(this)
        if(e.type == 'mouseenter'){
            $element.data('timer', setTimeout(function(){
                $element.twipsy({ html: true, placement: 'below', trigger: 'manual', title: function(){ 
                    var result = null;
                    $.ajax({
                                url: ('/teklif/' + $(this).data('url') + '/' + $(this).parents('tr').data('pk') + '/'),
                                type: 'get',
                                dataType: 'html',
                                async: false,
                                success: function(data) { result = data; }
                            });
                    return result
                }}).twipsy('show');
            }, 1000))
        } else {
            clearTimeout($element.data('timer'))
            setTimeout(function(){
                $element.twipsy('hide')
                $element.removeData('twipsy')
            }, 1500)
        }
    })

    //Popover intializations
    $('#main').on('click', '.edit', function(e){
        var $element = $(this)
        $('.twipsy').fadeOut();
        $element.removeData('popover')
        $element.popover({trigger: 'manual', html: true, placement: 'below', content: function(){
            return get_form($(this).data('form'), $(this).parents('tr').data('pk'))
        }, title: function(){ 
            return get_title(this);
        }});
        $element.popover('show')
        init_form($element.data('form'));
    })
    $('#main').on('click', '.dosya-dialog', function(e){
        var $element = $(this)
        $('.twipsy').fadeOut();
        $element.removeData('popover')
        $element.popover({trigger: 'live', html: true, placement: 'below', title: function(){ 
            return get_title(this)
        }, trigger: 'manual', content: function(){
            return  '<a target="_blank" href="' + $(this).data('href') + '" ' + 
                    'onclick="$(\u0027.close\u0027).click()" class="btn primary">Dosyayi Ac</a>' + 
                    ' <a class="btn" onclick="' +
                    '$(\u0027.content p\u0027).html(get_form(' + '\u0027' + $(this).data('form') + 
                    '\u0027,' + $(this).parents('tr').data('pk') + '));init_form(\u0027' + 
                    $(this).data('form') + '\u0027);">Yeni Ekle</a>'            
        }});
        $element.popover('show')
    })
    $('#main').on('click', '.durum-dialog', function(e){
        var $element = $(this)
        $('.twipsy').fadeOut();
        $element.removeData('popover')
        $element.popover({trigger: 'live', html: true, placement: 'below', title: function(){ 
            return get_title(this);
        }, trigger: 'manual', content: function(){
            return  '<select style="margin-bottom:10px"class="span3" ' + 
                    'onchange="var pop_height = $(\u0027.popover\u0027).height();update_form(' + 
                    $(this).parents('tr').data('pk') + ');">' +  
                    '<option value="" selected="selected">Islem secin</option>' + 
                    '<option value="genel">Genel guncelleme</option>' + 
                    '<option value="iletisim">Iletisime gectim</option>' + 
                    '<option value="yonlendi">Yonlendirdim</option>' + 
                    '<option value="aldik">Isi aldik</option>' + 
                    '<option value="sebep">Isi kaybettik</option>' + 
                    '<option value="iptal">Iptal ediyorum</option>' + 
                    '<option value="dondur">Donduruyorum</option>' + 
                    '</select>'
        }});
        $element.popover('show')
    })
}

function sifirla(){
    search_tutar.search('');
    $('.dropdown:last').removeClass('open');
    $('tbody tr').removeAttr('data-hiders');
    $('select').children('option[selected="selected"]').removeAttr('selected')
    $('select').each(function(){
        $(this).children('option:first').attr('selected','selected');
    });
    $('#filter-indicator').hide('slow', function(){$(this).find('.indicator').remove()})
}


function initSort(){
    //Table sort initializations
    $.tablesorter.addParser({
        id: 'comma-number',
        is: function(s){
            return false;
        },
        format: function(s){
            number = $(s).html().replace(/[\t\n\s\,]/g,'');
            if(number == 'x'){
                return 0
            } else {
                return parseInt(number);
            }
        },
        type: 'numeric'
    });
    $.tablesorter.addParser({
        id: 'last-action',
        is: function(s){
            return false;
        },
        format: function(s){
            action = $(s).filter('.last-action').html().replace(/[\t\n\s\,]/g,'');
            return parseInt(action);
        },
        type: 'numeric'
    });
    $.tablesorter.addParser({
        id: 'date',
        is: function(s){
            return false;
        },
        format: function(s){
            action = $(s).filter('.tarih').html().replace(/[\t\n\s\,]/g,'');
            return parseInt(action);
        },
        type: 'numeric'
    });
    $.tablesorter.addParser({
        id: 'special-text',
        is: function(s){
            return false;
        },
        format: function(s){
            text = s.replace(new RegExp('<[^<]+\>', 'g'), "")
            return text;
        },
        type: 'text'
    });

    sort_table = $('#main').tablesorter(
        {
            cssHeader: 'new-header',
            headers: {
                1: {
                    sorter: 'special-text'
                },  
                9: {
                    sorter: 'comma-number'
                },  
                10: {
                    sorter: 'comma-number'
                },
                0: {
                    sorter: 'last-action'
                },
                2: {
                    sorter: 'date'
                },
                4: {
                    sorter: false
                },
                5: {
                    sorter: 'special-text'
                },
                6: {
                    sorter: 'special-text'
                },
                7: {
                    sorter: 'special-text'
                },
                8: {
                    sorter: 'special-text'
                },
                3: {
                    sorter: 'special-text'
                }
            },
            textExtraction: function(node){return node.innerHTML;}
    });

    $('#main').bind('sortEnd', function(){ update_stripe(); });
}

//Filter initializations
function initSearch(){
    if(!search_isim_mesaj){
        search_isim_mesaj = $('#search').quicksearch('#main tbody tr', $.extend({} ,def_search_opts, {
            selector: "div.isim-mesaj"
        }));
    }
}
function initFilters1(){
    search_dosya = $().quicksearch('#main tbody tr', $.extend({}, def_search_opts, {
        selector: "[data-form='dosya']",
        testQuery: bool_test    
    }));
    search_durum = $().quicksearch('#main tbody tr', $.extend({}, def_search_opts, {
        selector: "[data-form='durum']",
        testQuery: text_test
    }));
}
function initFilters2(){
    search_daire = $().quicksearch('#main tbody tr', $.extend({}, def_search_opts, {
        selector: "[data-form='daire']",
        testQuery: number_bool_test
    }));
    $('.filter').click(function(){
        $('.close').click();
        $(this).removeData('popover')
        $(this).popover({html: true, placement: 'right', title: function(){ 
            return get_title(this); 
        }, trigger: 'manual', content: function(){
            return $($(this).data('search')).html()
        }}).popover('show');
        $('.popover').css('position','fixed');
    });
}
function initFilters3(){
    search_tutar = $().quicksearch('#main tbody tr', $.extend({}, def_search_opts, {
        selector: "[data-form='tutar']",
        testQuery: number_bool_test
    }));
    search_tarih = $().quicksearch('#main tbody tr', $.extend({}, def_search_opts, {
        selector: "div.tarih",
        testQuery: number_bool_test
    }));
}

function initFilters4(){
    search_sehir = $().quicksearch('#main tbody tr', $.extend({}, def_search_opts, {
        selector: ".sehir",
        testQuery: text_test
    }));
    search_sorumlu = $().quicksearch('#main tbody tr', $.extend({}, def_search_opts, {
        selector: ".sorumlu",
        testQuery: text_test
    }));
}
//Twipsy to get iscilik
//$('#sum-tutar').twipsy({ html: true, placement: 'below', title: function(){ 
//    var result = null;
//  var pk_list = ''
//  var offers = $('tbody tr').not('.hide').each(function(i,v){
//      comma = i > 0 ? '-' : '';
//      pk_list += comma + $(this).data('pk');
//  });
//    $.ajax({
//                url: ('/teklif/iscilik-tutar/'),
//                type: 'get',
//              data: {pks: pk_list},
//                dataType: 'html',
//                async: false,
//                success: function(data) { result = data; }
//            });
//   return result
//}, delayIn:1000});

//Wont be necessary will use '$.on'
//Initialize twipsy and popovers for all rows
//$('tbody tr').one('hover', function(){init_interaction($(this));});

function initStyle(){
    update_last_action($('tbody tr')); //Update last action
    $('.topbar').dropdown(); //Menu initialization
    //get_new_loop(); //Get new offers initialization
    update_stripe(); //Update table stripe colors
    update_sum();

}

// Old ready //

$(function() {

    var process = {
        steps: [
            function(){
                initFilters1();
                $('#load-info').html('Filtrelerin ilk kismi yukleniyor');
                $('#bar').css('width', '15%');
            },
            function(){
                initFilters2();
                $('#load-info').html('Filtrelerin ikinci kismi yukleniyor');
                $('#bar').css('width', '25%');
            },
            function(){
                initFilters3();
                $('#load-info').html('Filtrelerin ucuncu kismi yukleniyor');
                $('#bar').css('width', '50%');
            },
            function(){
                initFilters4()
                $('#load-info').html('Filtrelerin dorduncu kismi yukleniyor');
                $('#bar').css('width', '60%');
            },
             function(){
                initSearch();
                $('#load-info').html('Arama yukleniyor')
                $('#bar').css('width', '75%');
            },
            function(){
                $('#search-durum select').change(); //only show active jobs at launch
                $('#load-info').html('Ilk filtreleme yapiliyor');
                $('#bar').css('width', '85%');
            },
            function(){
                init_interaction();
                initStyle();
                $('#load-info').html('Sayfa gorunumu ayarlaniyor');
                $('#bar').css('width', '90%');
            },
            function(){
                initSort()
                $('#load-info').html('Siralama yukleniyor');
                $('#bar').css('width', '100%')
            },
            function(){
                // Delete progress bar from the page
                // Show transparent page items
                $('#progress').remove();
                $('.container, .topbar').css('opacity', 1);
                $('.container, .topbar').css('filter', '');
                if(focusOn) attention(focusOn);
            }
        ],
        index: 0,
        nextStep: function(){
            this.steps[this.index++]();
            if (this.index != this.steps.length) {
                var me = this;
                window.setTimeout(function(){
                    me.nextStep();
                }, 100);
            }
        }
    };

    process.nextStep();

})
