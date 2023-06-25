from django.urls import path
from . import views




urlpatterns = [
    path('',views.base,name='base'),
    path('home',views.home,name='home'),
    path('allprojects/',views.allprojects,name='allprojects'),
    path('allskills',views.allskills,name='allskills'),
    path('/<int:pk>',views.singleskill,name='singleskill'),
    path('<int:pk>',views.singleproject,name='singleproject'),
]
