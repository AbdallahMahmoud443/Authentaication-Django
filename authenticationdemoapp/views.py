
from django.http import HttpResponse
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import login,authenticate,update_session_auth_hash,logout
from authenticationdemoapp.forms import CreateStaffEmployeeForm, RoleForm, SignUpForm, UpdateStaffEmployeeForm, UserChangeProfileForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import Group,User,Permission
from django.contrib import messages
# Create your views here.


#* Create Custom decorator for validation role of user to access FBV for specific user
# Important for security issues
from functools import wraps
def user_has_role_or_superuser(roles): # user_has_role_or_superuser accept roles
    def decorator(view_func): # decorator accept (view function) is built in function
        @wraps(view_func)  #! Important step to wrapper view function
        @login_required # must user is loggedin
        def _wrapped_view(request,*args,**kwargs): # check function
            user_groups = request.user.groups.all().values_list('name',flat=True)
            if request.user.is_superuser or any(role in user_groups for role in roles):
               return view_func(request,*args,**kwargs)
            else:
                return redirect('HomePage')
        return _wrapped_view
    return decorator


def SignIn(request):
    #form = UserCreationForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Users add by default to (customer) group
            # Add User to the Customer's Group 
            customers_group,created = Group.objects.get_or_create(name='Customer') # create User
            print(created) # for explain => return Boolean
            user.groups.add(customers_group)  # add user in this group
            
            login(request,user) # make User Login After SignUp
            return redirect('HomePage')
    else:
       form = SignUpForm() 
    return render(request,'athenticationdemoapp/signin.html',{'form':form})


@login_required #  must user login to access this page 
def Home(request):
    return render(request,'athenticationdemoapp/home.html')

def Login(request):
    if request.method =='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            # get data from form 
           userName =  form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           # check user in database
           user = authenticate(request,username=userName,password=password) 
           if user is not None:
                login(request,user)
           return redirect('HomePage') 
    else:
        form = AuthenticationForm()
    return render(request,'athenticationdemoapp/login.html',{'form':form})


@login_required
def ChangePassword(request):
    if request.method == 'POST':
       form = PasswordChangeForm(request.user,request.POST)
       if form.is_valid():
          user = form.save()
          update_session_auth_hash(request,user) #! Important to Maintain the session
          return redirect('HomePage')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'athenticationdemoapp/changePassword.html',{'form':form})

@login_required
def ChangeProfile(request):
    if request.method == 'POST':
       form = UserChangeProfileForm(instance=request.user,data=request.POST)
       if form.is_valid():
          form.save()
          return redirect('HomePage')
    else:
        form = UserChangeProfileForm(instance=request.user)
    return render(request,'athenticationdemoapp/changeProfile.html',{'form':form})

@login_required
def DeleteAcount(request):
    if request.method == 'POST':
       request.user.delete()
       return redirect('LoginPage')
    return render(request,'athenticationdemoapp/deleteAccount.html') # for get request

def LogOut(request):
    logout(request)
    return redirect('LoginPage')
    

    
def is_superuser(user):
    return  user.is_superuser
    
@login_required
@user_passes_test(is_superuser) # check if user is admin or not Default decorator in django
def RolesList(request):
    roles = Group.objects.all()
    return render(request,'athenticationdemoapp/rolesList.html',{'roles':roles})

