// Products information
var products = [
    // Villa sets
    {
        features: ['telefon-villa'],
        src: '/etv/t.png',
        system: 'villa',
        id: '001344',
        price: 330
    },
    {
        features: ['gdl-villa'],
        src: '/7vk/m.png',
        system: 'villa',
        id: '001366',
        price: 910
    },
    {
        features: ['gdm-villa'],
        src: '/43vk/b.png',
        system: 'villa',
        id: '001368',
        price: 800
    },

    // Monitors
    /* Et telefon */
    {
        features: ['doormen', 'telefon'],
        src: '/t/l.jpg',
        system: 'et',
        id: '001072',
        price: 70
    },

    /* Ft telefon */
    {
        features: ['private', 'two-doors', 'better-melody', 'doormen', 'telefon'],
        src: '/t/l.png',
        system: 'ft',
        id: '001061',
        price: 80
    },

    /* 4 + n E SILINECEK */ 
    {
        features: ['e'],
        src: '/e/w.png',
        system: '4+n',
        id: '001033',
        price: 25
    },

    /* 4 + n Kd SILINECEK */
    {
        features: ['kd'],
        src: '/kd/g.png',
        system: '4+n',
        id: '001227',
        price: 25
    },

    /* 8 + n Kd */
    {
        features: ['two-doors', 'better-melody', 'private', 'kd'],
        src: '/kd/g.png',
        system: '8+n',
        id: '001226',
        price: 32
    },
    {
        features: ['two-doors', 'better-melody', 'private', 'doormen', 'adjust-sound', 'kd'],
        src: '/kd/g.png',
        system: '8+n',
        id: '001223',
        price: 34
    },

    /* 8 + n Fnk */
    {
        features: ['two-doors', 'white', 'fnk'],
        src: '/fnk/wkpn.png',
        system: '8+n',
        id: '001430',
        price: 36
    },
    {
        features: ['two-doors', 'gold', 'doormen','adjust-sound', 'fnk'],
        src: '/fnk/gkpn.png',
        system: '8+n',
        id: '001435',
        price: 38
    },
    {
        features: ['two-doors', 'chrome', 'doormen', 'adjust-sound', 'flash', 'fnk'],
        src: '/fnk/mkpn.png',
        system: '8+n',
        id: '001437',
        price: 66
    },

    /* 8 + n Sa */
    {
        features: ['two-doors', 'sa'],
        src: '/sa/dn.png',
        system: '8+n',
        id: '001012',
        price: 36
    },
    {
        features: ['two-doors', 'doormen','sa'],
        src: '/sa/d.png',
        system: '8+n',
        id: '001013',
        price: 38
    },

    /* Bus Plus + n Eko SILINECEK */
    {
        features: ['bw', 'doormen','medium-install', 'eko'],
        src: '/eko/sb.png',
        system: 'plus+n',
        id: '001560',
        price: 250
    },
    {
        features: ['color', 'doormen','medium-install',  'eko'],
        src: '/eko/c.png',
        system: 'plus+n',
        id: '001561',
        price: 310
    },

    /* Bus Plus + n Gdm SILINECEK */
    {
        features: ['2,5', 'doormen', 'white', 'medium-install', 'gdm'],
        src: '/gdm/k25.png',
        system: 'plus+n',
        id: '001702',
        price: 268
    },
    {
        features: ['3,5', 'doormen', 'white', 'medium-install', 'gdm'],
        src: '/gdm/k35.png',
        system: 'plus+n',
        id: '001703',
        price: 300
    },

    /* Bus Plus + n Gdmm SILINECEK */
    {
        features: ['4,3', 'doormen', 'white', 'medium-install', 'gdmm'],
        src: '/gdmm/knkp.png',
        system: 'plus+n',
        id: '001704',
        price: 300
    },



    /* Bus Plus Gdm */
    {
        features: ['2,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdm'],
        src: '/gdm/k25.png',
        system: 'plus',
        id: '001721',
        price: 336
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdm'],
        src: '/gdm/k35.png',
        system: 'plus',
        id: '001720',
        price: 370
    },

    /* SILINECEK */
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdm'],
        src: '/gdm/kkp.png',
        system: 'plus',
        id: '001719',
        price: 360
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'flash', 'gold','gdm'],
        src: '/gdm/gmn.png',
        system: 'plus',
        id: '001729',
        price: 380
    },


    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'flash', 'intercom','memory', 'gold','gdm'],
        src: '/gdm/gm.png',
        system: 'plus',
        id: '001724',
        price: 580
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdmm'],
        src: '/gdmm/knkp.png',
        system: 'plus',
        id: '001105/MODERN/KREM',
        price: 370
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'bronz','gdmm'],
        src: '/gdmm/bnkp.png',
        system: 'plus',
        id: '001105/MODERN/BRONZ',
        price: 374
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'antrasit','gdmm'],
        src: '/gdmm/ankp.png',
        system: 'plus',
        id: '001105/MODERN/ANTRASIT',
        price: 374
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'silver','gdmm'],
        src: '/gdmm/snkp.png',
        system: 'plus',
        id: '001105/MODERN/SILVER',
        price: 374
    },

    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdmk'],
        src: '/gdmk/bnkp.png',
        system: 'plus',
        id: '001105/KARE/BEYAZ',
        price: 374
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'black','gdmk'],
        src: '/gdmk/snkp.png',
        system: 'plus',
        id: '001105/KARE/SIYAH',
        price: 374
    },

    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'handsfree', 'white','gdmm'],
        src: '/gdmm/knkp.png',
        system: 'plus',
        id: '001107/MODERN/KREM',
        price: 390
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'handsfree', 'bronz','gdmm'],
        src: '/gdmm/bnkp.png',
        system: 'plus',
        id: '001107/MODERN/BRONZ',
        price: 394
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'handsfree', 'antrasit','gdmm'],
        src: '/gdmm/ankp.png',
        system: 'plus',
        id: '001107/MODERN/ANTRASIT',
        price: 394
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'handsfree', 'silver','gdmm'],
        src: '/gdmm/snkp.png',
        system: 'plus',
        id: '001107/MODERN/SILVER',
        price: 394
    },

    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white', 'handsfree', 'gdmk'],
        src: '/gdmk/bnkp.png',
        system: 'plus',
        id: '001107/KARE/BEYAZ',
        price: 394
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'black', 'handsfree', 'gdmk'],
        src: '/gdmk/snkp.png',
        system: 'plus',
        id: '001107/KARE/SIYAH',
        price: 394
    },

    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdmm'],
        src: '/gdmm/kkp.png',
        system: 'plus',
        id: '001106/MODERN/KREM',
        price: 390
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'bronz','gdmm'],
        src: '/gdmm/bkp.png',
        system: 'plus',
        id: '001106/MODERN/BRONZ',
        price: 394
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'antrasit','gdmm'],
        src: '/gdmm/akp.png',
        system: 'plus',
        id: '001106/MODERN/ANTRASIT',
        price: 394
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'silver','gdmm'],
        src: '/gdmm/skp.png',
        system: 'plus',
        id: '001106/MODERN/SILVER',
        price: 394
    },

    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdmk'],
        src: '/gdmk/bkp.png',
        system: 'plus',
        id: '001106/KARE/BEYAZ',
        price: 394
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'black','gdmk'],
        src: '/gdmk/skp.png',
        system: 'plus',
        id: '001106/KARE/SIYAH',
        price: 394
    },

    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdmm'],
        src: '/gdmm/kkp.png',
        system: 'plus',
        id: '001108/MODERN/KREM',
        price: 410
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'bronz','gdmm'],
        src: '/gdmm/bkp.png',
        system: 'plus',
        id: '001108/MODERN/BRONZ',
        price: 414
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'antrasit','gdmm'],
        src: '/gdmm/akp.png',
        system: 'plus',
        id: '001108/MODERN/ANTRASIT',
        price: 414
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'silver','gdmm'],
        src: '/gdmm/skp.png',
        system: 'plus',
        id: '001108/MODERN/SILVER',
        price: 414
    },

    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdmk'],
        src: '/gdmk/bkp.png',
        system: 'plus',
        id: '001108/KARE/BEYAZ',
        price: 414
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'black','gdmk'],
        src: '/gdmk/skp.png',
        system: 'plus',
        id: '001108/KARE/SIYAH',
        price: 414
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-button','white','43s'],
        src: '/43s/b.png',
        system: 'plus',
        id: '001122',
        price: 440
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-button', 'black','43s'],
        src: '/43s/s.png',
        system: 'plus',
        id: '001120',
        price: 440
    },


    /* 1122D 1120D GELSIN */


    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-screen', 'white','43s'],
        src: '/43s/bt.png',
        system: 'plus',
        id: '001162',
        price: 550
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-screen', 'black','43s'],
        src: '/43s/st.png',
        system: 'plus',
        id: '001160',
        price: 550
    },

    {
        features: ['7', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-button', 'white','7s'],
        src: '/7s/bb.png',
        system: 'plus',
        id: '001127',
        price: 620
    },
    {
        features: ['7', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-button', 'black','7s'],
        src: '/7s/sb.png',
        system: 'plus',
        id: '001125',
        price: 620
    },
    {
        features: ['7', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-screen', 'white','7s'],
        src: '/7s/b.png',
        system: 'plus',
        id: '001132',
        price: 700
    },
    {
        features: ['7', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-screen', 'black','7s'],
        src: '/7s/s.png',
        system: 'plus',
        id: '001130',
        price: 700
    },

    /* Bus Plus Gdl */
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/knkp.png',
        system: 'plus',
        id: '001730/KREM',
        price: 556
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/bnkp.png',
        system: 'plus',
        id: '001730/BRONZ',
        price: 560
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/ankp.png',
        system: 'plus',
        id: '001730/ANTRASIT',
        price: 560
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'silver','gdl'],
        src: '/gdl/ankp.png',
        system: 'plus',
        id: '001730/SILVER',
        price: 560
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/knkp.png',
        system: 'plus',
        id: '001733/KREM',
        price: 576
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/bnkp.png',
        system: 'plus',
        id: '001733/BRONZ',
        price: 580
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/ankp.png',
        system: 'plus',
        id: '001733/ANTRASIT',
        price: 580
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'silver','gdl'],
        src: '/gdl/ankp.png',
        system: 'plus',
        id: '001733/SILVER',
        price: 580
    },

    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/k.png',
        system: 'plus',
        id: '001731/KREM',
        price: 576
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/b.png',
        system: 'plus',
        id: '001731/BRONZ',
        price: 580
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/a.png',
        system: 'plus',
        id: '001731/ANTRASIT',
        price: 580
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'silver','gdl'],
        src: '/gdl/a.png',
        system: 'plus',
        id: '001731/SILVER',
        price: 580
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/k.png',
        system: 'plus',
        id: '001734/KREM',
        price: 596
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/b.png',
        system: 'plus',
        id: '001734/BRONZ',
        price: 600
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/a.png',
        system: 'plus',
        id: '001734/ANTRASIT',
        price: 600
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'silver','gdl'],
        src: '/gdl/a.png',
        system: 'plus',
        id: '001734/SILVER',
        price: 600
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'white','gdlm'],
        src: '/gdlm/knkp.png',
        system: 'plus',
        id: '001730/MODERN/KREM',
        price: 556
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'bronz','gdlm'],
        src: '/gdlm/bnkp.png',
        system: 'plus',
        id: '001730/MODERN/BRONZ',
        price: 560
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'antrasit','gdlm'],
        src: '/gdlm/ankp.png',
        system: 'plus',
        id: '001730/MODERN/ANTRASIT',
        price: 560
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'silver','gdlm'],
        src: '/gdlm/snkp.png',
        system: 'plus',
        id: '001730/MODERN/SILVER',
        price: 560
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'white','gdlm'],
        src: '/gdlm/knkp.png',
        system: 'plus',
        id: '001733/MODERN/KREM',
        price: 576
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'bronz','gdlm'],
        src: '/gdlm/bnkp.png',
        system: 'plus',
        id: '001733/MODERN/BRONZ',
        price: 580
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'antrasit','gdlm'],
        src: '/gdlm/ankp.png',
        system: 'plus',
        id: '001733/MODERN/ANTRASIT',
        price: 580
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'silver','gdlm'],
        src: '/gdlm/snkp.png',
        system: 'plus',
        id: '001733/MODERN/SILVER',
        price: 580
    },

    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'white','gdlm'],
        src: '/gdlm/kkp.png',
        system: 'plus',
        id: '001731/MODERN/KREM',
        price: 576
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'bronz','gdlm'],
        src: '/gdlm/bkp.png',
        system: 'plus',
        id: '001731/MODERN/BRONZ',
        price: 580
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'antrasit','gdlm'],
        src: '/gdlm/akp.png',
        system: 'plus',
        id: '001731/MODERN/ANTRASIT',
        price: 580
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'silver','gdlm'],
        src: '/gdlm/skp.png',
        system: 'plus',
        id: '001731/MODERN/SILVER',
        price: 580
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'white','gdlm'],
        src: '/gdlm/kkp.png',
        system: 'plus',
        id: '001734/MODERN/KREM',
        price: 596
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'bronz','gdlm'],
        src: '/gdlm/bkp.png',
        system: 'plus',
        id: '001734/MODERN/BRONZ',
        price: 590
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'antrasit','gdlm'],
        src: '/gdlm/akp.png',
        system: 'plus',
        id: '001734/MODERN/ANTRASIT',
        price: 590
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'silver','gdlm'],
        src: '/gdlm/skp.png',
        system: 'plus',
        id: '001734/MODERN/SILVER',
        price: 590
    },

    /* Bus Plus Gt */
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'gt'],
        src: '/gt/35.png',
        system: 'plus',
        id: '001666',
        price: 370
    },
    {
        features: ['doormen', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'gt'],
        src: '/gt/35.png',
        system: 'plus',
        id: '001667',
        price: 390
    },

    /* Bus Plus Eko */
    {
        features: ['bw', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'eko'],
        src: '/eko/sb.png',
        system: 'plus',
        id: '001562',
        price: 316
    },
    {
        features: ['color', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'eko'],
        src: '/eko/c.png',
        system: 'plus',
        id: '001565',
        price: 370
    },
    {
        features: ['bw', 'doormen', 'easy-install', 'two-doors', 'security', 'market', 'intercom', 'extra-camera', 'eko'],
        src: '/eko/sb.png',
        system: 'plus',
        id: '001692',
        price: 336
    },
    {
        features: ['color', 'doormen', 'easy-install', 'two-doors', 'security', 'market', 'intercom', 'extra-camera', 'eko'],
        src: '/eko/c.png',
        system: 'plus',
        id: '001691',
        price: 390
    },

    // Panels
    /* Ft Panel */
    {
        features: ['panel', 'tough-panel'],
        src: '/toughp/gb.png',
        system: 'ft',
        id: '004962',
        price: function(apartment) {
            var price = 148
              , jumps = [12, 28, 44, 60, 76, 92]
            price += apartment * 10
            $.each(jumps, function(i, v){ if(apartment > v) price += 72 }) // Yan sira farki
            return price
        }
	// Nasil bulduk?
	// Paket listede 12 liden 11 li cikartilir ondan da sube fiyati cikartilir
	// ondan da buton fiyati cikartinca ek panelin taban fiyati bulunur
    },

    /* Et Panel */
    {
        features: ['panel', 'light-panel'],
        src: '/lightp/sg.png',
        system: 'et',
        id: '004845',
        price: function(apartment) {
            var price = 136 // en kucukten buton farki cikartilir
              , jumps = [20, 46, 72, 98]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 16 // usttekinden alttakini cikartip
            $.each(jumps, function(i, v){ if(apartment > v) price += 50 })
            return price            
        }
    },

    /* 4 + n Panel SILINECEK alttakiyle beraber */
    {
        features: ['panel', 'light-panel'],
        src: '/lightp/sg.png',
        system: '4+n',
        id: '004849',
        price: function(apartment) {
            var price = 54
              , jumps = [20, 46, 72, 98]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 14
            $.each(jumps, function(i, v){ if(apartment > v) price += 34 })
            return price            
        }
    },
    {
        features: ['panel', 'tough-panel'],
        src: '/toughp/gb.png',
        system: '4+n',
        id: '004813',
        price: function(apartment) {
            var price = 82
              , jumps = [12, 28, 44, 60, 76, 92]
            price += apartment * 10
            $.each(jumps, function(i, v){ if(apartment > v) price += 54 })
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
            var price = 74
              , jumps = [20, 46, 72, 52, 68, 84]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 16
            $.each(jumps, function(i, v){ if(apartment > v) price += 46 })
            return price            
        }
    },
    {
        features: ['panel', 'tough-panel'],
        src: '/toughp/gb.png',
        system: '8+n',
        id: '004813',
        price: function(apartment) {
            var price = 98
              , jumps = [12, 28, 44, 60, 76, 92]
            price += apartment * 12
            $.each(jumps, function(i, v){ if(apartment > v) price += 72 })
            return price
        }
    },

    /* Bus Plus + n Panel SILINECEK ALTTAKIYLE*/
    {
        features: ['panel', 'light-base', 'light-panel'],
        src: '/lightp/gb.png',
        system: 'plus+n',
        id: '008317',
        price: function(apartment) {
            var price = 416
              , jumps = [10, 20, 40, 52, 68, 84]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 14
            $.each(jumps, function(i, v){ if(apartment > v) price += 62 })
            return price
        }
    },
    {
        features: ['panel', 'light-base', 'password', 'light-panel'],
        src: '/lightp/kd.png',
        system: 'plus+n',
        id: '008330',
        price: function(apartment) {
            var price = 642
              , jumps = [16, 32, 48, 64, 80, 96]
            if(apartment < 10) apartment = 10
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 14
            // $.each(jumps, function(i, v){ if(apartment > v && v == 16) price += 72; else if(apartment > v) price += 60})
            $.each(jumps, function(i, v){ if(apartment > v)  price += 62})
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
            var price = 458
              , jumps = [10, 20, 40, 52, 68, 84]
              , converter = (apartment / 16 - apartment / 16 % 1) * 120
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 16
            $.each(jumps, function(i, v){ if(apartment > v) price += 72 }) // Yan siradan butun buton maliyetini cikartinca bulunuyor
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
            return 700
        }
    },
    {
        features: ['panel', 'light-base', 'tough-panel'],
        src: '/toughp/bd.png',
        system: 'plus',
        id: '008312',
        price: function(apartment) {
            return 840
        }
    },
    //FIXME: urun sablon ekle, isikli altlikli resim
    {
        features: ['panel', 'city', 'light-base'],
        src: '/city/s.png',
        system: 'plus',
        id: '003485',
        price: function(apartment) {
            return 1150
        }
    },
    //FIXME: urunu sablon ekle
    {
        features: ['panel', 'crea', 'light-base'],
        src: '/crea/m.png',
        system: 'plus',
        id: '003491',
        price: function(apartment) {
            return 1020
        }
    },
    //FIXME: urunu sablon ekle
    // {
    //     features: ['panel', 'buttons', 'crea'],
    //     src: '/crea/m.png',
    //     system: 'plus',
    //     id: '003491/BUTONLU',
    //     price: function(apartment) {
    //         // 16 daire ve katlarinda 70 lira buton donusturucu fiyati (converter)
    //         // diger butonlar geldiginde boy standartli panele gore fiyat ekle
    //         // light-base ini ayarla eger buton sayisi artarsa
    //         var price = 850
    //           , jumps = [16, 32, 48, 64, 80, 96]
    //         if(apartment < 10) apartment = 10
    //         if(apartment % 2 != 0) apartment++
    //         price += apartment / 2 * 12
    //         $.each(jumps, function(i, v){ if(apartment > v && v == 16) price += 72; else if(apartment > v) price += 60})
    //         return price
    //     }
    // },
    {
        features: ['panel', 'luks'],
        src: '/luksp/pc.png',
        system: 'plus',
        id: '003479',
        price: function(apartment) {
            return 1000
        }
    },
    //FIXME: urun sablon ekle
    {
        features: ['panel', 'vision'],
        src: '/vision/m.png',
        system: 'plus',
        id: '003488',
        price: function(apartment) {
            return 1250
        }
    }
]

