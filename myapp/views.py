from django.shortcuts import render
from .models import contact1
# Create your views here.
def home(request):
    contaxt={'home':'active'}
    return render(request, 'myapp/home.html',contaxt)
def education(request):
    education={'education':'active'}
    return render(request,'myapp/education.html',education)
def skills(request):
    skills={'skills':'active'}
    return render(request,'myapp/skills.html',skills) 
def contact(request):
    if request.method=='POST': 
        name = request.POST['name']
        email = request.POST['email']
        title = request.POST['title']
        text = request.POST['text']
        con=contact1(name=name, email=email, title=title, text=text)
        con.save()
    
    return render(request,'myapp/contact.html')     
           
 