from django.core.files.storage import default_storage
from django.core.files import File
from media_bundler.bundler import PngSpriteBundle
from compressor.cache import get_hexdigest
from audio.settings import STATIC_ROOT
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
        super(PngSpriteCustom, self).make_bundle(versioner)
        file_path = self.get_bundle_path()
        file_name = os.path.basename(file_path)
        default_storage.save('resim/' + file_name, File(open(file_path,'rb')))

    def generate_css(self, packing):
        super(PngSpriteCustom, self).generate_css(packing)
        default_storage.save(os.path.relpath(self.css_file, STATIC_ROOT), 
                             File(open(self.css_file, 'rb')))
