from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="Index"),
    path('dash.html', views.dash, name = "dash"),
    path('login.html', views.login, name="login"),
    path('Profissional.html', views.profissional, name="Profissional"),
    path('cadatrogeral.html', views.cadastrogeral,name="cadastrogeral"),
    path('novopaciente.html', views.novopaciente, name= "novopaciente"),
    path('teste.html',views.teste,name="teste"),
    path('reteste.html',views.reteste,name="reteste"),
    path('medidasacusticas.html',views.medidasacusticas,name="medidasacusticas"),
    path('Audmetria.html',views.Audiometria,name="Audiometria"),
    path('PEATEintegridade.html',views.Peate,name="Peate"),
    path('Peatefrequenciaespecifica.html',views.PeateFrequencia,name="Peatefrequencia")
]

