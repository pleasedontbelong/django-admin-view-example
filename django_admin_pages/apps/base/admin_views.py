from django.contrib.admin.views.main import ChangeList


class InactiveUsersView(ChangeList):
    """
    This view displays the list of inactive users
    """
    def __init__(self, *args, **kwargs):
        super(InactiveUsersView, self).__init__(*args, **kwargs)
        self.list_display = ('username', 'email', 'date_joined', 'last_login')

    def get_queryset(self, request):
        qs = super(InactiveUsersView, self).get_queryset(request)
        # filter inactive and admin users
        return qs.filter(is_staff=False, is_active=False, is_superuser=False)
