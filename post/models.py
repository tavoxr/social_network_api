from django.contrib import auth
from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE, related_name='posts')
    text = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}\'s post ({self.create_date.isoformat()})'


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE, related_name='+')
    comment = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment from {self.user} on {self.post}'


class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return f'Like from {self.user} on {self.post}'
