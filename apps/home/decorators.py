from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/login/')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    # if allowed_roles is None:
    #     allowed_roles = []
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            j=0
            for i in allowed_roles:
                print('Allowed:',i)
                #if request.user.groups.filter(name = i).count():
                group = request.user.groups.all()[j].name
            
                if group in allowed_roles: 
                    print('Group:',group)     
                    return view_func(request, *args, **kwargs)
                j=j+1
            
            return HttpResponse("You are not authorized")
        return wrapper_func
    return decorator