from django.http import HttpResponseRedirect
from django.urls import reverse


def role_required(roles):
    def method_wrapper(function):
        def wrap(request, *args, **kwargs):

            if request.user.profile.role not in roles:
                return HttpResponseRedirect(reverse("dashboard:index"))

            return function(request, *args, **kwargs)

        return wrap
    return method_wrapper