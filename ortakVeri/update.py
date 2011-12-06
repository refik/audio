from audio.ortakVeri.sprite import PngSpriteCustom
from audio.settings import MEDIA_BUNDLES

bundle = MEDIA_BUNDLES[0]
bundler = PngSpriteCustom(bundle['name'], bundle['path'], 
                          bundle['url'], bundle['files'], 
                          bundle['type'], bundle['css_file'])

bundler.make_bundle(0)

