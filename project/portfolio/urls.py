
from django.urls import path
from portfolio import views
urlpatterns = [path('',views.homee,name="homee"),
    path('home',views.home,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('blog',views.blogs,name="Blog"),
    path('internship',views.internship,name="internship"),
    
]
