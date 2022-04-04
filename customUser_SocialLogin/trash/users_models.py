from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.

# 필요없을거같다
class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    # user.save(using=self._db)
    user.save()
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    # user=self._create_user(email, password, True, True, **extra_fields)
    # user.save(using=self._db)
    # return user
    return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=20)

    username = models.CharField(max_length=20, unique=True, null=True)

    first_name = models.CharField(max_length=12, null=True)
    last_name = models.CharField(max_length=12, null=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # 가장 기본적으로 django에서는 username_field로 지정한 field를 통해 login한다.
    # 필드이름이 username이라고 해서 무조건 Login에 사용되는 field가 되는게 아니라
    # 여기서 지정해줘야한다
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    # 가입할때 띄울 field들. blank=False로 되어있거나 아예 없어야함(default가 false)
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def __str__(self) -> str:
        return self.email

# class SocialPlatform(models.Model):
#     platform = models.CharField(max_length=20, default=0)
#     class Meta:
#         db_table = "social_platform"