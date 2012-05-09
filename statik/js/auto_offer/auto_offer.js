window.onload = function(){
    /*
     * Parameters
     */

    // Duration of animations
    var time = 1000

    // For ease of development
    var sampleUrl = $('.orbimot img').prop('src')
      , urlBase = sampleUrl.slice(0, sampleUrl.search('auto_offer') + 10)

    // State of the users choices
    state = {
        'building': 'single',
        'apartment': 1,
        'block': 1,
        'preference': 'video',
        'monitor': '',
        'panel': '',
        'extra': { 'panels': [], 'monitors': []},
        'price': 0
    }

    // A list of costs are imported through costs.js - include: products, systems, extras
    // A list of counties imoprted through county.js - include: county

    // Required functions to prepare each slide 
    var callbacks = {
        buildings: function() {
            // Hide back button at navigation
            $('#navigation-back').fadeOut(time)

            $('#navigation-continue').html('Devam')
            
            $('#navigation-continue').unbind('click')
            
            // Hide price container               
            $('#header-price-container').hide(time) 
        },
        apartments: function() {
            // Show back button at navigation
            $('#navigation-back').fadeIn(time)
            $('.apartments-input').hide().filter('[data-type*="' + state.building + '"]').show()
            setTimeout(function() {$('#apartments input:visible:first').focus()}, time)

            $('#navigation-continue').on('click', function(event) {
                if(!checkInput($('#apartments input:visible'))) {
                    event.stopPropagation()
                    $('#apartments').find('.error:first input').focus()
                }
            })

            // Hide the price header
            $('#header-price-container').hide(time)
        },
        preferences: function() {
            //Hide price at header
            $('#header-price-container').hide(time)

            $('#navigation-continue').unbind('click')

            $('#apartments input:visible').each(function(){
                state[$(this).data('state')] = parseInt($(this).val())
            })
        },
        monitors: function() {
            // Button state
            $('#navigation-continue').html('Devam')

            //Hide monitors groups and show the relevant one
            $('.monitors.set').hide().filter('[data-preference="' + state.preference + '"]').show()
            
            // Hide all feature containers and show the relevant one
            $('#monitors .features').hide().filter(
                '[data-mold="' + focusedProduct($('#monitors').find('.orbimot:visible, .undos:visible')).data("mold") + '"]'
            ).show()

            $('.monitors.set:visible .monitors-body .orbimot').trigger('turn')

            // Start showing the price at header
            $('#header-price-container').show(time)
        },
        panels: function() {
            // Button state
            $('#navigation-continue').html('Bitir')

            // Hide panel groups and show the relevant one
            $('.panels.set').hide().filter('[data-system="' + state.monitor.system + '"]').show()

            // Hide all feature containers and show the relevant one
            $('#panels .features').hide().filter(
                '[data-mold="' + focusedProduct($('#panels').find('.undos:visible, .orbimot:visible')).data("mold") + '"]'
            ).show()

            $('#navigation-continue').unbind('click')
        },
        offer: function() {
            // Button state
            $('#navigation-continue').html('Yolla')
            
            $('#offer-price').html(numberWithCommas(state.price.toFixed()))

            // Adjust the font-size if price is too large
            if(state.price > 9999) $('#offer-price-container').css('font-size','60px')
            else $('#offer-price-container').css('font-size','80px')

            var information = $('<ul>').addClass('unstyled')
            information.append(
                $('<li>').append($('<strong>').text('Bina: '), t(state.building))
              , $('<li>').append($('<strong>').text('Şube: '), state.monitor.id)
              , $('<li>').append($('<strong>').text('Panel: '), state.panel.id)
              , $('<li>').append($('<strong>').text('Daire: '), state.apartment)
            )

            // Villa kits dont have seperate panel id
            if(state.building == 'villa') {
                information.children().eq(2).remove()
                information.children().eq(2).remove()
            }
            
            $('#offer .well').html(information)

            $('#navigation-continue').unbind('click').on('click', function(event) {
                if(!checkInput($('#offer form').find('select option:selected, textarea, input'))){
                    event.stopPropagation()
                    $('#offer').find('.error:first').find('input, textarea, select').focus()
                } else {
                    var postDict = $('#offer form').serializeArray()
                    postDict.push({name: 'type', value: 'offer'}, {name: 'state', value: JSON.stringify(state)})
                    $.post('/teklif-formu/', postDict) 
                }
            })

            setTimeout(function() {$('#offer input:visible:first').focus()}, time)
        },
        sent: function() {
            // Button state
            $('#navigation-continue').html('Baştan Başla').unbind('click').on('click', function(){ 
                location.reload(true) 
            })

            // Hide back button at navigation
            $('#navigation-back').fadeOut(time)

            //Hide price at header
            $('#header-price-container').hide(time)
        },
        villa: function() {
            // Showing price at top
            $('#header-price-container').show(time) 
            $('#navigation-back').fadeIn(time)
            
            // Navigation button text
            $('#navigation-continue').html('Bitir')
            
            // Show the relevant feature
            $('#villa .features').hide().filter(
                 '[data-mold="' + focusedProduct($('#villa').find('.orbimot:visible')).data("mold") + '"]'
            ).show()

            $('#villa .orbimot').trigger('turn')

            $('#navigation-continue').unbind('click')
        }
    }

    var translations = {
        'multiple': 'Site',
        'single': 'Apartman',
        'villa': 'Villa'
    }

    // Content for popovers with keys
    var popovers = {
        'easy-install': 'Bu özellik, binanızdaki mevcut kabloları kullanip ekstra kablo eklemeden isçilik ' + 
                        've kablodan tasarruf etmenizi sağlar',
        'light-base': 'Panelinizin altına eklenen bu aksesuar binanıza şıklık katar' +
                      '<img src="' + urlBase + '/lb/b.jpg"><img src="' + urlBase + '/lb/g.jpg">',
        'camera-angle': 'Kameranın döndürülerek, panelin tam karşısında durmayan misafirlerinizi de görmenizi sağlar',
        'panel-info': 'Devam butonuna tıklarsanız daha ayrıntılı inceleyebilirsiniz',
        'flash': '<img style="float: right;" src="' + urlBase + '/se/l.gif"> Cihazınız çaldığında ses çıkmasını istemiyorsanız'+                 ' ya da evinizde duyma güçlüğü çeken sakin varsa, parlak ışıkla uyari sağlar',
        'name-search': 'Dijital ekran üzerinde bina sakinlerinin isimleri ile arama yapılmasını sağlar',
        'price': 'Bu fiyata KDV ve işçilik dahildir',
        'better-melody': 'Zil sesinin tonu kulağa daha hoş gelecek şekilde geliştirilmiştir. Zile kısa basılma durumunda ' + 
                         'kaçırılmaması için belli bir süre çalmaya devam eder',
        'private': 'Kapıdaki misafirinizle konuşurken, aynı zamanda diafonunu açan başka bina sakinlerinin konuşmalarınızı ' +
                   'dinlemesini engeller',
        'memory': 'Kapıya gelen misafirlerinizin fotoğrafını çekip, hafızasında saklama imkanı sunar'
    }

    /*
     * Helper functions
     */

    // Validate email
    function validateEmail(email) { 
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        return re.test(email)
    } 

    // Check if input has only number 
    function onlyNumbers(string) {
        var re = /^\s*\d+\s*$/;
        return re.test(string)
    }

    // Validate and style the inputs
    function checkInput(inputList) {
        var flag = true
        inputList.each(function(){
            var controlGroup = $(this).parents('.control-group')
              , value = $(this).val()
            if((value == "" && $(this).prop('name') != 'mesaj') || ($(this).prop('name') == 'email' && validateEmail(value) != true) || 
               ($(this).parents('#apartments').length && !onlyNumbers(value))) {
                controlGroup.addClass('error')
                flag = false
            }
            else {
                controlGroup.removeClass('error')
            }
        })
        return flag
    }

    // Returns numbers with commas (ex: 1000000 -> 1,000,000)
    function numberWithCommas(number) {
        return number.toString().replace(/\B(?=(?:\d{3})+(?!\d))/g, ",")
    }

    // Given a set of features, returns the lowest priced product
    // that has those features
    function findProduct(desiredFeatures, system) {
        var newProduct
        $.each(products, function(i, product){
            var productFeatures = product.features
              , matchCount = 0

            $.each(desiredFeatures, function(i, feature){
                if($.inArray(feature, productFeatures) != -1)
                    matchCount++
            })
            if(system != null && product.system != system) {
                matchCount = 0
            }            
            if(matchCount == desiredFeatures.length){
                newProduct = product
                return false    
            }
        })
        return newProduct
    }

    // Update the price according to state
    function updatePrice() {
        var currentPriceText = $('#header-price').html()
          , extraCost = 0
        state.price = 0
        if(state.building == 'villa') {
            state.price += state.monitor.price
        } else {
            state.price += state.monitor.price * state.apartment 
            state.price += state.panel.price(state.apartment/state.block) * state.block
        }
        
        $.each(state.extra.monitors.concat(state.extra.panels), function(index, element) {
            if(extras[element]) { 
                extraCost = extras[element](state) 
                state.price += extraCost
            }
        })

        state.price += systems[state.monitor.system](state)

        var workCost = work[state.monitor.system](state) 

        state.price *= 0.767
        state.price += workCost

        // Debugging calculation
        // console.log(
        //      '*******', state, '********',
        //      '\nMonitor: ', state.monitor.price * state.apartment, 
        //      '\nPanel: ',  state.panel.price(state.apartment/state.block) * state.block,
        //      '\nSystem: ', systems[state.monitor.system](state),
        //      '\nWork: ', workCost,
        //      '\nExtra: ', extraCost,
        //      '\n**************************'
        // )

        if (state.building != 'villa') {
            var newPriceText = numberWithCommas((state.price / state.apartment).toFixed())
        }
        else {
            var newPriceText = numberWithCommas(state.price.toFixed())
        }
        if(newPriceText != currentPriceText)
            $('#header-price').fadeOut(time/2, function(){$(this).html(newPriceText)}).fadeIn(time/2)
    }

    // Given a container, returns the focused product
    function focusedProduct(container) {
        if(container.hasClass('orbimot')) return container.orbimot('focused')
        else if(container.hasClass('undos')) return container.find('img[data-focused]')
        else return container.find('img')
    }

    // Small animation for switching between panels
    function switchUndos(container, initialize) {
        var focused = focusedProduct(container)
          , other = container.find('img').not(focused)
          , cWidth = container.width()
          , cHeight = container.height()
        focused.removeAttr('data-focused')
        other.attr('data-focused', '')
        focused.animate({
            left: '0px',
            top: (cHeight - focused.data('height') * 0.5) / 2 + 'px',
            height: focused.data('height') * 0.5 + 'px',
            opacity: 0.5
        }, time)
        other.animate({
            left: cWidth - other.data('width') + 'px',
            top: (cHeight - other.data('height')) / 2 + 'px',
            height: other.data('height') + 'px',
            opacity: 1
        }, time)
        if(initialize != true)
            container.trigger('turn')
    }

    // Translate strings from translations array
    function t(text) {
        return translations[text]
    }

    /*
     * Adding functionalities
     */

    /* Animations */

    // Initializing orbimots
    $("#buildings .orbimot").orbimot({
        minimumScale: 0.5,
        duration: time,
        sizeSet: true
    })

    $('#monitors [data-preference="video"] .orbimot').orbimot({
        ellipseConstant: 64,
        minimumScale: 0.05,
        changeOpacity: true,
        duration: time,
        sizeSet: true
    })

    $('#monitors [data-preference="sound"] .orbimot').orbimot({
        ellipseConstant: 64,
        minimumScale: 0.25,
        changeOpacity: true,
        duration: time,
        sizeSet: true
    })

    $("#panels .orbimot").orbimot({
        ellipseConstant: 1000,
        minimumScale: 0.10,
        duration: time,
        sizeSet: true
    })

    $("#villa .orbimot").orbimot({
        ellipseConstant: 81,
        minimumScale: 0.10,
        duration: time,
        sizeSet: true
    })   

    // Initializing undos
    $('.undos').each(function() {
        var $this = $(this).find('img')
          , cWidth = $(this).width()
          , cHeight = $(this).height()
        if($this.length == 2) {
            var first = $this.eq(0)
              , second = $this.eq(1)
            first .data('height', first .height())
            second.data('height', second.height())
            first .data('width', first .width())
            second.data('width', second.width())
            switchUndos($(this), true)
            switchUndos($(this), true)
        } else {
            var image = $this.eq(0)
            image.css('left', (cWidth - image.width()) / 2 + 'px')
            image.css('top', (cHeight - image.height()) / 2 + 'px')
        }
    })

    /* Event bindings */

    // Interrupt tab key, it with layout
    $(document).keydown(function(event) {
        if(event.keyCode == 9) event.preventDefault()
    })

    $(document).scroll(function(event) {
        if($('.popover').length != 0) $('.popover').remove()
    })

    // Navigation button event binding
    $("#navigation").on("click", "a", function(event){
        if($(this).hasClass('disable')) return false
        var direction = $(this).data("direction")
          , sign = direction == "continue" ? "-" : "+"
          , slideLength = parseInt($("#slide-container").css("left")) * -1 || 0
          , visibleSlideIndex = slideLength / 2000
          , nextIndex = direction == "continue" ? visibleSlideIndex + 1 : visibleSlideIndex - 1
          , nextVisible = $(".slide").eq(nextIndex)

        // Slide the container
        $("#slide-container").animate({
            left: sign + "=2000px"
        }, time)

        // Change the titles
        $("#header-description").fadeOut(time/2, function() {
            $(this).find('span').html(nextVisible.data('title'))
            $(this).find('small').html(nextVisible.data('help'))
        }).fadeIn(time/2)

        // Call the necessary callbacks to prepare the slide
        var callback = callbacks[nextVisible.prop('id')] || function(){}
        callback()

        // Disable to prevent overlapped animations
        $('#navigation a').addClass('disable')
        setTimeout(function(){ $('#navigation a').removeClass('disable') }, time)
    })

    // Inner navigation button
    $("#slide-container").on("click", ".inner-navigation .btn", function(event) {
        var actUpon = $(this).parents(".slide").find(".orbimot:visible, .undos:visible")
        if (actUpon.hasClass('disable')) return false
        actUpon.addClass('disable')
        if (actUpon.hasClass('orbimot')) 
            actUpon.orbimot("turn", $(this).data('direction'))
        else  
            switchUndos(actUpon)
        setTimeout(function(){actUpon.removeClass('disable')}, time)
    })

    // Orbimot and undos click on image functionality
    $('.orbimot, .undos').on('click', 'img', function() {
        var image = $(this)
          , container = image.parents('.orbimot, .undos')
        if (container.hasClass('disable')) return false
        container.addClass('disable')
        if(container.hasClass('orbimot'))
            container.orbimot('turnTo', image)
        else if(container.find('img').length == 2 && image.data('focused')!="") {
            switchUndos(container)
        }
        setTimeout(function(){container.removeClass('disable')}, time)
    })

    // As building orbimot turns, adjust the state
    $("#buildings .orbimot").on("turn", function(event) {
        var type = $(this).orbimot("focused").data("type")
          , headerPriceHTML = $('#header-price-container').html()
        $("#buildings-information").fadeOut(time/2, function() {
            $(this).html(t(type))
        }).fadeIn(time/2)
        state.building = type

        // Making sure previous choices are consistent
        if(state.building == 'villa') { 
            state.apartment = 1
            state.block = 1
            state.panel = '' 
        } else if(state.building == 'single') {
            state.block = 1
        }

        // Custom order if user selects villa as building type
        if(state.building == 'villa') {
            $('#header-price-container').html(headerPriceHTML.replace('Daire başı:', 'Toplam fiyat:'))
            $('#villa').insertAfter($('#buildings'))
            $('#apartments, #preferences, #monitors, #panels').insertAfter($('#sent')) 
        } else {
            $('#header-price-container').html(headerPriceHTML.replace('Toplam fiyat:', 'Daire başı:'))
            $('#apartments, #preferences, #monitors, #panels').insertAfter($('#buildings'))
            $('#villa').insertAfter($('#sent'))
        }
    })

    // When preference changed, adjust the state
    $("#preferences").on("click", ".btn", function(event) {
        if (!$(this).hasClass('btn-success')) {
            $("#preferences .btn").toggleClass("btn-success")
            state.preference = $(this).data("preference")
        }
    })

    // When input is changed, make sure its error class is gone. It may be right
    $('#slide-container').on('keydown change', 'select, input, textarea', function() {
        $(this).parents('.control-group').removeClass('error')
    })

    // Change recorder product when a diffrent mold is requested
    $('#slide-container').on("turn", ".orbimot, .undos", function(event) {
        var features = $(this).siblings('.features')
          , focused = focusedProduct($(this))
          , featureToShow =  features
                .filter('[data-mold="' + focused.data('mold') + '"]')
                .find('input:not([data-extra]):first')
                .trigger('change')
                .parents('.features')
                                     
        features.filter(':visible').stop(true).fadeOut(time/2, function(){
            featureToShow.fadeIn(time/2)
        })
    })
    
    // Action to take when a feature is requested
    $('#slide-container').on('change', '.features input', function(event) {
        var checked = $(this)
          , checkedStatus = checked.prop('checked')
          , features=checked.parents('.features').find('input:checked').map(function(index,element){return element.value})||[]
          , mold = checked.parents('.features').data('mold'); features.push(mold)
          , container = checked.parents('.set, .villa-body').find('.orbimot, .undos')
          , focused = focusedProduct(container)
          , type = checked.parents('#monitors, #panels, #villa').prop('id')
          , product = type == 'panels' ? findProduct(features, state.monitor.system) : findProduct(features)
        if (type == 'villa') type = 'monitors'
        if (typeof product == "undefined") {
            product = type == 'panels'?findProduct([checked.val(),mold],state.monitor.system):findProduct([checked.val(), mold])
            checked.parents('.features')
                .find('input').prop('checked', false)
                .each(function(index, checkbox){
                    if($.inArray($(checkbox).val(), product.features) != -1) {
                        if ($(checkbox).data('extra') != "" )
                            $(checkbox).prop('checked', true)
                        else if ($(checkbox).data('extra') == ""  && $.inArray($(checkbox).val(), state.extra[type]) != -1)
                            $(checkbox).prop('checked', true) 
                    }
                })
            if (checked.data('extra') == "")
                checked.prop('checked', 'checked')
        } else {
            checked.parents('.features').find('input').each(function(){
                if($.inArray($(this).val(),product.features)!=-1 &&$(this).data('extra')!=""&&state[type.slice(0,-1)]!=product){
                    $(this).prop('checked', true)
                }
            })
        }

        if (checked.data('extra') == "" && checked.prop('checked') == true) 
            checked.prop('checked', true)

        state.extra[type] =$.makeArray(
            checked.parents('.features')
                .find('input[data-extra]:checked')
                .map(function(index,element){
                    return $(element).val()
                })
        )
       
        // If product has a new image, swap and reposition it 
        if (focused.prop('src').search(product.src) == -1) {
            var productCache = product
            focused.fadeOut(time/2, function() {
                $(this).show()
                var left = $(this).css('left')
                  , width = $(this).width()
                $(this).prop('src', urlBase + productCache.src)
                var difference = width - $(this).width()
                  , sign = difference < 0 ? '-' : '+'
                if(difference < 0) difference *= -1
                $(this).css('left', sign + '=' + difference / 2 + 'px')
                $(this).hide()
            }).fadeIn(time/2)
        }
        
        if (type=='monitors') {
            state.monitor = product
            if(state.building == 'villa') {
                state.extra.panels = []
                updatePrice()
            } else {
                var panelContainer = $('.panels.set[data-system="' + product.system + '"]').find('.orbimot, .undos')
                panelContainer.trigger('turn')
            }
        } else {
            var previousPanel = state.panel
            state.panel = product
            updatePrice()
            if(state.panel.system != previousPanel.system || 
              (state.panel.system == state.panel.system && previousPanel != state.panel)) {
                $('#monitors-panel-info .images').fadeOut(time/2, function(){
                    $('#monitors-panel-info img').remove()
                    $.each(products, function(index, element) {
                        if($.inArray('panel', element.features) != -1 && element.system == state.monitor.system) {
                            var panel = new Image()
                            panel.onload = function(){ 
                                var image = this
                                $('#monitors-panel-info .images').append(image)
                                
                                // Sniffing IE8
                                if(image.height) { 
                                    $(image).css('height', image.height * 0.25 + 'px')
                                } else {
                                    $(image).prop('height', image.getAttribute('height') * 0.25)
                                    $(image).prop('width', image.getAttribute('width') * 0.25)
                                }

                                if(image.src.search(state.panel.src) != -1) {
                                    $(image).css('opacity', 1)
                                }                           
                            }
                            panel.src = urlBase + element.src
                        }
                    })
                }).fadeIn(time/2)
            }
        }
    })

    // Change the set of county based on city
    allOptions = $('select[name="ilce"] option').clone()
    $('select[name="sehir"]').on('change', function() {
        if($(this).find('option:selected').val()) {
            city = $(this).find('option:selected').html();
            $('select[name="ilce"] option').remove()
            allOptions.filter(function() {
                if($.inArray($(this).html(), county[city]) == -1 && $(this).val() != '') {
                    return false
                } else {
                    return true
                }
            }).appendTo($('select[name="ilce"]'));
        }
    });

    /* Popovers */
    
    $('#monitors .features [data-info]').popover({
        title: function() { return $.trim($(this).text()) },
        content: function(){ return popovers[$(this).data('info')] },
        placement: 'left'
    })

    $('#panels .features [data-info]').popover({
        title: function() { return $.trim($(this).text()) },
        content: function(){ return popovers[$(this).data('info')] },
        placement: 'bottom'
    })

    $('[data-info]').not('.features [data-info]').popover({
        content: function(){ return popovers[$(this).data('info')] }
    })

    /* Custom scrollbar */

    // Starting custom scrollbar for product features
    $('.features[data-scroll] ul').jScrollPane()
    
    // Scroll pane deselects input boxes, hacky fix
    $('input[data-default]').prop('checked','checked')

    /* Styling the page */

    // Input areas are cached, not good
    $('form, input, textarea').prop('autocomplete','off')

    // Slowly reveal the page and position it
    setTimeout(function(){window.scrollTo(0,0)}, 1000)
    $('.curtain').fadeOut(time)
}
