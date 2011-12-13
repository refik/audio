from storages.backends.mosso import CloudFilesStorage, CloudStorageDirectory
from filebrowser.storage import StorageMixin
from audio.ortakVeri.cache import method_cache
import traceback
import datetime
import time

class AudioStorage(CloudFilesStorage, StorageMixin):
    #@method_cache(30)
    def _get_container_url(self, *args, **kwargs):
        return super(AudioStorage, self)._get_container_url(*args, **kwargs)
    def open(self, *args, **kwargs):
        file = super(AudioStorage, self).open(*args, **kwargs)
        # PIL PngImagePlugin cant open what cloudfiles Object returns
        # It needs a tell method and cloudfiles read method doesnt work
        # that way. This hack is a workaround for png files used by PIL
        if file.file.content_type == 'image/png':
            caller = traceback.extract_stack(limit=2)[0][2]
            if caller == '_dimensions' or caller == 'version_generator':
                file.file.save_to_filename('/tmp/pngfile.png')
                file = open('/tmp/pngfile.png', 'rb')
        return file
 
    #@method_cache(30)
    def _open(self, *args, **kwargs):
        return super(AudioStorage, self)._open(*args, **kwargs)

    #@method_cache(30)
    def exists(self, *args, **kwargs):
        return super(AudioStorage, self).exists(*args, **kwargs)

    #@method_cache(30)
    def listdir(self, *args, **kwargs):
        return super(AudioStorage, self).listdir(*args, **kwargs)

    #@method_cache(30)
    def full_listdir(self, *args, **kwargs):
        return super(AudioStorage, self).full_listdir(*args, **kwargs)

    #@method_cache(30)
    def size(self, *args, **kwargs):
        return super(AudioStorage, self).size(*args, **kwargs)

    #@method_cache(30)
    def url(self, name):
        return super(AudioStorage, self).url(name)

    def _get_cloud_obj(self, name):
        # Filebrowser checks folders with '/' at the end, doesnt work
        if name.endswith('/'):
            name = name[:-1]
        return super(AudioStorage, self)._get_cloud_obj(name)

    @method_cache(30)
    def isdir(self, name):
        if self.exists(name) and self.size(name) == 0:
            return True
        else:
            return False

    #@method_cache(30)
    def modified_time(self, path):
        date = self._get_cloud_obj(path).last_modified
        struct = time.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')
        return datetime.datetime(*struct[:6])

    #@method_cache(30)
    def isfile(self, name):
        if self.exists(name) and self.size(name) != 0:
            return True
        else:
            return False

    # Django appends _1 to filenames
    # don't need that
    def get_available_name(self, name):
        return name

    def makedirs(self, name):
        return self._save(name, CloudStorageDirectory(name))
