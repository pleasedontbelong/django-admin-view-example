from django.contrib.admin.views.main import ChangeList


class InactiveUsersView(ChangeList):
    def __init__(self, *args, **kwargs):
        super(InactiveUsersView, self).__init__(*args, **kwargs)
        self.list_display = ('username', 'email', 'date_joined', 'last_login')

    def get_queryset(self, request):
        qs = super(InactiveUsersView, self).get_queryset(request)
        return qs.exclude(is_staff=False).exclude(is_active=False).exclude(is_superuser=False)
