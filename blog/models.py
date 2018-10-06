from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    userid = models.IntegerField(default=0)
    isLoggedin=models.BooleanField(default=False)
    dat_pub = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title