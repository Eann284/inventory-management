from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, name, role, area, password=None, stock=0):
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(
            email = self.normalize_email(email),
            name=name,
            role=role,
            area=area,
            stock=stock
        )
        user.set_password(password)

        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email=email,
            name=name,
            role='ADMIN',
            area='Main',
            password=password,
        )


        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class UserManagerModel(AbstractBaseUser, PermissionsMixin):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email =  models.EmailField(unique=True)
    role = models.CharField(
        max_length=50,
        choices= [
            ('ADMIN','Admin'),
            ('SUPERVISOR','Supervisor'),
            ('CUSTODIAN','Custodian'),
            ('TECHNICIAN','Technician'),
        ]
    ) 

    area = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def __str__(self):
        return self.name

    @property
    def id(self):
        return self.uid


    class Meta:
        db_table = 'user_manager'