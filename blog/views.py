from django.shortcuts import render
from django.views.generic.base import TemplateView


''' just uses for get request and  not request for form and action like delete ,edit,and more'''


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'shahram'
        # context['post'] = Post.Object.all()
        return context
