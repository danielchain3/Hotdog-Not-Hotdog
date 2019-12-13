from django import forms
from .models import Post

import binascii
import hashlib
from PIL import Image
from hashing import hashing_client as hc
from storage import flagging_client as sc

class PostForm(forms.ModelForm):

    hash = forms.CharField(required=False)
    class Meta:
        model = Post
        fields = ['name', 'image','hash']


    def clean_hash(self):
        image = self.cleaned_data.get('image', False)

        bytestream = (str)(Image.open(image).tobytes())
        hash = hc.run_hashing(bytestream)
        

        #use storage rpc call to check if the hash exist
        #if not exist the hash will return and the redis storage at rpc server will also be updated
        response = sc.runUserSubmit('david123', hash)
        existed = response['existed']

        if existed:
            raise forms.ValidationError('This image already exists or is flagged as inappropriate.')
        else:
            return hash

        # try:
        #     match = Post.objects.get(hash=hash)
        # except Post.DoesNotExist:
        #     return hash
        

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if not image:
            return image
        maxdim = 512
        if any(dim > maxdim for dim in image.image.size):
            # Resize too large image up to the max_size
            i = Image.open(image.file)
            fmt = i.format.lower()
            i.thumbnail((maxdim, maxdim))
            # We must reset io.BytesIO object, otherwise resized image bytes
            # will get appended to the original image  
            image.file = type(image.file)()
            i.save(image.file, fmt)
        return image




"""
import binascii
import hashlib

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['name', 'image']

    def Hashing (self, bytestreams):
        #store the orignal byte stream
        bs = bytestream.encode('utf-8')

        #hash result
        result = hashlib.sha256(bs).hexdigest()
        
        return result

    def clean(self):
        byte = bytearray(self.image.read())
        byte = binascii.hexlify(byte)
        
        top_secret = Hashing(byte)

        cleaned_data = super().clean()
        hash = self.cleaned_data.get('hash')
        try:
            match = Post.objects.get(hash=hash)
        except Post.DoesNotExist:
            # Unable to find a user, this is fine
            return top_secret
        raise forms.ValidationError('This image already exists.')
"""