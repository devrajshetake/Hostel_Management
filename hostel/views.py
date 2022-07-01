from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from hostel.models import contactUs,VisitorDetails,studentDetails
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=studentDetails
    fields=['user','fname','lname','dob','mob','mob1','mob2','email1','email2','state','caste','nation','aadhar','pan','blood','allergy','guard','gaddress','gnumber','sphoto','aphoto','svaccine','certi']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        studentDetails=self.get_object()
        if self.request.user==studentDetails.fname:
            return True
        else:
            return False

def saveContactDetails(request):
    if request.method=='POST':
      name=  request.POST.get('name')
      email=  request.POST.get('email')
      message=  request.POST.get('message')
      contact=contactUs(name=name,email_id=email,message=message)
      contact.save()
    return render(request,'hostel/homepage.html')

def saveVisitorDetails(request):
    if request.method=='POST':
      fname=  request.POST.get('fname')
      lname=  request.POST.get('lname')
      email=  request.POST.get('email')
      room=  request.POST.get('room')
      phone=  request.POST.get('phone')
      intime=  request.POST.get('intime')
      outtime=  request.POST.get('outtime')
      relation=  request.POST.get('relation')
      visitor=VisitorDetails(fname=fname,email=email,lname=lname,room=room,phone=phone,intime=intime,outtime=outtime,relation=relation)
      visitor.save()
    return render(request,'hostel/visitor.html')

def login_user(request):
    if request.method=='POST':
        username=  request.POST.get('username')
        password=  request.POST.get('password')
        user=authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            # if user.is_active:
            return redirect('home-page')
        else:
            messages.success(request, "Wrong login credentials!")
            return redirect('login-page')
    
    return render(request,'hostel/login.html')

from django.contrib.auth import login, authenticate  # add to imports

# def login_page(request):
#     message = ''
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 message = f'Hello {user.username}! You have been logged in'
#             else:
#                 message = 'Login failed!'
#     return render(
#         request, 'authentication/login.html', context={'form': form, 'message': message})


# def profile(request):
#     return render(request,'hostel/viewprof.html')

def home(request):
    
    try: 
        std = studentDetails.objects.get(fname=request.user)
        if std.mob1:
            canAccessProfile = True
        else:
            canAccessProfile = False
    except:
        canAccessProfile = False
    info={'st': studentDetails.objects.all(),'user':User.first_name, 'canAccessProfile':canAccessProfile,'std':std}
    return render(request,'hostel/homepage.html',info)

def logout(request):
    return render(request,'hostel/logout.html')

def aboutUs(request):
    return render(request,'hostel/about_us.html')

def rules(request):
    return render(request,'hostel/rules.html')
    
def saveStudentDetails(request):
    if request.method =='POST':
        sname=request.POST.get('fname')
        pname=request.POST.get('lname')
        branch=request.POST.get('branch')
        year=request.POST.get('year')
        reg=request.POST.get('reg')
        roll=request.POST.get('roll')
        dob=request.POST.get('dob')
        address=request.POST.get('mob')
        snumber=request.POST.get('mob1')
        pnumber=request.POST.get('mob2')
        semail=request.POST.get('email1')
        pemail=request.POST.get('email2')
        hcity=request.POST.get('hometown')
        state=request.POST.get('state')
        caste=request.POST.get('caste')
        nation=request.POST.get('nation')
        aadhar=request.POST.get('aadhar')
        pan=request.POST.get('pan')
        blood=request.POST.get('blood')
        allergy=request.POST.get('allergy')
        guard=request.POST.get('guard')
        gaddress=request.POST.get('gaddress')
        gnumber=request.POST.get('gnumber')
        sphoto=request.POST.get('sphoto')
        
        aphoto=request.POST.get('aphoto')
        svaccine=request.POST.get('svaccine')
        certi=request.POST.get('certi')
        student=studentDetails(fname=sname,lname=pname,dob=dob,branch=branch,year=year,reg=reg,roll=roll,mob=address,mob1=snumber,mob2=pnumber,email1=semail,email2=pemail,hometown=hcity,state=state,caste=caste,nation=nation,aadhar=aadhar,pan=pan,blood=blood,allergy=allergy,guard=guard,gaddress=gaddress,gnumber=gnumber,sphoto=sphoto,aphoto=aphoto,svaccine=svaccine,certi=certi)
        student.save()
        if student is not None:
            messages.success(request, "Registration Successful!")
        else:
            messages.success(request, "Invalid data!")

    return render(request,'hostel/student_registration.html')
def visitor_registration(request):
    return render(request,'hostel/visitor.html')

def view_profile(request, user_pk):
    # user = User.objects.get(username = uname)
    profile = studentDetails.objects.get(pk = user_pk)
    context = {
        "profile":profile
    }
    return render(request,'hostel/viewprof.html', context)

def facilities(request):
    return render(request,'hostel/facilities.html')

def student_registration(request):
    return render(request,'hostel/student_registration.html')

@staff_member_required(redirect_field_name='login-page',  login_url='login-page')
def student_details(request):
    s1={'student':studentDetails.objects.all()}
    return render(request,'users/table.html',s1)

@staff_member_required(redirect_field_name='login-page',  login_url='login-page')
def add_student(request):
    if request.method == "POST":
        uname = request.POST['uname1']
        pass1 = request.POST['pass']
        name = request.POST['name1'].split()
        try:
            user = User.objects.create_user(username=uname, password = pass1)
            user.first_name = name[0]
            user.save()
            prof = studentDetails(fname = user)
            prof.fname = name[0]
            prof.lname = name[1]
            prof.save()
            messages.success(request, "Student added successfully!")
        except:
            messages.error(request, "Username already exists!!")
        
    return render(request,'hostel/add_student.html')

# <<<<<<< HEAD

# =======
# <<<<<<< HEAD
# >>>>>>> d4208c7395e1a41fcf3cbbd951381dcadc4e2a0d
def profile(request):
    # try: 
    std = studentDetails.objects.get(user = request.user)
    #     if std.mob1:
    #         canAccessProfile = True
    #     else:
    #         canAccessProfile = False
    # except:
    #     canAccessProfile = False
    info={
        'std':std
        }
    
    return render(request,'hostel/profile.html',info)
def profile(request):
    return render(request,'hostel/profile.html')

def profile(request):
    return render(request,'hostel/profile.html')     
