

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Libro
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import LibroForm

class HomeView(ListView):
    model = Libro
    template_name = 'books/home.html'
    context_object_name = 'libros'
    queryset = Libro.objects.order_by('-fecha_publicacion')[:3]

class AboutView(ListView):
    template_name = 'books/about.html'
    model = Libro

class LibroListView(ListView):
    model = Libro
    template_name = 'books/libro_list.html'
    context_object_name = 'libros'

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'books/libro_detail.html'

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'books/libro_form.html'
    success_url = reverse_lazy('libro-list')

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)


class LibroUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'books/libro_form.html'
    success_url = reverse_lazy('libro-list')

    def test_func(self):
        libro = self.get_object()
        return self.request.user == libro.creado_por


class LibroDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Libro
    template_name = 'books/libro_confirm_delete.html'
    success_url = reverse_lazy('libro-list')

    def test_func(self):
        libro = self.get_object()
        return self.request.user == libro.creado_por

