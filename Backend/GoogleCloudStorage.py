import mimetypes
import os
from django.core.files.storage import Storage
from django.core.files.base import File

# imports the google cloud client library
from google.cloud import storage

# chunk size must be a multiple of 256K
CHUNK_SIZE = (1024 * 256) * 1

class GoogleCloudFile(File):
    def __init__(self, name, mode, storage, bucket_name):
        self.name = name
        self.type = mimetypes.guess(name)[0]
        self._mode = mode
        self._storage = storage
        self._file = None
        # get the blob from the storage bucket
        self.blob = storage.get_bucket(bucket_name).get_blob(name)

        # if the file does not exist, create a new blob that stores the file
        if not self.blob and 'w' in mode:
            self.blob = Blob(
                    self.name, bucket_name,
                    chunk_size=CHUNK_SIZE)
        
        # return size of the file
        def __len__(self):
            return self.blob.size
        
        def _get_file(self):
            if self._file is not None:
                return self._file

        def _set_file(self, value):
            self._file = value

        def read(self):
            if 'r' in self._mode:
                return super(GoogleCloudFile, self).read()

        def write(self, content):
            if 'w' in self._mode:
                return super(GoogleCloudFile, self).write(content)
        
        def close(self):
            self._file.close()

class GoogleCloudStorage(Storage):
    def __init__(self, bucket_name):
        self.storage_client = storage.Client()
        self._bucket = None 
        self.bucket_name = bucket_name

    @property
    def bucket(self):
        if self._bucket == None:
            try:
                self._bucket = self.storage_client.get_bucket(self.bucket_name)
            except:
                self._bucket = self.storage_client.create_bucket(self.bucket_name)
        return self._bucket

    def _open(self, name, mode='rb'):
        """
        Reads the file from GCP Storage and checks if it exists
        Returns the file object if the file exists
        """
        file_object = GoogleCloudFile(name, mode, self.storage_client,\
                self.bucket_name)
        if file_object.blob == None:
            raise IOError("%s does not exist" % name)
        else:
            return file_object

    def _save(self, name, content):
        new_file = GoogleCloudFile(name, 'rw', self.storage_client, \
                self.bucket_name)
        new_file.blob.upload_from_file(content, rewind=True, size=content.size,\
                content_type=new_file.type)
        return name

    def delete(self, name):
        self.bucket.delete_blob(name)

    def exists(self, name):
        try:
            self.storage_client.get_bucket(self.bucket_name)
            return True
        except:
            return False


    def listdir(self, name):
        return list(self.bucket.list_blobs())

    def size(self, name):
        blob = self._get_blob(name)
        return self.blob.size

    def url(self, name):
        return self._get_blob(name).generate_signed_url()

