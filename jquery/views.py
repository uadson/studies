from django.shortcuts import render

from django.views import generic


class IndexView(generic.TemplateView):
	template_name = 'jquery/index.html'


class ListView(generic.TemplateView):
	template_name = 'jquery/list.html'


class AjaxView(generic.TemplateView):
	template_name = 'jquery/ajax.html'
