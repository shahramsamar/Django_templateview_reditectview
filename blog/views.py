from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView


''' just uses for get request and  not request for form and action like delete ,edit,and more'''


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'shahram'
        # context['post'] = Post.Object.all()
        return context

''' just redirects to '''
class RedirectToDjango(RedirectView):
    url = 'https://www.djangoproject.com/'
    
    
    def get_redirect_url(self, *args, **kwargs):
        # post = get_object_or_404(*Post,pk=kwargs['pk'])
        return super().get_redirect_url(*args, **kwargs)