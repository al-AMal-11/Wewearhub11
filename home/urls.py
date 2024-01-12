from django.urls import path , include
from . import views 

urlpatterns = [
    path('', views.home,name='home_page' ),
    path('about/', views.about,name='about_page' ),
    path('contact/', views.contact,name='contacts_page' ),
    # path('contacts/save', views.contact_form,name='contacts_save' ),
    #path('shore/', views.shote,name='shore_page' ),
    path('logout/', views.dologout,name='user_logout' ),
    

    
]
