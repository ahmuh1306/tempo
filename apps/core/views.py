# Imports
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.team.models import Invitation
from apps.userprofile.models import UserProfile
from .forms import ContactForm

# Views
def frontpage(request):
    return render(request, 'core/frontpage.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')

def plans(request):
    return render(request, 'core/plans.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            userprofile = UserProfile.objects.create(user=user)

            login(request, user)

            invitations = Invitation.objects.filter(email=user.email, status=Invitation.INVITED)
            if invitations:
                return redirect('accept_invitation')
            else:
                return redirect('dashboard')

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['info@ahmadmuhammad.co.za'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_success')
    
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'core/contact_success.html')