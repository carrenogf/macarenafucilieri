from django.urls import path
import core.views as homeViews



urlpatterns = [
    path('',homeViews.homeView,name='home'),
    path('servicios/',homeViews.serviciosView,name='servicios'),
    path('sobremi/',homeViews.aboutView,name="about"),
    path('contacto/',homeViews.contactoView,name="contacto")
]