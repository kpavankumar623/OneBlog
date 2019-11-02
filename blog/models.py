from django.db import models
from django import forms
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class  Blog(models.Model):
    blog_title = models.CharField(max_length = 200)
    blog_type = models.CharField(max_length = 100)
    blog_content = RichTextUploadingField()
    published_date = models.DateField(auto_now=True)
    feautured_image = models.ImageField(upload_to = "feautured_images/", default = 'blog_default.jpg')
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=0)

class UploadForm( forms.ModelForm):
    feautured_image = forms.ImageField(required=False)
    class Meta:
        model = Blog
        fields = ('blog_title','blog_type','feautured_image','blog_content')
