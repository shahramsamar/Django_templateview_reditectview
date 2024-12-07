from django.urls import path
from blog import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name ='blog'

urlpatterns = [
    # path('',TemplateView.as_view(template_name='index.html', extra_context={'name': 'shahram'})),
    path('', views.IndexView.as_view(), name='cbv-index'),
    path('go-to-django', RedirectView.as_view(url='https://www.djangoproject.com/'), name='redirect-to-django'),
    path('go-to-index', RedirectView.as_view(pattern_name='blog:cbv-index'), name='redirect-to-index'),
    path('go-to-djangoo', views.RedirectToDjango.as_view(), name='redirect-to-django'),


    

]
