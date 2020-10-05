from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    @property
    def num_likes(self):
        return self.liked.object.all().count()


like_choices = (('like', 'like'), ('unlike', 'unlike'))


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=like_choices, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)
