from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth, messages
#only login user could see profile page
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm #helpForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Vaksinasi
from .chartjs import processData

# def register(request):
#     currentUserDet = user_auth.models.User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             #including encryption for the password
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users_act/register.html', {'form': form}) 

# def yearlyData():
#     vaksin2018 = Vaksinasi.objects.filter(year = 2018)
#     vaksin2019 = Vaksinasi.objects.filter(year = 2019)
#     vaksin2020 = Vaksinasi.objects.filter(year = 2020)
#     print("vaksin 2018")
#     print(vaksin2018)
#     print("vaksin 2019")
#     print(vaksin2019)
#     print("vaksin 2020")
#     print(vaksin2020)
    # dataYear =  processData.firstChart(vaksin2018, vaksin2019, vaksin2020)

@login_required(login_url="/login/")
def index(request):
    if request.method == "GET":    
        vaksin = Vaksinasi.objects.all()
        dict = processData.firstChart(vaksin)
        print("Here is dict:")
        print(dict)
        # yearlyData()
        context = {
            'segment': 'index',
            'vaksin':dict
            }
    #context:
    #{'segment': 'index', 'vaksin': <QuerySet [<Vaksinasi: Baling-2018-157-100>, 
    # <Vaksinasi: Sik-2018-109-98>, <Vaksinasi: Alor Setar-2018-318-210>, 
    # <Vaksinasi: Langkawi-2020-3926-2136>, '...(remaining elements truncated)...']>}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
