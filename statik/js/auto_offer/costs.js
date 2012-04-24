// Products information
var products = [
    // Villa sets
    {
        features: ['telefon-villa'],
        src: '/etv/t.png',
        system: 'villa',
        id: '001344',
        price: 160
    },
    {
        features: ['bw', 'eko-villa'],
        src: '/evk/bw.png',
        system: 'villa',
        id: '001390',
        price: 450
    },
    {
        features: ['c', 'eko-villa'],
        src: '/evk/c.png',
        system: 'villa',
        id: '001389',
        price: 550
    },
    {
        features: ['x-villa'],
        src: '/fvk/x.png',
        system: 'villa',
        id: '001421',
        price: 650
    },

    // Monitors
    /* Et telefon */
    {
        features: ['doormen', 'telefon'],
        src: '/t/l.jpg',
        system: 'et',
        id: '001072',
        price: 38
    },

    /* Ft telefon */
    {
        features: ['private', 'two-doors', 'better-melody', 'doormen', 'telefon'],
        src: '/t/l.jpg',
        system: 'ft',
        id: '001061',
        price: 43
    },

    /* 4 + n E */
    {
        features: ['e'],
        src: '/e/w.png',
        system: '4+n',
        id: '001033',
        price: 17
    },

    /* 4 + n Kd */
    {
        features: ['kd'],
        src: '/kd/g.png',
        system: '4+n',
        id: '001227',
        price: 17
    },

    /* 8 + n Kd */
    {
        features: ['two-doors', 'better-melody', 'private', 'kd'],
        src: '/kd/g.png',
        system: '8+n',
        id: '001226',
        price: 19
    },
    {
        features: ['two-doors', 'better-melody', 'private', 'doormen', 'adjust-sound', 'kd'],
        src: '/kd/g.png',
        system: '8+n',
        id: '001223',
        price: 21
    },

    /* 8 + n Fnk */
    {
        features: ['two-doors', 'white', 'fnk'],
        src: '/fnk/wkpn.png',
        system: '8+n',
        id: '001430',
        price: 25
    },
    {
        features: ['two-doors', 'gold', 'doormen','adjust-sound', 'fnk'],
        src: '/fnk/gkpn.png',
        system: '8+n',
        id: '001435',
        price: 27
    },
    {
        features: ['two-doors', 'chrome', 'doormen', 'adjust-sound', 'flash', 'fnk'],
        src: '/fnk/mkpn.png',
        system: '8+n',
        id: '001437',
        price: 40
    },

    /* 8 + n Sa */
    {
        features: ['two-doors', 'sa'],
        src: '/sa/dn.png',
        system: '8+n',
        id: '001012',
        price: 25
    },
    {
        features: ['two-doors', 'doormen','sa'],
        src: '/sa/d.png',
        system: '8+n',
        id: '001013',
        price: 26
    },

    /* Bus Plus + n Eko */
    {
        features: ['bw', 'doormen', 'eko'],
        src: '/eko/bwkpn.png',
        system: 'plus+n',
        id: '001560',
        price: 200
    },
    {
        features: ['color', 'doormen', 'eko'],
        src: '/eko/ckpn.png',
        system: 'plus+n',
        id: '001561',
        price: 300 
    },

    /* Bus Plus + n Gdm */
    {
        features: ['2,5', 'doormen', 'white','gdm'],
        src: '/gdm/25kpn.png',
        system: 'plus+n',
        id: '001702',
        price: 230
    },
    {
        features: ['3,5', 'doormen', 'white', 'gdm'],
        src: '/gdm/35kpn.png',
        system: 'plus+n',
        id: '001703',
        price: 250
    },

    /* Bus Plus Gdm */
    {
        features: ['2,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdm'],
        src: '/gdm/25kpn.png',
        system: 'plus',
        id: '001721',
        price: 270
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdm'],
        src: '/gdm/35kpn.png',
        system: 'plus',
        id: '001720',
        price: 290
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdm'],
        src: '/gdm/35kp.png',
        system: 'plus',
        id: '001719',
        price: 320
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'flash', 'gold','gdm'],
        src: '/gdm/gmn.png',
        system: 'plus',
        id: '001729',
        price: 340
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'flash', 'intercom','memory', 'gold','gdm'],
        src: '/gdm/gm.png',
        system: 'plus',
        id: '001724',
        price: 480
    },

    /* Bus Plus Slim */
    {
        features: ['doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'slim'],
        src: '/slim/kpn.png',
        system: 'plus',
        id: '001669',
        price: 470
    },
    {
        features: ['doormen', 'easy-install', 'two-doors', 'security', 'market', 'intercom', 'extra-camera', 'slim'],
        src: '/slim/kp.png',
        system: 'plus',
        id: '001672',
        price: 500
    },

    /* Bus Plus Eko */
    {
        features: ['bw', 'doormen', 'easy-install', 'two-doors', 'security', 'market', 'intercom', 'extra-camera', 'eko'],
        src: '/eko/bwkp.png',
        system: 'plus',
        id: '001692',
        price: 230
    },
    {
        features: ['color', 'doormen', 'easy-install', 'two-doors', 'security', 'market', 'intercom', 'extra-camera', 'eko'],
        src: '/eko/ckp.png',
        system: 'plus',
        id: '001691',
        price: 368
    },

    // Panels
    /* Ft Panel */
    {
        features: ['panel', 'tough-panel'],
        src: '/toughp/gb.png',
        system: 'ft',
        id: '004962',
        price: function(apartment) {
            var price = 78
              , jumps = [12, 28, 44, 60, 76, 92]
            price += apartment * 8
            $.each(jumps, function(i, v){ if(apartment > v) price += 38 })
            return price
        }
    },

    /* Et Panel */
    {
        features: ['panel', 'light-panel'],
        src: '/lightp/sg.png',
        system: 'et',
        id: '004845',
        price: function(apartment) {
            var price = 54
              , jumps = [20, 46, 72, 52, 68, 84]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 11
            $.each(jumps, function(i, v){ if(apartment > v) price += 27 })
            return price            
        }
    },

    /* 4 + n Panel */
    {
        features: ['panel', 'light-panel'],
        src: '/lightp/sg.png',
        system: '4+n',
        id: '004849',
        price: function(apartment) {
            var price = 39
              , jumps = [20, 46, 72, 52, 68, 84]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 11
            $.each(jumps, function(i, v){ if(apartment > v) price += 27 })
            return price            
        }
    },
    {
        features: ['panel', 'tough-panel'],
        src: '/toughp/gb.png',
        system: '4+n',
        id: '004813',
        price: function(apartment) {
            var price = 66
              , jumps = [12, 28, 44, 60, 76, 92]
            price += apartment * 8
            $.each(jumps, function(i, v){ if(apartment > v) price += 38 })
            return price
        }
    },

    /* 8 + n Panel */
    {
        features: ['panel', 'light-panel'],
        src: '/lightp/sg.png',
        system: '8+n',
        id: '004849',
        price: function(apartment) {
            var price = 39
              , jumps = [20, 46, 72, 52, 68, 84]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 11
            $.each(jumps, function(i, v){ if(apartment > v) price += 27 })
            return price            
        }
    },
    {
        features: ['panel', 'tough-panel'],
        src: '/toughp/gb.png',
        system: '8+n',
        id: '004813',
        price: function(apartment) {
            var price = 66
              , jumps = [12, 28, 44, 60, 76, 92]
            price += apartment * 8
            $.each(jumps, function(i, v){ if(apartment > v) price += 38 })
            return price
        }
    },

    /* Bus Plus + n Panel */
    {
        features: ['panel', 'light-base', 'light-panel'],
        src: '/lightp/gb.png',
        system: 'plus+n',
        id: '008317',
        price: function(apartment) {
            var price = 340
              , jumps = [10, 20, 40, 52, 68, 84]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 10
            $.each(jumps, function(i, v){ if(apartment > v) price += 45 })
            return price
        }
    },
    {
        features: ['panel', 'light-base', 'password', 'light-panel'],
        src: '/lightp/kd.png',
        system: 'plus+n',
        id: '008330',
        price: function(apartment) {
            var price = 545
              , jumps = [16, 32, 48, 64, 80, 96]
            if(apartment < 10) apartment = 10
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 10
            $.each(jumps, function(i, v){ if(apartment > v && v == 16) price += 55; else if(apartment > v) price += 45})
            return price
        }
    },

    /* Bus Plus Panel */
    {
        features: ['panel', 'light-base', 'button', 'light-panel'],
        src: '/lightp/gb.png',
        system: 'plus',
        id: '008317',
        price: function(apartment) {
            var price = 340
              , jumps = [10, 20, 40, 52, 68, 84]
              , converter = (apartment / 16 - apartment / 16 % 1) * 50
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 10
            $.each(jumps, function(i, v){ if(apartment > v) price += 45 })
            price += converter
            return price
        }
    },
    {
        features: ['panel', 'light-base', 'name-search', 'password', 'digital', 'light-panel'],
        src: '/lightp/gd.png',
        system: 'plus',
        id: '003480',
        price: function(apartment) {
            return 540
        }
    },
    {
        features: ['panel', 'light-base', 'tough-panel'],
        src: '/toughp/bd.png',
        system: 'plus',
        id: '008312',
        price: function(apartment) {
            return 640
        }
    },
    {
        features: ['panel', 'luks'],
        src: '/luksp/pc.png',
        system: 'plus',
        id: '003479',
        price: function(apartment) {
            return 850
        }
    }
]

