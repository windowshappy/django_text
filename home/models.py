from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=30, unique=True)
    user_password = models.CharField(max_length=30)

    def __str__(self):
        return 'User:  %s' % self.user_name
    # class Meta:
    #     db_table = 't_user'
