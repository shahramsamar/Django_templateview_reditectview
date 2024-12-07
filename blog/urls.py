from django.urls import path
from blog import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('',TemplateView.as_view(template_name='index.html', extra_context={'name': 'shahram'})),
    path('', views.IndexView.as_view(), name='cbv-index'),

]
