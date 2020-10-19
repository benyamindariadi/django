from django.contrib import admin

from . import models


class GroupMemberInline(admin.TabularInline): #nyatuin group member(user) dengan admin. (groupmember=admin)
    model = models.GroupMember



admin.site.register(models.Group)
