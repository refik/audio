from django.core.files.storage import default_storage
from media_bundler.bundler import PngSpriteBundle
from compressor.cache import get_hexdigest
import time
import os

class PngSpriteCustom(PngSpriteBundle):
    def __init__(self, *args, **kwargs):
        super(PngSpriteCustom, self).__init__(*args, **kwargs)
        stamp = get_hexdigest(time.time(),12)
        self.name += stamp

    def css_class_name(self, rule_name):
        versioned_name = self.name
        noversion_name = versioned_name[:-12]
        self.name = noversion_name
        css_name = super(PngSpriteCustom, self).css_class_name(rule_name)
        self.name = versioned_name
        return css_name

    def make_bundle(self, versioner):
        super(PngSpriteCustom, self).__init__(versioner)
        file_path = self.get_bundle_path()
        file_name = os.path.basename(file_path)
        default_storage.save('resim/sprite/' + file_name, open(file_path,'rb'))
