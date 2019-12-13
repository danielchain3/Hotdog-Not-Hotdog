from django import forms
from .models import Post

import binascii
import hashlib
from PIL import Image
from hashing import hashing_client as hc

class PostForm(forms.ModelForm):

    hash = forms.CharField(required=False)
    class Meta:
        model = Post
        fields = ['title', 'cover','hash']


    def clean_hash(self):
        cover = self.cleaned_data.get('cover', False)

        bytestream = (str)(Image.open(cover).tobytes())
s
        hash = hc.run_hashing(bytestream)
        try:
            match = Post.objects.get(hash=hash)
        except Post.DoesNotExist:
            return hash
        raise forms.ValidationError('This image already exists or is flagged as inappropriate.')

    def clean_cover(self):
        cover = self.cleaned_data.get('cover')

        if not cover:
            return cover
        maxdim = 512
        if any(dim > maxdim for dim in cover.image.size):
            # Resize too large image up to the max_size
            i = Image.open(cover.file)
            fmt = i.format.lower()
            i.thumbnail((maxdim, maxdim))
            # We must reset io.BytesIO object, otherwise resized image bytes
            # will get appended to the original image  
            cover.file = type(cover.file)()
            i.save(cover.file, fmt)
        return cover




"""
import binascii
import hashlib

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'cover']

    def Hashing (self, bytestreams):
        #store the orignal byte stream
        bs = bytestream.encode('utf-8')

        #hash result
        result = hashlib.sha256(bs).hexdigest()
        
        return result

    def clean(self):
        byte = bytearray(self.cover.read())
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