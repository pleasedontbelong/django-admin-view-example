# -*- coding: utf-8 -*-
'''
Created on 2015-03-24 19:17
@summary: custom admin page for users
@author: pablo
'''
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf.urls import patterns, url
from functools import update_wrapper
from .admin_views import InactiveUsersView


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')

    def get_urls(self):
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        urls = super(UserAdmin, self).get_urls()

        my_urls = patterns(
            '',
            url(r'^inactive/$',
                wrap(self.changelist_view),
                name="inactive_users")
        )
        return my_urls + urls

    def get_changelist(self, request):
        if request.resolver_match.url_name == "inactive_users":
            return InactiveUsersView
        return super(UserAdmin, self).get_changelist(request)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
