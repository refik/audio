from django.core.files.storage import default_storage
from django.core.files import File
from media_bundler.bundler import PngSpriteBundle
from audio.settings import STATIC_ROOT, STATIC_URL
from audio.ortakVeri.randomstr import random_string
import time
import os
import re

class PngSpriteCustom(PngSpriteBundle):
    def __init__(self, *args, **kwargs):
        super(PngSpriteCustom, self).__init__(*args, **kwargs)
        stamp = random_string(6)
        self.name += stamp

    def css_class_name(self, rule_name):
        versioned_name = self.name
        noversion_name = versioned_name[:-6]
        self.name = noversion_name
        css_name = super(PngSpriteCustom, self).css_class_name(rule_name)
        self.name = versioned_name
        return css_name

    def make_bundle(self, versioner):
        super(PngSpriteCustom, self).make_bundle(versioner)
        file_path = self.get_bundle_path()
        file_name = os.path.basename(file_path)
        default_storage.save('resim/' + file_name, File(open(file_path,'rb')))

    # Default version doesn't accept filenames with digits
    CSS_REGEXP = re.compile(r"[^a-zA-Z0-9\-_]")

    def generate_css(self, packing):
        super(PngSpriteCustom, self).generate_css(packing)
        default_storage.save(os.path.relpath(self.css_file, STATIC_ROOT), 
                             File(open(self.css_file, 'rb')))

def sprite_generator(name, pictures):
    files = [default_storage.open(pic.path).file for pic in pictures]
    for f in files:
        f.save_to_filename('/tmp/%s' % os.path.basename(f.name))
    bundler = PngSpriteCustom(
        name,
        '/tmp/',
        STATIC_URL + 'resim/',
        tuple([os.path.basename(f.name) for f in files]),
        'png-sprite',
        STATIC_ROOT + '/css/' + name + '.css')
    bundler.make_bundle(0)
