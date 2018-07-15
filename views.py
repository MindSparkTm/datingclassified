from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Userad, Replyad, Usads, Europeads,Submitfeedback
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.template.loader import get_template



import sendgrid
import os
from sendgrid.helpers.mail import *
import base64

import logging


class Index(CreateView):
    model = Userad

    def get(self, request):
        return render(request, 'plentyofcats/index.html', {"status": "initial"})

    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        age = int(request.POST['age'])
        country = request.POST['country']
        email = request.POST['email']
        uploadedfile = request.FILES['uploadedfile']
        fs = FileSystemStorage()

        filename = fs.save(uploadedfile.name, uploadedfile)
        uploaded_file_url = fs.url(filename)

        userad = Userad(title=title, email=email, description=description, category=category, age=age, country=country,
                        uploaded_file_url=uploaded_file_url)
        userad.save()

        return HttpResponseRedirect(reverse("Index"))


class Usaindex(CreateView):
    model = Usads

    def get(self, request):
        return render(request, 'plentyofcats/usa.html', {"status": "initial"})

    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        age = int(request.POST['age'])
        state = request.POST['state']
        email = request.POST['email']
        uploadedfile = request.FILES['uploadedfile']
        fs = FileSystemStorage()

        filename = fs.save(uploadedfile.name, uploadedfile)
        uploaded_file_url = fs.url(filename)

        userad = Usads(title=title, email=email, description=description, category=category, age=age, state=state,
                       uploaded_file_url=uploaded_file_url)
        userad.save()

        return HttpResponseRedirect(reverse("Usaindex"))


class Europeindex(CreateView):
    model = Europeads

    def get(self, request):
        return render(request, 'plentyofcats/europe.html', {"status": "initial"})

    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        age = int(request.POST['age'])
        country = request.POST['country']
        state = request.POST['state']
        email = request.POST['email']
        uploadedfile = request.FILES['uploadedfile']
        fs = FileSystemStorage()

        filename = fs.save(uploadedfile.name, uploadedfile)
        uploaded_file_url = fs.url(filename)

        userad = Europeads(title=title, email=email, description=description, category=category, age=age,
                           country=country, state=state, uploaded_file_url=uploaded_file_url)
        userad.save()

        return HttpResponseRedirect(reverse("Europeindex"))


class Menseekingwomen(CreateView):
    model = Userad

    def get(self, request):
        return render(request, 'plentyofcats/menseekingwomen.html')


class Menseekingwomenus(CreateView):
    model = Usads

    def get(self, request):
        return render(request, 'plentyofcats/menseekingwomenus.html')


class Menseekingmen(CreateView):
    model = Userad

    def get(self, request):
        return render(request, 'plentyofcats/menseekingmen.html')


class Menseekingmenus(CreateView):
    model = Usads

    def get(self, request):
        return render(request, 'plentyofcats/menseekingmenus.html')


class Womenseekingmen(CreateView):
    model = Userad

    def get(self, request):
        return render(request, 'plentyofcats/womenseekingmen.html')


class Womenseekingmenus(CreateView):
    model = Usads

    def get(self, request):
        return render(request, 'plentyofcats/womenseekingmenus.html')


class Womenseekingwomen(CreateView):
    model = Userad

    def get(self, request):
        print('yayayay')

        return render(request, 'plentyofcats/womenseekingwomen.html')



class Womenseekingwomenus(CreateView):
    model = Usads

    def get(self, request):
        print('yayayay')

        return render(request, 'plentyofcats/womenseekingwomenus.html')

class submitfeedback(CreateView):
    model = Submitfeedback

    def get(self, request):
        print('yayayay')

        return render(request, 'plentyofcats/submitfeedback.html')

    def post(self,request):
        print('entered')
        description = request.POST['description']
        email = request.POST['email']

        submitfeedback = Submitfeedback( description=description,email=email)
        submitfeedback.save()

        sendfeed(email, "smartsurajit2008@gmail.com", "Feedback", description);
        return HttpResponseRedirect(reverse("Usaindex"))



