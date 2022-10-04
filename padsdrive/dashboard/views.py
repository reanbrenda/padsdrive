from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse



def dashboard(request):
    context = {'segment': 'dashboard'}

    html_template = loader.get_template('dashboard.html')
    return HttpResponse(html_template.render(context, request))


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
    
def createPadDriveGroup(request):
    if request.method == "POST":
        name = request.POST['name']
        county = request.POST['county']
        email=request.POST['email']
        donation_amount=request.POST['donation_amount']
        contact_person=request.POST['contact_person']
        phone_number=request.POST['phone_number']
        no_pads=request.POST['no_pads']
        
        paddrivegroup_obj =PadDriveGroup.objects.create(name=name,county=county,email=email,donation_amount=donation_amount,contact_person=contact_person,phone_number=phone_number,no_pads=no_pads)
        messages.success(request, "pad drive group created successfully")

    return render(request, 'createpaddrive.html')


def Paddrivegroup_list(request):
    paddrivegroup_data = PadDriveGroup.objects.filter()
    d = {'paddrivegoup':paddrivegroup_data}
    return render(request, 'tables.html',d)
