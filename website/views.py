from django.shortcuts import render, redirect
from django.contrib import messages
from website.models import Contact
from website.forms import ContactForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.

def index_view(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent successfully!")
            return redirect('website:index')
        else:
            messages.error(request, "Please correct the errors below.")
    
    context = {
        'Birthday': '8 April 1990',
        'Website': 'www.example.com',
        'Phone': '+98 913 123 1234',
        'City': 'Esfahan, Iran',
        'Age': 26,
        'Degree': 'B.Sc. in Mechanical Engineering',
        'Email': 'example@gmail.com',
        'Freelance': 'Available',
        'form': form,  # فرم کانتکت پاس داده شود
    }
    return render(request, 'website/index.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.name = "Anonymous"
            if not ticket.subject:
                ticket.subject = None
            ticket.save()

            messages.add_message(request, messages.SUCCESS, 'Your ticket submited successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket didnt submited!')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})

def coming_soon(request, exception=None):
    return render(request, "coming_soon.html", status=404)