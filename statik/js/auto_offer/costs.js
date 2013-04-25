// Products information
var products = [
    // Villa sets
    {
        features: ['telefon-villa'],
        src: '/etv/t.png',
        system: 'villa',
        id: '001344',
        price: 190
    },
    {
        features: ['bw', 'eko-villa'],
        src: '/evk/ekobw.png',
        system: 'villa',
        id: '001390',
        price: 500
    },
    {
        features: ['c', 'eko-villa'],
        src: '/evk/ekoc.png',
        system: 'villa',
        id: '001389',
        price: 600
    },
    {
        features: ['x-villa'],
        src: '/56vk/x.png',
        system: 'villa',
        id: '001421',
        price: 700
    },
    {
        features: ['gdl-villa'],
        src: '/7vk/m.png',
        system: 'villa',
        id: '001366',
        price: 650
    },
    {
        features: ['gdm-villa'],
        src: '/43vk/b.png',
        system: 'villa',
        id: '001368',
        price: 600
    },

    // Monitors
    /* Et telefon */
    {
        features: ['doormen', 'telefon'],
        src: '/t/l.jpg',
        system: 'et',
        id: '001072',
        price: 46
    },

    /* Ft telefon */
    {
        features: ['private', 'two-doors', 'better-melody', 'doormen', 'telefon'],
        src: '/t/l.png',
        system: 'ft',
        id: '001061',
        price: 55
    },

    /* 4 + n E */
    {
        features: ['e'],
        src: '/e/w.png',
        system: '4+n',
        id: '001033',
        price: 22
    },

    /* 4 + n Kd */
    {
        features: ['kd'],
        src: '/kd/g.png',
        system: '4+n',
        id: '001227',
        price: 22
    },

    /* 8 + n Kd */
    {
        features: ['two-doors', 'better-melody', 'private', 'kd'],
        src: '/kd/g.png',
        system: '8+n',
        id: '001226',
        price: 24
    },
    {
        features: ['two-doors', 'better-melody', 'private', 'doormen', 'adjust-sound', 'kd'],
        src: '/kd/g.png',
        system: '8+n',
        id: '001223',
        price: 25
    },

    /* 8 + n Fnk */
    {
        features: ['two-doors', 'white', 'fnk'],
        src: '/fnk/wkpn.png',
        system: '8+n',
        id: '001430',
        price: 27
    },
    {
        features: ['two-doors', 'gold', 'doormen','adjust-sound', 'fnk'],
        src: '/fnk/gkpn.png',
        system: '8+n',
        id: '001435',
        price: 29
    },
    {
        features: ['two-doors', 'chrome', 'doormen', 'adjust-sound', 'flash', 'fnk'],
        src: '/fnk/mkpn.png',
        system: '8+n',
        id: '001437',
        price: 46
    },

    /* 8 + n Sa */
    {
        features: ['two-doors', 'sa'],
        src: '/sa/dn.png',
        system: '8+n',
        id: '001012',
        price: 27
    },
    {
        features: ['two-doors', 'doormen','sa'],
        src: '/sa/d.png',
        system: '8+n',
        id: '001013',
        price: 28
    },

    /* Bus Plus + n Eko */
    {
        features: ['bw', 'doormen','medium-install', 'eko'],
        src: '/eko/sb.png',
        system: 'plus+n',
        id: '001560',
        price: 230
    },
    {
        features: ['color', 'doormen','medium-install',  'eko'],
        src: '/eko/c.png',
        system: 'plus+n',
        id: '001561',
        price: 300
    },

    /* Bus Plus + n Gdm */
    {
        features: ['2,5', 'doormen', 'white', 'medium-install', 'gdm'],
        src: '/gdm/k25.png',
        system: 'plus+n',
        id: '001702',
        price: 240
    },
    {
        features: ['3,5', 'doormen', 'white', 'medium-install', 'gdm'],
        src: '/gdm/k35.png',
        system: 'plus+n',
        id: '001703',
        price: 270
    },

    /* Bus Plus Gdm */
    {
        features: ['2,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdm'],
        src: '/gdm/k25.png',
        system: 'plus',
        id: '001721',
        price: 280
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdm'],
        src: '/gdm/k35.png',
        system: 'plus',
        id: '001720',
        price: 310
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'bronz','gdm'],
        src: '/gdm/b.png',
        system: 'plus',
        id: '001720B',
        price: 314
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'antrasit','gdm'],
        src: '/gdm/a.png',
        system: 'plus',
        id: '001720A',
        price: 314
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdm'],
        src: '/gdm/kkp.png',
        system: 'plus',
        id: '001719',
        price: 330
    },
    {
        features: ['3,5', 'handsfree', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'bronz','gdm'],
        src: '/gdm/b.png',
        system: 'plus',
        id: '001705',
        price: 330
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'flash', 'gold','gdm'],
        src: '/gdm/gmn.png',
        system: 'plus',
        id: '001729',
        price: 350
    },
    {
        features: ['3,5', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'antrasit','gdm'],
        src: '/gdm/kpa.png',
        system: 'plus',
        id: '001706',
        price: 350
    },
    {
        features: ['3,5', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'flash', 'intercom','memory', 'gold','gdm'],
        src: '/gdm/gm.png',
        system: 'plus',
        id: '001724',
        price: 500
    },

    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdmm'],
        src: '/gdmm/knkp.png',
        system: 'plus',
        id: '001105/MODERN/KREM',
        price: 326
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'bronz','gdmm'],
        src: '/gdmm/bnkp.png',
        system: 'plus',
        id: '001105/MODERN/BRONZ',
        price: 330
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'antrasit','gdmm'],
        src: '/gdmm/ankp.png',
        system: 'plus',
        id: '001105/MODERN/ANTRASIT',
        price: 330
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'silver','gdmm'],
        src: '/gdmm/snkp.png',
        system: 'plus',
        id: '001105/MODERN/SILVER',
        price: 330
    },

    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white','gdmk'],
        src: '/gdmk/bnkp.png',
        system: 'plus',
        id: '001105/KARE/BEYAZ',
        price: 330
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'black','gdmk'],
        src: '/gdmk/snkp.png',
        system: 'plus',
        id: '001105/KARE/SIYAH',
        price: 330
    },

    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'handsfree', 'white','gdmm'],
        src: '/gdmm/knkp.png',
        system: 'plus',
        id: '001107/MODERN/KREM',
        price: 346
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'handsfree', 'bronz','gdmm'],
        src: '/gdmm/bnkp.png',
        system: 'plus',
        id: '001107/MODERN/BRONZ',
        price: 350
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'handsfree', 'antrasit','gdmm'],
        src: '/gdmm/ankp.png',
        system: 'plus',
        id: '001107/MODERN/ANTRASIT',
        price: 350
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'handsfree', 'silver','gdmm'],
        src: '/gdmm/snkp.png',
        system: 'plus',
        id: '001107/MODERN/SILVER',
        price: 350
    },

    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'white', 'handsfree', 'gdmk'],
        src: '/gdmk/bnkp.png',
        system: 'plus',
        id: '001107/KARE/BEYAZ',
        price: 350
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'black', 'handsfree', 'gdmk'],
        src: '/gdmk/snkp.png',
        system: 'plus',
        id: '001107/KARE/SIYAH',
        price: 350
    },

    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdmm'],
        src: '/gdmm/kkp.png',
        system: 'plus',
        id: '001106/MODERN/KREM',
        price: 346
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'bronz','gdmm'],
        src: '/gdmm/bkp.png',
        system: 'plus',
        id: '001106/MODERN/BRONZ',
        price: 350
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'antrasit','gdmm'],
        src: '/gdmm/akp.png',
        system: 'plus',
        id: '001106/MODERN/ANTRASIT',
        price: 350
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'silver','gdmm'],
        src: '/gdmm/skp.png',
        system: 'plus',
        id: '001106/MODERN/SILVER',
        price: 350
    },

    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdmk'],
        src: '/gdmk/bkp.png',
        system: 'plus',
        id: '001106/KARE/BEYAZ',
        price: 350
    },
    {
        features: ['4,3', 'doormen', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'black','gdmk'],
        src: '/gdmk/skp.png',
        system: 'plus',
        id: '001106/KARE/SIYAH',
        price: 350
    },

    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdmm'],
        src: '/gdmm/kkp.png',
        system: 'plus',
        id: '001108/MODERN/KREM',
        price: 366
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'bronz','gdmm'],
        src: '/gdmm/bkp.png',
        system: 'plus',
        id: '001108/MODERN/BRONZ',
        price: 370
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'antrasit','gdmm'],
        src: '/gdmm/akp.png',
        system: 'plus',
        id: '001108/MODERN/ANTRASIT',
        price: 370
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'silver','gdmm'],
        src: '/gdmm/skp.png',
        system: 'plus',
        id: '001108/MODERN/SILVER',
        price: 370
    },

    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'white','gdmk'],
        src: '/gdmk/bkp.png',
        system: 'plus',
        id: '001108/KARE/BEYAZ',
        price: 370
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'black','gdmk'],
        src: '/gdmk/skp.png',
        system: 'plus',
        id: '001108/KARE/SIYAH',
        price: 370
    },

    // FIXME:  Urun sablon ekle
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-button','white','43s'],
        src: '/43s/b.png',
        system: 'plus',
        id: '001122',
        price: 380
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-button', 'black','43s'],
        src: '/43s/s.png',
        system: 'plus',
        id: '001120',
        price: 380
    },

    // FIXME:  Urun sablon ekle
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-screen', 'white','43s'],
        src: '/43s/bt.png',
        system: 'plus',
        id: '001162',
        price: 450
    },
    {
        features: ['4,3', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-screen', 'black','43s'],
        src: '/43s/st.png',
        system: 'plus',
        id: '001160',
        price: 450
    },

    // FIXME:  Urun sablon ekle
    {
        features: ['7', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-button', 'white','7s'],
        src: '/7s/bb.png',
        system: 'plus',
        id: '001127',
        price: 520
    },
    {
        features: ['7', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-button', 'black','7s'],
        src: '/7s/sb.png',
        system: 'plus',
        id: '001125',
        price: 520
    },
    {
        features: ['7', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-screen', 'white','7s'],
        src: '/7s/b.png',
        system: 'plus',
        id: '001132',
        price: 600
    },
    {
        features: ['7', 'doormen', 'handsfree', 'pick-melody', 'call-control', 'easy-install', 'two-doors', 'market', 'security', 'extra-camera', 'intercom', 'touch-screen', 'black','7s'],
        src: '/7s/s.png',
        system: 'plus',
        id: '001130',
        price: 600
    },

    /* Bus Plus Gdl */
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/knkp.png',
        system: 'plus',
        id: '001730/KREM',
        price: 466
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/bnkp.png',
        system: 'plus',
        id: '001730/BRONZ',
        price: 470
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/ankp.png',
        system: 'plus',
        id: '001730/ANTRASIT',
        price: 470
    },
    // FIXME: Resmini degisti 
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'silver','gdl'],
        src: '/gdl/ankp.png',
        system: 'plus',
        id: '001730/SILVER',
        price: 470
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/knkp.png',
        system: 'plus',
        id: '001733/KREM',
        price: 486
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/bnkp.png',
        system: 'plus',
        id: '001733/BRONZ',
        price: 490
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/ankp.png',
        system: 'plus',
        id: '001733/ANTRASIT',
        price: 490
    },
    // FIXME: resmini degistir
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'silver','gdl'],
        src: '/gdl/ankp.png',
        system: 'plus',
        id: '001733/SILVER',
        price: 490
    },

    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/k.png',
        system: 'plus',
        id: '001731/KREM',
        price: 486
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/b.png',
        system: 'plus',
        id: '001731/BRONZ',
        price: 490
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/a.png',
        system: 'plus',
        id: '001731/ANTRASIT',
        price: 490
    },
    // FIXME: urun sablon ekle, resim ekle
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'silver','gdl'],
        src: '/gdl/a.png',
        system: 'plus',
        id: '001731/SILVER',
        price: 490
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'white','gdl'],
        src: '/gdl/k.png',
        system: 'plus',
        id: '001734/KREM',
        price: 506
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'bronz','gdl'],
        src: '/gdl/b.png',
        system: 'plus',
        id: '001734/BRONZ',
        price: 510
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'antrasit','gdl'],
        src: '/gdl/a.png',
        system: 'plus',
        id: '001734/ANTRASIT',
        price: 510
    },
    // FIXME: resim ekle
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'silver','gdl'],
        src: '/gdl/a.png',
        system: 'plus',
        id: '001734/SILVER',
        price: 510
    },



    // FIXME: urun sablon ekle
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'white','gdlm'],
        src: '/gdlm/knkp.png',
        system: 'plus',
        id: '001730/KREM',
        price: 466
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'bronz','gdlm'],
        src: '/gdlm/bnkp.png',
        system: 'plus',
        id: '001730/BRONZ',
        price: 470
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'antrasit','gdlm'],
        src: '/gdlm/ankp.png',
        system: 'plus',
        id: '001730/ANTRASIT',
        price: 470
    },
    {
        features: ['doormen', 'two-doors', 'security', 'extra-camera', 'silver','gdlm'],
        src: '/gdlm/snkp.png',
        system: 'plus',
        id: '001730/SILVER',
        price: 470
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'white','gdlm'],
        src: '/gdlm/knkp.png',
        system: 'plus',
        id: '001733/KREM',
        price: 486
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'bronz','gdlm'],
        src: '/gdlm/bnkp.png',
        system: 'plus',
        id: '001733/BRONZ',
        price: 490
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'antrasit','gdlm'],
        src: '/gdlm/ankp.png',
        system: 'plus',
        id: '001733/ANTRASIT',
        price: 490
    },
    {
        features: ['doormen', 'handsfree', 'two-doors', 'security', 'extra-camera', 'silver','gdlm'],
        src: '/gdlm/snkp.png',
        system: 'plus',
        id: '001733/SILVER',
        price: 490
    },

    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'white','gdlm'],
        src: '/gdlm/kkp.png',
        system: 'plus',
        id: '001731/KREM',
        price: 486
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'bronz','gdlm'],
        src: '/gdlm/bkp.png',
        system: 'plus',
        id: '001731/BRONZ',
        price: 490
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'antrasit','gdlm'],
        src: '/gdlm/akp.png',
        system: 'plus',
        id: '001731/ANTRASIT',
        price: 490
    },
    {
        features: ['doormen', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'silver','gdlm'],
        src: '/gdlm/skp.png',
        system: 'plus',
        id: '001731/SILVER',
        price: 490
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'white','gdlm'],
        src: '/gdlm/kkp.png',
        system: 'plus',
        id: '001734/KREM',
        price: 506
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'bronz','gdlm'],
        src: '/gdlm/bkp.png',
        system: 'plus',
        id: '001734/BRONZ',
        price: 510
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'antrasit','gdlm'],
        src: '/gdlm/akp.png',
        system: 'plus',
        id: '001734/ANTRASIT',
        price: 510
    },
    {
        features: ['doormen', 'handsfree', 'alarm', 'memory', 'pick-melody', 'call-control', 'market', 'intercom', 'two-doors', 'security', 'extra-camera', 'silver','gdlm'],
        src: '/gdlm/skp.png',
        system: 'plus',
        id: '001734/SILVER',
        price: 510
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
        price: 360
    },


    /* Bus Plus Slim */
    {
        features: ['doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'slim'],
        src: '/slim/kpn.png',
        system: 'plus',
        id: '001669',
        price: 460
    },
    {
        features: ['doormen', 'easy-install', 'two-doors', 'security', 'market', 'intercom', 'extra-camera', 'slim'],
        src: '/slim/kp.png',
        system: 'plus',
        id: '001672',
        price: 480
    },

    /* Bus Plus Eko */
    {
        features: ['bw', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'eko'],
        src: '/eko/sb.png',
        system: 'plus',
        id: '001562',
        price: 260
    },
    {
        features: ['color', 'doormen', 'easy-install', 'two-doors', 'security', 'extra-camera', 'eko'],
        src: '/eko/c.png',
        system: 'plus',
        id: '001565',
        price: 330
    },
    {
        features: ['bw', 'doormen', 'easy-install', 'two-doors', 'security', 'market', 'intercom', 'extra-camera', 'eko'],
        src: '/eko/sb.png',
        system: 'plus',
        id: '001692',
        price: 280
    },
    {
        features: ['color', 'doormen', 'easy-install', 'two-doors', 'security', 'market', 'intercom', 'extra-camera', 'eko'],
        src: '/eko/c.png',
        system: 'plus',
        id: '001691',
        price: 350
    },

    // Panels
    /* Ft Panel */
    {
        features: ['panel', 'tough-panel'],
        src: '/toughp/gb.png',
        system: 'ft',
        id: '004962',
        price: function(apartment) {
            var price = 85
              , jumps = [12, 28, 44, 60, 76, 92]
            price += apartment * 9
            $.each(jumps, function(i, v){ if(apartment > v) price += 50 })
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
            var price = 68
              , jumps = [20, 46, 72, 52, 68, 84]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 12
            $.each(jumps, function(i, v){ if(apartment > v) price += 32 })
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
            var price = 48
              , jumps = [20, 46, 72, 52, 68, 84]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 12
            $.each(jumps, function(i, v){ if(apartment > v) price += 32 })
            return price            
        }
    },
    {
        features: ['panel', 'tough-panel'],
        src: '/toughp/gb.png',
        system: '4+n',
        id: '004813',
        price: function(apartment) {
            var price = 75
              , jumps = [12, 28, 44, 60, 76, 92]
            price += apartment * 9
            $.each(jumps, function(i, v){ if(apartment > v) price += 50 })
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
            var price = 48
              , jumps = [20, 46, 72, 52, 68, 84]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 12
            $.each(jumps, function(i, v){ if(apartment > v) price += 32 })
            return price            
        }
    },
    {
        features: ['panel', 'tough-panel'],
        src: '/toughp/gb.png',
        system: '8+n',
        id: '004813',
        price: function(apartment) {
            var price = 75
              , jumps = [12, 28, 44, 60, 76, 92]
            price += apartment * 9
            $.each(jumps, function(i, v){ if(apartment > v) price += 50 })
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
            var price = 368
              , jumps = [10, 20, 40, 52, 68, 84]
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 12
            $.each(jumps, function(i, v){ if(apartment > v) price += 60 })
            return price
        }
    },
    {
        features: ['panel', 'light-base', 'password', 'light-panel'],
        src: '/lightp/kd.png',
        system: 'plus+n',
        id: '008330',
        price: function(apartment) {
            var price = 600
              , jumps = [16, 32, 48, 64, 80, 96]
            if(apartment < 10) apartment = 10
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 12
            $.each(jumps, function(i, v){ if(apartment > v && v == 16) price += 72; else if(apartment > v) price += 60})
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
            var price = 368
              , jumps = [10, 20, 40, 52, 68, 84]
              , converter = (apartment / 16 - apartment / 16 % 1) * 70
            if(apartment % 2 != 0) apartment++
            price += apartment / 2 * 12
            $.each(jumps, function(i, v){ if(apartment > v) price += 60 })
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
            return 580
        }
    },
    {
        features: ['panel', 'light-base', 'tough-panel'],
        src: '/toughp/bd.png',
        system: 'plus',
        id: '008312',
        price: function(apartment) {
            return 690
        }
    },
    //FIXME: urun sablon ekle, isikli altlikli resim
    {
        features: ['panel', 'city', 'light-base'],
        src: '/city/s.png',
        system: 'plus',
        id: '003485',
        price: function(apartment) {
            return 950
        }
    },
    //FIXME: urunu sablon ekle
    {
        features: ['panel', 'crea', 'light-base'],
        src: '/crea/m.png',
        system: 'plus',
        id: '003491',
        price: function(apartment) {
            var price = 850
            return price
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
            return 900
        }
    },
    //FIXME: urun sablon ekle
    {
        features: ['panel', 'vision'],
        src: '/vision/m.png',
        system: 'plus',
        id: '003488',
        price: function(apartment) {
            return 1050
        }
    }



]