def getdatafromad(request):
    if request.method == 'GET':
        category = request.GET['category']
        country = request.GET['country']
        print('country', country)
        userad = Userad.objects.filter(category=category).filter(country=country).order_by('-postid').values()
        userad = list(userad)
        print('userad', userad)

        return JsonResponse(userad, safe=False)  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")


def getdatafromusad(request):
    if request.method == 'GET':
        category = request.GET['category']
        state = request.GET['state']
        print('country', state)
        userad = Usads.objects.filter(category=category).filter(state=state).order_by('-postid').values()
        userad = list(userad)
        print('userad', userad)

        return JsonResponse(userad, safe=False)  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")



class Postdetails(CreateView):
    model = Userad

    template_name = 'plentyofcats/displaypost.html'

    def get(self, request, *args, **kwargs):
        postid = str(self.kwargs['id'])
        postid = postid.replace('id/', '')
        print ('postid', postid)
        useradobject = Userad.objects.filter(postid=postid).values()
        print('useradobject', useradobject)

        return render(request, 'plentyofcats/displaypost.html', {'Useradobject': useradobject})


class Uspostdetails(CreateView):
    model = Usads

    template_name = 'plentyofcats/displaypostus.html'

    def get(self, request, *args, **kwargs):
        postid = str(self.kwargs['id'])
        postid = postid.replace('id/', '')
        print ('postid', postid)
        useradobject = Usads.objects.filter(postid=postid).values()
        print('usaobject', useradobject)

        return render(request, 'plentyofcats/displaypostus.html', {'Useradobject': useradobject})

    def post(self,request,*args, **kwargs):
        print('entered')
        description = request.POST['description']
        email = request.POST['email']
        postemail = request.POST['postemail']
        print('postemail', postemail)

        uploadedfile = request.FILES['uploadedfile']
        fs = FileSystemStorage()

        filename = fs.save(uploadedfile.name, uploadedfile)
        uploaded_file_url = fs.url(filename)

        replyad = Replyad(email=email, description=description, uploaded_file_url=uploaded_file_url)

        replyad.save()
        sendemail(email, postemail, "You have a new message", description, uploaded_file_url)
        return HttpResponseRedirect(reverse("Usaindex"))


def sendemail(sender,recipient,subject,content,url):
    sg = sendgrid.SendGridAPIClient(apikey="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")
    mail = Mail()
    from_email = Email(sender)
    to_email = Email(recipient)
    subject = "Your post has a new reply"
    per = Personalization()
    mail.from_email = from_email
    mail.subject = subject
    html_content = Content("text/html", "<html><head>"+content+"</head><body><a href=\"http://206.189.75.57"+url+"\">Click here to see Image</a></body></html>")
    plain_content = Content("text/plain", "and easy ")

    ### Add plain content first
    mail.add_content(plain_content)

    ### Add HTML content next
    mail.add_content(html_content)

    per.add_to(to_email)
    mail.add_personalization(per)
    response = sg.client.mail.send.post(request_body=mail.get())
    print('response',response)







def sendfeed(sender,recipient,subject,content):
    sg = sendgrid.SendGridAPIClient(apikey="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")
    mail = Mail()
    from_email = Email(sender)
    to_email = Email(recipient)
    subject = "Your post has a new reply"
    per = Personalization()
    mail.from_email = from_email
    mail.subject = subject
    html_content = Content("text/html", "<html><head>"+content+"</head><body></body></html>")
    plain_content = Content("text/plain", "and easy ")

    ### Add plain content first
    mail.add_content(plain_content)

    ### Add HTML content next
    mail.add_content(html_content)

    per.add_to(to_email)
    mail.add_personalization(per)
    response = sg.client.mail.send.post(request_body=mail.get())
    print('response',response)


