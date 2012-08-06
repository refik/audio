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
        src: '/evk/ekobw.png',
        system: 'villa',
        id: '001390',
        price: 450
    },
    {
        features: ['c', 'eko-villa'],
        src: '/evk/ekoc.png',
        system: 'villa',
        id: '001389',
        price: 550
    },
    {
        features: ['x-villa'],
        src: '/56vk/x.png',
        system: 'villa',
        id: '001421',
        price: 650
    },
    {
        features: ['gdl-villa'],
        src: '/7vk/a.png',
        system: 'villa',
        id: '001366',
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
        src: '/t/l.png',
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
        price: 19
    },

    /* 4 + n Kd */
    {
        features: ['kd'],
        src: '/kd/g.png',
        system: '4+n',
        id: '001227',
        price: 19
    },

    /* 8 + n Kd */
    {
        features: ['two-doors', 'better-melody', 'private', 'kd'],
        src: '/kd/g.png',
        system: '8+n',
        id: '001226',
        price: 21
    },
    {
        features: ['two-doors', 'better-melody', 'private', 'doormen', 'adjust-sound', 'kd'],
        src: '/kd/g.png',
        system: '8+n',
        id: '001223',
        price: 22
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

    /* Gts Eko */
    {
        features: ['bw', 'doormen', 'eko'],
        src: '/eko/sb.png',
        system: 'gts',
        id: '001678',
        price: 170
    },
    {
        features: ['color', 'doormen', 'eko'],
        src: '/eko/c.png',
        system: 'gts',
        id: '001687',
        price: 260 
    },

    /* Gts Gdm */
    {
        features: ['2,5', 'doormen', 'white','gdm'],
        src: '/gdm/k25.png',
        system: 'gts',
        id: '001750',
        price: 180
    },
    {
        features: ['3,5', 'doormen', 'white', 'gdm'],
        src: '/gdm/k35.png',
        system: 'gts',
        id: '001683',
        price: 210
    },

    /* Bus Plus + n Eko */
    {
        features: ['bw', 'doormen','medium-install', 'eko'],
        src: '/eko/sb.png',
        system: 'plus+n',
        id: '001560',
        price: 200
    },
    {
        features: ['color', 'doormen','medium-install',  'eko'],
        src: '/eko/c.png',
        system: 'plus+n',
        id: '001561',
        price: 290 
    },

    /* Bus Plus + n Gdm */
    {
        features: ['2,5', 'doormen', 'white', 'medium-install', 'gdm'],
        src: '/gdm/k25.png',
        system: 'plus+n',
        id: '001702',
        price: 220
    },
    {
        features: ['3,5', 'doormen', 'white', 'medium-install', 'gdm'],
        src: '/gdm/k35.png',
        system: 'plus+n',
        id: '001703',
        price: 250
    },

    /* Bus Plus Gdm */
    {
        features: ['2,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdm'],
        src: '/gdm/k25.png',
        system: 'plus',
        id: '001721',
        price: 260
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdm'],
        src: '/gdm/k35.png',
        system: 'plus',
        id: '001720',
        price: 290
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'bronz','gdm'],
        src: '/gdm/b.png',
        system: 'plus',
        id: '001720B',
        price: 296
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'antrasit','gdm'],
        src: '/gdm/a.png',
        system: 'plus',
        id: '001720A',
        price: 296
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdm'],
        src: '/gdm/kkp.png',
        system: 'plus',
        id: '001719',
        price: 304
    },
    {
        features: ['3,5', 'handsfree', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'bronz','gdm'],
        src: '/gdm/b.png',
        system: 'plus',
        id: '001705',
        price: 310
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'flash', 'gold','gdm'],
        src: '/gdm/gmn.png',
        system: 'plus',
        id: '001729',
        price: 324
    },
    {
        features: ['3,5', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'antrasit','gdm'],
        src: '/gdm/kpa.png',
        system: 'plus',
        id: '001706',
        price: 324
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'flash', 'intercom','memory', 'gold','gdm'],
        src: '/gdm/gm.png',
        system: 'plus',
        id: '001724',
        price: 460
    },

    /* Bus Plus Gdl */
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/knkp.png',
        system: 'plus',
        id: '001730/KREM',
        price: 444
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/bnkp.png',
        system: 'plus',
        id: '001730/BRONZ',
        price: 450
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/ankp.png',
        system: 'plus',
        id: '001730/ANTRASIT',
        price: 450
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/knkp.png',
        system: 'plus',
        id: '001733/KREM',
        price: 464
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/bnkp.png',
        system: 'plus',
        id: '001733/BRONZ',
        price: 470
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/ankp.png',
        system: 'plus',
        id: '001733/ANTRASIT',
        price: 470
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/k.png',
        system: 'plus',
        id: '001731/KREM',
        price: 458
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/b.png',
        system: 'plus',
        id: '001731/BRONZ',
        price: 464
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/a.png',
        system: 'plus',
        id: '001731/ANTRASIT',
        price: 464
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/k.png',
        system: 'plus',
        id: '001734/KREM',
        price: 478
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/b.png',
        system: 'plus',
        id: '001734/BRONZ',
        price: 484
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/a.png',
        system: 'plus',
        id: '001734/ANTRASIT',
        price: 484
    },

    /* Bus Plus Gt */
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'gt'],
        src: '/gt/35.png',
        system: 'plus',
        id: '001666',
        price: 340
    },
    {
        features: ['doormen', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'gt'],
        src: '/gt/35.png',
        system: 'plus',
        id: '001667',
        price: 354
    },


    /* Bus Plus Slim */
    {
        features: ['doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'slim'],
        src: '/slim/kpn.png',
        system: 'plus',
        id: '001669',
        price: 440
    },
    {
        features: ['doormen', 'easy-install', 'two-doors', 'security', 'market', 'intercom', 'extra-camera', 'slim'],
        src: '/slim/kp.png',
        system: 'plus',
        id: '001672',
        price: 454
    },

    /* Bus Plus Eko */
    {
        features: ['bw', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'eko'],
        src: '/eko/sb.png',
        system: 'plus',
        id: '001562',
        price: 230
    },
    {
        features: ['color', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'eko'],
        src: '/eko/c.png',
        system: 'plus',
        id: '001565',
        price: 320
    },
    {
        features: ['bw', 'doormen', 'easy-install', 'two-doors', 'security', 'market', 'intercom', 'extra-camera', 'eko'],
        src: '/eko/sb.png',
        system: 'plus',
        id: '001692',
        price: 244
    },
    {
        features: ['color', 'doormen', 'easy-install', 'two-doors', 'security', 'market', 'intercom', 'extra-camera', 'eko'],
        src: '/eko/c.png',
        system: 'plus',
        id: '001691',
        price: 334
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

    /* Gts Panel */
    {
        features: ['panel', 'light-panel'],
        src: '/lightp/gb.png',
        system: 'gts',
        id: '004856',
        price: function(apartment) {
            var price = 247
              , jumps = [20, 46, 72, 52, 68, 84]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 11
            $.each(jumps, function(i, v){ if(apartment > v) price += 27 })
            return price            
        }
    },
    {
        features: ['panel', 'light-base', 'password', 'light-panel'],
        src: '/lightp/karma.png',
        system: 'gts',
        id: '004855',
        price: function(apartment) {
            var price = 380
              , kgp = 38
            if(apartment % 2 != 0) apartment++
            if(apartment > 21) price += 16
            price += apartment / 2 * 11
            if(11 < apartment < 21) price = 516
            price += kgp
            return price
        }
    },
    {
        features: ['panel', 'luks'],
        src: '/luksp/pc.png',
        system: 'gts',
        id: '00346X',
        price: function(apartment) {
            return 750
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
    'gts': function(state) {
	    var video = 44 + (state.apartment * 0.2 * 30)
          , cable = (state.apartment * 7 + 100 - (state.apartment * 7 % 100)) * (2.9 + 1.5)
          , cu = 198
          , notColor = -50
        if($.inArray('bw', state.monitor.features) != -1)
            notColor = 0
        cu *= state.block
        return video + cu + cable + notColor
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
        cu *= state.block
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
    'gts': function(state) {
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
    'alarm': function(state) {
        return 80
    },
    'memory': function(state) {
        return 136
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
        else if(state.monitor.system == "gts")
            return 125
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
