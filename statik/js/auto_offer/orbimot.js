/*
 * jQuery Orbimot - Orbital Motion Plugin
 * Copyright (c) 2012 Refik Turkeli
 * Released under the MIT license
 * Version: 0.1 (12/Feb/2012)
 * Examples and documentation at - http://orbimot.com
 */
 
(function($){
    
    // Class definition of plugin
    var Orbimot = function(element, options){
        this.init(element, options)
    }
    Orbimot.prototype = {
        
        constructor: Orbimot,
    	
        init: function(element, options){
            var plugin = this
            plugin.$element = element
            plugin.images = plugin.$element.children('img')
            plugin.options = $.extend({}, $.fn.orbimot.defaults, options)
            
            // Maximum x coordinate value the path equation will receive.
            plugin.maximumX = Math.sqrt(plugin.options.ellipseConstant)
            
            // Positions of the images on each state
            plugin.order = $.fn.orbimot.orders[plugin.images.length]
            plugin.focusPosition = plugin.order[0]
            
            // Widths and heights of the images 
            plugin.widths = $.map(plugin.images, function(element){return $(element).width()})
            plugin.heights = $.map(plugin.images, function(element){return $(element).height()})
            
            // Set initial styles of elements
            plugin.setInitialStyle()
            
            // Coefficient for scaling the equation values to pixels
            plugin.coefficient = plugin.getCoefficient()

            // Saving the duration
            originalDuration = plugin.options.duration

            // Setting duration to 0, next turn will 
            // be done only for initial poisitioning
            plugin.options.duration = 0

            // Turn once to position the elements
            plugin.turn('right')
            plugin.turn('left')

            // Restoring to saved duration
            plugin.options.duration = originalDuration
        },
        
        /*
        Equation that will be used for calculating image paths
        Position argument it receives is explained in $.fn.orbimot.orders
        */
        equation: function(position){
            var plugin = this, 
                x = position[0] * plugin.maximumX,
                axis = position[1]
            return axis * Math.sqrt(1 - (x * x) / plugin.options.ellipseConstant)
        },
        
        /*
        On cartesian coordinates (0, -1) -> 100% | (0,1) -> 0%
        Lower the y value of element, the higher proximity value it has. This value is used
        for scaling size and opacity of images as they move closer or away. 
        100% - 0% range is mapped to 100% - minimumScale 
        */
        proximity: function(position){
            var plugin = this,
                y = plugin.equation(position),
                proximity = y * ((plugin.options.minimumScale + 1) / 2 - 1) + (plugin.options.minimumScale + 1) / 2
            return proximity
        },
        
        // Set size or position of container element and images
        setInitialStyle: function(){
            var plugin = this
            if(!plugin.options.sizeSet){
                plugin.$element.width(plugin.options.width)
                plugin.$element.height(plugin.options.height)
            }
            if(plugin.$element.css('position') == 'static') plugin.$element.css('position', 'relative')
            plugin.images.css('position', 'absolute')
        },
        
        /*
        Scales the equation values to pixels. Calculates the biggest possible value
        that would ensure no image gets out of the container while animating
        It then sets the pixel coordinates axis values according to coefficient
        */
        getCoefficient: function(){
            var plugin = this,
                width = plugin.$element.width(),
                height = plugin.$element.height(),
                widest = Math.max.apply(null, plugin.widths),
                highest = Math.max.apply(null, plugin.heights),
                axisScale = 1 - (1 - plugin.options.minimumScale) / 2,
                widthBased = (width - widest * axisScale) / (plugin.maximumX * 2),
                heightBased = 0,
                fullMeasure = 0,
                overhead = 0
            
            // Solver for finding heightBased coefficient
            while(fullMeasure <= height && heightBased <= widthBased && highest <= height) {
                overhead = 2 * heightBased - highest * (0.5 - plugin.options.minimumScale / 2)
                fullMeasure = overhead > 0 ? highest + overhead : highest
                heightBased++
            }

            coefficient = Math.min(widthBased, heightBased)
            overhead = 2 * coefficient - highest * (0.5 - plugin.options.minimumScale / 2)
            plugin.widthAxis = width / 2 
            plugin.heightAxis = overhead > 0 ? (highest + overhead) / 2 : height / 2 - coefficient
            return coefficient
        },

        // Receives position from orders, calculates left and top css value
        positionToPixel: function(position){
            var plugin = this,
                y = plugin.equation(position),
                x = position[0] * plugin.maximumX,
                left = plugin.widthAxis + (x * plugin.coefficient),
                top = plugin.heightAxis - (y * plugin.coefficient)
            return [left, top]
        },
        
        wrapIndex: function(index){
            var plugin = this,
                size = plugin.order.length,
                wrappedIndex = index
            if(wrappedIndex < 0) wrappedIndex = size - 1
            else if(wrappedIndex > size - 1) wrappedIndex = 0
            return wrappedIndex
        },
        
        // Turn once to 'right' or 'left'
        turn: function(direction){
            var plugin = this
            plugin.images.each(function(){
                $(this).animate({path: new Path(plugin, this, direction)}, plugin.options.duration)
            })
            if (direction == 'right') plugin.order = plugin.order.slice(1).concat(plugin.order.slice(0,1))
            else if(direction == 'left') plugin.order = plugin.order.slice(-1).concat(plugin.order.slice(0,-1))
            plugin.$element.trigger('turn')
        },

        turnTo: function(image){
            var plugin = this
            while(!plugin.focused().is(image[0])) plugin.turn('right')
        },
        
        // Return the focused image
        focused: function(){
            var plugin = this,
                focusIndex =  $.inArray(plugin.focusPosition, plugin.order)
            return plugin.images.eq(focusIndex)
        }

    }
    
    // Class definition for animation path
    var Path = function(plugin, image, direction){
        var state = {},
            orderIndex = plugin.images.index(image),
		    departure = plugin.order[orderIndex],
    	    nextIndex = plugin.wrapIndex(direction == 'right' ? orderIndex + 1 : orderIndex - 1),
		    destination = plugin.order[nextIndex]

        var axis = departure[1] + destination[1] < 0 ? -1 : 1,
            pToPosition = function(p){return p * (departure[0] - destination[0]) + destination[0]}

        this.css = function(p){
    		var position = [pToPosition(p), axis],
    		    cssPosition = plugin.positionToPixel(position),
			    proximity = plugin.proximity(position)
    		state.zIndex = Math.floor(proximity * 100)
    		state.width = plugin.widths[orderIndex] * proximity + 'px'
			state.height = plugin.heights[orderIndex]  * proximity + 'px'
    		state.left = cssPosition[0] - (parseFloat(state.width) / 2) + 'px'
    		state.top = cssPosition[1] - (parseFloat(state.height) / 2) + 'px'
			state.opacity = plugin.options.changeOpacity ? proximity : 1
            state.filter = plugin.options.changeOpacity ? 'alpha(opacity=' + (proximity * 100).toFixed(0) + ')' : ''
    		return state
    	}
    }
    
    // Plugin Definition
    $.fn.orbimot = function(option){
        var pluginArguments = arguments
            returnValue = this
        this.each(function(){
            var $this = $(this),
                data = $this.data('orbimot'),
                options = typeof option == 'object' && option
            if(!data) $this.data('orbimot', new Orbimot($this, options))
            if(typeof option == 'string' ) {
                var methodReturn = data[option](Array.prototype.slice.call(pluginArguments,1))
                if(methodReturn) returnValue = methodReturn
            }
        })
        return returnValue
    }
    
    /* 
    These are the coordinates of the images depending on how many there is. 
    First number is the ratio to multiply with maximum cartesian x value, second
    number is the identifier of whether the image is on, below or above the x axis.
    These positions are picked with experimenting when the rotation looks best.
    */
    $.fn.orbimot.orders = {
        2: [[0,-1], [0,1]],
        3: [[0,-1], [1,0], [-1,0]],
		4: [[0,-1], [1,0], [0,1], [-1,0]],
		5: [[0,-1], [1,0], [0.5,1], [-0.5,1], [-1,0]],
		6: [[0,-1], [1,0], [0.5,1], [0,1], [-0.5,1], [-1,0]],
		7: [[0,-1], [1,0], [0.6,1], [0.2,1], [-0.2,1], [-0.6,1], [-1,0]],
		8: [[0,-1], [0.86,-1], [1,0], [0.5,1], [0,1], [-0.5,1], [-1,0], [-0.86,-1]],
		9: [[0,-1], [0.86,-1], [1,0], [0.6,1], [0.2,1], [-0.2,1], [-0.6,1], [-1,0], [-0.86,-1]]
    }
	
	$.fn.orbimot.defaults = {
		ellipseConstant: 25,// The biggger this constant, the more elliptical path images will follow
	    changeOpacity: true,// Opacity will decrease as image goes away 
		minimumScale: 0.25, // Minimum constant to scale down and reduce opacity as image goes away 
		duration: 1000,     // Amount of time it will take for one position rotation
		sizeSet: false,     // Set true if you manually set width and height. Else, plugin options will be used
		height: 400,        // Height of the container
		width: 600          // Width of the container
	}
    
    // Path argument for jQuery.animate, custom states for animation. Defined by Path class
    $.fx.step.path = function(fx){
        var css = fx.end.css(1 - fx.pos)
        for(var i in css) fx.elem.style[i] = css[i]
    }
})(jQuery)
