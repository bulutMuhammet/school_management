from django.shortcuts import reverse,HttpResponseRedirect

def anonymous_required(func):
    def wrap(request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("dashboard:index"))
        return func(request,*args,**kwargs)
    return wrap