from django.urls import path
from web1 import views
from django.conf.urls.static import static
urlpatterns = [
    #path('', views.home),
    path('',views.homePageLanding, name='home'),
    path('/home', views.home, name='homepage'),
    path('/navbar', views.nav, name='navbar')
   
    
]
    