@login_required
@user_passes_test(is_superuser) # check if user is admin or not 
def CreateRole(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('RoleListPage')
    else:
        form = RoleForm()
        
    return render(request,'athenticationdemoapp/createRole.html',{'form':form})
    
@login_required
@user_passes_test(is_superuser) # check if user is admin or not 
def UpdateRole(request,role_id):
    role = Group.objects.get(pk=role_id)
    if request.method == "POST":
        form = RoleForm(request.POST,instance=role)
        if form.is_valid():
            form.save()
            return redirect('RoleListPage')
    else:
        form = RoleForm(instance=role)
        
    return render(request,'athenticationdemoapp/updateRole.html',{'form':form})

@login_required
@user_passes_test(is_superuser) # check if user is admin or not 
def DeleteRole(request,role_id):
    role = Group.objects.get(pk=role_id)
    group_uers = User.objects.filter(groups__name=role).count() # can't delete group which have users
    if group_uers == 0:
       role.delete()
       return redirect('RoleListPage')
    else:
        ErrorMessage ='This Role Cannot Be Deleted...as it has users'
        return HttpResponse(ErrorMessage)


@login_required
#@user_passes_test(is_superuser)
@user_has_role_or_superuser(['HR','HR Senior','HR Manager'])
def StaffList(request):
    staff_members = User.objects.filter(is_staff=True)
    user_groups = request.user.groups.all().values_list('name',flat=True)
    print(user_groups)
    return render(request,'athenticationdemoapp/staff_list.html',{'staff_members':staff_members,
                                                                  'user_groups':user_groups})

@login_required
#@user_passes_test(is_superuser)
@user_has_role_or_superuser(['HR'])
def CreateStaffEmployee(request):
    if request.method =="POST":
       form=CreateStaffEmployeeForm(request.POST)
       if form.is_valid():
           user= form.save(commit=False)
           user.is_staff = True
           user.save()
           # Add User To a group 
           roleName = form.cleaned_data.get('role')
           staffGroup,created = Group.objects.get_or_create(name=roleName)
           user.groups.add(staffGroup)
           return redirect('StaffListPage')
    else:
        form=CreateStaffEmployeeForm()
    return render(request,'athenticationdemoapp/createStaffEmployee.html',{'form':form})

@login_required
#@user_passes_test(is_superuser)
@user_has_role_or_superuser(['HR Senior'])
def UpdateStaffEmployee(request,user_id):
    # Get User
    user = User.objects.get(pk=user_id)
    if request.method =="POST":
       form = UpdateStaffEmployeeForm(request.POST,instance=user) 
       if form.is_valid():
            form.save()
             # Add User To a group 
            roleName = form.cleaned_data.get('role')
            staffGroup,created = Group.objects.get_or_create(name=roleName)
            user.groups.clear() #! clear old group important step
            user.groups.add(staffGroup)
            return redirect('StaffListPage')
    else:
        #Get Group Name
        groupName =user.groups.values_list('name',flat=True).first() # object (get name of group)
        # Get Group 
        staff_group = Group.objects.get(name=groupName) # select group
        form =UpdateStaffEmployeeForm(instance=user)
    return render(request,'athenticationdemoapp/updateStaffEmployee.html',{'form':form,'staff_group':staff_group})

@login_required
#@user_passes_test(is_superuser)
@user_has_role_or_superuser(['HR Manager'])
def DeleteStaffEmployee(request,user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('StaffListPage')


@login_required
@user_passes_test(is_superuser)
def AssociatePermissions(request,role_id):
    role = Group.objects.get(pk=role_id) # Get Role
    relevant_permissions = ['add_staff','update_staff','view_staff','delete_staff'] # All custome permission names
    if request.method == "POST":
        try:
       
            selected_permission_ids = request.POST.getlist('permissions') # Get All Ids
            selected_permissions = Permission.objects.filter(pk__in=selected_permission_ids) # Get Permission
            role.permissions.set(selected_permissions) # Add Permissions in specific Role
            messages.success(request,"Permission Associated Successfully")
            return redirect('RoleListPage')
        except Exception as e:
            print(f"Error Associating Permission:{e}")
            messages.success(request,"An Erro Occur while Associating permission,Please Try Again")
    else:
        all_permissions = Permission.objects.filter(codename__in=relevant_permissions) # get all custom permissions
        
    return render(request,'athenticationdemoapp/associatePermissions.html',{'role':role,'all_permissions':all_permissions})



        