var systems = {
    'plus': function(state) {
	    var video = 44 + (state.apartment * 0.2 * 30)
          , cable = (state.apartment * 7 + 100 - (state.apartment * 7 % 100)) * 2.1 * 0.7 
          , apartment = state.apartment / state.block
          , power
        if(apartment <= 30)
            power = 110
        else if(apartment <= 60)
            power = 220
        else
            power = 280
        power *= state.block
        return video + power + cable
    },
    'plus+n': function(state) {
	    var video = 44 + (state.apartment * 0.2 * 30)
          , cable = (state.apartment * 7 + 100 - (state.apartment * 7 % 100)) * 2.1 * 2 
          , apartment = state.apartment / state.block
          , power
        if(apartment <= 30)
            power = 110
        else if(apartment <= 60)
            power = 220
        else
            power = 280
        power *= state.block
        return video + power + cable
    },
    '8+n': function(state) {
        var apartment = state.apartment / state.block
          , cable = state.apartment * 7 * 2 * 2.1
          , cu
        if($.inArray('two-doors', state.extra.monitors) != -1 || $.inArray('doormen', state.extra.monitors) != -1)
            cu = 250
        else if(apartment > 25)
            cu = 190
        else
            cu = 130
        cu*= state.block
        return cable + cu
    },
    '4+n': function(state) {
        var cable = state.apartment * 7 * 1.3  * 2
          , cu = 140
        cu*= state.block
    	return cu + cable
    },
    'et': function(state) {
        var cable = state.apartment * 7 * 1.3  * 2
          , cu = 150
        cu*= state.block
    	return cable + cu
    },
    'ft': function(state) {
        var apartment = state.apartment / state.block
          , cable = state.apartment * 7 * 1.3 * 2
          , cu
        if($.inArray('two-doors', state.extra.monitors) != -1)
            cu = 220
        else
            cu = 170
        cu*= state.block
        return cable + cu
    }, 
    'villa': function(state) {
    	return 65
    }
}

