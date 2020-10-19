from django.contrib import auth
from django.db import models
from django.utils import timezone

#buat model database untuk user (nama kolom2 untuk user termasuk dalam libs django, makanya simple codenya)
#ga perlu isi admin.py krn model yg dibuat termasuk dalam libs django
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username) #username dari libs django auth/models.user
