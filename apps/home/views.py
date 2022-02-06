from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth, messages
#only login user could see profile page

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
#     return render(request, 'accounts/register.html', {'form': form}) 

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
        # print(vaksin)
        dist = processData.firstChart(vaksin)
        # print("Here is dist:")
        # print(dist)

        daerah = processData.get_label(vaksin)
        # print("daerah:",daerah)

        distinct_year = Vaksinasi.objects.all().values_list('year', flat=True).distinct()
        print(distinct_year)
       
        v_able_sum, v_done_sum, whole_perc, year = processData.sum_year(vaksin)
        
        v_doneAble15 = processData.get_vac_done_able(vaksin,2015)
        v_doneAble16 = processData.get_vac_done_able(vaksin,2016)
        v_doneAble17 = processData.get_vac_done_able(vaksin,2017)
        v_doneAble18 = processData.get_vac_done_able(vaksin,2018)
        v_doneAble19 = processData.get_vac_done_able(vaksin,2019)
        v_doneAble20 = processData.get_vac_done_able(vaksin,2020)

        v_perc15 = processData.get_vac_perc(vaksin,2015)
        v_perc16 = processData.get_vac_perc(vaksin,2016)
        v_perc17 = processData.get_vac_perc(vaksin,2017)
        v_perc18 = processData.get_vac_perc(vaksin,2018)
        v_perc19 = processData.get_vac_perc(vaksin,2019)
        v_perc20 = processData.get_vac_perc(vaksin,2020)

        # sorted_list15 = processData.sorted_data(daerah, v_perc15)
        # sorted_list16 = processData.sorted_data(daerah, v_perc16)
        # sorted_list17 = processData.sorted_data(daerah, v_perc17)   
        # sorted_list18 = processData.sorted_data(daerah, v_perc18)
        # sorted_list19 = processData.sorted_data(daerah, v_perc19)
        sorted_list20 = processData.sorted_data(daerah, v_perc20)

        #sorted percentage follow daerah 2020 (daerah 2020, value ascending)
        sorted_perc15 = processData.sorted_not20(daerah, v_perc15, sorted_list20)
        sorted_perc16 = processData.sorted_not20(daerah, v_perc16, sorted_list20)
        sorted_perc17 = processData.sorted_not20(daerah, v_perc17, sorted_list20)   
        sorted_perc18 = processData.sorted_not20(daerah, v_perc18, sorted_list20)
        sorted_perc19 = processData.sorted_not20(daerah, v_perc19, sorted_list20)

        # print(sorted_perc18)
        # print(sorted_perc19)
        # print(sorted_list20[0][1])
       
        context = {
            'segment': 'index',
            'dist':dist[0],
            'perc':dist[1],
            'year':dist[2],
            'vaksin':vaksin,
            # 'daerah':daerah,
            # 'v_done19':v_doneable19,
            # 'v_done18':v_doneable18,
            # 'v_done20':v_doneable20,
            #sorted value 
            'sorted_daerah': sorted_list20[0],
            'sorted_perc15': sorted_perc15,
            'sorted_perc16': sorted_perc16,
            'sorted_perc17': sorted_perc17,
            'sorted_perc18': sorted_perc18,
            'sorted_perc19': sorted_perc19,
            'sorted_perc20': sorted_list20[1],
            'v_able_sum' : v_able_sum, 
            'v_done_sum' : v_done_sum,
            'whole_perc' : whole_perc,
            }

    #context:
    #{'segment': 'index', 'vaksin': <QuerySet [<Vaksinasi: Baling-2018-157-100>, 
    # <Vaksinasi: Sik-2018-109-98>, <Vaksinasi: Alor Setar-2018-318-210>, 
    # <Vaksinasi: Langkawi-2020-3926-2136>, '...(remaining elements truncated)...']>}
    html_template = loader.get_template('home/index.html')
    # return HttpResponse(html_template.render(context, request))
    return render(request, 'home/index.html', context)

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
