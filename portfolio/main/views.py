from django.shortcuts import render , redirect
from .models import Project,Visitor

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'main/home.html' , {'projects' : projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Visitor.objects.create(name=name , email=email , message=message)
        return redirect('thanks')
    return render(request , 'main/contact.html')

def about(request):
    context = {
        'personal_details' : ['Name : Bharath V',
                              'Role : Software Engineer',
                              'Location : Chennai',
                              'Contact : bharathvelu14@gmail.com'],
        'summary': "Dynamic and detail-oriented Python developer with over a year of hands-on experience in designing, "
                   "developing, and maintaining robust applications. Proficient in Python frameworks like Flask "
                   "and libraries such as Pandas and NumPy.",
        'education': "Bachelor of Engineering in Mechanical Engineering from Vel Tech High Tech Dr. Rangarajan "
                     "Dr.Sakunthala Engineering College, Avadi.",
        'languages': ["English - Professional", "Tamil - Native"],
        'skills': ["Python", "Flask", "MySQL", "PostgreSQL", "RESTful APIs"],
        
    }
    return render(request, 'main/about.html', context)

def thanks(request):
    return render(request , 'main/thanks.html')