var systems = {
    'plus': function(state) {
	    var video = 98 + (state.apartment * 0.2 * 44)
          // , cable = (state.apartment * 7 + 100 - (state.apartment * 7 % 100)) * 2.7 * 0.7  // 23 Subat 2015, buraya yeni bina cok gelmiyor ve cikarinca bizim musteriye verdigimiz teklifle ayni fiyata geliyor burasi
          , apartment = state.apartment / state.block
          , power
        if(apartment <= 30)
            power = 142
        else if(apartment <= 60)
            power = 284
        else
            power = 362
        power *= state.block
        return video + power + cable
    },
    'plus+n': function(state) { // SILINECEK
	    var video = 70 + (state.apartment * 0.2 * 40)
          , cable = (state.apartment * 7 + 100 - (state.apartment * 7 % 100)) * 2.7 * 2 
          , apartment = state.apartment / state.block
          , power
        if(apartment <= 30)
            power = 130
        else if(apartment <= 60)
            power = 260
        else
            power = 350
        power *= state.block
        return video + power + cable
    },
    '8+n': function(state) {
        var apartment = state.apartment / state.block
          , cable = state.apartment * 7 * 2 * 3 // 7 her dairede kulanilan kablo mesafesi, 2 de tolerans, 3 fiyat
          , cu
        if($.inArray('two-doors', state.extra.monitors) != -1 || $.inArray('doormen', state.extra.monitors) != -1)
            cu = 320
        else if(apartment > 25)
            cu = 260
        else
            cu = 200
        cu*= state.block
        return cable + cu
    },
    '4+n': function(state) { // SILINECEK
        var cable = state.apartment * 7 * 1.7  * 2
          , cu = 166
        cu *= state.block
    	return cu + cable
    },
    'et': function(state) {
        var cable = state.apartment * 7 * 2  * 2
          , cu = 214
        cu*= state.block
    	return cable + cu
    },
    'ft': function(state) {
        var apartment = state.apartment / state.block
          , cable = state.apartment * 7 * 2 * 2
          , cu
        if($.inArray('two-doors', state.extra.monitors) != -1)
            cu = 310
        else
            cu = 250
        cu*= state.block
        return cable + cu
    }, 
    'villa': function(state) {
    	return 80 // kablo fiyati
    }
}

