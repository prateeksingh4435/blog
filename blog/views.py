from django.shortcuts import HttpResponse,render,redirect
from Blogging.models import Blog,signupdata,WriteBlockchainBlog,WriteTechnologyBlog,WriteRoboticsBlog,WriteWebBlog ,BlogByUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def blog(request):
    if request.user.is_authenticated:
        return render(request,'index2.html')
    else:
        return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        member = request.POST.get('checkbox')
        select = request.POST.get('select')
        desc = request.POST.get('textarea')
        alldata = Blog(firstname = firstname , lastname =lastname,email=email,member=member,query=select,concern=desc)
        messages.success(request,'We will review it and get bact to you soon ')
        alldata.save()


    return render(request,'contact.html',)

def technology(request):
    if request.user.is_authenticated:
        blog = WriteTechnologyBlog.objects.all()

        return render(request,'tech.html',{'blog':blog})
    else:
        messages.error(request,'Login to read latest blog ')
        return redirect('blog')


def designing(request):
    if request.user.is_authenticated:
        blog = WriteWebBlog.objects.all()
        
        return render(request,'web.html',{'blog':blog})
    else:
        messages.error(request, 'Login to read latest blog ')

        return redirect('blog')
def blockchain(request):
    if request.user.is_authenticated:
        blog = WriteBlockchainBlog.objects.all()
        
        return render(request,'block.html',{'blog':blog})
    else:
        messages.error(request, 'Login to read latest blog ')
        return redirect('blog')

def robotics(request):
    if request.user.is_authenticated:
        blog = WriteRoboticsBlog.objects.all()
        
        return render(request,'robo.html',{'blog':blog})
    else:
        messages.error(request, 'Login to read latest blog ')
        return redirect('blog')
def signup(request):
    if request.method=="POST":
        firstname  = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username  = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirmpassword')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already used")
                return redirect('signup')
            user = signupdata(firstname = firstname ,lastname = lastname , email= email,username = username,password1=password1,password2 =password2)
            user.save()
            my_user = User.objects.create_user(username=username, password=password1)
            my_user.first_name = firstname
            my_user.last_name = lastname
            my_user.email = email

            my_user.save()
            messages.success(request, 'Sign-up successful')
            return redirect('loginpage')
        else:
            messages.error(request,'Password and Confirm Password Not Match')


    return render(request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Login-successfully')
            return redirect('authenticationpage')

        else:
            messages.error(request,'Invalid username and password')

    return render(request,'login.html')

def authenticationpage(request):
    if request.user.is_authenticated:
        return render(request,'index2.html')


def logoutpage(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return redirect('blog')


def writeablog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
             
            category = request.POST.get('select')
            topic = request.POST.get('topic')
            blog = request.POST.get('writeablog')
            
            a = BlogByUser(name = name , email = email , category = category , topic = topic , blog = blog)
            a.save()
            messages.success(request, "We will review your blog, and if we think it's good, we will post it on our website." )
            return redirect('writeablog')

            
        return render(request,'writeablog.html')
    else:
        
        messages.error(request,'Login to Write a Blog ')
        return render(request,'index.html')
