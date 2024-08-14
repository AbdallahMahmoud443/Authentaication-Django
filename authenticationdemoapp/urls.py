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
    path('createlist/',views.CreateRole,name='CreateRolePage'),
]