var work = {
    'plus': function(state) {
        return state.apartment * 50
    }, 
    'plus+n': function(state) { // SILINECEK
        return state.apartment * 50
    },
    'villa': function(state) {
        return 200
    },
    '8+n': function(state) {
        return state.price * 0.3 + state.apartment * 15 
    },
    '4+n': function(state) { // SILINECEK
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
        if(state.monitor == "001366") return 580 + 122 // urun + besleme (7' villa kit)
        if(state.monitor == "001368") return 390 + 122 // "", (4.3 villa kit)
        if(state.monitor == "001344") return 70 + 12 // et telefon + konsept panel butonu
    },
    'security': function(state) { 
        return 500 + 122 + 300 // guvenlik konsolu + guc kaynagi + kablo 100 metre
    },
    // Bunlar icin yeni kod acildi (alarm, memory)
    'alarm': function(state) {
        return 100
    },
    'memory': function(state) {
        return 160
    },
    'extra-camera': function(state) { 
        var cable = state.block * 70 * 2.6 // 2.6 kablo maliyeti koaks
          , module = state.panel.id == "003479" ? 0 : 120 // 120 lira kamera secme modulu
        return cable + module + 550 + 60 + 100 + 100 // + guvenlik kamerasi + adaptor + iscilik + kablo
    },
    'two-doors': function(state) { 
        if(state.monitor.system == "villa" && state.monitor == "001366") return 384
        else if(state.monitor.system == "villa" && state.monitor == "001368") return 384
        else if(state.monitor.system == "villa" && state.monitor == "001454") return 450
        else return state.panel.price(state.apartment)
    },
    'market': function(state) { 
        return 200  // uyarlama fiyat, cihaz + iscilik + kablo
    },
    'doormen': function(state) { 
        if(state.monitor.system == "plus" || state.monitor.system == "plus+n")
            return 200
        else if(state.monitor.system == "et" || state.monitor.system == "ft")
            return 100 // uyarlama fiyat
        else 
            return 48
    },
    'light-base': function(state) { 
        var basePrice = 0
        if(state.panel.id == "008312" || state.panel.id == "003485" || state.panel.id == "003491") basePrice = 380
        else if(state.panel.id == "003480") basePrice = 380
        else if(state.panel.id == "008317") {
            var apartment = state.apartment / state.block
            if(apartment <= 11) basePrice = 380
            else if(apartment <= 20) basePrice = 410
            else basePrice = 460
        }
        basePrice *= state.block
        return basePrice
    }
}

