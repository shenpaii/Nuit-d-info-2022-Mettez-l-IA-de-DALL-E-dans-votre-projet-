from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from .forms import ContactForm 
from django.contrib import messages
import smtplib, ssl
# Create your views here.

def home(request):
    context = {}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(request, form.cleaned_data)
        else:
           print (form.errors) #TODO to be replaced by validation error in form of warning message
    else:
        form = ContactForm()

    context = {'form': form}


    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))

def send_mail(request, data):
    port = 1025
    receiver_email = "entreprise.verdrei@gmail.com"
    password = "123verdrei"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP("localhost", port) as server:
        server.sendmail(data['email'], receiver_email, data['message'])

    messages.success(request, 'Message Sent!')
    return redirect('/')


def chatbot(request):

    
    pass