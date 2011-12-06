from storages.backends.mosso import CloudFilesStorage, CloudStorageDirectory
from filebrowser.storage import StorageMixin
from audio.ortakVeri.cache import method_cache
import datetime
import time

class AudioStorage(CloudFilesStorage, StorageMixin):
    @method_cache(30)
    def _get_container_url(self, *args, **kwargs):
        return super(AudioStorage, self)._get_container_url(*args, **kwargs)

    @method_cache(30)
    def _open(self, *args, **kwargs):
        return super(AudioStorage, self)._open(*args, **kwargs)

    @method_cache(30)
    def exists(self, *args, **kwargs):
        return super(AudioStorage, self).exists(*args, **kwargs)

    @method_cache(30)
    def listdir(self, *args, **kwargs):
        return super(AudioStorage, self).listdir(*args, **kwargs)

    @method_cache(30)
    def full_listdir(self, *args, **kwargs):
        return super(AudioStorage, self).full_listdir(*args, **kwargs)

    @method_cache(30)
    def size(self, *args, **kwargs):
        return super(AudioStorage, self).size(*args, **kwargs)

    @method_cache(30)
    def url(self, *args, **kwargs):
        return super(AudioStorage, self)._get_container_url()

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

    @method_cache(30)
    def modified_time(self, path):
        date = self._get_cloud_obj(path).last_modified
        struct = time.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')
        return datetime.datetime(*struct[:6])

    @method_cache(30)
    def isfile(self, name):
        if self.exists(name) and self.size(name) != 0:
            return True
        else:
            return False

    def makedirs(self, name):
        return self._save(name, CloudStorageDirectory(name))
