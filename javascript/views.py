from django.urls import reverse_lazy
from django.views import generic

from django.urls import reverse_lazy

from javascript.forms import CalcImcForm


class IndexView(generic.FormView):
    template_name = 'javascript/index.html'
    form_class = CalcImcForm
    success_url = '/home/'

    def form_valid(self, form, *args, **kwargs):
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
        
