from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views import generic

from django.urls import reverse_lazy

from ajax.forms import CarForm

from ajax.models import Car


class IndexView(generic.ListView):
    model = Car
    queryset = Car.objects.all()
    template_name = 'ajax/index.html'
    context_object_name = 'cars'


# Cadastrar Carro
class CarFormView(generic.FormView):
    template_name = 'ajax/form.html'
    form_class = CarForm
    success_url = reverse_lazy('ajax:index')

    def form_valid(self, form, *args, **kwargs):
        form.save()
        return super(CarFormView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs,):
        return super(CarFormView).form_invalid(form, *args, **kwargs)


# Visualizar Carro
class CarDetailView(generic.DetailView):
    model = Car
    context_object_name = 'car'
    template_name = 'ajax/detail.html'


# Editar Carro
class CarUpdateView(generic.UpdateView):
    model = Car
    fields = '__all__'
    template_name = 'ajax/edit.html'
    success_url = reverse_lazy('ajax:index')


# Excluindo Carro
# class CarDeleteView(generic.DeleteView):
#     model = Car
#     template_name = 'ajax/delete.html'
#     success_url = reverse_lazy('ajax:index')

def delete(request, pk):
    car = Car.objects.get(pk=pk)
    car.delete()
    return redirect('ajax:index')