from audio.ozelSayfa.sprite import PngSpriteRefik
from audio.settings import MEDIA_BUNDLES

bundle = MEDIA_BUNDLES[0]
bundler = PngSpriteRefik(bundle['name'], bundle['path'], 
                          bundle['url'], bundle['files'], 
                          bundle['type'], bundle['css_file'])

bundler.make_bundle(0)

