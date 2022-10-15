from django.urls import path
from . import views

urlpatterns = [
    path('restapidatapatient/',views.getdata,name="getdata"),
    path('restapionepatient/<int:id>',views.modify,name="modify"),
    path('restapidatadoctor/',views.getdatadoctor,name="getdata"),
    path('restapionedoctor/<int:id>',views.modifydoctor,name="modify")
]