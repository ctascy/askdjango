from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator




#User #ManyToManyField를 직접 세팅



class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목', validators=[MinLengthValidator(3)])
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_posts')
    tags = models.ManyToManyField('Tag', blank=True)#매니투매니는 반드시 블랭크 트루 옵션 줄 것, Tag를 문자열로 하는게 좋다
    content = models.TextField()
    photo = models.ImageField()
    # lat = models.FloatField()
    # lng = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    image = models.ImageField(blank=True)#경로기 때문에 문자열로 이해

    def __str__(self):
        return self.message[:50]#50자 까지 미리 보여주기
