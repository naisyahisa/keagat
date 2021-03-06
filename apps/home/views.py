from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth, messages
#only login user could see profile page
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView, DetailView
from django.urls import reverse
from matplotlib.style import context

from apps.authentication.models import Helpdesk
from .models import Vaksinasi
from .chartjs import processData
from .decorators import allowed_users, unauthenticated_user

@login_required(login_url="/login/")
def index(request):
    if request.method == "GET":    
        vaksin = Vaksinasi.objects.all()
        
        dist = processData.firstChart(vaksin)

        daerah = processData.get_label(vaksin)
       
        v_able_sum, v_done_sum, whole_perc, year = processData.sum_year(vaksin)

        # print(pred_able, pred_done)
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

        sorted_list20 = processData.sorted_data(daerah, v_perc20)
        
        #sorted percentage follow daerah 2020 (daerah 2020, value ascending)
        sorted_perc15 = processData.sorted_not20(daerah, v_perc15, sorted_list20)
        sorted_perc16 = processData.sorted_not20(daerah, v_perc16, sorted_list20)
        sorted_perc17 = processData.sorted_not20(daerah, v_perc17, sorted_list20)   
        sorted_perc18 = processData.sorted_not20(daerah, v_perc18, sorted_list20)
        sorted_perc19 = processData.sorted_not20(daerah, v_perc19, sorted_list20)

        sorted_daerah = sorted_list20[0]
        # print('sorted daerah', sorted_daerah)
        v_able_daerah = processData.daerah_vac_able(sorted_daerah,vaksin)
        
        diff_whole_perc_current = round(whole_perc[-1] - whole_perc[-2], 2)
        diff_vac_able_current = round(v_able_sum[-1] - v_able_sum[-2], 2)
        diff_vac_done_current = round(v_done_sum[-1] - v_done_sum[-2], 2)

        sum_able = processData.sum(v_able_sum)
        sum_done = processData.sum(v_done_sum)
        notyet_v = sum_able-sum_done
       
        
        context = {
            'segment': 'index',
            'dist':dist[0],
            'perc':dist[1],
            'year':dist[2],
            'vaksin':vaksin,
            #sorted value 
            'sorted_daerah': sorted_list20[0],
            'sorted_perc15': sorted_perc15,
            'sorted_perc16': sorted_perc16,
            'sorted_perc17': sorted_perc17,
            'sorted_perc18': sorted_perc18,
            'sorted_perc19': sorted_perc19,
            'sorted_perc20': sorted_list20[1],
            'v_able_sum': v_able_sum, 
            'v_done_sum': v_done_sum,
            'jangkaan': v_done_sum[-1],
            'sum_able': sum_able,
            'sum_done': sum_done,
            'notyet_v': notyet_v,
            'asc_year': year,
            'whole_perc' : whole_perc,
            'latest_v_able':v_able_sum[-1],
            'latest_v_done':v_done_sum[-1],
            'latest_whole_perc' : whole_perc[-1],
            'diff_whole_perc': diff_whole_perc_current,
            'diff_v_able': diff_vac_able_current,
            'diff_v_done': diff_vac_done_current,
            'highest_daerah': sorted_list20[0][-1],
            'fastest': sorted_list20[1][-1],
            'lowest_daerah': sorted_list20[0][0],
            'slowest': sorted_list20[1][0],
            'v_able_daerah': v_able_daerah
            }

   
    # html_template = loader.get_template('home/index.html')
    # return HttpResponse(html_template.render(context, request))
    return render(request, 'home/index.html', context)


@allowed_users(allowed_roles=['helpdesk_staff','admin_staff'])
def helpdesk_inbox(request):
    help = Helpdesk.objects.all()
    baru, selesai, lain = processData.helpChart(help)
    context = {
        'baru': baru,
        'selesai': selesai,
        'lain': lain
    }
    return render(request, 'home/billing.html',context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        print('template', load_template)

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        if load_template == 'register.html':
            html_template = loader.get_template('accounts/' + load_template)
            print('context', context)
            return HttpResponse(html_template.render(context, request))
        

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

# def post(request):

#     post = Post.objects.all()
#     context = {
#         'posts': post.title,
#     }
#     print('post request',context)
#     return render(request,'post.html', context)

# class PostView(ListView):
#     model = Post
#     template_name = 'post.html'
#     context_object_name = 'posts'
#     print('context object name', context_object_name)