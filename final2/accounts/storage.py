from django.core.files.storage import FileSystemStorage
from django.db.models.fields.files import ImageField
from django.conf import settings
from django.core.files.move import file_move_safe

from django.core.files import File, locks

import os
import sys

from django.core.files.images import ImageFile

import binascii

import ../../grpc/Hashing service/hashing_client as hc




class MyStorage(FileSystemStorage):
    #custom storage class needs to do 
    #1. make RPC call to RPC servers to retrieve hashed image, whenever receive content from user, 
    # make RPC call to external servers as client. 
    #2. delete: when user wants to delete their images, make RPC call to do so
    #3. (done) exists???? tell if the file already in our database 
    #4. 
    #

    # def _open(self, name, mode='rb'):
    #     # print('open!!')
    #     return super()._open(name, mode='rb')

    def save(self, name, content, max_length=None):
        # Get the proper name for the file, as it will actually be saved.
        if name is None:
            name = content.name
        byte = bytearray(content.read())
        byte = binascii.hexlify(byte)

        hashOfPhoto = hc.run_hashing(byte)
        print(name)
        print(hashOfPhoto) 

        # print(binascii.hexlify(byte))

        return self._save(hashOfPhoto, content)


    def _save(self, name, content):
        # print(f'about to save {name} to {self.path(name)}')

        if self.exists(name):
            self.delete(name)
            # print("deleted!!!")

        full_path = self.path(name)

        # Create any intermediate directories that do not exist.
        directory = os.path.dirname(full_path)
        if not os.path.exists(directory):
            try:
                if self.directory_permissions_mode is not None:
                    # os.makedirs applies the global umask, so we reset it,
                    # for consistency with file_permissions_mode behavior.
                    old_umask = os.umask(0)
                    try:
                        os.makedirs(directory, self.directory_permissions_mode)
                    finally:
                        os.umask(old_umask)
                else:
                    os.makedirs(directory)
            except FileExistsError:
                # There's a race between os.path.exists() and os.makedirs().
                # If os.makedirs() fails with FileExistsError, the directory
                # was created concurrently.
                pass
        if not os.path.isdir(directory):
            raise IOError("%s exists and is not a directory." % directory)


        while True:
            try:
                # This file has a file path that we can move.
                if hasattr(content, 'temporary_file_path'):
                    file_move_safe(content.temporary_file_path(), full_path)

                # This is a normal uploadedfile that we can stream.
                else:
                    # The current umask value is masked out by os.open!
                    fd = os.open(full_path, self.OS_OPEN_FLAGS, 0o666)
                    _file = None
                    try:
                        locks.lock(fd, locks.LOCK_EX)
                        for chunk in content.chunks():
                            if _file is None:
                                mode = 'wb' if isinstance(chunk, bytes) else 'wt'
                                _file = os.fdopen(fd, mode)
                            _file.write(chunk)
                    finally:
                        locks.unlock(fd)
                        if _file is not None:
                            _file.close()
                        else:
                            os.close(fd)
            except FileExistsError:
                # A new name is needed if the file exists.
                pass
                name = self.get_available_name(name)
                full_path = self.path(name)
            else:
                # OK, the file save worked. Break out of the loop.
                break

        if self.file_permissions_mode is not None:
            os.chmod(full_path, self.file_permissions_mode)

        # Store filenames with forward slashes, even on Windows.
        return name.replace('\\', '/')


    def exists(self, name):
        # print(f"check if {name} at {self.path(name)} exist")
        # print(os.path.exists(self.path(name)))
        return os.path.exists(self.path(name))

        
