from django.urls import path
from . import views




urlpatterns = [
    path('base',views.base,name='base'),
    path('',views.home,name='home'),
    path('allprojects/',views.allprojects,name='allprojects'),
    path('allskills',views.allskills,name='allskills'),
    path('/<int:pk>',views.singleproject,name='singleproject'),
    path('<int:pk>',views.singleskill,name='singleskill'),
    path('contactme',views.contactme,name='contactme'),
    path('enqsuc',views.enqsuccess,name='enqsuc'),
]
