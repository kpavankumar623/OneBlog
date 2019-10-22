from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.
class  Blog(models.Model):
    blog_title = models.CharField(max_length = 200)
    blog_type = models.CharField(max_length = 100)
    blog_content = models.TextField()
    published_date = models.DateField('date publised')
    feautured_image = models.ImageField(upload_to='feautured_images/')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=0)

class UploadForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('feautured_image',)