var systems = {
    'plus': function(state) {
	    var video = 60 + (state.apartment * 0.2 * 34)
          , cable = (state.apartment * 7 + 100 - (state.apartment * 7 % 100)) * 2.4 * 0.7 
          , apartment = state.apartment / state.block
          , power
        if(apartment <= 30)
            power = 120
        else if(apartment <= 60)
            power = 240
        else
            power = 320
        power *= state.block
        return video + power + cable
    },
    'plus+n': function(state) {
	    var video = 60 + (state.apartment * 0.2 * 34)
          , cable = (state.apartment * 7 + 100 - (state.apartment * 7 % 100)) * 2.4 * 2 
          , apartment = state.apartment / state.block
          , power
        if(apartment <= 30)
            power = 120
        else if(apartment <= 60)
            power = 240
        else
            power = 320
        power *= state.block
        return video + power + cable
    },
    '8+n': function(state) {
        var apartment = state.apartment / state.block
          , cable = state.apartment * 7 * 2 * 2.4
          , cu
        if($.inArray('two-doors', state.extra.monitors) != -1 || $.inArray('doormen', state.extra.monitors) != -1)
            cu = 270
        else if(apartment > 25)
            cu = 210
        else
            cu = 150
        cu*= state.block
        return cable + cu
    },
    '4+n': function(state) {
        var cable = state.apartment * 7 * 1.5  * 2
          , cu = 150
        cu *= state.block
    	return cu + cable
    },
    'et': function(state) {
        var cable = state.apartment * 7 * 1.5  * 2
          , cu = 160
        cu*= state.block
    	return cable + cu
    },
    'ft': function(state) {
        var apartment = state.apartment / state.block
          , cable = state.apartment * 7 * 1.5 * 2
          , cu
        if($.inArray('two-doors', state.extra.monitors) != -1)
            cu = 240
        else
            cu = 190
        cu*= state.block
        return cable + cu
    }, 
    'villa': function(state) {
    	return 70
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
        // ucuz urunde ucuz iscilik
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
        if(state.monitor == "001366") return 490 + 100
        if(state.monitor == "001368") return 350 + 100
        if(state.monitor == "001390") return 230 + 100
        if(state.monitor == "001389") return 330 + 100
        if(state.monitor == "001344") return 46 + 9
    },
    'security': function(state) { 
        return 370 + 100 + 240
    },
    // Bunlar icin yeni kod acildi (alarm, memory)
    'alarm': function(state) {
        return 90
    },
    'memory': function(state) {
        return 150
    },
    'extra-camera': function(state) { 
        var cable = state.block * 70 * 2.4 
          , module = state.panel.id == "003479" ? 0 : 90
        return cable + module + 400 + 60 + 100 + 100
    },
    'two-doors': function(state) { 
        if(state.monitor.system == "villa" && state.monitor == "001421") return 280 + 100
        else if(state.monitor.system == "villa" && state.monitor == "001366") return 280 
        else if(state.monitor.system == "villa" && state.monitor == "001368") return 280 
        else return state.panel.price(state.apartment)
    },
    'market': function(state) { 
        return 180  // uyarlama fiyat, cihaz + iscilik + kablo
    },
    'doormen': function(state) { 
        if(state.monitor.system == "plus" || state.monitor.system == "plus+n")
            return 180 
        else if(state.monitor.system == "et" || state.monitor.system == "ft")
            return 75 // uyarlama fiyat
        else 
            return 45
    },
    'light-base': function(state) { 
        var basePrice = 0
        if(state.panel.id == "008312" || state.panel.id == "003485" || state.panel.id == "003491") basePrice = 290
        else if(state.panel.id == "003480") basePrice = 270
        else if(state.panel.id == "008317") {
            var apartment = state.apartment / state.block
            if(apartment <= 11) basePrice = 270
            else if(apartment <= 20) basePrice = 310
            else basePrice = 350
        }
        basePrice *= state.block
        return basePrice
    }
}
