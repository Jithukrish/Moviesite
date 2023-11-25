from multiprocessing import AuthenticationError
from pyexpat.errors import messages
# from telnetlib import auth

from django.contrib.auth.models import User,auth
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
# def login(request):
#     return render(request,'login.html')
def login(request):
    if request.method=='POST':
    
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password  )

        if user is not None:
            auth.login(request , user)
            return redirect('/home')    
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/")
    else:
        return render(request,'login.html')

        

def logout(request):
    return render(request,'login.html')
def signup(request):
    if request.method=='POST':
    
        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']
        cpassword= request.POST['cpassword']


        user = User.objects.create_user(username = username , password = password , email = email)
        user.save()
        print('user created')
        # return redirect('/login')
        return HttpResponse('''<script>alert("registration successfully");window.location="/login"</script>''')
    return render(request,'signup.html')
def action(request):
    return render(request,'action.html')
def anime(request):
    return render(request,'anime.html')

def comedy(request):
    return render(request,'comedy.html')
def contactus(request):
    if request.method=='POST':
    
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname= request.POST['lastname']
        phone= request.POST['phone']
        subject=request.POOST['subject']
        message= request.POST['message']
        # message= request.POST['message']



        user = User.objects.create_user(firstname = firstname , lastname = lastname , email = email, phone=phone,subject=subject ,message=message)
        user.save()
        print('messege send')
        # return redirect('/login')
        return HttpResponse('''<script>alert(" successfully send your message");window.location="/contactus"</script>''')
    # return render(request,'signup.html')
    return render(request,'contactus.html')
def crime(request):
    return render(request,'crime.html')
def documentary(request):
    return render(request,'documentary.html')
def drama(request):
    return render(request,'drama.html')
def dummy(request):
    return render(request,'dummy.html')

def fantasy(request):
    return render(request,'fantasy.html')
def faq(request):
    return render(request,'faq.html')
def horror(request):
    return render(request,'horror.html')

def kids(request):
    return render(request,'kids.html')
def movie_min(request):
    return render(request,'movie-min.html')
def movies(request):
    return render(request,'movies.html')


def news(request):
    return render(request,'news.html')
def popular(request):
    return render(request,'popular.html')
def premium(request):
    return render(request,'premium.html')



def quiz(request):
    return render(request,'quiz.html')
def romance(request):
    return render(request,'romance.html')
#signup check
def suspense(request):
    return render(request,'suspense.html')
def tv(request):
    return render(request,'tv.html')
def war(request):
    return render(request,'war.html')
def web_series(request):
    return render(request,'web-series.html')
def logout(request):
    auth.logout(request)
    return redirect('/')










