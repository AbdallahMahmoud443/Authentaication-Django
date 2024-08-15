from django.urls import path
from . import views

urlpatterns = [
    path('signin/',views.SignIn,name='SignInPage'),
    path('home/',views.Home,name='HomePage'),
    path('login/',views.Login,name='LoginPage'),
    path('changepassword/',views.ChangePassword,name='ChangePasswordPage'),
    path('changeprofile/',views.ChangeProfile,name='ChangeProfilePage'),
    path('deleteuser/',views.DeleteAcount,name='DeleteAcountPage'),
    path('logout/',views.LogOut,name='LogOutPage'),
    
    path('roleslist/',views.RolesList,name='RoleListPage'),
    path('createrole/',views.CreateRole,name='CreateRolePage'),
    path('updaterole/<int:role_id>/',views.UpdateRole,name='UpdateRolePage'),
    path('deleterole/<int:role_id>/',views.DeleteRole,name='DeleteRolePage'),
    
    path('stafflist/',views.StaffList,name='StaffListPage'),
    path('createemployee/',views.CreateStaffEmployee,name='CreateStaffEmployeePage'),
    path('updatecreareemployee/<int:user_id>/',views.UpdateStaffEmployee,name='UpdateStaffEmployeePage'),
    path('deletecreareemployee/<int:user_id>/',views.DeleteStaffEmployee,name='DeleteStaffEmployeePage'),
    
]
