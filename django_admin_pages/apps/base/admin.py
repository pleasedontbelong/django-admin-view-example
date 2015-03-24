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
        # this is just a copy paste from the admin code
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)
        # get the default urls
        urls = super(UserAdmin, self).get_urls()
        # define my own urls
        my_urls = patterns(
            '',
            url(r'^inactive/$',
                wrap(self.changelist_view),
                name="inactive_users")
        )
        # return the complete list of urls
        return my_urls + urls

    def get_changelist(self, request):
        """
        This method must return the view to be used for listing the model
        """
        # for inactive users use the InactiveUsersView
        if request.resolver_match.url_name == "inactive_users":
            return InactiveUsersView
        return super(UserAdmin, self).get_changelist(request)

# we must unregister the default user model
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
