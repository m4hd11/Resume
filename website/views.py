from django.shortcuts import render

# Create your views here.

def index_view(request):
    context = {
        'Birthday': '8 April 1990',
        'Website': 'www.example.com',
        'Phone': '+98 913 123 1234',
        'City': 'Esfahan, Iran',
        'Age': 26,
        'Degree': 'B.Sc. in Mechanical Engineering',
        'Email': 'example@gmail.com',
        'Freelance': 'Available',
    }
    return render(request, 'website/index.html', context)