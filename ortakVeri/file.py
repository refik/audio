from django.core.files.storage import default_storage
import os

def save_to_local(cloud_path, local_path):
    local_file = open(local_path, 'wb')
    cloud_file = default_storage.open(cloud_path).file
    for chunk in cloud_file.stream():
        local_file.write(chunk)
    local_file.close()
    return True
            
