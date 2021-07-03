from django.db import models

# Create your models here.

class Post(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    passport=models.CharField(max_length=18)
    tel=models.IntegerField()
    country=models.CharField(max_length=255, default='-')
    comeform=models.TextField()
    district=models.CharField(max_length=255, default='-')
    canton=models.CharField(max_length=255,default='-')
    terminus=models.TextField()
    ldistrict=models.CharField(max_length=255, default='-')
    lcanton=models.CharField(max_length=255, default='-')
    image=models.ImageField(upload_to="pageimage",blank=True)
    class Meta:
        db_table="page_post"