var work = {
    'plus': function(state) {
        return state.apartment * 40
    }, 
    'plus+n': function(state) {
        return state.apartment * 50
    },
    'villa': function(state) {
        if(state.monitor.id == '001389') return 150
        else return 200
    },
    '8+n': function(state) {
        return state.price * 0.3 + state.apartment * 15 
    },
    '4+n': function(state) {
        return state.price * 0.3 + state.apartment * 15 
    },
    'ft': function(state) {
        return state.price * 0.25 + state.apartment * 15 
    },
    'et': function(state) {
        return state.price * 0.25 + state.apartment * 15 
    }
}

var extras = {
    'extra-monitor': function(state) {
        if(state.monitor == "001421") return 530 
        if(state.monitor == "001390") return 220 + 76
        if(state.monitor == "001389") return 330 + 76
        if(state.monitor == "001344") return 46
    },
    'security': function(state) { 
        return 350 + 80 + 210
    },
    'extra-camera': function(state) { 
        var cable = state.block * 70 * 2.1 
          , module = state.panel.id == "003479" ? 0 : 70
        return cable + module + 360 + 44 + 80 + 100
    },
    'two-doors': function(state) { 
        if(state.monitor.system == "villa" && state.monitor == "001421") return 330
        else return state.panel.price(state.apartment)
    },
    'market': function(state) { 
        return 150 
    },
    'doormen': function(state) { 
        if(state.monitor.system == "plus" || state.monitor.system == "plus+n")
            return 150 
        else if(state.monitor.system == "et" || state.monitor.system == "ft")
            return 60
        else 
            return 45
    },
    'light-base': function(state) { 
        var basePrice = 0
        if(state.panel.id == "008312") basePrice = 270
        else if(state.panel.id == "003480") basePrice = 250
        else if(state.panel.id == "008317") {
            var apartment = state.apartment / state.block
            if(apartment <= 11) basePrice = 250
            else if(apartment <= 20) basePrice = 290
            else basePrice = 330
        }
        basePrice *= state.block
        return basePrice
    }
}
