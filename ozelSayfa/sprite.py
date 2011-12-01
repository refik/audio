from media_bundler.bundler import PngSpriteBundle
from compressor.cache import get_hexdigest
import time

class PngSpriteRefik(PngSpriteBundle):
    def __init__(self, *args, **kwargs):
        super(PngSpriteRefik, self).__init__(*args, **kwargs)
        stamp = get_hexdigest(time.time(),12)
        self.name += stamp

    def css_class_name(self, rule_name):
        versioned_name = self.name
        noversion_name = versioned_name[:-12]
        self.name = noversion_name
        css_name = super(PngSpriteRefik, self).css_class_name(rule_name)
        self.name = versioned_name
        return css_name

