from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PersonForm
from django.utils import timezone
from .models import Person


class PersonListView(ListView):
    model = Person
    paginate_by = 100
    template_name = "myapp/person.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now
        return context


class PersonDetailView(DetailView):
    model = Person
    template_name = "myapp/person_detail.html"


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "myapp/person_create.html"
    success_url = "/"


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "myapp/person_update.html"
    success_url = "/"


class PersonDeleteView(DeleteView):
    model = Person
    template_name = "myapp/person_delete.html"
    success_url = "/"


"""
    'CreateView' - A view that displays a form for creating an object, redisplaying the form with validation errors (if there are any) and saving the object.
    'DeleteView' - A view that displays a confirmation page and deletes an existing object. 
    'DetailView' - A view for a specific object based on its ID
    'ListView' - Show a list/array of objects in a View
    'UpdateView' - A view that displays a form for updating an object, redisplaying the form with validation errors (if there are any) and saving the object.
"""