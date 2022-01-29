from django.urls import path
from .views import *
#from pages.views import AboutView, IndexView, ContactView

urlpatterns = [
    #path('', index, name="index"),
    #path('about/', about, name="about"),
    #path('contact/', contact, name="contact"),

    #path('teachers/', teachers, name="teachers"),

    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    #path(route, view, opt(kısayol ismi))
]
