from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from datetime import date
import uuid
time = date.today().strftime("%m/%d/%y")

# Create your models here.
class Post(models.Model):
    content   = models.TextField()
    title     = models.CharField(max_length=10)
    image     = models.ImageField(upload_to='images')
    name      = models.TextField()
    time      = models.DateField()

class Comment(models.Model):
    comment   = models.TextField()
    time      = models.DateField()
    name      = models.TextField()
    pid       = models.IntegerField()

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password, about, image, rank, location, verified=False, last_login=time, is_active=True, is_creator=False, is_staff=False, is_prostaff=False, is_superuser=False):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.username    = username
        user.password    = password
        user.location    = location
        user.verified    = verified
        user.first_name  = first_name
        user.last_name   = last_name
        user.rank        = rank
        user.email       = email
        user.image       = image
        user.about       = about
        user.active      = is_active
        user.prostaff    = is_prostaff
        user.staff       = is_staff
        user.login       = last_login
        user.superuser   = is_superuser
        user.save(using=self._db)
        return user
        
    def create_superuser(self, image,  email, username, first_name, last_name, password):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.email = email
        user.first_name  = first_name
        user.last_name   = last_name
        user.username    = username
        user.password    = password
        user.image       = image
        user.prostaff    = True
        user.is_creator    = True
        user.is_superuser    = True
        user.staff       = True
        user.active      = True
        user.save(using=self._db)
        return user
        
    def create_pro(self, email, username, image, password, verified, rank, location, about):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.username       = username
        user.password       = password
        user.location       = location
        user.verified       = verified
        user.rank           = rank
        user.email          = email
        user.image          = image
        user.about          = about
        user.prostaff       = True
        user.save(using=self._db)
        return user
        
    def create_staff(self, email, username, password, verified, image, location, about):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.username       = username
        user.password       = password
        user.location       = location
        user.verified         = verified
        user.email          = email
        user.image          = image
        user.staff          = True
        user.is_creator    = True
        user.prostaff       = True
        user.active         = True
        user.about          = about
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    first_name      = models.CharField(max_length=30)
    last_name      = models.CharField(max_length=30)
    username      = models.CharField(max_length=30)
    email         = models.EmailField(max_length=255, unique=True)
    rank         = models.CharField(max_length=3, blank=True, null=True)
    verified        = models.CharField(max_length=30, blank=True, null=True)
    creator    = models.BooleanField(default=False, blank=True, null=True)
    supersuer    = models.BooleanField(default=False, blank=True, null=True)
    password      = models.CharField(blank=False, max_length=30)
    about         = models.CharField(max_length=100, blank=True, null=True)
    image         = models.ImageField(upload_to='profile', null=True, blank=True)
    location      = models.CharField(max_length=30, blank=True, null=True)
    created_on    = models.DateTimeField(auto_now_add=True)
    updated_on    = models.DateTimeField(auto_now=True)
    last_login    = models.DateTimeField(blank=True, null=True)
    staff         = models.BooleanField(default=False, blank=True, null=True)
    prostaff         = models.BooleanField(default=False, blank=True, null=True)
    active        = models.BooleanField(default=True, blank=True, null=True)
    api_token     = models.UUIDField(default=uuid.uuid4, editable=False)
    token_created_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.verified + " " + self.rank

    def get_short_name(self):
        return self.location

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
         return True

    @property
    def is_staff(self):
         return self.staff

    @property
    def is_prostaff(self):
         return self.prostaff

    @property
    def is_superuserf(self):
         return self.superuser

    @property
    def is_creator(self):
         return self.creator

    @property
    def is_active(self):
         return self.active

    def api_token_reset(self):
        self.api_token = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ('created_on',)
        db_table = 'users'

    def __unicode__(self):
        return self.get_full_name()
