from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class  Blog(models.Model):
    blog_title = models.CharField(max_length = 200)
    blog_type = models.CharField(max_length = 100)
    blog_content = RichTextUploadingField()
    published_date = models.DateField(auto_now=True)
    feautured_image = models.ImageField(upload_to='feautured_images/', default = 'media/blog-default.jpg')
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=0)

class UploadForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('feautured_image',)
