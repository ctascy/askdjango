from django.db import models
from django.conf import settings
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

# def follow(self, to_user):
#     self.following_set.add(to_user)
#
# setattr(User, 'follow', follow)
def follow(self, to_user):
    # follow = Follow.objects.create(from_user=self, to_user=to_user)
    kwargs = {'from_user':self, 'to_user':to_user}
    if not Follow.objects.filter(**kwargs).exists(): #**kwargs 는 언팩 기능
        Follow.objects.create(**kwargs)

    # try:
    #    Follow.objects.create(from_user=self, to_user=to_user)
    # except IntegrityError:
    #    pass
setattr(User, 'follow', follow)


# def unfollow(self, to_user):
#     self.following_set.remove(to_user)
#
# setattr(User, 'unfollow', unfollow)
def unfollow(self, to_user):
    Follow.objects.filter(from_user=self, to_user=to_user).delete()

setattr(User, 'unfollow', unfollow)



class Follow(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following_set')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follower_set')
    is_blocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) #최초 저장시에만
    updated_at = models.DateTimeField(auto_now=True) #업데이트 될 때 마다
    class Meta:
        unique_together=[
        ['from_user','to_user']
        ]

class PhoneField():
    pass

class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 11)
        super(PhoneField, self).__init__(*args, **kwargs)
        validator = RegexValidator(r'^01[016789]\d{7,8}$',
            message='휴대폰 번호를 입력해주세요.')
        self.validators.append(validator)

        

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone = PhoneField()
    # phone = models.CharField(max_length=20)
    birth_year = models.PositiveIntegerField()
