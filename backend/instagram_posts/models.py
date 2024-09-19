from django.db import models

# Create your models here.

class InstagramAccount(models.Model):
    username = models.CharField(max_length=255, unique=True)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='instagram/user_photos')  
    followers = models.IntegerField()
    followees = models.IntegerField()


    def __str__(self):
        return self.username


class InstagramPost(models.Model):
    account = models.ForeignKey(InstagramAccount, on_delete=models.CASCADE, related_name='posts')
    #url = models.URLField()
    date = models.DateTimeField()
    caption = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='instagram/user_post')

    def __str__(self):
        return f'Post by {self.account.username} on {self.date}'
